# Part 152 — CKN "Factor 12" Formula Discrepancy Audit (Part 54)

**Phase:** 152 — `simulations/solver/t71_ckn_factor12_audit.py`
**Date:** 2026-09-27
**Status:** DONE. Discrepancy traced to its exact source and resolved;
"factor 12" survives (precise value 12.24). The underlying numbers and
code (`cosmo_constant.py`, `cosmo_constant_a3.py`, `cosmo_constant_v2.py`)
were already correct and mutually consistent — the bug was a units
conflation in `cosmological_constant_fcc.md`'s own prose, now fixed.
**Output log:** `simulations/solver/outputs/t71_ckn_factor12_audit_20260927.txt`
**Closes:** TODO_04.md T71

---

## 1. The Question

Two citations of the CKN (Cohen-Kaplan-Nelson) bound appeared, on a
quick read, not to match:

```
cosmological_constant_fcc.md (Part 54, Eq. 54.1): rho_CKN ~ hbar*c/(l_P^2*L_H^2)
equation_reference.md / the actual code:          rho_CKN = c^2/(G*L_H^2)
```

A quick hand-check substituting `l_P^2=ħG/c^3` into the first form did
not obviously reduce to the second — flagged in TODO_04.md rather than
chased down at the time, per this project's own tracking discipline.

---

## 2. What Was Actually Wrong (and What Wasn't)

**Traced to source, not assumed:** the discrepancy is real, but it is
**not** a numerical error anywhere the project's actual computations
happen. `cosmo_constant.py`, `cosmo_constant_a3.py`, and
`cosmo_constant_v2.py` all independently define
`RHO_CKN = C**2/(G*L_H**2)` and all compute the same `~7.1×10⁻²⁶ kg/m³`
— these were never wrong, and `equation_reference.md`'s citation of
that same formula and number was never wrong either.

**The actual bug** is in `cosmological_constant_fcc.md`'s own prose,
specifically Eq. 54.1:

```
rho_Lambda ~ rho_Planck x (l_P / L_H)^2     ... (54.1, as originally written)
           ~ hbar c / (l_P^2 x L_H^2)
```

This chains two expressions with "~" as though they were the same
quantity. They are not — **[VERIFIED, `verify_dimensional_mismatch()`]**:

```
dim[hbar*c/(l_P^2*L_H^2)] = {mass: 1, length: -1, time: -2}   = ENERGY density (J/m^3)
dim[c^2/(G*L_H^2)]        = {mass: 1, length: -3}              = MASS density (kg/m^3)
ratio of the two dimensions = {length: 2, time: -2}             = exactly c^2
```

**Why this happened:** `rho_Planck` is used in two different senses
across this project — as a **mass** density
(`rho_Planck = c⁵/(ħG²)`, the convention used everywhere else, e.g.
`cosmo_constant.py`) and, in this one line, implicitly as an **energy**
density (`ħc/l_P⁴ = rho_Planck_mass · c²`). `rho_Planck_mass·(l_P/L_H)²`
gives the correct mass density `c²/(G·L_H²)`; `rho_Planck_energy·(l_P/L_H)²`
gives `ħc/(l_P²L_H²)` — an energy density, off by exactly `c²`. Writing
both on one "~" chain silently conflated the two.

---

## 3. Verification

### 3.1 Dimensional Check (`sympy.physics.units`)

**[VERIFIED, S1–S3]** `hbar*c/(l_P²·L_H²)` has base dimensions
`{mass:1, length:-1, time:-2}`, matching `joule/meter³` exactly (energy
density). `c²/(G·L_H²)` has base dimensions `{mass:1, length:-3}`,
matching `kilogram/meter³` exactly (mass density). Their ratio's
dimensions, `{length:2, time:-2}`, match `c²` exactly.

### 3.2 Algebraic Reconciliation

**[VERIFIED, S4–S5]** Substituting the standard identity `l_P²=ħG/c³`:

```
hbar*c/(l_P^2*L_H^2) = c^4/(G*L_H^2)                    [residual 0, exact]
```

Dividing by `c²` (the standard energy-density → mass-density
conversion, `ρ_mass = ρ_energy/c²`):

```
c^4/(G*L_H^2) / c^2 = c^2/(G*L_H^2)                     [residual 0, exact]
```

**This exactly matches the code's own formula.** The two cited
expressions are not inconsistent — they are the energy-density and
mass-density versions of the same physical bound, related by the
standard, well-defined `c²` conversion that Part 54's prose never
stated explicitly.

### 3.3 The Code's Own Internal Identity, Checked for the First Time

