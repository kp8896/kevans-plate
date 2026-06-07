#!/usr/bin/env python3
"""Append a session entry to the curriculum progress ledger — and (optionally)
pull/commit/push it — in ONE command, so Toby can durably record a study session
without any hand-editing or multi-step git.

This is the mechanism behind the kevans-plate CLAUDE.md rule:
"Toby writes the one-line entry to curriculum/30-progress-ledger.md at session end
... and commits + push so it stays durable."

Toby (the @TobyZieglerBot Hermes agent) runs on Kevan's Mac and has shell access +
the repo's SSH push auth, so he calls this directly at session end. Pure-stdlib,
no deps. Plain invocation (no pipe-to-shell, no python -c) so it doesn't trip the
Hermes approval gate.

USAGE
  # just edit the file (safe, no git) — used in testing:
  ledger-append.py "2026-06-07 | Apple Academy / C1 | IN-PROGRESS | cert — | confidence 2/5 | note: ..."

  # the real session-end call Toby makes — edit + pull + commit + push:
  ledger-append.py --push \
      "2026-06-07 | Apple Academy / C1 | IN-PROGRESS | cert — | confidence 2/5 | note: ..." \
      --shaky "Warmth vs. competence axes|0/5|Apple C1 2026-06-07" \
      --shaky "Slide discipline|1/5|Apple C1 2026-06-07"

  # point at a different ledger (testing):
  ledger-append.py --ledger /tmp/copy.md --no-git "..."

EXIT CODES
  0 ok (entry inserted, or already present = idempotent no-op)
  2 ledger file or its "## Module log" section not found
  3 git step failed (edit still succeeded and is on disk)
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

# Default ledger: ../30-progress-ledger.md relative to this script (curriculum/scripts/).
DEFAULT_LEDGER = (Path(__file__).resolve().parent.parent / "30-progress-ledger.md")

MODULE_LOG_HEADING = "## Module log"
SHAKY_HEADING = "## Shaky / spaced-review queue"
NONE_YET = "- [ ] _none yet_"


def _find_module_log_insert_line(lines: list[str]) -> int:
    """Return the line index AFTER the opening ``` fence under '## Module log'.

    The ledger keeps entries newest-at-top inside a fenced block:

        ## Module log (newest at top)

        ```
        <newest entry goes here>
        <older entries...>
        ```
    """
    in_section = False
    for i, line in enumerate(lines):
        if line.startswith(MODULE_LOG_HEADING):
            in_section = True
            continue
        if in_section and line.rstrip() == "```":
            return i + 1  # insert right after the opening fence = newest at top
    return -1


def insert_module_entry(lines: list[str], entry: str) -> tuple[list[str], bool]:
    """Insert `entry` as the newest Module-log line. Idempotent on exact match."""
    entry = entry.strip()
    if any(line.strip() == entry for line in lines):
        return lines, False  # already present — no-op (safe on push-retry)

    idx = _find_module_log_insert_line(lines)
    if idx < 0:
        raise LookupError(f"'{MODULE_LOG_HEADING}' fenced block not found in ledger")

    # entry line + a trailing blank so consecutive entries stay readable
    out = lines[:idx] + [entry + "\n", "\n"] + lines[idx:]
    return out, True


def add_shaky_items(lines: list[str], shaky: list[str]) -> tuple[list[str], int]:
    """Add '<text>|<conf>|<source>' items under the Shaky/spaced-review queue.

    Replaces the '_none yet_' placeholder when present; otherwise inserts after
    the section's intro line. Idempotent per-item on the rendered bullet.
    """
    if not shaky:
        return lines, 0

    bullets = []
    for raw in shaky:
        parts = [p.strip() for p in raw.split("|")]
        text = parts[0] if parts else raw.strip()
        conf = parts[1] if len(parts) > 1 and parts[1] else None
        src = parts[2] if len(parts) > 2 and parts[2] else None
        tail = ""
        if conf:
            tail += f" — conf {conf}"
        if src:
            tail += f" · {src}"
        bullets.append(f"- [ ] {text}{tail}")

    existing = {line.strip() for line in lines}
    bullets = [b for b in bullets if b not in existing]  # idempotent
    if not bullets:
        return lines, 0

    # Find the Shaky section bounds.
    start = next((i for i, l in enumerate(lines) if l.startswith(SHAKY_HEADING)), -1)
    if start < 0:
        return lines, 0  # no shaky section — silently skip (entry still recorded)
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))

    block = lines[start:end]
    none_idx = next((i for i, l in enumerate(block) if l.strip() == NONE_YET), -1)
    rendered = [b + "\n" for b in bullets]
    if none_idx >= 0:
        block = block[:none_idx] + rendered + block[none_idx + 1:]
    else:
        # insert after the first non-heading, non-blank intro line
        ins = 1
        for i in range(1, len(block)):
            if block[i].strip() and not block[i].startswith("#"):
                ins = i + 1
                break
        block = block[:ins] + ["\n"] + rendered + block[ins:]

    return lines[:start] + block + lines[end:], len(bullets)


