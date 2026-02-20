# Condensate Tetrad Extension (Part 12)

This document extends the PDTP mathematical formalization by constructing an
explicit tetrad extension of the condensate order parameter. The scalar PDTP
Lagrangian (Parts 1–11) produces only one GW polarization mode (breathing).
LIGO observations confirm two tensor modes. Here we write the extended
Lagrangian that produces both tensor and breathing modes, derive its field
equations, perform linearized perturbation analysis, and verify consistency
with all previous results.

**Prerequisite reading:**
- [mathematical_formalization.md](mathematical_formalization.md) (Part 1) — Lagrangian, field equations
- [advanced_formalization.md](advanced_formalization.md) (Part 2) — SVT identification, post-Newtonian
- [hard_problems.md](hard_problems.md) §1 — GW polarization analysis, §1.10 tetrad status

Every established result is cited. Every new result is marked as PDTP Original.

---

## Table of Contents

1. [Motivation and Problem Statement](#1-motivation-and-problem-statement)
2. [The He-3A Paradigm](#2-the-he-3a-paradigm)
3. [Extended PDTP Order Parameter](#3-extended-pdtp-order-parameter)
4. [The Extended Lagrangian](#4-the-extended-lagrangian)
5. [Field Equations from the Extended Lagrangian](#5-field-equations-from-the-extended-lagrangian)
6. [Linearized Perturbation Analysis](#6-linearized-perturbation-analysis)
7. [Recovery of Existing PDTP Results](#7-recovery-of-existing-pdtp-results)
8. [Symmetry Breaking Analysis](#8-symmetry-breaking-analysis)
9. [New Predictions](#9-new-predictions-from-the-extension)
10. [Honest Assessment](#10-honest-assessment)
11. [Summary of Results](#11-summary-of-results)
12. [References](#12-references)

---

## 1. Motivation and Problem Statement

### 1.1 The Polarization Problem

The scalar PDTP Lagrangian from Part 1 is:

```
L_scalar = ½(∂_μ φ)(∂^μ φ) + Σᵢ ½(∂_μ ψᵢ)(∂^μ ψᵢ) + Σᵢ gᵢ cos(ψᵢ − φ)   ... (1.1)
```

The field equation outside matter is □φ = 0. This is the massless Klein-Gordon
equation, whose solutions are scalar waves with **one** polarization degree of
freedom — the breathing mode (isotropic expansion/contraction transverse to
propagation).

**Source:** [Klein-Gordon equation — Wikipedia](https://en.wikipedia.org/wiki/Klein%E2%80%93Gordon_equation)

In the E(2) classification of gravitational wave polarizations, the scalar PDTP
belongs to class O₁ (one breathing mode only).

**Source:** Eardley, D. M., Lee, D. L., Lightman, A. P. (1973), "Gravitational-Wave
Observations as a Tool for Testing Relativistic Gravity," *Phys. Rev. Lett.*, 30, 884.

### 1.2 What LIGO Observes

LIGO/Virgo observations of binary black hole and binary neutron star mergers are
consistent with General Relativity's prediction of exactly two tensor (spin-2)
polarization modes: h₊ (plus) and h₊ (cross). These are transverse-traceless
perturbations of the spatial metric.

**Source:** LIGO Scientific Collaboration and Virgo Collaboration (2017), "GW170814:
A Three-Detector Observation of Gravitational Waves from a Binary-Black-Hole
Coalescence," *Phys. Rev. Lett.*, 119, 141101.

### 1.3 The Gap

| Feature | Scalar PDTP | Observations | Required |
|---------|------------|--------------|----------|
| Tensor modes (h₊, h×) | 0 | 2 (confirmed) | 2 |
| Breathing mode | 1 | < 10⁻⁵ relative | 1 (suppressed) |
| E(2) class | O₁ | N₂ (GR) or N₃ | N₃ |

To match observations, PDTP must produce tensor modes. The scalar Lagrangian
(1.1) cannot do this — a scalar field has no tensor degrees of freedom. The
condensate order parameter must be extended to carry internal geometric structure.

### 1.4 The Physical Precedent

Superfluid helium-3 in the A-phase (He-3A) provides a concrete physical example
where a condensate with internal vector structure produces emergent spin-2
excitations that obey the linearized Einstein equations. This is Volovik's
"emergent gravity" programme.

**Source:** Volovik, G. E. (2003), *The Universe in a Helium Droplet*, Oxford
University Press, Chapter 9: "Effective gravity."

The strategy for PDTP: follow Volovik's He-3A paradigm, adapted to a
relativistic (3+1)-dimensional setting with phase-locking.

---

## 2. The He-3A Paradigm

### 2.1 The He-3A Order Parameter

In superfluid ³He-A, Cooper pairs of ³He atoms form a condensate whose order
parameter is not a scalar but a tensor:

```
A_αi = Δ · d̂_α · (m̂_i + i n̂_i)                                  ... (2.1)
```

where:
- α is a spin index, i is an orbital index
- Δ is the gap amplitude (energy scale of pairing)
- d̂ is a unit vector in spin space (3 components)
- m̂, n̂ are orthogonal unit vectors in orbital space
- l̂ = m̂ × n̂ is the orbital angular momentum direction

**Source:** Volovik, G. E. (2003), *The Universe in a Helium Droplet*, Chapter 5:
"The A-phase order parameter."

**Source:** [Superfluid helium-3 — Wikipedia](https://en.wikipedia.org/wiki/Superfluid_helium-3)

### 2.2 Symmetry Breaking in He-3A

The normal phase of ³He has the symmetry group:

```
G = SO(3)_spin × SO(3)_orbit × U(1)_phase                         ... (2.2)
```

The A-phase condensate breaks this to:

```
H = SO(2)_combined (rotations about l̂ + spin rotations about d̂)   ... (2.3)
```

**Source:** Volovik (2003), Chapter 7.

The broken generators produce Goldstone bosons. The counting:

```
dim(G) − dim(H) = 3 + 3 + 1 − 1 = 6 broken generators            ... (2.4)
```

These 6 Goldstone modes include the spin-2 excitations that become emergent
gravitons.

### 2.3 The Emergent Metric

The long-wavelength, low-energy excitations of He-3A (Bogoliubov quasiparticles)
propagate in an effective curved spacetime described by the acoustic metric:

```
g^{ij}_eff ∝ m̂^i m̂^j + n̂^i n̂^j = δ^{ij} − l̂^i l̂^j           ... (2.5)
```

This is an **emergent metric** — it arises from the condensate's internal
structure, not from fundamental spacetime curvature. The triad (m̂, n̂, l̂)
serves as an emergent **dreibein** (3-dimensional tetrad).

**Source:** Volovik (2003), Chapter 9, equation (9.10).

### 2.4 Emergent Gravitons

Perturbations of the triad vectors m̂ and n̂ around their equilibrium values
produce perturbations δg^{ij} of the emergent metric. These perturbations:

1. Are spin-2 (because the metric is a symmetric tensor)
2. Obey linearized Einstein equations at low energies
3. Propagate at the speed of the relevant collective mode

These are Volovik's **emergent gravitons**: the collective excitations of the
condensate that look like gravitational waves to low-energy observers.

**Source:** Volovik (2003), Chapter 9: "Emergent gravitons are collective modes
of the order parameter."

### 2.5 The Key Lesson

```
┌─────────────────────────────────────────────────────────────────────┐
│  He-3A Lesson for PDTP                                              │
│                                                                     │
│  1. A scalar condensate (like He-4) produces only scalar modes.     │
│  2. A tensor condensate (like He-3A) produces spin-2 modes.         │
│  3. The spin-2 modes obey linearized Einstein equations.            │
│  4. The condensate internal structure IS the emergent geometry.      │
│                                                                     │
│  Implication: PDTP must extend Φ = √ρ₀ e^{iφ} (scalar)             │
│  to include geometric (tetrad) degrees of freedom.                  │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 3. Extended PDTP Order Parameter

### 3.1 From Scalar to Tensor Order Parameter

The current PDTP vacuum condensate wavefunction is scalar:

```
Φ_scalar = √ρ₀ · exp(iφ(x,t))                                     ... (3.1)
```

This has 2 real degrees of freedom: amplitude ρ₀ and phase φ.

**PDTP Original.** We extend the order parameter to include a tetrad field:

```
Φ_extended = √ρ₀ · exp(iφ(x,t)) · e^a_μ(x,t)                     ... (3.2)
```

where e^a_μ is the **tetrad** (vierbein): a set of four vector fields (a = 0,1,2,3)
in the tangent space that define a local reference frame at each spacetime point.

**Source:** [Tetrad formalism — Wikipedia](https://en.wikipedia.org/wiki/Tetrad_formalism)

The physical metric is constructed from the tetrad as:

```
g_μν(x) = η_{ab} e^a_μ(x) e^b_ν(x)                                ... (3.3)
```

where η_{ab} = diag(−1, +1, +1, +1) is the Minkowski metric. This is the
standard tetrad-metric relationship used in GR.

### 3.2 Physical Interpretation

In the scalar PDTP (equation 3.1):
- φ encodes the **gravitational potential** (Newtonian limit: φ ↔ U)
- Gradients ∂_μ φ encode gravitational acceleration
- The metric is the flat Minkowski metric everywhere

In the extended PDTP (equation 3.2):
- φ still encodes the **scalar** gravitational degree of freedom
- e^a_μ encodes the **tensor** gravitational degrees of freedom
- Together, they define the full dynamical metric g_μν via equation (3.3)
- The condensate's internal structure IS the geometry of spacetime

This is the direct analogue of the He-3A paradigm (§2): the triad
(m̂, n̂, l̂) in He-3A plays the role of the tetrad e^a_μ in PDTP.

### 3.3 Degree of Freedom Counting

The tetrad e^a_μ has 4 × 4 = 16 components. Not all are physical:

**Gauge redundancies:**

1. **Local Lorentz invariance.** The physics is unchanged under local Lorentz
   rotations of the tangent-space index:
   ```
   e^a_μ → Λ^a_b(x) e^b_μ,    Λ ∈ SO(3,1)                        ... (3.4)
   ```
   This removes 6 degrees of freedom (the 6 parameters of the Lorentz group).

   **Source:** [Lorentz group — Wikipedia](https://en.wikipedia.org/wiki/Lorentz_group)

2. **Diffeomorphism invariance.** The physics is unchanged under coordinate
   transformations x^μ → x'^μ(x):
   ```
   e^a_μ → e^a_ν ∂x^ν/∂x'^μ                                       ... (3.5)
   ```
   This removes 4 degrees of freedom (the 4 functions x'^μ).

   **Source:** [Diffeomorphism — Wikipedia](https://en.wikipedia.org/wiki/Diffeomorphism)

**Physical degrees of freedom:**

```
16 (tetrad) − 6 (Lorentz) − 4 (diffeo) = 6 off-shell              ... (3.6)
```

Of these 6, the equations of motion further constrain 4 (the constraint
equations of GR), leaving:

```
6 − 4 (constraints) = 2 propagating tensor modes                   ... (3.7)
```

Adding the scalar sector (phase φ):

```
2 (tensor from tetrad) + 1 (breathing from φ) = 3 propagating modes ... (3.8)
```

**Source:** The standard GR DOF counting is reviewed in Wald, R. M. (1984),
*General Relativity*, University of Chicago Press, §4.4. The addition of a
scalar gives the Brans-Dicke counting.

**PDTP Original.** The extended PDTP has 3 propagating GW modes: 2 tensor
(from e^a_μ) + 1 breathing (from φ). This is E(2) class N₃, matching the
prediction stated in hard_problems.md §1.6.

### 3.4 Comparison Table

| Property | Scalar PDTP | Extended PDTP | GR |
|----------|------------|---------------|-----|
| Order parameter | √ρ₀ e^{iφ} | √ρ₀ e^{iφ} e^a_μ | g_μν |
| Field content | 1 scalar | 1 scalar + tetrad | metric |
| Propagating modes | 1 (breathing) | 3 (2 tensor + 1 breathing) | 2 (tensor) |
| E(2) class | O₁ | N₃ | N₂ |
| Phase coupling | ✓ | ✓ | — |
| Analogy | Superfluid ⁴He | Superfluid ³He-A | — |

---

## 4. The Extended Lagrangian

### 4.1 Structure

**PDTP Original.** The extended PDTP Lagrangian density is:

```
L_PDTP = L_gravity + L_phase + L_matter + L_coupling                ... (4.1)
```

We now specify each term.

### 4.2 Gravitational Sector: Palatini Action

The dynamics of the tetrad field are governed by the **Palatini action** (first-order
formulation of gravity):

```
L_gravity = (c⁴ / 16πG) · e · e^a_μ e^b_ν R^{μν}_{ab}[ω]         ... (4.2)
```

where:
- e = det(e^a_μ) is the tetrad determinant, equal to √(−g)
- R^{μν}_{ab}[ω] is the curvature (Riemann) tensor of the spin connection ω^{ab}_μ
- G is Newton's gravitational constant
- The spin connection ω^{ab}_μ is treated as an **independent** variable
  (Palatini formalism)

**Source:** [Palatini variation — Wikipedia](https://en.wikipedia.org/wiki/Palatini_variation).
The Palatini action is equivalent to the Einstein-Hilbert action for matter
without spin (the torsion-free case), but is more natural in the tetrad formalism.

**Source:** [Einstein-Cartan theory — Wikipedia](https://en.wikipedia.org/wiki/Einstein%E2%80%93Cartan_theory)

The curvature tensor is defined from the spin connection as:

```
R^{ab}_{μν} = ∂_μ ω^{ab}_ν − ∂_ν ω^{ab}_μ
              + ω^a_{cμ} ω^{cb}_ν − ω^a_{cν} ω^{cb}_μ            ... (4.3)
```

**Source:** [Spin connection — Wikipedia](https://en.wikipedia.org/wiki/Spin_connection)

### 4.3 Phase Sector (Covariantized)

The scalar phase field φ is now a field on the curved spacetime defined by the
tetrad. Its kinetic term must be covariantized:

```
L_phase = ½ · e · g^{μν} ∂_μ φ ∂_ν φ                               ... (4.4)
```

where g^{μν} is the inverse metric constructed from the tetrad:

```
g^{μν} = η^{ab} e_a^μ e_b^ν                                        ... (4.5)
```

In the flat-space limit (e^a_μ → δ^a_μ), this reduces to the original PDTP
kinetic term ½(∂_μφ)(∂^μφ).

### 4.4 Matter Sector (Covariantized)

Each matter-wave field ψᵢ is similarly covariantized:

```
L_matter = Σᵢ ½ · e · g^{μν} ∂_μ ψᵢ ∂_ν ψᵢ                       ... (4.6)
```

### 4.5 Phase-Locking Coupling

The PDTP coupling between matter phases and spacetime phase is:

```
L_coupling = Σᵢ e · gᵢ · cos(ψᵢ − φ)                               ... (4.7)
```

The factor e = √(−g) ensures the coupling is a proper scalar density, so the
action S = ∫ L d⁴x is diffeomorphism-invariant.

### 4.6 The Complete Extended Lagrangian

Combining equations (4.2), (4.4), (4.6), (4.7):

```
┌──────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│  L_PDTP = (c⁴/16πG) · e · e^a_μ e^b_ν R^{μν}_{ab}[ω]                  │
│                                                                          │
│         + ½ · e · g^{μν} ∂_μ φ ∂_ν φ                                    │
│                                                                          │
│         + Σᵢ ½ · e · g^{μν} ∂_μ ψᵢ ∂_ν ψᵢ                             │
│                                                                          │
│         + Σᵢ e · gᵢ · cos(ψᵢ − φ)                                      │
│                                                                          │
│                                                         ... (4.8)        │
│                                                                          │
│  Independent variables: e^a_μ, ω^{ab}_μ, φ, ψᵢ                         │
│  Metric: g_μν = η_{ab} e^a_μ e^b_ν                                      │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

**PDTP Original.** Equation (4.8) is the central result of this document.
It extends the scalar PDTP Lagrangian to include dynamical spacetime geometry
via the tetrad, while preserving the phase-locking mechanism that is the core
of PDTP.

### 4.7 Key Structural Features

1. **The metric couples everything.** The tetrad defines g_μν via (3.3), and
   this metric appears in L_phase, L_matter, and L_coupling. This means the
   tetrad is dynamically coupled to the phase and matter sectors: matter
   curves spacetime (through the stress-energy tensor), and spacetime
   curvature affects matter propagation.

2. **Phase-locking is preserved.** The cos(ψᵢ − φ) coupling is identical
   to the scalar PDTP, just multiplied by e for covariance. The phase-locking
   mechanism — and everything derived from it in Parts 1–11 — survives.

3. **Gravity is not postulated twice.** In the scalar PDTP, gravity emerged
   from the phase gradient ∂_μ φ. In the extended PDTP, there are two
   contributions: the scalar phase gradient AND the tensor tetrad curvature.
   These are not independent — the scalar sector is the trace part of the
   full metric dynamics. In the weak-field limit, the scalar sector dominates
   (Newtonian gravity), while the tensor sector provides the additional
   polarization modes.

4. **Palatini is natural.** Using the Palatini (first-order) formalism where
   ω and e are independent is natural for a condensate interpretation: the
   tetrad represents the condensate's frame, and the connection represents
   how that frame twists in spacetime. They are logically distinct properties
   of the condensate.

---

## 5. Field Equations from the Extended Lagrangian

### 5.1 Variation with Respect to the Spin Connection: Torsion Equation

The action is S = ∫ L_PDTP d⁴x. Varying with respect to ω^{ab}_μ:

```
δS/δω^{ab}_μ = 0                                                    ... (5.1)
```

Only L_gravity depends on ω (the matter and phase sectors couple to ω only
through the metric, and in the Palatini formalism the metric is built from
the tetrad alone). The variation gives:

```
∂_μ(e e^a_ν e^b_ρ) ε^{μνρσ} − e (e^a_ν T^b_{μσ} − e^b_ν T^a_{μσ}) = 0
```

which simplifies to the **torsion equation**:

```
T^a_{μν} ≡ ∂_μ e^a_ν − ∂_ν e^a_μ + ω^a_{bμ} e^b_ν − ω^a_{bν} e^b_μ = 0
                                                                     ... (5.2)
```

**Source:** [Torsion tensor — Wikipedia](https://en.wikipedia.org/wiki/Torsion_tensor)

**Result:** The torsion vanishes because the matter sector contains only scalar
fields (φ and ψᵢ), which have no spin. This means the spin connection equals
the Levi-Civita connection:

```
ω^{ab}_μ = ω^{ab}_μ[e]    (determined entirely by the tetrad)       ... (5.3)
```

**Source:** The vanishing of torsion for scalar matter in the Palatini formalism
is a standard result. See Carroll, S. (2004), *Spacetime and Geometry*, §3.5.

**Physical meaning:** The condensate has no intrinsic twist (torsion). The
connection is entirely determined by the tetrad — the condensate's geometry
is Riemannian (not Riemann-Cartan). If fermionic matter is added, torsion
would reappear (see §9.3).

### 5.2 Variation with Respect to the Tetrad: Einstein Equation

Varying the action with respect to e^a_μ and using ω = ω[e] from (5.3):

```
δS/δe^a_μ = 0                                                       ... (5.4)
```

The gravitational sector gives the Einstein tensor G_μν. The matter sectors
give the stress-energy tensor T_μν. The result is:

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  G_μν = (8πG/c⁴) T_μν                                       │
│                                                              │
│  where: T_μν = T^(φ)_μν + Σᵢ T^(ψᵢ)_μν + T^(coupling)_μν  │
│                                              ... (5.5)       │
└──────────────────────────────────────────────────────────────┘
```

**Source:** [Einstein field equations — Wikipedia](https://en.wikipedia.org/wiki/Einstein_field_equations)

The individual stress-energy contributions are:

**Phase field contribution:**

```
T^(φ)_μν = ∂_μ φ ∂_ν φ − ½ g_μν (∂_α φ)(∂^α φ)                   ... (5.6)
```

**Source:** The stress-energy tensor of a minimally coupled scalar field is
standard. See [Stress-energy tensor — Wikipedia](https://en.wikipedia.org/wiki/Stress%E2%80%93energy_tensor).

**Matter field contribution (each species):**

```
T^(ψᵢ)_μν = ∂_μ ψᵢ ∂_ν ψᵢ − ½ g_μν (∂_α ψᵢ)(∂^α ψᵢ)           ... (5.7)
```

**Coupling contribution:**

```
T^(coupling)_μν = −g_μν · Σᵢ gᵢ cos(ψᵢ − φ)                       ... (5.8)
```

This comes from the variation of e · gᵢ cos(ψᵢ − φ) with respect to the
metric. The coupling acts as a cosmological-constant-like term in the
stress-energy — it contributes to the energy density and pressure but has
no momentum flow.

**PDTP Original.** The coupling stress-energy (5.8) is a distinctive feature
of the extended PDTP. When all phases are aligned (ψᵢ = φ), the coupling
energy density is −Σ gᵢ (negative, like a cosmological constant). When
phases are misaligned, this energy increases. The coupling acts as a
potential energy stored in the phase difference.

### 5.3 Variation with Respect to φ: Covariant Phase Field Equation

Varying the action with respect to φ:

```
δS/δφ = 0
```

gives:

```
∂_μ(e g^{μν} ∂_ν φ) = e · Σᵢ gᵢ sin(ψᵢ − φ)
```

Dividing by e and recognizing the covariant d'Alembertian □_g:

```
┌──────────────────────────────────────────────────────────┐
│                                                          │
│  □_g φ = Σᵢ gᵢ sin(ψᵢ − φ)                             │
│                                              ... (5.9)   │
│                                                          │
│  where □_g φ ≡ (1/√(−g)) ∂_μ(√(−g) g^{μν} ∂_ν φ)      │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

**Source:** [d'Alembert operator in curved spacetime — Wikipedia](https://en.wikipedia.org/wiki/D%27Alembert_operator)

**Key observation:** This is the **same** field equation as in the scalar PDTP
(Part 1, equation 3.5), but with the flat-space □ replaced by the curved-space
□_g. In the weak-field limit (g_μν → η_μν), equation (5.9) reduces exactly to
the Part 1 equation.

### 5.4 Variation with Respect to ψⱼ: Covariant Matter Field Equation

Similarly, varying with respect to ψⱼ:

```
┌──────────────────────────────────────────────────────────┐
│                                                          │
│  □_g ψⱼ = −gⱼ sin(ψⱼ − φ)                              │
│                                              ... (5.10)  │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

Again, this is the covariantized version of Part 1, equation (3.7).

### 5.5 Summary of Field Equations

The extended PDTP has four sets of field equations:

| Equation | Variable | Result | Reduces to (flat limit) |
|----------|----------|--------|------------------------|
| (5.2) | ω^{ab}_μ | T^a_{μν} = 0 (no torsion) | — |
| (5.5) | e^a_μ | G_μν = (8πG/c⁴) T_μν | — (new) |
| (5.9) | φ | □_g φ = Σ gᵢ sin(ψᵢ − φ) | □φ = Σ gᵢ sin(ψᵢ − φ) |
| (5.10) | ψⱼ | □_g ψⱼ = −gⱼ sin(ψⱼ − φ) | □ψⱼ = −gⱼ sin(ψⱼ − φ) |

**PDTP Original.** The Einstein equation (5.5) is **new** — it does not appear
in the scalar PDTP. It governs the tensor gravitational degrees of freedom
(gravitational waves with + and × polarizations). The phase equations (5.9)
and (5.10) are covariantized versions of the existing scalar equations.

### 5.6 The Two Gravitational Sectors

The extended PDTP has a distinctive two-sector gravitational structure:

1. **Tensor sector** (tetrad/metric): Governed by the Einstein equation (5.5).
   Describes how mass-energy curves spacetime. Produces tensor GW modes.

2. **Scalar sector** (phase φ): Governed by the phase equation (5.9).
   Describes the phase-locking between matter and spacetime. Produces the
   breathing GW mode.

These sectors are **coupled**: the phase field φ contributes to the stress-energy
T_μν that sources the Einstein equation, and the metric g_μν from the Einstein
equation appears in the covariant d'Alembertian □_g of the phase equation.

**PDTP Original.** This two-sector structure is the defining feature of the
extended PDTP. It means PDTP is not simply "GR plus a scalar field" — the
scalar field has a specific physical origin (condensate phase) and a specific
coupling to matter (cosine phase-locking) that is absent in generic scalar-tensor
theories.

---

## 6. Linearized Perturbation Analysis

### 6.1 Background Solution

We linearize around the flat, phase-aligned background:

```
e^a_μ = δ^a_μ        (flat Minkowski tetrad)
φ = φ₀ = const       (uniform spacetime phase)
ψᵢ = φ₀              (all matter phases aligned)                    ... (6.1)
```

This satisfies all field equations:
- Torsion: trivially zero for constant tetrad
- Einstein: G_μν = 0 and T_μν = 0 (no gradients, coupling contribution is pure
  cosmological constant which we absorb into the background)
- Phase equations: sin(φ₀ − φ₀) = 0

### 6.2 Perturbation Ansatz

We perturb:

```
e^a_μ = δ^a_μ + ε^a_μ(x)     |ε| ≪ 1
φ = φ₀ + δφ(x)               |δφ| ≪ 1
ψᵢ = φ₀ + δψᵢ(x)            |δψᵢ| ≪ 1                            ... (6.2)
```

The metric perturbation is:

```
g_μν = η_μν + h_μν

where h_μν = η_{ab}(δ^a_μ ε^b_ν + ε^a_μ δ^b_ν) = ε_μν + ε_νμ    ... (6.3)
```

(Here we lower the tangent-space index using η_{ab}, so ε_μν ≡ η_{ab} ε^b_μ.)

### 6.3 Decomposition of the Tetrad Perturbation

The perturbation ε_{μν} can be decomposed into symmetric and antisymmetric parts:

```
ε_{μν} = ε_{(μν)} + ε_{[μν]}                                       ... (6.4)
```

**Antisymmetric part ε_{[μν]}:** This is a local Lorentz transformation — it
rotates the tetrad without changing the metric (since h_μν = ε_{μν} + ε_{νμ}
is automatically symmetric). It has 6 components, corresponding to the 6
parameters of the Lorentz group. These are **pure gauge**.

**Source:** [Tetrad formalism — Wikipedia](https://en.wikipedia.org/wiki/Tetrad_formalism)

**Symmetric part ε_{(μν)}:** This equals ½ h_{μν} and contains the physical
metric perturbation. It has 10 independent components.

### 6.4 Decomposition of the Metric Perturbation

The symmetric metric perturbation h_{μν} (10 components) further decomposes
under the spatial rotation group SO(3). For a wave propagating in the z-direction:

**Source:** [Gravitational wave — Wikipedia](https://en.wikipedia.org/wiki/Gravitational_wave),
section "Polarizations."

**Tensor modes (2 components):** The transverse-traceless (TT) part:

```
h^{TT}_{ij} with h^{TT}_{0μ} = 0, h^{TT}_{ii} = 0, ∂_i h^{TT}_{ij} = 0
                                                                     ... (6.5)
```

For propagation along z, the two independent modes are:

```
h₊: h_{xx} = −h_{yy} = A₊ cos(kz − ωt)
h×: h_{xy} = h_{yx} = A× cos(kz − ωt)                              ... (6.6)
```

**Vector modes (4 components):** h_{0i} and the transverse vector part of h_{ij}.
These are constrained by the linearized equations (not freely propagating).

**Scalar modes (4 components):** h_{00}, the trace h_{ii}, and longitudinal parts.
The trace couples to the scalar field δφ.

### 6.5 Linearized Tensor Equation

Substituting the perturbation ansatz into the Einstein equation (5.5) and
keeping only first-order terms, the TT part satisfies:

```
┌──────────────────────────────────────────────────────────┐
│                                                          │
│  □ h^{TT}_{ij} = 0                          ... (6.7)   │
│                                                          │
│  i.e., (−∂²/∂t² + ∇²) h^{TT}_{ij} = 0                 │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

**Source:** The linearized Einstein equation for TT perturbations is standard.
See [Linearized gravity — Wikipedia](https://en.wikipedia.org/wiki/Linearized_gravity).

**Result:** Tensor gravitational waves propagate at the speed of light c, with
two independent polarizations (h₊ and h×). This matches GR exactly.

**PDTP Original.** The tensor modes in extended PDTP obey the same equation as
in GR. This is expected: the Palatini action (4.2) IS the Einstein-Hilbert
action in tetrad form, so linearized perturbations must give standard GR
gravitational waves.

### 6.6 Linearized Scalar Equation

The scalar perturbation δφ, linearized from equation (5.9) around the
background (6.1):

```
□ δφ = Σᵢ gᵢ cos(0) · (δψᵢ − δφ)

□ δφ = Σᵢ gᵢ (δψᵢ − δφ)                                           ... (6.8)
```

For the coupled matter perturbations, from (5.10):

```
□ δψⱼ = −gⱼ (δψⱼ − δφ)                                            ... (6.9)
```

These are exactly the linearized equations from Part 1, §6.2. In particular,
the relative phase perturbation θⱼ ≡ δψⱼ − δφ satisfies:

```
□ θⱼ + 2gⱼ θⱼ = 0                                                  ... (6.10)
```

This is the Klein-Gordon equation with mass-squared m²_eff = 2gⱼ > 0, giving
a **massive** breathing mode with dispersion relation ω² = k² + 2gⱼ.

**Source:** This matches Part 1, §6.3, equation (6.8). The mass gap ensures
stability and Yukawa suppression at long distances.

### 6.7 Mode Summary

```
┌──────────────────────────────────────────────────────────────────────┐
│  Extended PDTP: Linearized GW Modes                                  │
│                                                                      │
│  Mode        │ Equation       │ Speed   │ Mass    │ Origin           │
│  ────────────┼────────────────┼─────────┼─────────┼──────────────    │
│  h₊ (tensor) │ □h = 0        │ c       │ 0       │ tetrad e^a_μ     │
│  h× (tensor) │ □h = 0        │ c       │ 0       │ tetrad e^a_μ     │
│  breathing   │ □θ + 2gθ = 0  │ < c     │ √(2g)  │ phase φ          │
│                                                                      │
│  E(2) classification: N₃ (2 tensor + 1 scalar transverse)           │
│                                                                      │
│  Tensor modes: identical to GR                                       │
│  Breathing mode: massive, Yukawa-suppressed at distances > ℏ/(c√2g) │
│  Breathing/tensor ratio: < 10⁻⁵ (from Cassini bound, Part 3 §1.9)  │
└──────────────────────────────────────────────────────────────────────┘
```

**PDTP Original.** The extended PDTP predicts E(2) class N₃ gravitational
waves: 2 tensor modes identical to GR plus 1 massive breathing mode that is
Yukawa-suppressed at solar-system scales and below current detection thresholds.

---

## 7. Recovery of Existing PDTP Results

### 7.1 Weak-Field Static Limit → Newtonian Gravity

In the weak-field static limit:
- e^a_μ ≈ δ^a_μ + small perturbation → g_μν ≈ η_μν + h_μν
- Time derivatives negligible → □_g → ∇²
- Phase equation (5.9) reduces to: ∇²φ = Σ gᵢ sin(ψᵢ − φ)

This is identical to the scalar PDTP result (Part 1, §7). The Newtonian
potential recovery, Poisson equation, and Newton's constant identification
all follow unchanged.

**Source:** [mathematical_formalization.md](mathematical_formalization.md), §7.

### 7.2 PPN Parameters

The PPN parameters γ = 1 and β = 1 were derived in Part 3 (hard_problems.md §2)
using the acoustic metric / Painlevé-Gullstrand argument. This argument depends
on:

1. The speed of sound in the condensate equals c (Lorentz invariance)
2. The condensate density perturbation δρ/ρ₀ = 2U in isotropic coordinates

Both properties are preserved in the extended PDTP:

1. The Palatini action is Lorentz-invariant by construction, so c_s = c
2. The condensate density ρ₀ appears in the order parameter (3.2); its
   perturbation due to the Newtonian potential follows the same Euler
   equation as before

Therefore γ = 1 and β = 1 remain valid.

**Source:** [hard_problems.md](hard_problems.md), §2.

### 7.3 Phase Coupling Mechanism

The cos(ψᵢ − φ) coupling in (4.7) is identical in form to the scalar PDTP.
All results that depend on this coupling — the Kuramoto connection (Part 1 §4),
stability analysis (Part 1 §6), energy cost of phase control (Part 1 §8),
coherence-dependent gravity predictions (Part 1 §9) — are unchanged.

### 7.4 Conservation Laws

The extended Lagrangian (4.8) is invariant under:
- **Time translations** → energy conservation (Hamiltonian)
- **Space translations** → momentum conservation
- **Global phase shift** φ → φ + α, ψᵢ → ψᵢ + α → phase charge conservation

These are the same symmetries as in the scalar PDTP (Part 1, §5), now
supplemented by the diffeomorphism invariance of the tetrad sector.

**Source:** [Noether's theorem — Wikipedia](https://en.wikipedia.org/wiki/Noether%27s_theorem)

### 7.5 Momentum Balance

The momentum balance results of Part 11 (momentum_balance.md) extend naturally:
the total stress-energy tensor T_μν is covariantly conserved:

```
∇_μ T^μν = 0                                                        ... (7.1)
```

This is the covariant version of the flat-space conservation ∂_μ T^μν = 0
used in Part 11. The local momentum transfer between φ and ψ fields is
unchanged; the tetrad sector provides the global framework (curved spacetime)
in which this transfer occurs.

### 7.6 Consistency Verification

```
┌──────────────────────────────────────────────────────────────────────┐
│  Consistency with Parts 1–11                                         │
│                                                                      │
│  Result                     │ Scalar PDTP │ Extended PDTP │ Status   │
│  ──────────────────────────-┼─────────────┼───────────────┼────────  │
│  Newtonian gravity (1/r)    │ ✓           │ ✓             │ Same     │
│  Poisson equation           │ ✓           │ ✓             │ Same     │
│  PPN γ = 1, β = 1          │ ✓           │ ✓             │ Same     │
│  Kuramoto connection        │ ✓           │ ✓             │ Same     │
│  Stability (ω² > 0)        │ ✓           │ ✓             │ Same     │
│  Energy conservation        │ ✓           │ ✓             │ Extended │
│  Momentum conservation      │ ✓           │ ✓             │ Extended │
│  Phase charge conservation  │ ✓           │ ✓             │ Same     │
│  Breathing mode             │ ✓           │ ✓             │ Same     │
│  Tensor modes (h₊, h×)     │ ✗           │ ✓             │ NEW      │
│  Strong-field EP            │ ✓           │ ✓             │ Same     │
│  Momentum balance           │ ✓           │ ✓             │ Covariant│
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

---

## 8. Symmetry Breaking Analysis

### 8.1 The Question

The extended order parameter (3.2) contains a tetrad e^a_μ. For this to be
physically meaningful, the vacuum condensate must spontaneously choose a
particular tetrad — breaking some larger symmetry group G down to the
Lorentz subgroup SO(3,1).

Why? Because the vacuum should be maximally symmetric, but the condensate
"freezes" into a configuration with a specific frame. The broken symmetries
produce Goldstone bosons — and these are the gravitational degrees of freedom.

### 8.2 The He-3A Pattern (Review)

In He-3A (§2.2):

```
G = SO(3)_spin × SO(3)_orbit × U(1)_phase
H = SO(2)_combined
Broken generators: 6
Goldstone modes: spin-2 (emergent gravitons) + others                ... (8.1)
```

The emergent gravitons are the gapless Goldstone modes associated with
spontaneous breaking of rotational symmetry by the orbital triad.

**Source:** Volovik (2003), Chapter 9.

### 8.3 The PDTP Pattern

**PDTP Original.** For the relativistic (3+1)-dimensional case, the symmetry
breaking pattern is:

```
G = GL(4,ℝ) (general linear group — arbitrary frame choices)
H = SO(3,1) (Lorentz group — preserved by the condensate)
                                                                     ... (8.2)
```

**Source:** The GL(4,ℝ) → SO(3,1) breaking pattern for emergent gravity from
a condensate is discussed in Volovik (2003), Chapter 9.4, and in:
Wetterich, C. (2005), "Gravity from spinors," *Phys. Rev. D*, 70, 105004.

The broken generators:

```
dim(GL(4,ℝ)) − dim(SO(3,1)) = 16 − 6 = 10                         ... (8.3)
```

These 10 broken generators produce 10 Goldstone-like modes. However:

1. **4 are absorbed** by diffeomorphism gauge invariance (analogous to the
   Higgs mechanism, where Goldstone bosons are "eaten" by gauge fields).
   These become the constraint variables of GR.

2. **6 remain** as physical degrees of freedom.

Of these 6 physical modes:
- 4 are constrained by the equations of motion (GR constraint equations)
- **2 are freely propagating** → the tensor GW modes (h₊, h×)

**Source:** The counting of graviton polarizations as Goldstone bosons of broken
GL(4,ℝ) symmetry is discussed in:
Bjorken, J. D. (2001), "Emergent gauge bosons," hep-th/0111196.

### 8.4 Adding the Phase Sector

The PDTP condensate also has a U(1) phase. The full symmetry breaking is:

```
G_full = GL(4,ℝ) × U(1)_phase
H_full = SO(3,1)
                                                                     ... (8.4)
Broken generators: 16 + 1 − 6 = 11
```

The additional U(1) breaking produces one more Goldstone mode: the breathing
mode (scalar GW). But this mode acquires a mass from the coupling potential
gᵢ cos(ψᵢ − φ) — it is a **pseudo-Goldstone boson**, gapped by the explicit
breaking of the phase shift symmetry that occurs when matter couples in.

```
m²_breathing = 2g (from Part 1, §6.3)                               ... (8.5)
```

This is why the breathing mode is massive (Yukawa-suppressed) while the tensor
modes are massless — the tensor modes are true Goldstone bosons of a gauged
symmetry, while the breathing mode is a pseudo-Goldstone with a mass gap from
the coupling.

**PDTP Original.** The mass hierarchy m_tensor = 0 < m_breathing = √(2g) has
a natural explanation in the symmetry breaking pattern: tensor modes are exact
Goldstones, the breathing mode is a pseudo-Goldstone.

### 8.5 Connection to Group Field Theory

In the GFT approach to quantum gravity (Oriti 2014, Gielen & Sindoni 2016),
the fundamental "atoms of spacetime" are quantum tetrahedra. A GFT condensate
is a coherent state of many such tetrahedra.

**Source:** Oriti, D. (2014), "Group field theory as the microscopic description
of the quantum spacetime fluid," *Proceedings of Science*, PoS(QG-Ph)030.
arXiv:0710.3276.

**Source:** Gielen, S. & Sindoni, L. (2016), "Quantum cosmology from group field
theory condensates: a review," *SIGMA*, 12, 082. arXiv:1602.08104.

Key points:

1. Each quantum tetrahedron carries geometric data: 4 face areas, 4 face
   normals, and a total volume. This data naturally encodes a local frame
   (tetrad).

2. A coherent superposition of many tetrahedra → a macroscopic state with
   a smooth average tetrad field e^a_μ(x).

3. The condensate phase of the GFT field IS the phase φ — the same degree
   of freedom as in PDTP.

**PDTP Original.** GFT provides a candidate microscopic origin for the PDTP
order parameter (3.2): the tetrad e^a_μ arises from the average geometry of
quantum tetrahedra in the GFT condensate, and the phase φ is the condensate
phase of the GFT field.

```
GFT condensate ─── average ──→ smooth tetrad e^a_μ + phase φ
                               = PDTP extended order parameter (3.2)
```

This is not a derivation (GFT itself is not a complete theory), but it
shows that the PDTP order parameter has a plausible microscopic origin.

---

## 9. New Predictions from the Extension

### 9.1 Frame-Dragging (Gravitomagnetism)

In GR, a rotating mass drags spacetime around it — the **Lense-Thirring effect**.
This is encoded in the off-diagonal metric components g_{0i}, which represent
a "gravitomagnetic" field.

**Source:** [Lense-Thirring precession — Wikipedia](https://en.wikipedia.org/wiki/Lense%E2%80%93Thirring_precession)

In the scalar PDTP, the phase field φ has no vector structure — it cannot
produce the g_{0i} components needed for frame-dragging. This was a known
limitation.

**PDTP Original.** In the extended PDTP, the tetrad e^a_μ has off-diagonal
components that naturally produce g_{0i} ≠ 0. A rotating mass distribution
creates a non-trivial stress-energy T_{0i}, which sources the Einstein
equation (5.5) and produces the correct Lense-Thirring metric.

The frame-dragging rate for a sphere of mass M and angular momentum J:

```
Ω_LT = 2GJ / (c²r³)                                                ... (9.1)
```

This is the standard GR result, and it follows from the extended PDTP because
the tetrad sector obeys the Einstein equation.

**Source:** [Frame-dragging — Wikipedia](https://en.wikipedia.org/wiki/Frame-dragging)

**Experimental verification:** Gravity Probe B measured frame-dragging by Earth
to ~19% precision, consistent with GR. The extended PDTP predicts the same value.

### 9.2 Kerr Metric Recovery

A rotating black hole in GR is described by the **Kerr metric**.

**Source:** [Kerr metric — Wikipedia](https://en.wikipedia.org/wiki/Kerr_metric)

In the extended PDTP, a stationary rotating condensate flow produces an
acoustic metric that matches the Kerr geometry. This was shown for acoustic
analogues by Visser (1998):

**Source:** Visser, M. (1998), "Acoustic black holes: horizons, ergospheres
and Hawking radiation," *Class. Quantum Grav.*, 15, 1767.

The key elements:
- The condensate has a background flow velocity v_i (from the rotating source)
- The tetrad encodes both the density perturbation and the flow
- The resulting acoustic metric has an ergosphere (where the flow exceeds c)
  and a horizon (where the radial flow exceeds c)

**PDTP Original.** The extended PDTP recovers the Kerr metric for rotating
sources through the standard Einstein equation (5.5). The phase sector φ
provides the scalar (Newtonian) part, while the tetrad sector provides the
rotational (gravitomagnetic) part. Both are needed for the full Kerr solution.

### 9.3 Torsion at Extreme Densities

The torsion equation (5.2) gives T^a_{μν} = 0 for scalar matter. But if the
condensate has **fermionic** constituents (as suggested by the He-3A analogy,
where Cooper pairs are spin-½ atoms), then at sufficiently high densities,
spin-torsion coupling could become relevant.

**Source:** [Einstein-Cartan theory — Wikipedia](https://en.wikipedia.org/wiki/Einstein%E2%80%93Cartan_theory),
section "Spin and torsion."

In Einstein-Cartan theory, the torsion tensor is sourced by the spin density:

```
T^a_{μν} ∝ S^a_{μν}    (spin density tensor)                        ... (9.2)
```

**Source:** Hehl, F. W., von der Heyde, P., Kerlick, G. D., Nester, J. M.
(1976), "General relativity with spin and torsion: Foundations and prospects,"
*Rev. Mod. Phys.*, 48, 393.

Torsion effects are suppressed by a factor of (ρ/ρ_Planck), so they are only
relevant at Planck-scale densities or (more speculatively) at nuclear densities
inside neutron stars.

**PDTP Original.** If the vacuum condensate has fermionic substructure (as in
the He-3A analogy), the extended PDTP naturally accommodates torsion at extreme
densities. This would be a departure from standard GR and a potential
observational signature in neutron star interiors. However, the torsion
contribution is model-dependent (it requires knowing the spin structure of the
condensate constituents).

### 9.4 Predictions Summary

| Prediction | Scalar PDTP | Extended PDTP | Status |
|------------|------------|---------------|--------|
| Newtonian gravity | ✓ | ✓ | Confirmed |
| Tensor GW modes | ✗ | ✓ | Confirmed (LIGO) |
| Frame-dragging | ✗ | ✓ | Confirmed (GP-B) |
| Kerr black holes | ✗ | ✓ | Consistent |
| Breathing mode | ✓ (detectable) | ✓ (Yukawa-suppressed) | Not yet detected |
| Torsion (NS interior) | ✗ | Possible | Not yet testable |

---

## 10. Honest Assessment

### 10.1 What This Extension Achieves

```
┌──────────────────────────────────────────────────────────────────────┐
│  ACHIEVED                                                            │
│                                                                      │
│  1. Full extended Lagrangian written (equation 4.8)                  │
│  2. All four field equations derived (§5)                            │
│  3. Tensor GW modes shown to emerge (§6, equation 6.7)              │
│  4. DOF counting correct: 2 tensor + 1 breathing (§3.3)             │
│  5. All Parts 1–11 results preserved in weak-field limit (§7)       │
│  6. Symmetry breaking pattern identified: GL(4,R) × U(1) → SO(3,1) │
│  7. Mass hierarchy explained: tensor massless, breathing massive     │
│  8. Frame-dragging and Kerr metric recovered (§9)                   │
│  9. GFT condensate identified as candidate microscopic origin (§8.5)│
│                                                                      │
│  Status upgrade: "structural gap identified" → "formal extension     │
│  constructed with derived consequences"                              │
└──────────────────────────────────────────────────────────────────────┘
```

### 10.2 What This Extension Does NOT Achieve

```
┌──────────────────────────────────────────────────────────────────────┐
│  NOT ACHIEVED (genuinely open)                                       │
│                                                                      │
│  1. Microscopic origin of tetrad structure                           │
│     - WHY the condensate has tetrad DOF is not derived               │
│     - GFT provides a candidate, but GFT itself is not complete       │
│     - This requires condensate microphysics (deepest open problem)   │
│                                                                      │
│  2. Why GL(4,R) → SO(3,1)                                           │
│     - The symmetry breaking pattern is stated, not derived           │
│     - Need: potential V(e) with minimum at Lorentz-invariant config  │
│     - He-3A provides precedent but not proof                         │
│                                                                      │
│  3. Numerical value of the symmetry breaking scale                   │
│     - When does the tetrad "freeze"? At what energy/temperature?     │
│     - Connected to the vacuum condensation temperature (unknown)     │
│                                                                      │
│  4. Uniqueness of the Palatini choice                                │
│     - Why Palatini and not metric formalism? (Both are equivalent    │
│       for scalar matter, so this is aesthetic not physical)           │
│     - Higher-derivative terms? (Suppressed at low energies)          │
│                                                                      │
│  5. Double pulsar tension                                            │
│     - The ~1% GW emission deficit (from strong_field_ep.md §7)      │
│       is not resolved by adding tetrads                              │
│     - Still requires numerical NS interior solution                  │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

### 10.3 Relationship to the Scalar PDTP

The extended PDTP (this document) is **not a replacement** for the scalar PDTP
(Parts 1–11). Rather:

- The scalar PDTP captures the **dominant physics** in the weak-field regime
  (Newtonian gravity, phase-locking, stability, conservation laws).
- The extended PDTP adds the **tensor sector** needed for gravitational wave
  polarization, frame-dragging, and rotating black holes.
- All scalar PDTP results are limiting cases of the extended theory.

The relationship is analogous to the relationship between Newtonian gravity
and General Relativity: the simpler theory is sufficient for most purposes,
but the fuller theory is needed for specific phenomena (here: GW polarization
and rotation effects).

---

## 11. Summary of Results

**Central result:** The PDTP condensate order parameter can be extended from
scalar (phase only) to tensor (phase + tetrad) by writing:

```
Φ = √ρ₀ · exp(iφ) · e^a_μ
```

The extended Lagrangian (4.8) combines:
- Palatini action for tetrad dynamics (→ Einstein equation)
- Covariantized phase kinetic term
- Covariantized matter kinetic terms
- Phase-locking coupling cos(ψᵢ − φ)

**Key results:**

1. **Tensor GW modes emerge:** □h^{TT}_{ij} = 0 — two tensor polarizations
   propagating at speed c, identical to GR (equation 6.7).

2. **Breathing mode preserved:** massive, with m² = 2g, Yukawa-suppressed
   at long distances (equation 6.10).

3. **E(2) class N₃:** 2 tensor + 1 breathing mode — consistent with all
   current observations.

4. **All previous results preserved:** Newtonian gravity, PPN parameters,
   Kuramoto connection, stability, conservation laws, momentum balance
   all carry over unchanged (§7).

5. **New predictions unlocked:** frame-dragging, Kerr metric, torsion at
   extreme densities (§9).

6. **Symmetry breaking understood:** GL(4,R) × U(1) → SO(3,1), with tensor
   modes as exact Goldstones and breathing mode as pseudo-Goldstone (§8).

7. **GFT connection:** quantum tetrahedra condensate provides a candidate
   microscopic origin for the order parameter (§8.5).

**Remaining open:** Microscopic origin of tetrad structure, symmetry breaking
potential, double pulsar tension.

---

## 12. References

### Established Physics Sources

1. [Klein-Gordon equation — Wikipedia](https://en.wikipedia.org/wiki/Klein%E2%80%93Gordon_equation)
2. Eardley, D. M., Lee, D. L., Lightman, A. P. (1973), "Gravitational-Wave
   Observations as a Tool for Testing Relativistic Gravity," *Phys. Rev. Lett.*,
   30, 884.
3. LIGO Scientific Collaboration and Virgo Collaboration (2017), "GW170814,"
   *Phys. Rev. Lett.*, 119, 141101.
4. Volovik, G. E. (2003), *The Universe in a Helium Droplet*, Oxford University
   Press. Chapters 5, 7, 9.
5. [Superfluid helium-3 — Wikipedia](https://en.wikipedia.org/wiki/Superfluid_helium-3)
6. Barceló, C., Liberati, S., Visser, M. (2005), "Analogue Gravity," *Living
   Reviews in Relativity*, 8, 12.
7. [Tetrad formalism — Wikipedia](https://en.wikipedia.org/wiki/Tetrad_formalism)
8. [Lorentz group — Wikipedia](https://en.wikipedia.org/wiki/Lorentz_group)
9. [Diffeomorphism — Wikipedia](https://en.wikipedia.org/wiki/Diffeomorphism)
10. Wald, R. M. (1984), *General Relativity*, University of Chicago Press.
11. [Palatini variation — Wikipedia](https://en.wikipedia.org/wiki/Palatini_variation)
12. [Einstein-Cartan theory — Wikipedia](https://en.wikipedia.org/wiki/Einstein%E2%80%93Cartan_theory)
13. [Spin connection — Wikipedia](https://en.wikipedia.org/wiki/Spin_connection)
14. [Torsion tensor — Wikipedia](https://en.wikipedia.org/wiki/Torsion_tensor)
15. Carroll, S. (2004), *Spacetime and Geometry*, Addison-Wesley.
16. [Einstein field equations — Wikipedia](https://en.wikipedia.org/wiki/Einstein_field_equations)
17. [Stress-energy tensor — Wikipedia](https://en.wikipedia.org/wiki/Stress%E2%80%93energy_tensor)
18. [d'Alembert operator — Wikipedia](https://en.wikipedia.org/wiki/D%27Alembert_operator)
19. [Gravitational wave — Wikipedia](https://en.wikipedia.org/wiki/Gravitational_wave)
20. [Linearized gravity — Wikipedia](https://en.wikipedia.org/wiki/Linearized_gravity)
21. [Noether's theorem — Wikipedia](https://en.wikipedia.org/wiki/Noether%27s_theorem)
22. [Lense-Thirring precession — Wikipedia](https://en.wikipedia.org/wiki/Lense%E2%80%93Thirring_precession)
23. [Frame-dragging — Wikipedia](https://en.wikipedia.org/wiki/Frame-dragging)
24. [Kerr metric — Wikipedia](https://en.wikipedia.org/wiki/Kerr_metric)
25. Visser, M. (1998), "Acoustic black holes," *Class. Quantum Grav.*, 15, 1767.
26. Hehl, F. W., von der Heyde, P., Kerlick, G. D., Nester, J. M. (1976),
    *Rev. Mod. Phys.*, 48, 393.
27. Oriti, D. (2014), "Group field theory as the microscopic description of the
    quantum spacetime fluid," *Proceedings of Science*, PoS(QG-Ph)030. arXiv:0710.3276.
28. Gielen, S. & Sindoni, L. (2016), "Quantum cosmology from group field theory
    condensates: a review," *SIGMA*, 12, 082. arXiv:1602.08104.
29. Wetterich, C. (2005), "Gravity from spinors," *Phys. Rev. D*, 70, 105004.
30. Bjorken, J. D. (2001), "Emergent gauge bosons," hep-th/0111196.

### PDTP Original Results

1. Extended order parameter Φ = √ρ₀ e^{iφ} e^a_μ (equation 3.2)
2. Extended Lagrangian combining Palatini + phase coupling (equation 4.8)
3. Coupling stress-energy T^(coupling)_μν (equation 5.8)
4. Two-sector gravitational structure: tensor + scalar (§5.6)
5. E(2) class N₃ GW polarization from PDTP (§6.7)
6. Mass hierarchy: m_tensor = 0, m_breathing = √(2g) (§8.4)
7. Symmetry breaking GL(4,R) × U(1) → SO(3,1) (§8.3–8.4)
8. Pseudo-Goldstone interpretation of breathing mode (§8.4)
9. GFT condensate → PDTP order parameter mapping (§8.5)
10. Frame-dragging recovery in extended PDTP (§9.1)
11. Kerr metric recovery from extended PDTP (§9.2)
12. Torsion prediction at extreme densities (§9.3)

---

*End of Part 12: Condensate Tetrad Extension*