**[VERIFIED, S6]** `cosmo_constant.py`'s own comment asserts
`rho_Planck·(l_P/L_H)² = c²/(G·L_H²)` (using the mass-density
`rho_Planck=c⁵/(ħG²)`) — never independently checked before this audit.
Confirmed exactly, residual 0.

### 3.4 Precise Numerical Recomputation

**[RECOMPUTED, S7–S9]**, using the same constants already established
elsewhere in the project (`sudoku_engine.py`, CODATA/Planck-2018-based):

```
L_H            = 1.372676e+26 m
rho_CKN        = 7.146601e-26 kg/m^3
rho_Lambda_obs = 5.840920e-27 kg/m^3
ratio          = 12.2354
```

Cross-checked via the independent `rho_Planck·(l_P/L_H)²` route:
agrees to 1 part in 10¹⁶ (floating-point precision, not a coincidence).
**"Factor 12" survives, and is now pinned down more precisely: 12.24,**
not merely re-cited from an earlier, less precisely stated figure.

### 3.5 What the Literal Misreading Would Have Given

**[COMPUTED, S10]**, for the record: if Part 54's prose formula were
taken completely at face value — computing `ħc/L_eff⁴` in plain SI
units and comparing it directly to `ρ_Λ` as if both were mass
densities — the resulting "ratio" would be `~1.10×10¹⁸`, not `~12`. This
confirms the two-formula confusion is exactly `c²` in size, precisely
the discrepancy this audit traced, not a separate or smaller error.

---

## 4. Sudoku Scorecard — 10/10 PASS

| # | Check | Result |
|---|-------|--------|
| S1 | `ħc/(l_P²L_H²)` has energy-density dimensions | PASS |
| S2 | `c²/(G·L_H²)` has mass-density dimensions | PASS |
| S3 | The two formulas differ by exactly `c²` dimensionally | PASS |
| S4 | Energy-density form reduces exactly to `c⁴/(G·L_H²)` | PASS |
| S5 | Dividing by `c²` reconciles exactly with the code's formula | PASS |
| S6 | Code's own `rho_Planck·(l_P/L_H)²=c²/(G·L_H²)` identity confirmed | PASS |
| S7 | Two independent routes to `rho_CKN` agree to <10⁻¹² | PASS |
| S8 | Recomputed `rho_CKN` matches the previously-cited 7.1×10⁻²⁶ kg/m³ | PASS |
| S9 | Ratio is within the previously-cited "~12" ballpark (12.24) | PASS |
| S10 | Literal misread ratio is exactly `c²` times too large | PASS |

No bugs found in this script itself on first run (RECHECK ran clean) —
one real bug *was* found in the target of the audit (§2), which is the
whole point of this exercise, and is fixed in §5.

---

## 5. Fix Applied

`cosmological_constant_fcc.md`'s Eq. 54.1 corrected to show both forms
explicitly, with the missing `c²` conversion stated rather than implied
— see that document's own Changelog note for the exact edit. No change
to any other document: `equation_reference.md`'s citation and every
`.py` script were already correct.

---

## 6. Verdict and Status

**TODO_04.md T71 — RESOLVED.**

1. The discrepancy was real (the two formulas are not dimensionally
   identical) but not a computational error — it was a units-labeling
   gap in one document's prose, now closed.
2. "Factor 12" survives verification, refined to **12.24** at full
   precision, cross-checked two independent ways to 1 part in 10¹⁶.
3. Every already-published number (`7.1×10⁻²⁶ kg/m³`, "factor 12" /
   "consistent with the geometric mean") stands as previously stated —
   nothing downstream needs correcting.
4. **Step 4 of this item's own filing** (whether qwen's Suggestion 4 —
   GHY boundary term + Padmanabhan bulk-surface equipartition — is
   worth its own task to explain the now-confirmed factor) is
   **deferred, not started**: this item's own scope was the
   dimensional-consistency check only; a decision on Suggestion 4 would
   be its own separate, planned item if pursued.

---

## 7. Sources

- **Reused, not re-derived:** Cohen, Kaplan, Nelson (1999), *Phys. Rev.
  Lett.* 82, 4971 (the CKN bound itself); Part 54
  (`cosmological_constant_fcc.md`) and its three supporting scripts
  (`cosmo_constant.py`, `cosmo_constant_a3.py`, `cosmo_constant_v2.py`);
  Planck Collaboration (2018), *A&A* 641, A6 (`Ω_Λ`, `H_0`).
- **PDTP Originals in this document:** none — this is a dimensional-
  consistency audit of an already-published result, not new physics.
  The `sympy.physics.units` verification method and the precise
  recomputed ratio (12.24, vs. the previously-cited unrefined "~12")
  are this Part's own contribution.

---

*This document is part of the PDTP research series. See
[TODO_04.md](../../TODO_04.md) for the active roadmap.*