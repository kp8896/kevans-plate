# 21 — Graduate Plan B: "Balanced" (Robotics + Machine Learning)

**Theme:** The focused spine **plus** perception depth and real mobile-robotics —
the difference between "trained a sim robot" and "understands robot perception &
control."
**Best if:** you want genuine breadth across vision, RL, and mobile robotics with
multiple credentials.

| | |
|---|---|
| **Estimated workload** | ~900 hrs |
| **Duration (3 hr/day)** | **~11.5 months** |
| **Range** | ~17 mo (2 hr/day) → ~9 mo (4 hr/day) |
| **Cost** | ~$200–$600 (Coursera certs via aid; ETH/edX verified cert is the likely real cost) |
| **Certificates earned** | Everything in Grad A **plus** ETH Zürich Autonomous Mobile Robots · Generative AI with LLMs · additional NVIDIA DLI · (free) Hugging Face LLM/Agents |

Plan B *contains* Grad Plan A. Additions below.

---

## Phases 1–4 — same as Grad Plan A (~520 hrs)
DL Specialization → HF Deep RL → Modern Robotics (+capstone) → Isaac Sim.
See `20-grad-A-focused.md`.

## Phase 5 — Computer Vision depth (~8 weeks, ~100 hrs)

| Course | Hrs | Cert | Why |
|---|---|---|---|
| **Stanford CS231n** — Deep Learning for Computer Vision (free materials + assignments) | ~80 | ❌ | Robot perception is mostly vision. Gold-standard course; do the assignments. |
| fast.ai — Practical Deep Learning (Part 1, selected lessons) | ~20 | ❌ | Top-down applied PyTorch to cement vision skills. |

**Milestone:** implement/explain an object detector; relate it to robot perception.

## Phase 6 — Real Mobile Robotics (~10 weeks, ~140 hrs)

| Course | Hrs | Cert | Why |
|---|---|---|---|
| **ETH Zürich — Autonomous Mobile Robots (AMRx, edX)** | ~120 | ✅ verified | Probabilistic localization, **SLAM**, perception, motion planning for real wheeled/legged/drone robots. The "how robots know where they are" course. |
| ROS 2 — navigation / MoveIt deeper tutorials | ~20 | — | Apply localization & planning in the standard stack. |

**Milestone:** explain a SLAM pipeline end-to-end; run a navigation demo in sim.

## Phase 7 — Modern AI / LLMs for robotics (~5 weeks, ~70 hrs)

| Course | Hrs | Cert | Why |
|---|---|---|---|
| **Generative AI with LLMs** (AWS + DeepLearning.AI) | ~16 | ✅ | LLMs increasingly drive robot high-level reasoning/planning. |
| **Hugging Face — LLM + Agents courses** | ~30 | ✅ free | Build agentic behavior; connect to robot control conceptually. |
| Expanded Isaac Lab capstone + a **Kaggle competition** | ~24 | Kaggle | A public portfolio piece. |

**Capstone deliverable:** a perception-driven robotics project in simulation —
e.g., a robot that *sees* (CS231n vision), *localizes* (ETH SLAM), and *acts*
(RL/control), with an LLM for task-level instructions. Write it up as a portfolio
centerpiece.

---

## What you finish with
A well-rounded graduate profile: deep learning, RL, computer vision, real mobile
robotics + SLAM, and modern LLM/agent skills — with five-plus credentials and a
substantial simulated-robotics portfolio.

## Next step
**Grad Plan C** adds research-grade depth (Berkeley CS285, Stanford CS229/224n,
UPenn) and the optional accredited-MS bridge (Georgia Tech OMSCS).
