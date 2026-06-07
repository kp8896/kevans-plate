# 00 — The Framework: HOW this works

This is the operating system for the whole program. Courses are the *content*;
this file is the *machine* that turns content into a credential and into durable
understanding.

---

## 1. The operating model (who does what)

```
        ┌─────────────────────────────────────────────────────────┐
        │  CLAUDE (registrar / architect)                          │
        │  • owns & maintains the roadmap (these files)            │
        │  • tracks progress, adjusts pace & scope                 │
        │  • ingests what you learn into MEMORY (30-progress-ledger)│
        └───────────────┬─────────────────────────────────────────┘
                        │ roadmap + "what's next"
                        ▼
   SAME ──────►  ┌──────────────┐  teaches   ┌──────────────┐
   triage:       │   TOBY       │ ─────────► │   YOU        │
   sorts inbox   │  (tutor)     │            │  (student)   │
   links into    │  explains,   │ ◄───────── │  2–4 hrs/day │
   the catalog   │  quizzes,    │  questions │  learn/build │
                 │  Socratic    │            │  sit exams   │
                 └──────────────┘            └──────┬───────┘
                                                    │ "I finished X / I'm stuck on Y"
                                                    ▼
                                          back to CLAUDE → updates MEMORY
```

**The loop in one sentence:** *Claude routes → Toby teaches → you learn & build →
you report → Claude writes it to memory and re-plans.*

### Role contracts

