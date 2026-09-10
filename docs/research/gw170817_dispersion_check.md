# Part 142 — GW170817 Constraint on PDTP's GW Structure

**Phase:** 142 — `simulations/solver/t74_gw170817_dispersion.py`
**Date:** 2026-09-10
**Status:** DONE — PASS (tensor sector, exact/by construction) + CONSTRUCTIVE
NEGATIVE (scalar sector, evanescent/undetectable). 11/12 Sudoku PASS, 1 honest N/A.
**Output log:** `simulations/solver/outputs/t74_gw170817_dispersion_20260910.txt`
**Closes:** TODO_04.md T74
**Byproduct:** found and fixed a ~22-orders-of-magnitude numerical erratum in
`two_phase_rederivation.md` (Part 63) Section S7, unrelated to but same genre
as T68 — see Section 5.

---

## 1. The Question

GW170817 (arXiv:1710.06168v2, Boran, Desai, Kahya & Woodard 2018, "GW170817
Falsifies Dark Matter Emulators" — real 2018 paper, already downloaded and
read in full) pinned gravitational-wave and gamma-ray arrival times together
to within 1.7 seconds after ~40 Mpc of travel, killing or severely
constraining an entire class of modified-gravity "dark matter emulator"
theories (including TeVeS, see T75) whose extra field content predicts GWs
propagating on a different metric/speed than photons.

**Does PDTP's own GW structure respect this?**

PDTP does not have a single GW-carrying object — it has **two structurally
distinct modes**, and they must be treated separately:

- **Tensor sector** (φ₊ / SU(3) emergent metric, Parts 75–76): the actual
  quadrupole strain signal LIGO detected and template-matched for GW170817.
- **Scalar/breathing sector** (φ₋, Parts 61–63/113): a *separate*,
  already-derived, **massive** mode — not what GW170817's timing measurement
  probes at all, but worth checking on its own terms.

---

## 2. Tensor Sector — PASS by Construction

### 2.1 Starting Point

`docs/research/condensate_microphysics.md`, Constraint 3, already
establishes:

```
c_s = c    (Lorentz-invariant condensate condition)          [ESTABLISHED, Part 3]
```

**Source:** required for the PPN parameter γ=1 (Schwarzschild recovery via
the acoustic metric) — a *design* constraint the condensate had to satisfy,
not a post-hoc observation. Re-verified unchanged in the two-phase extension:
`two_phase_rederivation.md` Sudoku check S8 computes `c_s/c = 1.0000000000`
(algebraic identity, any m_cond).

### 2.2 Computing GW170817's Own Bound (From Source Numbers, Not Memory)

Rather than quote a remembered "~10⁻¹⁵" figure, the bound is computed
directly here from the numbers in the downloaded paper itself (Section II:
merger time; Section III: Δt = 1.7 s; NGC 4993 distance = 40 Mpc, citing
Freedman et al. 2001):

```
d = 40 Mpc = 1.2343e24 m                                      [Eq. 142.1]
d/c = 4.1171e15 s                                              [Eq. 142.2]
|dv|/c ~ dt/(d/c) = 1.7 / 4.1171e15 = 4.13e-16                 [Eq. 142.3]
[COMPUTED — simplified order-of-magnitude version of the official
LIGO/Virgo+Fermi analysis, which additionally subtracts an astrophysical
merger-to-γ-ray-emission delay estimate to get an asymmetric bound; this
number is the same order of magnitude, shown transparently from this
project's own downloaded source rather than cited from memory.]
```

### 2.3 Result

**Result (142.4) [PDTP Original, numeric]:** PDTP's tensor-sector deviation
is **exactly 0** (algebraic identity), which is trivially inside the
computed empirical bound of 4.13×10⁻¹⁶ by construction — `c_s = c` was
required for PPN γ=1 from the start (Part 3), not tuned to satisfy
GW170817 after the fact. Worth stating with the actual number rather than
leaving as an unquantified assumption.

**Plain English:** PDTP's real gravitational-wave carrier already had to
travel at exactly light speed to match ordinary Newtonian/GR light-bending
tests, long before GW170817 existed. GW170817's extremely tight 1.7-second
bound is automatically satisfied — not because PDTP was built to dodge it,
but because the requirement that made PDTP match everyday gravity in the
first place is even stricter.

---

## 3. Scalar/Breathing Sector (φ₋) — Structurally Off-Target, and Undetectable

### 3.1 Why "Speed Bound" Is the Wrong Question for φ₋

