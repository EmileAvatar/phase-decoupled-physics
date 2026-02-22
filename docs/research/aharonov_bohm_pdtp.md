# The Aharonov-Bohm Effect and PDTP Phase Structure

Phase as the fundamental physical quantity: experimental evidence,
geometric formulation, and PDTP interpretation.

**Part 18 — Deep Analysis** (expanded from preliminary document)

**Status:** Research analysis with quantitative derivations and
geometric classification. Not experimentally validated.

**Bottom line:** PDTP's phase-centric framework is geometrically
consistent (fiber bundle classification: U(1)_global × SO(3,1)),
reproduces the COW gravitational phase shift exactly, and connects
to cosmic strings as condensate vortices. The EM–gravity phase
parallel is genuine but does not constitute unification. The 2022
Overstreet et al. experiment provides the strongest experimental
support for the "phase is fundamental" paradigm.

**Prerequisites:** [mathematical_formalization.md](../technical/mathematical_formalization.md) (Part 1),
[tetrad_extension.md](tetrad_extension.md) (Part 12),
[cosmological_constant_analysis.md](cosmological_constant_analysis.md) (Part 17)

---

## Table of Contents

**Preliminary Analysis (original document):**
1. [The Experiment: Tonomura (1986)](#1-the-experiment-tonomura-1986)
2. [Standard Physics Explanation](#2-standard-physics-explanation)
3. [PDTP Interpretation](#3-pdtp-interpretation)
4. [Structural Parallels](#4-structural-parallels)
5. [What This Means for PDTP](#5-what-this-means-for-pdtp)
6. [Limitations and Honest Assessment](#6-limitations-and-honest-assessment)

**Deep Analysis (Part 18):**
7. [The COW Experiment — PDTP Derivation](#7-the-cow-experiment--pdtp-derivation-part-18)
8. [Fiber Bundle Structure of PDTP](#8-fiber-bundle-structure-of-pdtp-part-18)
9. [Topological Aspects — Phase Vortices and Defects](#9-topological-aspects--phase-vortices-and-defects-part-18)
10. [EM–Gravity Unification Hints](#10-emgravity-unification-hints-part-18)
11. [Impact on Existing PDTP Results](#11-impact-on-existing-pdtp-results-part-18)
12. [Remaining Open Questions](#12-remaining-open-questions-part-18)
13. [References](#13-references)

---

## 1. The Experiment: Tonomura (1986)

### 1.1 Background

In 1959, Yakir Aharonov and David Bohm predicted that a charged particle
could be affected by electromagnetic potentials even in regions where both
the electric field **E** and magnetic field **B** are zero. This was
controversial because classical electromagnetism treats the vector
potential **A** as merely a mathematical convenience — only **E** and **B**
were considered "real."

**Source:** Aharonov, Y. & Bohm, D. (1959), "Significance of electromagnetic
potentials in the quantum theory," *Physical Review* 115(3), 485–491.

**Source:** [Aharonov-Bohm effect — Wikipedia](https://en.wikipedia.org/wiki/Aharonov%E2%80%93Bohm_effect)

### 1.2 Tonomura's Definitive Experiment

Akira Tonomura at Hitachi Research Laboratory performed the definitive
experimental verification in 1986. Previous experiments had been criticized
for possible magnetic field leakage. Tonomura eliminated this objection
completely.

**The setup:**

1. A tiny **toroidal (doughnut-shaped) ferromagnet**, only 6 micrometers
   in diameter, was fabricated
2. The toroid was coated with a **niobium superconductor** — this confines
   the magnetic field completely inside the doughnut via the **Meissner
   effect** (superconductors expel magnetic fields)
3. An additional **copper layer** was added on top for extra shielding
4. Result: **B = 0 everywhere outside the doughnut** — the magnetic flux
   is trapped entirely inside the ring

**The measurement:**

Using **electron holography** (a technique Tonomura pioneered), an electron
beam was split:
- One part passed **through the hole** in the center of the doughnut
- The other part passed **around the outside** of the doughnut
- Both paths are in regions where B = 0 — no magnetic field touches
  either beam
- The two beams were recombined to create an interference pattern

**What was observed:**

The interference fringes were **displaced by exactly half a fringe spacing**
between the inside and outside paths. Electrons that went through the hole
had their quantum phase shifted relative to those that went around, despite
neither beam ever encountering a magnetic field.

**Source:** Tonomura, A. et al. (1986), "Evidence for Aharonov-Bohm effect
with magnetic field completely shielded from electron wave,"
*Physical Review Letters* 56(8), 792–795.

**Source:** [Hitachi — Verification of the Aharonov-Bohm effect](https://www.hitachi.com/rd/research/materials/quantum/aharonov-bohm/index.html)

### 1.3 Why This Was Revolutionary

The experiment proved that:

1. **The vector potential A is physically real**, not just a mathematical
   tool — it directly affects the quantum phase of particles
2. **Phase shifts occur without any force** — no energy is exchanged,
   no momentum is transferred, yet the wavefunction is physically altered
3. **Potentials, not fields, are the fundamental quantities** in quantum
   mechanics

---

## 2. Standard Physics Explanation

### 2.1 The Phase Shift Formula

In quantum mechanics, a charged particle moving through a region with
vector potential **A** acquires an additional phase:

```
Δψ = (e/ℏ) ∫ A · dl
```

For a closed path encircling magnetic flux Φ_B:

```
Δψ = (e/ℏ) Φ_B
```

**Source:** [Aharonov-Bohm effect — Wikipedia](https://en.wikipedia.org/wiki/Aharonov%E2%80%93Bohm_effect)

This is a **topological** result — it depends only on the total enclosed
flux, not on the details of the path or the local field values.

### 2.2 Why B = 0 Doesn't Mean A = 0

A key mathematical fact: you cannot make **A** = 0 everywhere outside a
region that contains magnetic flux. This is a topological constraint.

The magnetic field is B = ∇ × A (the curl of A). Having B = 0 means
A is curl-free, but it can still be nonzero — it just has to be a
gradient (locally). Globally, around a flux-containing region, A cannot
be a pure gradient, and this is what produces the phase shift.

**Source:** [Stokes' theorem — Wikipedia](https://en.wikipedia.org/wiki/Stokes%27_theorem)

### 2.3 The Geometric (Fiber Bundle) Interpretation

Modern physics interprets the AB effect using **fiber bundle theory**:

- The electromagnetic field is a **connection** on a U(1) principal bundle
- The vector potential **A** is the connection 1-form
- The phase shift around a closed loop is the **holonomy** of this connection
- The AB effect shows that the connection (A), not just the curvature (B),
  has physical meaning

This geometric language is important because it generalizes to gravity:
in GR, the gravitational field is also a connection (the Christoffel
connection), and parallel transport around a closed loop produces a
rotation (= curvature = gravity).

**Source:** [Connection (fiber bundle) — Wikipedia](https://en.wikipedia.org/wiki/Connection_(mathematics))

---

## 3. PDTP Interpretation

### 3.1 Phase Is the Fundamental Quantity

In standard physics, force is fundamental and phase is derived. The AB
effect inverts this: **phase is fundamental** and force is derived (or
absent entirely).

PDTP makes the same inversion for gravity:

| Standard View | PDTP View |
|---------------|-----------|
| Gravity is a force (Newton) or curvature (Einstein) | Gravity is phase-locking between ψ and φ |
| Phase is a mathematical property of wavefunctions | Phase is a physical field with real dynamics |
| Potentials are mathematical conveniences | Potentials (phase gradients) are the reality |

The AB effect is experimental proof that the "phase is fundamental" view
is correct — at least for electromagnetism. PDTP extends this principle
to gravity.

### 3.2 Phase Coupling Without Force

The most striking feature of the AB effect: **the electron's phase is
altered without any force acting on it.** No energy is exchanged. No
momentum is transferred. Yet the phase — and therefore the interference
pattern — is physically changed.

In PDTP, gravity works the same way:

- The coupling between matter phase ψ and spacetime phase φ is through
  cos(ψ − φ)
- When ψ and φ are synchronized (phase-locked), the system is in its
  ground state — this IS gravity
- The coupling is a **phase relationship**, not a force in the Newtonian
  sense
- Forces emerge as a consequence of phase gradients, not the other way
  around

The AB effect demonstrates that this kind of "force-free phase coupling"
is a real physical phenomenon, not just a theoretical possibility.

### 3.3 Tonomura's Ring as a Phase-Drift Analogy

The connection to PDTP is particularly vivid in Tonomura's toroidal
geometry:

**Inside the ring (through the hole):**
- Electrons acquire phase shift Δψ = (e/ℏ)Φ_B
- The magnetic flux creates a region where the electron's phase
  **drifts relative to what it would be without the flux**
- No force acts — only the phase landscape is altered

**Outside the ring:**
- Electrons propagate with no phase shift
- The phase landscape is unmodified

**The PDTP analogy:**

This is structurally identical to what a PDTP device would do:

| Tonomura's Ring | PDTP Coupling Suppression |
|-----------------|--------------------------|
| Magnetic flux inside ring | Modified phase coupling inside device |
| A ≠ 0 but B = 0 outside | Phase gradient exists but no "force field" |
| Electron phase shifts without force | Matter phase ψ drifts from spacetime phase φ |
| Phase shift is topological | Phase decoupling depends on coupling geometry |
| Ring doesn't push electrons | PDTP device doesn't push against spacetime |

The ring doesn't exert a force on the electrons — it **alters the phase
landscape** they travel through. A PDTP device would alter the phase
landscape between matter and spacetime.

### 3.4 The Electromagnetic–Gravitational Phase Analogy

PDTP proposes that gravity is to the spacetime phase φ what
electromagnetism is to the electromagnetic gauge phase. The structural
parallel:

**Electromagnetism (established physics):**
```
Phase shift: Δψ_EM = (e/ℏ) ∫ A_μ dx^μ
Coupling: minimal coupling, ∂_μ → ∂_μ − ieA_μ
Symmetry: local U(1) gauge invariance
Observable: interference pattern shift (AB effect)
```

**PDTP gravity (proposed):**
```
Phase relationship: cos(ψ − φ)
Coupling: phase-locking, strength g
Symmetry: global U(1) (φ → φ+c, ψ → ψ+c)
Observable: gravitational attraction (phase synchronization)
```

**Key differences:**
- EM phase coupling is **local U(1) gauge** — the phase can be shifted
  independently at each spacetime point
- PDTP phase coupling is **global U(1)** — the symmetry is a simultaneous
  shift of all phases
- EM uses the vector potential A_μ (a gauge field); PDTP uses the scalar
  phase φ (a physical field)
- In EM, the potential is not directly observable (gauge freedom); in PDTP,
  the phase difference (ψ − φ) IS the observable

Despite these differences, the conceptual lesson is the same: **phase
relationships are physically real and can produce observable effects
without local forces.**

---

## 4. Structural Parallels

### 4.1 Summary Table

| Feature | AB Effect (EM) | PDTP Gravity |
|---------|----------------|--------------|
| Fundamental quantity | Phase of wavefunction | Phase of matter (ψ) and spacetime (φ) |
| What does the coupling | Vector potential A | Phase-locking cos(ψ−φ) |
| Force involved? | No (B = 0 on electron path) | No (gravity emerges from phase, not imposed) |
| What's altered | Quantum phase | Phase relationship ψ − φ |
| Observable effect | Interference fringe shift | Gravitational attraction |
| Geometry matters? | Yes (topological — enclosed flux) | Yes (phase gradients determine "force") |
| Energy exchanged? | No | Not for static phase-lock (yes for phase changes) |

### 4.2 What Both Effects Share

1. **Phase is primary, force is secondary (or absent)**
   - AB: force = 0, but phase changes → observable effect
   - PDTP: force emerges from phase-locking, not the other way around

2. **Potentials/phases are more fundamental than fields/forces**
   - AB: A is real, B is derived (B = curl A)
   - PDTP: φ is real, gravity is derived (from phase gradients)

3. **Non-local character**
   - AB: the effect depends on flux enclosed by the path, not local fields
   - PDTP: phase-locking is a relationship between fields, not a local force

4. **No classical explanation**
   - AB: impossible in classical electromagnetism (requires QM)
   - PDTP: impossible in classical gravity (requires quantum phase structure)

---

## 5. What This Means for PDTP

### 5.1 Experimental Support for the Phase Paradigm

The AB effect doesn't prove PDTP is correct — but it proves that the
**type of physics PDTP proposes** actually exists in nature:

- Phase relationships CAN produce observable effects without forces ✓
- Potentials CAN be more fundamental than fields ✓
- Quantum phases CAN be physically real, not just mathematical ✓
- Phase shifts CAN occur in force-free regions ✓

This makes PDTP's core proposal — that gravity is a phase-locking
phenomenon — at least **physically plausible**, not just mathematically
possible.

### 5.2 The AB Effect as Precedent

Before the AB effect was experimentally confirmed, many physicists
dismissed it as impossible. The idea that a potential (A) could affect
physics in a region where the field (B) is zero seemed absurd.

PDTP faces a similar skepticism: the idea that gravity could be a phase
effect rather than a fundamental force/curvature seems strange. But the
AB effect established that "phase effects without forces" are a real
category of physics. PDTP extends this category from electromagnetism
to gravity.

### 5.3 Implications for PDTP Engineering

If phase coupling can be controlled (as Tonomura did for EM phase with
his toroidal magnet), then in principle, gravitational phase coupling
might also be controllable. The AB effect shows that:

- Phase environments can be **engineered** (the superconducting toroid)
- Phase shifts can be **precisely controlled** (quantized flux)
- Phase effects are **real and measurable** (electron holography)

These are exactly the capabilities a PDTP device would need — but for
gravitational phase rather than electromagnetic phase.

---

## 6. Limitations and Honest Assessment

### 6.1 What the AB Effect Does NOT Prove for PDTP

1. **The AB effect is electromagnetic, not gravitational.** It proves
   phase matters for EM; it does not directly prove phase matters for
   gravity.

2. **Different symmetry structures.** EM has local U(1) gauge symmetry;
   PDTP has global U(1). These are fundamentally different mathematical
   structures.

3. **Different field types.** The EM vector potential A_μ is a gauge field
   (spin-1); PDTP's spacetime phase φ is a scalar field (spin-0). The
   tetrad extension adds tensor structure, but it's still not a gauge
   field in the EM sense.

4. **Scale gap.** The AB effect operates at quantum scales (single
   electrons). PDTP requires macroscopic phase coherence — a vastly
   harder requirement.

5. **No gravitational AB effect observed.** A gravitational analog of
   the AB effect (phase shift from a gravitational potential without
   tidal forces) has been proposed but not observed.

### 6.2 The Gravitational AB Analog

A gravitational Aharonov-Bohm effect has been theoretically predicted
in GR: a particle traveling through a region with gravitational potential
but no tidal forces (no curvature) should acquire a phase shift:

```
Δψ_grav = (m/ℏ) ∫ Φ_grav dt
```

where Φ_grav is the Newtonian gravitational potential. This is the
**Colella-Overhauser-Werner (COW)** effect, which HAS been observed
for neutrons in Earth's gravitational field (1975).

**Source:** Colella, R., Overhauser, A.W. & Werner, S.A. (1975),
"Observation of gravitationally induced quantum interference,"
*Physical Review Letters* 34, 1472–1474.

**Source:** [COW experiment — Wikipedia](https://en.wikipedia.org/wiki/Colella%E2%80%93Overhauser%E2%80%93Werner_experiment)

The COW experiment shows that gravitational potentials DO affect quantum
phases — strengthening the PDTP interpretation that phase is central
to gravity.

### 6.3 Status

The AB effect provides **conceptual support** for PDTP's phase-centric
worldview. It is:
- **Strong evidence** that phase is physically real (not just math)
- **A precedent** for force-free phase effects in nature
- **An analogy**, not a proof, for gravitational phase-locking
- **Motivation** for pursuing PDTP, not validation of it

---

## 7. The COW Experiment — PDTP Derivation (Part 18)

### 7.1 The Experiment

In 1975, Colella, Overhauser, and Werner (COW) performed the first
experiment demonstrating quantum interference due to gravity. A neutron
beam was split in a silicon crystal interferometer, with the two paths
at different heights in Earth's gravitational field. Despite neutrons
being electrically neutral (so no EM coupling), the gravitational
potential difference produced a measurable phase shift in the
interference pattern.

**Source:** Colella, R., Overhauser, A.W. & Werner, S.A. (1975),
"Observation of gravitationally induced quantum interference,"
*Physical Review Letters* 34, 1472–1474.

**Source:** [COW experiment — Wikipedia](https://en.wikipedia.org/wiki/Colella%E2%80%93Overhauser%E2%80%93Werner_experiment)

### 7.2 Standard QM Derivation

The gravitational phase shift is derived from the Schrödinger equation
with a gravitational potential V = mgh:

```
ψ(x,t) = ψ₀ exp(i(k·x − ωt))
```

A particle at height h in a gravitational field acquires an additional
phase from the potential energy:

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  Δφ_grav = (1/ℏ) ∫ V dt = (m/ℏ) ∫ g·Δh dt         (7.1)  │
│                                                              │
│  For paths at heights h₁ and h₂ with separation d:          │
│                                                              │
│  Δφ = (m g d / ℏ) × (L / v)                         (7.2)  │
│                                                              │
│  where L = path length, v = neutron velocity                 │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**Source:** [Neutron interferometer — Wikipedia](https://en.wikipedia.org/wiki/Neutron_interferometer)

Using the de Broglie relation p = mv = h/λ (so v = h/(mλ)), and
defining the interferometer area A = L × d projected perpendicular
to gravity:

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  Δφ_COW = (2π m² g A sin α) / (h²/λ)                       │
│                                                              │
│         = 2π m² g A λ sin α / h²                     (7.3)  │
│                                                              │
│  where α = tilt angle of interferometer relative to          │
│  horizontal, A = enclosed area, λ = neutron wavelength       │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**Source:** [Neutron interferometer — Wikipedia](https://en.wikipedia.org/wiki/Neutron_interferometer)

This formula was confirmed experimentally by COW to within ~1%.
The key insight: **gravitational potentials produce quantum phase
shifts**, just as electromagnetic potentials do in the AB effect.

### 7.3 PDTP Derivation

In PDTP, the matter-wave phase ψ and spacetime phase φ are coupled
through the Lagrangian:

```
L = ½(∂_μφ)(∂^μφ) + ½(∂_μψ)(∂^μψ) + g cos(ψ − φ)
```

**Source:** [mathematical_formalization.md](../technical/mathematical_formalization.md) eq. (1.1)

In the weak-field, non-relativistic limit (established in Part 1),
PDTP reproduces the Newtonian gravitational potential:

```
Φ_grav = −GM/r ≈ gh    (near Earth's surface)
```

**Source:** [mathematical_formalization.md](../technical/mathematical_formalization.md) §2.5

A matter-wave propagating through a region with gravitational potential
Φ acquires a phase shift from the standard quantum mechanical relation:

```
ψ(x,t) ∝ exp(i S/ℏ)
```

where S is the classical action. For a particle in a gravitational
potential, the action along a path includes the potential energy:

```
S = ∫ (½mv² − mΦ) dt
```

**Source:** [Path integral formulation — Wikipedia](https://en.wikipedia.org/wiki/Path_integral_formulation)

The phase difference between two paths at different heights is:

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  Δφ_PDTP = (1/ℏ) ∫ m Φ_grav dt                             │
│                                                              │
│          = (m/ℏ) ∫ g·Δh dt                           (7.4)  │
│                                                              │
│  This is IDENTICAL to the standard QM result (7.1).         │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**PDTP Original.** PDTP reproduces the COW phase shift exactly
because it reproduces Newtonian gravity exactly in the weak-field
limit. The COW experiment is a **consistency check**, not a new
test of PDTP — any theory that reproduces Newton's gravity must
also reproduce the COW result.

### 7.4 What the COW Experiment Proves for PDTP

The COW result demonstrates:

1. **Gravitational potentials produce quantum phase shifts.** This is
   exactly what PDTP claims: gravity IS a phase relationship.

2. **The gravitational phase shift has the form (m/ℏ)∫Φ dt.** In
   PDTP, this emerges from the phase-locking cos(ψ − φ) when the
   potential modifies the local phase gradient.

3. **Phase effects are physically real for gravity.** The COW
   experiment is the gravitational counterpart of the AB effect — it
   proves that gravitational phases, like electromagnetic phases, are
   physically observable.

However, the COW result does NOT distinguish PDTP from GR, because
both predict the same phase shift in the non-relativistic limit.

### 7.5 The 2022 Gravitational AB Experiment (Overstreet et al.)

In 2022, Overstreet et al. at Stanford demonstrated a gravitational
Aharonov-Bohm effect using atom interferometry. Unlike the COW
experiment (which uses Earth's uniform field), this experiment placed
a kilogram-scale source mass near one arm of the interferometer:

- Ultra-cold rubidium atoms were split into two wave packets
  ~25 cm apart
- A tungsten source mass was positioned near one wave packet
- The gravitational phase shift was measured independently of any
  classical deflection
- The result confirmed that gravity produces AB-type phase shifts:
  the potential Φ, not just the tidal force ∇²Φ, is physically real

**Source:** Overstreet, C. et al. (2022), "Observation of a
gravitational Aharonov-Bohm effect," *Science* 375, 226–229.

This is particularly significant for PDTP because:

- It directly measures a gravitational PHASE effect (not force)
- The phase is the fundamental quantity in PDTP's framework
- The result is consistent with both GR and PDTP predictions
- It demonstrates that gravitational phases can be engineered
  and measured with precision — a prerequisite for any future
  PDTP-specific tests

**PDTP Original.** The Overstreet et al. result provides the
strongest experimental support for the "phase is fundamental"
paradigm that PDTP is built on. While it does not distinguish
PDTP from GR, it confirms that gravitational physics operates
through phase relationships, exactly as PDTP proposes.

---

## 8. Fiber Bundle Structure of PDTP (Part 18)

### 8.1 Electromagnetism as a Fiber Bundle (Review)

Modern physics formulates electromagnetism as a connection on a
U(1) principal fiber bundle:

| Component | Mathematical Object | Physical Meaning |
|-----------|-------------------|-----------------|
| Base space | Spacetime manifold M | Where physics happens |
| Fiber | U(1) ≅ circle | Phase of charged particle |
| Connection | A_μ (vector potential) | How phase is "transported" |
| Curvature | F_μν = ∂_μA_ν − ∂_νA_μ | Electromagnetic field (E, B) |
| Holonomy | exp(ie/ℏ ∮A·dl) | Phase shift around closed loop |

**Source:** [Fiber bundle — Wikipedia](https://en.wikipedia.org/wiki/Fiber_bundle)

**Source:** [Connection (fiber bundle) — Wikipedia](https://en.wikipedia.org/wiki/Connection_(mathematics))

The AB effect IS the holonomy: the phase shift around a closed path
depends on the connection (A), not just the curvature (F). This is
a topological statement about the bundle structure.

The key property: EM has a **local** U(1) gauge symmetry, meaning
the phase can be shifted independently at each spacetime point:

```
ψ → e^{iα(x)} ψ,    A_μ → A_μ + (1/e) ∂_μα
```

This gauge freedom is what makes A_μ "not directly observable" while
the holonomy (gauge-invariant) IS observable.

### 8.2 General Relativity as a Fiber Bundle (Review)

GR can be formulated as a connection on the frame bundle:

| Component | Mathematical Object | Physical Meaning |
|-----------|-------------------|-----------------|
| Base space | Spacetime manifold M | Where physics happens |
| Fiber | SO(3,1) (Lorentz group) | Local reference frames |
| Connection | ω^a_{bμ} (spin connection) | How frames are transported |
| Curvature | R^a_{bμν} | Riemann tensor (gravity) |
| Holonomy | Parallel transport around loop | Rotation = curvature |

**Source:** Weatherall, J.O. (2016), "Fiber Bundles, Yang-Mills Theory,
and General Relativity," *Synthese* 193, 2389–2425.

**Source:** [Frame bundle — Wikipedia](https://en.wikipedia.org/wiki/Frame_bundle)

In the tetrad formulation (which Part 12 uses), the basic variables
are the tetrad e^a_μ and the spin connection ω^a_{bμ}. The Einstein
equation emerges from varying the Palatini action with respect to
these variables.

The gravitational analog of the AB effect: parallel-transporting a
vector around a closed loop in curved spacetime rotates it. The
rotation angle is the holonomy of the Levi-Civita connection —
this IS spacetime curvature.

### 8.3 PDTP's Fiber Bundle Structure (PDTP Original)

Now we can classify PDTP in this geometric language.

**The scalar sector (phase equation):**

PDTP's scalar sector has a global U(1) symmetry:

```
φ → φ + c,    ψ → ψ + c    (c = constant)
```

This is a **trivial** U(1) bundle — the phase can be shifted, but
only by the SAME constant everywhere. There is no gauge freedom:
the phase difference (ψ − φ) is directly observable.

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  PDTP scalar sector fiber bundle:                            │
│                                                              │
│  Base:       Spacetime M                                     │
│  Fiber:      U(1) (trivial bundle)                           │
│  Connection: ∂_μ(ψ − φ) (phase gradient)              (8.1) │
│  Curvature:  ∂_μ∂_ν(ψ−φ) − ∂_ν∂_μ(ψ−φ) = 0               │
│              (vanishes for smooth phase fields)              │
│  Holonomy:   ∮ ∂_μ(ψ−φ) dx^μ = 0   (smooth fields)         │
│              ∮ ∂_μ(ψ−φ) dx^μ = 2πn  (vortex defects)        │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**PDTP Original.** The crucial structural difference between PDTP
and electromagnetism:

| Property | EM (local U(1)) | PDTP scalar (global U(1)) |
|----------|----------------|--------------------------|
| Gauge freedom | Yes — A_μ is not observable | No — (ψ − φ) IS observable |
| Bundle type | Non-trivial (can have flux) | Trivial (smooth fields) |
| Holonomy | Non-zero (AB effect) | Zero (unless vortex defects) |
| Connection | A_μ (4 components) | ∂_μ(ψ−φ) (derived, not independent) |
| Topological effects | Rich (monopoles, instantons) | Limited (only vortex defects) |

This is an **honest structural limitation**: PDTP's scalar sector
has less geometric richness than electromagnetism. The global U(1)
symmetry is simpler than local U(1), and this limits the topological
phenomena available.

**The tensor sector (tetrad extension):**

Part 12 introduces the tetrad e^a_μ, which lives on the SO(3,1)
frame bundle — exactly the same geometric structure as GR:

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  PDTP tensor sector fiber bundle:                            │
│                                                              │
│  Base:       Spacetime M                                     │
│  Fiber:      SO(3,1) (Lorentz group)                         │
│  Connection: ω^a_{bμ} (spin connection)                (8.2) │
│  Curvature:  R^a_{bμν} (Riemann tensor)                      │
│  Holonomy:   Parallel transport rotation                     │
│                                                              │
│  This is identical to GR's fiber bundle structure.           │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**Source:** [tetrad_extension.md](tetrad_extension.md) §5

### 8.4 The Two-Sector Geometric Structure

The complete extended PDTP has a **product bundle structure**:

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  Full PDTP geometry:                                         │
│                                                              │
│  U(1)_global × SO(3,1)                                (8.3) │
│                                                              │
│  Scalar sector: trivial U(1) bundle (phase dynamics)         │
│  Tensor sector: SO(3,1) frame bundle (spacetime geometry)    │
│                                                              │
│  Compare to electrogravity:                                  │
│                                                              │
│  U(1)_local × SO(3,1)                                       │
│                                                              │
│  EM: non-trivial U(1) bundle (gauge field)                   │
│  GR: SO(3,1) frame bundle (spacetime geometry)               │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**PDTP Original.** The geometric content of PDTP is: a trivial U(1)
scalar bundle coupled to the standard SO(3,1) frame bundle of GR.
The scalar sector provides the "why" of gravity (phase-locking
mechanism); the tensor sector provides the "how" (spacetime
curvature). The product structure U(1)_global × SO(3,1) is the
natural fiber bundle classification of the extended PDTP.

### 8.5 Could PDTP's U(1) Become Local?

A natural question: could PDTP's global U(1) be promoted to a
local U(1) gauge symmetry?

If φ → φ + α(x) and ψ → ψ + α(x) independently at each point,
then:
- The phase difference (ψ − φ) would no longer be directly
  observable (it becomes gauge-dependent)
- A gauge field A_μ would need to be introduced to maintain
  covariance: ∂_μ(ψ−φ) → ∂_μ(ψ−φ) − A_μ
- The resulting theory would look like PDTP + electromagnetism

This is suggestive but speculative. It would require:
- A physical motivation for gauging the symmetry
- Identification of A_μ with the electromagnetic potential
- Compatibility with the known structure of QED

This direction is explored further in §10 (EM–gravity unification).

---

## 9. Topological Aspects — Phase Vortices and Defects (Part 18)

### 9.1 Quantized Vortices in Superfluids (Review)

In superfluid helium-4, the order parameter is a complex field
Ψ = |Ψ| e^{iθ}, and the superfluid velocity is:

```
v_s = (ℏ/m) ∇θ
```

The circulation around any closed loop is quantized:

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  Γ = ∮ v_s · dl = (ℏ/m) ∮ ∇θ · dl = n × (h/m)      (9.1)  │
│                                                              │
│  where n is an integer (winding number)                      │
│  h/m ≈ 9.97 × 10⁻⁸ m²/s for ⁴He                           │
│                                                              │
│  This is the Onsager-Feynman quantization condition.         │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**Source:** [Quantum vortex — Wikipedia](https://en.wikipedia.org/wiki/Quantum_vortex)

**Source:** [Superfluid helium-4 — Wikipedia](https://en.wikipedia.org/wiki/Superfluid_helium-4)

Quantized vortices are **topological defects**: they cannot be
removed by smooth deformation of the order parameter. The winding
number n is a topological invariant. Vortex lines are one-dimensional
defects where the condensate order parameter vanishes (|Ψ| = 0 at
the vortex core).

### 9.2 Phase Vortices in the PDTP Condensate (PDTP Original)

If the spacetime condensate has a phase field φ, then by direct
analogy with superfluids, topological defects are possible:

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  PDTP phase vortex condition:                                │
│                                                              │
│  ∮ ∇φ · dl = 2πn                                     (9.2)  │
│                                                              │
│  where n = integer (winding number)                          │
│                                                              │
│  At the vortex core: the condensate order parameter           │
│  vanishes — spacetime becomes singular.                      │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

A PDTP vortex line would be a one-dimensional region where the
spacetime condensate breaks down. The phase φ winds by 2πn around
the vortex, creating a topological defect.

### 9.3 Connection to Cosmic Strings

Remarkably, GR already has objects that match this description:
**cosmic strings**.

A cosmic string is a one-dimensional topological defect in spacetime
with the following properties:

- The spacetime around a cosmic string is **locally flat** (no
  curvature) but **globally conical** (a wedge of angle Δθ is
  removed)
- The deficit angle is Δθ = 8πGμ/c², where μ is the string's
  linear mass density
- A complete circuit around the string covers less than 2π
- Light passing on opposite sides of the string produces
  **double images** without distortion

**Source:** [Cosmic string — Wikipedia](https://en.wikipedia.org/wiki/Cosmic_string)

The gravitational AB effect of cosmic strings is well-established
in GR: a particle circling a cosmic string acquires a phase shift
despite the spacetime being flat everywhere along its path. This
is directly analogous to the EM AB effect.

**PDTP interpretation:**

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  PDTP cosmic string interpretation:                          │
│                                                              │
│  GR description:     conical deficit Δθ = 8πGμ/c²           │
│  PDTP description:   phase vortex with winding number n      │
│                                                              │
│  The deficit angle maps to phase winding:                    │
│                                                              │
│  Δθ ↔ 2πn    (topological identification)            (9.3)  │
│                                                              │
│  A cosmic string IS a phase vortex in the spacetime          │
│  condensate — a line where the condensate order              │
│  parameter vanishes and the phase winds.                     │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**PDTP Original.** In the condensate picture, cosmic strings have
a natural interpretation as quantized vortex lines in the spacetime
phase field. The conical deficit angle corresponds to the phase
winding number. This provides a physical mechanism for cosmic
string formation: they are topological defects formed during a
cosmological phase transition of the spacetime condensate, just
as vortex lines form in superfluid helium during rapid cooling.

### 9.4 Phase Defects and Dark Energy (Speculative)

Could topological defects in the condensate be related to
cosmological phase drift (Part 17)?

If the universe contains a network of phase vortices at cosmological
scales, their collective effect could produce:

- **Effective decoherence**: many vortices disrupting long-range
  phase coherence, leading to phase drift
- **Dark energy**: the energy stored in vortex cores contributing
  to the cosmological constant
- **Scale-dependent behavior**: below the inter-vortex spacing,
  the condensate is coherent; above it, phase coherence breaks down

This connects to the "phase drift mechanism" identified in Part 17
as a genuinely open problem.

However, this is highly speculative:
- No quantitative estimate of vortex density
- No calculation of vortex contribution to dark energy
- No mechanism for vortex formation at cosmological scales
- No observational signature identified

### 9.5 Topological Classification

The topological defects available in PDTP depend on the symmetry
structure:

| Symmetry | Defect Type | Dimension | PDTP Equivalent |
|----------|------------|-----------|-----------------|
| U(1) → 1 (broken) | Vortex lines | 1D (strings) | Cosmic strings |
| U(1) → 1 (broken) | Domain walls | 2D | Not identified |
| SO(3,1) defects | Frame singularities | Various | Standard GR singularities |

**Source:** [Topological defect — Wikipedia](https://en.wikipedia.org/wiki/Topological_defect)

**PDTP Original.** The PDTP condensate admits vortex line defects
(cosmic strings) as the natural topological excitations of the
U(1) phase field. Domain walls (2D defects) are also possible if
the condensate has multiple ground states (e.g., φ = 0 and φ = π
for the cosine potential). Higher-dimensional defects (monopoles,
textures) would require a larger symmetry group than U(1).

### 9.6 Honest Assessment

The topological analysis is the most speculative part of this
document:

- The cosmic string = phase vortex identification is **suggestive
  but not derived** — it requires showing that the PDTP condensate
  dynamics actually produce conical spacetime near a vortex core
- The dark energy connection is **purely qualitative** with no
  quantitative support
- The vortex analogy is strong for U(1) superfluids but may not
  carry over to the full two-sector PDTP structure
- No observational predictions emerge from this analysis

This section identifies **directions for future work**, not results.

---

## 10. EM–Gravity Unification Hints (Part 18)

### 10.1 The Parallel Structure (Review)

Both electromagnetism and gravity can be formulated as gauge theories
with fiber bundle structure:

| Feature | Electromagnetism | Gravity (GR) |
|---------|-----------------|-------------|
| Gauge group | U(1) (local) | SO(3,1) (local) |
| Connection | A_μ (vector potential) | ω^a_{bμ} (spin connection) |
| Field strength | F_μν (EM field) | R^a_{bμν} (Riemann tensor) |
| Matter coupling | Minimal: ∂_μ → D_μ = ∂_μ − ieA_μ | Covariant derivative with Γ |
| Charge | Electric charge e | Mass-energy |

**Source:** Weatherall, J.O. (2016), "Fiber Bundles, Yang-Mills Theory,
and General Relativity," *Synthese* 193, 2389–2425.

Both are connections on principal bundles. Both produce dynamics from
curvature. Both have conservation laws from gauge invariance (charge
conservation, energy-momentum conservation).

### 10.2 Kaluza-Klein Unification (Review)

In 1921, Kaluza showed that 5-dimensional general relativity naturally
contains both 4D gravity and electromagnetism:

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  5D metric decomposition:                                    │
│                                                              │
│  ĝ_AB  →  g_μν    (4D metric — gravity)                     │
│            A_μ     (vector potential — EM)              (10.1)│
│            Φ       (scalar — dilaton)                         │
│                                                              │
│  15 components = 10 (gravity) + 4 (EM) + 1 (scalar)         │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**Source:** [Kaluza-Klein theory — Wikipedia](https://en.wikipedia.org/wiki/Kaluza%E2%80%93Klein_theory)

The "Kaluza miracle": the 5D vacuum Einstein equations produce:
- 4D Einstein equations with EM stress-energy as source
- Maxwell's equations
- A scalar field equation

The extra dimension is compactified (rolled up) to a circle of
Planck-scale radius, explaining why it is not directly observed.

### 10.3 PDTP Perspective on EM–Gravity Parallels (PDTP Original)

In PDTP's framework, both EM and gravity involve phase coupling:

```
EM phase coupling:      ψ → exp(ieA_μ dx^μ/ℏ) ψ
PDTP gravity coupling:  L_int = g cos(ψ − φ)
```

Both describe how a matter-wave phase (ψ) interacts with a
background field (A for EM, φ for gravity). The structural parallels:

| Feature | EM Phase Coupling | PDTP Gravity Coupling |
|---------|------------------|----------------------|
| Background field | A_μ (gauge field) | φ (scalar field) |
| Coupling constant | e (charge) | g (mass-dependent) |
| Symmetry | Local U(1) | Global U(1) |
| Phase observable? | No (gauge freedom) | Yes (ψ−φ is physical) |
| Nonlinear? | No (minimal coupling is linear) | Yes (cosine coupling) |
| AB-type effect? | Yes (Tonomura 1986) | Yes (COW 1975, Overstreet 2022) |

**Key structural difference:**

EM has **local gauge invariance** — the phase can be shifted by
different amounts at different points. This requires a compensating
gauge field A_μ, which IS the electromagnetic potential.

PDTP has **global U(1) invariance** — the phase can only be shifted
by the SAME amount everywhere. No compensating gauge field is needed.

If PDTP's global U(1) were promoted to local U(1), a gauge field
would necessarily appear. The question: **is this gauge field the
electromagnetic potential?**

### 10.4 Could Gauging PDTP Produce Electromagnetism?

Consider promoting φ → φ + α(x) to a local symmetry:

```
ψ → ψ + α(x),    φ → φ + α(x)
```

The kinetic term ½(∂_μφ)(∂^μφ) is NOT invariant under local shifts.
To restore invariance, introduce a gauge field B_μ:

```
∂_μφ → D_μφ = ∂_μφ − B_μ
```

The coupling cos(ψ − φ) IS invariant (the local shift cancels).
But the kinetic terms require:

```
L = ½(D_μφ)(D^μφ) + ½(D_μψ)(D^μψ) + g cos(ψ − φ) − ¼F_μνF^μν
```

where F_μν = ∂_μB_ν − ∂_νB_μ is the field strength of B.

**This looks like a scalar field theory coupled to electromagnetism.**

However, identifying B_μ with the EM potential A_μ faces serious
obstacles:

1. **Charge quantization**: EM coupling is proportional to electric
   charge e, which is universal. PDTP coupling g is proportional to
   mass, which varies.

2. **Different coupling constants**: the EM fine structure constant
   α ≈ 1/137 has nothing to do with the gravitational coupling
   G ~ g/ρ₀.

3. **No known scalar–EM coupling of this form**: the cosine coupling
   between scalar fields is not part of the Standard Model.

4. **Kaluza-Klein does it differently**: KK unifies gravity and EM
   through extra dimensions, not through gauging a scalar phase.

### 10.5 Honest Assessment

The EM–gravity parallel in PDTP is **suggestive but not unification**:

- Both involve phase coupling: ✓ (interesting structural parallel)
- Both have fiber bundle formulation: ✓ (different bundle types)
- Both have AB-type effects: ✓ (experimentally confirmed)
- PDTP naturally produces EM from gauging: ✗ (obstacles in §10.4)
- Kaluza-Klein connection: unclear (KK uses 5D geometry, PDTP uses
  phase-locking — different mechanisms)

**PDTP Original.** The phase coupling parallel between EM and PDTP
gravity is genuine and deep — both frameworks operate through phase
relationships rather than direct forces. However, this parallel does
not constitute unification. Gauging PDTP's U(1) symmetry does not
naturally reproduce electromagnetism due to fundamental differences
in coupling constants and charge structure. The Kaluza-Klein route
remains a separate (and better-established) approach to unification.

---

## 11. Impact on Existing PDTP Results (Part 18)

### 11.1 Tetrad Extension (Part 12) — Confirmed

The fiber bundle analysis (§8) confirms that Part 12's tetrad
formulation has the correct geometric structure:

- The SO(3,1) frame bundle is the standard geometric framework
  for gravity
- The scalar phase φ on the trivial U(1) bundle provides the
  additional PDTP ingredient
- The product structure U(1)_global × SO(3,1) is geometrically
  consistent

**No modifications needed.** The existing tetrad extension is
compatible with the fiber bundle classification.

### 11.2 Gravitational Waves (Parts 12–13) — No Change

The topological analysis (§9) raises the theoretical possibility
of GW scattering from phase vortices (cosmic strings), but:

- Cosmic string GW signatures are already studied in standard GR
- PDTP does not add new predictions for GW–cosmic string interaction
- The breathing mode GW (PDTP-specific) is unaffected by topological
  considerations

**No modifications needed.**

### 11.3 COW Experiment — Consistency Verified

The derivation in §7 confirms that PDTP reproduces the COW phase
shift exactly:

- This is required by the weak-field limit agreement with Newton
- It does not provide a new test of PDTP vs. GR
- The Overstreet et al. (2022) result further confirms that
  gravitational phases are physically real

**Constraint:** Any future modification of PDTP must continue to
reproduce the COW result. This is a necessary (but not sufficient)
condition for consistency.

### 11.4 New Experimental Connections

The deeper AB analysis identifies two potential experimental
directions:

1. **Precision gravitational phase measurements**: Atom interferometry
   (Overstreet et al. type) could potentially detect PDTP-specific
   phase corrections — but only if the scalar sector contributes
   measurably. The Cassini bound (ε_s < 10⁻⁵ from Part 7) severely
   constrains this.

2. **Cosmic string observations**: If cosmic strings are condensate
   vortices (§9.3), then:
   - Their properties would be constrained by condensate physics
   - Their formation mechanism would be a cosmological phase
     transition
   - Observational limits on cosmic strings constrain PDTP's
     condensate parameters

   However, no cosmic strings have been definitively observed.

### 11.5 Summary of Impact

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  Impact of AB/Phase Analysis on Previous Results:            │
│                                                              │
│  Tetrad extension (Part 12):     CONFIRMED (consistent)      │
│  Gravitational waves (Part 12–13): NO CHANGE                 │
│  COW experiment:                 CONSISTENCY VERIFIED         │
│  Binary pulsar (Part 13):       NO CHANGE                    │
│  Cosmological constant (Part 17): CONNECTED (via vortices)   │
│                                                              │
│  No existing results need modification.                      │
│  The geometric/topological analysis deepens understanding    │
│  without altering predictions.                               │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**PDTP Original.** The deeper AB analysis confirms that PDTP's
existing mathematical structure is geometrically consistent. The
fiber bundle classification (U(1)_global × SO(3,1)) correctly
captures the two-sector structure. Topological considerations
(vortices, cosmic strings) open new interpretive directions but
do not modify existing predictions.

---

## 12. Remaining Open Questions (Part 18)

The deeper analysis has addressed the five research questions
posed in the preliminary analysis (§7 of the original document).
Here is the updated status:

| Original Question | Status | Where Addressed |
|------------------|--------|-----------------|
| Fiber bundle formulation | **Completed** — classified as U(1)_global × SO(3,1) | §8 |
| COW experiment derivation | **Completed** — matches standard QM exactly | §7 |
| Topological aspects | **Explored** — vortex = cosmic string identification | §9 |
| EM–gravity unification | **Analyzed** — parallel identified, not unification | §10 |
| Impact on existing results | **Assessed** — no modifications needed | §11 |

### 12.1 New Open Questions

The analysis has raised new questions:

1. **Vortex dynamics in the PDTP condensate**
   - Do the field equations □φ = Σ gᵢ sin(ψᵢ − φ) admit vortex
     solutions?
   - What is the energy per unit length of a PDTP vortex?
   - Does this match the cosmic string linear density μ?

2. **Local vs. global U(1)**
   - Is there a physical reason to promote PDTP's global U(1) to
     local? Would this generate EM?
   - What constrains the symmetry structure from observation?

3. **Condensate phase transition**
   - If cosmic strings are phase vortices, they should form during
     a cosmological phase transition at temperature T_c
   - What is T_c for the spacetime condensate?
   - Does this connect to the condensate microphysics (Part 14)?

4. **Scalar sector phase corrections**
   - Can precision atom interferometry (beyond COW) detect
     PDTP-specific phase corrections?
   - What is the predicted size of the correction? (Likely
     suppressed by Cassini bound ε_s < 10⁻⁵)

---

## 13. References

### Standard Physics

**Source:** Aharonov, Y. & Bohm, D. (1959), "Significance of electromagnetic
potentials in the quantum theory," *Physical Review* 115(3), 485–491.

**Source:** Tonomura, A. et al. (1982), "Observation of Aharonov-Bohm Effect
by Electron Holography," *Physical Review Letters* 48(21), 1443–1446.

**Source:** Tonomura, A. et al. (1986), "Evidence for Aharonov-Bohm effect
with magnetic field completely shielded from electron wave,"
*Physical Review Letters* 56(8), 792–795.

**Source:** Colella, R., Overhauser, A.W. & Werner, S.A. (1975),
"Observation of gravitationally induced quantum interference,"
*Physical Review Letters* 34, 1472–1474.

**Source:** Overstreet, C. et al. (2022), "Observation of a gravitational
Aharonov-Bohm effect," *Science* 375, 226–229.

**Source:** Weatherall, J.O. (2016), "Fiber Bundles, Yang-Mills Theory,
and General Relativity," *Synthese* 193, 2389–2425.

**Source:** [Aharonov-Bohm effect — Wikipedia](https://en.wikipedia.org/wiki/Aharonov%E2%80%93Bohm_effect)

**Source:** [COW experiment — Wikipedia](https://en.wikipedia.org/wiki/Colella%E2%80%93Overhauser%E2%80%93Werner_experiment)

**Source:** [Hitachi — Verification of the Aharonov-Bohm effect](https://www.hitachi.com/rd/research/materials/quantum/aharonov-bohm/index.html)

**Source:** [Meissner effect — Wikipedia](https://en.wikipedia.org/wiki/Meissner_effect)

**Source:** [Connection (fiber bundle) — Wikipedia](https://en.wikipedia.org/wiki/Connection_(mathematics))

**Source:** [Fiber bundle — Wikipedia](https://en.wikipedia.org/wiki/Fiber_bundle)

**Source:** [Frame bundle — Wikipedia](https://en.wikipedia.org/wiki/Frame_bundle)

**Source:** [Quantum vortex — Wikipedia](https://en.wikipedia.org/wiki/Quantum_vortex)

**Source:** [Superfluid helium-4 — Wikipedia](https://en.wikipedia.org/wiki/Superfluid_helium-4)

**Source:** [Cosmic string — Wikipedia](https://en.wikipedia.org/wiki/Cosmic_string)

**Source:** [Topological defect — Wikipedia](https://en.wikipedia.org/wiki/Topological_defect)

**Source:** [Kaluza-Klein theory — Wikipedia](https://en.wikipedia.org/wiki/Kaluza%E2%80%93Klein_theory)

**Source:** [Neutron interferometer — Wikipedia](https://en.wikipedia.org/wiki/Neutron_interferometer)

**Source:** [Path integral formulation — Wikipedia](https://en.wikipedia.org/wiki/Path_integral_formulation)

### PDTP Original Analysis (Preliminary — §§1–6)

**PDTP Original:** Structural parallel between AB electromagnetic phase
coupling and PDTP gravitational phase coupling (§3)

**PDTP Original:** Tonomura ring as phase-drift analogy for PDTP coupling
suppression (§3.3)

**PDTP Original:** EM–gravity phase analogy table and comparison (§3.4)

**PDTP Original:** AB effect as experimental precedent for PDTP's
phase-centric worldview (§5)

### PDTP Original Analysis (Deep Analysis — §§7–12)

**PDTP Original:** COW experiment derivation from PDTP Lagrangian — matches
standard QM exactly via weak-field limit (§7.3)

**PDTP Original:** Overstreet et al. (2022) as strongest experimental
support for PDTP's phase-centric paradigm (§7.5)

**PDTP Original:** Fiber bundle classification of PDTP: U(1)_global ×
SO(3,1) product bundle structure (§8.3, §8.4)

**PDTP Original:** Structural comparison table — trivial U(1) (PDTP)
vs non-trivial U(1) (EM) bundle (§8.3)

**PDTP Original:** Cosmic strings interpreted as quantized vortex lines
in the spacetime condensate phase field (§9.3)

**PDTP Original:** Deficit angle ↔ phase winding number topological
identification (§9.3)

**PDTP Original:** Topological classification of PDTP defects: vortex
lines and possible domain walls from U(1) symmetry breaking (§9.5)

**PDTP Original:** EM–gravity phase coupling parallel analysis — genuine
structural parallel, not unification (§10.3, §10.5)

**PDTP Original:** Analysis of gauging PDTP U(1) — obstacles to EM
emergence identified (§10.4)

**PDTP Original:** Assessment of impact on all previous Parts — no
modifications needed, geometric consistency confirmed (§11)

---

End of aharonov_bohm_pdtp.md
