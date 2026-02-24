# Vacuum Energy and the Tensor Sector: Background Subtraction

Analysis of whether the PDTP tensor sector can be extended to exclude vacuum
energy from gravitating — the condensate background subtraction mechanism.

**Prerequisite reading:**
- [cosmological_constant_analysis.md](cosmological_constant_analysis.md) (Part 17) — full cosmological constant analysis
- [tetrad_extension.md](tetrad_extension.md) (Part 12) — Palatini action and tensor sector derivation

Every established result is cited. Every new result is marked as PDTP Original.

---

## Table of Contents

1. [The PDTP Trilemma](#1-the-pdtp-trilemma)
2. [Three Options for Resolution](#2-three-options-for-resolution)
3. [Option 3: Condensate Background Subtraction](#3-option-3-condensate-background-subtraction)
4. [Analysis of the Palatini Variation](#4-analysis-of-the-palatini-variation)
5. [Implementation at the Action Level](#5-implementation-at-the-action-level)
6. [Comparison with Known Approaches](#6-comparison-with-known-approaches)
7. [Constraints and Risks](#7-constraints-and-risks)
8. [Assessment: What Is Resolved vs Open](#8-assessment-what-is-resolved-vs-open)
9. [Summary](#9-summary)
10. [References](#10-references)

---

## 1. The PDTP Trilemma

### 1.1 What PDTP Wants

The extended PDTP framework (Parts 1–12) simultaneously requires three things:

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  (a) EXACT GR RECOVERY                                       │
│      G_μν = 8πG T_μν from the Palatini variation            │
│      Required: pass all solar system and binary pulsar tests │
│                                                              │
│  (b) SCALAR SECTOR VACUUM FILTERING                          │
│      □φ = Σ gᵢ sin(ψᵢ − φ)                                  │
│      Random-phase vacuum fluctuations average to zero        │
│      Phase-mismatch coupling is insensitive to vacuum energy │
│                                                              │
│  (c) TENSOR SECTOR Λ SOLUTION                                │
│      Vacuum energy should not gravitate at 10⁹⁶ kg/m³       │
│      The tensor sector should not "see" ρ_vacuum             │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### 1.2 The Trilemma

The problem: **all three cannot be simultaneously satisfied** with the
current PDTP formulation.

**Why (a) and (b) are compatible:**
The scalar sector (b) and the tensor sector (a) are largely decoupled.
The Palatini variation gives G_μν = 8πG T_μν independently of the
phase-locking dynamics. Both can hold at the same time.

**Why (a) and (c) conflict:**
If the tensor sector exactly recovers GR — G_μν = 8πG T_μν with the
full stress-energy tensor — then vacuum energy gravitates with its full
QFT-predicted value (ρ ~ 10⁹⁶ kg/m³). Exact GR recovery means the
cosmological constant problem is inherited exactly.

**Why (b) and (c) together require relaxing (a):**
The scalar sector solves its own vacuum energy problem structurally
(phase averaging). To extend this solution to the tensor sector, T_μν
must be modified — which means G_μν ≠ 8πG T_μν^(full). This modifies
GR and threatens solar system tests.

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  The PDTP Trilemma:                                          │
│                                                              │
│  (a) + (b)  =  OK (current status of Parts 1–17)            │
│  (a) + (c)  =  IMPOSSIBLE (GR + Λ solution don't coexist)   │
│  (b) + (c)  =  POSSIBLE (but requires relaxing (a))          │
│                                                              │
│  Must choose: exact GR, OR cosmological constant solution.   │
│  Cannot have both.                                           │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**PDTP Original.** The PDTP trilemma: simultaneous exact GR recovery,
scalar vacuum filtering, and tensor sector Λ resolution are mutually
inconsistent under the current formulation. One must be relaxed.

**Source:** [cosmological_constant_analysis.md](cosmological_constant_analysis.md) §5.1–5.2 (problem diagnosed)

---

## 2. Three Options for Resolution

### 2.1 Option 1: Accept the Limitation (Current Status)

Leave exact GR recovery (a) intact and accept that the tensor sector
inherits the cosmological constant problem:

```
Scalar sector:  vacuum energy averages out  ✓  (structural)
Tensor sector:  vacuum energy gravitates    ✗  (same as GR)
Overall:        partial reframing, not a solution
```

**Status:** This is the honest current state of PDTP (Parts 1–17).
The cosmological constant problem is "halved" — it disappears in the
scalar sector but persists in the tensor sector. Not a resolution.

**Advantage:** No modification to GR — all solar system tests pass trivially.

**Disadvantage:** The cosmological constant problem remains fully unsolved
in the sector that matters (G_μν = 8πG T_μν drives spacetime curvature).

### 2.2 Option 2: Normal Ordering

In quantum field theory, **normal ordering** moves all creation operators
to the left of all annihilation operators. The effect on vacuum energy:
the zero-point contribution of every quantum field mode is removed by
construction, since ⟨0|:H:|0⟩ = 0 for any normal-ordered Hamiltonian.

**Source:** [Normal order — Wikipedia](https://en.wikipedia.org/wiki/Normal_order)

Applied to PDTP: if the condensate Hamiltonian is normal-ordered before
computing T_μν, the vacuum energy contribution vanishes. The tensor sector
then couples only to particle excitations above the vacuum.

```
T_μν^(QFT) = ⟨T_μν⟩_particles + ⟨T_μν⟩_zero-point

Normal ordering removes zero-point:
T_μν^(normal) = ⟨T_μν⟩_particles only

→ G_μν = 8πG T_μν^(normal)  (vacuum energy does not gravitate)
```

**Problem:** Normal ordering in flat space removes vacuum energy by
definition, but this procedure is not Lorentz-covariant in curved
spacetime. Extending normal ordering to a dynamical condensate metric
requires specifying a preferred vacuum state — but in curved spacetime,
there is no unique vacuum.

**Source:** [Scalar–tensor theory — Wikipedia](https://en.wikipedia.org/wiki/Scalar%E2%80%93tensor_theory)

Normal ordering also does not address the condensate's OWN vacuum energy
(the zero-point of the condensate modes). It removes external quantum
field contributions but not the condensate ground state energy itself.

**Verdict:** Technically motivated but ambiguous in curved spacetime.
Requires a preferred condensate vacuum — which PDTP has (the condensate
ground state), making this slightly more tractable than in standard QFT,
but the formalization remains incomplete.

### 2.3 Option 3: Background Subtraction (Recommended)

Both external reviews of Part 17 converged on the same recommendation:
**condensate background subtraction**.

The physical idea:
- The PDTP condensate IS spacetime. Its ground state density ρ₀ defines
  the metric background — it is already "encoded" in the tetrad e^a_μ.
- When we write G_μν = 8πG T_μν, the metric g_μν on the left is BUILT
  FROM the condensate tetrad. The condensate ground state is already
  included in the geometry itself.
- Only DEVIATIONS from the ground state — δρ = ρ − ρ₀ — represent
  genuine perturbations that should gravitate as an additional source.

```
T_μν^(phys) = T_μν^(full) − ⟨T_μν⟩_condensate        ... (2.1)

Modified Einstein equation:
G_μν = 8πG T_μν^(phys) = 8πG (T_μν^(full) − ⟨T_μν⟩₀)   ... (2.2)
```

The condensate ground state contribution ⟨T_μν⟩₀ is already "paid for"
by the background metric — it is not an additional source of curvature.

**PDTP Original.** Background subtraction in the PDTP context: the
condensate ground state stress-energy ⟨T_μν⟩₀ is part of the background
metric (carried by the tetrad), not a gravitating source. Only
perturbations δT_μν = T_μν − ⟨T_μν⟩₀ appear on the right-hand side of
the Einstein equation.

---

## 3. Option 3: Condensate Background Subtraction

### 3.1 Physical Motivation

The condensate ground state is characterized by:

```
φ(x,t) = ω₀ t     (uniform oscillation)               ... (3.1)
ρ(x,t) = ρ₀       (uniform density)                   ... (3.2)
ψᵢ = φ             (all matter phases locked to φ)     ... (3.3)
```

In this state, the stress-energy tensor has a UNIFORM background value:

```
⟨T_μν⟩₀ = diag(ρ₀ c², ρ₀ c², ρ₀ c², ρ₀ c²) × (constant)
```

This uniform background is indistinguishable from a renormalization of
the cosmological constant. More importantly, it defines the geometry:
the flat Minkowski metric IS the geometry of the condensate ground state.

**Analogy — The Acoustic Metric:**

In a Bose-Einstein condensate or superfluid, sound waves (phonons)
propagate on an effective "acoustic metric" determined by the background
flow velocity and density:

```
ds²_acoustic = (ρ_s/m c_s) [−(c_s² − v²) dt² − 2v·dx dt + dx²]
```

The total fluid mass (the background density ρ_s) does not appear as
a gravitating source in the acoustic metric — it defines the metric.
Only PERTURBATIONS (density waves, vortices) propagate and interact as
"matter" on this background.

**Source:** [Acoustic metric — Wikipedia](https://en.wikipedia.org/wiki/Acoustic_metric)

**Source:** [Analog models of gravity — Wikipedia](https://en.wikipedia.org/wiki/Analog_models_of_gravity)

PDTP is the non-analogue version of this: not sound waves on a BEC, but
actual spacetime as a condensate where the background density defines
the metric, and only excitations contribute to T_μν.

### 3.2 Formal Statement

Define the physical stress-energy tensor as:

```
T_μν^(phys) ≡ T_μν^(full) − ⟨T_μν⟩₀                  ... (3.4)
```

where ⟨T_μν⟩₀ is the ground-state expectation value evaluated in the
Minkowski background (the condensate at ρ = ρ₀, φ = ω₀ t).

The modified gravitational field equation becomes:

```
G_μν = 8πG T_μν^(phys) = 8πG (T_μν^(full) − ⟨T_μν⟩₀)   ... (3.5)
```

For vacuum quantum fluctuations with random phases:

```
⟨T_μν⟩_vacuum-fluctuations ≈ ⟨T_μν⟩₀  (vacuum fluctuations ARE
                                          the background condensate
                                          activity)
```

Therefore: T_μν^(phys) for vacuum fluctuations ≈ 0.

Vacuum energy does not gravitate because it is part of the condensate
ground state — it is "the geometry," not "matter on the geometry."

### 3.3 The Vacuum Energy Reframing

The key step: PDTP identifies the QFT vacuum with the condensate ground
state.

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  Standard QFT:  |0⟩ = empty space, zero particles           │
│                  vacuum energy ρ_vac ~ ρ_Planck              │
│                  This energy GRAVITATES in GR                │
│                                                              │
│  PDTP:          |0⟩ = condensate ground state               │
│                  The condensate AT its ground state IS the   │
│                  flat metric — it already defines spacetime  │
│                  Adding ρ₀ to the Einstein equation would    │
│                  DOUBLE-COUNT the background geometry        │
│                                                              │
│  Background subtraction removes the double-counting.         │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**PDTP Original.** Adding the full vacuum energy to the Einstein equation
in PDTP constitutes double-counting: the condensate ground state defines
the background metric AND appears again as a gravitating source. Background
subtraction removes this double-counting by construction.

---

## 4. Analysis of the Palatini Variation

### 4.1 What the Current Palatini Variation Produces

From Part 12 (tetrad_extension.md §5), the Palatini variation of the
extended PDTP action:

```
S_PDTP = S_Palatini + S_phase + S_matter                    ... (4.1)

S_Palatini = (1/16πG) ∫ e e^μ_a e^ν_b R^{ab}_{μν}[ω] d⁴x  ... (4.2)
```

Varying with respect to the tetrad e^a_μ while treating ω^{ab}_μ as
independent (Palatini formalism) gives:

```
G_μν[g] = 8πG T_μν                                         ... (4.3)

where T_μν = T_μν^(phase) + T_μν^(matter)                  ... (4.4)
```

**Source:** [tetrad_extension.md](tetrad_extension.md) §5.5–5.6

This T_μν is the full stress-energy tensor — it contains ALL contributions
from the phase field and matter fields, including their vacuum fluctuations.

### 4.2 Does the Palatini Variation Naturally Produce Background Subtraction?

**Answer: No.**

The variation is mechanical: we vary S = S_Palatini + S_matter with
respect to e^a_μ. The result is:

```
Variation of S_Palatini: →  G_μν (left side)
Variation of S_matter:   →  T_μν^(full) (right side)

⇒ G_μν = 8πG T_μν^(full)                                   ... (4.5)
```

Nothing in the standard Palatini variation isolates ground-state
contributions. The variation is blind to the distinction between "what
defines the background" and "what propagates on it."

This is not a failure of the Palatini formalism — it is a feature. The
Palatini formalism faithfully implements the principle that all energy
gravitates. Obtaining background subtraction requires **explicitly
building it into the action**.

**Source:** [Palatini variation — Wikipedia](https://en.wikipedia.org/wiki/Palatini_variation)

### 4.3 What Would Need to Change in the Action

To implement T_μν^(phys) = T_μν − ⟨T_μν⟩₀ in the Palatini framework,
one option is to subtract the ground-state action from S_matter:

```
S_matter^(phys) ≡ S_matter − S_matter^(ground-state)       ... (4.6)
```

Then the variation gives:

```
δS_matter^(phys) / δe^a_μ = T_μν − ⟨T_μν⟩₀  =  T_μν^(phys)
```

This is equivalent to normal-ordering the matter action around the
condensate background — keeping only perturbations.

**The challenge:** S_matter^(ground-state) depends on the condensate
background solution, which is dynamical. The subtraction couples the
matter sector to the condensate state in a field-theoretic way that
requires careful implementation to avoid new instabilities or
non-localities.

---

## 5. Implementation at the Action Level

### 5.1 Option A: Explicit Ground-State Subtraction

Modify the action by subtracting the condensate ground-state contribution:

```
S_PDTP^(modified) = S_Palatini + S_phase + S_matter
                    − ∫ e ⟨L_matter⟩₀ d⁴x               ... (5.1)
```

where ⟨L_matter⟩₀ is the matter Lagrangian density evaluated at the
condensate ground state.

**Variation result:**

```
G_μν = 8πG (T_μν − ⟨T_μν⟩₀)                              ... (5.2)
```

The subtraction term adds a constant (Minkowski space) contribution
to the right-hand side that cancels the ground-state energy. Dark energy
then corresponds only to deviations from this ground state.

**Key property:** If the condensate is exactly in its ground state,
the right-hand side vanishes (no cosmological constant). If the condensate
is slightly above its ground state (as PDTP proposes for dark energy),
the right-hand side gives a small positive ρ_Λ proportional to the
fractional excitation δρ/ρ₀.

### 5.2 Option B: Perturbative Reformulation

Instead of subtracting the ground state, reformulate the entire theory
as a perturbation expansion around the condensate ground state:

```
φ = ω₀ t + δφ
ρ = ρ₀ + δρ                                                ... (5.3)
ψᵢ = φ + δψᵢ

e^a_μ = η^a_μ + h^a_μ   (tetrad as Minkowski + perturbation)
```

Then S_PDTP is expanded to quadratic order in perturbations. The
zeroth-order (ground-state) terms do not contribute to the variation
because they are constants in the background. Only perturbative terms
contribute to T_μν.

**Result:** By construction, the perturbative T_μν contains only δφ,
δρ, δψᵢ, h^a_μ — not the background values. The ground-state energy
does not appear.

This is the most natural implementation from the condensate perspective:
it is exactly what is done in the acoustic metric derivation — the
effective metric for phonons is derived by expanding the BEC action
around the condensate background.

**Source:** [Acoustic metric — Wikipedia](https://en.wikipedia.org/wiki/Acoustic_metric)

### 5.3 Option C: Equation of Motion Modification

Rather than modifying the action, modify the Einstein equation directly
by subtracting the Minkowski-background T_μν:

```
G_μν = 8πG (T_μν − ⟨T_μν⟩_Minkowski)                    ... (5.4)
```

This is operationally equivalent to Options A and B but is done "by
hand" as a prescription rather than derived from an action.

**Disadvantage:** This prescription lacks an action principle. It is not
clear what symmetry or conservation law this corresponds to, and it may
be inconsistent with the contracted Bianchi identity ∇^μ G_μν = 0
unless the subtracted term also satisfies ∇^μ ⟨T_μν⟩₀ = 0 (which it
does if the background is exactly Minkowski).

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  Preferred implementation: Option B (perturbative)           │
│                                                              │
│  Reason: Closest to the condensate physics motivation.        │
│  The condensate ground state defines the background;         │
│  all dynamics are perturbations around it. This is the       │
│  standard BEC/superfluid approach extended to gravity.        │
│                                                              │
│  Status: Framework described; formal derivation not yet done │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**PDTP Original.** Option B — perturbative reformulation around the
condensate ground state — is the natural implementation of background
subtraction in PDTP. The action is expanded around the ground-state
solution (φ = ω₀ t, ρ = ρ₀, e^a_μ = η^a_μ) to quadratic order in
perturbations. By construction, only perturbative excitations contribute
to T_μν; the ground-state condensate energy is absorbed into the
background metric.

---

## 6. Comparison with Known Approaches

### 6.1 Unimodular Gravity

Unimodular gravity is a modification of GR in which the trace of the
Einstein equation is removed by imposing the constraint det(g_μν) = 1
(fixed volume element). The result is a trace-free Einstein equation:

```
G_μν − (1/4) g_μν G = 8πG (T_μν − (1/4) g_μν T)         ... (6.1)
```

**Source:** Weinberg, S. (1989), "The cosmological constant problem,"
*Rev. Mod. Phys.* 61, 1 (discusses unimodular gravity as approach)

The cosmological constant Λ appears as an **integration constant** in
unimodular gravity, not as a vacuum energy contribution. This shifts
the problem: instead of asking why ρ_vacuum is small, one asks why
the integration constant was small initially.

**Comparison with PDTP Option 3:**

| Feature | Unimodular gravity | PDTP background subtraction |
|---------|--------------------|-----------------------------|
| How vacuum energy is handled | Λ = integration constant | Absorbed into background metric |
| Physical motivation | Gauge constraint on metric | Condensate defines background |
| Requires new physics | Yes (fix det g) | Yes (perturbative action formulation) |
| GR in weak field | Recovered | Recovered at leading order |
| Solves coincidence problem | No | No |
| Derivable from action | Yes | Yes (Option B) |

PDTP's Option B and unimodular gravity share the same spirit: the
cosmological constant is not a gravitating energy density but a feature
of the background geometry. The mechanisms are different — unimodular
gravity uses a volume constraint, PDTP uses condensate ground-state
subtraction.

### 6.2 Vacuum Energy Sequestering (Kaloper-Padilla)

Vacuum energy sequestering is a mechanism proposed by Kaloper and Padilla
in which a global constraint (a Lagrange multiplier over all of spacetime)
cancels the contribution of local vacuum energy to the cosmological
constant:

```
S = ∫ d⁴x √−g [M²_Pl R/2 − λ − L_matter] + σ(∫ d⁴x √−g λ/μ⁴)
```

The global constraint forces the spatially averaged vacuum energy to
exactly cancel the cosmological constant from L_matter.

**Comparison with PDTP Option 3:**

PDTP's background subtraction is locally defined (it operates on T_μν
field by field) whereas sequestering is a global (spacetime-integrated)
constraint. The PDTP mechanism is more natural from a condensate physics
perspective — no non-local integration is needed — but the mechanism
for enforcing the subtraction is less explicit.

### 6.3 Acoustic Metric / Analogue Gravity

The acoustic metric is the most direct physical analogy for the PDTP
background subtraction mechanism.

In a BEC with condensate density ρ_s and flow velocity v:
- The acoustic metric g^{acoustic}_{μν} depends only on ρ_s and v (the
  background condensate state)
- Phonons propagate on this metric — they cannot "feel" the total mass
  of the condensate, only its local gradients and flow
- The total condensate energy ρ_s is encoded in the metric, not
  an additional gravitating source

**Source:** [Acoustic metric — Wikipedia](https://en.wikipedia.org/wiki/Acoustic_metric)

**Source:** [Analog models of gravity — Wikipedia](https://en.wikipedia.org/wiki/Analog_models_of_gravity)

PDTP aspires to the same relationship: just as phonons in a BEC do not
gravitate against the total condensate mass (they ARE the metric), matter
in PDTP should not gravitate against the condensate ground state (the
ground state IS spacetime). The connection is more than analogy — PDTP
is built on exactly this principle. The background subtraction mechanism
is its formal implementation.

### 6.4 Emergent Gravity (Jacobson, Verlinde)

Emergent gravity derives GR from thermodynamic first principles:
spacetime curvature encodes the entropy of quantum information (Jacobson)
or gravity is an entropic force (Verlinde). In these frameworks, the
Einstein equation arises as an equation of state for spacetime entropy.

The cosmological constant problem in emergent gravity: if GR is an
equation of state, vacuum energy may not need to gravitate in the
standard way — the "zero-energy" state is determined by thermodynamic
equilibrium, not energy content.

**Comparison with PDTP:** The condensate interpretation of PDTP is
structurally similar to emergent gravity — both treat spacetime as a
collective phenomenon. The background subtraction in PDTP can be seen
as the "thermodynamic reference state" (the condensate ground state)
being the correct zero energy for the equation of state.

---

## 7. Constraints and Risks

### 7.1 Solar System Tests

If the tensor sector is modified (Options A, B, or C), the modified
Einstein equation is:

```
G_μν = 8πG (T_μν − ⟨T_μν⟩₀)                              ... (7.1)
```

For normal matter (stars, planets), T_μν >> ⟨T_μν⟩₀ at local scales:

```
For a solar-mass object:  T_μν^(matter) ~ ρ_sun c² ~ 10³² kg/m³
Condensate background:    ⟨T_μν⟩₀ ~ ρ₀ ~ 10⁹⁶ kg/m³ (uniform!)
```

Wait — this seems problematic: ⟨T_μν⟩₀ is enormous and uniform.
However, the subtraction removes a CONSTANT uniform background.
A constant uniform T_μν contribution to the Einstein equation gives
only a cosmological constant — it does NOT affect local gravitational
dynamics (Gauss's law: uniform background does not produce local gravity).

Therefore, the modified equation at local scales becomes:

```
G_μν ≈ 8πG T_μν^(matter)     (+ small Λ_residual term)    ... (7.2)
```

This is indistinguishable from GR locally. Solar system tests are
passed trivially if ⟨T_μν⟩₀ is exactly uniform.

**Source:** [Tests of general relativity — Wikipedia](https://en.wikipedia.org/wiki/Tests_of_general_relativity)

### 7.2 When Would Modifications Become Observable?

The subtraction ⟨T_μν⟩₀ is uniform only in the condensate ground state.
If the condensate has spatial structure — e.g., near a black hole, or
at early cosmological times when the condensate was not yet in its ground
state — ⟨T_μν⟩₀ may vary spatially.

In that case:

```
∇_μ ⟨T_μν⟩₀ ≠ 0
→ G_μν = 8πG (T_μν − ⟨T_μν⟩₀) differs from GR locally
```

This could produce:
- Modified gravitational dynamics near black holes (relevant for strong-
  field tests: double pulsars, gravitational wave production)
- Modified expansion history at very early times (before condensate reached
  its ground state)
- Small modifications to post-Newtonian parameters at second order

**Source:** [Tests of general relativity — Wikipedia](https://en.wikipedia.org/wiki/Tests_of_general_relativity)

### 7.3 Key Risk: Stability of the Subtraction

The most serious risk: if ⟨T_μν⟩₀ is defined as the condensate ground
state, but the condensate is dynamically evolving (e.g., during phase
drift that drives dark energy), then ⟨T_μν⟩₀ is also time-evolving.
A time-evolving subtraction term is equivalent to a dynamical scalar
field modifying GR.

```
⟨T_μν⟩₀(t) evolving → G_μν = 8πG T_μν − 8πG ⟨T_μν⟩₀(t)
                      → Effectively: G_μν + f(t) g_μν = 8πG T_μν^(matter)
```

This is a form of scalar-tensor theory (an effective varying G or Λ).
Such theories are constrained by:
- Cassini bound: post-Newtonian parameter |γ − 1| < 2.3 × 10⁻⁵
- Lunar laser ranging (ω_BD > 40,000)

**Source:** [Brans–Dicke theory — Wikipedia](https://en.wikipedia.org/wiki/Brans%E2%80%93Dicke_theory)

The background subtraction must be shown to either:
1. Produce a static (time-independent) subtraction — eliminates this risk
2. Produce temporal variation too small to exceed current bounds

---

## 8. Assessment: What Is Resolved vs Open

### 8.1 What This Analysis Establishes

| Claim | Status |
|-------|--------|
| The PDTP trilemma is real — (a), (b), (c) cannot all hold | **Established** |
| The Palatini variation does NOT naturally produce background subtraction | **Established** |
| Background subtraction is the physically motivated Option 3 | **Established** |
| Three implementation options (A, B, C) are identified | **Established** |
| Option B (perturbative) is the most natural implementation | **PDTP Original** |
| Local physics (solar system) is not modified if ⟨T_μν⟩₀ is uniform | **Established** |
| Risks from time-varying ⟨T_μν⟩₀ are bounded by scalar-tensor constraints | **Established** |

### 8.2 What Remains Open

**Open problem 1: Formal derivation of Option B.**

The perturbative expansion of S_PDTP around the condensate ground state
must be carried out explicitly, including the Palatini sector. This
requires showing that the tetrad perturbation h^a_μ decouples cleanly
from the background e^a_μ = η^a_μ, and that no mixing terms reintroduce
ground-state contributions to T_μν.

**Open problem 2: Treatment of vacuum quantum fluctuations.**

The background subtraction removes the condensate ground-state
stress-energy. But QFT vacuum fluctuations (Casimir effect, zero-point
modes of Standard Model fields) are not intrinsically the condensate —
they are fields propagating ON the condensate. Whether T_μν^(phys) for
these fields is also subtracted requires a more detailed treatment of
how SM fields couple to the PDTP condensate.

**Open problem 3: Coincidence problem.**

Background subtraction explains why vacuum energy doesn't gravitate.
It does NOT explain why the residual (the dark energy) has the specific
value ρ_Λ ≈ 6 × 10⁻²⁷ kg/m³, nor why ρ_Λ ≈ ρ_matter today. The
coincidence problem remains open.

**Open problem 4: Stability of the ground-state definition.**

The subtraction ⟨T_μν⟩₀ must be self-consistently defined in the
presence of gravitational dynamics. Defining the "ground state" of a
system that is also the spacetime requires careful handling — the ground
state changes as the universe expands.

### 8.3 Verdict

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  Background Subtraction in PDTP:                             │
│                                                              │
│  RESOLVED:                                                   │
│  • Trilemma clearly diagnosed                                │
│  • Background subtraction is physically motivated            │
│  • Acoustic metric analogy shows mechanism is sound in       │
│    condensate physics                                        │
│  • Solar system tests not threatened (uniform subtraction)   │
│  • Comparison with known approaches shows PDTP approach is   │
│    distinct and complementary                                │
│                                                              │
│  OPEN:                                                       │
│  • Formal action-level derivation not yet done               │
│  • SM vacuum fluctuations require separate treatment         │
│  • Coincidence problem unaddressed                           │
│  • Ground-state definition under dynamical evolution unclear │
│                                                              │
│  STATUS: Conceptual framework complete; formal derivation     │
│  pending. Background subtraction is a viable but unverified  │
│  direction for resolving the tensor sector Λ problem.        │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

## 9. Summary

### 9.1 The Core Diagnosis

PDTP's scalar sector naturally filters vacuum energy (phase averaging).
The tensor sector does not — it inherits GR's exact coupling to all
stress-energy. This creates the PDTP trilemma: exact GR recovery,
scalar vacuum filtering, and tensor sector Λ resolution cannot all
simultaneously hold.

### 9.2 The Recommended Resolution

Condensate background subtraction (Option 3 / Option B):

- The condensate ground state defines the background metric
- Its stress-energy ⟨T_μν⟩₀ is already "encoded" in the tetrad
- Only deviations δT_μν = T_μν − ⟨T_μν⟩₀ appear as gravitating sources
- This is the PDTP version of the acoustic metric: the background
  condensate is geometry, not matter

### 9.3 Implementation

The natural implementation is a perturbative expansion of S_PDTP around
the condensate ground state. At linear order in perturbations, only
δφ, δψᵢ, δρ, and h^a_μ contribute to T_μν. The ground-state energy
is absorbed into the background Minkowski metric.

### 9.4 Comparison with Known Approaches

| Approach | Mechanism | PDTP similarity |
|----------|-----------|-----------------|
| Unimodular gravity | Λ = integration constant | Same spirit; different mechanism |
| Vacuum energy sequestering | Global Lagrange multiplier | Non-local; PDTP is local |
| Acoustic metric | Background = geometry | Direct physical analogy |
| Emergent gravity | GR as equation of state | Conceptually aligned |

### 9.5 What the Analysis Does NOT Solve

- The formal derivation of background subtraction from the PDTP action
- The coincidence problem (why ρ_Λ ~ ρ_matter now)
- The value of ρ_Λ from first principles
- SM vacuum fluctuations and their coupling to the condensate

---

## 10. References

### Established Sources

1. [Palatini variation — Wikipedia](https://en.wikipedia.org/wiki/Palatini_variation)
2. [Acoustic metric — Wikipedia](https://en.wikipedia.org/wiki/Acoustic_metric)
3. [Analog models of gravity — Wikipedia](https://en.wikipedia.org/wiki/Analog_models_of_gravity)
4. [Normal order — Wikipedia](https://en.wikipedia.org/wiki/Normal_order)
5. [Brans–Dicke theory — Wikipedia](https://en.wikipedia.org/wiki/Brans%E2%80%93Dicke_theory)
6. [Tests of general relativity — Wikipedia](https://en.wikipedia.org/wiki/Tests_of_general_relativity)
7. [Vacuum state — Wikipedia](https://en.wikipedia.org/wiki/Vacuum_state)
8. [Cosmological constant problem — Wikipedia](https://en.wikipedia.org/wiki/Cosmological_constant_problem)
9. Weinberg, S. (1989), "The cosmological constant problem," *Rev. Mod. Phys.* 61, 1
10. Carroll, S. (2004), *Spacetime and Geometry*, Addison-Wesley

### PDTP Internal References

11. [cosmological_constant_analysis.md](cosmological_constant_analysis.md) — Part 17
12. [tetrad_extension.md](tetrad_extension.md) — Part 12

### PDTP Original Results

1. The PDTP trilemma: simultaneous exact GR recovery, scalar vacuum
   filtering, and tensor Λ resolution are mutually inconsistent (§1.2)
2. Background subtraction removes double-counting of condensate ground-
   state energy in the Einstein equation (§3.3)
3. The Palatini variation does not naturally produce background subtraction
   — explicit action modification is required (§4.2)
4. Option B (perturbative expansion around ground state) is the most
   natural implementation, analogous to the acoustic metric derivation (§5.2)
5. Background subtraction with uniform ⟨T_μν⟩₀ does not modify local
   gravitational dynamics — solar system tests are passed (§7.1)

---

End of Document