`two_phase_rederivation.md` Section S7 already derives φ₋'s dispersion
relation:

```
omega^2 = c^2*k^2 + 2*g*Phi,   omega_gap^2 = 2*g*Phi              [Eq S7.5-S7.6, DERIVED]
```

where Φ is the **local, dimensionless** gravitational potential
(GM/(Rc²) — the doc's own definition). This is a genuine **massive**
Klein-Gordon dispersion, not a modified propagation speed for a massless
mode. GW170817's arrival-time measurement is of the tensor waveform LIGO
matched to standard templates; it says nothing directly about a separate,
undetected massive scalar mode. The right question is not "does φ₋ satisfy
the speed bound" but **"could φ₋ propagate as an observable oscillating
signal at LIGO frequencies at all, anywhere along the 40 Mpc path?"**

### 3.2 Derivation — Local Gap Frequency, Two Independent Routes

**Step 1.** Substitute T68's corrected bare coupling
`g_bare = omega_gap_Planck^2/c^2` (NOT `g = omega_gap` directly — that
identification was exactly T68's bug) into Eq S7.6, using Φ dimensionless:

```
omega_local^2 = 2*g_bare*Phi*c^2 = 2*omega_gap_Planck^2*Phi
omega_local = omega_gap_Planck * sqrt(2*Phi)                    [Eq 142.5, Route 1]
```

**Step 2 — independent cross-check**, following T68's own kappa route
(`t68_g_units_phi_minus_mass.py`): `kappa = sqrt(2*g_bare*Phi)` (a
wavenumber, 1/length), then `omega_local = c*kappa`:

```
omega_local = c*sqrt(2*(omega_gap_Planck^2/c^2)*Phi) = omega_gap_Planck*sqrt(2*Phi)
                                                                   [Eq 142.6, Route 2]
```

**SymPy: Route 1 − Route 2 = 0 exactly** (`derive_local_gap_frequency_
formula()`), confirming no error was reintroduced relative to T68's fix.

**Step 3 — dimensional check.** Φ is dimensionless by the doc's own
definition (Section 3.1), so `omega_gap_Planck * sqrt(Phi)` is (1/time) ×
(dimensionless) = 1/time exactly. **SymPy: verified** (`derive_dimensional_
check()`, tracked via a time-dimension placeholder symbol).

**Step 4 — cross-Part consistency.** At Earth's surface
(Φ_Earth = 6.96×10⁻¹⁰), `E_local = ħ*omega_local` evaluates to
**4.555×10¹⁴ GeV** — matching T68's independently-derived, already-published
`reversed_higgs.py` correction (`g_units_audit_scoping.md` Section 7b) to
better than 1%. This is not a coincidence: both routes trace to the same
T68-corrected `g_bare = omega_gap^2/c^2` identity, evaluated at the same
reference point, via genuinely different derivation paths (a potential-well
mass formula here vs. a field-equation reduction there).

### 3.3 Is φ₋ Detectable at LIGO Frequencies? No — By a Vast Margin

**Step 5.** Compare `omega_local(Earth)` to GW170817's observed frequency
sweep (24–500 Hz, Abbott et al. 2017 PRL 119, 161101):

```
omega_local(Earth) = 6.921e38 rad/s
omega_LIGO(24 Hz)  = 150.8 rad/s   -> ratio = 4.59e36
omega_LIGO(500 Hz) = 3142 rad/s    -> ratio = 2.20e35            [Eq 142.7, COMPUTED]
```

φ₋'s local mass gap is **35–36 orders of magnitude** above the entire
GW170817 observing band, even using Earth's own comparatively weak
gravitational potential as the reference point — not a marginal miss.

**Step 6 — evanescence.** When `omega_gap_local > omega`, the dispersion
relation gives an imaginary wavenumber: the mode does not propagate, it
decays exponentially with length scale `L_decay = c/omega_gap_local`:

```
L_decay(Earth) = c / omega_local(Earth) = 4.33e-31 m
L_decay(Earth) / l_Planck = 2.68e4                                [Eq 142.8, COMPUTED]
```

Consistent (same order-of-magnitude ballpark) with the project's existing
"L_heal ~ Planck length" biharmonic-screening characterization (Part 61) —
an independent cross-check via a completely different derivation route
(dispersion relation vs. static biharmonic equation) arriving at the same
qualitative conclusion.

**Step 7 — is there ANY realistic Φ small enough to avoid this?** Solving
Eq 142.7's threshold for the potential at which the mode stops being
evanescent at a LIGO frequency:

```
Phi/c^2 |_threshold = omega_LIGO^2 / (2*omega_gap_Planck^2)
  = 3.30e-83  (at 24 Hz)  to  1.43e-80  (at 500 Hz)               [Eq 142.9, COMPUTED]
```

Compare to a real, standard cosmological scale for how small Φ actually
gets even in the emptiest regions of the universe: the Sachs-Wolfe relation
between CMB temperature fluctuations and large-scale-structure potential
gives Φ/c² ~ 3×(ΔT/T) ~ 10⁻⁵ (Sachs, R.K. and Wolfe, A.M. (1967), *ApJ*
147, 73) — **77 orders of magnitude larger** than the threshold needed.

### 3.4 Result

**Result (142.10) [DERIVED, NEGATIVE]:** φ₋ is evanescent (cannot
propagate as an oscillating signal) at any GW170817-band frequency, for
**every physically realized gravitational potential in the universe**,
including the emptiest cosmic voids — not merely "very small," but
threshold-inaccessible by ~77 orders of magnitude. **There is no possible
φ₋ signal for GW170817 to have constrained** — the question of whether it
"satisfies" the speed bound is dissolved, not merely answered affirmatively.

**Plain English:** PDTP's extra "breathing" mode isn't just faint at the
frequencies LIGO listens at — it physically cannot exist as a traveling
wave there, anywhere in the real universe. It would need a region of space
with essentially *zero* gravitational influence from anything, ever, which
does not exist even in the emptiest cosmic voids. GW170817 didn't have
anything to say about this mode, one way or the other, because the mode was
never going to show up in that kind of measurement in the first place.

---

## 4. Sudoku Scorecard — 11/12 PASS, 1 Honest N/A

| # | Check | Computed | Expected | Result |
|---|-------|----------|----------|--------|
| S1 | c_s=c tensor-sector deviation exactly 0 | 0.0 | 0 (exact identity) | PASS |
| S2 | Computed GW170817 speed bound in sane range | 4.13e-16 | 1e-17 to 1e-13 | PASS |
| S3 | PDTP tensor deviation (0) << empirical bound | 0 vs 4.13e-16 | 0 < bound | PASS |
| S4 | Two independent ω_local(Φ) routes agree | residual 0 | 0 (exact) | PASS |
| S5 | E_local(Earth) matches T68's published figure | 4.555e14 GeV | ~4.5e14 GeV (±5%) | PASS |
| S6 | ω_local(Earth) >> LIGO band (24 Hz) | ratio 4.59e36 | > 1e30 | PASS |
| S7 | Decay length within few OoM of l_Planck | 2.68e4 × l_P | O(1)-O(6) × l_P | PASS |
| S8 | LSS potential (1e-5) vastly exceeds threshold | ratio 3.03e77 | >> 1 | PASS |
| S9 | Part 63's "G·m_P²/ħ" reduces to c (erratum confirmed) | True | True | PASS |
| S10 | Part 63's stated vs. correct ω_gap | 22.0 orders off | erratum, not P/F | N/A |
| S11 | ω_local formula dimensionally 1/T | 1/T | 1/T | PASS |
| S12 | Robust across full 24–500 Hz sweep | both >> 1e28 | both >> 1 | PASS |

All values read directly from `t74_gw170817_dispersion.py`'s returned
dicts (RECHECK compliance); see the output log for the full run.

---

## 5. Byproduct: Part 63 (`two_phase_rederivation.md`) S7 Erratum

While cross-checking against the doc's own "Numerical estimate on Earth's
surface" block, its stated `g_coupling ~ G*m_P²/ħ ~ 2.95×10⁴² rad/s` was
found to be wrong on inspection: **SymPy confirms** `G*m_P²/ħ` reduces
*identically* to `c` (not a frequency at all), via the definition
`G = ħc/m_cond²` (m_cond = m_P) — an algebraic tautology, not a meaningful
"g" value. The doc's resulting `omega_gap ~ 6.4×10¹⁶ rad/s` is consequently
**~22 orders of magnitude too small** (correct value: 6.92×10³⁸ rad/s,
Section 3.2). This is a distinct erratum from T68's bug (T68's checklist
did not audit this specific Part 63 section — see `g_units_audit_scoping.md`'s
9/9 checklist, none of whose items cover Section S7) but the same general
class of error (informal treatment of a coupling's units).

**Impact:** none of Part 63's 16/16 PASS verdicts change — Eq S7.5's
*symbolic* dispersion relation and the mass-term derivation (S7.1–S7.4,
SymPy-verified) are unaffected; only the illustrative numeric plug-in at
the end was wrong. Corrected directly in `two_phase_rederivation.md`
(2026-09-10), same treatment T68 gave `phi_minus_local_mass_and_crossover.md`'s
"~42 orders" erratum.

---

## 6. Independence Argument (Sudoku Rules 3–5, CLAUDE.md)

- U(1) single-phase sector: untouched — this Part only evaluates already-
  established two-phase (φ₋) and SU(3)-tensor (c_s=c) results, introduces
  no new coupling.
- Two-phase Lagrangian (Newton's 3rd law, Jeans eigenvalue): untouched —
  no new term added; Eq S7.1–S7.6 reused exactly as derived in Part 63.
- Part 114's χᵃ contact vertex / T73's Mechanism B (Planck-suppressed
  contact interaction): unrelated — this Part concerns φ₋'s own
  propagation, not the SU(3) octet's self-interaction.
- T68's g-units correction: reused, not re-litigated — both routes here
  build directly on `g_bare = omega_gap^2/c^2`, cross-verified to agree
  with T68's own published number.

---

## 7. Verdict and Status

**TODO_04.md T74 — RESOLVED: PASS (tensor sector) + CONSTRUCTIVE NEGATIVE
(scalar sector, undetectable-by-construction).**

1. **(142.4)** Tensor sector: c_s=c is exact, trivially satisfying
   GW170817's ~4×10⁻¹⁶ bound by a design requirement predating the
   observation itself.
2. **(142.10)** Scalar/breathing sector: evanescent at LIGO-band
   frequencies for every physically realized Φ in the universe (77 orders
   of margin even against the emptiest cosmic voids) — GW170817 could not
   have constrained this mode because it can never propagate there.
3. Byproduct: fixed a ~22-orders-of-magnitude numerical erratum in Part 63
   (Section 5), found only because this Part required redoing the
   calculation from first principles rather than reusing the existing
   number.

**Overall reading:** PDTP passes this real, external, historically theory-
killing constraint cleanly on both fronts — one trivially (by a
pre-existing design requirement), one because the extra mode PDTP predicts
is structurally incapable of being what such a measurement could probe.
Neither outcome required any new assumption or free parameter.

**What remains open:** whether φ₋'s coupling to a binary-neutron-star
SOURCE (as opposed to its propagation, addressed here) could produce any
other observable signature nearer the merger itself — not attempted here,
flagged as a possible future item, distinct from the propagation question
this Part answers.

---

## 8. Sources

- **Source:** Boran, S., Desai, S., Kahya, E.O., and Woodard, R.P. (2018),
  "GW170817 Falsifies Dark Matter Emulators", arXiv:1710.06168v2 — GW170817
  observation numbers (Δt=1.7s, d=40 Mpc) used directly in Section 2.2.
- **Source:** Abbott, B.P. et al. (LIGO Scientific, Virgo) (2017), "GW170817:
  Observation of Gravitational Waves from a Binary Neutron Star Inspiral",
  *Phys. Rev. Lett.* 119, 161101 — GW170817's observed 24–500 Hz frequency
  sweep, used in Section 3.3.
- **Source:** Sachs, R.K. and Wolfe, A.M. (1967), "Perturbations of a
  Cosmological Model and Angular Variations of the Microwave Background",
  *Astrophysical Journal* 147, 73 — Φ/c² ~ 10⁻⁵ large-scale-structure
  potential scale, Section 3.3.
- **Reused, not re-derived:** `condensate_microphysics.md` Constraint 3
  (c_s=c); `two_phase_rederivation.md` Eq S7.1–S7.6 (φ₋ dispersion); T68
  (`g_units_audit_scoping.md`, `t68_g_units_phi_minus_mass.py`) — bare
  coupling correction and Earth-surface cross-check value.
- **PDTP Originals in this document:** Eq. 142.3 (GW170817 speed bound,
  computed from source numbers), Eq. 142.5–142.8 (φ₋ local gap frequency
  and decay length reapplication), Eq. 142.9–142.10 (propagation
  threshold vs. LSS potential, negative result).

---

*This document is part of the PDTP research series. See
[TODO_04.md](../../TODO_04.md) for the active roadmap.*
