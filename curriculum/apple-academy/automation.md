# Toby's Study Guide — Automation

> **Unit 2 / Process · Course 1.** Official workload **~3–4 hrs**. **21 items, 3
> parts.** Award: **pass the course assessment ≥ 70% + submit survey** (1 assessment).
> *Toby's original notes — not the course materials.*

> 🤖 **Robotics throughline:** this course's Part 3 (end effectors, part
> presentation, metrology, robotic arms, pick-and-place) is foundational robotics —
> a direct bridge to your **graduate Robotics+ML track**.

**Objectives:** explain what automation is & why it's used · identify basic types
& uses · describe the value of modular design · list common tools/support.

---

## Part 1 — INTRODUCTION TO AUTOMATION

- **2.2 What automation looks like (Apple examples):** Mac Pro uses **CNC machining**
  (precise metal/glass shaping), **robotic arms** (polishing, lens placement,
  adhesive), **automated washing/cooling/cleaning**, and **automated circuit
  assembly**; Apple Vision Pro likewise. Automation = machines doing tasks faster
  and more consistently than by hand.
- **2.3 Why automate:** Slowing **productivity** pushes firms to work smarter. The
  three classic reasons: **Safety** (remove people from dangerous jobs), **Quality**
  (accuracy & consistency, fewer errors), **Delivery** (speed & throughput).

**Toby's one-liner:** *Automate for Safety, Quality, Delivery — especially as
productivity growth stalls.*

## Part 2 — TYPES OF AUTOMATION SYSTEMS

First split: **Hard automation** (does one fixed task, hard/costly to change,
great for high-volume) vs **Soft automation** (reprogrammable, adaptable, great
for variety). Then four named types:

| Type | Flexibility | Typical use | Changeover | Throughput |
|---|---|---|---|---|
| **Fixed** | Low | Mass production, one product | Slow & expensive | Very high |
| **Programmable** | Moderate | Batch, moderate variation | Moderate | Med–high |
| **Flexible** | High | Frequent change, customization | Fast & easy | Medium |
| **Integrated** | High (connected) | Automated handling + assembly lines | — | High |

**Toby's one-liner:** *Fixed = fast but rigid; programmable = batch; flexible =
change-friendly; integrated = the whole line talking to itself.*

## Part 3 — DESIGNING FOR AUTOMATION  *(the robotics core)*

**Modular design**: break complex products into simple, manageable sections. And
**change is cheap early, expensive late** (the asymmetric cost-of-change curve) —
design it right up front. Four key design factors:

- **Part presentation** — get each part positioned/oriented consistently so a
  machine can grab it: **fixtures, feeders, robotic/adaptive methods.**
- **End effectors** — the robot's "hands": **grippers** (handling) and **process
  end effectors** (tools that do work). Pick the right one per part.
- **Metrology** — measurement for quality/process control: **dimensional**
  (size/shape), **force/weight**, **position/alignment.**
- **Transfer methods** — how parts move safely between stations.

Best practices: avoid tangling/jamming/damage; consistent orientation = fast,
accurate picks = smooth flow.

**Toby's one-liner:** *Present the part → grab it with the right end effector →
measure it (metrology) → move it (transfer) → keep it modular.*

---

## ✅ Active-recall self-quiz
1. Give the three reasons to automate and a one-line example of each.
2. Hard vs soft automation — core difference?
3. Rank fixed/programmable/flexible/integrated by flexibility and by changeover speed.
4. Name the four key design-for-automation factors.
5. What are the two families of end effectors, and what's each for?
6. Why is "design for automation early" cheaper than fixing it later?

## ✍️ "Your turn" practice
- [ ] Pick a task in your operation; classify which automation **type** fits and why.
- [ ] For that task, sketch part presentation + the end effector you'd choose.
- [ ] Name one quality check (metrology) you'd build in.

## 🏭 → 🤖 Tie-in
Part 3 *is* applied robotics. Carry these terms (end effector, part presentation,
metrology) into **Modern Robotics** and **Isaac Sim** in the grad track — you'll
meet them again as grippers, manipulation, and perception.

## ✅ Completion checklist
- [ ] All lessons in D2L · [ ] self-quiz ≥ 6/6 · [ ] **assessment ≥ 70%** ·
      [ ] survey · [ ] log in `_tracker.md` + `../30-progress-ledger.md`.

*Unit 2 (Process) Course 1 of 3 · could count as **4 of 5** toward Badge I.*
