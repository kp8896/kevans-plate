# CLAUDE.md — project memory for `kevans-plate`

Orientation for any Claude session opened on this repo (including Toby's).

## What this repo holds
- **`curriculum/`** — Kevan's **self-directed university**: a structured, mostly-free
  certificate curriculum (built 2026-06-07). **This is the active project.**
- `index.html`, `README.md` — the original "Kevan's Plate" dashboard (Microsoft
  tasks / Donna integration). Not part of the curriculum work.

## Start here (read in this order)
1. `curriculum/BUILD-LOG.md` — **what we built and why** (the reference point).
2. `curriculum/30-progress-ledger.md` — **active state**: chosen plan, pace, what's
   done, what's next. *This is the living memory — update it as study happens.*
3. `curriculum/RUN-A-SESSION.md` — how to **fire Toby** for a classroom session.
4. `curriculum/README.md` — full folder index.

## Active state (as of 2026-06-07)
- **Plan:** Undergrad **Plan A — "Focused," AI-focused config** (Google PM swapped
  for Google AI Essentials + Prompting). ~120–150 hrs; began 2026-06-07; **10 h/week
  committed floor** → target finish ~late Sept 2026 (earlier if he pushes past 10).
- **First up:** Apple Manufacturing Academy → "Communications & Presentation Skills"
  (Day 1 of `curriculum/apple-academy/_study-schedule.md`). Kevan starts from ZERO.
- **Calibration checkpoint:** ~Jun 25 (after Apple Badge I) → decide B/C from real
  pace data.

## The cast
- **Kevan** = student · **Toby** = tutor (runs sessions) · **Same** = inbox triage ·
  **Donna** = assistant/orchestrator · **Claude** = architect/registrar.

## Conventions (important)
- **The repo is the memory.** Claude here runs in a cloud clone, not on Kevan's
  Macs — so commit + push everything; Macs sync via `git pull`.
- **IP rule:** for Apple/MSU (and similar) course materials, store **structure +
  original synthesized notes only — never verbatim course content.**
- **Source of truth for "what to study next"** = `30-progress-ledger.md` → Active
  selection. Ignore unrelated saved items (e.g., CS221/CS229/MIT robotics) unless
  they're in the active plan.
- **Branch:** work on `claude/college-curriculum-plan-SCajr` unless told otherwise.

## Toby integration (live as of 2026-06-07)
- **Toby runs classroom sessions** and pulls study guides from this repo.
- **Detailed session transcripts** live in Kevan's Mac workspace at
  `10-projects/learning-curriculum/sessions/<date>-<course>.md` (PARA second-brain,
  not this repo).
- **Ledger ownership:** Toby writes the one-line entry to
  `curriculum/30-progress-ledger.md` at session end (after Kevan confirms). **Claude
  should NOT write the ledger during active study** — avoid merge collisions. Claude
  owns curriculum *structure* (plans, guides, catalog, build log); Toby owns *session
  logging*. Whoever writes the ledger should commit + push so it stays durable.
