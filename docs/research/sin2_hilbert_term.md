# Hilbert Space sin^2 Term — Second Fourier Harmonic (Part 104, T23)

**Status:** PRODUCTIVE — new physics, new prediction, w_a NOT resolved
**Date:** 2026-04-12
**Script:** `simulations/solver/t23_sin2_term.py` (Phase 72)
**Prerequisites:**
- [tan_critical_point.md](tan_critical_point.md) — Part 99: Delta = pi/4 crossover
- [loss_tangent_dark_energy.md](loss_tangent_dark_energy.md) — Part 102: w_a = -0.149 (factor 5 too small)
- Part 61: two-phase Lagrangian (+cos/-cos)
- Part 28b: alpha = cos(Delta) = Re<psi|phi> (polarization analogy)

---

## 1. Plain English Summary

The PDTP Lagrangian currently uses `g cos(psi - phi)` as the coupling between
matter and the spacetime condensate. This is like two pendulums connected by
a spring — they prefer to swing in sync (Delta = 0).

This investigation asks: **is there a second spring?** Specifically, could there
be a `lambda sin^2(psi - phi)` term that we've been missing?

**What we found:**

1. **It's allowed.** The sin^2 term is the second Fourier harmonic of the
   coupling potential. All PDTP symmetries (U(1) shift, parity, periodicity)
   permit it. Nothing forbids it.

2. **It creates a phase transition.** If lambda exceeds g/2, the stable
   equilibrium shifts from Delta = 0 (perfect alignment) to a nonzero
   Delta* = arccos(g/(2*lambda)). This is permanent partial decoupling —
   matter and the condensate can never fully align.

3. **It does NOT fix the dark energy problem.** The w_a prediction stays
   far from the DESI value (-0.75). The best the sin^2 term achieves is
   w_a ~ -0.075, still a factor of 10 short. The slow-roll mechanism is
   the bottleneck, not the potential shape.

4. **It arises naturally from the two-phase system.** In the two-phase
   Lagrangian (Part 61), integrating out phi_- fluctuations at 1-loop
   generates exactly this kind of second-harmonic correction.

5. **New prediction:** If the sin^2 term exists with lambda >= g/2, then
   gravitational coupling is permanently reduced: alpha* = g/(2*lambda) < 1.
   This is testable with lunar laser ranging (precision dG/G < 10^-13/yr).

**Bottom line:** The sin^2 term is real physics (allowed, natural, generates
a phase transition) but it doesn't solve the outstanding problems (w_a, G
derivation). It goes on the shelf as a known allowed extension, not an
urgent addition.

---

## 2. The Question

PDTP's coupling potential is V(Delta) = g cos(Delta). But is this the
*complete* potential, or just the leading term of a Fourier series?

The most general coupling consistent with:
- U(1) shift symmetry (phi -> phi+c, psi -> psi+c simultaneously)
- Parity (Delta -> -Delta)
- 2*pi periodicity

is a **Fourier cosine series**:

```
V(Delta) = a_0 + a_1 cos(Delta) + a_2 cos(2*Delta) + a_3 cos(3*Delta) + ...
                                                                     [Eq 104.6, DERIVED]
```

Parity kills all sin(n*Delta) terms. The constant a_0 doesn't affect physics.
Current PDTP has only a_1 = g. The sin^2 term sets a_2 = -lambda/2:

```
lambda sin^2(Delta) = lambda(1 - cos(2*Delta))/2 = lambda/2 - (lambda/2) cos(2*Delta)
```

This is the **second Fourier harmonic** of the coupling.

---

## 3. Extended Lagrangian

### 3.1 The Lagrangian

```
L_ext = (1/2)(d_mu phi)^2 + (1/2)(d_mu psi)^2
        + g cos(psi - phi) + lambda sin^2(psi - phi)
                                                          [PDTP Original + extension]
```

### 3.2 Field Equations

**Starting point:** Euler-Lagrange for phi and psi from L_ext.

**Step 1:** Define Delta = psi - phi. The coupling depends only on Delta.

**Step 2:** Compute d(V_c)/d(phi) where V_c = g cos(Delta) + lambda sin^2(Delta).

Using the chain rule (d(Delta)/d(phi) = -1):

```
d(V_c)/d(phi) = [dV_c/dDelta] * (-1)
dV_c/dDelta = -g sin(Delta) + lambda * 2 sin(Delta) cos(Delta)
            = -g sin(Delta) + lambda sin(2*Delta)
```

