# Two-Phase Jeans Eigenvalue Correction: √3·g, not 2√2·g (Part 154)

**TODO:** TODO_04.md T83, sub-task **83b** — worked by **CLAUDE OPUS 5.5**
(`claude-opus-5-5`), 2026-09-28.
**Script:** `simulations/solver/t83b_jeans_correction.py`
**Log:** `simulations/solver/outputs/t83b_jeans_correction_<timestamp>.txt`
**Scorecard:** 10 matches, 2 contradictions out of 12 tests (both
contradictions are the old value / its hidden assumption — expected).
**Status:** CORRECTED. The instability survives (sign unchanged); its
magnitude was wrong by the factor √3/(2√2) ≈ 0.612. Root cause: forces were
used as accelerations for fields whose inertia is 2.

---

## Plain-English Summary

Part 61 found that the two-phase Lagrangian has a runaway ("Jeans") mode —
a disturbance that grows by itself, which PDTP reads as the seed of
gravitational clumping. That finding **still stands**. What was wrong is
*how fast* it grows.

The mistake is like computing a car's acceleration by dividing the engine
force by the mass of a motorbike. When bulk and surface phases are
combined into the new variables φ₊ and φ₋, each new variable ends up
"twice as heavy" (its kinetic term is φ̇² instead of ½φ̇²). Part 61 used the
heavy-variable force with a light-variable mass. Part 61 *did* use the
heavy mass for Newton's 3rd law (ψ̈ = −2φ̈₊) — so the old eigenvalue and the
old Newton's-3rd-law result were quietly using two different masses for
the same field. Only one can be right, and a check that avoids the change
of variables entirely confirms it is the heavier one.

**Also found (bonus):** the runaway mode lives at the "unlocked" point
(φ₋ = 0). At the true vacuum identified in Part 119 (φ₋ = π/2), both modes
are stable oscillations. So the instability describes the system rolling
*toward* its vacuum, not an instability *of* the vacuum.

**Also found (new sub-task 83j):** the same heavy-vs-light slip appears in
Part 62's "reversed Higgs" mass formula m² = 2gΦ; with the correct inertia
it is m² = gΦ.

---

## 1. Starting Point [ASSUMED]

Two-phase Lagrangian (Part 61), uniform fields:

```
L = 1/2 (psi_t^2 + phi_b_t^2 + phi_s_t^2) + g cos(psi - phi_b) - g cos(psi - phi_s)   (154.1)
```

$$
L = \tfrac12\left(\dot\psi^2 + \dot\phi_b^2 + \dot\phi_s^2\right) + g\cos(\psi-\phi_b) - g\cos(\psi-\phi_s)
$$

**Sign conventions:** L = T − V with V = −L_int; linear system ẍ = Mx;
eigenvalue λ > 0 ⇒ growth rate σ = √λ; λ < 0 ⇒ oscillation ω = √(−λ).
**Source (small oscillations, ẍ = −K⁻¹ Hess(V) x):** Goldstein,
*Classical Mechanics*, §6.2.

---

## 2. Route 1 — Original Fields, No Change of Variables [DERIVED, VERIFIED]

All three fields have unit inertia (K = identity), so M = −Hess(V).

**Step 1.** V = −g cos(ψ − φ_b) + g cos(ψ − φ_s).
**Step 2.** Expand about ψ = φ_b = φ_s = 0 using cos x ≈ 1 − x²/2:
V ≈ const + (g/2)(ψ − φ_b)² − (g/2)(ψ − φ_s)².
**Step 3.** Second derivatives: ∂²V/∂ψ² = g − g = 0; ∂²V/∂φ_b² = g;
∂²V/∂φ_s² = −g; ∂²V/∂ψ∂φ_b = −g; ∂²V/∂ψ∂φ_s = +g; ∂²V/∂φ_b∂φ_s = 0.
**Step 4.** M = −Hess(V):

```
M = [[ 0,  g, -g],
     [ g, -g,  0],
     [-g,  0,  g]]                                                         (154.2)
```

$$
M = \begin{pmatrix} 0 & g & -g \\ g & -g & 0 \\ -g & 0 & g \end{pmatrix}
$$

**Step 5.** Characteristic polynomial, expanding det(M − λI) along the
first row of [[−λ, g, −g], [g, −g−λ, 0], [−g, 0, g−λ]]:
- term 1: (−λ)·[(−g−λ)(g−λ) − 0] = (−λ)(λ² − g²) = −λ³ + λg²
- term 2: −(g)·[g(g−λ) − 0] = −g³ + λg²
- term 3: (−g)·[g·0 − (−g−λ)(−g)] = (−g)·[−g(g+λ)] = g³ + λg²
- sum: −λ³ + 3λg² = −λ(λ² − 3g²)

