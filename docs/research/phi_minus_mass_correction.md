# φ₋ (Reversed-Higgs) Mass Correction: m² = gΦ, not 2gΦ (Part 157)

**TODO:** TODO_04.md T83, sub-task **83j** — worked by **CLAUDE OPUS 5.5**
(`claude-opus-5-5`), 2026-09-28.
**Script:** `simulations/solver/t83j_phi_minus_mass.py`
**Log:** `simulations/solver/outputs/t83j_phi_minus_mass_<timestamp>.txt`
**Scorecard:** 10 matches, 1 contradiction out of 11 (the contradiction is
the old value being corrected).
**Status:** CORRECTED. The environment-dependent φ₋ mass is **m² = g·Φ**
(Φ = sin(ψ − φ₊)); Part 62's m² = 2g·Φ took the potential curvature V″ as
the mass without dividing by φ₋'s inertia 2. The "reversed Higgs" behaviour
itself (massless in vacuum, massive near matter) is unchanged.

---

## Plain-English Summary

This is the last instance of the "heavy variable" slip found in 83b and 83c.
When the bulk and surface phases are recombined into φ₊ and φ₋, both new
variables carry **twice** the usual inertia. A field's mass is how *stiff*
its potential is divided by how *heavy* the field is — Part 62 used the
stiffness alone. Dividing by 2:

- **Every φ₋ mass and gap energy is 1/√2 ≈ 0.71 of the published value.**
  Near Earth 31.7 → **22.4 GeV**; near a neutron star 566 → **400 TeV**;
  ranges grow by √2 (Earth 0.006 → 0.0085 fm).