Therefore:

```
d(V_c)/d(phi) = g sin(Delta) - lambda sin(2*Delta)
```

Similarly (d(Delta)/d(psi) = +1):

```
d(V_c)/d(psi) = -g sin(Delta) + lambda sin(2*Delta)
```

**Eq 104.2 [PDTP Original, DERIVED, SymPy VERIFIED]:**

```
Box(phi) = g sin(Delta) - lambda sin(2*Delta)
Box(psi) = -g sin(Delta) + lambda sin(2*Delta)
```

**Step 3:** Momentum conservation check:

```
Box(phi) + Box(psi) = [g sin(D) - lam sin(2D)] + [-g sin(D) + lam sin(2D)] = 0
```

Exact for all lambda. This follows from Noether's theorem: V_c depends only on
Delta = psi - phi, so the simultaneous shift phi -> phi+c, psi -> psi+c is a
symmetry. The conserved current d^mu(phi + psi) has zero divergence.

**Step 4:** Delta equation of motion:

```
Box(Delta) = Box(psi) - Box(phi) = -2g sin(D) + 2 lambda sin(2D)
           = -2 sin(D) [g - 2 lambda cos(D)]
```

### 3.3 Effective Potential

**Step 5:** For homogeneous mode: ddot(D) = -dV_eff/dD.

Integrating dV_eff/dD = 2g sin(D) - 4 lambda sin(D) cos(D):

**Eq 104.1 [PDTP Original, DERIVED, SymPy VERIFIED]:**

```
V_eff(Delta) = -2g cos(Delta) + 2 lambda cos^2(Delta) + const
```

Positive-definite form (V_eff(0) = 0):

```
V_eff(Delta) = 2g(1 - cos Delta) - 2 lambda sin^2(Delta)
             = (1 - cos Delta) [2g - 2 lambda (1 + cos Delta)]
```

**Recovery (lambda = 0):** V_eff -> 2g(1 - cos D). This is exactly Part 99's
pendulum potential. CHECK.

---

## 4. Stability Analysis

### 4.1 Fixed Points

Setting dV_eff/dD = 2 sin(D) [g - 2 lambda cos(D)] = 0:

**(a)** sin(D) = 0 -> D = 0 or D = pi (same as standard PDTP)

**(b)** cos(D*) = g/(2*lambda) -> **new fixed point** if lambda >= g/2.

**Eq 104.4 [PDTP Original, DERIVED, SymPy VERIFIED]:**

```
D* = arccos(g / (2*lambda))     [exists when lambda >= g/2]
```

### 4.2 Stability at D = 0

Linearizing: ddot(D) ~ -(2g - 4*lambda) D, so:

**Eq 104.3 [PDTP Original, DERIVED, SymPy VERIFIED]:**

```
omega^2(D=0) = 2g - 4*lambda
```

- lambda < g/2: omega^2 > 0 -> D=0 STABLE (standard PDTP)
- lambda = g/2: omega^2 = 0 -> CRITICAL POINT
- lambda > g/2: omega^2 < 0 -> D=0 UNSTABLE

### 4.3 Phase Diagram

This is a **pitchfork bifurcation** (Z_2 symmetric, since D and -D are equivalent):

| lambda/g | Ground state | alpha* = cos(D*) | Physics |
|----------|-------------|-------------------|---------|
| 0.00 | D = 0 | 1.000 | Standard PDTP |
| 0.25 | D = 0 | 1.000 | Weakened oscillation |
| 0.50 | D = 0 (marginal) | 1.000 | Critical point |
| 0.75 | D = 48.2 deg | 0.667 | Partial decoupling |
| 1.00 | D = 60.0 deg | 0.500 | Half decoupled |
| 2.00 | D = 75.5 deg | 0.250 | Mostly decoupled |

**Special case:** D* = pi/4 (Part 99 crossover) occurs at lambda/g = sqrt(2)/2 = 0.707.

### 4.4 Plain English

Think of it this way: the cos(Delta) coupling is like gravity pulling two
objects together (aligned). The sin^2(Delta) coupling is like a magnetic
repulsion that pushes them apart (misaligned). When the repulsion is weak
(lambda < g/2), gravity wins and everything stays aligned. When repulsion
exceeds gravity (lambda > g/2), the system settles at a compromise angle
where the two forces balance. This is the "permanent partial decoupling."

