# Loss Tangent and Dark Energy Crossover (Part 102, T3)

**Status:** PARTIAL — mapping works, cosmological z-prediction fails
**Date:** 2026-04-07
**Script:** `simulations/solver/t3_loss_tangent.py`
**Prerequisites:**
- [tan_critical_point.md](tan_critical_point.md) — Part 99: the Δ = π/4 critical point
- [wz_dark_energy_pdtp.md](wz_dark_energy_pdtp.md) — Part 25: slow-roll w(z) from phase drift
- [phase_drift_mechanism.md](phase_drift_mechanism.md) — Part 19: Langevin dark energy
- [cosmological_constant_fcc.md](cosmological_constant_fcc.md) — Part 54: Λ as free parameter

---

## 1. Plain English Summary

Part 99 found a critical point in the PDTP pendulum at Δ = π/4 where the "restoring
coupling" equals the "decoupling force" (tan Δ = 1). The potential energy there is
29.3% of the maximum possible — we called that the "sizzling onset".

This part (T3) asks a concrete question:

> **Is the universe *at* this sizzling crossover *today*, and does that explain
> why the DESI DR2 data shows an apparent dark energy transition around z ≈ 0.5-0.7?**

**Short answer:** structurally yes, cosmologically no.

1. The math works out: the full nonlinear pendulum (not just the harmonic approximation
   of Part 25) gives a clean slow-roll formula ε = g(1 + cos Δ)/(9H²), which reduces
   exactly to the Part 25 result in the Δ → 0 limit.
2. There is a suggestive numerical coincidence: f_c = 1 − 1/√2 ≈ 0.293 is within 7%
   of today's matter density fraction Ω_m,0 ≈ 0.315.
3. **But** the slow-roll equation of motion *damps* Δ toward 0, not away from it.
   A naive "drift growing with time" picture is backwards. The PDTP pendulum is a
   relaxing oscillator, not a tensioning one.
4. And even if we force Case A (Δ_0 = π/4 exactly today), the predicted w_a
   (≈ −0.147) is a factor of 5 smaller than DESI's observed value (−0.75), the
   same under-prediction Part 25 already noted for constant coupling.

So T3 **does not** rescue the dark energy transition from being a free-parameter
puzzle. It clarifies the structural relationship between the Part 99 critical point
and Part 25 drift, but it does not produce a new redshift scale.

This is a negative/partial result — still useful, because it pins down exactly what
is and is not predicted by the pendulum picture alone.

---

## 2. Setup and Notation

### 2.1 The PDTP pendulum (Part 99)

From the U(1) Lagrangian field equations:

```
box(phi) = g sin(psi - phi)           (A)
box(psi) = -g sin(psi - phi)          (B)
```

Subtracting (A) from (B) for a homogeneous mode Δ(t) = ψ(t) − φ(t):

```
d²Δ/dt² = -2g sin(Δ)                   [Eq 99.1, DERIVED]
```

This is a simple pendulum equation with effective potential (choosing V(0) = 0 as
baseline):

```
V(Δ) = 2g (1 − cos Δ)                   [positive definite]
```

Special values:

| Δ | physical state | V/(2g) | α = cos Δ |
|---|----------------|--------|-----------|
| 0 | fully coupled (gravity normal) | 0 | 1 |
| π/4 | force-coupling crossover (**sizzling onset**) | 1 − 1/√2 ≈ 0.293 | 1/√2 |
| π/2 | fully decoupled (gravity off) | 1 | 0 |
| π | anti-coupled (unstable maximum) | 2 | −1 |

The Part 99 result: Δ = π/4 is **not a fixed point** of the dynamics. It is a
diagnostic threshold where the sine-force equals the cosine-coupling (Eq 99.3).

### 2.2 Adding cosmological friction

In an FRW background H(t) = ȧ/a, a homogeneous mode of a scalar field picks up
Hubble friction (standard result):

```
d²Δ/dt² + 3H (dΔ/dt) + 2g sin(Δ) = 0     [Eq 102.0, PDTP Original]
```

This is the full-pendulum generalisation of the Part 25 Langevin equation
(Eq 2.6), which used the linearised potential V ≈ ½ g_eff Δ².

