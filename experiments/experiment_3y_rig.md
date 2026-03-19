# Experiment: 3Y Phase-Decoupling Test Rig

**Status:** Proposed — not yet built
**Date:** 2026-03-15
**Budget:** R1,500–R15,000 (~$90–$900 USD)
**Goal:** Scan for a resonant frequency at which coherent EM oscillation
in a Y-junction geometry produces a measurable gravitational anomaly.

**PDTP basis:**
- Three oscillators at 120° = Z3 topological defect (same as baryon, Part 37)
- At the Y-junction centre, three phases cancel: psi_1 + psi_2 + psi_3 = 0
- This forces alpha = cos(psi - phi) → 0 at the node
- If a resonant frequency exists, the effect is amplified (standing wave)
- Decoupling energy: ~10 kW/ton (Part 28b) — power is not the bottleneck

**Falsifiability:**
- If NO frequency produces ANY anomaly across the full scan range → mechanism
  is falsified (the coupling doesn't work this way)
- If a specific frequency produces a repeatable anomaly → breakthrough detection

**Inspiration:**
- Bob Lazar's description of 3 "gravity amplifiers" in Y-configuration
- Leidenfrost effect: thin incoherent boundary layer, not bulk destruction
- Acoustic levitation: standing waves create pressure nodes that suspend objects
- Musical resonance: standing waves amplify energy at specific frequencies

---

## Table of Contents

1. [Theory Summary](#1-theory-summary)
2. [What We Are Testing](#2-what-we-are-testing)
3. [Resonance and Amplification](#3-resonance-and-amplification)
4. [Copper Coils as Phase Drivers](#4-copper-coils-as-phase-drivers)
5. [Build Tiers](#5-build-tiers)
6. [Tier 1: Minimum Viable Rig (R1,500)](#6-tier-1-minimum-viable-rig-r1500)
7. [Tier 2: Upgraded Rig (R5,000)](#7-tier-2-upgraded-rig-r5000)
8. [Tier 3: Serious Rig (R15,000)](#8-tier-3-serious-rig-r15000)
9. [The Detector: DIY Torsion Balance](#9-the-detector-diy-torsion-balance)
10. [Software and Data Collection](#10-software-and-data-collection)
11. [Experimental Protocol](#11-experimental-protocol)
12. [What Success Looks Like](#12-what-success-looks-like)
13. [Safety Notes](#13-safety-notes)
14. [Shopping List](#14-shopping-list)
15. [Scaling Up: From Garage to Craft](#15-scaling-up-from-garage-to-craft)
16. [References](#16-references)

---

## 1. Theory Summary

### 1.1 The PDTP Decoupling Mechanism

Gravity in PDTP is phase-locking: alpha = cos(psi - phi), where psi is the
matter phase and phi is the spacetime condensate phase. When alpha = 1,
gravity is normal. When alpha = 0, matter is decoupled from spacetime.

To make alpha → 0, you drive psi away from phi. You do NOT break spacetime
(that requires Planck-scale energy ~10^8 J per bond). You detach matter
FROM spacetime — a much cheaper operation (~10 kW/ton sustained power).

**Source:** PDTP Part 28b (polarization language); Part 64 (temperature)

### 1.2 The Y-Junction Topology

Three oscillators at 120° phase offset create a Z3 topological defect:

```
        [Oscillator 1]
        phase = 0 deg
             |
             |
    ---------+----------
   /                     \
[Osc 2]              [Osc 3]
phase = 120 deg      phase = 240 deg
```

At the centre node: psi_1 + psi_2 + psi_3 = e^{i*0} + e^{i*2pi/3} + e^{i*4pi/3} = 0

This is the same topology as:
- A baryon (3 quarks connected by Y-shaped flux tubes, Part 37)
- The Z3 centre of SU(3) (colour confinement geometry)
- Bob Lazar's 3 "gravity amplifiers" in triangular arrangement

**Source:** PDTP Part 37 (SU(3) condensate extension); Part 23 (colour as phase)

### 1.3 The Leidenfrost Analogy

We are NOT trying to:
- Melt spacetime (requires T ~ 10^31 K)
- Break gravitational bonds (requires ~10^8 J per Planck-scale bond)
- Create a wormhole or warp bubble

We ARE trying to:
- Create a thin BOUNDARY LAYER of phase incoherence
- Like the Leidenfrost steam layer (droplet floats on its own vapour)
- Like acoustic levitation (standing wave pressure node suspends object)
- The hull vibrates; the vibration creates the decoupling layer

---

## 2. What We Are Testing

### 2.1 Primary Hypothesis

**There exists a frequency f_res at which coherent EM oscillation in a
Y-junction geometry produces a measurable reduction in gravitational
coupling (alpha < 1) at the centre node.**

### 2.2 What We Do NOT Know

- The resonant frequency f_res (could be Hz, kHz, MHz, GHz, or higher)
- The coupling mechanism (EM → condensate phase)
- The required power level
- Whether the effect is detectable at tabletop scale

### 2.3 What We DO Know

- The topology is correct (Z3, proven in Parts 37/53)
- The energy budget is feasible (~10 kW/ton from Part 28b)
- The phase-cancellation at the Y-node is exact (trigonometric identity)
- Resonance can amplify tiny effects by factors of 10^3–10^8

### 2.4 The Experimental Strategy

**Frequency sweep.** We don't derive f_res first — we scan for it.
Like tuning a radio: sweep across frequencies and listen for a signal.

If PDTP is correct, there exists SOME frequency where the gravimeter
twitches. If it never twitches across the full scan range — the
mechanism is falsified (or the effect is below our detection threshold).

---

## 3. Resonance and Amplification

### 3.1 Why Resonance Matters

The raw PDTP signal at tabletop power levels is predicted to be tiny
(alpha deviates from 1 by perhaps 10^-20 or less). We cannot detect this
directly. But resonance can amplify a tiny signal by enormous factors.

### 3.2 How Resonance Works (Music Analogy)

In music, resonance = energy accumulation at a specific frequency:

| System | Mechanism | Amplification |
|--------|-----------|---------------|
| Guitar body | Air cavity resonance, wood vibration modes | 10–20x |
| Organ pipe | Standing wave: length = wavelength/2 | ~100x |
| Wine glass | Circular standing wave at natural frequency | ~1000x (shatters!) |
| Violin string | Fundamental + harmonics build up | ~50x |
| Concert hall | Room modes at specific frequencies | ~10x |
| Laser cavity | Photons bounce between mirrors, coherent buildup | 10^6–10^8x |
| Acoustic horn | Impedance matching (small area → large area) | 10–50x |

The principle in every case:
1. Energy is injected at a specific frequency
2. The geometry causes constructive interference (wave adds to itself)
3. Energy builds up over many cycles until losses = input
4. At steady state: amplification = Quality factor Q

### 3.3 Quality Factor Q

The quality factor Q determines how much amplification you get:

```
Q = energy stored / energy lost per cycle
Amplification at resonance ~ Q
```

Typical Q values:
- Tuning fork: Q ~ 1,000
- Quartz crystal: Q ~ 10,000–100,000
- Superconducting RF cavity: Q ~ 10^9–10^11
- Copper RF cavity (room temperature): Q ~ 10,000–50,000

**For our rig:** even a modest Q of 1,000 means the effective signal is
amplified 1,000×. A quartz crystal oscillator at Q = 100,000 gives
100,000× amplification. This is why resonance makes the experiment viable.

### 3.4 Standing Waves in the Y-Frame

If the triangular frame has side length L, standing waves form when:

```
L = n * lambda / 2    (n = 1, 2, 3, ...)
```

For a frame with L = 30 cm:
- n=1: lambda = 60 cm → f = c_sound/lambda ~ 570 Hz (acoustic in air)
- n=1: lambda = 60 cm → f = c/lambda ~ 500 MHz (electromagnetic)

The acoustic and EM resonances are at VERY different frequencies because
sound travels at ~340 m/s and EM at 3×10^8 m/s. We should scan both
regimes.

### 3.5 The Lazar Connection

Bob Lazar described the S4 craft as having 3 "gravity amplifiers" that
amplified a "gravity A wave." In PDTP language:
- "Gravity A wave" = condensate phase oscillation
- "Amplifier" = resonant cavity that builds up phase oscillation energy
- "3 amplifiers" = Y-junction Z3 topology

The amplification mechanism is the same as a laser: coherent oscillation
bouncing inside a resonant structure, building up over many cycles.

**Source:** Lazar's public descriptions (1989 interviews). Speculative
connection — included for motivation, not as evidence.

---

## 4. Copper Coils as Phase Drivers

### 4.1 Why Coils, Not Speakers

Speakers push AIR molecules. Coils drive ELECTRONS directly.

In PDTP, the matter phase psi belongs to charged particles (electrons,
quarks). To drive psi, you need to couple to these particles directly.
An oscillating magnetic field from a coil does this:

```
Coil current oscillates at frequency f
    → oscillating B-field
    → oscillating force on electrons (Lorentz force: F = qv × B)
    → electrons oscillate → psi oscillates at frequency f
    → if f = f_res → alpha = cos(psi - phi) → 0 at node
```

### 4.2 Induction vs Radiation

Two regimes depending on frequency:

| Regime | Frequency | Mechanism | Coil type |
|--------|-----------|-----------|-----------|
| Near-field (induction) | Hz–MHz | Direct magnetic coupling | Wound copper coil |
| Far-field (radiation) | MHz–GHz | EM wave propagation | Antenna / RF cavity |
| Microwave | GHz–THz | Cavity resonance | Waveguide / horn |

**For the garage rig:** start with wound copper coils (near-field, Hz to MHz).
Cheap, easy to build, direct coupling to metal test mass.

### 4.3 Coil Design

Simple solenoid coil:
- Copper wire: 0.5–1.0 mm diameter (enamelled)
- Turns: 50–200 turns per coil
- Diameter: 5–10 cm
- Inductance: ~0.1–10 mH (depending on turns and diameter)
- Driven by: audio amplifier (Hz–kHz) or RF amplifier (kHz–MHz)

The coil IS the oscillator. Three coils at 120° = three phase drivers.

### 4.4 Phase Transfer to Hull (Scaled-Up Version)

For a full-scale craft (30m diameter):
- Hull made of conductive material (aluminium, copper-clad composite)
- Coils embedded in or wrapped around the hull
- Three coil arrays at 120° around the equator
- Driven by 3-phase power supply (standard industrial equipment!)

This is structurally identical to a **3-phase electric motor** — except
instead of spinning a rotor, you're driving phase oscillations in the hull.

```
3-phase motor:  3 coils at 120° → rotating magnetic field → rotor spins
3Y decoupler:   3 coils at 120° → rotating phase field → alpha → 0 at surface
```

The 3-phase power infrastructure already exists worldwide. Every
industrial facility has 3-phase power at 50/60 Hz. The technology to
DRIVE the coils is off-the-shelf. The unknown is the FREQUENCY.

---

## 5. Build Tiers

| Tier | Budget (ZAR) | Budget (USD) | Detector | Frequency range |
|------|-------------|-------------|----------|-----------------|
| 1 | R1,500 | $90 | MEMS accelerometer | 20 Hz – 20 kHz |
| 2 | R5,000 | $300 | DIY torsion balance + laser | 20 Hz – 100 kHz |
| 3 | R15,000 | $900 | Torsion balance + lock-in amp + vacuum | 1 Hz – 10 MHz |

---

## 6. Tier 1: Minimum Viable Rig (R1,500)

### 6.1 What You Build

Three piezoelectric transducers mounted at 120° on a triangular frame,
driven by an Arduino with 120° phase offset. A MEMS accelerometer at
the centre detects any anomaly.

### 6.2 Components

| Item | Specification | Source | Cost (ZAR) |
|------|--------------|--------|------------|
| 3x piezo transducers | 27 mm, 4 kHz resonance | Communica / AliExpress | R60 |
| Arduino Mega 2560 | 3 PWM outputs for 3-phase | Micro Robotics / DIYElectronics | R400 |
| 3x TDA2030 amplifier boards | 18W per channel | Communica / AliExpress | R120 |
| ADXL345 accelerometer | 3-axis, 13-bit, ±16g | Micro Robotics | R80 |
| 12V power supply | 3A minimum | Any electronics shop | R150 |
| Breadboard + jumper wires | Standard | Micro Robotics | R100 |
| Aluminium angle (25×25 mm) | 1m length, cut to 3×30 cm | Builders Warehouse | R80 |
| Small lead weight (test mass) | 200g fishing sinker | Fishing shop | R30 |
| USB cable + laptop | For data logging | (you have this) | R0 |
| Mounting screws, hot glue, etc. | Misc hardware | Builders Warehouse | R50 |
| **Total** | | | **~R1,070** |

### 6.3 Assembly Steps

**Step 1: Build the frame (30 minutes)**
1. Cut aluminium angle into 3 pieces of 30 cm each
2. Drill holes at each end (3 mm)
3. Bolt together into an equilateral triangle
4. The triangle should be rigid — no wobble

**Step 2: Mount the transducers (20 minutes)**
1. Hot-glue one piezo transducer at each vertex of the triangle
2. Orient them to radiate INWARD toward the centre
3. The centre of the triangle is where the Y-junction node will be

**Step 3: Wire the electronics (1 hour)**
1. Connect each piezo to its own TDA2030 amplifier board
2. Connect amplifier inputs to Arduino PWM pins (pins 9, 10, 11)
3. Connect ADXL345 accelerometer to Arduino I2C (SDA=20, SCL=21)
4. Power: 12V supply → amplifiers; USB → Arduino

**Step 4: Upload the firmware (30 minutes)**
```
Arduino sketch: 3_phase_sweep.ino

- Generate 3 sine waves with 120° phase offset
- Start at 20 Hz, sweep to 20 kHz in 1 Hz steps
- At each frequency: hold for 5 seconds, read accelerometer
- Log frequency + accelerometer XYZ to serial → laptop
- Flag any reading that deviates > 3 sigma from baseline
```

**Step 5: Place the test mass (5 minutes)**
1. Hang the lead sinker from a thin thread at the centre of the triangle
2. The thread attaches to a crossbar above the frame
3. The sinker should hang freely, touching nothing

**Step 6: Run the sweep (overnight)**
1. Place entire rig on stable surface (concrete floor ideal)
2. Cover with box to block drafts
3. Run at night when traffic vibration is minimal
4. Arduino sweeps 20 Hz → 20 kHz, 1 Hz steps, 5 sec each
5. Total sweep time: ~28 hours (20,000 steps × 5 sec)

### 6.4 Limitations

- MEMS accelerometer sensitivity: ~10^-4 g (not great)
- Piezo transducers are narrowband (resonant at 4 kHz, weak elsewhere)
- Air coupling (acoustic pressure) will dominate over any gravitational signal
- This tier is really a PROOF OF CONCEPT for the rig, not a serious search

---

## 7. Tier 2: Upgraded Rig (R5,000)

### 7.1 Upgrades Over Tier 1

| Upgrade | Why | Cost (ZAR) |
|---------|-----|------------|
| Replace piezos with copper coils | Direct EM coupling to test mass | R300 |
| DIY torsion balance | 10,000x more sensitive than MEMS | R500 |
| Laser pointer + photodiode | Read torsion angle optically | R200 |
| Broadband amplifier | Flat response 20 Hz – 100 kHz | R600 |
| Signal generator (AD9833 module) | Precise frequency control, 0.1 Hz resolution | R150 |
| Second Arduino (data acquisition) | Dedicated to reading detector | R400 |
| Shielding box (grounded metal) | Block EM interference from coils | R300 |

### 7.2 Building the Copper Coils

**Materials per coil:**
- 20m of 0.5 mm enamelled copper wire — R40
- PVC pipe section (25 mm diameter, 5 cm long) as former — R10
- Wind 100 turns onto the PVC former
- Inductance: ~0.5 mH per coil
- Impedance at 10 kHz: ~30 ohms (easy to drive with audio amp)

**Assembly:**
1. Wind 100 turns of 0.5 mm wire onto PVC former
2. Secure with tape or varnish
3. Solder leads to amplifier output
4. Mount at triangle vertices, axis pointing to centre

### 7.3 Building the Torsion Balance

This is the critical upgrade. A torsion balance can detect forces
~10,000x smaller than a MEMS accelerometer.

**Materials:**
- 30 cm thin tungsten wire (fishing leader, 0.1 mm) — R50
- Light aluminium rod (30 cm, from a BBQ skewer or thin dowel) — R10
- 2x small lead masses (50g each, fishing sinkers) — R30
- Small mirror (1 cm, from craft supplies or broken CD) — R10
- Laser pointer (red, <5 mW) — R40
- Photodiode (BPW34 or similar) — R20
- Mounting frame (wood or aluminium) — R100

**Assembly:**

```
    Mounting point (ceiling/frame)
         |
    [tungsten wire, 30 cm]
         |
    [===mirror===]           ← aluminium rod, 30 cm
    |            |
  [50g]        [50g]         ← lead masses at each end


    [Laser] ----→ mirror ----→ [photodiode on wall, 2m away]
```

1. Attach tungsten wire to the ceiling mount
2. Tie the aluminium rod horizontally to the bottom of the wire
3. Glue small masses to each end of the rod
4. Glue mirror to the centre of the rod
5. Aim laser at mirror; reflected beam hits photodiode 2m away
6. ANY tiny rotation of the rod moves the laser spot on the photodiode
7. At 2m throw: 1 microradian rotation = 2 micron spot movement

**Sensitivity estimate:**
- Tungsten wire torsion constant: ~10^-8 N⋅m/rad
- Minimum detectable torque: ~10^-11 N⋅m (limited by thermal noise)
- For test mass 1 cm from coil: minimum force ~ 10^-9 N
- This is ~10^-7 g on a 1 kg mass — 1000x better than MEMS

### 7.4 Experimental Setup

```
    [SHIELDING BOX - grounded aluminium]
    |                                    |
    |   [Coil 1]                         |
    |     \                              |
    |      \    [test mass on            |
    |       +--- torsion balance]        |
    |      /                             |
    |     /                              |
    |   [Coil 2]     [Coil 3]           |
    |                                    |
    |   [laser in] ---→ [mirror]         |
    |                    ↓               |
    |---------[photodiode out]-----------|
```

The shielding box is CRITICAL — it blocks EM forces from the coils
acting directly on the test mass. You only want to detect effects that
pass THROUGH the shielding (gravitational effects pass through everything;
EM effects are blocked by the grounded metal box).

**Control test:** Run the sweep with the shielding box and WITHOUT it.
Any signal that only appears WITHOUT the box is EM interference (not gravity).
Only signals that appear WITH the box are candidates for gravitational effects.

---

## 8. Tier 3: Serious Rig (R15,000)

### 8.1 Additional Upgrades

| Upgrade | Why | Cost (ZAR) |
|---------|-----|------------|
| Vacuum chamber (modified pressure cooker) | Eliminate air damping | R500 |
| Lock-in amplifier (DIY from Arduino Due) | Extract signal from noise | R800 |
| RF signal generator (SI5351 module) | Extend range to 10 MHz+ | R200 |
| Mu-metal sheet | Magnetic shielding | R1,500 |
| Quartz crystal oscillators (set of 10) | Fixed high-Q resonance points | R300 |
| Better photodiode (quadrant detector) | 2D spot tracking | R500 |
| Vibration isolation (inner tube + sand box) | Kill floor vibrations | R300 |

### 8.2 The Lock-In Amplifier (DIY)

This is the single most important upgrade. A lock-in amplifier extracts
a tiny signal buried in noise by correlating with a known reference.

**How it works:**
1. Modulate the coil drive: ON for 1 second, OFF for 1 second (1 Hz square wave)
2. Read the torsion balance continuously
3. Multiply the reading by the modulation signal (+1 when ON, -1 when OFF)
4. Average over many cycles (minutes to hours)
5. Anything NOT at the modulation frequency averages to zero
6. Only the signal correlated with the drive survives

**Noise rejection:** a 1-hour integration at 1 Hz modulation rejects noise
by a factor of sqrt(3600) ~ 60. A 10-hour overnight run: sqrt(36000) ~ 190.

This effectively multiplies your detector sensitivity by ~100-200x.

**Implementation:** Arduino Due (R600) with 12-bit ADC, running correlation
algorithm in firmware. Reference signal from the drive Arduino.

### 8.3 Vacuum Chamber

A modified pressure cooker with:
- Torsion balance mounted inside
- Feedthrough for laser (glass window)
- Feedthrough for photodiode wire (epoxy seal)
- Pumped down with a hand vacuum pump (R200) to ~10 mbar
- Eliminates air damping → Q of torsion balance increases 10-100x

### 8.4 Vibration Isolation

Stack of:
1. Heavy concrete block or paving slab (from garden, free)
2. Partially inflated car/bicycle inner tube (R50)
3. Sand-filled box (R100)
4. Experimental rig on top

This gives ~40 dB vibration isolation above 10 Hz. Essential for
overnight runs when trucks drive past.

---

## 9. The Detector: DIY Torsion Balance

### 9.1 Sensitivity Comparison

| Detector | Sensitivity | Cost | Ease |
|----------|------------|------|------|
| Smartphone accelerometer | ~10^-3 g | Free | Trivial |
| MEMS (ADXL355) | ~10^-6 g | R300 | Easy |
| DIY torsion balance | ~10^-8 g | R500 | Medium |
| Torsion + lock-in + vacuum | ~10^-10 g | R3,000 | Hard |
| Commercial superconducting | ~10^-12 g | R7,000,000 | Buy it |

The DIY torsion balance + lock-in amplifier + vacuum gets you within
a factor of 100 of a commercial superconducting gravimeter, for 0.04%
of the cost.

### 9.2 Calibration

Before searching for new physics, calibrate the torsion balance:

1. Place a known mass (e.g., 1 kg lead brick) at a known distance
2. Compute expected gravitational force: F = G*m1*m2/r^2
3. Measure the torsion balance deflection
4. This gives you the conversion factor: deflection per Newton

Example: 200g test mass, 1 kg calibration mass at 5 cm:
F = 6.67e-11 * 0.2 * 1.0 / 0.05^2 = 5.3e-9 N

This is detectable with the Tier 2/3 torsion balance. If you can measure
this Cavendish force, your detector is working correctly.

---

## 10. Software and Data Collection

### 10.1 Arduino Firmware

**Drive Arduino (generates 3-phase signal):**
```
Pseudocode:

for freq = START_FREQ to END_FREQ step STEP_SIZE:
    // Generate 3 sine waves at 120 degree offset
    for t = 0 to DWELL_TIME:
        phase1 = 2 * pi * freq * t
        phase2 = phase1 + 2 * pi / 3
        phase3 = phase1 + 4 * pi / 3

        DAC_out_1 = sin(phase1)
        DAC_out_2 = sin(phase2)
        DAC_out_3 = sin(phase3)

    // Modulation: alternate ON/OFF for lock-in
    for cycle = 0 to N_CYCLES:
        drive_on(freq, HALF_PERIOD)
        drive_off(HALF_PERIOD)

    serial_send(freq, "DONE")
```

**Detector Arduino (reads torsion balance):**
```
Pseudocode:

while True:
    voltage = ADC_read(photodiode_pin)
    modulation = digital_read(reference_pin)  // from drive Arduino

    // Lock-in multiplication
    if modulation == HIGH:
        accumulator += voltage
    else:
        accumulator -= voltage
    count += 1

    if count == SAMPLES_PER_BIN:
        lockin_signal = accumulator / count
        serial_send(timestamp, frequency, lockin_signal, raw_voltage)
        accumulator = 0
        count = 0
```

### 10.2 Python Analysis Script

```python
# analysis.py — process sweep data
# Reads CSV from Arduino serial log
# Plots: lock-in signal vs frequency
# Flags: any point > 3 sigma above noise floor

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("sweep_data.csv", delimiter=",")
freq = data[:, 0]
signal = data[:, 1]

# Compute noise floor (median absolute deviation)
noise = np.median(np.abs(signal - np.median(signal))) * 1.4826
threshold = 3 * noise

# Find candidates
candidates = np.where(np.abs(signal) > threshold)[0]

plt.figure(figsize=(14, 6))
plt.semilogy(freq, np.abs(signal), 'b-', linewidth=0.5)
plt.axhline(threshold, color='r', linestyle='--', label='3-sigma threshold')
for c in candidates:
    plt.axvline(freq[c], color='g', alpha=0.3)
plt.xlabel("Frequency (Hz)")
plt.ylabel("|Lock-in signal| (V)")
plt.title("3Y Frequency Sweep — Gravitational Anomaly Search")
plt.legend()
plt.savefig("sweep_result.png", dpi=150)
plt.show()

print(f"Noise floor: {noise:.2e} V")
print(f"3-sigma threshold: {threshold:.2e} V")
print(f"Candidates found: {len(candidates)}")
for c in candidates:
    print(f"  f = {freq[c]:.1f} Hz, signal = {signal[c]:.2e} V")
```

---

## 11. Experimental Protocol

### 11.1 Pre-Run Checklist

- [ ] Torsion balance calibrated with known mass (Cavendish test)
- [ ] Laser aligned on photodiode (check with oscilloscope: clean signal)
- [ ] 3-phase signal verified (oscilloscope: 3 channels at 120° offset)
- [ ] Shielding box grounded (wire from box to house earth)
- [ ] Vibration isolation in place (inner tube, sand box)
- [ ] Laptop connected, serial logging active
- [ ] Room temperature stable (close windows, no fans)
- [ ] Run at night (minimal traffic, footsteps, etc.)

### 11.2 Control Runs (Do These First!)

**Control A: Coils OFF, detector ON**
- Run for 2 hours with coils disconnected
- This gives you the BASELINE noise floor
- Any signal here is environmental (not from your rig)

**Control B: Coils ON, NO shielding**
- Run a frequency sweep without the metal shielding box
- Any signal here is likely EM interference (Lorentz force on test mass)
- This tells you what your EM contamination looks like

**Control C: Coils ON, WITH shielding, single phase (not 3-phase)**
- Run with only ONE coil active (no Y-junction topology)
- If the 3Y topology is special, single-phase should show nothing
- If signal appears with single phase too → not topology-dependent

### 11.3 Main Run

1. All controls passed → proceed
2. Coils ON, 3-phase, shielded, full sweep
3. Frequency range: depends on tier
   - Tier 1: 20 Hz – 20 kHz (overnight, ~28 hrs)
   - Tier 2: 20 Hz – 100 kHz (2 nights)
   - Tier 3: 1 Hz – 10 MHz (1 week with automation)
4. Dwell time per frequency: 5–30 seconds (longer = more sensitivity)
5. Log everything: frequency, detector reading, room temperature, time

### 11.4 If You Find Something

1. **DO NOT get excited yet.** Most anomalies are instrumental.
2. Repeat the measurement 5 times at the candidate frequency.
3. Run Control C (single phase) at that frequency — signal should vanish.
4. Remove the test mass — signal should vanish.
5. Rotate the entire rig 90° — signal should follow the rig, not the room.
6. Change the test mass material (lead → copper → wood) — does signal change?
7. If it passes ALL checks: you have a candidate detection.
8. Contact a university physics department for independent replication.

---

## 12. What Success Looks Like

### 12.1 Positive Result

A frequency f_res where:
- Signal appears with 3-phase Y-junction topology
- Signal vanishes with single-phase drive
- Signal vanishes when test mass is removed
- Signal persists through EM shielding
- Signal is repeatable across 5+ independent runs

This would be the first experimental evidence for gravitational
phase-coupling and would warrant immediate professional replication.

### 12.2 Null Result

No signal at any frequency across the full scan range. This means:
- **(a)** The effect is below our detection threshold (likely), OR
- **(b)** The coupling mechanism is different from what we assumed, OR
- **(c)** The decoupling mechanism does not work this way (falsification)

A null result is still valuable — it sets an upper limit on the
coupling strength at each frequency, which constrains the theory.

### 12.3 Systematic Effects to Watch For

| Effect | How it fools you | How to check |
|--------|-----------------|--------------|
| Acoustic coupling | Sound from piezos pushes test mass | Switch to coils (no sound) |
| EM interference | Lorentz force on test mass | Use shielding box |
| Thermal drift | Temperature changes during sweep | Log room temp; run at night |
| Floor vibration | Traffic, walking, wind | Vibration isolation; run at 3 AM |
| Electrical crosstalk | Drive signal leaks into detector ADC | Separate power supplies; twisted pair |
| Piezoelectric effect in quartz | If torsion wire is near coils | Keep wire far from coils |

---

## 13. Safety Notes

- **Electrical:** 12V DC is safe. If using RF amplifiers (>30V), use proper
  connectors and keep hands away from live terminals.
- **Laser:** Use <5 mW (Class 3R). Never look into the beam. Use a beam stop.
- **Lead:** Wash hands after handling lead sinkers. Do not eat lead.
- **Vacuum:** Pressure cooker under vacuum can implode if glass window fails.
  Use safety glasses. Do not exceed rated vacuum.
- **RF (Tier 3):** At MHz frequencies, keep away from RF amplifier output.
  RF burns are painful and heal slowly.

---

## 14. Shopping List

### 14.1 Tier 1 — Complete List

| # | Item | Qty | Unit (ZAR) | Total (ZAR) | Where to buy |
|---|------|-----|-----------|-------------|-------------|
| 1 | Piezo transducer 27mm | 3 | R20 | R60 | Communica / AliExpress |
| 2 | Arduino Mega 2560 | 1 | R400 | R400 | Micro Robotics |
| 3 | TDA2030 amp board | 3 | R40 | R120 | Communica |
| 4 | ADXL345 accelerometer | 1 | R80 | R80 | Micro Robotics |
| 5 | 12V 3A power supply | 1 | R150 | R150 | Electronics shop |
| 6 | Breadboard + wires | 1 | R100 | R100 | Micro Robotics |
| 7 | Aluminium angle 25mm | 1m | R80 | R80 | Builders Warehouse |
| 8 | Lead sinker 200g | 1 | R30 | R30 | Fishing / outdoor shop |
| 9 | Screws, glue, tape | Misc | R50 | R50 | Builders Warehouse |
| | **Tier 1 Total** | | | **R1,070** | |

### 14.2 Tier 2 — Additional Items

| # | Item | Qty | Unit (ZAR) | Total (ZAR) | Where to buy |
|---|------|-----|-----------|-------------|-------------|
| 10 | Enamelled copper wire 0.5mm (20m) | 3 | R40 | R120 | Communica / Mantech |
| 11 | PVC pipe 25mm (offcuts) | 3 | R10 | R30 | Builders Warehouse |
| 12 | Tungsten wire 0.1mm (1m) | 1 | R80 | R80 | Fishing shop (leader wire) |
| 13 | Laser pointer <5mW | 1 | R40 | R40 | Any shop |
| 14 | Photodiode BPW34 | 1 | R30 | R30 | Communica |
| 15 | Small mirror (1cm) | 1 | R20 | R20 | Craft shop / old CD |
| 16 | AD9833 signal generator | 1 | R150 | R150 | AliExpress |
| 17 | Audio amplifier (PAM8610) | 1 | R100 | R100 | Communica |
| 18 | Aluminium sheet (shielding) | 0.5m^2 | R200 | R200 | Metal supplier |
| 19 | Arduino Nano (detector) | 1 | R150 | R150 | Micro Robotics |
| 20 | Lead sinkers 50g | 2 | R15 | R30 | Fishing shop |
| 21 | Thin aluminium rod 30cm | 1 | R20 | R20 | Hardware store |
| 22 | Wood for mounting frame | Misc | R100 | R100 | Builders Warehouse |
| | **Tier 2 Additional** | | | **R1,070** | |
| | **Tier 2 Total (incl Tier 1)** | | | **R2,140** | |

### 14.3 Tier 3 — Additional Items

| # | Item | Qty | Unit (ZAR) | Total (ZAR) | Where to buy |
|---|------|-----|-----------|-------------|-------------|
| 23 | Arduino Due (12-bit ADC) | 1 | R600 | R600 | Micro Robotics |
| 24 | SI5351 clock generator | 1 | R100 | R100 | AliExpress |
| 25 | Mu-metal sheet (15×15cm) | 2 | R750 | R1,500 | Magnetic Shield Corp (import) |
| 26 | Pressure cooker (vacuum chamber) | 1 | R400 | R400 | Game / Makro |
| 27 | Hand vacuum pump | 1 | R200 | R200 | AutoZone / Midas |
| 28 | Glass window (sight glass) | 1 | R100 | R100 | Plumbing supply |
| 29 | Epoxy (vacuum-safe) | 1 | R80 | R80 | Builders Warehouse |
| 30 | Bicycle inner tube | 1 | R60 | R60 | Cycle shop |
| 31 | Sand (10kg bag) | 1 | R30 | R30 | Builders Warehouse |
| 32 | Concrete paving slab | 1 | R40 | R40 | Builders Warehouse |
| 33 | Quartz crystal oscillators (set) | 10 | R30 | R300 | AliExpress |
| 34 | Quadrant photodiode | 1 | R500 | R500 | Thorlabs / import |
| | **Tier 3 Additional** | | | **R3,910** | |
| | **Tier 3 Total (incl Tier 1+2)** | | | **R6,120** | |

---

## 15. Scaling Up: From Garage to Craft

### 15.1 The Progression

| Stage | Scale | Budget | What it proves |
|-------|-------|--------|---------------|
| Garage rig | 30 cm triangle | R2,000–R6,000 | Detection of resonant frequency |
| Lab rig | 3 m triangle, higher power | R100,000 | Quantitative coupling measurement |
| Prototype shell | 3 m sphere with coils | R1,000,000 | Leidenfrost layer formation |
| Test craft | 10 m hull, 3-phase coils | R50,000,000+ | Gravitational anomaly on craft |
| Full craft | 30 m hull | ??? | Flight (if everything works) |

Each stage validates the next. You never build the bigger one until the
smaller one works.

### 15.2 Copper Coils on a Hull (Phase Transfer)

For the full-scale craft, the hull itself becomes the resonant cavity:

```
Cross-section of 30m craft hull:

    ╭────────────────────────────────╮
    │  Copper coil array (120°)  [1] │
    │      ╲                  ╱      │
    │        ╲    INTERIOR  ╱        │
    │          ╲          ╱          │
    │    [2]     ╲      ╱     [3]    │
    │  Coil       ╲  ╱       Coil   │
    │  array       ╳        array   │
    │  (240°)    ╱  ╲       (0°)    │
    │          ╱      ╲              │
    │        ╱    CRAFT  ╲           │
    │      ╱    INTERIOR   ╲         │
    │    ╱                    ╲      │
    ╰────────────────────────────────╯
          Conductive hull (Al or Cu)
```

The hull is the "wine glass." The coils are the "singer's voice."
At the resonant frequency, the entire hull vibrates coherently in the
3-phase pattern, creating a standing wave where alpha → 0 on the surface.

### 15.3 Three-Phase Industrial Connection

A 30m craft with 3 coil arrays is electrically identical to a
3-phase induction motor — just spherical instead of cylindrical.

- Standard 3-phase power: 380V, 50 Hz (South Africa)
- Variable frequency drive (VFD): adjusts frequency from 0 to 500+ Hz
- Higher frequencies: RF amplifier replaces VFD

The DRIVE ELECTRONICS are commodity industrial equipment. The only
unknown is the frequency setting on the VFD.

---

## 16. References

1. **Source:** PDTP Part 37 — Z3 vortex topology (Y-junction geometry)
2. **Source:** PDTP Part 28b — Decoupling energy ~10 kW/ton
3. **Source:** PDTP Part 64 — Temperature, J = E_Planck/(4*pi)
4. **Source:** [Cavendish experiment — Wikipedia](https://en.wikipedia.org/wiki/Cavendish_experiment)
5. **Source:** [Lock-in amplifier — Wikipedia](https://en.wikipedia.org/wiki/Lock-in_amplifier)
6. **Source:** [Acoustic levitation — Wikipedia](https://en.wikipedia.org/wiki/Acoustic_levitation)
7. **Source:** [Kosterlitz-Thouless transition — Wikipedia](https://en.wikipedia.org/wiki/Kosterlitz%E2%80%93Thouless_transition)
8. **Source:** [Three-phase electric power — Wikipedia](https://en.wikipedia.org/wiki/Three-phase_electric_power)
9. **Inspiration:** Bob Lazar (1989) — 3 gravity amplifiers in Y-configuration.
   Speculative connection; included for motivation, not as evidence.
10. **Inspiration:** Leidenfrost effect — thin boundary layer decoupling
11. **Source:** Ryazanov, Providukhina, Sibgatullin & Ermanyuk (2021), "Biharmonic Attractors
    of Internal Gravity Waves", *Fluid Dynamics* 56(3), 403-412.
    DOI: 10.1134/S0015462821030046. Open access.
    Relevance: biharmonic forcing of wave attractors produces triad resonance cascades
    and beating regimes with order-of-magnitude energy bursts — directly relevant to
    multi-frequency forcing in the 3Y geometry.
