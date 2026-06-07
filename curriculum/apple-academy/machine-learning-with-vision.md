# Toby's Study Guide — Machine Learning with Vision

> **Unit 4 / Data · Course 1.** Workload **~3–4 hrs**. **19 items, 3 parts.**
> Award: **pass the TWO module assessments ≥ 70% + survey.**
> *Toby's original notes — not the course materials.*

> ⭐⭐ **This is the keystone course of your whole program.** It's where the
> manufacturing major and the AI/robotics throughline finally merge — a miniature
> of Stanford **CS231n** and the conceptual base for your **graduate Robotics+ML
> track.** Everything you flagged earlier (SMT's AOI, QCO's image anomaly
> detection) is *this*.

**Objectives:** explain core AI/ML concepts · state what computer vision is &
recognize applications · apply ML + CV to real problems.

---

## Part 1 — INTRODUCTION TO MACHINE LEARNING

- **2.2 History / the nested circles:** **AI ⊃ ML ⊃ DL.** AI = smart machines; **ML**
  = learns from *data* (not hand-coded rules); **DL** = ML using multi-layer **neural
  networks** for complex patterns. (AlphaGo as the landmark example.)
- **2.3 Taxonomy — the three learning types:**
  - **Supervised** — learns from **labeled** data. Two jobs: **regression** (predict
    a number) and **classification** (predict a category). *(spam filter, medical
    image diagnosis)*
  - **Unsupervised** — finds structure in **unlabeled** data *(customer grouping)*.
  - **Reinforcement** — learns by **trial & error / reward** *(← the grad-track RL link)*.
- **2.4 ML elements — data & labels:** data types & **quality** ("garbage in,
  garbage out"); **labeling** = attaching known answers so supervised models can learn.
- **2.5 ML process:** **data preparation → data split (train / validation / test) →
  training.** The split is what lets you check the model generalizes.

**Toby's one-liner:** *AI⊃ML⊃DL; supervised (regression/classification) vs
unsupervised vs reinforcement; and it all runs on labeled, well-split, quality data.*

## Part 2 — COMPUTER VISION

- **3.2 What CV is:** letting computers **"see"** — capture, interpret, respond to
  images/video. Everyday: face ID, photo organizing, security, driver assist,
  **industrial inspection/sorting.**
- **3.3 The image pipeline:** **capture → preprocess → feature extraction → analysis.**
  Preprocessing: blur/sharpen, denoise, grayscale, brightness/contrast. Algorithms:
  **edge detection, segmentation/grouping, restoration.**
- **3.4 Advanced (your robotics bridge):** **object tracking & action
  classification; 3D vision** (depth perception); and **autocalibration of robot
  workcells using 3D vision** — literally robotics perception.

**Toby's one-liner:** *Capture → clean → extract features (edges/segments) →
understand; and 3D vision + tracking is where CV becomes robotics.*

## Part 3 — USE CASES (applied defect detection)

- **Apple Create ML** — Apple's no/low-code tool to train vision models; model types;
  data types. (Apple model library: **DeepLabV3** = segmentation, **PoseNet** = pose
  estimation.)
- **Use case 1 — metal nut defect detection**; **Use case 2 — craft-stick damage via
  Apple AOI** (the same **AOI** from your SMT course!); **Use case 3 — part
  identification** (detecting/naming multiple objects).
- **The vision-QC recipe:** collect & label photos (Good vs Defective) → separate
  object from background (**contour detection**) → checks (symmetry, aspect ratio) →
  classify **Pass / Marginal / Failure** → boost data with **image augmentation.**
- **Manufacturing examples:** assembly, inventory, barcodes, face recognition,
  **defect detection.**

**Toby's one-liner:** *Label good vs bad → segment the part → measure & classify →
augment to improve. That's automated optical inspection, powered by ML.*

---

## ✅ Active-recall self-quiz
1. Draw the AI/ML/DL relationship and define each.
2. Supervised vs unsupervised vs reinforcement — one line + example each.
3. What's the difference between regression and classification?
4. List the 4 stages of the image pipeline.
5. Why split data into train/validation/test?
6. Walk the vision-based defect-detection recipe end to end.
7. Where does 3D vision connect to robotics?

## ✍️ "Your turn" practice
- [ ] Take a real part; define "Good" vs "Defective" categories you'd label.
- [ ] Sketch the capture→preprocess→features→classify pipeline for it.
- [ ] Name one defect from your **SMT** notes a vision model could catch automatically.

## 🏭 → 🤖 Tie-in (the convergence point)
This course unifies the program: **SMT defects** + **QCO image anomaly detection**
+ **Preventive/Predictive maintenance** all become ML problems here. Next stops in
the grad track: **DeepLearning.AI Deep Learning Specialization**, **Stanford
CS231n** (the deep version of Part 2), and robot **perception** in Isaac Sim.

## ✅ Completion checklist
- [ ] All lessons in D2L · [ ] self-quiz ≥ 7/7 · [ ] **BOTH module assessments ≥ 70%** ·
      [ ] survey · [ ] log in `_tracker.md` + `../30-progress-ledger.md`.

*Unit 4 (Data) Course 1 of 2 — your highest-priority course.*