```
lambda in { 0, +sqrt(3) g, -sqrt(3) g }                                    (154.3)
```

$$
\lambda \in \{0,\ +\sqrt3\,g,\ -\sqrt3\,g\}
$$

[VERIFIED: S1 (SymPy), S8 (numpy at g = 1: −1.7320508, 0.0, +1.7320508).]
The zero eigenvalue is the joint-shift Goldstone mode (Part 153, S7 here).
Eigenvalues are basis-independent, so no later change of variables can
change ±√3·g.

---

## 3. Route 2 — Mode Variables With Correct Inertias [DERIVED, VERIFIED]

**Step 1 (kinetic term).** With φ_b = φ₊ + φ₋, φ_s = φ₊ − φ₋:
½(φ̇₊ + φ̇₋)² + ½(φ̇₊ − φ̇₋)² = φ̇₊² + φ̇₋² (cross terms cancel).
In the ½·I·q̇² convention the inertias are I₊ = I₋ = 2; I_ψ = 1.
[VERIFIED: S4, (2, 2, 0).]

**Step 2 (forces).** L_int = 2g sin(ψ − φ₊) sin φ₋ (product identity,
A&S 4.3.37; S11 residual 0). With Θ = ψ − φ₊:
F_ψ = 2g cos Θ sin φ₋; F₊ = −2g cos Θ sin φ₋; F₋ = 2g sin Θ cos φ₋.

**Step 3 (accelerations = F/I), linearised at Θ = 0, φ₋ = 0:**
ψ̈ = 2gφ₋; φ̈₊ = −gφ₋; φ̈₋ = gΘ.
**Step 4.** Θ̈ = ψ̈ − φ̈₊ = 2gφ₋ + gφ₋ = 3gφ₋.

```
d^2/dt^2 [Theta, phi_-] = [[0, 3g], [g, 0]] [Theta, phi_-],   lambda = +/- sqrt(3) g   (154.4)
```

$$
\frac{d^2}{dt^2}\begin{pmatrix}\Theta\ \phi_-\end{pmatrix} = \begin{pmatrix}0 & 3g\ g & 0\end{pmatrix}\begin{pmatrix}\Theta\ \phi_-\end{pmatrix},\qquad \lambda = \pm\sqrt3\,g
$$

det(M − λI) = λ² − 3g². [VERIFIED: route 2 eigenvalues equal route 1's
nonzero eigenvalues, S1.] Newton's 3rd law with the same inertias:
ψ̈ + 2φ̈₊ = F_ψ + F₊ = 0 [VERIFIED: S5, residual 0].

---

## 4. Route 3 — Diagnosing the Old Value [VERIFIED]

Set every inertia to 1 (i.e. read the forces F as accelerations):
φ̈₊ = −2gφ₋, φ̈₋ = 2gΘ, Θ̈ = 4gφ₋ ⇒ M = [[0, 4g], [2g, 0]], λ = ±2√2·g.
This reproduces Part 61's matrix exactly [S3 MATCH] — so the old value is
fully explained by the inertia-1 assumption. With the same inertias,
ψ̈ + 2φ̈₊ = −2g sin φ₋ cos(φ₊ − ψ) ≠ 0 [S6 CONTRADICTION]: the old eigenvalue
is incompatible with Part 61's own Newton's 3rd law. The source is the
labelling in `two_phase_lagrangian.py`: `euler_lagrange_1d` correctly
returned the force ∂L/∂q, but the verification labels and the eigenvalue
block called it q̈.

```
lambda_new / lambda_old = sqrt(3) / (2 sqrt(2)) = sqrt(6)/4 = 0.6124       (154.5)
```

$$
\frac{\lambda_\text{new}}{\lambda_\text{old}} = \frac{\sqrt3}{2\sqrt2} = \frac{\sqrt6}{4} \approx 0.612
$$

---

## 5. Dispersion, Jeans Wavenumber, Vacuum [DERIVED, VERIFIED]

**Dispersion.** Each field obeys I(∂_t² − c²∇²)q = F, so dividing by I
keeps the c²k² term unchanged: ω² = c²k² − λ.

```
omega^2 = c^2 k^2 - sqrt(3) g   (Jeans branch);   omega^2 = c^2 k^2 + sqrt(3) g   (gapped branch)   (154.6)
k_J = (sqrt(3) g)^(1/2) / c,     k_J,new / k_J,old = (sqrt(6)/4)^(1/2) = 0.7825                  (154.7)
```

$$
\omega^2 = c^2k^2 \mp \sqrt3\,g,\qquad k_J = \frac{\sqrt{\sqrt3\,g}}{c},\qquad \frac{k_{J,\text{new}}}{k_{J,\text{old}}} = 0.7825
$$