- **What does *not* change:** the potential itself (−2gΦ sin φ₋), the vacuum
  at φ₋ = π/2, "massless in vacuum / massive near matter", and every verdict
  that depended only on orders of magnitude (e.g. T74's 77-orders margin).
- **Part 119 (Λ as a locking fossil) is exactly unaffected where it
  matters.** Its key results are written in terms of the *measured* ε, and
  the slow-roll relation ε = m²/(9H²) doesn't care about inertia. So
  m/H = 3√ε, the freeze condition ε < 1/9 and the φ₋ mass today are all
  unchanged; only the bookkeeping number g_dyn doubles.
- **Part 117's quartic** halves (λ₄ = g² sin²β/(3k̄²)) because it had the
  same slip in the φ₊ stiffness — but the natural gap scale also halves, so
  its size at the gap (λ₄/g = sin²β/3) is unchanged.
- **One claimed coincidence is lost.** Part 113 said the φ₋ mass at a
  horizon *exactly* equals the breathing-mode gap (both 2g). Corrected, it
  is g vs 2g — not a match.
- **One T51 argument softens.** T51 said plugging g_dyn into the Λ formula
  would need φ_vac > π/2. With the corrected g_dyn it needs 1.55 rad — just
  under π/2, but still an O(1) angle, so T51's conclusion stands.

---

## 1. Derivation [DERIVED, VERIFIED]

**Starting point** [ASSUMED, Part 61]: kinetic term φ̇₊² + φ̇₋² (inertia 2
each, verified Part 154 S4), coupling 2g sin(ψ − φ₊) sin φ₋. With
Φ = sin(ψ − φ₊) as a background (Part 62), the φ₋ potential is

```
V(phi_-) = -2 g Phi sin(phi_-)                                              (157.1)
```

$$
V(\phi_-) = -2g\,\Phi\,\sin\phi_-
$$

**Step 1.** V′ = −2gΦ cos φ₋ = 0 at φ₋ = π/2; V″ = 2gΦ sin φ₋ = 2gΦ there.
**Step 2 (small oscillations,** Goldstein §6.2**):** L = ½·I·φ̇₋² − V ⇒
ω² = V″/I. With I₋ = 2:

```
m^2(phi_-) = V''/I_- = 2 g Phi / 2 = g Phi                                 (157.2)
```

$$
m_{\phi_-}^2 = \frac{V''}{I_-} = g\,\Phi
$$

[VERIFIED: S1 (SymPy), S5 ratio 1/2.] **Step 3 (canonical check).** With
φ_c = √2 φ₋ (kinetic ½φ̇_c²), d²V/dφ_c² = V″/2 = gΦ [S2]. **Step 4
(independent check).** Part 154's full linear dynamics at the vacuum
(Θ = φ₋ = π/2, Φ = 1) give the φ₋ eigenvalue −g, i.e. m² = g [S3]. Part 62's
2gΦ is reproduced exactly by setting I₋ = 1 [S4].
**Dimensions:** [g] = m⁻² (term_glossary §4), Φ dimensionless ⇒ [m²] = m⁻²
(a wavenumber²; ×c² for a frequency²) ✓.

**Dispersion:** ω² = c²k² + gΦ; E_gap = ħ√(gΦ) (natural units).

## 2. Slow Roll: Part 119 Is Inertia-Independent [DERIVED, VERIFIED]

For a mode with L = ½I q̇² − ½I m² q², overdamped roll 3H q̇ = −V′/I:
q̇ = −m² q/(3H), K = ½I q̇² = ½I m⁴q²/(9H²), V = ½I m² q², so

```
eps = K / V = m^2 / (9 H^2)    ->    m / H = 3 sqrt(eps)                     (157.3)
```

$$
\varepsilon = \frac{K}{V} = \frac{m^2}{9H^2} \;\Rightarrow\; \frac{m}{H} = 3\sqrt{\varepsilon}
$$

[VERIFIED: S6 (no I in the result), S7.] **Source (slow-roll):**
[Inflaton — Wikipedia](https://en.wikipedia.org/wiki/Inflaton). Part 119
combined "m² = 2g" with "ε = 2g/(9H²)"; both carried the same convention,
so Eq 119.1 is exact once expressed in m. With m fixed by the measured ε,
g_dyn = m² = 9H₀²ε₀ = 4.065×10⁻³⁶ s⁻² (was 2.03×10⁻³⁶) [S8: ratio 2].

## 3. Part 117 Induced Quartic [DERIVED, VERIFIED]

Integrating out the φ₊ fluctuation η: the gradient energy from (∂φ₊)² is
k̄²η² = ½(2k̄²)η², so M = 2k̄² (Part 117 used k̄²). V_ind = −J²/(2M) with
J = −2g sin β sin φ₋ (Part 117) gives

```
V_ind = -(g^2 sin^2(beta)/kbar^2) sin^2(phi_-),   lambda_4 = g^2 sin^2(beta) / (3 kbar^2)    (157.4)
```

$$
\lambda_4 = \frac{g^2\sin^2\beta}{3\bar k^2}
$$

[VERIFIED: S9 ratio 1/2.] At the natural gap k̄² = m²(Φ=1) = g (was 2g):
λ₄/g = sin²β/3, identical to Part 117's value [S10].

## 4. Sudoku Scorecard

| ID | Test | Computed | Expected | Result |
|----|------|----------|----------|--------|
| S1 | m² = V″/I₋ vs Part 62 | gΦ | 2gΦ | **CONTRADICTION** (the correction) |
| S2 | Canonical field gives same m² | gΦ | gΦ | MATCH |
| S3 | Part 154 vacuum eigenvalue | −g | −g | MATCH |
| S4 | Part 62 reproduced with I₋ = 1 | 2gΦ | 2gΦ | MATCH |
| S5 | m² ratio new/old | 1/2 | 1/2 | MATCH |
| S6 | ε = m²/(9H²), inertia-free | m²/(9H²) | same | MATCH |
| S7 | m/H = 3√ε invariant | 3√ε | 3√ε | MATCH |
| S8 | g_dyn ratio at fixed m | 2 | 2 | MATCH |
| S9 | λ₄ ratio (same k̄) | 1/2 | 1/2 | MATCH |
| S10 | λ₄/g at natural gap | sin²β/3 | sin²β/3 | MATCH |
| S11 | Mass rescaling factor | 0.707107 | 1/√2 | MATCH |

**RECHECK note:** the first run of S7 returned −3√ε because the solver
symbol ε was not declared positive (a bug in the check); fixed and noted in
the script. **Two-phase checks:** Newton's 3rd law, Jeans sign untouched.
**Standard Model compatibility:** no new term; φ₋ couples only to the
gravitational sector — no gauge/particle-content impact.

---

## 5. Impact

**Scripts fixed and re-run** (score before → after):

| Script (Part) | Change | Score |
|---------------|--------|-------|
| `reversed_higgs.py` (62) | `PHI_MINUS_M2_COEFF = 1.0` in 6 mass computations; roll time uses a = gΦ | 10/10 → 10/10 |
| `t9_two_phase_tan.py` (113) | m² coefficient 1; S07 was circular (2·sin(π/2) vs 2) → now compares V″/2 with ω_gap² | 12/12 → **11/12** (S07 fails: the lost coincidence) |
| `condensate_layer_fcc.py` (89/96) | Earth 22.4 GeV, NS 400 TeV, proton 30 µeV; S21 reference updated | 12/12 → 12/12 |
| `dispersion_two_phase.py` (80) | E_gap = ħ√(gΦ) | 10/10 → 10/10 |
| `t46_lambda_fossil.py` (119) | g_cosmo = 9H²ε, m² = g; T3/T6/T7/T12 updated; m unchanged | 12/12 → 12/12 |
| `t51_dimensional_audit.py` (T51) | g_dyn = 9H²ε; T8 ref updated; **T11 now FAILS** (φ_vac,req = 1.5525 < π/2) | → 11/12 |
| `phi_minus_quartic.py` (117) | stiffness 2k̄², gap k̄² = g; λ₄ halves, λ₄/g at gap unchanged | 10/10 → 10/10 |
| `scale_selection.py` (69) | μ² = g sin δ, L_kink = c/√g; also 83b leftover g = ω_gap²/√3 | 10/10 → 10/10 |
| `leidenfrost_decoupling.py` (71/110) | ω(φ₋) = √(gΦ); also 83b leftover g = ω_gap²/√3, ΔE = m c²/√3 | 9/10 → 9/10 (LD-S6 fails, **pre-existing**) |
| `t26_lazar_truth_table.py` (135) | 83b leftover: ΔE = m_P c²/√3 (was /(2√2)); OoM verdict unchanged | runs |
| `t18`, `t74`, `two_phase_rederivation`, `coupling_constant_g`, `koide_reexamine`, `white_comparison`, `t68` | coefficient 1 | unchanged (7/10 for koide is pre-existing) |
| ~15 print-only scripts | wording (regex on unambiguous φ₋ mass statements only) | not re-run where print-only |

**Correct neighbours deliberately untouched:** the single-phase relative-mode
gap ω² = 2g (inertias 1, 1 — confirmed Part 156 S9) wherever it appears
(`mathematical_formalization.md` §5, tetrad/tensor-GW breathing-mode notes);
the φ₋ potential amplitude A = 2gΦ (e.g. `cp_violation_quantitative.py`).

**Docs:** ~25 research docs corrected in place (regex on φ₋ mass statements +
the headline numbers), banners added to Parts 113, 117, 119; equation_reference
rows 80.1, 94.10, 96.8, 113.7/113.7b, 117.14/117.16, 128.3 and the Part 62 row
updated; glossary updated. `falsifiable_predictions.md` updated with user
approval (2026-09-28): Eq F.12, hollow-shell range, horizon formula + 113.7b note, Eq F.22. **Deferred to 83h:** CLAUDE.md's
"m² = 2gΦ" key-equation line.

## 6. Analysis [SPECULATIVE]

Nothing qualitative about the reversed-Higgs picture changes. Two points
deserve a note: (1) the Part 113 "φ₋ = breathing mode at the horizon"
identification was supported by a numerical coincidence that is now gone —
the identification may still be right structurally, but it is no longer
numerically *confirmed*; (2) the T51 value φ_vac,req = 1.5525 rad sits
0.018 rad below π/2. That proximity is flagged, **not** interpreted: T51's
own reasoning (g_Λ and g_dyn differ by ~10¹²²) already establishes that
g_dyn is not the Λ coupling, independent of this number.

**Status:** 83j DONE. Falsifiable-prediction numbers corrected with user approval.
