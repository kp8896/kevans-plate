# Toby's Study Guide — SMT Success

> **Unit 1 / Foundations · Course 3.** Official workload **~1–2 hrs** (read/watch +
> assessment + survey). **18 items in 4 sections** (2 content parts).
> *Toby's original notes for active recall — not the course materials.*

> 🎓 **Award (in D2L):** complete all activities, **pass the course assessment
> ≥ 70%** (one assessment), and **submit the end-of-course survey**.

**Objectives:** identify the main steps & equipment of SMT assembly · recognize
common solder-paste-printing and placement defects · explain how inspection
systems catch/prevent defects · apply this to improve quality and reduce errors.

> ⭐ **Why this course matters most for you:** SMT inspection (SPI and AOI) is
> **machine vision** — cameras + algorithms judging quality. It's the direct
> bridge from your manufacturing major to **Unit 4: Machine Learning with Vision**
> and your **robotics/ML graduate track.** Learn the defects here; later you'll
> learn to *detect them with ML*.

---

## Part 1 — THE SMT LINE LAYOUT

**Vocabulary first:**
- **MLB** = Main Logic Board — the primary circuit board inside Apple products.
- **PCB / PCBA** = Printed Circuit Board / …Assembly (the board once parts are on it).
- **SMT** = Surface-Mount Technology — mounting components directly onto the board
  surface. **Ingredients:** the PCB, **solder paste**, and the **components**.

**The 6-step line (memorize this chain):**
1. **Solder paste printing** — *Screen Printer* lays paste on the pads through a **stencil**.
2. **SPI (Solder Paste Inspection)** — checks paste amount/alignment, catches bridges.
3. **Component placement** — *Pick & Place / Chip Mounter* sets parts onto the paste.
4. **Pre-reflow AOI (Automated Optical Inspection)** — verifies parts present/placed/oriented.
5. **Reflow soldering** — *Reflow Oven* melts the paste into solid joints.
6. **Post-reflow AOI** — final optical check for solder/joint problems.

**Details worth knowing:**
- **Solder paste** = solder powder + flux; powder size and **stencil** quality drive print quality.
- **Pick & place** machines place tiny parts fast and precisely — and parts keep
  **shrinking**, which makes placement and inspection harder.
- **Reflow profile** has 4 zones: **preheat → soak → reflow → cool.** The
  temperature curve (thermal profile) must be right or joints fail.

**Toby's one-liner:** *Print → inspect → place → inspect → reflow → inspect.*
Inspection is baked in at three points — that's the quality system.

## Part 2 — COMMON SMT DEFECTS

**Big idea:** most defects trace to one of the three process steps, and **SPI/AOI
vision** is how you catch them early (cheap) instead of late (expensive).

| Stage | Defects | Quick meaning |
|---|---|---|
| **Printing** | Bridge · Insufficient · Misaligned | paste shorts pads / too little / wrong spot |
| **Placement** | Shifted · Missing · Wrong polarity | part off-position / absent / backwards |
| **Reflow** | Tombstoning · Head-in-Pillow (HiP) · Solder open | part stands up / gap = weak joint / no joint at all |
| **Other** | Solder bridging · Capacitor cracks | shorts / internal crack from stress/heat |

**Detection:** **SPI** checks the *paste* (coverage, alignment, bridges) right after
printing; **AOI** checks the *components* (presence, placement, orientation, type)
before and after reflow. **Early detection** = far lower cost than catching it at
final test or in the field.

**Toby's one-liner:** *Defects are born at print/place/reflow; SPI and AOI (vision)
are how you catch each one before it's expensive.*

---

## ✅ Active-recall self-quiz
1. Decode: MLB, PCBA, SMT. What are the three "ingredients" of SMT?
2. List the 6 steps of the SMT line in order, with each machine.
3. What's the difference between **SPI** and **AOI** — and where does each sit?
4. Name the 4 reflow zones in order.
5. Match the defect to its stage: tombstoning, bridge, wrong polarity, Head-in-Pillow.
6. Why does early (vision-based) defect detection matter financially?

## ✍️ "Your turn" practice
- [ ] Draw the 6-step line from memory and label every machine + inspection point.
- [ ] For each of the 3 stages, name one defect and how SPI/AOI would catch it.
- [ ] One-paragraph note: *"Where could Machine Learning improve AOI defect
      detection?"* — seed for your Unit 4 course.

## 🏭 → 🤖 Tie-in (your throughline)
This is the most strategically important Foundations course for you: it grounds the
**Machine Learning with Vision** course (AOI = computer vision), connects to your
**Apple Manufacturing Academy major**, and feeds the **robotics/ML grad track**
(perception, defect classification, automated inspection).

## ✅ Completion checklist
- [ ] Do all lessons in D2L · [ ] self-quiz ≥ 6/6 from memory ·
      [ ] **pass the course assessment (≥ 70%)** · [ ] submit survey ·
      [ ] log in `_tracker.md` + `../30-progress-ledger.md`.

*Course **3 of 3** in Unit 1 (Foundations) — finishing this completes the
Foundations content; **3 of 5** toward Badge I.*