[VERIFIED: S12.] **Dimensions:** [g] = m⁻² in the static field equation
(term_glossary §4); in the time equation the same coefficient carries
c²·g (s⁻²), so √(√3 g_dyn)/c is m⁻¹ ✓.

**At the Part 119 vacuum (Θ = φ₋ = π/2), correct inertias:**
M = diag(−3g, −g): both eigenvalues negative ⇒ two stable oscillations,
ω² = 3g and ω² = g [VERIFIED: S10]. The Jeans instability belongs to the
unlocked point φ₋ = 0, not to the vacuum.

---

## 6. Sudoku Scorecard

| ID | Test | Computed | Expected | Result |
|----|------|----------|----------|--------|
| S1 | Route 1 nonzero eigenvalues = Route 2 | ±√3·g | equal | MATCH |
| S2 | Route 2 vs old Part 61 value | ±√3·g | ±2√2·g | **CONTRADICTION** (the correction) |
| S3 | Route 3 reproduces Part 61 matrix | [[0,4g],[2g,0]] | same | MATCH |
| S4 | Inertias of φ₊, φ₋; cross term | (2, 2, 0) | (2, 2, 0) | MATCH |
| S5 | Newton 3rd, inertias (1,2,2) | 0 | 0 | MATCH |
| S6 | Newton 3rd, inertias (1,1,1) | −2g sin φ₋ cos(φ₊−ψ) | 0 | **CONTRADICTION** (old assumption) |
| S7 | Route 1 zero mode (Goldstone) | multiplicity 1 | 1 | MATCH |
| S8 | numpy eigenvalue vs √3 | 1.7320508 | 1.7320508 | MATCH |
| S9 | Positive growth eigenvalue exists | √3·g | > 0 | MATCH |
| S10 | Part 119 vacuum stable | −3g, −g | < 0 | MATCH |
| S11 | Product identity residual | 0 | 0 | MATCH |
| S12 | k_J ratio | 0.782542 | 0.782542 | MATCH |

**Score: 10 matches, 2 contradictions out of 12.** Both contradictions
share one assumption (inertia 1 for φ₊, φ₋) and are exactly what is being
corrected. **Two-phase checks:** Newton's 3rd law preserved (S5); Jeans
eigenvalue still positive (S9). **Standard Model compatibility:** no new
field or term; a numerical correction inside the existing two-phase sector
— no gauge, particle-content or conservation-law impact.

---

## 7. Impact on Other Results

| Where | Effect |
|-------|--------|
| `two_phase_lagrangian.py` (Part 61) | Eigenvalue now computed (was a typed string); labels fixed; 10/10 still PASS |
| `white_comparison.py` WH11 | Was circular (typed M, checked its own eigenvalue); now re-derived from L; 12/12 PASS |
| `condensate_layer_fcc.py` | 3 hardcoded `True` flags (RECHECK violation) replaced by computed checks; biharmonic flag now "NOT CHECKED (83c)" |
| `cosmo_constant_v2.py` (Part 68) | g is *calibrated* from ω_gap (g = ω_gap²/coeff), so every observable (k_J, κ, ω_beat) is unchanged; only the inferred g shifts by 2√2/√3 ≈ 1.633. Re-run: 15/15, output identical except labels |
| Print-only scripts (cp_violation, cp_violation_quantitative, frequency_reframe, phi_minus_quartic, t55, coupling_constant_g, emergent_c) | Quoted value updated; no computed number depends on it; not re-run |
| Docs quoting 2√2·g | Corrected in place with a pointer here |
| Biharmonic ∇⁴Φ + 4g²Φ and φ₋ docstrings | Same inertia slip — sub-task 83c |
| Part 62 m² = 2gΦ (reversed Higgs) | Same slip: V″ not divided by I₋ = 2 ⇒ m² = gΦ — new sub-task 83j |
| CLAUDE.md "eigenvalue +2√2 g" | Updated in 83h (CLAUDE.md edited only when T83 is done) |

---

## 8. Analysis [SPECULATIVE]

The physical reading of Part 61 (unstable mode ↔ gravitational clumping)
is unaffected in kind, but two refinements follow: (1) the growth rate is
√(√3·g) rather than √(2√2·g), about 22% slower; (2) since the vacuum is
stable (S10), the instability is a property of the unlocked starting point
— closer to "the condensate falling into its vacuum" than to "the vacuum
is unstable". Whether that roll is what PDTP should identify with
clumping is an interpretation question for 83i/83j, not settled here.

**Status:** 83b DONE. No falsifiable prediction changes (the Jeans scale
is Planckian and not an observed number; `cosmo_constant_v2` observables
unchanged).