---

## 5. Slow-Roll w_a Analysis

### 5.1 Extended Epsilon

Adding Hubble friction:

```
3H dot(D) = -[2g - 4*lambda*cos(D)] sin(D)     [slow-roll]
```

Following the same derivation as Part 102 (kinetic/potential ratio):

**Eq 104.5 [PDTP Original, DERIVED]:**

```
epsilon(D, r) = (g/(9*H^2)) * (1-2r cos D)^2 * (1+cos D) / (1 - r(1+cos D))
```

where r = lambda/g.

**Recovery (r = 0):** epsilon = g(1+cos D)/(9 H^2). Part 102 Eq 102.1 exactly. CHECK.

### 5.2 Result: w_a CANNOT Reach DESI

A 2D scan over r in [0, 0.49] and D_0 in [5, 85] degrees, fixing
epsilon_0 = 0.0947 (DESI w_0 = -0.827), found:

```
Best w_a = -0.075 at lambda/g = 0.00, D_0 = 85 deg
DESI target: w_a = -0.75
Gap: 0.675 (factor ~10 off)
```

The sin^2 term CANNOT resolve the w_a tension. The slow-roll approximation
itself is the bottleneck: the kinetic-to-potential ratio epsilon is too small
to generate a large w_a regardless of the potential shape.

