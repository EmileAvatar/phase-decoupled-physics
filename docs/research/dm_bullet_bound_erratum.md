# Bullet Cluster Bound Unit-Conversion Erratum (Part 138)

**Method:** Consistency audit findings (T69, sub-point 1) — two independent
unit-conversion errors, both found by direct recomputation during a
routine audit rather than by chasing a suspected problem. The primary
finding (Sec 1-5) is a 1000x error in the Bullet Cluster bound constant,
used across three scripts and six documents since Part 89/96/118; a
second, unrelated finding (Sec 6) is a 1000x PeV-to-GeV conversion error
in a neutrino-detectability table (Part 89 Eq 89.21).
**Status:** [ESTABLISHED, unit conversion] — erratum, not new physics.
**Script:** the Bullet-bound fix is in `simulations/solver/sigma_m_erratum.py`,
`simulations/solver/condensate_layer_fcc.py`,
`simulations/solver/condensate_layer_optics.py` (all rerun, all Sudoku
suites unchanged at 100% PASS); the KM3 finding (Sec 6) is doc-only, no
backing script existed.
**Cross-checks:** Part 89, Part 96, Part 116, Part 118 (all cite the
Bullet Cluster margin corrected here)
**Date:** 2026-09-02

---

## Plain English Summary

While auditing `dark_matter_energy.md` for T69 (a routine consistency
check, not a new physics investigation), a specific number came under
scrutiny: "1 cm²/g = 10⁻⁴ m²/kg," used throughout the project as the
converted form of the Bullet Cluster's dark-matter self-interaction bound.
**That conversion is wrong — 1 cm²/g actually equals 10⁻¹ m²/kg (0.1
m²/kg), a factor of 1000 larger.** The error was baked into an actual
Python constant (not just a prose typo) in three separate scripts, dating
back to Part 89/96 and inherited by Part 118's own erratum script when it
was written. Every place the project has quoted a "44.3 orders of
magnitude" safety margin for PDTP's dark-matter self-interaction
prediction should read **47.3 orders**. **This changes no conclusion
anywhere** — PDTP's predicted value was always tens of orders of
magnitude below both the wrong bound and the correct one, so nothing
that depended on this number as a pass/fail test flips — but the specific
number itself was wrong everywhere it appeared, and is now fixed.

---

## 1. How This Was Found

T69's sub-point 1 asked for a consistency audit of `dark_matter_energy.md`
— reading the document end to end and verifying every computed number
traces correctly to its source. Line 219 of that document states:

```
sigma/m_DM < 1 cm^2/g = 10^-4 m^2/kg          (as originally written)
```

Manual unit conversion did not reproduce this figure, prompting a direct
SymPy check rather than either accepting the document's number or
asserting the discrepancy from memory alone.

## 2. The Correct Conversion [VERIFIED]

**Source:** Standard SI unit conversion, verified computationally rather
than asserted:

```python
from sympy.physics.units import convert_to, meter, kilogram, gram, centimeter
expr = (1 * centimeter**2) / (1 * gram)
convert_to(expr, [meter, kilogram]).simplify()
# -> meter**2/(10*kilogram)  =  0.1 m^2/kg
```

By hand: 1 cm = 10⁻² m, so 1 cm² = 10⁻⁴ m². 1 g = 10⁻³ kg. Therefore:

```
1 cm^2/g = (10^-4 m^2) / (10^-3 kg) = 10^(-4-(-3)) m^2/kg = 10^-1 m^2/kg = 0.1 m^2/kg   (1)
```

[VERIFIED, SymPy] **1 cm²/g = 0.1 m²/kg, not 10⁻⁴ m²/kg.** The
most likely origin of the error: converting the cm²→m² factor (10⁻⁴)
correctly, but then forgetting to also divide by the g→kg factor (10⁻³)
in the denominator — i.e., treating grams as if they were already
kilograms. That single missing step accounts for exactly the observed
1000x (= 10⁻³) discrepancy.

## 3. Where the Bug Lived

The wrong constant `1.0e-4` (labeled "= 1 cm²/g") appears, as an actual
Python value (not just prose), in:

| File | Context | Live comparison affected? |
|---|---|---|
| `sigma_m_erratum.py` | `BULLET_BOUND_M2KG = 1.0e-4` | **Yes** — feeds directly into `margin = log10(BULLET_BOUND_M2KG / som_new)`, the number quoted everywhere as "44.3 orders" |
| `condensate_layer_fcc.py` | `Bullet = 1.0e-4` | Yes, but PASS/FAIL outcome (`bullet_ok`) unaffected — PDTP's value is ~50+ orders below either constant |
| `condensate_layer_optics.py` | `sigma_per_m_bullet = 1.0e-4` | No — this test (S12) compares the same formula computed two ways using the same constant on both sides; the constant's correctness never entered the PASS/FAIL logic, only the displayed log10 estimate |

**`sigma_m_erratum.py` is the load-bearing case.** Every citation of
"44.3 orders" across the project traces back to this one script's output.

## 4. The Corrected Numbers [DERIVED, VERIFIED]

With `BULLET_BOUND_M2KG` corrected to `1.0e-1`, `sigma_m_erratum.py`
rerun end to end:

```
sigma/m (PDTP, n=1 Planck vortex) = 5.2e-49 m^2/kg    (unchanged -- not affected by this bug)
Bullet bound (corrected)          = 1.0e-1 m^2/kg     (was wrongly 1.0e-4)
margin = log10(1.0e-1 / 5.2e-49)  = 47.3 orders of magnitude   (was 44.3)
```

