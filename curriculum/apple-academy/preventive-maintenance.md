# Toby's Study Guide — Preventive Maintenance

> **Unit 2 / Process · Course 3.** Official workload **~3–4 hrs**. **17 items, 2
> parts.** Award: **pass the course assessment ≥ 70% + submit survey** (1 assessment).
> *Toby's original notes — not the course materials.*

> 🤖📊 **ML throughline:** **Predictive maintenance** and **condition monitoring**
> here are sensor-data + analytics problems — the manufacturing face of machine
> learning. This is the direct setup for **Unit 4: Predictive Maintenance** (Data)
> and the anomaly-detection side of your **robotics/ML grad track.**

**Objectives:** explain the purpose/benefits of PM · identify common PM tasks &
techniques · recognize signs of equipment problems & when to maintain · build a
basic PM plan for your context.

---

## Part 1 — PM & THEORY

**Four maintenance categories:** **Corrective** (fix after failure), **Preventive**
(regular checks/tasks to stop failures before they happen), **Improvement** (make
it better/more reliable), **Modification** (change the design/function).

**The four PM strategies (know the differences cold):**
- **Condition-based** — monitor *actual* condition (sensors/inspections); act when
  wear/anomaly shows. 5 steps: **select asset → collect data → analyze → corrective
  action → implement.** *(e.g., change oil when vibration rises.)*
- **Predetermined** — fixed schedule from history; read failure data/spikes,
  compute **MTBF (Mean Time Between Failures)**, plan intervals.
- **Predictive** — use data **trends/models to forecast** when failure will occur
  and act *just* before. The most data/ML-heavy.
- **Monitoring** — ongoing sensor/visual data feeding the above (data tables, trends).

**Toby's one-liner:** *Corrective = after; preventive = on a schedule (MTBF);
condition-based = when sensors say so; predictive = before, by forecasting.*

## Part 2 — CASE STUDY: jet soldering line

- **Jet soldering** + why it's used; the process at a glance.
- **Key parameters** (e.g., **shot height, laser energy, nitrogen pressure**) — drift
  here causes defects like **insufficient wetting** or **excessive solder.**
- **Failure analysis tools:** the **fishbone (Ishikawa) diagram** for root-cause +
  the **scientific method** (identify → gather info → test).
- **PM setup:** tie PM tasks to the key parameters (e.g., shot-height checks),
  **determine frequency** from failure data, use a **PM maturity checklist**, and an
  **OCAP (Out of Control Action Plan)** — a step-by-step troubleshooting checklist
  triggered when failure rates exceed a threshold.

**Toby's one-liner:** *Watch the key parameters → fishbone the root cause → set PM
frequency from the data → and have an OCAP ready when it goes out of control.*

---

## ✅ Active-recall self-quiz
1. Name the four maintenance categories.
2. Distinguish condition-based vs predetermined vs predictive — *when* does each act?
3. What is MTBF and how is it used?
4. What does a fishbone diagram do, and when?
5. What is OCAP and what triggers it?
6. Why is predictive maintenance the most "ML-like" strategy?

## ✍️ "Your turn" practice
- [ ] Pick one machine; list 3 key parameters that signal its health.
- [ ] Choose a PM strategy for it (condition-based / predetermined / predictive) and justify.
- [ ] Draft a 3-line OCAP: trigger → first checks → escalation.

## 🏭 → 🤖 Tie-in
This is the manufacturing entry point to ML: predictive maintenance = **time-series
sensor data + anomaly detection/forecasting**. Carry it straight into **Unit 4
Predictive Maintenance** and the grad track's RL/perception work.

## ✅ Completion checklist
- [ ] All lessons in D2L · [ ] self-quiz ≥ 6/6 · [ ] **assessment ≥ 70%** ·
      [ ] survey · [ ] log in `_tracker.md` + `../30-progress-ledger.md`.

*Unit 2 (Process) Course 3 of 3 — completes Unit 2 content.*
