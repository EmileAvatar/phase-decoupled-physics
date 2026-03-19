# Experiment: Phase-Gradient Coil Drum

**Status:** Proposed — not yet built
**Date:** 2026-03-15
**Budget:** £200–£500 (~R5,000–R12,000 / $250–$650 USD)
**Goal:** Test whether a traveling EM phase wave through a toroidal coil
array produces a measurable weight anomaly in a superconducting sample,
consistent with EM-to-gravitational condensate coupling.

**PDTP basis:**
- A ring of N coils, each driven at phase offset 360/N degrees, creates a
  traveling phase wave — identical to a linear induction motor or traveling
  wave tube amplifier (proven technology)
- If EM phase couples (even weakly) to the gravitational condensate phase phi,
  the traveling wave acts as a lever: EM phase drive -> condensate phase shift
  -> alpha = cos(psi - phi) deviates from 1
- The collective condensate mode frequency (omega_gap) is the target, NOT
  individual particle Compton frequencies (~10^23 Hz)
- BCS analogy: superconducting gap (~100 GHz) is 9 orders below electron
  Compton frequency (~10^20 Hz) — collective modes are MUCH lower than
  single-particle frequencies

**Falsifiability:**
- If NO frequency across the full sweep produces ANY weight anomaly -> the
  EM-to-gravitational coupling does not exist at this power level (constrains
  coupling constant)
- If a specific frequency produces a repeatable, shielding-independent weight
  anomaly -> candidate detection of EM-gravitational phase coupling

**How this differs from the 3Y Rig:**

| Feature | 3Y Rig | Coil Drum |
|---------|--------|-----------|
| Geometry | Triangular Y-junction (Z3 node) | Toroidal ring (traveling wave) |
| Wave type | Standing wave at centre node | Traveling phase wave around ring |
| Topology | Z3 topological defect | Continuous phase gradient (U(1)) |
| Target sample | Lead test mass on torsion balance | YBCO superconductor ring |
| Detector | Laser/photodiode torsion readout | Precision scale (mg resolution) |
| PDTP mechanism | Phase cancellation: psi_1+psi_2+psi_3=0 | Phase drag: traveling EM wave entrains phi |
| Frequency range | Hz to MHz sweep | Hz to MHz sweep |
| Key reference | Part 37 (Z3 vortex topology) | Tajmar (2006) gravitomagnetic anomaly |

The two experiments are complementary: 3Y tests topological (Z3) coupling,
Coil Drum tests continuous (U(1)) phase dragging. Both should be run.

---

## Table of Contents