- **Claude (me).** I keep `10`–`22` accurate, recalc graduation dates when your
  pace changes, and after each module I append to `30-progress-ledger.md`
  (what you covered, what stuck, what's shaky, certs earned). When you re-run me,
  I read the ledger first so I "remember" where you are. **This ledger is the
  memory** — because I can't reach your Macs, memory lives in the repo and
  travels by `git pull`.
- **Toby (tutor).** For each topic, Toby: (1) pre-teaches the mental model before
  you watch the lecture, (2) answers your questions in plain language, (3) runs a
  10-minute **active-recall quiz** at the end, (4) flags what you didn't actually
  understand so it goes into the ledger as "shaky." Toby teaches *for
  understanding*, not to make you a coder.
- **Same (triage).** Takes raw `00-inbox` links, dedupes against
  `01-course-catalog.md`, tags each (brand / topic / cert? / hours / level), and
  either slots it into a plan or files it under "electives / someday."
- **You.** Show up 2–4 hrs/day. Do the active recall. Sit the exams. Tell the
  system when something clicks or doesn't — that's what keeps the plan honest.

---

## 2. Cadence

### Daily session (2–4 hrs)
A repeatable shape, not a grind:

1. **Warm-up (5–10 min)** — Toby asks 3 recall questions from last session.
2. **Teach (10–15 min)** — Toby frames today's concept *before* the video.
3. **Learn (60–150 min)** — lectures / labs / reading. One concept at a time.
4. **Do (20–40 min)** — a small artifact: notes in your words, a worked example,
   a sentence-level "explain it back."
5. **Lock-in (10 min)** — Toby quizzes; you rate confidence 1–5. Anything ≤3
   gets logged as "shaky" for spaced review.

### Weekly review (≈30 min, with Claude)
- Update the ledger: modules done, hours logged, confidence trend.
- Re-forecast the graduation date from *actual* hours, not planned.
- Pull one "shaky" item forward for a spaced-repetition pass.

### Monthly milestone
- One **deliverable** (a brief, a mini-project, or a sat exam) that proves the
  month wasn't just video-watching.
- A 15-minute "what's working / what's dragging" with Claude → adjust scope.

### Certificate checkpoints
Treat each certificate/badge as a term-end exam. Don't drift between programs;
finish one, bank the credential, then start the next.

---

## 3. Certificate cost tactics (how to pay near-$0)

The brands differ a lot in how "free" they are. Use the right tactic per platform:

| Platform | Free path | When you pay | Tactic |
|---|---|---|---|
| **Apple Manufacturing Academy (MSU)** | Fully free; MSU Credly badges | never | You're enrolled — just complete modules. |
| **Anthropic Academy** | Free, completion certs | never | Take freely. |
| **Anthropic CCA-F exam** | Free for Claude Partner Network employees | $99/attempt otherwise | Check partner-network eligibility before paying. |
| **Microsoft Learn** | Training 100% free | Exam $99 (Fundamentals) / $165 (Associate) | Get a **free exam voucher** at a Microsoft *Virtual Training Day*. |
| **Coursera** (Google/IBM/Stanford/DeepLearning.AI/Northwestern) | Audit = videos/readings free; **certs need ~$49/mo** | per cert | **Apply for Financial Aid** (≈100%, ~15-day wait) *or* sprint to finish a cert in **one** subscription month. Coursera Plus (~$399/yr) wins only if doing many at once. |
| **edX** (ETH Zürich, MITx) | Audit free | Verified cert per-course fee | Audit for knowledge; pay only when you want the paper. |
| **IBM SkillsBuild** | Free badges | never | Take freely. |
| **Google Cloud Skills / Kaggle / fast.ai / Hugging Face / MIT 6.S191 / Stanford CS open courses / ROS docs / NVIDIA Isaac** | Free | mostly never (some NVIDIA DLI assessed courses paid) | Take freely; these carry the "free + real" load. |

**Sprint rule:** Coursera bills monthly, so **batch** a certificate into a single
intense month (2–4 hr/day finishes most 6-month-paced certs in 3–5 weeks) =
one $49 charge instead of six. Financial aid removes even that.

**⚠️ Time-sensitive (verify before committing):**
- Microsoft **AI-900 retires Jun 30, 2026** → successor **AI-901**. Sit AI-900
  now or target AI-901.
- Microsoft **AI-102 also retires Jun 30, 2026** — check the successor.

---

## 4. The redundancy-removal map (one course per concept)

The biggest risk with these brands is paying for the same idea five times. Decisions:

| Concept | **Kept (the one you do)** | Dropped / demoted (redundant) |
|---|---|---|
| **AI literacy / fluency** | **Anthropic — AI Fluency: Framework & Foundations** (free cert, your top brand) | Google AI Essentials, Microsoft+LinkedIn "Career Essentials in GenAI" → *optional reinforcement only* |
| **No-code "how AI works" concepts** | **IBM SkillsBuild — AI Fundamentals** (free badge, zero code) | duplicative intro-AI MOOCs |
| **ML foundations (literacy, not building)** | **Stanford/DeepLearning.AI — Machine Learning Specialization** (audit free for literacy; pay only if you want the marquee cert) | IBM Machine Learning, IBM AI Engineering (coding-heavy) |
| **Prompt engineering** | **Anthropic Prompt Engineering Interactive Tutorial** (free practice) | standalone paid prompt courses |
| **Data analytics (one primary cert)** | **Google Data Analytics** (brand) *or* **IBM Data Science** (ACE credit) — pick per plan | the other becomes optional; skip duplicate "data analyst" certs |
| **Project management** | **Google Project Management** (ACE credit) | IBM Project Manager |
| **Cloud/AI vendor cert** | **Microsoft AI-900/AI-901** (cheap, real, fast) | Azure Associate tracks unless you want depth |
| **AI capstone credential** | **Anthropic CCA-F** (proctored, real credential) | — |
| **Deep learning (grad spine)** | **DeepLearning.AI — Deep Learning Specialization** (cert) | redundant intro-DL certs |
| **Reinforcement learning** | **Hugging Face Deep RL** (free cert) → **Berkeley CS285** (depth) | duplicate RL MOOCs |
| **Robotics fundamentals** | **Modern Robotics — Northwestern** (cert + capstone) | UPenn Robotics → broaden-only in Plan C |

**Kept OFF the critical path (you're not becoming a coder):** IBM AI Engineering,
IBM Generative AI Engineering, IBM AI Developer, IBM Data Engineering. They teach
PyTorch/Flask/Spark software engineering. Listed as optional in the catalog only.

---

## 5. Broadening beyond manufacturing (deliberately)

Your day-to-day is manufacturing/operations, but the degree is wider on purpose
so you understand the *system* around your work:

- **AI fluency & limits** → know what these tools can and can't do.
- **Data literacy** → read dashboards and analyses critically.
- **Project management** → run initiatives, not just tasks.
- **Technical literacy** → understand, at altitude, what code and ML models are
  doing — without being on the hook to write production software.
- **(Plan C) gen-ed electives** → e.g., Yale's *Financial Markets*, a
  *Learning How to Learn* refresher — breadth that makes you a sharper generalist.

---

## 6. How memory actually works here

After each module you (or I, when you re-run me) append a one-line entry to
`30-progress-ledger.md`:

```
2026-06-18 | Anthropic AI Fluency F&F | DONE | cert ✅ | confidence 4/5 |
            note: the 4D framework (Delegation/Description/Discernment/Diligence)
            is the spine — reuse it when judging any AI output.
```

That single habit is what makes this a *university* and not a playlist: the
system remembers what you know, surfaces what's shaky, and never re-teaches what
already stuck. Commit the ledger with `git` and it follows you across machines.