---

## 3. Slow-Roll ε for the Full Pendulum

### 3.1 Derivation step by step

**Slow-roll condition:** Hubble friction dominates over inertia,
|Δ̈| ≪ |3H Δ̇|. Dropping Δ̈:

```
3H (dΔ/dt) = -2g sin(Δ)
=>  dΔ/dt = -(2g / (3H)) sin(Δ)            [Eq 102.A]
```

**Kinetic energy density** (per oscillator, normalised):

```
K = ½ (dΔ/dt)²
  = ½ × (2g/(3H))² × sin²(Δ)
  = 2 g² sin²(Δ) / (9 H²)
```

**Potential energy density:**

```
V = 2g (1 − cos Δ)
```

**Ratio ε ≡ K/V:**

```
ε = [2 g² sin²Δ / (9 H²)] / [2g (1 − cos Δ)]
  = g sin²Δ / [9 H² (1 − cos Δ)]
```

Use the identity sin²Δ = 1 − cos²Δ = (1 − cos Δ)(1 + cos Δ):

```
ε(Δ, H) = g (1 + cos Δ) / (9 H²)           [Eq 102.1, PDTP Original]
```

**Harmonic limit (Δ → 0):**

```
cos Δ → 1
=>  ε → 2g / (9 H²)
```

Identifying with Part 25 Eq 3.3 (ε = g_eff/(9H²)):

```
g_eff = 2g                                  [Eq 102.2, DERIVED]
```

This is **internally consistent** with Part 99 (where the factor 2 appears from
adding Eq A and Eq B) and with Part 25 (where g_eff is defined as the coefficient
of the quadratic potential in δφ).

### 3.2 Equation of state

Using Part 25 Eq 4.1:

```
w(Δ, H) = (ε − 1) / (ε + 1)                 [Eq 102.6, via Part 25]
```

Because ε depends on cos Δ, the full pendulum gives a Δ-dependent equation of
state, whereas Part 25's harmonic limit gives w only as a function of the scalar
field amplitude.

---

## 4. Δ_0 Inference from DESI DR2

### 4.1 Inversion from w_0

Part 25 Eq 5.1 inverts w(ε) = (ε − 1)/(ε + 1):

```
ε_0 = (1 + w_0) / (1 − w_0)
```

For DESI DR2 best-fit **w_0 = −0.827**:

```
ε_0 = (1 − 0.827)/(1 + 0.827) = 0.173 / 1.827 ≈ 0.0947       [Eq 102.7]
```

### 4.2 Two unknowns, one equation

From Eq 102.1:

```
ε_0 = g (1 + cos Δ_0) / (9 H_0²)
=> g / H_0² = 9 ε_0 / (1 + cos Δ_0)
```

This is one equation in two unknowns (g, Δ_0). We need an extra assumption.

**Case A** (hypothesis): assume Δ_0 = π/4 **exactly**, i.e. the universe is
*at* the sizzling crossover today.

```
g / H_0² = 9 × 0.0947 / (1 + 1/√2) ≈ 0.499
=> g ≈ 0.499 × H_0²  ≈  2.4 × 10⁻³⁶ s⁻²
=> g_eff = 2g  ≈  4.8 × 10⁻³⁶ s⁻²
```

Compare to Part 25 Eq 5.3 (**independent inference** from the same DESI data):

```
g_eff (Part 25)  ≈  4.4 × 10⁻³⁶ s⁻²
```

**Within 10%.** The Case-A assumption is therefore numerically self-consistent.

**Case B:** Use Part 25's independent g_eff = 4.4 × 10⁻³⁶ s⁻² (so g = 2.2 × 10⁻³⁶).
Then solve for Δ_0:

```
(1 + cos Δ_0) = 9 ε_0 H_0² / g  ≈  1.906
=> cos Δ_0 = 0.906
=> Δ_0 ≈ 0.438 rad ≈ 25.1°
```

**Δ_0 ≈ 25° in Case B**, which is **not** π/4 = 45°. Instead, the universe would
be well inside the "coupled" regime, nowhere near the sizzling onset.

