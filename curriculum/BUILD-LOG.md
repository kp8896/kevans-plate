# Curriculum Build Log

A dated record of what we built and **why** — so when you forget the details, this
is the reference point. (The `30-progress-ledger.md` tracks ongoing study; this
file records the design decisions.)

---

## 2026-06-07 — Initial build session

**Goal:** turn a pile of saved links + named priority brands into a structured,
mostly-free "college" curriculum with certificates, a graduation timeline, and a
repeatable way to actually study it. Plus a graduate ("masters") track in
robotics + ML.

**Delivery constraint:** this work was done by Claude in a cloud container (a fresh
clone of `kevans-plate`), **not** on Kevan's Macs — no SSH/local access. So the
**repo on GitHub is the shared memory**; Macs sync via `git pull`.

### What we built (in order)
1. **Framework + plans** (`curriculum/`): operating model (`00-framework.md`),
   vetted multi-brand catalog (`01-course-catalog.md`), **3 undergrad plans**
   (A focused / B balanced / C broad) and **3 grad robotics+ML plans**, plus the
   living `30-progress-ledger.md`.
2. **Apple major, fully mapped** (`apple-academy/`): the real program is "Smart
   Manufacturing for American Business" (MSU D2L), **4 Units → 11 courses**, stacked
   **Badges I/II/III (5/10/15 courses)**. Wrote **Toby study guides for all 11**, a
   day-by-day **study schedule**, and a tracker. **IP rule honored:** structure +
   original notes only, never verbatim Apple/MSU materials. Confirmed real workload
   ≈ **3–4 hrs/course** (~36 hrs total; Badges I & II in ~2 weeks).
3. **Anthropic track** (`anthropic/_path.md`): 4 tiers (Fluency → Practitioner →
   Builder → **CCA-F** proctored credential).
4. **Agentic AI track** (`agentic-ai/_path.md`): emerged from inbox finds —
   Anthropic Builder → HF MCP → Microsoft MCP → IBM RAG selectives → CCA-F.
5. **Session runner** (`RUN-A-SESSION.md`): copy-paste prompt to fire **Toby** +
   the session script.

### Key decisions (the "why")
- **Anchor = Apple Manufacturing Academy** (enrolled, free, MSU badges). Every plan
  starts here.
- **Anthropic is paramount** — AI Fluency in every plan; CCA-F as the credential.
- **Certificates + brand names lead; redundancy removed** (one course per concept —
  see the dedup map in `00-framework.md`).
- **"Understand the code, don't become a coder"** — a deliberate technical-literacy
  thread; coding-heavy engineering tracks kept off the undergrad critical path.
- **Inbox triaged (7 links, all cleared):** added Harvard CS50 AI, HF MCP, IBM
  RAG/Agentic, Microsoft MCP, MIT ML reference texts, Stanford CS230; deduped MIT
  6.S191. These surfaced the **Agentic AI** track.
- **CHOSEN: Undergrad Plan A — "Focused,"** then **reconfigured AI-focused**:
  swapped Google Project Management (~140 hrs) → **Google AI Essentials + Prompting**
  (~20 hrs). Plan A is now **~120–150 hrs**.
- **Calibration approach:** the Apple block (Week 1–2) is the velocity gauge; decide
  whether to roll into B/C **from real logged data**, not optimism.

### ⭐ Path A outline (the ACTIVE plan)
- **Config:** AI-focused. **Start:** Mon 2026-06-15. **Workload:** ~120–150 hrs.
- **Target finish:** ~early Aug 2026 (3 hr/day) · range ~late Jul → ~Sep 2026
  (4→2 hr/day) · ~Nov–Dec 2026 at 1 hr/day.
- **Cost:** ~$0–$100 (financial aid + free MS exam voucher).
- **6 credentials:** Anthropic AI Fluency · IBM AI Fundamentals badge · Apple/MSU
  Smart Manufacturing **Badge I** · Microsoft **AI-900/AI-901** · Google **AI
  Essentials** · Google **Prompting Essentials**.
- **Sequence:**
  1. **Apple Badge I** (5 courses, ~17 hrs) — *Week 1–2, scheduled, = calibration*
  2. Anthropic AI Fluency (~5 hrs)
  3. IBM SkillsBuild AI Fundamentals (~15 hrs)
  4. Microsoft AI-900/AI-901 (~20 hrs)
  5. Google AI Essentials + Prompting (~20 hrs)
  6. Capstone — Operations Improvement brief (~10 hrs)
- **Then:** decide B/C or go to grad — from the calibration numbers.
- **Add-backs parked:** Google PM (ACE credit) and Google Data Analytics.

### The cast
- **Kevan** — student (2–4 hr/day, starting from zero).
- **Toby** — tutor; runs classroom sessions (see `RUN-A-SESSION.md`).
- **Same** — triage (inbox → catalog).
- **Donna** — assistant/orchestrator (hands sessions to Toby).
- **Claude** — architect/registrar (built this; maintains the roadmap + memory).

### Status at end of session
- All tracks built and pushed to branch `claude/college-curriculum-plan-SCajr`.
- Plan A committed + configured. First session (Apple Communications) being fired
  via Donna → Toby.
- **Next milestone:** calibration checkpoint ~2026-06-25 (after Apple Badge I).

---

## 2026-06-08 — First session run; ledger now auto-recorded; pace set

**Context:** Session 1 happened (Apple Academy Course 1, Communications & Presentation
Skills).

### What changed
1. **Session entries are now recorded automatically.** Closing a study session no longer
   requires hand-editing this ledger — the committed helper
   `curriculum/scripts/ledger-append.py --push` inserts the entry (newest-at-top), adds
   any shaky-review items, and commits + pushes (idempotent, one retry on a concurrent
   push). The tutor (Toby) runs it at session end; no manual git.
   *(The tutor is FabACab-rooted infrastructure — the agent-side capability + config
   detail is recorded in FabACab/Donna governance, not in this public repo.)*
2. **Session 1 recorded:** Apple C1 IN-PROGRESS, confidence 2/5, D2L Sections 1–3
   assigned, 4 shaky items seeded into the spaced-review queue.
3. **Pace committed: 10 h/week** — Kevan's "first goal" (push for more). Forecast
   recomputed off ~120–150 hrs → **~late Sept 2026 floor** (~mid-Aug at 15 h/wk).
   Supersedes the 2026-06-07 "3 hr/day → early Aug" target above.

### Canonical-location note (important)
This repo (`kevans-plate/curriculum/`) is the **single source of truth** — Apple-first
sequence, 10 h/wk. A parallel 2026-06-07 draft (Anthropic-first) elsewhere is
**superseded**; this repo is what the tutor reads and writes.

### Status at end of session
- All changes committed + pushed to `claude/college-curriculum-plan-SCajr`.
- **Next milestone:** calibration checkpoint ~2026-06-25 (after Apple Badge I).
