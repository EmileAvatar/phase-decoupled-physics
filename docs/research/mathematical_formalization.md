# Mathematical Formalization of PDTP

This document contains the rigorous mathematical foundations of the Phase-Decoupled
Transport Physics (PDTP) framework. Every established result is cited. Every new
result is marked as PDTP Original. Every derivation is shown step by step.

---

## Table of Contents

1. [Mathematical Prerequisites](#1-mathematical-prerequisites)
2. [The PDTP Lagrangian](#2-the-pdtp-lagrangian)
3. [Derivation of Field Equations](#3-derivation-of-field-equations)
4. [Connection to the Kuramoto Model](#4-connection-to-the-kuramoto-model)
5. [Conservation Laws via Noether's Theorem](#5-conservation-laws-via-noethers-theorem)
6. [Stability Analysis](#6-stability-analysis)
7. [Weak-Field Limit: Recovery of Newtonian Gravity](#7-weak-field-limit-recovery-of-newtonian-gravity)
8. [Energy Cost of Phase Control](#8-energy-cost-of-phase-control)
9. [Numerical Predictions](#9-numerical-predictions)
10. [Summary of Results](#10-summary-of-results)
11. [References](#11-references)

---

## 1. Mathematical Prerequisites

This section collects the established mathematical tools used throughout this
document. Nothing here is new — these are standard results from classical
mechanics, field theory, and nonlinear dynamics.

### 1.1 The Euler-Lagrange Equation for Fields

For a scalar field φ(x,t) with Lagrangian density L(φ, ∂μφ), the equation of
motion is obtained by extremizing the action S = ∫ L d⁴x.

The Euler-Lagrange equation for fields is:

```
∂L/∂φ − ∂μ(∂L/∂(∂μφ)) = 0
```

This is the field-theoretic generalization of the particle mechanics Euler-Lagrange
equation d/dt(∂L/∂q̇) − ∂L/∂q = 0.

For a free scalar field with L = ½(∂μφ)(∂^μ φ), the Euler-Lagrange equation gives
the Klein-Gordon equation □φ = 0, where □ = ∂²/∂t² − ∇² is the d'Alembertian
operator (in the (+,−,−,−) metric signature).

**Source:** [Lagrangian (field theory) — Wikipedia](https://en.wikipedia.org/wiki/Lagrangian_(field_theory))

**Source:** [Scalar field theory — Wikipedia](https://en.wikipedia.org/wiki/Scalar_field_theory)

### 1.2 Noether's Theorem

If the Lagrangian density L is invariant under a continuous symmetry
transformation, there exists a conserved current j^μ satisfying ∂μ j^μ = 0,
and a corresponding conserved charge Q = ∫ j⁰ d³x.

Key symmetry-conservation pairs:

| Symmetry | Conserved Quantity |
|----------|-------------------|
| Time translation (t → t + ε) | Energy |
| Space translation (x → x + ε) | Momentum |
| Internal phase rotation (φ → φ + ε) | Charge / particle number |

The conserved energy-momentum tensor (canonical stress-energy tensor) is:

```
T^μν = (∂L/∂(∂μφ)) ∂^ν φ − η^μν L
```

where η^μν is the Minkowski metric.

**Source:** [Noether's theorem — Wikipedia](https://en.wikipedia.org/wiki/Noether%27s_theorem)

**Source:** Noether, E. (1918), "Invariante Variationsprobleme,"
*Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen*, 235–257.

### 1.3 The Sine-Gordon Equation

The sine-Gordon equation is a well-studied nonlinear partial differential equation:

```
□φ + m² sin(φ) = 0
```

It arises from the Lagrangian density:

```
L_SG = ½(∂μφ)(∂^μ φ) + m²(cos(φ) − 1)
```

Key properties:
- Admits soliton (kink) and antisoliton solutions
- Solitons are topologically stable
- Exact integrability in 1+1 dimensions
- The potential V(φ) = m²(1 − cos(φ)) has minima at φ = 2πn (integer n)

The PDTP field equations are a multi-field generalization of the sine-Gordon
equation, where the argument of the sine/cosine is the phase difference between
two fields rather than a single field.

**Source:** [Sine-Gordon equation — Wikipedia](https://en.wikipedia.org/wiki/Sine-Gordon_equation)

### 1.4 The Kuramoto Model

The Kuramoto model describes synchronization in a population of N coupled
oscillators with natural frequencies ωᵢ:

```
dθᵢ/dt = ωᵢ + (K/N) Σⱼ sin(θⱼ − θᵢ)     (i = 1, ..., N)
```

Key results:
- Below a critical coupling K_c, oscillators remain incoherent
- Above K_c, spontaneous synchronization occurs (phase transition)
- The order parameter r = |N⁻¹ Σⱼ exp(iθⱼ)| measures synchronization (r=0
  incoherent, r=1 fully synchronized)
- For identical oscillators (all ωᵢ equal), K_c = 0 — any coupling synchronizes

The Kuramoto model is the first-order (overdamped) limit of the PDTP field
equations, as shown in Section 4.

**Source:** [Kuramoto model — Wikipedia](https://en.wikipedia.org/wiki/Kuramoto_model)

**Source:** Kuramoto, Y. (1975), "Self-entrainment of a population of coupled
non-linear oscillators," in *International Symposium on Mathematical Problems
in Theoretical Physics*, Lecture Notes in Physics, vol. 39, pp. 420–422.

**Source:** Strogatz, S. H. (2000), "From Kuramoto to Crawford: exploring the
onset of synchronization in populations of coupled oscillators,"
*Physica D*, 143(1–4), 1–20.

### 1.5 The De Broglie Relation

Every massive particle has an associated matter-wave with wavelength:

```
λ = h/p
```

and the general wavefunction:

```
ψ(x,t) = A · exp(i(k·x − ωt + φ₀))
```

where k = p/ℏ is the wave vector, ω = E/ℏ is the angular frequency, and φ₀ is
the initial phase. The phase φ₀ is a real, measurable quantity — atom
interferometry experiments routinely measure gravitational effects via quantum
phase shifts.

**Source:** [Matter wave — Wikipedia](https://en.wikipedia.org/wiki/Matter_wave)

### 1.6 Lyapunov Stability

A system ẋ = f(x) has an equilibrium point at x* if f(x*) = 0. The equilibrium
is stable in the sense of Lyapunov if there exists a function V(x) such that:

1. V(x*) = 0 and V(x) > 0 for x ≠ x*
2. dV/dt ≤ 0 along trajectories of the system

If dV/dt < 0 strictly, the equilibrium is asymptotically stable.

For Hamiltonian systems (no dissipation), the Hamiltonian H itself serves as a
Lyapunov function with dH/dt = 0, proving Lyapunov stability (but not asymptotic
stability).

**Source:** [Lyapunov stability — Wikipedia](https://en.wikipedia.org/wiki/Lyapunov_stability)

---

## 2. The PDTP Lagrangian

### 2.1 Statement of the Lagrangian

**PDTP Original.** The PDTP framework proposes a system of coupled scalar fields:

- φ(x,t) — the spacetime phase field (collective phase degree of freedom of
  spacetime)
- ψᵢ(x,t) — matter-wave phase fields (one for each matter source i)

The Lagrangian density is:

```
L = ½(∂μφ)(∂^μ φ) + Σᵢ ½(∂μψᵢ)(∂^μ ψᵢ) + Σᵢ gᵢ cos(ψᵢ − φ)
```

where gᵢ > 0 is the coupling strength of the i-th matter field to spacetime.

### 2.2 Interpretation of Each Term

| Term | Role | Physical Meaning |
|------|------|-----------------|
| ½(∂μφ)(∂^μ φ) | Spacetime kinetic term | Propagation dynamics of the spacetime phase field |
| ½(∂μψᵢ)(∂^μ ψᵢ) | Matter kinetic term | Propagation dynamics of each matter-wave |
| gᵢ cos(ψᵢ − φ) | Coupling potential | Phase-lock interaction between matter and spacetime |

### 2.3 Why the Coupling Sign Must Be Positive

The sign of the coupling term determines whether phase-alignment (ψᵢ = φ) is
a stable or unstable equilibrium. This is critical: gravity is attractive, so
phase-locking must be the stable (low-energy) state.

**Proof by reduction to simple pendulum.**

Consider one matter field ψ coupled to spacetime φ in 0+1 dimensions (time only,
no spatial dependence). Set ψ = const and let θ = ψ − φ be the phase difference.

With **positive** coupling (+g cos θ):

```
L = ½(dθ/dt)² + g cos(θ)
```

The Euler-Lagrange equation gives:

```
d²θ/dt² + g sin(θ) = 0                                           ... (2.1)
```

This is the equation of a simple pendulum (length ℓ, g_gravity → g). The
equilibrium at θ = 0 (phases aligned) is **stable**: small perturbations
θ = 0 + ε give d²ε/dt² ≈ −gε, which is simple harmonic oscillation with
frequency √g.

With **negative** coupling (−g cos θ):

```
L = ½(dθ/dt)² − g cos(θ)
```

The Euler-Lagrange equation gives:

```
d²θ/dt² − g sin(θ) = 0                                           ... (2.2)
```

The equilibrium at θ = 0 is **unstable**: small perturbations give
d²ε/dt² ≈ +gε, which grows exponentially. Phases spontaneously anti-align.
This describes repulsion, not gravity.

**Conclusion:** The coupling term must be **+gᵢ cos(ψᵢ − φ)**, not
−gᵢ cos(ψᵢ − φ). Phase-alignment is the stable equilibrium, corresponding
to normal gravitational attraction.

**Source for the pendulum analogy:** The simple pendulum Lagrangian
L = ½mℓ²θ̇² + mgℓcos(θ) is standard. See
[Pendulum (mechanics) — Wikipedia](https://en.wikipedia.org/wiki/Pendulum_(mechanics)).

### 2.4 Comparison to the Sine-Gordon Lagrangian

The sine-Gordon Lagrangian (Section 1.3) is:

```
L_SG = ½(∂μφ)(∂^μ φ) + m²(cos(φ) − 1)
```

The PDTP Lagrangian has the same mathematical structure, but with two key
differences:

1. The argument of cosine is a **phase difference** (ψᵢ − φ) between two
   dynamical fields, not a single field φ
2. There are **multiple** matter fields ψᵢ, each coupled to the same spacetime
   field φ

This makes PDTP a multi-component, heterogeneous sine-Gordon system — a known
class of integrable and near-integrable nonlinear field theories.

### 2.5 Erratum

Previous documents in this repository
([einstein_comparison.md](../technical/einstein_comparison.md),
[quantum_gravity_deep_dive.md](quantum_gravity_deep_dive.md)) wrote the coupling
term with a negative sign: `− Σᵢ gᵢ cos(ψᵢ − φ)`. The field equation
`□φ = Σᵢ gᵢ sin(ψᵢ − φ)` stated in those documents is correct — but it
corresponds to the **positive** coupling sign, not the negative one as written.
This erratum corrects the Lagrangian to match the intended (and correct) field
equation. See the derivation in Section 3.

---

## 3. Derivation of Field Equations

### 3.1 Spacetime Phase Field Equation

Starting from the Lagrangian density:

```
L = ½(∂μφ)(∂^μ φ) + Σᵢ ½(∂μψᵢ)(∂^μ ψᵢ) + Σᵢ gᵢ cos(ψᵢ − φ)
```

Apply the Euler-Lagrange equation (Section 1.1) for the field φ:

```
∂L/∂φ − ∂μ(∂L/∂(∂μφ)) = 0
```

**Step 1: Compute ∂L/∂φ.**

The only term in L that depends on φ (not on ∂μφ) is the coupling term.

```
∂/∂φ [gᵢ cos(ψᵢ − φ)]
```

Apply the chain rule. Let u = ψᵢ − φ, so du/dφ = −1.

```
d/dφ [cos(u)] = −sin(u) · (du/dφ) = −sin(ψᵢ − φ) · (−1) = sin(ψᵢ − φ)
```

Therefore:

```
∂L/∂φ = Σᵢ gᵢ sin(ψᵢ − φ)
```

**Step 2: Compute ∂μ(∂L/∂(∂μφ)).**

The only term in L that depends on ∂μφ is the kinetic term ½(∂μφ)(∂^μ φ).

```
∂L/∂(∂μφ) = ∂^μ φ
```

```
∂μ(∂L/∂(∂μφ)) = ∂μ ∂^μ φ = □φ
```

**Step 3: Combine.**

```
Σᵢ gᵢ sin(ψᵢ − φ) − □φ = 0
```

Therefore:

```
┌─────────────────────────────────────┐
│  □φ = Σᵢ gᵢ sin(ψᵢ − φ)           │  ... (3.1)
└─────────────────────────────────────┘
```

This is the **spacetime phase field equation**. Spacetime's phase responds to
the net phase mismatch from all matter sources.

### 3.2 Matter Phase Field Equation

Apply the Euler-Lagrange equation for the j-th matter field ψⱼ:

```
∂L/∂ψⱼ − ∂μ(∂L/∂(∂μψⱼ)) = 0
```

**Step 1: Compute ∂L/∂ψⱼ.**

```
∂/∂ψⱼ [gⱼ cos(ψⱼ − φ)] = −gⱼ sin(ψⱼ − φ)
```

(Here du/dψⱼ = +1, so d cos(u)/dψⱼ = −sin(u) · 1 = −sin(ψⱼ − φ).)

```
∂L/∂ψⱼ = −gⱼ sin(ψⱼ − φ)
```

**Step 2: Compute ∂μ(∂L/∂(∂μψⱼ)).**

```
∂μ(∂L/∂(∂μψⱼ)) = □ψⱼ
```

**Step 3: Combine.**

```
−gⱼ sin(ψⱼ − φ) − □ψⱼ = 0
```

Therefore:

```
┌─────────────────────────────────────┐
│  □ψⱼ = −gⱼ sin(ψⱼ − φ)            │  ... (3.2)
└─────────────────────────────────────┘
```

This is the **matter phase field equation**. Each matter-wave is driven toward
phase alignment with spacetime.

### 3.3 Verification: Mutual Attraction

Equations (3.1) and (3.2) together describe mutual phase-locking:

- Spacetime (φ) is pulled toward matter phases (ψᵢ) by equation (3.1)
- Matter (ψⱼ) is pulled toward spacetime phase (φ) by equation (3.2)

To verify: consider one matter field ψ with θ = ψ − φ.

From (3.1): □φ = g sin(θ) — spacetime accelerates toward matter
From (3.2): □ψ = −g sin(θ) — matter accelerates toward spacetime

The relative phase satisfies:

```
□θ = □ψ − □φ = −g sin(θ) − g sin(θ) = −2g sin(θ)
```

In 0+1 dimensions: d²θ/dt² = −2g sin(θ). This is a pendulum equation with
effective coupling 2g. The equilibrium θ = 0 (phases locked) is **stable** with
oscillation frequency √(2g). ✓

### 3.4 Connection to Sine-Gordon

For a single matter-wave with ψ = const (external source), equation (3.1) becomes:

```
□φ + g sin(φ − ψ) = 0
```

This is exactly the sine-Gordon equation (Section 1.3) with a phase offset ψ.
All known sine-Gordon results (solitons, topological stability, Bäcklund
transforms) apply directly.

**Source:** This identification follows immediately from comparing with the
sine-Gordon equation □u + sin(u) = 0.
See [Sine-Gordon equation — Wikipedia](https://en.wikipedia.org/wiki/Sine-Gordon_equation).

---

## 4. Connection to the Kuramoto Model

### 4.1 The Overdamped Limit

**PDTP Original.** In condensed matter and biological systems, oscillator dynamics
are often overdamped — friction dominates over inertia, so the second-order
equation d²θ/dt² = −g sin(θ) − γ dθ/dt reduces to the first-order equation
γ dθ/dt ≈ −g sin(θ).

Apply this to the PDTP field equations. In the overdamped limit with damping γ,
for N oscillators at spatial positions xᵢ (ignoring spatial gradients):

From (3.1): γ_φ dφ/dt = Σᵢ gᵢ sin(ψᵢ − φ)

From (3.2): γ_ψ dψⱼ/dt = −gⱼ sin(ψⱼ − φ)

Adding natural frequencies ωᵢ (each oscillator has an intrinsic frequency):

```
dψⱼ/dt = ωⱼ − (gⱼ/γ_ψ) sin(ψⱼ − φ)
```

If we identify the spacetime field φ as the mean field (order parameter) of the
collective, this is precisely the **Kuramoto model** (Section 1.4):

```
dθᵢ/dt = ωᵢ + (K/N) Σⱼ sin(θⱼ − θᵢ)
```

with K = g/γ playing the role of the coupling constant.

### 4.2 Imported Results

Because the PDTP field equations reduce to the Kuramoto model in the overdamped
limit, all known Kuramoto results apply:

| Kuramoto Result | PDTP Implication |
|----------------|------------------|
| Critical coupling K_c exists | There is a minimum coupling g_c below which phase-locking fails |
| Spontaneous synchronization above K_c | Above g_c, matter automatically phase-locks to spacetime (= gravity emerges) |
| Order parameter r measures sync | r measures the degree of gravitational coupling |
| Identical oscillators: K_c = 0 | Identical matter-waves always synchronize (gravity is universal for identical particles) |
| Frequency distribution width Δω raises K_c | Greater mass diversity requires stronger coupling for gravitational coherence |

**Source:** Strogatz, S. H. (2000), "From Kuramoto to Crawford," *Physica D*,
143(1–4), 1–20. Available at:
[http://web.mit.edu/~jadbabai/www/ESE680/Strogatz_Kuramoto.pdf](http://web.mit.edu/~jadbabai/www/ESE680/Strogatz_Kuramoto.pdf)

### 4.3 PDTP as a Field-Theoretic Kuramoto Model

**PDTP Original.** The standard Kuramoto model describes N discrete oscillators
coupled all-to-all. The PDTP Lagrangian extends this to a continuum field theory
in 3+1 dimensions:

| Feature | Kuramoto | PDTP |
|---------|----------|------|
| Variables | Discrete phases θᵢ | Continuous fields φ(x,t), ψᵢ(x,t) |
| Dynamics | First-order (overdamped) | Second-order (wave equation) |
| Coupling | All-to-all, mean field | Local, through spacetime field φ |
| Spatial structure | None | Full 3+1 dimensional spacetime |
| Solitons | No | Yes (sine-Gordon kinks) |
| Lorentz invariance | No | Yes (by construction) |

The PDTP Lagrangian can be viewed as the relativistic, spatially extended,
second-order generalization of the Kuramoto model.

---

## 5. Conservation Laws via Noether's Theorem

### 5.1 Time Translation Symmetry → Energy Conservation

The Lagrangian L does not depend explicitly on time t. By Noether's theorem
(Section 1.2), this implies conservation of the Hamiltonian (energy).

**Derivation of the Hamiltonian density.**

The canonical momentum conjugate to φ is:

```
πφ = ∂L/∂(∂₀φ) = ∂₀φ = dφ/dt
```

Similarly for each ψⱼ:

```
πψⱼ = ∂L/∂(∂₀ψⱼ) = ∂₀ψⱼ = dψⱼ/dt
```

The Hamiltonian density is H = Σ (πᵢ · ∂₀φᵢ) − L:

```
H = πφ(∂₀φ) + Σⱼ πψⱼ(∂₀ψⱼ) − L
```

Substituting:

```
H = (∂₀φ)² + Σⱼ (∂₀ψⱼ)²
    − [½(∂₀φ)² − ½(∇φ)² + Σⱼ ½(∂₀ψⱼ)² − Σⱼ ½(∇ψⱼ)² + Σⱼ gⱼ cos(ψⱼ−φ)]
```

Note: (∂μφ)(∂^μφ) = (∂₀φ)² − (∇φ)² in the (+,−,−,−) metric.

Simplifying:

```
┌────────────────────────────────────────────────────────────────────┐
│  H = ½(∂₀φ)² + ½(∇φ)²                                            │
│    + Σⱼ [½(∂₀ψⱼ)² + ½(∇ψⱼ)²]                                    │
│    − Σⱼ gⱼ cos(ψⱼ − φ)                                           │  ... (5.1)
└────────────────────────────────────────────────────────────────────┘
```

The total energy E = ∫ H d³x is conserved: dE/dt = 0.

**Interpretation of each term:**

| Term | Type | Meaning |
|------|------|---------|
| ½(∂₀φ)² | Kinetic | Spacetime phase oscillation energy |
| ½(∇φ)² | Gradient | Spacetime phase spatial variation energy |
| ½(∂₀ψⱼ)² | Kinetic | Matter-wave oscillation energy |
| ½(∇ψⱼ)² | Gradient | Matter-wave spatial variation energy |
| −gⱼ cos(ψⱼ−φ) | Potential | Phase-lock energy (minimized when locked) |

The potential energy −gⱼ cos(ψⱼ − φ):
- Minimum value = −gⱼ when ψⱼ = φ (fully locked, lowest energy)
- Maximum value = +gⱼ when ψⱼ = φ + π (fully anti-locked, highest energy)
- Zero when ψⱼ = φ ± π/2 (decoupled)

This confirms that phase-locking is the energetically favored state (gravity
attracts to the lowest energy configuration).

### 5.2 Space Translation Symmetry → Momentum Conservation

The Lagrangian does not depend explicitly on spatial coordinates. By Noether's
theorem, the momentum density is conserved.

The canonical momentum density (k-th component) is:

```
P^k = πφ(∂^k φ) + Σⱼ πψⱼ(∂^k ψⱼ)
    = (∂₀φ)(∂^k φ) + Σⱼ (∂₀ψⱼ)(∂^k ψⱼ)                           ... (5.2)
```

The total momentum P = ∫ P^k d³x is conserved: dP/dt = 0.

### 5.3 Global Phase Shift Symmetry → Charge Conservation

The Lagrangian is invariant under a simultaneous global phase shift of all fields:

```
φ → φ + ε,  ψᵢ → ψᵢ + ε    (for all i)
```

because the coupling term cos(ψᵢ − φ) depends only on the difference, which is
unchanged by this shift.

By Noether's theorem, the associated conserved current is:

```
j^μ = ∂^μ φ + Σᵢ ∂^μ ψᵢ                                            ... (5.3)
```

and the conserved charge is:

```
Q = ∫ (∂₀φ + Σᵢ ∂₀ψᵢ) d³x                                         ... (5.4)
```

**PDTP interpretation:** This conserved charge represents the total "phase
momentum" of the system — the sum of all phase rates of change. It is the
analogue of total particle number in conventional field theory.

### 5.4 Verification: Energy Is Conserved On-Shell

To verify equation (5.1) directly, compute dH/dt using the field equations
(3.1) and (3.2):

```
dH/dt = (∂₀φ)(∂₀²φ) + (∇φ)·(∇∂₀φ)
      + Σⱼ [(∂₀ψⱼ)(∂₀²ψⱼ) + (∇ψⱼ)·(∇∂₀ψⱼ)]
      + Σⱼ gⱼ sin(ψⱼ−φ)(∂₀ψⱼ − ∂₀φ)
```

Using integration by parts: (∇φ)·(∇∂₀φ) → −(∇²φ)(∂₀φ) + boundary terms.

So:

```
dH/dt = (∂₀φ)(∂₀²φ − ∇²φ) + Σⱼ (∂₀ψⱼ)(∂₀²ψⱼ − ∇²ψⱼ)
      + Σⱼ gⱼ sin(ψⱼ−φ)(∂₀ψⱼ − ∂₀φ)
```

Using □φ = ∂₀²φ − ∇²φ:

```
dH/dt = (∂₀φ)(□φ) + Σⱼ (∂₀ψⱼ)(□ψⱼ)
      + Σⱼ gⱼ sin(ψⱼ−φ)(∂₀ψⱼ − ∂₀φ)
```

Substitute the field equations □φ = Σᵢ gᵢ sin(ψᵢ−φ) and □ψⱼ = −gⱼ sin(ψⱼ−φ):

```
dH/dt = (∂₀φ) Σᵢ gᵢ sin(ψᵢ−φ) + Σⱼ (∂₀ψⱼ)(−gⱼ sin(ψⱼ−φ))
      + Σⱼ gⱼ sin(ψⱼ−φ)(∂₀ψⱼ − ∂₀φ)
```

```
     = Σⱼ gⱼ sin(ψⱼ−φ) [(∂₀φ) − (∂₀ψⱼ) + (∂₀ψⱼ) − (∂₀φ)]
     = Σⱼ gⱼ sin(ψⱼ−φ) · 0
     = 0  ✓
```

Energy is exactly conserved. ✓

**Source for the method:** Standard Noether verification. See
[Noether's theorem — Wikipedia](https://en.wikipedia.org/wiki/Noether%27s_theorem).

---

## 6. Stability Analysis

### 6.1 Equilibrium State

The equilibrium (ground state) of the system is:

```
ψᵢ = φ = const    (all phases aligned, no spatial or temporal variation)
```

At equilibrium:
- All kinetic terms vanish: ∂₀φ = ∂₀ψᵢ = 0
- All gradient terms vanish: ∇φ = ∇ψᵢ = 0
- The coupling is at minimum energy: cos(ψᵢ − φ) = cos(0) = 1

### 6.2 Linearized Stability

**PDTP Original.** Perturb around equilibrium: let ψᵢ = φ₀ + δψᵢ and
φ = φ₀ + δφ, where δψᵢ and δφ are small perturbations.

Define the relative phase perturbation: θᵢ = δψᵢ − δφ.

From the combined equation (Section 3.3):

```
□θᵢ = −2gᵢ sin(θᵢ)
```

Linearize for small θᵢ (sin θ ≈ θ):

```
□θᵢ = −2gᵢ θᵢ
```

```
∂²θᵢ/∂t² − ∇²θᵢ = −2gᵢ θᵢ
```

```
∂²θᵢ/∂t² = ∇²θᵢ − 2gᵢ θᵢ                                          ... (6.1)
```

This is the **Klein-Gordon equation** with mass parameter m² = 2gᵢ:

```
(□ + 2gᵢ) θᵢ = 0
```

**Source:** The Klein-Gordon equation □φ + m²φ = 0 is the standard relativistic
wave equation for a massive scalar field. See
[Klein-Gordon equation — Wikipedia](https://en.wikipedia.org/wiki/Klein%E2%80%93Gordon_equation).

### 6.3 Dispersion Relation

Substitute a plane-wave ansatz θᵢ = θ₀ exp(i(k·x − ωt)):

```
−ω² + |k|² + 2gᵢ = 0
```

```
ω² = |k|² + 2gᵢ                                                    ... (6.2)
```

Since gᵢ > 0, we have ω² > 0 for all wave vectors k. Therefore ω is real
for all k, meaning:

- **No exponentially growing modes** — the equilibrium is stable
- **All perturbations oscillate** — they are bounded forever
- The "mass gap" √(2gᵢ) sets the minimum oscillation frequency

### 6.4 Physical Interpretation

The linearized perturbations of the phase-lock are massive Klein-Gordon waves.
This means:

1. **Phase-locking is stable** — small disturbances oscillate around the locked
   state, they do not grow
2. **The coupling strength gᵢ determines the "stiffness"** — stronger coupling
   means higher-frequency oscillations and faster return to equilibrium
3. **There is a mass gap** — perturbations below frequency √(2gᵢ) cannot
   propagate as free waves (they are evanescent)
4. **This is exactly how a Higgs-type mechanism works** — a cos potential with
   a minimum gives a mass to the fluctuations around that minimum

### 6.5 Lyapunov Stability via the Hamiltonian

The Hamiltonian (5.1) is bounded from below:

```
H ≥ −Σⱼ gⱼ    (minimum when all kinetic/gradient terms vanish and all
                phases are locked)
```

Since H is conserved (dH/dt = 0, proven in Section 5.4), the system cannot
escape from bounded energy surfaces. Any trajectory starting near the
equilibrium remains near it forever. This proves **Lyapunov stability**.

For asymptotic stability (actual convergence to equilibrium), additional
dissipation is required — e.g., coupling to an environment (decoherence).
In the Kuramoto limit (overdamped, Section 4.1), the damping γ provides this,
and asymptotic stability is proven for K > K_c.

**Source:** Jadbabaie, A., Motee, N., and Barahona, M. (2004), "On the
stability of the Kuramoto model of coupled nonlinear oscillators," in
*Proc. American Control Conference*. Available at:
[https://web.mit.edu/~jadbabai/www/ESE680/Kuramoto_reallyfinal.pdf](https://web.mit.edu/~jadbabai/www/ESE680/Kuramoto_reallyfinal.pdf)

---

## 7. Weak-Field Limit: Recovery of Newtonian Gravity

This section demonstrates that the PDTP field equations reduce to Newtonian
gravity in the appropriate limit. This is the most important consistency check.

### 7.1 Setup

**PDTP Original.** Consider a static, spherically symmetric mass M centered at
the origin. The mass consists of N matter-waves, all approximately phase-locked
to spacetime (normal matter: ψᵢ ≈ φ everywhere inside the mass).

We seek the spacetime phase field φ(r) outside the mass.

### 7.2 The Field Equation Outside Matter

Outside the mass (r > R, where R is the radius of the mass), there are no
matter sources. Equation (3.1) becomes:

```
□φ = 0    (no sources outside the mass)
```

In the static case (∂φ/∂t = 0):

```
∇²φ = 0                                                             ... (7.1)
```

This is the **Laplace equation** — the same equation that governs the Newtonian
gravitational potential outside a mass, and the electrostatic potential outside a
charge distribution.

**Source:** The Laplace equation ∇²Φ = 0 governs the gravitational potential
in vacuum. See
[Laplace's equation — Wikipedia](https://en.wikipedia.org/wiki/Laplace%27s_equation).

### 7.3 Spherically Symmetric Solution

For a spherically symmetric solution depending only on r = |x|:

```
∇²φ = (1/r²) d/dr(r² dφ/dr) = 0
```

The general solution is:

```
φ(r) = −C/r + φ_∞                                                   ... (7.2)
```

where C is a constant to be determined by matching to the interior, and φ_∞
is the asymptotic value at infinity.

This is a **1/r potential** — the same radial dependence as the Newtonian
gravitational potential Φ_N = −GM/r.

### 7.4 Matching to the Interior (Gauss's Law)

Inside the mass (r < R), equation (3.1) gives:

```
∇²φ = −Σᵢ gᵢ sin(ψᵢ − φ)    (static case, with ∂²φ/∂t² = 0)
```

Note: □φ = ∂²φ/∂t² − ∇²φ, so in the static case □φ = −∇²φ, and
□φ = Σᵢ gᵢ sin(ψᵢ − φ) gives −∇²φ = Σᵢ gᵢ sin(ψᵢ − φ), i.e.,
∇²φ = −Σᵢ gᵢ sin(ψᵢ − φ).

Integrate both sides over a sphere of radius r > R (enclosing the entire mass):

```
∫ ∇²φ d³x = −∫ Σᵢ gᵢ sin(ψᵢ − φ) d³x
```

By the divergence theorem (left side):

```
∮ ∇φ · dA = −∫ Σᵢ gᵢ sin(ψᵢ − φ) d³x
```

For the spherically symmetric exterior solution φ = −C/r + φ_∞:

```
∇φ = C/r² r̂
```

```
∮ ∇φ · dA = (C/r²)(4πr²) = 4πC
```

Therefore:

```
4πC = −∫ Σᵢ gᵢ sin(ψᵢ − φ) d³x                                    ... (7.3)
```

**Source for the divergence theorem:** See
[Divergence theorem — Wikipedia](https://en.wikipedia.org/wiki/Divergence_theorem).

### 7.5 Identification with Newton's Constant

Comparing equation (7.2) to the Newtonian potential Φ_N = −GM/r:

```
φ(r) − φ_∞ = −C/r    ↔    Φ_N = −GM/r
```

This requires: C = GM (up to a proportionality constant that sets units).

From equation (7.3):

```
GM = −(1/4π) ∫ Σᵢ gᵢ sin(ψᵢ − φ) d³x
```

In the weak-field limit (ψᵢ ≈ φ inside the mass, small phase differences):

```
sin(ψᵢ − φ) ≈ ψᵢ − φ
```

Define the **phase-charge density**:

```
ρ_phase(x) = Σᵢ gᵢ (ψᵢ(x) − φ(x))                                ... (7.4)
```

Then:

```
∇²φ = −ρ_phase                                                      ... (7.5)
```

This is the **Poisson equation for gravity**:

```
∇²Φ_N = 4πG ρ_mass
```

with the identification:

```
┌─────────────────────────────────────┐
│  ρ_phase ↔ 4πG ρ_mass              │  ... (7.6)
└─────────────────────────────────────┘
```

**The coupling constants gᵢ and the phase differences (ψᵢ − φ) encode what
Newtonian gravity calls "mass."** Newton's constant G is determined by the
relationship between coupling strength and mass density.

**Source:** The Poisson equation ∇²Φ = 4πGρ for Newtonian gravity is standard.
See [Poisson's equation — Wikipedia](https://en.wikipedia.org/wiki/Poisson%27s_equation#Newtonian_gravity).

### 7.6 Summary of the Newtonian Recovery

| PDTP Quantity | Newtonian Quantity |
|--------------|-------------------|
| Spacetime phase field φ(r) | Gravitational potential Φ(r) |
| Phase-charge density ρ_phase = Σ gᵢ(ψᵢ−φ) | Mass density ρ · 4πG |
| □φ = 0 outside matter | ∇²Φ = 0 outside matter (Laplace equation) |
| □φ = Σ gᵢ sin(ψᵢ−φ) inside matter | ∇²Φ = 4πGρ inside matter (Poisson equation) |
| φ ~ −C/r | Φ ~ −GM/r |
| Gauss's law matching at boundary | Gauss's law for gravity |

**PDTP recovers Newtonian gravity exactly in the weak-field, static limit.** ✓

---

## 8. Energy Cost of Phase Control

### 8.1 Energy to Decouple from Gravity

**PDTP Original.** From the Hamiltonian density (5.1), the potential energy of the
phase-lock between one matter-wave ψⱼ and spacetime φ is:

```
V_coupling = −gⱼ cos(ψⱼ − φ)
```

The energy states:

| Phase difference | cos(Δψ) | V_coupling | State |
|-----------------|---------|------------|-------|
| 0 (locked) | 1 | −gⱼ | Normal gravity (ground state) |
| π/4 (partial) | 1/√2 | −gⱼ/√2 | Reduced gravity |
| π/2 (decoupled) | 0 | 0 | Zero gravity |
| π (anti-locked) | −1 | +gⱼ | Maximum energy (unstable) |

The energy cost to go from fully locked to fully decoupled:

```
ΔE_decouple = V(π/2) − V(0) = 0 − (−gⱼ) = gⱼ                     ... (8.1)
```

### 8.2 Relating gⱼ to Known Physics

From Section 7, the coupling gⱼ is related to Newton's constant G and mass.
Specifically, from equation (7.6):

```
gⱼ · (ψⱼ − φ) ∼ 4πG · mⱼ · δ³(x − xⱼ)
```

For a point mass at rest, the gravitational self-energy is of order:

```
E_grav ∼ Gm²/R
```

where R is the size of the object. The coupling energy gⱼ is therefore related
to the gravitational binding energy.

**Order of magnitude estimate for gⱼ:**

For a 1 kg mass of radius R ∼ 0.1 m:

```
E_grav = Gm²/R = (6.674 × 10⁻¹¹)(1)²/(0.1) ≈ 6.7 × 10⁻¹⁰ J
```

This is an extraordinarily small energy — about 4 eV, or roughly the energy of
a single photon of visible light.

**PDTP Original.** This suggests that the energy cost to decouple a 1 kg mass
from gravity is of order its gravitational self-energy — approximately 10⁻⁹ J.
This is a strikingly small number.

### 8.3 Caveat

This estimate uses the gravitational self-energy as a proxy for gⱼ. The actual
relationship between gⱼ and measurable quantities requires solving the full
field equations with specific boundary conditions, which has not yet been done.
The estimate should be treated as an order-of-magnitude guide, not a precise
prediction.

### 8.4 Energy of Spatial Phase Gradients

If the coupling parameter α = cos(ψ−φ) varies in space (e.g., decoupled in
one region, locked elsewhere), there must be a transition region where ψ−φ
changes from 0 to π/2. This gradient costs additional energy:

```
E_gradient = ∫ ½(∇(ψ−φ))² d³x                                     ... (8.2)
```

From the gradient terms in the Hamiltonian. Sharper transitions (smaller
transition region) cost more energy. This is analogous to domain wall energy
in ferromagnets.

**Source for domain wall analogy:** See
[Domain wall (magnetism) — Wikipedia](https://en.wikipedia.org/wiki/Domain_wall_(magnetism)).

---

## 9. Numerical Predictions

### 9.1 The Coupling Parameter for Earth's Surface Gravity

**PDTP Original.** At Earth's surface, the Newtonian gravitational potential is:

```
Φ_N = −GM_Earth/R_Earth = −(6.674×10⁻¹¹)(5.972×10²⁴)/(6.371×10⁶)
     ≈ −6.25 × 10⁷ J/kg
```

The dimensionless gravitational potential is:

```
Φ_N/c² = −6.25 × 10⁷ / (3 × 10⁸)² ≈ −6.95 × 10⁻¹⁰
```

**Source:** The dimensionless potential GM/(rc²) characterizes the strength of
gravity. See
[Schwarzschild metric — Wikipedia](https://en.wikipedia.org/wiki/Schwarzschild_metric).

If the phase difference δφ = ψ − φ is proportional to the dimensionless potential:

```
δφ ∼ GM/(rc²) ∼ 7 × 10⁻¹⁰ radians
```

The coupling parameter deviation from unity:

```
δα = 1 − cos(δφ) ≈ ½(δφ)² ≈ ½(7 × 10⁻¹⁰)² ≈ 2.4 × 10⁻¹⁹       ... (9.1)
```

This is the predicted deviation of α from 1 at Earth's surface. It is
unmeasurably small with current technology (best gravimeters achieve ∼10⁻⁹
relative precision).

### 9.2 BEC Gravitational Anomaly Estimate

A Bose-Einstein Condensate (BEC) has N atoms sharing one quantum phase state.

**Source:** [Bose-Einstein condensate — Wikipedia](https://en.wikipedia.org/wiki/Bose%E2%80%93Einstein_condensate)

For a typical BEC:
- N ∼ 10⁶ atoms
- Atom mass m ∼ 10⁻²⁵ kg (rubidium-87)
- BEC size R ∼ 10⁻⁵ m

The gravitational self-energy of the BEC:

```
E_grav = GN²m²/R = (6.674×10⁻¹¹)(10⁶)²(10⁻²⁵)²/(10⁻⁵)
       = (6.674×10⁻¹¹)(10¹²)(10⁻⁵⁰)/(10⁻⁵)
       = 6.674 × 10⁻⁴⁴ J
```

This is about 4 × 10⁻²⁵ eV — far below any detectable threshold.

**PDTP Original.** The key question is whether quantum coherence amplifies the
phase effect. In incoherent matter, each atom's phase is random, so the net
phase-lock stress averages as √N (random walk). In a BEC, all N atoms share
one phase, so the net phase-lock stress scales as N (coherent sum).

The coherence amplification factor:

```
A_coherence = N / √N = √N                                           ... (9.2)
```

For N = 10⁶: A_coherence = 10³.

This amplifies the effective δφ by a factor of 10³, but from a baseline of
∼10⁻¹⁰, the result is still ∼10⁻⁷ — potentially within reach of future
atom interferometry experiments (current precision ∼10⁻⁹).

### 9.3 Predictions Summary Table

| Observable | PDTP Prediction | Current Precision | Testable? |
|-----------|----------------|-------------------|-----------|
| δα at Earth surface | ∼10⁻¹⁹ | ∼10⁻⁹ | No (10 orders of magnitude gap) |
| δα in BEC (N=10⁶) | ∼10⁻⁷ (with coherence amplification) | ∼10⁻⁹ | Approaching (2 orders of magnitude gap) |
| δα in large BEC (N=10¹⁰) | ∼10⁻⁵ | ∼10⁻⁹ | Yes, if large coherent systems can be built |
| Phase perturbation frequency | √(2g) ∼ ? | Gravitational wave detectors | Requires knowing g precisely |

### 9.4 Falsifiability

PDTP makes the following falsifiable predictions:

1. **A coherent matter system (BEC) should show a different free-fall rate than
   the same atoms in an incoherent gas**, with the deviation scaling as √N.

2. **The deviation should depend on the coherence of the system** — destroying
   coherence (by heating, for example) should eliminate the anomaly.

3. **The deviation should NOT depend on the chemical composition** of the atoms,
   only on N (number of coherent atoms) and g (coupling strength, which is
   universal for identical particles).

If any of these are observed, PDTP is supported. If coherent matter systems
show identical free-fall to incoherent matter at sufficient precision, PDTP's
coherence amplification mechanism is falsified.

---

## 10. Summary of Results

### What Has Been Derived

| Result | Section | Status |
|--------|---------|--------|
| Corrected Lagrangian (sign fix) | 2.3 | **PDTP Original** — stability proof |
| Spacetime field equation: □φ = Σ gᵢ sin(ψᵢ−φ) | 3.1 | Derived from Euler-Lagrange |
| Matter field equation: □ψⱼ = −gⱼ sin(ψⱼ−φ) | 3.2 | Derived from Euler-Lagrange |
| Mutual phase-locking verified | 3.3 | Derived |
| Connection to Kuramoto model | 4.1 | **PDTP Original** — new identification |
| Energy conservation | 5.1, 5.4 | Derived via Noether + verified directly |
| Momentum conservation | 5.2 | Derived via Noether |
| Phase charge conservation | 5.3 | Derived via Noether |
| Linearized stability (Klein-Gordon form) | 6.2 | Derived |
| Dispersion relation ω² = k² + 2g | 6.3 | Derived — all modes stable |
| Lyapunov stability | 6.5 | Proved via bounded Hamiltonian |
| Newtonian gravity recovery (1/r potential) | 7.2–7.5 | **PDTP Original** — key result |
| Poisson equation recovery | 7.5 | **PDTP Original** — weak-field limit |
| Energy cost of decoupling | 8.1–8.2 | **PDTP Original** — order of magnitude |
| Numerical predictions for BEC experiments | 9.2 | **PDTP Original** — falsifiable |

### What Remains Open

| Gap | Difficulty | Notes |
|-----|-----------|-------|
| Exact relationship between gᵢ and G | Medium | Requires solving the full nonlinear system |
| Post-Newtonian corrections (perihelion precession, etc.) | Hard | Need to go beyond the linearized limit |
| Quantum description of spacetime phase field φ | Very Hard | φ is not defined in standard QFT |
| EM and nuclear force integration | Hard | Current Lagrangian only describes gravity |
| Experimental test design | Engineering | Need ∼10⁻⁷ precision in coherent systems |

---

## 11. References

### Cited Sources (Established Physics)

1. [Lagrangian (field theory) — Wikipedia](https://en.wikipedia.org/wiki/Lagrangian_(field_theory))
2. [Scalar field theory — Wikipedia](https://en.wikipedia.org/wiki/Scalar_field_theory)
3. [Noether's theorem — Wikipedia](https://en.wikipedia.org/wiki/Noether%27s_theorem)
4. Noether, E. (1918), "Invariante Variationsprobleme,"
   *Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen*, 235–257.
5. [Sine-Gordon equation — Wikipedia](https://en.wikipedia.org/wiki/Sine-Gordon_equation)
6. [Kuramoto model — Wikipedia](https://en.wikipedia.org/wiki/Kuramoto_model)
7. Kuramoto, Y. (1975), "Self-entrainment of a population of coupled non-linear
   oscillators," in *International Symposium on Mathematical Problems in
   Theoretical Physics*, Lecture Notes in Physics, vol. 39, pp. 420–422.
8. Strogatz, S. H. (2000), "From Kuramoto to Crawford: exploring the onset of
   synchronization in populations of coupled oscillators," *Physica D*,
   143(1–4), 1–20.
   [PDF](http://web.mit.edu/~jadbabai/www/ESE680/Strogatz_Kuramoto.pdf)
9. Jadbabaie, A., Motee, N., and Barahona, M. (2004), "On the stability of
   the Kuramoto model of coupled nonlinear oscillators," in *Proc. American
   Control Conference*.
   [PDF](https://web.mit.edu/~jadbabai/www/ESE680/Kuramoto_reallyfinal.pdf)
10. [Klein-Gordon equation — Wikipedia](https://en.wikipedia.org/wiki/Klein%E2%80%93Gordon_equation)
11. [Matter wave — Wikipedia](https://en.wikipedia.org/wiki/Matter_wave)
12. [Lyapunov stability — Wikipedia](https://en.wikipedia.org/wiki/Lyapunov_stability)
13. [Pendulum (mechanics) — Wikipedia](https://en.wikipedia.org/wiki/Pendulum_(mechanics))
14. [Laplace's equation — Wikipedia](https://en.wikipedia.org/wiki/Laplace%27s_equation)
15. [Divergence theorem — Wikipedia](https://en.wikipedia.org/wiki/Divergence_theorem)
16. [Poisson's equation — Wikipedia](https://en.wikipedia.org/wiki/Poisson%27s_equation#Newtonian_gravity)
17. [Schwarzschild metric — Wikipedia](https://en.wikipedia.org/wiki/Schwarzschild_metric)
18. [Bose-Einstein condensate — Wikipedia](https://en.wikipedia.org/wiki/Bose%E2%80%93Einstein_condensate)
19. [Domain wall (magnetism) — Wikipedia](https://en.wikipedia.org/wiki/Domain_wall_(magnetism))

---

This document is part of the Phase-Decoupled Physics project.
It contains both established physics (cited) and speculative extensions
(marked as PDTP Original). The speculative content has not been
experimentally validated.

---

End of Document