**Interpretation:** Case A and Case B disagree by a factor of ~1.8 in Δ_0.
The disagreement comes from the 10% numerical slack in g_eff, which gets
amplified by the nonlinearity. Neither case is ruled out by T3 alone.

---

## 5. Slow-Roll Attractor Direction: A Critical Negative

### 5.1 The sign problem

From Eq 102.A:

```
dΔ/dt = -(2g / (3H)) sin(Δ)
```

For Δ ∈ (0, π) we have sin Δ > 0, so dΔ/dt < 0. That means:

> **Δ is DECREASING over time.** The pendulum is relaxing toward Δ = 0.

**Physical picture:** the Hubble-friction-damped pendulum cannot tension itself
up. It only unwinds. If Δ_initial ≈ π (near the unstable maximum), the system
rolls down to Δ_today < Δ_initial. If Δ_initial ≈ 0 (already coupled), Δ stays ≈ 0.

### 5.2 Why this contradicts naive intuition

A naive picture ("dark energy is growing drift") would require
Δ_today > Δ_past, i.e. dΔ/dt > 0. The slow-roll attractor **directly
contradicts** this.

### 5.3 How dark energy can still grow as a fraction

Observation says Ω_DE grows with time while Ω_m decreases. This is compatible
with V(Δ) **shrinking** in absolute terms, provided it shrinks slower than matter
dilutes. In LCDM:

```
ρ_m(a)  ~ a^(-3)        (matter dilutes)
ρ_DE(a) ~ ~const        (V nearly frozen)
```

Even if ρ_DE is *slowly decreasing* (because Δ is slowly relaxing), the matter
term drops much faster, so Ω_DE = ρ_DE / ρ_total still grows. This is the
standard "slow-roll quintessence" behaviour.

**The PDTP pendulum reproduces this automatically** — so the negative sign is
not fatal to the dark energy story. But it rules out the picture of "rising
drift" which was the original T3 hypothesis.

### 5.4 w(z) table (Case A)

Under Case A, assuming Δ stays near π/4 (slow relaxation) and H(z) follows LCDM:

| z | H(z)/H_0 | ε(z) | w(z) |
|---|----------|------|------|
| 0.00 | 1.0000 | 9.47 × 10⁻² | −0.827 |
| 0.20 | 1.0923 | 7.94 × 10⁻² | −0.853 |
| 0.50 | 1.2543 | 6.02 × 10⁻² | −0.886 |
| 0.70 | 1.3743 | 5.01 × 10⁻² | −0.905 |
| 1.00 | 1.5708 | 3.84 × 10⁻² | −0.926 |
| 1.50 | 1.9299 | 2.54 × 10⁻² | −0.950 |
| 2.00 | 2.3130 | 1.77 × 10⁻² | −0.965 |

