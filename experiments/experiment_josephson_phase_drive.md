# Experiment JPD: Josephson Phase-Drive Decoupling Testbed

**Status:** Proposed — not yet built  [SPECULATIVE]
**Date:** 2026-06-10
**Schematic:** `experiment_josephson_phase_drive_schematic.svg`
**Class:** Goal 2 (phase decoupling) — depends on Goal 1; this is a *null-test
search*, not an "antigravity device". Every claim below tagged honestly.

---

## 1. Why This Design (and what the earlier rigs were missing)

The earlier concepts (3Y coil rig, coil drum) drive **electromagnetic** phase
in copper. But PDTP decoupling requires driving the **matter-wave phase ψ**
in α = cos(ψ − φ). In ordinary metal, every atom carries its own incoherent
ψ — there is no handle to grab. Only two laboratory systems have a single,
macroscopic, experimentally addressable matter phase:

1. **Superconductors** — all Cooper pairs share one condensate phase
   (Bardeen, Cooper & Schrieffer 1957)
2. Atomic BECs / superfluids — coherent but tiny mass

And superconductors come with a precision tool for *rotating* that phase:
the **AC Josephson effect** (Josephson 1962): a DC voltage V across a
junction makes the phase difference wind at exactly

```
dδ/dt = 2eV/ħ        i.e.  f_slip = (483.6 GHz per mV) × V      [ESTABLISHED]
```

This is metrology-grade physics — it *defines* the volt (Josephson constant
K_J = 2e/h, CODATA exact). No other technology rotates a matter phase at a
known, tunable rate. **My take: if PDTP decoupling can be tested on a
benchtop at all, this is the handle.**

---

## 2. The Hypothesis Under Test

**H1 [SPECULATIVE — the core assumption]:** the Cooper-pair condensate phase
is (or couples linearly to) the PDTP matter phase ψ appearing in
α = cos(ψ − φ).

**The PDTP chain if H1 holds:**
- A voltage-biased superconducting island has its condensate phase rotating
  at f_slip relative to everything else (lab frame / condensate φ).
- α = cos(ψ − φ) then oscillates at f_slip; sustained winding gives a
  time-averaged coupling ⟨α⟩ → 0 for the coherent electrons. [SPECULATIVE]
- The coherent fraction of the island's mass decouples: its weight drops.

**Honest caveat [ASSUMED]:** PDTP's ψ is the matter-wave (Compton) phase,
whose natural frequency is m c²/ħ ~ 10²⁰ Hz. H1 assumes the *relative slip
rate* is what matters (α depends only on the phase difference), so any
sustained slip decouples on time scales ≫ 1/f_slip. A null result falsifies
H1 + this mechanism — not all of PDTP.

---

## 3. The Signal Size (computed, honest)

Only the Cooper-pair condensate participates — the ionic lattice stays
locked. Maximum possible effect = the conduction-electron mass fraction:

```
Nb: 1 conduction electron per atom, A = 92.9
δm/m (max) = m_e / (92.9 × m_u) = 9.11e-31 / 1.54e-25 ≈ 5.9e-6   (~6 ppm)
```

For a **100 g niobium ring**: maximum weight deficit ≈ **590 μg**.
A commercial 1-μg mass comparator therefore has ~600× headroom — the
measurement is *easy* by precision-metrology standards. This is the design's
key virtue: the expected signal (if any) is comfortably above instrument
noise, so a null is a *real* null.

**Power check (PDTP, Part 29):** decoupling cost ~10 kW/ton = 10 W/kg
applies to the decoupled mass — here 0.6 mg of coherent electrons → ~6 μW.
Negligible. The cryocooler (~kW wall power) dominates, as expected:
the bottleneck is mechanism, not energy. [consistent with Part 29]

**Frequency scan range:** bias 1 nV → 1 mV covers f_slip ≈ 0.5 MHz → 484 GHz
(Nb junctions cap near the gap frequency ~700 GHz). Nearly six decades of
matter-phase slip rate from a single DC knob — no other rig concept comes
close.

---

## 4. Apparatus (see schematic SVG)

1. **Test mass:** annular Nb ring (~100 g) containing a series array of
   Josephson junctions (SIS trilayer or grain-boundary). The ring is an
   electrically isolated island biased through the array.
2. **Phase drive:** low-noise DC bias source (nV–mV), sweepable; bias
   modulated ON/OFF at ~0.1 Hz for lock-in detection.
3. **Cryostat:** 4 K pulse-tube (Tier B) or 77 K LN2 with YBCO ring (Tier A).
4. **Weighing:** the cold insert hangs from a precision mass comparator
   (1 μg readability) through a thermal/vibration decoupling stage;
   a matched **dummy ring** (normal metal, same mass/shape, same heater
   dissipation) hangs on the comparator's counter side.