def _git(args: list[str], cwd: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-C", str(cwd), *args],
        capture_output=True, text=True,
    )


def git_pull(repo: Path) -> bool:
    r = _git(["pull", "--rebase", "--autostash"], repo)
    if r.returncode != 0:
        sys.stderr.write(f"git pull failed:\n{r.stderr}\n")
        return False
    return True


def git_commit_push(repo: Path, ledger: Path, message: str) -> bool:
    add = _git(["add", str(ledger)], repo)
    if add.returncode != 0:
        sys.stderr.write(f"git add failed:\n{add.stderr}\n")
        return False
    # commit only if there's actually a staged change
    diff = _git(["diff", "--cached", "--quiet"], repo)
    if diff.returncode == 0:
        print("nothing staged (idempotent no-op) — not committing")
        return True
    commit = _git(["commit", "-m", message], repo)
    if commit.returncode != 0:
        sys.stderr.write(f"git commit failed:\n{commit.stderr}\n")
        return False
    push = _git(["push"], repo)
    if push.returncode != 0:
        # one rebase-and-retry for the concurrent-writer (cloud surface) case
        sys.stderr.write("push rejected — pulling --rebase and retrying once\n")
        if not git_pull(repo):
            return False
        push = _git(["push"], repo)
        if push.returncode != 0:
            sys.stderr.write(f"git push failed after retry:\n{push.stderr}\n")
            return False
    sha = _git(["rev-parse", "--short", "HEAD"], repo).stdout.strip()
    print(f"pushed: {sha}")
    return True


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Append a session entry to the curriculum ledger.")
    ap.add_argument("entry", help="the one-line ledger entry (the full pipe-delimited line)")
    ap.add_argument("--shaky", action="append", default=[],
                    help="repeatable: 'text|conf|source' shaky/spaced-review item")
    ap.add_argument("--ledger", default=str(DEFAULT_LEDGER), help="path to the ledger file")
    ap.add_argument("--push", action="store_true",
                    help="pull --rebase, then commit + push the change (the real session-end call)")
    ap.add_argument("--no-git", action="store_true", help="edit the file only; never touch git")
    ap.add_argument("--message", default=None, help="override the git commit message")
    args = ap.parse_args(argv)

    ledger = Path(args.ledger).resolve()
    if not ledger.is_file():
        sys.stderr.write(f"ledger not found: {ledger}\n")
        return 2
    repo = ledger.parent
    while repo != repo.parent and not (repo / ".git").exists():
        repo = repo.parent

    # pull BEFORE editing so we layer onto the latest (cloud surface may have pushed)
    if args.push and not args.no_git:
        if not (repo / ".git").exists():
            sys.stderr.write(f"no git repo found above {ledger}\n")
            return 3
        if not git_pull(repo):
            return 3

    lines = ledger.read_text(encoding="utf-8").splitlines(keepends=True)
    try:
        lines, entry_added = insert_module_entry(lines, args.entry)
    except LookupError as e:
        sys.stderr.write(f"{e}\n")
        return 2
    lines, shaky_added = add_shaky_items(lines, args.shaky)

    if not entry_added and shaky_added == 0:
        print("entry + shaky items already present — nothing to do")
        return 0

    ledger.write_text("".join(lines), encoding="utf-8")
    print(f"ledger updated: entry_added={entry_added} shaky_added={shaky_added} -> {ledger}")

    if args.push and not args.no_git:
        module = args.entry.split("|")[1].strip() if "|" in args.entry else "session"
        msg = args.message or f"Ledger: {module} (Toby session, auto)"
        if not git_commit_push(repo, ledger, msg):
            return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