1. [Theory Summary](#1-theory-summary)
2. [What We Are Testing](#2-what-we-are-testing)
3. [The Linear Induction Motor Analogy](#3-the-linear-induction-motor-analogy)
4. [The BCS Gap Analogy](#4-the-bcs-gap-analogy)
5. [Why a Superconductor](#5-why-a-superconductor)
6. [Build Specification](#6-build-specification)
7. [Coil Winding Details](#7-coil-winding-details)
8. [Electronics and Control](#8-electronics-and-control)
9. [Experimental Protocol](#9-experimental-protocol)
10. [Control Runs](#10-control-runs)
11. [Data Analysis](#11-data-analysis)
12. [What Success Looks Like](#12-what-success-looks-like)
13. [Systematic Effects](#13-systematic-effects)
14. [Safety Notes](#14-safety-notes)
15. [Shopping List](#15-shopping-list)
16. [Connection to Acoustic Levitation Concept](#16-connection-to-acoustic-levitation-concept)
17. [References](#17-references)

---

## 1. Theory Summary

### 1.1 Traveling Phase Wave

A ring of N coils, each carrying the same AC signal but with a phase offset
of 360/N degrees between neighbours, creates a **traveling phase wave** that
moves around the ring at controllable speed:

```
v_phase = omega * d

where:
    omega = angular frequency of the AC drive (rad/s)
    d     = coil spacing (metres)
```

This is NOT a propagating EM wave (which travels at c). It is a **slow-wave
structure** — the phase pattern crawls around the ring at v_phase << c.
The speed is set by the drive frequency and geometry, not by the speed of light.

**Source:** This is the operating principle of:
- [Linear induction motor](https://en.wikipedia.org/wiki/Linear_induction_motor) (maglev trains)
- [Traveling-wave tube](https://en.wikipedia.org/wiki/Traveling-wave_tube) (microwave amplifiers)
- [Three-phase electric motor](https://en.wikipedia.org/wiki/Three-phase_electric_power) (industrial motors)

All proven, century-old technology. The novelty is the APPLICATION: using the
traveling EM phase pattern to probe coupling to the gravitational condensate.

### 1.2 PDTP Phase Coupling

In PDTP, the gravitational coupling is:

```
alpha = cos(psi - phi)                                          [ASSUMED]

where:
    psi = matter phase (driven by EM oscillation in coils)
    phi = spacetime condensate phase (the gravitational field)
```

If the coil array drives psi in a traveling wave pattern, and if ANY coupling
exists between EM oscillation and the condensate phase phi, then the traveling
wave acts as a **phase drag** — pulling phi along with psi.

The effect on gravity is:

```
If phi shifts by delta_phi at frequency omega:
    alpha = cos(psi - phi - delta_phi) != cos(psi - phi)
    -> effective gravitational coupling changes
    -> weight of assembly changes by delta_W = M * g * (1 - alpha_new)
```

Even a tiny coupling (delta_phi ~ 10^-7 radians, as suggested by Tajmar 2006)
would produce a measurable weight change at milligram resolution.

### 1.3 The Tajmar Hint

In 2006, Martin Tajmar and colleagues reported an anomalous frame-dragging-like
signal from a spinning superconductor (niobium ring at ~5K). The measured
gravitomagnetic field was:

```
B_g ~ 10^-14 rad/s    (at edge of spinning ring)

Ratio to Lense-Thirring prediction: ~ 10^18 (way too large for GR)
Coupling constant (if real): g_EM->grav ~ 10^-7
```

This result has NOT been independently confirmed and remains controversial.
ESA's Gravity Probe B did not see the effect. However:
- The experiment was published in a peer-reviewed journal
- The anomaly tracked the rotation frequency, not a systematic artifact
- If real, it suggests EM-gravitational coupling exists at ~10^-7 level

**Source:** Tajmar et al. (2006), "Measurement of Gravitomagnetic and
Acceleration Fields Around Rotating Superconductors", AIP Conference
Proceedings 880, 1071.

**IMPORTANT:** We are NOT assuming Tajmar is correct. We are testing whether
a similar coupling exists, using a different method (traveling phase wave
instead of rigid rotation). If the coupling does not exist, we get a null
result that constrains the coupling constant. Either outcome is valuable.

---

## 2. What We Are Testing

### 2.1 Primary Hypothesis

**A traveling EM phase wave through a toroidal coil array, passing through
a superconducting sample, produces a frequency-dependent weight anomaly
consistent with EM-to-gravitational phase coupling.**

### 2.2 What We Do NOT Know

- Whether EM-to-gravitational coupling exists at all
- The coupling constant (Tajmar suggests ~10^-7; could be much smaller)
- The resonant frequency (if any)
- Whether a superconductor is necessary or just helpful

### 2.3 What We DO Know

- Traveling phase waves in coil arrays are proven technology
- Superconductors have macroscopic quantum coherence (all Cooper pairs in
  the same quantum state — maximum collective coupling)
- The BCS gap frequency (~100 GHz for YBCO) is a natural resonance candidate
- Precision scales with mg resolution are commercially available (~R500)

### 2.4 Experimental Strategy

**Frequency sweep with precision weighing.** Drive the coil array at
frequency f, measure the total weight of the assembly (coils + YBCO ring +
LN2 dewar) on a precision scale. Sweep f from 1 Hz to 1 MHz. Plot weight
vs frequency. Look for any deviation from the baseline.

---

## 3. The Linear Induction Motor Analogy

### 3.1 How a Linear Induction Motor Works

A linear induction motor (LIM) has a row of coils, each energized in
sequence with a phase offset. This creates a magnetic field pattern that
travels along the row:

```
Time t=0:    [N]  [ ]  [S]  [ ]  [N]  [ ]  [S]
Time t=T/4:  [ ]  [N]  [ ]  [S]  [ ]  [N]  [ ]
Time t=T/2:  [S]  [ ]  [N]  [ ]  [S]  [ ]  [N]

-> Magnetic field pattern moves to the right at v = wavelength * frequency
```

A conducting plate placed near the coils experiences eddy currents that
interact with the traveling field — the plate is DRAGGED along.

**Source:** [Linear induction motor — Wikipedia](https://en.wikipedia.org/wiki/Linear_induction_motor)

### 3.2 The PDTP Version

Replace "conducting plate" with "gravitational condensate":

```
Standard LIM:    Traveling B-field -> eddy currents in metal -> drag force
PDTP coil drum:  Traveling EM phase -> phase coupling to phi -> condensate drag
```

The coil drum IS a linear induction motor wrapped into a toroid. Instead of
dragging a metal plate, we are testing whether it drags the condensate phase.

If the condensate phase phi is dragged by the traveling EM pattern, the
effective gravitational coupling alpha = cos(psi - phi) changes — and the
assembly weight shifts.

### 3.3 Why Toroidal Geometry

A straight row of coils creates a traveling wave that exits at one end.
Wrapping the row into a toroid creates a **closed traveling wave** —
the phase pattern circulates endlessly, building up over many cycles.

```
Top view of toroidal coil drum:

        Coil 1 (0 deg)
           |
    Coil 6 +---+ Coil 2 (60 deg)
     (300)  | * |
    Coil 5 +---+ Coil 3 (120 deg)
     (240)     |
        Coil 4 (180 deg)

    * = YBCO ring inside the toroid
    Phase wave rotates: 1->2->3->4->5->6->1->...
```

Advantages of toroidal geometry:
- **Contained field:** magnetic field stays inside the toroid (no stray fields)
- **Continuous circulation:** phase wave has no start/end — builds up coherently
- **Matches saucer geometry:** a toroidal field pattern in a disk-shaped structure
- **No external reaction force:** all forces are internal to the assembly

---

## 4. The BCS Gap Analogy

### 4.1 Why Collective Modes Matter

The naive PDTP prediction for the condensate frequency is:

```
omega_gap = m_cond * c^2 / hbar

If m_cond = m_Planck: omega_gap ~ 10^43 Hz    (impossible to reach)
If m_cond = m_proton: omega_gap ~ 10^23 Hz    (still impossible)
```

But this is the SINGLE-PARTICLE frequency. Collective modes can be
orders of magnitude lower:

### 4.2 BCS Superconductor Precedent

| Quantity | Value | Scale |
|----------|-------|-------|
| Electron Compton frequency | ~1.2 x 10^20 Hz | Single particle |
| Plasma frequency (metal) | ~10^15 Hz | Collective (electrons) |
| BCS gap frequency (Nb, 9K) | ~7 x 10^11 Hz | Collective (Cooper pairs) |
| BCS gap frequency (YBCO, 93K) | ~1 x 10^13 Hz | Collective (Cooper pairs) |

The BCS gap is **9 orders of magnitude** below the electron Compton frequency.

**Source:** [BCS theory — Wikipedia](https://en.wikipedia.org/wiki/BCS_theory)

### 4.3 Implication for PDTP

If the gravitational condensate has a collective mode analogous to the BCS gap,
its frequency could be enormously lower than m_cond c^2/hbar. How much lower
depends on the condensate density and coupling — which we don't know.

This is WHY we sweep frequency: we cannot predict the resonance from first
principles (m_cond is unknown), so we scan experimentally.

The BCS analogy suggests the relevant frequency could be in an accessible
range (Hz to GHz), not at Planck scale. This is the theoretical motivation
for the experiment being feasible at all.

---

## 5. Why a Superconductor

### 5.1 Macroscopic Quantum Coherence

A superconductor below T_c has ALL its Cooper pairs in a single quantum
state. This means:

- The phase psi is the SAME across the entire sample (macroscopic coherence)
- Phase oscillations in the coil array couple to ALL Cooper pairs simultaneously
- The effective coupling is amplified by the number of Cooper pairs: N ~ 10^22

In a normal metal, electrons are incoherent — each has a random phase.
Driving them with a phase wave produces no collective effect. In a
superconductor, the collective response is macroscopic.

**Source:** [Macroscopic quantum phenomena — Wikipedia](https://en.wikipedia.org/wiki/Macroscopic_quantum_phenomena)

### 5.2 Why YBCO (Not Niobium)

| Property | Niobium (Nb) | YBCO |
|----------|-------------|------|
| T_c | 9.2 K | 93 K |
| Coolant | Liquid helium (4K, expensive) | Liquid nitrogen (77K, cheap) |
| Cost per cooldown | ~£200 | ~£5 |
| Availability | Specialist supplier | Educational/hobby supplier |
| BCS gap | ~1.4 meV (~340 GHz) | ~30 meV (~7 THz) |
| Coherence length | ~40 nm | ~1.5 nm (anisotropic) |

YBCO is a high-T_c superconductor cooled by liquid nitrogen (77K). LN2 costs
about £5 per litre and is available from welding suppliers and universities.
This makes repeated experiments affordable.

**Source:** [Yttrium barium copper oxide — Wikipedia](https://en.wikipedia.org/wiki/Yttrium_barium_copper_oxide)

### 5.3 YBCO Ring Geometry

A ring (toroid or annulus) placed inside the coil drum:

```
Cross-section:

    [Coil] [Coil] [Coil] [Coil] [Coil] [Coil]
     ╭──────────────────────────────────────╮
     │              Toroid former            │
     │    ╭──────────────────────────╮      │
     │    │      YBCO ring           │      │
     │    │    (superconducting)     │      │
     │    ╰──────────────────────────╯      │
     ╰──────────────────────────────────────╯
    [Coil] [Coil] [Coil] [Coil] [Coil] [Coil]
```

The YBCO ring sits inside the bore of the coil drum. The traveling magnetic
field from the coils passes through the superconductor, coupling to the
Cooper pair condensate.

---

## 6. Build Specification

### 6.1 Toroidal Former

- **Material:** Fiberglass tube or 3D-printed PLA/ABS
- **Major radius (R):** 75 mm (centre of toroid to centre of tube)
- **Minor radius (r):** 15 mm (tube cross-section radius)
- **Total outer diameter:** 180 mm
- **Number of coil slots:** 12 (one every 30 degrees) or 6 (every 60 degrees)
- Minimum viable: 3 coils at 120 degrees (three-phase)

### 6.2 Assembly Overview

```
Side view:

    ┌─────────────────────────┐
    │    Precision scale       │
    │  ┌───────────────────┐  │
    │  │  Styrofoam dewar   │  │
    │  │  ┌─────────────┐  │  │
    │  │  │ LN2 (77 K)  │  │  │
    │  │  │  ┌───────┐  │  │  │
    │  │  │  │ Coil   │  │  │  │
    │  │  │  │ drum   │  │  │  │
    │  │  │  │ + YBCO │  │  │  │
    │  │  │  └───────┘  │  │  │
    │  │  └─────────────┘  │  │
    │  └───────────────────┘  │
    └─────────────────────────┘

    Wires exit through top to controller (no force on scale from wires)
```

The entire assembly (coil drum + YBCO ring + LN2 dewar) sits on the
precision scale. Only the signal wires exit the top — and these must be
arranged to exert zero net vertical force (loose drape, symmetrical routing).

### 6.3 Key Dimensions

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Toroid major radius R | 75 mm | Fits inside small dewar |
| Toroid minor radius r | 15 mm | Room for coil windings |
| Number of coils N | 6 (minimum 3) | 60 deg spacing; 3-phase minimum |
| Coil turns | 100 per coil | ~0.5 mH inductance |
| Wire diameter | 0.5 mm enamelled copper | Standard, cheap |
| YBCO ring OD | 40 mm | Available from educational suppliers |
| YBCO ring ID | 25 mm | Standard YBCO ring geometry |
| YBCO ring height | 10 mm | Standard |
| Total assembly mass | ~2 kg (with LN2) | Within scale capacity |

---

## 7. Coil Winding Details

### 7.1 Winding Each Coil

Each coil is wound on a section of the toroidal former:

```
One coil segment (side view):

    ┌──────┐
    │ Turn │
    │  100 │  <- 100 turns of 0.5mm enamelled copper
    │  ... │
    │  002 │
    │  001 │
    └──────┘
      30 deg arc of toroid
```

**Winding procedure:**
1. Mark the toroid former into N equal segments (e.g., 6 segments of 60 deg)
2. Wind 100 turns of 0.5 mm enamelled copper wire on each segment
3. Leave ~5 mm gap between adjacent coils (prevents shorting)
4. Secure windings with kapton tape or polyurethane varnish
5. Bring out two leads per coil (start and end of winding)
6. Label leads: Coil 1A, Coil 1B, Coil 2A, Coil 2B, etc.

### 7.2 Electrical Properties (per coil)

| Property | Value | Formula |
|----------|-------|---------|
| Turns | 100 | N |
| Wire length | ~10 m | pi * d_coil * N_turns |
| DC resistance | ~0.9 ohm | rho * L / A (copper at 20C) |
| Inductance | ~0.5 mH | Depends on geometry |
| Impedance at 1 kHz | ~3.2 ohm | sqrt(R^2 + (2*pi*f*L)^2) |
| Impedance at 10 kHz | ~31 ohm | Same formula |
| Impedance at 100 kHz | ~314 ohm | Same formula |
| Self-resonant frequency | ~1 MHz | Estimate; parasitic capacitance |

At frequencies above the self-resonant frequency (~1 MHz), the coil
behaves as a capacitor, not an inductor. For higher frequencies,
fewer turns or different coil geometry is needed.

### 7.3 Phase Wiring

For 6 coils with 60-degree spacing:

```
Coil 1: phase = 0 deg
Coil 2: phase = 60 deg
Coil 3: phase = 120 deg
Coil 4: phase = 180 deg
Coil 5: phase = 240 deg
Coil 6: phase = 300 deg
```

For minimum 3-coil configuration (120-degree spacing):

```
Coil A: phase = 0 deg
Coil B: phase = 120 deg
Coil C: phase = 240 deg
```

The three-phase configuration is the minimum that produces a smooth
traveling wave. More coils = smoother wave = less harmonic content.

---

## 8. Electronics and Control

### 8.1 Controller

**STM32 (recommended)** or Arduino Mega with DDS modules:

| Component | Function | Cost |
|-----------|----------|------|
| STM32F411 Black Pill | Master controller, 100 MHz clock | R200 |
| 3x AD9833 DDS modules | Sine wave generation, 0-12.5 MHz | R450 |
| 3x TDA2030 amplifiers | Current drive for coils, 18W each | R120 |
| 12V 5A power supply | Amplifier power | R200 |
| USB serial adapter | Data logging to laptop | R60 |

**Alternative (cheaper):** Arduino Mega + 3 PWM outputs + RC low-pass
filters. Limited to ~50 kHz but adequate for initial sweep.

### 8.2 DDS Phase Control

The AD9833 DDS (Direct Digital Synthesis) chip generates a precise sine
wave at any frequency from 0 to 12.5 MHz with 0.1 Hz resolution. Each
chip has an independent phase register.

```
Setup:
    DDS 1: frequency = f, phase = 0
    DDS 2: frequency = f, phase = 120 deg (0x555 in 12-bit register)
    DDS 3: frequency = f, phase = 240 deg (0xAAA in 12-bit register)

All three DDS share the same clock -> phase relationship is exact
```

**Source:** [AD9833 datasheet](https://www.analog.com/en/products/ad9833.html)

### 8.3 Amplifier Stage

Each DDS output (~0.6 Vpp) is amplified by a TDA2030 to drive the coil:

```
DDS output (0.6 Vpp, high-Z)
    |
    v
TDA2030 (gain = 20, Vout up to 14 Vpp into 4 ohm)
    |
    v
Coil (0.5 mH, ~1 ohm DC)
```

At low frequencies (<1 kHz), the coil impedance is ~1 ohm -> current up
to 7A peak (high!). Use a series resistor (10 ohm) to limit current at
low frequencies, or reduce amplifier gain.

At higher frequencies (>10 kHz), coil impedance rises naturally and
limits current.

### 8.4 Firmware Pseudocode

```
// STM32 firmware: coil_drum_sweep.c

configure_DDS(3 modules, shared 25MHz clock)
configure_serial(115200 baud, USB)

for f = START_FREQ to END_FREQ step STEP_SIZE:

    // Set all three DDS to same frequency, 120 deg apart
    DDS_1.set(f, phase=0)
    DDS_2.set(f, phase=120)
    DDS_3.set(f, phase=240)

    // Wait for transients to settle
    delay(SETTLE_TIME)  // 2 seconds

    // Read scale weight (N readings, average)
    weight_sum = 0
    for i = 0 to N_SAMPLES:
        weight_sum += read_scale()
        delay(SAMPLE_INTERVAL)
    weight_avg = weight_sum / N_SAMPLES

    // Log to serial
    serial_send(f, weight_avg, timestamp)

// All frequencies done
DDS_all_off()
serial_send("SWEEP_COMPLETE")
```

---

## 9. Experimental Protocol

### 9.1 Pre-Run Setup

1. Wind coils on toroidal former (Section 7)
2. Place YBCO ring inside the bore of the toroid
3. Put assembly into a styrofoam dewar (insulated container)
4. Place dewar on precision scale
5. Route signal wires out the top with a loose drape (no tension on scale)
6. Connect to controller board
7. Verify 3-phase output on oscilloscope (120-degree offset confirmed)
8. Power up scale, wait for reading to stabilize (10 minutes)

### 9.2 Cooldown Procedure

1. Record baseline weight (room temperature, coils OFF)
2. Pour liquid nitrogen slowly into the dewar until YBCO is submerged
3. Wait for boiling to settle (~5 minutes)
4. Record weight with LN2 (coils still OFF) — this is the COLD BASELINE
5. LN2 will evaporate during the run — record weight at regular intervals
   to track the evaporation slope (linear in time)

### 9.3 Frequency Sweep

| Parameter | Value | Notes |
|-----------|-------|-------|
| Start frequency | 1 Hz | Below any expected resonance |
| End frequency | 1 MHz | Coil self-resonance limit |
| Step size | Logarithmic: 10 steps/decade | 1, 1.26, 1.58, 2, 2.5, 3.16, ... |
| Total steps | ~60 (6 decades x 10 steps) | |
| Dwell time per step | 30 seconds | 10s settle + 20s measurement |
| Total sweep time | ~30 minutes | Repeat 3x = 90 minutes |
| LN2 hold time | ~2 hours in styrofoam | Enough for 3 sweeps |

### 9.4 Measurement at Each Frequency

1. Set DDS to frequency f with 120-degree phase offsets
2. Wait 10 seconds for transients to settle
3. Read scale 100 times over 20 seconds (5 Hz sample rate)
4. Compute mean weight and standard deviation
5. Log: f, mean_weight, stdev, timestamp, LN2_level_estimate
6. Move to next frequency

### 9.5 Repeat Runs

Run the full sweep 3 times:
- Run 1: Forward sweep (low to high frequency)
- Run 2: Reverse sweep (high to low frequency)
- Run 3: Forward sweep again

If a candidate signal appears, it must be present in all 3 runs at the
same frequency (not shifting with time/temperature/LN2 level).

---

## 10. Control Runs

**Control A: Coils OFF, cold YBCO, scale reading**
- LN2 poured, YBCO cold, coils disconnected
- Record weight for 30 minutes
- This gives the baseline drift (evaporation slope + thermal drift)
- Any anomaly here is environmental, not from the coils

**Control B: Coils ON, room temperature (NO LN2, YBCO warm)**
- Same frequency sweep but YBCO is above T_c (not superconducting)
- If the effect requires superconductivity, it should VANISH here
- If signal appears at room temperature too -> not SC-dependent

**Control C: Coils ON, cold YBCO, single phase (NOT 3-phase)**
- Only one coil active (no traveling wave, just oscillating field)
- If the traveling wave topology is essential, single-phase shows nothing
- If signal appears with single phase too -> not topology-dependent

**Control D: Coils ON, cold YBCO, reversed phase direction**
- Swap phase assignments: Coil 1=0, Coil 2=240, Coil 3=120
- This reverses the traveling wave direction
- If the effect is real and direction-dependent, the weight anomaly
  should reverse sign (heavier <-> lighter)
- If no direction dependence -> signal is not from traveling wave

---

## 11. Data Analysis

### 11.1 Subtracting the Evaporation Baseline

LN2 evaporates continuously. The raw weight vs time curve slopes downward.
Fit a linear trend to the Control A data and subtract it from all runs:

```python
# Baseline subtraction
evap_rate = linear_fit(control_a_weight, control_a_time)  # g/s
corrected_weight[i] = raw_weight[i] - evap_rate * time[i]
```

### 11.2 Signal Detection

For each frequency step, compute:

```
delta_W(f) = weight_coils_on(f) - weight_coils_off(f)

Noise floor = median(|delta_W|) * 1.4826   (MAD estimator)
Threshold = 5 * noise_floor                  (5-sigma)

Candidate = any f where |delta_W(f)| > threshold
```

Use 5-sigma (not 3-sigma) because we are scanning ~60 frequencies —
the look-elsewhere effect requires a higher threshold.

### 11.3 Consistency Checks

A candidate signal must satisfy ALL of:
1. Present in all 3 forward/reverse sweeps at the same frequency
2. Absent in Control B (room temperature -> not SC-dependent is suspicious)
3. Absent in Control C (single phase)
4. Reverses in Control D (reversed phase direction) — or at least changes
5. Amplitude consistent across sweeps (not growing or shrinking with time)

### 11.4 Analysis Script

```python
# coil_drum_analysis.py
import numpy as np
import matplotlib.pyplot as plt

# Load sweep data (columns: frequency, weight_mean, weight_std, time)
data = np.loadtxt("sweep_data.csv", delimiter=",")
freq = data[:, 0]
weight = data[:, 1]
weight_err = data[:, 2]
time = data[:, 3]

# Load control A for evaporation baseline
ctrl = np.loadtxt("control_a.csv", delimiter=",")
evap_rate = np.polyfit(ctrl[:, 3], ctrl[:, 1], 1)[0]  # g/s

# Subtract evaporation
weight_corr = weight - evap_rate * time

# Compute deviation from mean
baseline = np.median(weight_corr)
delta_w = weight_corr - baseline
noise = np.median(np.abs(delta_w)) * 1.4826
threshold = 5 * noise

# Plot
fig, ax = plt.subplots(figsize=(12, 5))
ax.semilogx(freq, delta_w * 1000, 'b.-')  # convert to mg
ax.axhline(threshold * 1000, color='r', ls='--', label='5-sigma')
ax.axhline(-threshold * 1000, color='r', ls='--')
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Weight anomaly (mg)")
ax.set_title("Coil Drum Sweep - Weight vs Frequency")
ax.legend()
plt.savefig("coil_drum_result.png", dpi=150)
plt.show()

candidates = np.where(np.abs(delta_w) > threshold)[0]
print(f"Noise floor: {noise*1000:.3f} mg")
print(f"5-sigma threshold: {threshold*1000:.3f} mg")
print(f"Candidates: {len(candidates)}")
for c in candidates:
    print(f"  f = {freq[c]:.1f} Hz, delta_W = {delta_w[c]*1000:.3f} mg")
```

---

## 12. What Success Looks Like

### 12.1 Positive Result

A frequency f_res where the weight anomaly:
- Is present with 3-phase traveling wave in superconducting YBCO
- Vanishes at room temperature (YBCO above T_c)
- Vanishes with single-phase drive (no traveling wave)
- Reverses when phase direction is reversed
- Reproduces across 3+ independent runs
- Exceeds 5-sigma above the noise floor

This would be evidence for EM-to-gravitational condensate phase coupling
and would justify immediate scaling up and professional replication.

### 12.2 Null Result

No signal at any frequency. This means:
- **(a)** The coupling constant is below our detection threshold, OR
- **(b)** A superconductor at 77K is not sufficient (need lower T?), OR
- **(c)** The traveling-wave mechanism does not couple to gravity

A null result with a quantified noise floor (e.g., "coupling < 10^-8 at
95% confidence") is a publishable constraint on EM-gravitational coupling.

### 12.3 Sensitivity Estimate

Precision scale resolution: 1 mg = 10^-6 kg
Assembly mass: ~2 kg
Minimum detectable fractional weight change:

```
delta_alpha_min = delta_W / (M * g)
                = 10^-6 / (2 * 9.81)
                = 5 x 10^-8

This is comparable to the Tajmar coupling (~10^-7).
If the coupling is weaker than ~10^-8, we won't see it with this setup.
```

---

## 13. Systematic Effects

| Effect | How it fools you | How to check |
|--------|-----------------|--------------|
| LN2 evaporation | Weight decreases steadily | Subtract linear baseline (Control A) |
| Thermal contraction | Scale reading shifts as dewar cools | Wait for thermal equilibrium |
| EM force on scale | Stray field pushes on metal scale pan | Use non-magnetic scale; mu-metal shield |
| Lorentz force on wires | Current-carrying wires in Earth's B-field | Twist wire pairs; symmetrical routing |
| Vibration from amplifiers | Mechanical coupling through wires/table | Decouple amps from scale; soft wire drape |
| Convection from LN2 | Cold air descends, changes buoyancy | Enclose in box; Control A captures this |
| Acoustic radiation pressure | Coils vibrate -> sound -> pressure on scale | Control C (single phase has same sound level) |
| Eddy currents in scale | Oscillating field induces currents in scale metal | Place mu-metal between assembly and scale |

The most dangerous systematic is **EM force on the scale itself**. The
precision scale contains metal parts that will interact with stray magnetic
fields. Mitigation: mu-metal sheet between the dewar and scale platform;
or place scale far below with a rigid rod connecting to the assembly.

---

## 14. Safety Notes

- **Liquid nitrogen:** Causes instant frostbite on skin contact. Use
  cryogenic gloves and safety glasses. Work in ventilated area (LN2
  displaces oxygen). Never seal LN2 in a closed container.
- **Electrical:** 12V DC is safe. If using RF amplifiers (>30V), use
  proper connectors and keep hands away.
- **Magnetic fields:** Coils at high current produce strong local B-fields.
  Keep pacemakers, magnetic media, and credit cards away.
- **YBCO:** Ceramic — brittle, can shatter if dropped. Fragments are sharp.
  Handle with care.
- **Pressure:** Styrofoam dewar is not pressure-rated. Never seal it.
  Always leave a vent for boil-off gas.

---

## 15. Shopping List

| # | Item | Qty | Cost (GBP) | Source |
|---|------|-----|-----------|--------|
| 1 | Enamelled copper wire 0.5mm (100m) | 1 | £12 | Amazon / eBay |
| 2 | Fiberglass tube 30mm OD (toroid former) | 1m | £8 | eBay / composites supplier |
| 3 | YBCO superconductor ring (40mm OD) | 1 | £50 | can-superconductors.com |
| 4 | Liquid nitrogen (5L) | 1 | £10 | BOC / university / welding supply |
| 5 | Styrofoam cooler box (small, for dewar) | 1 | £5 | Hardware store |
| 6 | STM32F411 Black Pill | 1 | £8 | AliExpress |
| 7 | AD9833 DDS module | 3 | £15 | AliExpress |
| 8 | TDA2030 amplifier board | 3 | £6 | AliExpress |
| 9 | 12V 5A power supply | 1 | £10 | Amazon |
| 10 | Precision scale (0.01g / 10mg resolution, 5kg capacity) | 1 | £30 | Amazon |
| 11 | Jumper wires, solder, tape, etc. | Misc | £10 | Any electronics shop |
| 12 | Mu-metal sheet (15x15cm, optional) | 1 | £40 | Magnetic Shield Corp / eBay |
| | **Total (without mu-metal)** | | **~£164** | |
| | **Total (with mu-metal)** | | **~£204** | |

### Optional Upgrades

| # | Item | Cost (GBP) | Purpose |
|---|------|-----------|---------|
| 13 | SI5351 clock generator (replaces AD9833) | £5 | Higher frequency range, cheaper |
| 14 | USB oscilloscope (Hantek 6022BE) | £40 | Verify phase relationships |
| 15 | Second YBCO ring (different size) | £50 | Test size dependence |
| 16 | Neodymium magnets (for Meissner check) | £5 | Verify YBCO is superconducting |
| 17 | Cryogenic thermocouple (Type T) | £10 | Monitor YBCO temperature |

---

## 16. Connection to Acoustic Levitation Concept

This experiment is the "Level 2" step from the acoustic levitation PDTP
analogy (see `docs/applications/acoustic_levitation_pdtp_analogy.md`):

```
Level 1: Classical acoustic levitation (wave physics intuition)
Level 2: EM phase array + superconductor (THIS EXPERIMENT)
Level 3: Full PDTP experiment (requires knowing m_cond)
```

The coil drum is also the laboratory-scale version of the phase-gradient
concept described in the 3Y rig scaling section (Section 15 of
`experiment_3y_rig.md`): a ring of coils at phase offsets, wrapped into
a toroid instead of arranged in a triangle.

**Key difference from 3Y:**
- 3Y tests Z3 topology (cancellation at Y-junction node)
- Coil drum tests U(1) traveling wave (continuous phase dragging)
- Both could work; they test different coupling mechanisms

If either experiment produces a positive result, the other should be
tested immediately to determine which mechanism (Z3 or U(1)) is active.

---

## 17. References

1. **Source:** [Linear induction motor — Wikipedia](https://en.wikipedia.org/wiki/Linear_induction_motor)
   Operating principle identical to coil drum (traveling magnetic field from phased coil array)
2. **Source:** [Traveling-wave tube — Wikipedia](https://en.wikipedia.org/wiki/Traveling-wave_tube)
   Slow-wave structure: phase velocity controllable by geometry
3. **Source:** [Three-phase electric power — Wikipedia](https://en.wikipedia.org/wiki/Three-phase_electric_power)
   Minimum 3 phases at 120 deg for smooth traveling wave
4. **Source:** [BCS theory — Wikipedia](https://en.wikipedia.org/wiki/BCS_theory)
   Collective gap frequency orders of magnitude below single-particle frequency
5. **Source:** [Yttrium barium copper oxide — Wikipedia](https://en.wikipedia.org/wiki/Yttrium_barium_copper_oxide)
   YBCO: T_c = 93K, cooled by liquid nitrogen
6. **Source:** [Macroscopic quantum phenomena — Wikipedia](https://en.wikipedia.org/wiki/Macroscopic_quantum_phenomena)
   Superconductor: all Cooper pairs in single quantum state
7. **Source:** Tajmar et al. (2006), "Measurement of Gravitomagnetic and Acceleration
   Fields Around Rotating Superconductors", AIP Conf. Proc. 880, 1071.
   Anomalous gravitomagnetic signal from spinning SC; coupling ~10^-7; unconfirmed.
8. **Source:** PDTP Part 29 — Decoupling energy ~10 kW/ton
9. **Source:** PDTP Part 34 — BEC self-consistency: c_s = c for any m_cond
10. **Source:** PDTP Part 37 — SU(3) condensate extension; Z3 vortex topology
11. **Inspiration:** Bob Lazar (1989) — 3 gravity amplifiers, saucer geometry.
    Speculative connection; included for motivation, not as evidence.
12. **Related experiment:** [experiment_3y_rig.md](experiment_3y_rig.md) — Z3 topology test
13. **Related concept:** [acoustic_levitation_pdtp_analogy.md](../docs/applications/acoustic_levitation_pdtp_analogy.md)
    — standing wave decoupling analogy
