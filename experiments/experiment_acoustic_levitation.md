# Experiment: Acoustic Standing Wave Levitation — Inverted as Decoupling Mechanism

**Status:** Proposed — not yet built
**Date:** 2026-03-16
**Budget:** R500–R3,000 (~$30–$180 USD)
**Goal:** Build a working acoustic levitation rig to demonstrate the wave-node
physics that underpins PDTP's decoupling concept, then explore the "inverted"
configuration where the object itself drives the standing wave.

**PDTP basis:**
- In acoustic levitation, an object sits PASSIVELY at a pressure node — zero net
  force from the standing wave. No contact, no propulsion, no exhaust.
- The PDTP inversion: the object (craft) GENERATES the standing wave in the
  spacetime condensate phi, creating its own node where alpha = cos(psi - phi) = 0
- This experiment is the **Level 1 analog** from the experimental ladder
  (see `docs/applications/acoustic_levitation_pdtp_analogy.md`)
- Purpose: build physical intuition about wave-node trapping before attempting
  EM-to-gravitational coupling experiments (3Y rig, coil drum)

**Falsifiability (of the analogy, not PDTP itself):**
- This experiment demonstrates KNOWN acoustic physics — it will work
- The PDTP question is whether the analogy extends to the gravitational condensate
- A successful acoustic rig proves the MECHANISM (standing wave node trapping);
  the 3Y rig and coil drum test the APPLICATION (gravitational condensate coupling)

**How this fits with the other experiments:**

| Experiment | What it tests | Medium | Level |
|------------|--------------|--------|-------|
| **Acoustic levitation (THIS)** | Wave-node trapping mechanism | Air (pressure waves) | Level 1: analog |
| 3Y Rig | Z3 topological coupling | EM field + lead test mass | Level 2: EM-gravity |
| Coil Drum | U(1) traveling wave coupling | EM field + YBCO superconductor | Level 2: EM-gravity |
| Full PDTP experiment | Direct condensate measurement | Spacetime condensate | Level 3: direct |

---

## Table of Contents

