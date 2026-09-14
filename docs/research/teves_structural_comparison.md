# Part 143 — TeVeS Structural Comparison [Scoping]

**Phase:** 143 (literature/structural comparison — no script, no Sudoku check;
matches T75's own "Low effort, not new math" scope)
**Date:** 2026-09-10
**Status:** DONE — scoping comparison complete, all three filed questions answered.
**Closes:** TODO_04.md T75

---

## 1. What TeVeS Actually Is

**Source:** Bekenstein, J.D. (2004), "Relativistic gravitation theory for the
MOND paradigm", *Phys. Rev. D* 70, 083509, astro-ph/0403694 (already cited
as reference [44] in the GW170817 paper read in full for T74,
`assets/pdfs/1710.06168v2.pdf`).

TeVeS (Tensor-Vector-Scalar gravity) is Bekenstein's relativistic
completion of MOND. Its field content, verified via WebSearch (not
asserted from memory):

- A dynamical metric g_μν (Einstein-Hilbert-like tensor sector).
- A **unit-norm, timelike vector field** A_μ — dynamically selects a
  preferred reference frame, breaking local Lorentz SO(3,1) invariance.
- Two scalar fields, one dynamical (a k-essence field with a nonstandard
  kinetic term that produces MOND's interpolation function in the
  weak-field limit), one non-dynamical.
- A **disformal transformation** relating the "Einstein" metric (which the
  vector and scalar couple to) and the "physical" metric ordinary matter
  couples to — this is the actual mechanism, not the vector field alone.

---

## 2. Q1 — What Does the Vector Field Buy TeVeS?