This confirms Part 102's finding: w_a ~ -0.75 requires a non-slow-roll
mechanism (e.g., Part 25's phenomenological m = 3 parameter for g_eff(a)).

---

## 6. Physical Interpretation

### 6.1 Hilbert Space Inner Product

From Part 28b, the phase difference Delta defines a Hilbert-space-like
inner product:

```
<psi|phi> = e^{i*Delta} = cos(Delta) + i sin(Delta)
```

- **cos(Delta) = Re<psi|phi>** — the gravitational coupling (how aligned)
- **sin^2(Delta) = |Im<psi|phi>|^2** — the cross-polarization intensity

The existing g cos(Delta) uses the real part. The new lambda sin^2(Delta)
uses the squared imaginary part.

### 6.2 Optics Analogy

- cos(Delta) = Malus's law (same polarizer: transmitted intensity ~ cos^2)
- sin^2(Delta) = crossed-polarizer transmission (how much "leaks through"
  when the polarizers are misaligned)

### 6.3 Sign Meaning

- lambda > 0: rewards misalignment (decoupling force)
- lambda < 0: penalizes misalignment (extra binding beyond gravity)

---

## 7. Two-Phase Extension

### 7.1 Extended Two-Phase Lagrangian

Using Option A (sin^2 follows the same sign pattern as cos):

```
L_ext = g[cos(D_b) - cos(D_s)] + lambda[sin^2(D_b) - sin^2(D_s)]
```

### 7.2 In phi_+/phi_- Variables

Using Sigma = psi - phi_+ and the Part 61 change of variables:

```
cos(D_b) - cos(D_s) = 2 sin(Sigma) sin(phi_-)            [Part 61]
sin^2(D_b) - sin^2(D_s) = -sin(2*Sigma) sin(2*phi_-)     [SymPy VERIFIED]
```

Therefore:

```
L_ext = 2g sin(Sigma) sin(phi_-) - lambda sin(2*Sigma) sin(2*phi_-)
```

The lambda term has **double frequency** in both Sigma and phi_-.
When phi_- = 0 (vacuum): both terms vanish. No vacuum contribution.

---

## 8. SymPy Verification

| # | Check | Result |
|---|-------|--------|
| S1 | Box(phi) = g sin(D) - lambda sin(2D) | PASS (residual = 0) |
| S2 | Box(psi) = -g sin(D) + lambda sin(2D) | PASS (residual = 0) |
| S3 | Box(phi) + Box(psi) = 0 (momentum) | PASS (sum = 0) |
| S4 | V_eff = -2g cos(D) + 2 lambda cos^2(D) | PASS (residual = 0) |
| S5 | omega^2(D=0) = 2g - 4*lambda | PASS (residual = 0) |
| S6 | cos(D*) = g/(2*lambda) | PASS |
| S7 | sin^2(D) = (1-cos(2D))/2 | PASS |
| S8 | V_eff(lambda=0) = -2g cos(D) | PASS |
| S9 | sin^2(S-p) - sin^2(S+p) = -sin(2S)sin(2p) | PASS (residual = 0) |

**SymPy: 9/9 PASS**

---

## 9. Sudoku Consistency Check

| # | Test | Ratio | Result |
|---|------|-------|--------|
| S1 | omega^2(lam=0) = 2g [Part 99] | 1.000000 | PASS |
| S2 | eps(D=0, lam=0) = 2g/(9H^2) [Part 102] | 1.000000 | PASS |
| S3 | Momentum conservation = 0 [Noether] | 0.000000 | PASS |
| S4 | omega^2(lam=g/2) = 0 [pitchfork] | 0.000000 | PASS |
| S5 | D*(lam=g) = 60 deg | 1.000000 | PASS |
| S6 | V(D*) < 0 when lam > g/2 [lower energy] | 1.000000 | PASS |
| S7 | V_eff(-D) = V_eff(D) [parity] | 1.000000 | PASS |
| S8 | V_eff(D+2pi) = V_eff(D) [periodicity] | 1.000000 | PASS |
| S9 | cos(Db)-cos(Ds) = 2 sin(S) sin(p) [Part 61] | 1.000000 | PASS |
| S10 | sin^2(Db)-sin^2(Ds) = -sin(2S)sin(2p) | 1.000000 | PASS |

**Sudoku: 10/10 PASS**

---

## 10. Equations Summary

| Eq # | Equation | Tag |
|------|----------|-----|
| 104.1 | V_eff(D) = -2g cos(D) + 2 lambda cos^2(D) | [PDTP Original, DERIVED, SymPy VERIFIED] |
| 104.2 | Box(phi) = g sin(D) - lambda sin(2D); Box(psi) = -g sin(D) + lambda sin(2D) | [PDTP Original, DERIVED, SymPy VERIFIED] |
| 104.3 | omega^2(D=0) = 2g - 4*lambda | [PDTP Original, DERIVED, SymPy VERIFIED] |
| 104.4 | D* = arccos(g/(2*lambda)), exists when lambda >= g/2 | [PDTP Original, DERIVED, SymPy VERIFIED] |
| 104.5 | epsilon = (g/(9H^2)) (1-2r cos D)^2 (1+cos D) / (1-r(1+cos D)), r = lambda/g | [PDTP Original, DERIVED] |
| 104.6 | V(Delta) = sum_n a_n cos(n*Delta) [most general parity-even U(1)-invariant coupling] | [DERIVED] |

---

## 11. Verdict

**PRODUCTIVE** — but not a breakthrough.

**What T23 delivers:**
1. A clean Fourier analysis of the PDTP coupling potential [Eq 104.6]
2. A new allowed term with exact field equations [Eq 104.2]
3. A **pitchfork phase transition** at lambda = g/2 [Eq 104.3-104.4]
4. A new prediction: permanent partial decoupling if lambda >= g/2
5. A physical interpretation: sin^2 = cross-polarization = |Im<psi|phi>|^2
6. A natural origin: phi_- fluctuations in the two-phase system

**What T23 does NOT deliver:**
1. No resolution of w_a tension (slow-roll is the bottleneck, not V shape)
2. No new constraint on m_cond or G
3. No determination of lambda (it's a new free parameter unless derived from
   phi_- variance, which requires UV cutoff)
4. No lensing fix (the gamma = 0 gap from Part 100/103 is unrelated to V shape)

**Recommendation:**
- Record sin^2 as a known allowed extension [DERIVED, SymPy VERIFIED]
- Do NOT add it to the core Lagrangian until lambda is determined or
  an observation requires it
- The pitchfork bifurcation is the most interesting result — it connects
  to Goal 2 (phase decoupling) as a MECHANISM for sustained decoupling
- Proceed to T22 (Platonic solids) or revisit w_a via non-slow-roll dynamics

---

## 12. References

1. Part 28b — alpha = cos(Delta) = Re<psi|phi> (polarization analogy)
2. Part 99 — Delta = pi/4 crossover; V(D) = 2g(1-cos D)
3. Part 102 — Loss tangent; w_a = -0.149 (factor 5 too small)
4. Part 61 — Two-phase Lagrangian; product coupling; 16/16 tests
5. Part 25 — Slow-roll w(z); epsilon = g_eff/(9H^2)
6. Weinberg (1972) "Gravitation and Cosmology" — Fourier potential analysis
7. Part 63 — Two-phase re-derivation; chi = phi_+ + pi/2 mapping