1. [Theory: How Acoustic Levitation Works](#1-theory-how-acoustic-levitation-works)
2. [The PDTP Inversion](#2-the-pdtp-inversion)
3. [Why Build This First](#3-why-build-this-first)
4. [Build Specification — Standard Rig](#4-build-specification--standard-rig)
5. [Build Specification — Inverted Rig](#5-build-specification--inverted-rig)
6. [Electronics and Control](#6-electronics-and-control)
7. [Assembly Steps](#7-assembly-steps)
8. [Experimental Protocol](#8-experimental-protocol)
9. [The Inversion Experiment](#9-the-inversion-experiment)
10. [What to Observe and Measure](#10-what-to-observe-and-measure)
11. [Connection to PDTP Decoupling](#11-connection-to-pdtp-decoupling)
12. [Why the Saucer Shape](#12-why-the-saucer-shape)
13. [Safety Notes](#13-safety-notes)
14. [Shopping List](#14-shopping-list)
15. [References](#15-references)

---

## 1. Theory: How Acoustic Levitation Works

### 1.1 Standing Waves

When a sound wave bouncing between a transducer and a reflector interferes
with itself, it creates a **standing wave** — fixed positions of zero pressure
oscillation (nodes) and maximum pressure oscillation (antinodes):

```
Transducer (top)
  ||||||||||||||||||||
  ~  ANTINODE (max pressure oscillation)
  -  NODE (zero pressure oscillation)       <-- object trapped here
  ~  ANTINODE
  -  NODE                                    <-- another trapping point
  ~  ANTINODE
  ||||||||||||||||||||
Reflector (bottom)
```

At a pressure node, the acoustic radiation pressure from above equals
the pressure from below — the net acoustic force is zero. A small object
placed at a node is trapped: pushed back if it drifts up or down.

**Source:** [Acoustic levitation — Wikipedia](https://en.wikipedia.org/wiki/Acoustic_levitation)

### 1.2 The Physics of Node Trapping

The restoring force near a node is:

```
F = -(dU/dx)                                                    [KNOWN]

where U is the acoustic potential:
    U = -(V_object / (4 * rho * c^2)) * [f1 * <p^2> - (3/2) * f2 * rho * <v^2>]

    V_object = volume of the levitated object
    rho = air density (~1.2 kg/m^3)
    c = speed of sound (~343 m/s)
    <p^2> = time-averaged pressure squared (varies with position)
    <v^2> = time-averaged velocity squared (varies with position)
    f1, f2 = compressibility and density contrast functions
```

For a rigid, dense object in air: f1 ~ 1, f2 ~ 1. The object is pushed
toward the pressure node (minimum of U).

**Source:** Gor'kov (1962), "On the forces acting on a small particle in
an acoustical field in an ideal fluid", Soviet Physics - Doklady 6, 773.

### 1.3 Key Parameters

| Parameter | Typical value | Why it matters |
|-----------|--------------|----------------|
| Frequency | 20–40 kHz | Ultrasonic (inaudible); wavelength ~8–17 mm |
| Wavelength | lambda = c/f = 343/28000 ~ 12 mm | Sets node spacing: lambda/2 ~ 6 mm |
| Node spacing | lambda/2 ~ 6 mm | Distance between trapping positions |
| Max object size | < lambda/2 ~ 6 mm | Object must be smaller than half-wavelength |
| Transducer power | 1–10 W | Enough for small (< 1g) objects |
| Levitation force | ~10^-3 N per watt | Lifts ~100 mg per watt in air |

### 1.4 What Can Be Levitated

Small, light objects float easily in acoustic standing waves:

- Styrofoam beads (1–3 mm)
- Water droplets (1–2 mm)
- Small insects (ants, flies)
- Grains of sand or salt
- Small electronic components (SMD resistors)
- Liquid droplets (ethanol, water, glycerin)

Maximum mass depends on transducer power and frequency. At 28 kHz with
a 10W transducer array, objects up to ~1 gram can be levitated.

---

## 2. The PDTP Inversion

### 2.1 Standard vs Inverted

| Feature | Standard acoustic levitation | PDTP inversion (Goal 2) |
|---------|------------------------------|-------------------------|
| Wave source | External transducer | The object/craft itself |
| Object role | Passive (sits at node) | Active (generates the wave) |
| Medium | Air (pressure waves) | Spacetime condensate (phase waves in phi) |
| Node position | Fixed by transducer/reflector | Created by object's own oscillation |
| Coupling | Acoustic radiation pressure | Phase-locking: alpha = cos(psi - phi) |
| At the node | Acoustic force = 0 | Gravitational coupling alpha = 0 |
| What is suspended | Small bead in air | Craft in gravitational field |

### 2.2 The Key Insight

In standard acoustic levitation, the object does nothing — it just sits
there while external waves hold it up. The object doesn't need to oscillate,
radiate, or do any work.

The PDTP inversion says: what if the object IS the transducer? What if
matter can drive oscillations in the gravitational condensate field phi,
creating its own standing wave pattern? Then the object sits at its own
node — gravitationally decoupled from the surrounding spacetime.

```
Standard:   [Transducer] ~~~~ NODE ~~~~ [Reflector]
                            |
                         [Object]  (passive)

Inverted:              [Object/Craft]
                      /      |      \
                ~~~~~ NODE SURFACE ~~~~~  (self-generated)
                     (alpha = 0 here)
```

### 2.3 The Acoustic Experiment Tests This

We can partially test the inversion concept using acoustic physics alone:

1. **Standard configuration:** External transducers levitate a passive bead
   → demonstrates node trapping (the basic mechanism)

2. **Inverted configuration:** Attach a tiny piezo transducer TO the bead
   (or to a small platform). The bead/platform drives its own acoustic wave.
   Can it create a standing wave that generates its own trapping node?

The inverted acoustic case is challenging (the transducer needs a reflector
or second surface to form a standing wave), but it demonstrates the CONCEPT
that a self-oscillating object can interact with its surrounding medium
through standing wave patterns.

---

## 3. Why Build This First

### 3.1 Physical Intuition

Most people have never seen acoustic levitation in person. Building the rig
gives immediate, visceral understanding of:

- How standing waves form
- How objects are trapped at nodes (zero-force equilibrium)
- How the trapping force depends on frequency (resonance!)
- How geometry determines node positions
- How the system responds to perturbations (stability)

This intuition transfers directly to the PDTP picture: replace "air pressure"
with "condensate phase", and "acoustic node" with "decoupling surface".

### 3.2 Cheap and Fast

The entire rig costs R500–R3,000 and can be built in an afternoon.
No liquid nitrogen, no superconductors, no precision scales.
Just ultrasonic transducers, a driver board, and some styrofoam beads.

### 3.3 Guaranteed to Work

Acoustic levitation is well-established physics. The rig WILL levitate
objects if built correctly. This gives a working baseline before moving
to the speculative experiments (3Y, coil drum).

### 3.4 Experimental Skills

Building the acoustic rig teaches:
- Wiring transducer arrays
- Driving piezoelectric elements
- Aligning transducer/reflector pairs
- Observing resonance phenomena
- Basic frequency tuning

All of these skills transfer to the 3Y rig and coil drum builds.

---

## 4. Build Specification — Standard Rig

### 4.1 Concept: Single-Axis Levitator

The simplest acoustic levitator: one transducer on top, one reflector
(or second transducer) on the bottom, facing each other. The standing
wave forms between them.

```
Side view:

    [Transducer]  (28 kHz ultrasonic)
         |
    ~ ~ ~ ~ ~ ~   antinode
    - - - - - -   NODE  <-- bead floats here
    ~ ~ ~ ~ ~ ~   antinode
    - - - - - -   NODE  <-- another bead here
    ~ ~ ~ ~ ~ ~   antinode
         |
    [Reflector]   (flat aluminium disc)

    Distance: ~3-5 half-wavelengths (18-30 mm at 28 kHz)
```

### 4.2 Multi-Transducer Array (Upgraded)

For stronger trapping and 3D control, use an array of transducers in a
bowl or hemisphere shape (the TinyLev design):

```
Top view of transducer array (one hemisphere):

         o o o
       o o o o o
      o o o o o o
       o o o o o
         o o o

    o = 28 kHz ultrasonic transducer (HC-SR04 type)
    72 transducers total (36 top + 36 bottom)
```

**Source:** Marzo et al. (2017), "TinyLev: A multi-emitter single-axis
acoustic levitator", Review of Scientific Instruments 88, 085105.
Open-source hardware design available on GitHub.

### 4.3 Key Dimensions

| Parameter | Simple rig | Array rig |
|-----------|-----------|-----------|
| Transducers | 1 (+ reflector) | 72 (36 + 36) |
| Frequency | 28 kHz or 40 kHz | 40 kHz |
| Transducer-reflector gap | 18–30 mm | 60–100 mm |
| Number of trapping nodes | 2–4 | 3–8 |
| Maximum object size | ~3 mm | ~5 mm |
| Trapping force | ~10^-4 N | ~10^-3 N |
| Cost | R500 | R3,000 |

---

## 5. Build Specification — Inverted Rig

### 5.1 Concept: Self-Oscillating Platform

After demonstrating standard levitation, attempt the inversion:

**Version A: Reflector-assisted inversion**
1. Mount a small piezo disc (10 mm) on a lightweight platform (balsa wood, 3g)
2. Suspend the platform from a thin thread
3. Place a reflector disc 6 mm below the platform
4. Drive the piezo at 40 kHz
5. The platform emits ultrasound downward -> reflects -> standing wave forms
6. A small bead placed BETWEEN the platform and reflector levitates
7. The platform now experiences an UPWARD reaction force from the standing wave

This is "inverted" because the SOURCE of the wave is ON the object, not external.
The platform pushes itself up by generating a standing wave below it.

```
    [Thread]
       |
    [Platform + piezo transducer]  (self-oscillating, 3g)
       |
    ~ ~ ~ ~ ~ ~   standing wave (generated by platform)
    - - - - -    NODE
    ~ ~ ~ ~ ~ ~
       |
    [Reflector]
```

**Version B: Counter-propagating (no reflector)**
1. Mount two piezo discs on opposite sides of a platform (top and bottom)
2. Drive both at the same frequency, same phase
3. The platform radiates symmetrically up and down
4. If placed between two reflectors (floor + ceiling), standing waves form
5. The platform experiences a net force toward the nearest node

This version has the platform driving its own standing wave in BOTH
directions — closest to the PDTP concept where the craft generates a
symmetric decoupling shell.

### 5.2 What to Expect

The inverted rig will NOT levitate the platform (the reaction force from
a small piezo in air is tiny — micronewtons, not enough to lift 3 grams).

What it WILL demonstrate:
- The platform generates a measurable acoustic field
- A standing wave forms between the platform and the reflector
- Beads CAN be trapped in the standing wave created by the platform
- The platform experiences a small upward reaction force (measurable
  with a sensitive balance or by observing thread tension changes)

The point is to demonstrate the CONCEPT: a self-oscillating object can
create standing waves that interact with its surroundings, generating
forces on itself. The PDTP extension is that these forces could, in
principle, include gravitational decoupling forces.

---

## 6. Electronics and Control

### 6.1 Simple Rig (1 transducer + reflector)

| Component | Function | Cost (ZAR) |
|-----------|----------|------------|
| HC-SR04 transducer (harvested) | 40 kHz ultrasonic emitter | R30 |
| L298N H-bridge module | Drive transducer at 40 kHz | R60 |
| Arduino Nano | Generate 40 kHz square wave | R100 |
| 5V 2A USB power supply | Power everything | R50 |
| Aluminium disc (reflector) | 30 mm diameter, 3 mm thick | R20 |
| Adjustable mount (3D printed or wood) | Set transducer-reflector gap | R50 |
| Styrofoam beads | Test objects for levitation | R20 |
| **Total** | | **~R330** |

### 6.2 Array Rig (72 transducers — TinyLev)

| Component | Function | Cost (ZAR) |
|-----------|----------|------------|
| 72x 40 kHz ultrasonic transducers | Emitter array (2 hemispheres) | R720 |
| 2x L298N H-bridge modules | Drive top and bottom arrays | R120 |
| Arduino Nano | Generate 40 kHz + phase control | R100 |
| 3D-printed hemisphere holders | Mount transducers in bowl shape | R300 |
| 5V 5A power supply | Drive all transducers | R100 |
| Styrofoam beads | Test objects | R20 |
| Jumper wires, solder | Wiring | R50 |
| **Total** | | **~R1,410** |

**Note:** The 40 kHz transducers are the same ones used in HC-SR04
ultrasonic distance sensors. You can harvest them from cheap HC-SR04
modules (~R10 each) or buy bare transducers from AliExpress (~R8 each).

### 6.3 Driver Circuit

The transducer needs a 40 kHz square wave at 10–20 Vpp:

```
Arduino Nano (pin 9: 40 kHz PWM)
    |
    v
L298N H-bridge (converts 5V logic to 12V drive)
    |
    v
Transducer (40 kHz piezo, driven at resonance)
```

Arduino generates 40 kHz using Timer1:

```
// Arduino 40 kHz generator
void setup() {
    pinMode(9, OUTPUT);
    // Timer1: Fast PWM, TOP = ICR1
    TCCR1A = _BV(COM1A0);        // Toggle OC1A on compare match
    TCCR1B = _BV(WGM12) | _BV(CS10);  // CTC mode, no prescaler
    OCR1A = 199;                  // 16 MHz / (2 * 200) = 40 kHz
}
void loop() {}
```

For the array rig, ALL transducers in each hemisphere are wired in
parallel (same phase). The two hemispheres are driven with opposite
phase (180 degrees apart) to create constructive interference at the centre.

### 6.4 Inverted Rig Electronics

Same as simple rig, but the transducer is mounted ON the platform
instead of on a fixed mount:

| Additional component | Function | Cost (ZAR) |
|---------------------|----------|------------|
| 10 mm piezo disc (lightweight) | Mounted on platform, emits downward | R15 |
| Balsa wood platform (30x30x2 mm) | Lightweight carrier (~3g) | R10 |
| Fine thread (nylon fishing line) | Suspend platform | R10 |
| Thin enamelled wire (0.1 mm) | Carry signal to piezo without adding weight | R20 |
| **Additional total** | | **~R55** |

---

## 7. Assembly Steps

### 7.1 Simple Rig (1 hour)

**Step 1: Harvest the transducer (10 min)**
1. Take an HC-SR04 ultrasonic module
2. Desolder the TRANSMITTER transducer (marked T or TX)
3. Note polarity (+/- on the casing)

**Step 2: Build the mount (20 min)**
1. Cut two pieces of wood/aluminium angle, 10 cm tall
2. Mount them vertically on a base board, 3 cm apart
3. Fix the transducer facing DOWN at the top of one post
4. Fix the reflector (aluminium disc) facing UP at the bottom of the other post
5. Make the reflector height adjustable (slot + bolt, or stack of washers)

**Step 3: Wire the driver (15 min)**
1. Connect Arduino pin 9 to L298N input IN1
2. Connect Arduino pin 10 to L298N input IN2 (for complementary drive)
3. Connect L298N outputs OUT1 and OUT2 to transducer leads
4. Power L298N with 12V (or 9V battery for portability)
5. Power Arduino via USB

**Step 4: Tune the gap (15 min)**
1. Upload the 40 kHz sketch to Arduino
2. Power on
3. Drop tiny styrofoam beads between the transducer and reflector
4. Adjust the reflector height until beads hover at a node
5. Optimal gap: integer multiples of lambda/2 = 4.3 mm (at 40 kHz)
6. Try gaps of ~8.5 mm (2 nodes), ~12.8 mm (3 nodes), ~17 mm (4 nodes)

### 7.2 Array Rig (Half day)

Follow the TinyLev open-source build instructions:

**Source:** Marzo et al., TinyLev — available at
[instructables.com/Acoustic-Levitator](https://www.instructables.com/Acoustic-Levitator/)

Key steps:
1. 3D print two hemisphere holders (STL files from TinyLev project)
2. Solder 36 transducers into each hemisphere (all parallel, matching polarity)
3. Wire hemispheres to L298N (top = channel A, bottom = channel B)
4. Upload TinyLev Arduino sketch (handles phase inversion automatically)
5. Position hemispheres facing each other, ~10 cm apart
6. Drop styrofoam beads — they should trap at multiple nodes

### 7.3 Inverted Rig (Add 30 min to simple rig)

After the simple rig works:

1. Glue a 10 mm piezo disc to the underside of a balsa wood platform
2. Solder 0.1 mm enamelled wire to the piezo leads
3. Suspend the platform from a thread tied to a crossbar above the rig
4. Route the thin wires down the thread (minimal added weight/tension)
5. Connect wires to the same L298N driver
6. Place the reflector 4-8 mm below the platform
7. Power on at 40 kHz
8. Drop tiny beads between the platform and reflector

---

## 8. Experimental Protocol

### 8.1 Standard Levitation Demonstration

**Objective:** Confirm that standing wave nodes trap objects.

1. Set up simple rig with transducer-reflector gap = 8.5 mm (2 nodes)
2. Power on at 40 kHz
3. Drop styrofoam beads (1-2 mm) from above using tweezers
4. Observe beads trapped at nodes
5. Record with phone camera (slow motion if available)
6. Gently blow on the bead — observe it return to the node (restoring force)
7. Vary the gap and observe nodes appearing/disappearing

**What to record:**
- Number of nodes vs gap distance
- Approximate restoring force (how hard you can blow before bead escapes)
- Largest object that can be levitated (try grains of salt, sand, etc.)

### 8.2 Frequency Sweep

**Objective:** Demonstrate resonance — the trapping force peaks at the
transducer's resonant frequency.

1. Modify the Arduino sketch to sweep frequency from 35 to 45 kHz
2. At each frequency, observe the levitated bead's stability
3. At resonance (~40 kHz), the bead is most strongly trapped
4. Off-resonance, the bead falls (insufficient force)

This directly demonstrates the PDTP principle: **the effect only works
at a specific frequency** (resonance). The 3Y rig and coil drum
experiments will scan for a similar resonance, but in the EM-gravitational
domain.

### 8.3 Node Stability Test

**Objective:** Demonstrate that nodes are stable equilibria.

1. Levitate a bead at a node
2. Use a thin needle to push the bead slightly off-node
3. Release — bead snaps back to the node
4. Push harder — bead escapes to the next node (or falls)
5. Map the trapping "basin" — how far can you push before escape?

This demonstrates that **nodes are attractors** — the bead is pulled back
to the equilibrium position. In PDTP, the decoupling surface (alpha = 0)
would similarly be a stable attractor if the analogy holds.

---

## 9. The Inversion Experiment

### 9.1 Setup

After demonstrating standard levitation, switch to the inverted rig:

1. Remove the external transducer from the standard rig
2. Hang the platform (with piezo on its underside) from a thread
3. Place the reflector below the platform
4. Connect the platform's piezo to the driver
5. Power on at 40 kHz

### 9.2 What to Test

**Test 1: Does the platform generate a standing wave?**
- Drop beads between the platform and reflector
- If they levitate, the platform IS generating a standing wave
- The platform is now a self-oscillating wave source (like a PDTP craft)

**Test 2: Does the platform experience a reaction force?**
- Observe the thread: does it go slack or taut when the wave is on?
- Use a milligram scale: place the platform on the scale, reflector below
- Compare weight readings: piezo ON vs piezo OFF
- Any upward force on the platform = self-generated acoustic lift
- Expected magnitude: micronewtons (probably below scale resolution,
  but worth trying)

**Test 3: Can the platform "levitate itself" (even partially)?**
- This is the ambitious test — the platform reduces its own effective weight
- Almost certainly NO with a simple piezo in air (insufficient force)
- BUT: if you use the array rig configuration and mount the entire
  upper array on a thread + scale, you can measure the reaction force
  on the array when it levitates objects below it (Newton's 3rd law:
  the levitated object pushes back on the source)

### 9.3 Why the Inversion Matters for PDTP

Even if the platform can't fully "levitate itself" acoustically
(the forces are too weak), the experiment demonstrates:

1. **A self-oscillating object can create standing waves in its medium**
2. **Those standing waves create forces (nodes trap objects)**
3. **The object itself experiences a reaction force** (Newton's 3rd law)
4. **The effect depends on frequency** (only works near resonance)

These are the SAME four properties that PDTP predicts for gravitational
decoupling. The acoustic experiment proves the mechanism works in a wave
medium — the open question is whether the gravitational condensate
behaves the same way.

---

## 10. What to Observe and Measure

### 10.1 Qualitative Observations

| Observation | What it demonstrates | PDTP parallel |
|-------------|---------------------|---------------|
| Bead hovers at node | Wave-node trapping is real | alpha = 0 at node surface |
| Bead returns after push | Node is a stable equilibrium | Decoupling surface is self-restoring |
| Bead falls off-resonance | Effect requires specific frequency | Must find f_res for condensate |
| Multiple beads at multiple nodes | Nodes form a regular pattern | Decoupling shell has specific geometry |
| Bead trapped with no contact | No mechanical support needed | Craft needs no reaction mass |
| Inverted: platform generates wave | Self-oscillating source works | Craft generates own decoupling field |

### 10.2 Quantitative Measurements

| Measurement | How to measure | Expected value |
|-------------|---------------|----------------|
| Node spacing | Ruler between trapped beads | lambda/2 = 4.3 mm at 40 kHz |
| Resonant frequency | Sweep, find max trapping force | 40 +/- 2 kHz (transducer spec) |
| Trapping force | Calibrated air jet to dislodge bead | ~10^-4 N at 1W |
| Maximum object mass | Try progressively heavier objects | ~0.5 g at 10W |
| Reaction force (inverted) | Milligram scale reading | < 1 mg (probably below resolution) |
| Standing wave pattern (inverted) | Bead trapped between platform and reflector | Same node spacing as standard |

---

## 11. Connection to PDTP Decoupling

### 11.1 The Analogy Map

```
ACOUSTIC                          PDTP
========                          ====
Air molecules                     Condensate field phi
Pressure waves                    Phase waves in phi
Speed of sound (343 m/s)          Speed of light (3 x 10^8 m/s)
Transducer frequency (40 kHz)     Condensate resonance (omega_gap, unknown)
Pressure node (P = 0)             Phase node (alpha = cos(psi-phi) = 0)
Acoustic radiation pressure       Phase-locking force (g * sin(psi-phi))
Node spacing (lambda/2)           Decoupling shell thickness
Object at node (levitates)        Craft at node (decoupled from gravity)
Reflector                         Condensate boundary / self-reflection
```

### 11.2 What Carries Over

| Property | Acoustic | PDTP | Confidence |
|----------|----------|------|------------|
| Nodes exist in standing waves | YES (proven) | Expected | HIGH |
| Nodes are stable equilibria | YES (proven) | Expected | HIGH |
| Force depends on frequency | YES (proven) | Expected | HIGH |
| Self-oscillation creates waves | YES (proven) | Unknown | MEDIUM |
| Self-generated node traps source | Weak (in air) | Speculative | LOW |
| No external support needed | YES (proven) | Expected | HIGH |

### 11.3 What Does NOT Carry Over

- **Medium:** Air is compressible and lossy; the condensate is (assumed)
  incompressible and nearly lossless
- **Coupling:** Acoustic coupling is mechanical (pressure on surface);
  PDTP coupling is phase-locking (quantum coherence)
- **Scale:** Acoustic works at cm scale; PDTP decoupling may require
  Planck-scale coherence (10^-35 m)
- **Self-levitation:** In air, the reaction force is tiny compared to
  gravity; in PDTP, the claim is that the coupling force IS gravity
  (so complete decoupling would mean zero weight, not just reduced)

### 11.4 The Saucer Connection

Bob Lazar described the S4 craft as having 3 "gravity amplifiers" that
generated "gravity A waves" (speculative; included for motivation only).

The acoustic analogy suggests:
- "Gravity amplifiers" = resonant transducers driving the condensate
- "Gravity A wave" = standing wave pattern in phi
- The craft sits at the node of its own standing wave
- The saucer shape maximizes the node surface area (see Section 12)

---

## 12. Why the Saucer Shape

### 12.1 Node Geometry from Source Shape

In acoustics, the node geometry depends on the transducer shape:

| Source shape | Node geometry | Trapping region |
|-------------|--------------|-----------------|
| Flat disc (1D) | Horizontal planes | Stack of planes |
| Ring (toroidal) | Flat equatorial plane | Disc-shaped region |
| Sphere | Spherical shells | Concentric shells |
| Hemisphere pair | Equatorial plane + shells | 3D trapping volume |

A **toroidal** source (ring of transducers) creates a node in the
equatorial plane — the natural node geometry is a FLAT DISC.

```
Cross-section of toroidal source and its node:

    ═══╗           ╔═══
       ║           ║
       ║   NODE    ║     <-- flat disc node in equatorial plane
       ║  (alpha=0)║
    ═══╝           ╚═══

    ═══ = toroidal transducer ring
```

### 12.2 Optimal Craft Shape

If the craft generates a toroidal standing wave in the condensate:
- The node is a flat disc in the equatorial plane
- Maximum decoupling area = disc (saucer) shape
- The craft body should be flat and centered on the equatorial node
- This is geometrically optimal — minimum mass, maximum node coverage

The saucer shape is NOT aerodynamic optimization (there's no atmosphere
interaction in decoupled flight). It IS wave-node geometry optimization.

### 12.3 Demonstrating with the Array Rig

The TinyLev rig (two hemispheres) creates nodes in the equatorial plane.
If you use a toroidal arrangement instead (ring of transducers), the
node geometry changes to a flat disc — you can SEE the saucer-shaped
trapping zone by sprinkling beads and observing where they collect.

---

## 13. Safety Notes

- **Ultrasound:** 40 kHz is inaudible but can cause headaches at high power
  (>10W). Keep power moderate and limit exposure time.
- **Hearing:** Some people can hear harmonics (20 kHz range). If anyone
  nearby complains of discomfort, reduce power or add enclosure.
- **Transducer voltage:** L298N can output up to 12V. Not dangerous but
  avoid touching live terminals.
- **Styrofoam beads:** Small, static-charged, go everywhere. Work on a
  tray. Clean up after.
- **Soldering:** Standard precautions (ventilation, don't touch iron tip).

---

## 14. Shopping List

### 14.1 Simple Rig (1 transducer + reflector)

| # | Item | Qty | Cost (ZAR) | Source |
|---|------|-----|-----------|--------|
| 1 | HC-SR04 ultrasonic module | 1 | R30 | Micro Robotics / AliExpress |
| 2 | Arduino Nano | 1 | R100 | Micro Robotics |
| 3 | L298N H-bridge module | 1 | R60 | Micro Robotics / Communica |
| 4 | 12V battery or power supply | 1 | R80 | Electronics shop |
| 5 | Aluminium disc 30mm (reflector) | 1 | R20 | Hardware store (cut from sheet) |
| 6 | Wood/aluminium for mount | Misc | R40 | Hardware store |
| 7 | Styrofoam beads (craft supplies) | Pack | R20 | Craft shop |
| 8 | Jumper wires, USB cable | Misc | R30 | Micro Robotics |
| | **Simple rig total** | | **~R380** | |

### 14.2 Array Rig (TinyLev style)

| # | Item | Qty | Cost (ZAR) | Source |
|---|------|-----|-----------|--------|
| 9 | 40 kHz ultrasonic transducers | 72 | R720 | AliExpress (bulk) |
| 10 | 3D-printed hemisphere holders | 2 | R300 | 3D print service / own printer |
| 11 | L298N H-bridge modules | 2 | R120 | Micro Robotics |
| 12 | 5V 5A power supply | 1 | R100 | Amazon / electronics shop |
| 13 | Perfboard for wiring | 2 | R40 | Communica |
| | **Array rig additional** | | **~R1,280** | |
| | **Array rig total (incl simple)** | | **~R1,660** | |

### 14.3 Inverted Rig (Add-on)

| # | Item | Qty | Cost (ZAR) | Source |
|---|------|-----|-----------|--------|
| 14 | Small piezo disc (10 mm) | 2 | R20 | Communica / AliExpress |
| 15 | Balsa wood sheet (1 mm thick) | 1 | R15 | Craft shop |
| 16 | Nylon fishing line (0.1 mm) | 1m | R10 | Fishing shop |
| 17 | Enamelled copper wire (0.1 mm) | 5m | R15 | Communica |
| | **Inverted add-on total** | | **~R60** | |

---

## 15. References

1. **Source:** [Acoustic levitation — Wikipedia](https://en.wikipedia.org/wiki/Acoustic_levitation)
   Standing wave node trapping of small objects in air
2. **Source:** Gor'kov, L. P. (1962), "On the forces acting on a small particle in an
   acoustical field in an ideal fluid", Soviet Physics - Doklady 6, 773.
   Theoretical framework for acoustic radiation force on particles.
3. **Source:** Marzo, A. et al. (2017), "TinyLev: A multi-emitter single-axis acoustic
   levitator", Review of Scientific Instruments 88, 085105.
   Open-source 72-transducer levitator design; build instructions available.
4. **Source:** [Ultrasonic transducer — Wikipedia](https://en.wikipedia.org/wiki/Ultrasonic_transducer)
   40 kHz piezoelectric transducers used in distance sensing and levitation
5. **Source:** PDTP Part 28b — Polarization analogy; decoupling energy ~10 kW/ton
6. **Source:** PDTP Part 29 — Decoupling cost; alpha = cos(psi - phi) -> 0
7. **Source:** PDTP Part 64 — Temperature; condensate excitation energy
8. **Related concept:** [acoustic_levitation_pdtp_analogy.md](../docs/applications/acoustic_levitation_pdtp_analogy.md)
   — high-level analogy document (this experiment is the buildable version)
9. **Related experiment:** [experiment_3y_rig.md](experiment_3y_rig.md) — Z3 topology EM-gravity test
10. **Related experiment:** [experiment_coil_drum.md](experiment_coil_drum.md) — traveling wave EM-gravity test
11. **Visual:** [Acoustic levitation diagram](../assets/images/acoustic%20standing%20waves%20levitation%20H19fQ==.jpg)
12. **Visual:** [Real acoustic levitation experiment](../assets/images/acoustic%20standing%20waves%20levitation%20472926_1_En_2_Fig1_HTML.png)
13. **Inspiration:** Bob Lazar (1989) — gravity amplifiers as resonant transducers.
    Speculative connection; included for motivation, not as evidence.
