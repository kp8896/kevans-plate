# Agentic AI Track — Learning Path & Tracker

> The track that emerged from your own sourcing. Goal: go from "I use AI" to **"I
> design and build multi-agent systems"** — MCP, tools, RAG, orchestration — capped
> by the **Claude Certified Architect (CCA-F)** credential. Built from 5 inbox
> resources (HF MCP, Microsoft MCP, IBM RAG/Agentic, Stanford CS230, Anthropic).

**Where this sits:** an **AI-engineering specialization** — between the undergrad
degree and the robotics/ML "masters." It's the one track where you *deliberately*
lean into code (you can't orchestrate agents without it), but you can stay at the
**design/config/orchestration** altitude and let Claude Code carry the typing.

**Prerequisites (you'll have these):** basic Python *reading* (Apple Predictive
Maintenance + ML with Vision), AI/LLM fluency (Anthropic Tier 1), API concept
basics (Building with the Claude API).

---

## The path (4 tiers → capstone)

### Tier 1 — Foundations: Anthropic Builder  · ~13 hrs · free certs
*(shared with `anthropic/_path.md` Tier 3 — do once, counts for both)*
| Course | Hrs | Cert | Status |
|---|---|---|---|
| Claude Code 101 | ~1–2 | ✅ | ⬜ |
| Intro to Agent Skills | ~1 | ✅ | ⬜ |
| Intro to Subagents | ~1 | ✅ | ⬜ |
| Intro to Model Context Protocol (MCP) | ~1–2 | ✅ | ⬜ |
| **Building with the Claude API** | ~8 | ✅ | ⬜ |

*Outcome:* you understand agents, tools, subagents, MCP, and the Claude API.

### Tier 2 — MCP depth: Hugging Face MCP Course  · ~12–16 hrs · free cert
| Resource | Hrs | Cert | Status |
|---|---|---|---|
| HF MCP Course (Units 0–3, built *with Anthropic*) | ~12–16 | ✅ free (fundamentals after Unit 1; completion after Units 2–3) | ⬜ |

*Outcome:* MCP in theory + practice with an SDK; a deployed MCP app. (Also directly
covers the ~18% MCP/tool-design domain of CCA-F.)

### Tier 3 — Build real servers: Microsoft MCP for Beginners  · ~20–25 hrs · no cert
| Resource | Focus | Status |
|---|---|---|
| MS MCP — Modules 0–3 (fundamentals + first server/client, VS Code, stdio/HTTP) | core build skills | ⬜ |
| MS MCP — Module 5 selectives (Azure, security/OAuth, routing, context engineering) | production patterns | ⬜ |
| MS MCP — Module 11 (13-lab **PostgreSQL** integration capstone) | DB-backed MCP server | ⬜ |

*Outcome:* you can build and deploy a **custom MCP server** wired to a real data
source (e.g., a database or an API you use). *Most code-heavy tier — lean on Claude
Code; aim to understand the architecture, not memorize syntax.*

### Tier 4 — Multi-agent & RAG: IBM (selective)  · ~41 hrs · IBM cert if completed in full
*Pull these 4 from the IBM RAG & Agentic AI cert — don't do all 10 linearly.*
| Course | Hrs | Why | Status |
|---|---|---|---|
| #4 Advanced RAG with Vector DBs & Retrievers | ~8 | real retrieval patterns (FAISS/Chroma, HNSW) | ⬜ |
| #7 Agentic AI with LangChain & LangGraph | ~10 | state, memory, Reflection/ReAct | ⬜ |
| #8 LangGraph + CrewAI + AutoGen + BeeAI | ~13 | **multi-agent orchestration** (your core interest) | ⬜ |
| #9 Build AI Agents using MCP | ~10 | MCP in the LangChain ecosystem | ⬜ |

*Outcome:* you can architect a **multi-agent system** with retrieval, memory, and
tool/MCP integration. *(Do the full 10-course cert if you want the IBM credential;
otherwise these 4 are the high-value core.)*

### 🎓 Capstone credential — CCA-F  · ~20 hrs prep + exam
| Item | Detail | Status |
|---|---|---|
| **Claude Certified Architect – Foundations** | 60 scenario MCQs · 120 min · ~720/1000 · **$99** (free via Claude Partner Network) | ⬜ |

Tiers 1–4 *are* the prep — they cover all five CCA-F domains (agentic architecture
27% · Claude Code 20% · prompt/structured output 20% · tools/MCP 18% · context mgmt).

---

## Supplements (free, optional depth)
- **Stanford CS230 — Lecture 8: "Agents, Prompts & RAG"** (Ng) — the academic framing.
- **MARL book** (marl-book.com) — multi-agent reinforcement learning theory (also a
  grad-track text); the bridge between this track and robotics/ML.
- **Anthropic Prompt Engineering Interactive Tutorial** — structured-output practice.

## Totals & pacing
- **Core (Tiers 1–2 + CCA-F):** ~45 hrs → ~3 weeks @ 2–3 hr/day → **CCA-F + free certs.**
- **Full track (Tiers 1–4 + CCA-F):** ~110 hrs → **~6–9 weeks** @ 2–3 hr/day.

### Sample schedule (3 hr/day, 6 days/wk)
| Week | Focus | Milestone |
|---|---|---|
| 1 | Tier 1 (Anthropic Builder) | free Academy certs |
| 2 | Tier 2 (HF MCP) | 🏅 HF MCP certificate |
| 3–4 | Tier 3 (MS MCP build + PostgreSQL capstone) | a working custom MCP server |
| 5–7 | Tier 4 (IBM #4, #7, #8, #9) | a multi-agent system |
| 8 | CCA-F prep + exam | 🎓 **CCA-F credential** |

## Capstone project (tie it to real work)
Build a **multi-agent assistant** for your own workflow: a custom **MCP server**
(Tier 3) exposing a real data source (a database / an API you use), orchestrated by
a **multi-agent crew** (Tier 4) with retrieval over your documents. This doubles as
CCA-F evidence *and* a real tool you'll keep using.

## Cost
Tiers 1–3: **free** (Anthropic Academy, HF, Microsoft OSS). Tier 4: Coursera
~$49/mo (financial aid available; or audit individual courses). CCA-F: $99 (free via
Partner Network). **Near-$0 path exists** via aid + the free tiers.

## How it interlocks
- **Anthropic track:** Tier 1 is shared — do it once.
- **Robotics/ML grad track:** multi-agent RL (MARL) and RL (CS285/HF Deep RL) are the
  shared theory; agents are ML applied to orchestration vs. control.
- **Your real agent-building work:** the Tier 3/4 capstone *is* that project,
  done with academic backing and a credential attached.

## Next action
Start **Tier 1** (if not already done via the Anthropic track). When you open the
**HF MCP Course**, say "Toby, build the MCP course guide" and I'll produce a study
guide + self-quiz like the others, and log progress here.