**Source:** WebSearch-verified (2026-09-10): the vector field's role
traces back to R.H. Sanders' earlier stratified scalar-tensor MOND
attempts, which Bekenstein incorporated specifically to fix **gravitational
lensing**. A pure scalar-tensor MOND completion under-predicts lensing
deflection by a factor of ~2 relative to what flat rotation curves would
imply; the vector field's disformal transformation between the "Einstein"
and "physical" metrics is what closes this gap (Bekenstein 2004; see also
Chiu et al. (2006), *ApJ* 636, 565, "Theoretical Aspects of Gravitational
Lensing in TeVeS"). Separately, the vector field's perturbations enhance
early-universe structure growth — stronger baryon infall into potential
wells, reducing (though not eliminating) the need for dark matter in
structure formation.

**Comparison to PDTP:** PDTP has **no vector (spin-1) field anywhere in
its Lagrangian** — already established, not a new finding here:

- T70/Part 140 classified PDTP's SU(3) octet χᵃ as **nonlinear-sigma-model
  scalars** (no gauge connection, no field-strength tensor), not real
  gauge bosons.
- `docs/research/polarization_analogy.md` (Part 28b) independently flagged
  this as the reason PDTP has no natural U(1) electromagnetic construction:
  a scalar field supports only longitudinal waves, not EM's transverse
  two-polarization structure — the same structural gap, reached from a
  completely different direction (an EM-analogy exercise, not a TeVeS
  comparison).

**Result:** TeVeS's vector field does two specific jobs PDTP's all-scalar
content structurally cannot do on its own — fix lensing via a disformal
metric relation, and provide a Lorentz-symmetry-breaking preferred frame
for enhanced structure growth. This is not a new gap discovered by this
comparison; it is the **same gap**, independently confirmed a third time
(T70's field-content classification, the polarization/EM analogy, and now
the TeVeS comparison all converge on: PDTP has no vector field, and every
place a vector field does real physical work in an established theory is
a place PDTP currently has nothing).

---

## 3. Q2 — Does PDTP Have Its Own MOND-Like Result?

**Yes, already on record — and already a documented negative.**
`docs/research/dark_matter_energy.md` Section 2.5, **Falsifiable
Prediction 9**:

> The two-phase biharmonic field equation ∇⁴Φ + 4g²Φ = source (Part 61)
> differs from Poisson's equation at length scales r ~ 1/(2g) ~ l_P. In
> principle, if the healing length L_heal were galaxy-scale, flat rotation
> curves would follow WITHOUT dark matter.
>
> **Current status (corrected 2026-09-14, T77):** L_heal ~ l_P (Planck
> scale) — ~54 orders of magnitude too small for galactic rotation curves.
>
> **Verdict: SPECULATIVE** — currently fails by roughly 54 orders of magnitude.

[Blockquote above reflects `dark_matter_energy.md`'s corrected text as of
2026-09-14 (T77) — this section originally quoted a stale "20 orders"
figure, caught and fixed while writing T77's Timeflow Gravity comparison,
which relied on this same result as a comparison point.]

This is PDTP's own structural analogue of MOND's phenomenology (a
modified-gravity screening length producing flat rotation curves without
particle dark matter) — and it is already known to fail by roughly 54
orders of magnitude, independent of anything found in this T75 comparison.

**Cross-check with T74 (2026-09-10, same day):** T74's φ₋ dispersion
calculation independently re-derived essentially the same screening
length via a completely different route (the massive Klein-Gordon
dispersion relation rather than the static biharmonic equation), finding
the evanescent decay length at Earth's own potential is
2.68×10⁴ × l_Planck — the same "stuck at Planck scale" conclusion,
confirmed twice by unrelated derivations. **PDTP has no live MOND
mechanism**, and this is now supported by two independent, mutually
consistent calculations rather than one.

---

## 4. Q3 — TeVeS's Post-GW170817 Status: A Lesson for T74's Framing

**Source:** WebSearch-verified (2026-09-10). Original TeVeS is
**ruled out** by GW170817's speed bound — confirmed directly in the paper
already read for T74 (`1710.06168v2.pdf`: "these observations... rule out
a whole class of modified theories of gravity designed to dispense with
the need for dark matter, called dark matter emulators. Examples include
Bekenstein's TeVeS theory").

"Generalized TeVeS" variants are sometimes described as surviving, but
this needs qualifying rather than repeating uncritically (correcting this
item's own original filing text, which said "some variants survive with a
decoupled GW sector" — too generous as stated): per Gravitational waves in
Einstein-æther and generalized TeVeS theory after GW170817 (arXiv:
1801.03382, 2018), the speed bound forces one of generalized TeVeS's
propagating modes to travel far faster than light, and generalized TeVeS
is excluded outright in the parameter region where no strong-coupling
problem exists; whether it survives at all depends on being pushed into
a narrow parameter region where strong-coupling pathologies would need to
be separately addressed. **Not a clean survival — a theory backed into an
increasingly small, awkward corner.**

**Lesson for T74:** this makes PDTP's own result (Section 2, T74/Part 142)
look structurally *better positioned* than TeVeS ever was, not merely
"also passing." TeVeS needed a purpose-built disformal transformation and
a separately-tuned vector kinetic term to survive lensing constraints even
*before* GW170817, and required retreating to a shrinking parameter corner
afterward. PDTP's tensor-sector `c_s = c` is a single pre-existing
identity, forced by an unrelated requirement (PPN γ=1) years before
GW170817 was ever relevant, with no tunable parameter involved at all. The
comparison is not "PDTP is like a survived TeVeS variant" — it is that
PDTP never had the kind of fine-tuning problem TeVeS's vector field
introduces in the first place, precisely *because* PDTP has no vector
field for GW170817 to have found a wrong propagation speed for.

---

## 5. Verdict and Status

**TODO_04.md T75 — RESOLVED (scoping comparison, no new derivation).**

1. TeVeS's vector field fixes lensing (disformal transformation) and
   enhances structure growth (Lorentz-breaking preferred frame) — two
   jobs PDTP's all-scalar content structurally cannot do, confirmed a
   third independent way (alongside T70 and `polarization_analogy.md`).
2. PDTP already has its own MOND-analogue attempt on record
   (Prediction 9), already known to fail by roughly 54 orders of
   magnitude (corrected 2026-09-14, T77, from a stale "20 orders"
   figure) — now corroborated by T74's independent re-derivation of the
   same screening scale via a different method.
3. TeVeS's post-GW170817 position is worse than this item's original
   filing text implied — corrected here. PDTP's clean, parameter-free
   tensor-sector pass (T74) is structurally stronger than anything TeVeS
   had even before GW170817.

**No new PDTP Original equations result from this Part** — it is a
literature/structural comparison, as scoped. No script, no Sudoku check
(nothing to substitute into 10+ established equations; the relevant
established results — T70, `polarization_analogy.md`, Prediction 9, T74 —
are all reused, not re-derived).

---

## 6. Sources

- **Source:** Bekenstein, J.D. (2004), "Relativistic gravitation theory
  for the MOND paradigm", *Phys. Rev. D* 70, 083509, astro-ph/0403694.
- **Source:** Chiu, M.-C. et al. (2006), "Theoretical Aspects of
  Gravitational Lensing in TeVeS", *Astrophysical Journal* 636, 565.
- **Source:** "Gravitational waves in Einstein-æther and generalized TeVeS
  theory after GW170817", arXiv:1801.03382 (2018) — post-GW170817 status
  of generalized TeVeS variants.
- **Source:** Boran, S., Desai, S., Kahya, E.O., and Woodard, R.P. (2018),
  arXiv:1710.06168v2 — TeVeS falsification statement, already read in full
  for T74.
- **Reused, not re-derived:** T70/Part 140 (χᵃ NLSM-scalar classification);
  `docs/research/polarization_analogy.md` Part 28b (PDTP's EM/vector-field
  gap); `docs/research/dark_matter_energy.md` Section 2.5 / Falsifiable
  Prediction 9 (PDTP's own MOND-analogue, ~54 orders too small, corrected
  2026-09-14/T77); T74/Part 142 (independent screening-length
  re-derivation, tensor-sector c_s=c).

---

*This document is part of the PDTP research series. See
[TODO_04.md](../../TODO_04.md) for the active roadmap.*