[VERIFIED] Sudoku re-run: `sigma_m_erratum.py` 7/7 PASS (unchanged count;
test T7's threshold "margin > 38 orders" is comfortably satisfied by
either 44.3 or 47.3). `condensate_layer_fcc.py` 12/12 PASS, combined with
Part 89's 12/12 for 24/24 total (unchanged). `condensate_layer_optics.py`
12/12 PASS (unchanged). **No test anywhere changes from PASS to FAIL or
vice versa.**

## 5. What Does and Does Not Change

**Changes:** every citation of "44.3 orders" (or "~44 orders") specifically
for the Bullet Cluster margin on PDTP's DM self-interaction cross-section
(Part 118's corrected sigma/m formula) becomes **47.3 orders**. This
appears in `dark_matter_energy.md` (4 places), `condensate_layer_optics.md`
(1 place), `dm_winding_selection.md` (2 places), `notes_mcond_lambda.md`
(1 place), `equation_reference.md` (Eq 118.3), and `TODO_04.md` (T45's
three sync locations) — all updated as part of this erratum.

**Does not change:**
- The PDTP prediction itself, sigma/m = 4πG²m_DM/v⁴ = 5.2×10⁻⁴⁹ m²/kg —
  this derivation (Part 118) is untouched; the bug was only in the
  comparison constant, never in PDTP's own formula or computed value.
- Any pass/fail verdict, anywhere — PDTP's value was always ~44-47 orders
  below the bound regardless of which (wrong or right) bound value was used.
- Parts 89, 96, 116's conclusions about dark matter being "automatically
  safe" against the Bullet Cluster constraint — still true, now by a
  slightly larger, correct margin.

## 6. Related Finding: KM3-230213A Neutrino Energy Ratio [Eq 138.2]

The same T69 audit pass, continuing past the Bullet-bound check, found a
second, unrelated unit-conversion error in the same document's Part 5
(neutrino detectability). `condensate_layer_optics.md`'s energy-ladder
table (Sec 89.21) states the ratio E/m_W for the record-breaking
KM3-230213A neutrino (220 PeV, KM3NeT Collaboration 2025) as **2737**.

**Recomputed from scratch:** 1 PeV = 10⁶ GeV (peta = 10¹⁵, giga = 10⁹,
ratio 10⁶). 220 PeV = 2.2×10⁸ GeV. m_W c² = 80.4 GeV.

```
E/m_W = 2.2e8 / 80.4 = 2.736e6                                            (2)
```

[VERIFIED, computed] The correct ratio is **2.7×10⁶, not 2737** — off by
almost exactly 1000x, the same signature as the Bullet-bound error, though
a different root cause (most likely 1 PeV mistakenly treated as 10³ GeV
instead of 10⁶ GeV — i.e. peta confused with tera). The SAME error, by the
same ~1000x factor, was also found in two neighboring rows of the same
table: the Glashow resonance (6.3 PeV, stated 78, correct 7.8×10⁴) and the
"previous record" neutrino (6.05 PeV, stated 75, correct 7.5×10⁴). All
three wrong rows are PeV-scale; the GeV and TeV rows in the same table
were already correct, confirming the error is specifically a PeV→GeV
conversion slip, not a general formula problem.

**No conclusion changes:** all three corrected ratios remain enormously
>> 1 (fully in the "propagating" regime), if anything more decisively than
the misstated smaller numbers suggested. Fixed in
`condensate_layer_optics.md` (table + Eq 89.21 prose) and
`dark_matter_energy.md` (Part 5 prose) — no backing Python script existed
for this doc-only table, so no code fix was needed here.

**Worth noting as a pattern:** this is the SECOND independent ~1000x
unit-conversion error found in the same file during the same audit pass
(the other being the Bullet-bound cm²/g→m²/kg conversion, Sec 1-5 above).
Both happen to be exactly 1000x, both sit at metric-prefix boundaries
(milli/kilo-scale for one, peta/giga-scale for the other), and neither
was caught by any prior Sudoku suite because neither affected a pass/fail
outcome — only a displayed magnitude. This suggests unit-prefix
conversions specifically (rather than the underlying physics formulas)
are a category worth extra scrutiny in any future audit, since they are
exactly the kind of error a PASS/FAIL-oriented Sudoku check is least
likely to catch on its own.

## 7. Verdict

[ESTABLISHED, corrected] Two genuine, previously-uncaught 1000x
unit-conversion errors, found by routine audit rather than by chasing a
suspected problem — exactly the value of the "consistency audit"
discipline T69 was scoped to apply. Consistent with the project's
existing practice (Part 118 itself was an erratum of Part 89): documented
plainly, fixed at the source, re-verified computationally, and every
downstream citation traced and corrected rather than left to drift
further. No physics conclusion in the project changes as a result.

---

## References

- `simulations/solver/sigma_m_erratum.py` — corrected script (Part 118's
  own erratum script; this Part corrects a bug introduced within it).
- `docs/research/dark_matter_energy.md` — Part 8 Update Log entry added.
- `docs/research/equation_reference.md` — Eq 138.1-138.2, Part 138 changelog entry.
- `docs/research/condensate_layer_optics.md` — energy-ladder table (Sec 6
  finding), Part 89 Eq 89.21 prose.
- Part 89, Part 96, Part 116, Part 118 — all cite the corrected margin.
- KM3NeT Collaboration (2025) — KM3-230213A, 220 PeV neutrino (Sec 6).

---

*End of Part 138 (T69 sub-point 1 finding).*