5. **Shielding:** mu-metal + superconducting shield around the test region
   (magnetic artifacts are the historical killer — see §6); vacuum jacket
   (no buoyancy/convection); fluxgate magnetometer as witness sensor.
6. **DAQ:** comparator readout → lock-in referenced to the 0.1 Hz bias
   modulation; bias voltage, temperature, B-field, tilt all logged.

---

## 5. Protocol

1. Cool below T_c with zero bias. Record baseline weight 24 h (drift model).
2. Apply bias V; modulate ON/OFF at 0.1 Hz; record comparator lock-in
   amplitude for 1 h per bias point.
3. Step V logarithmically: 1 nV → 1 mV (≈ 60 points, ~3 days per full scan).
4. **Controls (each must be null):**
   - Same scan ABOVE T_c (no condensate → PDTP predicts no signal;
     any "signal" here is an EM/thermal artifact)
   - Dummy-heater run (matched dissipation, no junction array)
   - Bias polarity reversal (a real slip-rate effect depends on |V|;
     a magnetic artifact flips sign)
   - Field-coil injection test to calibrate magnetic crosstalk
5. Success criterion: weight deficit synchronous with modulation, present
   only below T_c, polarity-even, scaling with condensate fraction.

---

## 6. Prior Art — Read Before Believing Anything

- **Podkletnov (1992)** claimed 0.3–2% weight reduction above spinning YBCO
  discs. **Never replicated** (NASA MSFC program, Hathaway et al. 2003 —
  null). Treat as cautionary tale: his configuration had rotating magnetic
  fields, RF, and evaporating LN2 — all classic artifact sources.
- **Tajmar et al. (2006–2011)** reported small anomalous accelerometer
  signals near spinning superconductors; not confirmed by independent
  groups (Canterbury ring-laser test — null).
- This design differs in kind: **no moving parts, no rotating fields**, a
  DC-biased phase drive with metrology-grade frequency control, and a
  differential weighing with matched dummy — built to kill artifacts first.

---

## 7. Outcomes and What Each Means

| Outcome | Interpretation |
|---------|----------------|
| Null at δm/m < 1e-8 across full band | H1 falsified ~600× below max prediction: the Cooper-pair phase is NOT the PDTP ψ (or the slip mechanism is wrong). Goal 2 loses its only benchtop handle; redirect to breathing-mode searches. |
| Signal scaling with condensate fraction, below T_c only, polarity-even | Candidate decoupling detection. Immediately: vary material (Nb vs YBCO vs Pb), mass, f_slip dependence. Independent replication before any claim. |
| Signal also above T_c or polarity-odd | Artifact (EM/thermal). Fix shielding, repeat. |

**The "UFO scaling" question, honestly [SPECULATIVE]:** even a confirmed
maximal effect lifts only the electron mass fraction (~6 ppm of weight) —
no craft floats on that. A platform-like device would need bulk matter
coherent at the *nuclear* mass fraction, i.e. coherent matter states that do
not exist in known physics. This experiment cannot build a UFO; it can only
answer whether the decoupling channel exists at all. That is the right
first question, and it is answerable for roughly the cost of a used car
(Tier A) — eight years before LISA flies.

---

## 8. Build Tiers

| Tier | Test mass | Cryo | Junctions | Budget (rough) |
|------|-----------|------|-----------|----------------|
| A | YBCO ring, ~50 g | LN2 (77 K) | grain-boundary array (noisy but cheap) | R30k–R80k |
| B | Nb ring, ~100 g | 4 K pulse-tube | fabricated SIS array (metrology grade) | $50k+ (institutional) |
| C | Pre-study | none | — | software only: artifact budget + comparator noise model |

Tier C should be done first: a week of modelling to confirm the 1-μg
comparator + 0.1 Hz lock-in reaches δm/m ~ 1e-8 against cryostat vibration.

---

## 9. References

- Josephson, B.D. (1962). "Possible new effects in superconductive tunnelling." *Phys. Lett.* 1, 251.
- Bardeen, J., Cooper, L.N. & Schrieffer, J.R. (1957). "Theory of superconductivity." *Phys. Rev.* 108, 1175.
- Podkletnov, E. & Nieminen, R. (1992). *Physica C* 203, 441. [unreplicated]
- Hathaway, G., Cleveland, B. & Bao, Y. (2003). "Gravity modification experiment using a rotating superconducting disk." *Physica C* 385, 488. [null replication]
- Tajmar, M. et al. (2007). "Measurement of gravitomagnetic and acceleration fields around rotating superconductors." *AIP Conf. Proc.* 880, 1071. [unconfirmed]
- PDTP: Part 28b (decoupling = crossed polarizers, ΔV = g), Part 29 (~10 kW/ton; mechanism is the bottleneck), Part 115 (ω_gap must be measured, not derived).
