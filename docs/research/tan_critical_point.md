# Part 99 — T2: Critical Point at tan(Δ) = 1

**Part:** 99
**Phase:** 67
**Date:** 2026-04-06
**Script:** `simulations/solver/tan_critical_point.py`
**Status:** DONE — 10/10 Sudoku PASS

---

## Plain English Summary

The PDTP framework couples matter-waves (ψ) to spacetime-waves (φ) via
cos(ψ−φ). The angle Δ = ψ−φ measures how far out of phase they are.
When Δ=0 they are perfectly in phase — full gravity. When Δ=90° they are
fully decoupled — zero gravity (the Leidenfrost state).

**Is there anything special at Δ=45°?**

Yes, but not a phase transition. At Δ=45° the *decoupling force* (which
drives Δ away from 0) exactly equals the *restoring coupling* (which
pulls Δ back to 0). Below 45° the coupling wins and the system snaps back
to gravity. Above 45° the force wins and the system drifts toward
decoupling. This is a diagnostic threshold — the "sizzling" onset in the
Leidenfrost analogy — not a bifurcation.

Three new numbers fall out automatically:

- **alpha_c = 1/√2 ≈ 0.707** — the coupling strength at the crossover
- **n_c = √2 ≈ 1.414** — the PDTP refractive index at the crossover
  (universal: independent of coupling strength g or condensate mass m_cond)
- **Energy fraction = 1 − 1/√2 ≈ 29.3%** — the fraction of total
  decoupling energy needed to reach the crossover

---

## 1. Background and Starting Point

**Source:** CLAUDE.md field equations (derived from L = ½(∂μφ)² + ½(∂μψ)² + g cos(ψ−φ))

The Euler-Lagrange equations are [ASSUMED from Lagrangian]:

$$\Box\phi = g\sin(\psi-\phi) \tag{A}$$

$$\Box\psi = -g\sin(\psi-\phi) \tag{B}$$

Subtracting (A) from (B):

$$\Box(\psi-\phi) = -2g\sin(\psi-\phi)$$

For a spatially homogeneous, time-dependent configuration (∂ᵢΔ = 0), with
□ = ∂ₜ² − ∇² (particle physics convention):

$$\ddot\Delta = -2g\sin\Delta \tag{99.1 [DERIVED]}$$

This is the **pendulum equation** with effective frequency g. The potential for
which this is a gradient flow is:

$$V(\Delta) = -2g\cos\Delta \tag{99.2 [DERIVED]}$$

**SymPy check:** dV/dΔ = 2g sin Δ; residual from substitution = 0. ✓

---

## 2. Fixed Points and Stability

The fixed points satisfy dV/dΔ = 2g sin Δ = 0:

$$\Delta^* = 0 \quad \text{(stable)}, \quad \Delta^* = \pi \quad \text{(unstable)} \tag{99.7, 99.8}$$

### 2.1 Stability at Δ = 0

Linearise: Δ = δ (small), sin δ ≈ δ

$$\ddot\delta = -2g\,\delta \implies \omega_0^2 = 2g \tag{99.7 [DERIVED]}$$

**This is the breathing mode frequency** derived in previous Parts. The
eigenvalue is positive (ω₀² > 0), confirming Δ = 0 is a **stable
minimum**. Small perturbations from full coupling oscillate with frequency
ω₀ = √(2g).

**SymPy check:** d²V/dΔ²|_{Δ=0} = 2g cos(0) = 2g. ✓

### 2.2 Instability at Δ = π

Linearise: Δ = π + δ', sin(π+δ') = −sin δ' ≈ −δ'