w(z) drops smoothly from −0.827 today toward −1 at high z (the "thawing
quintessence" freeze). No sharp transition appears near z ≈ 0.5 — this is a
standard smooth quintessence behaviour.

---

## 6. w_a Prediction and DESI Tension

### 6.1 Derivation of w_a (Case A, constant g)

Start from w(ε) = (ε − 1)/(ε + 1), with ε(z) = ε_0 × (H_0/H(z))². Expanding
near z = 0 to first order and identifying with CPL w(z) ≈ w_0 + w_a z/(1+z):

**Step 1:** LCDM Hubble evolution:

```
H(z)² = H_0² × [Ω_m (1+z)³ + Ω_DE]
d(H²)/dz |_{z=0} = 3 H_0² Ω_m
=> d(1/H²)/dz |_{z=0} = -3 Ω_m / H_0²      [standard result]
```

**Step 2:** Derivative of ε:

```
ε(z) = ε_0 × H_0² / H(z)²
dε/dz |_{z=0} = ε_0 × H_0² × [d(1/H²)/dz]_{z=0}
              = ε_0 × H_0² × (-3 Ω_m / H_0²)
              = -3 ε_0 Ω_m
```

**Step 3:** Chain rule for w:

```
dw/dε = 2 / (ε + 1)²
(dw/dz)_0 = (dw/dε)_0 × (dε/dz)_0
          = [2/(ε_0+1)²] × [-3 ε_0 Ω_m]
          = -6 ε_0 Ω_m / (ε_0 + 1)²
```

**Step 4:** CPL expansion:

```
w_CPL(z) = w_0 + w_a × z/(1+z)
d/dz [z/(1+z)]_{z=0} = 1
=> w_a = (dw/dz)_0
```

**Result [Eq 102.5, PDTP Original T3]:**

```
┌────────────────────────────────────────────────┐
│                                                │
│   w_a = -6 ε_0 Ω_m / (ε_0 + 1)²                │
│                                                │
└────────────────────────────────────────────────┘
```

### 6.2 Numerical value

```
ε_0 = 0.0947
Ω_m = 0.315
w_a = -6 × 0.0947 × 0.315 / (1.0947)² ≈ -0.149
```

### 6.3 Equivalence to Part 25 (m = 0)

Algebraic identity (SymPy verified):

```
(1 − w_0²) / 2 = 2 ε_0 / (ε_0 + 1)²
```

Therefore:

```
w_a (Part 25, m=0) = -(1 − w_0²)/2 × 3 Ω_m
                   = -[4 ε_0 /(ε_0+1)²] × (3/2) × Ω_m
                   = -6 ε_0 Ω_m /(ε_0+1)²
                   = w_a (T3, Case A)
```

**Conclusion:** T3 (Case A) is algebraically identical to Part 25 with m = 0.
No new prediction from T3 alone.

### 6.4 DESI tension

| Model | w_a (predicted) | w_a (DESI DR2) | Deviation |
|-------|-----------------|----------------|-----------|
| Part 25 m=0 / T3 Case A | −0.149 | −0.75 ± 0.29 | **5×** too small |
| Part 25 m=3 (a³ coupling) | −0.621 | −0.75 ± 0.29 | 0.4σ |

**T3 does not resolve the w_a tension.** A time-varying coupling (m ≳ 3, as
Part 25 noted) is still required to match DESI DR2. T3 adds **zero extra
predictive power** over the Part 25 m = 0 scenario — it just re-derives the
same result from the full-pendulum potential.

---

## 7. The f_c ≈ Ω_m Coincidence

### 7.1 The numeric match

From the potential:

```
V(Δ)/V(π/2) = 1 − cos Δ                    [Eq 102.3]
V(π/4)/V(π/2) = 1 − 1/√2 ≈ 0.2929          [Eq 102.4]
```

Today's matter density (Planck 2018): Ω_m,0 ≈ 0.315.

```
f_c / Ω_m,0 = 0.293 / 0.315 ≈ 0.930
```

**Within 7%.**

### 7.2 [SPECULATIVE] What it could mean

*If* this coincidence is not accidental, it would say:

> The universe sits at the Part 99 sizzling crossover (Δ_0 = π/4) **today**,
> and the 29.3% "potential energy fraction" is numerically tied to the
> matter density fraction by a relation we have not yet derived.

Such a relation would need to identify V(Δ)/V_max (a per-cell energy ratio)
with Ω_m (a global density ratio). These are **structurally different
quantities** — there is no a priori reason they should coincide.

### 7.3 What it probably means

A 7% match over a single free parameter is suggestive but nowhere near
conclusive. Candidate explanations:

1. **Coincidence.** Given the range of plausible "round numbers" 1 − 1/√2,
   1/3, 1/e etc., at least one will land within 10% of Ω_m by chance.
2. **Anthropic selection.** We observe the universe in the era where matter
   and dark energy are comparable; a pendulum sitting near Δ ≈ π/4 may be
   a natural "diagnostic epoch" condition rather than a derivation.
3. **Hidden derivation.** An extension of PDTP not yet known could fix
   Ω_m = 1 − 1/√2 exactly. No candidate mechanism is presently identified.

**Honest assessment:** tag as [SPECULATIVE]. Report the numerical match but
do not cite it as a derivation.

---

## 8. Transition Redshift: Why T3 Gives None

### 8.1 The LCDM crossing

In LCDM, matter and dark energy cross at:

```
Ω_m (1+z)³ = Ω_DE
(1+z)³ = 0.685 / 0.315 = 2.175
z_eq = 2.175^{1/3} − 1 ≈ 0.297
```

This matches the DESI z ≈ 0.45-0.7 transition to within the w_a spread.

### 8.2 No separate PDTP scale

Under Case A with constant g, the PDTP model gives:

```
ε(z) = ε_0 × [H_0 / H(z)]²
```

The only z-scale in this expression comes from H(z), which is already in LCDM.
There is no separate PDTP z-scale where the Δ = π/4 crossover "activates".

**Reason:** Δ = π/4 is a **phase-space threshold**, not a **redshift threshold**.
The system can linger near Δ = π/4 for arbitrary cosmological durations because
the potential is smooth and there is no bifurcation.

**Conclusion:** the DESI z_transition ≈ 0.5 is **not a PDTP prediction**. It is
inherited from LCDM and from the choice of Ω_m. T3 adds no new time-scale.

---

## 9. SymPy Verification (6/6 residuals = 0)

| Equation | Statement | Residual |
|----------|-----------|----------|
| 102.1 | ε = g(1 + cos Δ)/(9H²) from K/V | 0 |
| 102.2 | ε(Δ → 0) = 2g/(9H²) (harmonic limit) | 0 |
| 102.3 | V(Δ)/V(π/2) = 1 − cos Δ | 0 |
| 102.4 | V(π/4)/V(π/2) = 1 − 1/√2 | 0 |
| 102.5 | w_a = −6 ε Ω_m /(ε+1)² | 0 |
| identity | (1 − w_0²)/2 = 2ε/(ε+1)² | 0 |

All six checks in `verify_sympy()` return residual = 0 from SymPy.simplify.

---

## 10. Sudoku Consistency — 10/10 PASS

| # | Test | Value | Status |
|---|------|-------|--------|
| S1 | ε(Δ=0) = 2g/(9H²) | 0.2222 | PASS |
| S2 | ε(π/4) = g(1+1/√2)/(9H²) | 0.1897 | PASS |
| S3 | V(π/4)/V(π/2) = 1 − 1/√2 | 0.2929 | PASS |
| S4 | f_c = 1 − 1/√2 [Eq 102.4] | 0.2929 | PASS |
| S5 | ε_0 = (1+w_0)/(1−w_0) [Part 25 Eq 5.1] | 0.0947 | PASS |
| S6 | w(ε=0) = −1 [Λ limit] | −1.0000 | PASS |
| S7 | w(ε_0) round trip = w_0 | −0.827 | PASS |
| S8 | g/H_0² [Case A] = 9ε_0/(1+1/√2) | 0.4993 | PASS |
| S9 | w_a(T3) = w_a(Part 25, m=0) | −0.1494 | PASS |
| S10 | V(Δ)/V_max monotonic on (0, π/2) | 1 | PASS |

Sudoku score: **10 / 10 PASS.**

---

## 11. Key Equations Summary

```
┌────────────────────────────────────────────────────────────────────┐
│                                                                    │
│  Part 102 -- T3: Loss Tangent and Dark Energy Crossover           │
│                                                                    │
│  [Eq 102.0]  ddot(Delta) + 3H dot(Delta) = -2g sin(Delta)         │
│                                                          [DERIVED] │
│                                                                    │
│  [Eq 102.1]  eps(Delta, H) = g(1 + cos Delta) / (9 H^2)           │
│                                                   [PDTP Original] │
│                                                                    │
│  [Eq 102.2]  g_eff = 2g  (harmonic limit matches Part 25)         │
│                                                          [DERIVED] │
│                                                                    │
│  [Eq 102.3]  V(Delta) / V(pi/2) = 1 - cos Delta                   │
│                                                          [DERIVED] │
│                                                                    │
│  [Eq 102.4]  f_c = V(pi/4) / V(pi/2) = 1 - 1/sqrt(2) ~ 0.293      │
│                                                          [DERIVED] │
│                                                                    │
│  [Eq 102.5]  w_a = -6 eps_0 Omega_m / (eps_0 + 1)^2               │
│                                                   [PDTP Original] │
│              (identical to Part 25 m=0 by algebraic identity)     │
│                                                                    │
│  [Eq 102.6]  w(Delta, H) = (eps - 1)/(eps + 1)  [via Part 25]     │
│                                                                    │
│  [Eq 102.7]  eps_0 = 0.0947 from DESI w_0 = -0.827                │
│                                                   [OBSERVATIONAL] │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

---

## 12. Verdict and Open Questions

### 12.1 Verdict: **PARTIAL**

- **Structural mapping:** ✓ The full pendulum generalises Part 25 cleanly.
- **Numerical consistency:** ✓ Case-A g matches Part 25 g_eff to within 10%.
- **Numerical coincidence:** ≈ f_c ≈ Ω_m,0 within 7%, [SPECULATIVE] only.
- **DESI w_a match:** ✗ Factor 5 too small — same as Part 25 m=0.
- **z-scale prediction:** ✗ PDTP gives no new transition redshift.
- **Attractor direction:** ✗ Naive "growing drift" picture is wrong.

### 12.2 What T3 resolves

- The relationship between Part 99 (phase-space crossover) and Part 25
  (harmonic slow-roll): T3 shows they are the same physics in different
  limits, with g_eff = 2g exactly.
- The observation that the crossover Δ = π/4 is diagnostic, not dynamical.

### 12.3 What T3 does NOT resolve

- The DESI w_a tension (still requires Part 25 m = 3 or similar).
- Why Ω_m ≈ 30% (the f_c coincidence is not a derivation).
- The cosmological initial condition for Δ (why not Δ = 0 from the start?).
- Whether the Part 99 "sizzling onset" is accidentally where the universe
  is today, or there is a selection principle.

### 12.4 Connection to other open problems

- **T2 (Part 99):** T3 confirms Δ = π/4 is a threshold, not a bifurcation.
  Consistent with the Part 99 verdict.
- **Part 25 / m parameter:** T3 re-derives the m = 0 w_a formula from the
  full pendulum. It does NOT tell us why m should be 3. That remains open.
- **Part 54 (Λ problem):** Λ is still a free parameter; T3 does not remove
  the free-parameter status of the condensate energy scale.
- **T5 (condensate layers):** The factor g_eff = 2g here is a single-layer
  result. If multiple layers (C1 gravitational, C2 QCD) contribute, the
  effective g_eff may be a sum — which could change the w_a tension.
  Worth exploring under T5.

### 12.5 Falsifiability

- **If** DESI DR3 confirms w_0 = −0.827 and w_a = −0.75, the constant-g PDTP
  model is **ruled out** (factor-5 discrepancy in w_a).
- **If** DESI DR3 revises w_a toward −0.15, T3 Case A is **consistent**.
- **If** future measurements pin down Ω_m to 4 decimal places, the f_c ≈ Ω_m
  coincidence can be tested for improved/worsened agreement. A deviation
  > 5% would falsify any proposed derivation.

---

## 13. References

- **Part 99:** `tan_critical_point.md` — The tan(Δ) = 1 critical point
- **Part 25:** `wz_dark_energy_pdtp.md` — w(z) from phase drift
- **Part 19:** `phase_drift_mechanism.md` — Langevin equation for drift
- **Part 54:** `cosmological_constant_fcc.md` — Λ as a free parameter
- **Planck 2018:** [arXiv:1807.06209](https://arxiv.org/abs/1807.06209) —
  Ω_m = 0.315 ± 0.007
- **CPL:** Chevallier & Polarski (2001), Linder (2003) — w(z) = w_0 + w_a z/(1+z)
- **DESI DR2:** Adame et al. (2024) — w_0 = −0.827, w_a = −0.75
- **Equation of state (cosmology):**
  [Wikipedia](https://en.wikipedia.org/wiki/Equation_of_state_(cosmology))
- **Slow-roll approximation:**
  [Wikipedia](https://en.wikipedia.org/wiki/Slow-roll_approximation)

---

## 14. Script and Output

- **Script:** [simulations/solver/t3_loss_tangent.py](../../simulations/solver/t3_loss_tangent.py)
- **Output:** `simulations/solver/outputs/t3_loss_tangent_*.txt`
- **Runner:** `python simulations/solver/t3_loss_tangent.py` (standalone)
  or via `main.py` Phase 70.
