# Biharmonic Equation Re-derivation: ∇⁴φ₊ − g²φ₊ = −g²ψ (Part 155)

**TODO:** TODO_04.md T83, sub-task **83c** — worked by **CLAUDE OPUS 5.5**
(`claude-opus-5-5`), 2026-09-28.
**Script:** `simulations/solver/t83c_biharmonic.py`
**Log:** `simulations/solver/outputs/t83c_biharmonic_<timestamp>.txt`
**Scorecard:** 9 matches, 3 contradictions out of 12 tests (all three
contradictions are claims being corrected).
**Status:** CORRECTED. Part 61's "∇⁴Φ + 4g²Φ = source" does not follow from
the two-phase Lagrangian. The correct static equation is
**∇⁴φ₊ − g²φ₊ = −g²ψ**, whose Green's function has **no 1/r term at any
range**. Earlier statements that biharmonic gravity "reduces to Poisson /
Newton at short range" (Parts 61, 86) are withdrawn.

---

## Plain-English Summary

Part 61 combined two of its equations into one "fourth-order" equation for
gravity (a *biharmonic* equation: the Laplacian applied twice). Re-doing
that step carefully found **three slips**:

1. **Wrong mass** for the φ₊ and φ₋ fields (the same slip as sub-task 83b:
   they are "twice as heavy" as assumed). This changes 4g² into g².
2. **Wrong sign on the static equation** (∇²q = +force instead of
   −force/mass). This one happens to cancel out, because it appears twice.
3. **An algebra slip in the last line**, which flipped + into −. The step
   −∇⁴φ₊ = 4g²(ψ − φ₊) was rearranged as ∇⁴φ₊ **+** 4g²φ₊ = …, but it
   actually gives ∇⁴φ₊ **−** 4g²φ₊ = … . No choice of conventions produces
   the "+" (checked all four combinations).

**Why the sign matters.** With "+", a point source's field fades away
smoothly. With "−", it becomes a mix of a fading part and a *ripple* —
cos(r/a₀)/r — that keeps oscillating forever with a wavelength of about
2π × a₀ (Planck length for m_cond = m_P). Over any distance we can measure,
that ripple averages to zero.

**Why this matters for "Newton at short range".** Parts 61 and 86 said that
close to a source (r ≪ a₀) the equation looks like Newton's 1/r. It does
not: the fourth-order equation's field near a point source is
*constant minus a straight line* (≈ 1/(8πκ) − r/8π), never 1/r. Together
with Part 153 (83a), this means **neither the second-order nor the
fourth-order route currently produces Newton's 1/r strength from the
Lagrangian** — the 1/r *shape* only appears outside matter, where the
coupling is zero, and its *strength* is the open problem filed as 83i.

**What does not change.** Every negative verdict that used this equation
(the ~54-orders MOND failure, the Hubble-tension correction of order
(l_P/r)²) survives: the scale moves by only √2 (a₀/√2 → a₀).

---

## 1. Starting Point [ASSUMED]

Two-phase Lagrangian in mode variables (Part 61; kinetic diagonalisation
verified in Part 154):

```
L = 1/2 psi_t^2 + phi_+t^2 + phi_-t^2 - (same with gradients) + 2 g sin(psi - phi_+) sin(phi_-)   (155.1)
```

$$
\mathcal{L} = \tfrac12\dot\psi^2 + \dot\phi_+^2 + \dot\phi_-^2 - (\text{gradients}) + 2g\sin(\psi-\phi_+)\sin\phi_-
$$

Inertias: I_ψ = 1, I₊ = I₋ = 2. Field equation for each field
[Euler–Lagrange, Goldstein §13.3]: I(q_tt − ∇²q) = F_q with F_q = ∂L_int/∂q.
**Static:**

```
nabla^2 q = - F_q / I_q                                                     (155.2)
```

$$
\nabla^2 q = -\frac{F_q}{I_q}
$$

