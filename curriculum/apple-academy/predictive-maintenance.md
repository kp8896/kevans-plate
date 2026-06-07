# Toby's Study Guide — Predictive Maintenance (Data)

> **Unit 4 / Data · Course 2.** Workload **~3–4 hrs**. **12 items, 2 parts.**
> Award: **pass the TWO module assessments ≥ 70% + survey.**
> *Toby's original notes — not the course materials.*
> ⚠️ **Not the same as Unit 2's "Preventive Maintenance."** That one was strategy &
> theory; **this** is the data/ML version — IoT sensors + change-detection in code.

> 🐍 **Technical-literacy moment:** this course uses **Python** for data
> visualization and change detection. Per your goal ("understand the code at a high
> level, not become a coder"), aim to *follow* the logic — what each method does and
> why — not to write production code. It's the perfect on-ramp to the grad ML track.

**Objectives:** explain IoT & Industrial IoT in maintenance/monitoring · describe &
compare **change-detection methods** · apply data viz & change detection **in
Python** · tune model settings to improve accuracy & cut false alarms.

---

## Part 1 — INTRO TO IoT & PREDICTIVE MAINTENANCE

- **2.2 IoT:** a **network of physical objects with sensors + software** that
  collect & exchange data. (Smart thermostat, Apple Watch, connected cars.) **Five
  components** make up a system.
- **2.3 Industrial IoT (IIoT):** factory machines reporting performance + maintenance
  needs. Shifts you from reactive to **condition monitoring** (24/7 sensing of temp,
  vibration, etc.).
- **2.4 Building blocks / protocols:** how data flows; **IO-Link** (sensor-level) and
  **OPC UA** (interoperability standard) — the plumbing of a connected factory.
- **2.5 Condition monitoring of a bearing (the worked example):** **accelerometers**
  detect vibration → bearing faults; **time-series databases** store the stream; raw
  data vs **aggregation** (e.g., 14 hrs raw → 1-min averages) to see the signal.

**Toby's one-liner:** *Sensors (IoT) → stream to a time-series store → monitor
condition (vibration via accelerometers) → catch faults early.*

## Part 2 — CHANGE DETECTION MODELS

**Big idea:** **change detection** = automatically spotting when a data stream does
something **unexpected**; a sudden unnatural shift is called **drift.** Manual
watching doesn't scale, so algorithms raise the alert.

- **3.2 Raw signal–based methods** — look **directly** at incoming data for sudden
  changes, no prior pattern needed. Simple, fast, real-time. Algorithms: **ADWIN**
  (adaptive windowing) and **KSWIN** (Kolmogorov–Smirnov windowing).
- **3.3 Model-based methods** — use a **predictive model** of expected behavior, then
  flag deviations. Example: a **moving-average model** (predict from recent values;
  inside-vs-outside-temperature analogy; has a simple formula).
- **Tuning:** adjust settings to balance **sensitivity vs false alarms.**

**Toby's one-liner:** *Drift = unexpected shift. Raw-signal methods (ADWIN/KSWIN)
watch the data directly; model-based methods compare reality to a prediction —
tune both to avoid false alarms.*

---

## ✅ Active-recall self-quiz
1. Define IoT and IIoT; give one example of each.
2. What do accelerometers + time-series data do in condition monitoring?
3. What is "drift," and why automate its detection?
4. Raw-signal vs model-based change detection — how does each work?
5. Name the two raw-signal algorithms and one model-based approach.
6. What trade-off are you tuning when you adjust detection settings?

## ✍️ "Your turn" practice
- [ ] Pick a machine; name the sensor + signal you'd monitor (e.g., vibration).
- [ ] Decide: raw-signal or model-based detection — and why.
- [ ] In the Python examples, identify *where* the threshold/sensitivity is set
      (understand it; you don't have to write it).

## 🏭 → 🤖 Tie-in (closing the loop)
This completes the manufacturing→ML arc: **Preventive Maintenance** (Unit 2) gave
the strategy; **this** gives the **data + algorithms**. Next in the grad track:
time-series & anomaly detection deepen in **DeepLearning.AI** and **fast.ai**; the
Python comfort you build here makes **IBM/Google data certs** and the grad ML
courses far easier.

## ✅ Completion checklist
- [ ] All lessons in D2L · [ ] self-quiz ≥ 6/6 · [ ] **BOTH module assessments ≥ 70%** ·
      [ ] survey · [ ] log in `_tracker.md` + `../30-progress-ledger.md`.

*Unit 4 (Data) Course 2 of 2 — completes the program's current 11 courses.*
