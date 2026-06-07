# How to Fire Toby — Run a Classroom Session

The one-page protocol for starting a study session. Hand the **kickoff prompt** to
Donna/Toby; Toby runs the **session script**; you log the result.

> **Which course is next?** Always check `30-progress-ledger.md` → *Active selection*
> → *Plan A sequence*. Right now that's the **Apple major, in schedule order**
> (`apple-academy/_study-schedule.md`). **Ignore unrelated saved items** (CS221,
> CS229, MIT robotics, etc.) — they are *not* in the active plan.

---

## ▶️ Kickoff prompt (copy-paste) — Session 1

```
Toby, start my first classroom session.

CONTEXT (read these first):
- Repo: kevans-plate, branch claude/college-curriculum-plan-SCajr, folder curriculum/
- Your role + session format: curriculum/00-framework.md
- My active plan: curriculum/30-progress-ledger.md → Undergrad Plan A (AI-focused)
- Teaching script for today: curriculum/apple-academy/communications-and-presentation-skills.md

TODAY'S COURSE (Day 1 of apple-academy/_study-schedule.md):
- Apple Manufacturing Academy → Course 1: "Communications & Presentation Skills"
- I am starting from ZERO. Award = pass 2 module quizzes (≥70%) + survey, done in D2L.
- Do NOT start any other saved course — only this one.

RUN THE SESSION (per 00-framework.md daily loop):
1. Orient me in 3-4 sentences: what this course is + the award requirement.
2. Pre-teach Module 2 "Prepare": give me the mental model BEFORE I read.
3. Walk me through it Socratically, one concept at a time; check I actually get it.
4. Give me the active-recall quiz from the study guide; I answer; you score it and
   flag anything I rate ≤3/5 confidence as "shaky."
5. Tell me exactly which D2L lessons to complete next, then end with:
   - a one-line ledger entry to paste into curriculum/30-progress-ledger.md
   - my confidence rating + what's shaky for spaced review.

Begin.
```

**If Toby can't read the repo:** paste the contents of
`apple-academy/communications-and-presentation-skills.md` and `00-framework.md`
into the prompt, then give the same instructions.

---

## 🔇 Student channel = teaching only (rule)
Toby's chat with Kevan carries **teaching turns only**: the lesson, Socratic
questions, the quiz, feedback, D2L instructions, and the proposed ledger entry at
the end. **No operator telemetry in the student channel** — session state,
pipeline/path-B status, `/tutor/*` calls, "self-improvement review," and
memory-update notices stay in Toby's internal logs. One teaching turn, then wait
for Kevan's reply.

## 🧑‍🏫 Session script (what Toby does every time)
From `00-framework.md` §2, the daily loop:
1. **Warm-up** — 3 recall questions from last session (skip on session 1).
2. **Teach** — frame today's concept before the material.
3. **Learn** — guide through the lessons, one concept at a time.
4. **Do** — a small artifact (explain-it-back / worked example / the "Your turn").
5. **Lock-in** — active-recall quiz from the study guide; confidence 1–5; log shaky items.

## ✅ After the session — log it
Append to `curriculum/30-progress-ledger.md` (Module log), e.g.:
```
2026-06-15 | Apple: Communications & Presentation Skills | IN-PROGRESS | cert — | 4/5 |
            note: Purpose→Audience→Narrative→Recommendation before slides.
```
Mark **DONE** only after you pass the 2 quizzes + survey in D2L.

---

## 🔁 Next sessions
Same kickoff prompt, change two lines:
- **TODAY'S COURSE** → the next item in the Plan A sequence / Apple schedule.
- **Teaching script** → that course's guide in `apple-academy/` (or the relevant
  track folder). After Apple Badge I, the sequence continues: Anthropic AI Fluency
  → IBM AI Fundamentals → Microsoft AI-900 → Google AI Essentials+Prompting →
  capstone (see `30-progress-ledger.md`).
