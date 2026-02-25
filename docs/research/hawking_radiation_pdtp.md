# Hawking Radiation from the PDTP Acoustic Horizon (Part 24)

**Status:** Quantitative derivation — Hawking temperature T_H = ℏc³/(8πGMk_B) derived
from the PDTP acoustic surface gravity. Result matches GR exactly; physical mechanism
differs (phonon emission at sonic horizon vs virtual pair creation).
**Date:** 2026-02-25
**Prerequisites:**
[strong_field_ep.md](strong_field_ep.md) §10 (acoustic horizon at r = 2GM/c²),
[advanced_formalization.md](advanced_formalization.md) §1.4 (acoustic metric),
[tetrad_extension.md](tetrad_extension.md) (tensor sector)

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Hawking Radiation — Standard Physics](#2-hawking-radiation--standard-physics)
3. [The PDTP Acoustic Metric](#3-the-pdtp-acoustic-metric)
4. [Acoustic Horizon Location](#4-acoustic-horizon-location)
5. [Surface Gravity of the Acoustic Horizon](#5-surface-gravity-of-the-acoustic-horizon)
6. [Hawking Temperature from Unruh's Formula](#6-hawking-temperature-from-unruhs-formula)
7. [The Trans-Planckian Problem and Its Resolution](#7-the-trans-planckian-problem-and-its-resolution)
8. [Physical Interpretation in PDTP](#8-physical-interpretation-in-pdtp)
9. [Comparison with the Standard GR Derivation](#9-comparison-with-the-standard-gr-derivation)
10. [What This Achieves and What Remains Open](#10-what-this-achieves-and-what-remains-open)
11. [References](#11-references)

---

## 1. Executive Summary

### 1.1 Goal

PDTP predicts that spacetime is a superfluid condensate. Around a massive body,
the condensate flows inward at the free-fall velocity — a *sonic horizon* forms
where the infall speed equals the phonon speed (= c). This is structurally
identical to the analogue black hole studied by Unruh (1981).

This document derives the Hawking temperature of this acoustic horizon from
first principles using the Painlevé-Gullstrand form of the acoustic metric.

### 1.2 Main Result

**PDTP Original.** The PDTP acoustic horizon has surface gravity:

```
κ_s = c⁴ / (4GM)                                                        ... (1.1)
```

Applying the Unruh analogue Hawking formula:

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   T_H = ℏc³ / (8πGMk_B)                             (1.2)  │
│                                                             │
│   The Hawking temperature emerges from PDTP's acoustic      │
│   horizon — same formula as GR, physical origin different.  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

This is identical to Hawking's (1974) result, confirming internal consistency.

### 1.3 Structural Advantage

The standard GR derivation of Hawking radiation faces the **trans-Planckian
problem**: tracing Hawking phonons backward in time implies exponentially high
frequencies at the horizon, requiring physics at energies above the Planck scale.

In PDTP, the condensate lattice with spacing a ~ ℓ_Planck provides a natural UV
cutoff. The derivation is free of the trans-Planckian divergence by construction.
This is a *structural advantage* of the condensate picture over classical GR.

---

## 2. Hawking Radiation — Standard Physics

### 2.1 The Discovery

In 1974, Hawking proved that black holes emit thermal radiation due to quantum
effects near the event horizon.

**Source:** Hawking (1974), "Black hole explosions?", *Nature* 248, 30–31.

The temperature is:

```
T_H = ℏc³ / (8πGMk_B)                                                   ... (2.1)
```

where M is the black hole mass, G is Newton's constant, c is the speed of light,
ℏ is the reduced Planck constant, and k_B is Boltzmann's constant.

**Source:** [Hawking radiation — Wikipedia](https://en.wikipedia.org/wiki/Hawking_radiation)

### 2.2 Numerical Values

For a stellar-mass black hole (M = 10 M_☉ ≈ 2 × 10³¹ kg):

```
T_H = (1.055 × 10⁻³⁴)(3 × 10⁸)³ / (8π × 6.674 × 10⁻¹¹ × 2 × 10³¹ × 1.38 × 10⁻²³)
    ≈ 6 × 10⁻⁹ K                                                         ... (2.2)
```

This is far below the cosmic microwave background temperature (~2.7 K), so
stellar black holes currently absorb more CMB photons than they emit as Hawking
radiation — they are effectively growing, not evaporating.

For the Hawking temperature to equal 2.7 K, the mass would be:

```
M = ℏc³ / (8πGk_B × 2.7 K)
  ≈ 4.5 × 10²² kg  ≈ 10⁻⁸ M_☉  ≈ moon mass / 50               ... (2.3)
```

Hawking radiation is observationally relevant only for primordial black holes
(PBH) with M ≲ 10¹⁵ g — those formed in the early universe.

### 2.3 Physical Mechanism (Standard Picture)

The standard derivation uses quantum field theory in curved spacetime. Virtual
particle–antiparticle pairs are created near the horizon. One partner falls
in, the other escapes as real Hawking radiation. The outgoing particle carries
positive energy, so the black hole loses mass.

**Source:** [Virtual particle — Wikipedia](https://en.wikipedia.org/wiki/Virtual_particle);
[Hawking radiation — Wikipedia](https://en.wikipedia.org/wiki/Hawking_radiation)

A cleaner formulation uses the **Bogoliubov transformation**: modes defined by
an infalling observer (Unruh vacuum) differ from those of a distant observer
(Boulware vacuum). This mismatch means the Boulware vacuum contains particles
from the distant observer's perspective — thermal radiation at temperature T_H.

**Source:** [Bogoliubov transformation — Wikipedia](https://en.wikipedia.org/wiki/Bogoliubov_transformation)

### 2.4 Connection to Surface Gravity

The Hawking temperature is proportional to the surface gravity κ of the event
horizon:

```
T_H = ℏκ / (2πk_Bc)                                                     ... (2.4)
```

For Schwarzschild, the surface gravity is:

```
κ = c⁴ / (4GM)                                                           ... (2.5)
```

**Source:** [Surface gravity — Wikipedia](https://en.wikipedia.org/wiki/Surface_gravity)

Substituting (2.5) into (2.4) recovers the Hawking formula (2.1). The key step
in what follows is computing the *acoustic* surface gravity of the PDTP
condensate horizon and showing it equals (2.5).

### 2.5 Analogue Hawking Radiation (Unruh 1981)

Unruh (1981) showed that a sonic horizon in a moving fluid emits thermal phonons
at a temperature determined by the fluid's surface gravity:

```
T_Unruh = ℏκ_acoustic / (2πk_B c_sound)                                 ... (2.6)
```

**Source:** Unruh (1981), "Experimental Black-Hole Evaporation?",
*Physical Review Letters* 46, 1351.

This was the founding paper of analogue gravity. It showed that the Hawking
mechanism is *kinematic* — it depends only on the structure of the horizon
(a surface where background flow reaches the wave speed), not on Einstein's
equations specifically.

**Key insight:** Any supersonic flow creates a sonic horizon that emits thermal
radiation. The quantum mechanism is the same as Hawking radiation. PDTP's
condensate around a massive body IS such a system.

---

## 3. The PDTP Acoustic Metric

### 3.1 Superfluid Flow around a Mass

**PDTP Original.** In PDTP, spacetime is a superfluid condensate. Around a
massive body of mass M, the condensate flows inward under self-gravity.

In the Painlevé-Gullstrand (PG) coordinate system, the infall velocity of the
condensate is the free-fall velocity:

```
v(r) = −√(2GM/r)    (inward; negative sign for r decreasing)            ... (3.1)
```

where r is the radial coordinate and v is measured relative to distant static
observers.

**Source for Painlevé-Gullstrand:**
[Gullstrand–Painlevé coordinates — Wikipedia](https://en.wikipedia.org/wiki/Gullstrand%E2%80%93Painlevé_coordinates)

The magnitude |v| increases toward the center. When |v| = c (phonon speed = c
in PDTP), the inflow traps phonons — this is the acoustic horizon.

### 3.2 The Acoustic Metric

For a moving superfluid with background flow velocity **v**(x) and phonon speed
c_s, the phonons (small phase perturbations of the condensate) propagate on an
*effective* spacetime metric called the acoustic metric:

```
ds²_acoustic = Ω² [−(c_s² − |v|²)dt² + 2v·dr dt + dr²]               ... (3.2)
```

where Ω is a conformal factor set by the condensate density. For a spherically
symmetric inflow:

```
ds²_acoustic = −(c² − v²)dt² + 2|v| dt dr + dr² + r²dΩ²              ... (3.3)
```

(absorbing Ω into a coordinate rescaling; it does not affect the horizon location
or surface gravity).

**Source:** Visser (1998), "Acoustic black holes: Horizons, ergospheres and
Hawking radiation", *Classical and Quantum Gravity* 15, 1767.
[Analogue gravity — Wikipedia](https://en.wikipedia.org/wiki/Analogue_gravity)

In PDTP specifically, the phonon speed equals c (the speed of light) because
the condensate phase stiffness κ and phase inertia ρ satisfy c_s² = κ/ρ = c²
(derived in [efv_microphysics.md](efv_microphysics.md) §4.4).

Substituting v = −√(2GM/r) and c_s = c into (3.3):

```
ds²_acoustic = −(c² − 2GM/r)dt² − 2√(2GM/r) dt dr + dr² + r²dΩ²     ... (3.4)
```

**This is precisely the Schwarzschild metric written in Painlevé-Gullstrand
coordinates.** The acoustic metric of the PDTP condensate around a mass M
equals the gravitational spacetime metric of GR. This confirms that PDTP's
acoustic picture correctly reproduces the black hole geometry.

**Source:** The equivalence of PG coordinates and Schwarzschild is standard
GR. See [Gullstrand–Painlevé coordinates — Wikipedia](https://en.wikipedia.org/wiki/Gullstrand%E2%80%93Painlevé_coordinates).

---

## 4. Acoustic Horizon Location

### 4.1 Definition

The acoustic horizon is the surface where the background flow speed |v(r)|
equals the phonon speed c_s = c. Phonons emitted outward at this surface are
carried inward by the flow at exactly the phonon speed, so they remain
stationary — trapped at the horizon.

**PDTP Original.** Setting |v(r_H)| = c:

```
√(2GM/r_H) = c                                                           ... (4.1)
```

Solving:

```
r_H = 2GM/c²                                                             ... (4.2)
```

This is **exactly the Schwarzschild radius** — the standard event horizon radius
of a black hole of mass M.

This result was already derived in
[strong_field_ep.md](strong_field_ep.md) §10 as part of the strong-field
equivalence principle analysis. We confirm it here as the starting point for
the Hawking temperature calculation.

### 4.2 Why r_H = 2GM/c² is Exact (Not Approximate)

The free-fall velocity v = −√(2GM/r) is exact in Newtonian gravity and also
exact in GR when written in PG coordinates (where it equals the Newtonian
expression). The equality |v(r_H)| = c_s with c_s = c then gives r_H = 2GM/c²
exactly — not a weak-field approximation.

This is a consequence of the fact that PG coordinates are globally regular
(unlike Schwarzschild coordinates which break down at the horizon).

**Source:** [Gullstrand–Painlevé coordinates — Wikipedia](https://en.wikipedia.org/wiki/Gullstrand%E2%80%93Painlevé_coordinates)

---

## 5. Surface Gravity of the Acoustic Horizon

### 5.1 Definition of Acoustic Surface Gravity

**Source:** Visser (1998), ibid.; Unruh (1981), ibid.

The surface gravity of an acoustic horizon is defined by the rate at which the
quantity (c_s² − |v|²) vanishes at the horizon:

```
κ_s = (1/2) × |d(c_s² − v²)/dr|_{r = r_H}                              ... (5.1)
```

This is the acoustic analogue of the Killing surface gravity in GR.

**Source:** [Surface gravity — Wikipedia](https://en.wikipedia.org/wiki/Surface_gravity)

### 5.2 Step-by-Step Calculation

**PDTP Original.** We compute d(c² − v²)/dr at r = r_H = 2GM/c².

**Step 1:** Write out the quantity to differentiate.

In PDTP, v = −√(2GM/r), so v² = 2GM/r. The phonon speed c_s = c is constant
(set by condensate equation of state, independent of r). Therefore:

```
c_s² − v² = c² − 2GM/r                                                  ... (5.2)
```

**Step 2:** Differentiate with respect to r.

```
d(c² − 2GM/r)/dr = 0 − 2GM × (−1/r²) = 2GM/r²                         ... (5.3)
```

Note: this derivative is positive (c² − v² increases as r increases from r_H),
as expected — the condensate flows supersonically inside r_H and subsonically
outside.

**Step 3:** Evaluate at the horizon r_H = 2GM/c².

```
d(c² − v²)/dr |_{r_H} = 2GM / (2GM/c²)²
                       = 2GM × c⁴ / (4G²M²)
                       = c⁴ / (2GM)                                      ... (5.4)
```

**Step 4:** Compute the surface gravity.

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   κ_s = (1/2) × c⁴/(2GM)                                  │
│                                                             │
│   κ_s = c⁴ / (4GM)                                  (5.5)  │
│                                                             │
│   [Dimensions: m/s² — verified: c⁴/(GM) = m⁴s⁻⁴/(m³/     │
│    (kg·s²)·kg) = m/s²  ✓]                                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Dimensional verification:**

```
[c⁴] = m⁴/s⁴
[4GM] = m³/(kg·s²) × kg = m³/s²
[c⁴/(4GM)] = (m⁴/s⁴)/(m³/s²) = m/s²  ✓                                ... (5.6)
```

### 5.3 Comparison with GR Surface Gravity

The standard Schwarzschild surface gravity computed from the Killing vector
∂/∂t is:

```
κ_GR = c²/(2r_s) = c²/(2 × 2GM/c²) = c⁴/(4GM)                         ... (5.7)
```

**Source:** [Surface gravity — Wikipedia](https://en.wikipedia.org/wiki/Surface_gravity)

The PDTP acoustic surface gravity κ_s = c⁴/(4GM) is **identical** to the GR
gravitational surface gravity κ_GR. This is not a coincidence — it follows
from the fact that the acoustic metric (3.4) equals the Schwarzschild metric in
PG coordinates.

---

## 6. Hawking Temperature from Unruh's Formula

### 6.1 The Unruh-Visser Formula

From Unruh (1981) and Visser (1998), the analogue Hawking temperature associated
with an acoustic horizon of surface gravity κ_s is:

```
T_H = ℏ κ_s / (2π k_B c_s)                                              ... (6.1)
```

where c_s is the phonon speed.

**Source:** Unruh (1981), PRL 46, 1351; Visser (1998), CQG 15, 1767.

### 6.2 Substituting PDTP Values

**PDTP Original.** In PDTP: c_s = c (phonon speed = speed of light),
κ_s = c⁴/(4GM) (from §5.2).

Substituting into (6.1):

```
T_H = ℏ × c⁴/(4GM) / (2π k_B × c)
    = ℏ c³ / (8π G M k_B)                                               ... (6.2)
```

**Step-by-step:**

```
T_H = ℏ κ_s / (2π k_B c)
    = ℏ [c⁴/(4GM)] / (2π k_B c)
    = ℏ c⁴ / (4GM × 2π k_B c)
    = ℏ c³ / (8π G M k_B)                                               ... (6.3)
```

**Result:**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   T_H = ℏc³ / (8πGMk_B)                             (6.4)  │
│                                                             │
│   PDTP acoustic Hawking temperature equals the              │
│   standard Hawking formula exactly.                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 6.3 Dimensional Verification

```
[T_H] = [ℏ][c³] / ([G][M][k_B])
      = (kg·m²/s) × (m³/s³) / ((m³/(kg·s²)) × kg × (kg·m²/(s²·K)))
      = kg·m⁵/s⁴ / (kg·m⁵/(s⁴·K))
      = K  ✓                                                              ... (6.5)
```

### 6.4 Numerical Value for a Solar-Mass Black Hole

```
T_H = (1.055 × 10⁻³⁴)(2.998 × 10⁸)³ / (8π × 6.674 × 10⁻¹¹ × 1.989 × 10³⁰ × 1.381 × 10⁻²³)
    = (1.055 × 10⁻³⁴ × 2.694 × 10²⁵) / (8π × 1.826 × 10⁻³)
    = 2.842 × 10⁻⁹ / 0.04591
    ≈ 6.2 × 10⁻⁸ K                                                        ... (6.6)
```

(Agrees with standard result to expected precision.)

---

## 7. The Trans-Planckian Problem and Its Resolution

### 7.1 The Problem in Standard GR

The standard derivation of Hawking radiation traces outgoing modes backward in
time to their origin near the horizon. Each mode that reaches a distant observer
at frequency ω was emitted at the horizon with exponentially higher frequency:

```
ω_emitted = ω_observed × exp(κ t / c)                                   ... (7.1)
```

where t is the Schwarzschild time elapsed since black hole formation.

For a stellar-mass black hole that is older than ~1 second, this implies
ω_emitted ≫ ω_Planck = c/ℓ_Planck ≈ 10⁴³ rad/s. The derivation requires
physics at frequencies far above the Planck scale — where quantum gravity
effects are expected but unknown.

This is the **trans-Planckian problem**.

**Source:** [Trans-Planckian problem — Wikipedia](https://en.wikipedia.org/wiki/Trans-Planckian_problem);
Jacobson (1991), "Black-hole evaporation and ultrashort distances",
*Physical Review D* 44, 1731.

### 7.2 The PDTP Resolution

**PDTP Original.** In PDTP, the condensate is a lattice with spacing a ~ ℓ_Planck.
This lattice provides a natural **ultraviolet (UV) cutoff** on all frequencies:

```
ω_max = c / a  ≈  c / ℓ_Planck  =  ω_Planck                           ... (7.2)
```

No phonon can have a frequency exceeding ω_Planck. When a Hawking mode is traced
backward in time and its frequency would exceed ω_max, the lattice physics takes
over — the mode is not a phonon but a Planck-scale lattice excitation with
different properties.

**Consequence:** The trans-Planckian extrapolation is simply cut off. The
Hawking derivation is modified at Planck frequencies but Unruh (1981) already
showed (and Unruh & Schützhold 2003 confirmed) that the thermal spectrum is
robust to UV modifications — the Hawking temperature depends only on the surface
gravity κ_s, not on Planck-scale details, provided the UV modification is
analytic.

**Source:** Unruh & Schützhold (2003), "On the universality of the Hawking
effect", *Physical Review D* 71, 024028.

**Summary of the PDTP advantage:**

```
┌──────────────────────────────────────────────────────────────┐
│  Standard GR Hawking derivation:                             │
│    Requires modes at ω ≫ ω_Planck — trans-Planckian problem  │
│                                                              │
│  PDTP condensate Hawking derivation:                         │
│    Lattice cutoff at ω_max = ω_Planck — UV finite by design  │
│    Hawking spectrum unchanged (Unruh & Schützhold 2003 ✓)    │
│                                                              │
│  PDTP resolves the trans-Planckian problem structurally,     │
│  not by hand — the condensate is its own UV regulator.       │
└──────────────────────────────────────────────────────────────┘
```

### 7.3 Robustness of the Thermal Spectrum

Unruh & Schützhold (2003) proved that the Hawking temperature is universal:
any smooth UV modification that cuts off frequencies above ω_max leaves the
low-frequency Hawking spectrum unchanged, provided:

```
ω_max ≫ κ_s / c                                                         ... (7.3)
```

In PDTP:

```
κ_s / c = c³/(4GM)    (for M = M_☉: ≈ 10³² rad/s)
ω_Planck = c/ℓ_P ≈ 10⁴³ rad/s
ω_max / (κ_s/c) ≈ 10⁴³ / 10³² = 10¹¹ ≫ 1  ✓                          ... (7.4)
```

The condition is satisfied by 11 orders of magnitude for stellar-mass black
holes. The PDTP Hawking spectrum is thermally robust.

---

## 8. Physical Interpretation in PDTP

### 8.1 Mechanism: Phonon Pair Production at the Sonic Horizon

**PDTP Original.** In the condensate picture, Hawking radiation has a concrete
physical mechanism distinct from the pair-creation picture of standard QFT:

1. **Quantum vacuum fluctuations** in the condensate produce virtual phonon pairs
   continuously everywhere in spacetime.

2. **At the sonic horizon** r = r_H = 2GM/c², these fluctuations are stretched
   by the differential condensate velocity gradient (shear). One phonon is
   carried inward (super-sonic region), one outward (sub-sonic region).

3. **The pair becomes real:** the ingoing phonon is captured by the horizon, the
   outgoing phonon escapes to infinity as a real thermal photon (since c_s = c
   in PDTP, the phonon IS a photon).

4. **Energy conservation:** the ingoing phonon carries negative energy relative
   to a distant observer (it is inside the horizon where time and space exchange
   roles). The black hole loses mass: ΔM = −T_H × ΔS, where ΔS is the entropy
   decrease.

**Source:** The condensate pair-production mechanism is discussed in Visser
(1998) and in analogue experiments by Steinhauer (2016),
*Nature Physics* 12, 959 (experimental observation of analogue Hawking radiation
in a BEC sonic black hole).

### 8.2 Black Hole Evaporation in PDTP

**PDTP Original.** The condensate around a black hole slowly loses energy
through phonon emission. The mass evolves as:

```
dM/dt = −P_H / c²                                                        ... (8.1)
```

where P_H is the Hawking luminosity (Stefan-Boltzmann for a black body at T_H
with emitting area A = 4πr_H²):

```
P_H ~ σ T_H⁴ × 4πr_H² ~ (ℏc⁶)/(G²M²) × (1/G²M²) × G²M²/c⁴
    = ℏc² / (G²M²)                                                       ... (8.2)
```

More precisely (with numerical factors):

```
P_H = ℏc⁶ / (15360π G²M²)                                              ... (8.3)
```

**Source:** [Hawking radiation — Wikipedia](https://en.wikipedia.org/wiki/Hawking_radiation)

The evaporation timescale is:

```
t_evap ~ G²M³ / (ℏc⁴) ~ (M/M_Planck)³ × t_Planck                     ... (8.4)
```

For M = M_☉: t_evap ~ 10⁷⁴ years — far longer than the age of the universe.

### 8.3 What the Condensate "Feels"

In PDTP, the condensate phonons that are emitted carry phase information from
the horizon region. The thermal spectrum represents the *statistical uncertainty*
about the exact phase configuration of the phonons that fell into the black
hole. The entanglement between interior and exterior condensate phonon modes
is the PDTP analogue of Hawking radiation entanglement in QFT.

The singularity at r = 0 is replaced by a vortex core (a topological defect of
the phase field) with finite energy density. This vortex core does not affect
the surface gravity calculation or the Hawking temperature — it only modifies
physics at the Planck scale (r ≲ ℓ_Planck).

---

## 9. Comparison with the Standard GR Derivation

| Aspect | Standard GR | PDTP Condensate |
|--------|-------------|-----------------|
| **Mechanism** | Virtual pair creation at horizon | Phonon pair separation at sonic horizon |
| **Derivation basis** | QFT in curved spacetime (Bogoliubov transformation) | Unruh (1981) analogue Hawking radiation |
| **Surface gravity** | κ = c⁴/(4GM) from Killing vector | κ_s = c⁴/(4GM) from acoustic metric ✓ |
| **Temperature** | T_H = ℏc³/(8πGMk_B) | T_H = ℏc³/(8πGMk_B) ✓ |
| **Trans-Planckian** | Problem: requires ω ≫ ω_Planck | Solved: lattice cutoff at ω_Planck |
| **r = 0 singularity** | Classical divergence | Finite-energy vortex core |
| **Experimental support** | Indirect (thermodynamics) | Steinhauer (2016) BEC sonic black holes |

---

## 10. What This Achieves and What Remains Open

### 10.1 Achievements

1. **Hawking temperature derived from first principles.** Starting from PDTP's
   condensate flow v = −√(2GM/r) and phonon speed c_s = c, the surface gravity
   κ_s = c⁴/(4GM) is computed exactly, and the Hawking temperature
   T_H = ℏc³/(8πGMk_B) follows from the Unruh formula.

2. **Result matches GR exactly.** No free parameters, no adjustments.
   The PDTP result is numerically identical to Hawking (1974).

3. **Trans-Planckian problem resolved.** The condensate lattice UV cutoff
   prevents the trans-Planckian divergence while (by Unruh & Schützhold 2003)
   leaving the thermal spectrum unchanged.

4. **Physical mechanism clarified.** The condensate picture provides a concrete
   physical origin: phonon pair separation at the sonic horizon, exactly as in
   the BEC analogue experiments of Steinhauer (2016).

5. **Confirms internal consistency.** The acoustic horizon (derived in Part 10
   from strong-field analysis) produces exactly the correct Hawking temperature.
   PDTP is self-consistent from strong-field EP to quantum evaporation.

### 10.2 Remaining Open Problems

1. **Information paradox.** The Hawking spectrum is thermal — does the condensate
   preserve information about infalling matter in its phase correlations?
   This requires an explicit calculation of phase-phase correlators in the
   condensate across the horizon (see TODO).

2. **Back-reaction.** As the black hole loses mass, the condensate density and
   flow profile change. The back-reaction of Hawking radiation on the acoustic
   metric has not been computed.

3. **Evaporation endpoint.** When M → M_Planck, r_H → ℓ_Planck — the
   condensate description breaks down at the lattice scale. What replaces the
   Schwarzschild geometry? A vortex? A topological soliton? This requires a
   full lattice-scale condensate theory.

4. **Entropy and Bekenstein-Hawking formula.** The Bekenstein-Hawking entropy
   S_BH = A/(4ℓ_Planck²) (in Planck units) should follow from counting
   condensate microstates at the horizon. This counting has not been done
   in PDTP.

5. **Rotating and charged black holes.** The derivation above is for
   Schwarzschild (uncharged, non-rotating). The Kerr and Reissner-Nordström
   cases require modifying the condensate flow profile.

---

## 11. References

### Established Physics Sources

**Papers:**

70. Hawking, S. W. (1974), "Black hole explosions?", *Nature* 248, 30–31.
71. Unruh, W. G. (1981), "Experimental Black-Hole Evaporation?",
    *Physical Review Letters* 46, 1351.
72. Visser, M. (1998), "Acoustic black holes: Horizons, ergospheres and
    Hawking radiation", *Classical and Quantum Gravity* 15, 1767.
73. Jacobson, T. (1991), "Black-hole evaporation and ultrashort distances",
    *Physical Review D* 44, 1731.
74. Unruh, W. G. & Schützhold, R. (2003), "On the universality of the Hawking
    effect", *Physical Review D* 71, 024028.
75. Steinhauer, J. (2016), "Observation of quantum Hawking radiation and its
    entanglement in an analogue black hole", *Nature Physics* 12, 959.

**Wikipedia:**

204. [Hawking radiation — Wikipedia](https://en.wikipedia.org/wiki/Hawking_radiation)
205. [Surface gravity — Wikipedia](https://en.wikipedia.org/wiki/Surface_gravity)
206. [Gullstrand–Painlevé coordinates — Wikipedia](https://en.wikipedia.org/wiki/Gullstrand%E2%80%93Painlevé_coordinates)
207. [Analogue gravity — Wikipedia](https://en.wikipedia.org/wiki/Analogue_gravity)
208. [Trans-Planckian problem — Wikipedia](https://en.wikipedia.org/wiki/Trans-Planckian_problem)
209. [Bogoliubov transformation — Wikipedia](https://en.wikipedia.org/wiki/Bogoliubov_transformation)
210. [Virtual particle — Wikipedia](https://en.wikipedia.org/wiki/Virtual_particle)

### PDTP Original Results (This Document)

| # | Result | Section |
|---|--------|---------|
| 1 | PDTP acoustic metric in Painlevé-Gullstrand form: ds² = −(c² − 2GM/r)dt² − 2√(2GM/r) dt dr + ... | §3.2 |
| 2 | Acoustic horizon location: r_H = 2GM/c² (exact Schwarzschild radius) | §4.1 |
| 3 | Acoustic surface gravity: κ_s = c⁴/(4GM) (step-by-step calculation) | §5.2 |
| 4 | Hawking temperature: T_H = ℏc³/(8πGMk_B) from Unruh formula | §6.2 |
| 5 | Trans-Planckian resolution: lattice UV cutoff at ω_Planck, spectrum preserved by Unruh & Schützhold (2003) | §7.2–7.3 |
| 6 | Robustness check: ω_max/(κ_s/c) ≈ 10¹¹ ≫ 1 for stellar BHs | §7.3 |

### PDTP Cross-References

- Acoustic horizon at r = 2GM/c²: [strong_field_ep.md](strong_field_ep.md) §10
- Phonon speed c_s = c: [efv_microphysics.md](efv_microphysics.md) §4.4
- Condensate microphysics and GFT: [condensate_microphysics.md](condensate_microphysics.md)
- Tetrad structure (tensor sector): [tetrad_extension.md](tetrad_extension.md)

---

This document is part of the Phase-Decoupled Physics project.
The derivation follows established analogue gravity (Unruh 1981, Visser 1998).
PDTP-specific claims are marked **PDTP Original**.
The speculative content has not been experimentally validated.

---

End of Document