**Assumptions:** [A1] linearise at Θ = ψ − φ₊ = 0, φ₋ = 0 (Part 61's own
point); [A2] constant g, so ∇² can be treated as a commuting symbol D;
[A3] "fixed ψ" = ψ is a prescribed source (Part 61's own treatment);
[A4] g = g_bare, units m⁻², g = ω_gap²/c² = 1/a₀² (term_glossary §4).

---

## 2. Derivation [DERIVED, VERIFIED]

**Step 1 (linear forces).** Differentiating 2g sin(ψ − φ₊) sin φ₋ and
keeping first order (sin x ≈ x, cos x ≈ 1):
F₊ = −2g cos Θ sin φ₋ ≈ −2gφ₋; F₋ = 2g sin Θ cos φ₋ ≈ 2g(ψ − φ₊);
F_ψ ≈ 2gφ₋. [VERIFIED: log "Linearised forces".]

**Step 2 (static equations, 155.2).**
∇²φ₊ = −F₊/2 = gφ₋ … (a)
∇²φ₋ = −F₋/2 = −g(ψ − φ₊) … (b)

**Step 3 (eliminate φ₋).** From (a): φ₋ = ∇²φ₊/g. Apply ∇² and use (b):
∇⁴φ₊/g = −g(ψ − φ₊). Multiply by g:
∇⁴φ₊ = −g²ψ + g²φ₊. Move g²φ₊ to the left:

```
nabla^4 phi_+ - g^2 phi_+ = - g^2 psi                                       (155.3)
```

$$
\nabla^4\phi_+ - g^2\phi_+ = -g^2\,\psi
$$

[VERIFIED: S4 (source term −g²), P(D) = D² − g² by exact SymPy elimination.]

**Dimensions:** [∇⁴φ₊] = m⁻⁴; [g²φ₊] = (m⁻²)² = m⁻⁴ ✓ (φ, ψ dimensionless).

**Step 4 (where "+4g²" came from).** Repeating Steps 2–3 with each
combination of the old conventions (inertia 1 vs 2; static sign +F vs −F/I):

| Inertia | Static sign | P(D) = D² + c₀ | Source |
|---------|-------------|----------------|--------|
| (1, 2, 2) | −F/I (correct) | D² − g² | −g²ψ |
| (1, 2, 2) | +F | D² − g² | −g²ψ |
| (1, 1, 1) | −F | D² − 4g² | −4g²ψ |
| (1, 1, 1) | +F (Part 61's) | D² − 4g² | −4g²ψ |

[VERIFIED: S2, S3.] The static sign cancels (it enters both (a) and (b)).
Inertia 1 gives the factor 4. **No combination gives +4g²**; Part 61's
"+" is an algebra slip in its final rearrangement.

**Step 5 (dynamical ψ, for comparison).** If ψ obeys its own equation
(∇²ψ = −F_ψ = −2gφ₋), the static system Dx = Ax for x = (ψ, φ₊, φ₋) has
A = [[0, 0, −2g], [0, 0, g], [−g, g, 0]], eigenvalues {0, ±√3·g}
[VERIFIED: S5] — i.e. ∇⁴Θ − 3g²Θ = 0 with no source, plus the free
Goldstone combination. This is the static twin of Part 154's eigenvalues
and of Part 153's result that dynamical, locked matter sources nothing.

---

## 3. Green's Function: No 1/r at Any Range [DERIVED, VERIFIED]

Write κ⁴ = g² (κ = √g = 1/a₀). The Green's function solves
(∇⁴ − κ⁴)G = δ³(x).

**Step 1 (partial fractions in Fourier space).** With ∇² → −k²:
1/(k⁴ − κ⁴) = [1/(k² − κ²) − 1/(k² + κ²)] / (2κ²).

**Step 2 (known transforms).** 1/(k² + κ²) ↔ e^{−κr}/(4πr)
(**Source:** [Yukawa potential — Wikipedia](https://en.wikipedia.org/wiki/Yukawa_potential));
the principal-value transform of 1/(k² − κ²) is cos(κr)/(4πr) (standing-wave
Helmholtz Green's function). Hence

```
G(r) = ( cos(kappa r) - exp(-kappa r) ) / (8 pi kappa^2 r)                  (155.4)
```

$$
G(r) = \frac{\cos(\kappa r) - e^{-\kappa r}}{8\pi\kappa^2\, r}
$$

**Step 3 (checks).**
- (∇⁴ − κ⁴)G = 0 for r > 0: residual 0 [VERIFIED: S6].
- Closed form equals the partial-fraction sum at r = 0.5, 2, 7 to 10⁻¹⁴ [S10].
- Normalisation: lim r·∇²G = −1/(4π), so ∇²G ≈ −1/(4πr) = the Poisson
  Green's function, and ∇⁴G = δ at the origin [S7].

**Step 4 (small r).** Using cos x = 1 − x²/2 + …, e^{−x} = 1 − x + x²/2 − …:

```
G(r) = 1/(8 pi kappa) - r/(8 pi) + kappa r^2/(48 pi) + ...   (no 1/r term)   (155.5)
```

$$
G(r) = \frac{1}{8\pi\kappa} - \frac{r}{8\pi} + \frac{\kappa r^2}{48\pi} + \dots
$$

[VERIFIED: log "small-r series"; coefficient of 1/r = 0, S8.] Part 86's
statement "Φ(r) ≈ source/(8πr) at r ≪ 1/√g" is **withdrawn** [NEGATIVE].

**Step 5 (large r).** e^{−κr} dies off; G → cos(κr)/(8πκ²r): an undamped
oscillation with wavelength 2πa₀.

**Step 6 (the old operator, for completeness).** ∇⁴ + a (a > 0) has Fourier
kernel 1/(k⁴ + a), and G(0) = (1/2π²)∫₀^∞ k²/(k⁴+a) dk =
1/(4√2 π a^{1/4}) — finite, so no 1/r either [VERIFIED: S9, numeric
0.05626977 = analytic 0.05626977 at a = 1].

**Scale.** κ_new = √g = 1/a₀ vs κ_old = (4g²)^{1/4} = √(2g) = √2/a₀:
lengths grow by √2 [S11]; **L_bih = a₀** [S12]. (T47's former a₀/2 came
from the uncorrected coefficient with g mis-dimensioned as 1/length.)

---

## 4. Sudoku Scorecard

| ID | Test | Computed | Expected | Result |
|----|------|----------|----------|--------|
| S1 | Constant term, correct conventions | −g² | +4g² (Part 61) | **CONTRADICTION** (the correction) |
| S2 | Any convention combo gives +4g²? | −g², −g², −4g², −4g² | +4g² somewhere | **CONTRADICTION** (algebra slip located) |
| S3 | Part 61's own conventions give | −4g² | −4g² | MATCH |
| S4 | Source term | −g² | −g² | MATCH |
| S5 | Dynamical-ψ eigenvalues of ∇² | 0, ±√3·g | same | MATCH (= Part 154) |
| S6 | (∇⁴ − κ⁴)G, r > 0 | 0 | 0 | MATCH |
| S7 | r∇²G → −1/(4π) | −1/(4π) | −1/(4π) | MATCH |
| S8 | 1/r coefficient at small r | 0 | 1/(8π) (Part 86) | **CONTRADICTION** (claim withdrawn) |
| S9 | Old operator G(0) finite | 0.056270 | 0.056270 | MATCH |
| S10 | Closed form = decomposition | True | True | MATCH |
| S11 | L_new / L_old | √2 | √2 | MATCH |
| S12 | L_bih with g = 1/a₀² | a₀ | a₀ | MATCH |

**Score: 9 matches, 3 contradictions out of 12** — each contradiction is a
previously stated result being corrected. **Two-phase checks:** Newton's
3rd law and the Jeans sign are untouched (Part 154). **Standard Model
compatibility:** no new field or term; correction inside the existing
two-phase sector — no gauge, particle-content, or conservation impact.

---

## 5. Impact

| Where | Effect |
|-------|--------|
| `two_phase_lagrangian.py` (Part 61) | Equation now computed by elimination; scale a₀; "Poisson at short range" removed; 10/10 |
| `nonlinear_einstein.py` (Part 86) | Sign argument and "1/r at short range" withdrawn; Green's function computed; Strategy 3 verdict CONSISTENT → NEGATIVE; 12/12 |
| `t47_mcond_scanner.py` | L_bih = a₀ (was a₀/2); 12/12 |
| `coupling_constant_g.py`, `white_comparison.py` | Coefficient g² (was 4g²); 12/12 each |
| `condensate_layer_fcc.py` | Biharmonic flag now computed (was hardcoded, then NOT CHECKED); PASS |
| Print-only (cp_violation, cp_violation_quantitative, phi_minus_quartic, hubble_tension_c1) | Wording updated, not re-run |
| MOND attempt (dark_matter_energy §2.5; ~54 OoM failure, T77/T74) | Verdict unchanged (√2 scale shift); rotation-curve reading further weakened (tail oscillates at Planck wavelength) |
| Hubble tension Approach C (Part 88) | (l_P/r_s)² order unchanged |
| `falsifiable_predictions.md` Prediction 11 | Updated with user approval (2026-09-28): F.16 corrected, F.17 withdrawn, status → not currently viable |
| Part 62 reversed-Higgs mass (m² = 2gΦ → gΦ) | Sub-task 83j (not changed here) |

---

## 6. Analysis [SPECULATIVE]

The biharmonic equation was presented as PDTP's own modification of
gravity: Newton at short range, something new at long range. The corrected
equation is instead a crossover between a linear potential (inside a₀) and
a Planck-wavelength ripple (outside a₀); neither is Newtonian. Combined with
Part 153, the honest status is: **the two-phase Lagrangian's static sector,
as written, does not produce Newtonian gravity by either route**; the 1/r
must come from the coupling-free exterior, with a strength set by an
ingredient not yet in the Lagrangian (83i). The ripple itself is not an
observable at m_cond = m_P; for a lighter condensate (Part 61's sub-mm
table) it would be a genuinely distinctive signature — a spatially
oscillating force — but only if 83i supplies a source for it.

**Status:** 83c DONE. No falsifiable prediction added; Prediction 11
corrected with user approval (2026-09-28).