$$\ddot{\delta'} = +2g\,\delta' \implies \text{eigenvalue} = +2g > 0 \tag{99.8 [DERIVED]}$$

Positive eigenvalue → **unstable saddle**. A perturbation at Δ = π
grows exponentially.

### 2.3 At Δ = π/4 (tan = 1)

$$\left.\frac{dV}{d\Delta}\right|_{\Delta=\pi/4} = 2g\sin(\pi/4) = g\sqrt{2} \neq 0$$

**Δ = π/4 is NOT a fixed point.** The system is not at rest here. It is a
point on the slope between equilibrium (Δ=0) and decoupling (Δ=π/2).

---

## 3. Force-Coupling Crossover [Eq 99.3]

At any Δ, the equation of motion has two contributions:

| Quantity | Expression | Physical role |
|----------|-----------|---------------|
| Coupling term | 2g cos Δ = 2g α | Restoring — pulls toward Δ=0 |
| Force term | 2g sin Δ | Driving — pushes toward Δ=π/2 |

At Δ = π/4:

$$2g\sin(\pi/4) = 2g\cos(\pi/4) = g\sqrt{2}$$

$$\Rightarrow \tan(\Delta_c) = \frac{\sin\Delta_c}{\cos\Delta_c} = 1 \tag{99.3 [PDTP Original, DERIVED]}$$

**SymPy check:** tan(π/4) = 1 exactly. ✓

### Regime classification [Eq 99.4, PDTP Original]

| Regime | Condition | Dominant term | Leidenfrost analogy |
|--------|-----------|---------------|---------------------|
| Coupled | Δ < π/4 (tan < 1) | Coupling > Force | Direct contact / wetting |
| Crossover | Δ = π/4 (tan = 1) | Coupling = Force | **Sizzling onset** |
| Decoupling | π/4 < Δ < π/2 (tan > 1) | Force > Coupling | Vapour cushion forming |
| Decoupled | Δ = π/2 (tan → ∞) | Force ≫ Coupling | Full Leidenfrost state |

**Cross-check with Part 71** (leidenfrost_decoupling.md table): the pi/4
row already listed V/g = −0.707 as "Partial decoupling" [CONSISTENT]. The
identification of tan > 1 as the sizzling onset is a **new result** not
previously in the Leidenfrost analysis.

---

## 4. Refractive Index at the Crossover [Eq 99.5]

From Part 98 [Eq 98.1]: n = 1/α = 1/cos Δ.

At the crossover Δ = π/4:

$$\alpha_c = \cos(\pi/4) = \frac{1}{\sqrt{2}} \approx 0.7071 \tag{99.5a [DERIVED]}$$

$$n_c = \frac{1}{\alpha_c} = \sqrt{2} \approx 1.4142 \tag{99.5 [PDTP Original, DERIVED]}$$

**SymPy check:** 1/cos(π/4) − √2 = 0. ✓

**Why this matters:** n_c = √2 is a **universal PDTP number** — it does
not depend on the coupling strength g, the condensate mass m_cond, or
any other free parameter. Any regime where the decoupling force equals
the restoring coupling has a PDTP refractive index of exactly √2. This
is a parameter-free prediction.

---

## 5. Energy Analysis [Eq 99.6]

From V(Δ) = −2g cos Δ:

| State | Δ | V (units of g) | Description |
|-------|---|----------------|-------------|
| Coupled | 0 | −2g | Global minimum |
| Crossover | π/4 | −√2 g ≈ −1.414g | tan = 1 threshold |
| Decoupled | π/2 | 0 | Zero coupling |
| Anti-coupled | π | +2g | Unstable maximum |

**Energy to crossover from full coupling:**

$$\Delta V_{\text{cross}} = V(\pi/4) - V(0) = -\sqrt{2}\,g - (-2g) = (2-\sqrt{2})\,g \approx 0.586\,g$$

**Energy to fully decouple:**

$$\Delta V_{\text{dec}} = V(\pi/2) - V(0) = 0 - (-2g) = 2g$$

**Fraction of decoupling energy at crossover:**

$$f_c = \frac{(2-\sqrt{2})\,g}{2g} = 1 - \frac{1}{\sqrt{2}} \approx 0.2929 \tag{99.6 [PDTP Original, DERIVED]}$$

**SymPy check:** symbolic computation of (V(π/4)−V(0))/(V(π/2)−V(0)) − (1−1/√2) = 0. ✓

**Interpretation:** the system must acquire 29.3% of the total decoupling
energy before the decoupling force overtakes the restoring coupling. This
is the minimum energy threshold for the "sizzling" regime to begin. The
remaining 70.7% of the energy is required to complete decoupling.

**Separatrix energy:** E_sep = V(π) = +2g. A system starting from rest
at Δ=π/4 has energy E = V(π/4) = −√2 g ≪ E_sep, so it is deep inside
the bound oscillation regime and will NOT spontaneously escape to decoupling.

---

## 6. Two-Phase Check

From Part 61 two-phase Lagrangian:

$$L = +g\cos(\psi-\phi_b) - g\cos(\psi-\phi_s)$$

The coupled phases are:

$$\Delta_+ = \frac{\Delta_b + \Delta_s}{2}, \quad \Delta_- = \frac{\Delta_b - \Delta_s}{2}$$

At the crossover Δ₊ = π/4:

$$n_+ = \frac{1}{\cos(\pi/4)} = \sqrt{2} \quad \text{[same as single-phase]}$$

In vacuum, φ₋ ≈ 0 (Part 71 Sec 4.1), so Δ₋ ≈ 0 and n₋ ≈ 1.

**Two-phase correction** to n₊ is second order in Δ₋:

$$n_+ \to n_+ \left(1 + \frac{\Delta_-^2}{2}\right) \approx \sqrt{2} + O(\Delta_-^2)$$

In vacuum this correction is negligible. Near dense matter (Part 62
reversed Higgs), φ₋ acquires a mass and Δ₋ could be small but nonzero —
a higher-order effect outside the scope of this Part.

**Conclusion:** The two-phase Lagrangian leaves the crossover result unchanged
in vacuum. [CONSISTENT with Part 61]

---

## 7. SymPy Verification Summary

All PDTP Original results verified symbolically:

| Check | Expression | Residual | Result |
|-------|-----------|---------|--------|
| dV/dΔ | 2g sin Δ | 0 | VERIFIED |
| d²V/dΔ² | 2g cos Δ | 0 | VERIFIED |
| tan(π/4) = 1 [Eq 99.3] | tan(π/4) − 1 | 0 | VERIFIED |
| n_c = √2 [Eq 99.5] | 1/cos(π/4) − √2 | 0 | VERIFIED |
| Energy fraction [Eq 99.6] | (V(π/4)−V(0))/(V(π/2)−V(0)) − (1−1/√2) | 0 | VERIFIED |
| ω₀² = 2g [Eq 99.7] | d²V/dΔ²|_{Δ=0} − 2g | 0 | VERIFIED |

---

## 8. Sudoku Consistency (10/10 PASS)

| Test | Check | Result |
|------|-------|--------|
| S1 | tan(0) = 0 (fully coupled) | PASS |
| S2 | tan(π/4) = 1 [Eq 99.3] | PASS |
| S3 | cos(π/4) = 1/√2 [Eq 99.5a] | PASS |
| S4 | n_c = √2 [Eq 99.5] | PASS |
| S5 | V(0) = −2g (minimum) | PASS |
| S6 | V(π/2) = 0 (decoupled) | PASS |
| S7 | ω₀² = 2g (breathing mode) [Eq 99.7] | PASS |
| S8 | d²V at π: −2g (unstable) [Eq 99.8] | PASS |
| S9 | Energy fraction = 1−1/√2 [Eq 99.6] | PASS |
| S10 | Two-phase n₊ = √2 at Δ₊=π/4 (Part 61) | PASS |

---

## 9. Equations Summary

| Eq # | Formula | Status | Source |
|------|---------|--------|--------|
| 99.1 | ddot(Δ) = −2g sin Δ | [DERIVED] | EL from Lagrangian |
| 99.2 | V(Δ) = −2g cos Δ | [DERIVED] | dV/dΔ = −ddot(Δ) |
| 99.3 | tan(Δ_c) = 1, Δ_c = π/4 | [PDTP Original, DERIVED] | sin = cos at π/4 |
| 99.4 | Regime classification (tan<1,=1,>1) | [PDTP Original, DERIVED] | force/coupling ratio |
| 99.5 | n_c = 1/cos(π/4) = √2 | [PDTP Original, DERIVED] | Eq 98.1 + Eq 99.3 |
| 99.5a | α_c = cos(π/4) = 1/√2 | [DERIVED] | direct |
| 99.6 | f_c = 1 − 1/√2 ≈ 0.293 | [PDTP Original, DERIVED] | energy fraction |
| 99.7 | ω₀² = 2g (breathing mode at Δ=0) | [DERIVED] | linearisation |
| 99.8 | Eigenvalue at Δ=π: +2g (unstable) | [DERIVED] | linearisation |

---

## 10. Open Questions

1. **Dark energy:** if Δ grows cosmologically (phase drift), does the
   universe pass through Δ = π/4 today? If so, the dark energy transition
   at z ~ 0.7 would correspond to the sizzling onset. This is T3.

2. **Observable signature:** near a compact object where Δ_+ approaches
   π/4, the PDTP refractive index would be n ≈ √2 ≈ 1.414. Is this
   distinguishable from standard GR lensing at that density?

3. **Two-phase crossover:** is there a separate crossover for Δ₋? The
   reversed Higgs (Part 62) gives φ₋ a mass near matter — does Δ₋ ever
   reach π/4 inside a neutron star?

---

*[SPECULATIVE] All physical interpretations above are speculative until
experimentally tested. Mathematical derivations are exact.*
