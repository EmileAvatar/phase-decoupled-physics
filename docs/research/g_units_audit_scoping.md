# g's Units Project-Wide — Audit Scoping Notes (T68)

**Status:** CHECKLIST COMPLETE (9/9) — see Section 7e. **Central question
of the whole audit RESOLVED**: Hypothesis 1 (a single project-wide
units-conversion slip -- reducing the covariant field equation
`box(phi)=g*sin(psi-phi)` to a pure-time equation while silently dropping
the `1/c^2` from `box`) confirmed across THREE independent chains: Part
62's local phi_- mass, Part 128's Lambda (g_Lambda), and Part
99/25/102/119's g_dyn. Not two distinct physical couplings after all --
one bug, found at its root each time. Concrete fixes: `[g] = 1/length^2`
(not `1/time^2`); `g_bare = (historical 1/time^2 value)/c^2`. One
numerical result corrected (phi_- local mass swing: 21.6 orders, not
~42; both endpoint numbers were already right, fixed at the source in
`phi_minus_local_mass_and_crossover.md`). No numbers change for g_Lambda
or g_dyn's own established uses (the mislabeling cancels in their ratio).
One downstream consequence flagged, not yet fixed: `falsifiable_
predictions.md` Eq F.12 needs its own plan-first update. One new,
narrower, separate question surfaced (Part 94's g=omega_gap vs Part 99's
implied g=omega_gap^2/2) and is filed as its own item, not folded into
T68. No new Part number assigned to this audit itself (per project
convention -- it's a units correction traced across many existing Parts,
not a new physics result of its own).
**Prerequisites:** Part 33 (`vortex_winding_derivation.md`), Part 94
(`coupling_constant_g.md`), Part 61/62 (two-phase Lagrangian, reversed
Higgs), Part 95 (`emergent_c.md`), Part 128/T51 (`lambda_locking_fossil.md`
Sec 11), Part 131 (`phi_minus_local_mass_and_crossover.md` Sec 7-9 — where
this was first flagged).
**Date:** 2026-09-06

---

## Plain English Summary

The project uses one symbol, "g", for the strength of the coupling between
matter and spacetime in the core Lagrangian. Different Parts, written
months apart, have been quietly assuming different *units* for g — some
treat it as a frequency (cycles per second), others derived, independently
and correctly for their own context, that it must be a frequency-*squared*
(one more power of "per second"). Applying the wrong one swings a real
physical prediction (the local mass of the phi_- field near Earth) by
tens of orders of magnitude. This note does not fix the problem — it
documents three specific things found while sizing it up, so the actual
fix is done carefully, one Part at a time, rather than guessed at. The
three findings: (1) there's a third possible explanation nobody had
written down yet — this might not be two different physical quantities
at all, but one quantity written inconsistently in two different unit
conventions (physicists' "natural units" vs. plain SI units), which would
change how this gets fixed; (2) some of the project's own consistency
checks (Sudoku tests) that currently say "PASS" for g-dependent formulas
turn out to be checking something narrower than we thought — they can
pass even when the units are wrong, because they check internal
algebra, not the actual physical number; (3) a specific claimed number
(a "~42 orders of magnitude" swing) doesn't reproduce under a first-pass
hand check, which is itself useful — it means this needs to be redone
properly with every unit tracked, not estimated.

---

## 1. The Problem (Recap)

Two conventions for the bare Lagrangian coupling `g` (as in
`L = g cos(psi - phi)`, `box(phi) = g sin(psi-phi)`) are both live in the
project:

- **Convention A (frequency, [g] = 1/s):** Parts 33, 94, and by extension
  61/62/96/113 identify `g = omega_gap = m_cond c^2/hbar` directly.
- **Convention B (1/s^2, one power more):** Part 128 (T51) derived,
  independently and from the field equation's own structure
  (`box(phi) = g sin(psi-phi)`, phi dimensionless), that `[g] = 1/s^2`.

Applying Convention B's fix to Part 62/131's phi_- local-mass formula
swings the Earth-surface prediction from ~105 eV to ~4.5e14 GeV.

---

## 2. Step 1 — Why a Blind Repo-Wide Search Doesn't Work

A grep for bare "g" across `docs/research/` returns 73 files. This is
almost entirely noise: "g" collides with gravitational acceleration,
the Gell-Mann-matrix index `g_i`, the metric `g_mu_nu`, and other unrelated
uses. **Lesson for the next pass:** do not re-run a blind grep; work
through the ~8 Parts T68 itself already named (33, 61, 62, 94, 96, 113,
117, 119, 128), one at a time, plus the two docs where the units question
was actually raised (`emergent_c.md` Result 7, `phi_minus_local_mass_and_
crossover.md` Sec 7). Section 7 below turns this into an explicit
checklist.

---

## 3. Finding 1 — A Third Candidate: Natural Units vs. SI, Not Two Physical Objects

`emergent_c.md` Result 7 (Part 61, written before Part 128/T51 existed)
already carries a caveat that neither T68's filing note nor the original
plan for this session had surfaced:

> "The dispersion formula uses g in the **natural-unit sense** (units
> [mass]^2). The Eq 4e value g = 1.86e43 rad/s (SI) gives a k_J that is
> an order-of-magnitude estimate. The exact value requires resolving the
> SI vs natural-unit normalization of g."

[FLAGGED, not yet verified] In natural units (hbar = c = 1), mass and
frequency share a dimension ("energy"), but **mass-squared does not**
share that dimension with a bare frequency — it is one power higher,
exactly matching Part 128's independent 1/s^2 finding. This raises a real
possibility that Convention A and Convention B are not two different
*physical* couplings at all, but **one physical coupling, correctly
identified in natural units as having dimension [mass]^2, that has been
silently converted to SI (as `g = omega_gap`, dimension 1/s) in some
Parts without carrying through the extra power** — i.e. a units-
conversion slip rather than a conflation of two distinct objects.

This matters for how T68 eventually resolves: if this hypothesis holds,
the fix is a **single, consistent SI-conversion factor** applied
project-wide (not a decision about which of two different physical
quantities each formula "really" wants), and Part 119/T51's own
`g_dyn != g_Lambda` finding (already on record, 122 orders apart) would
need to be re-examined under the same lens rather than taken as proof
of two genuinely separate couplings.

**Not yet checked:** whether this hypothesis actually reconciles the
numbers (does the natural-units-to-SI conversion factor, applied
correctly, turn Convention A's value into Convention B's, or are they
still inconsistent after accounting for it?). This requires redoing the
natural-units derivation of `box(phi) = g sin(psi-phi)` explicitly with
hbar and c restored, side by side with Part 94's SI derivation of
`g = omega_gap`, and comparing term by term.

---

## 4. Finding 2 — A Sudoku Blind Spot

Part 131's own Sudoku scorecard (`phi_minus_local_mass_and_crossover.md`
Sec 8) includes:

> S9: `m^2(Delta_+) = 2g sin(Delta_+)` exactly — **PASS**

[OBSERVED] This test passes regardless of which numerical convention is
substituted for `g`, because it verifies that the mass-squared formula
matches an independently re-derived series expansion of the *same*
potential — an internal algebraic consistency check, not a check against
an external, absolutely-dimensioned physical quantity. **A units bug of
exactly this kind (a formula that is internally self-consistent but
uses the wrong absolute units for one symbol) is invisible to this class
of test by construction.**

**Implication for the audit:** every existing "PASS" cited as evidence
for a g-dependent formula needs to be re-read to check *what kind* of
consistency it actually verifies (internal/relative vs. external/
absolute) before it can be used as evidence that a given Part's "g" is
correctly dimensioned. This is a general methodological note, not
specific to Part 131 — worth checking whether it applies to other
g-dependent Sudoku suites too (Parts 61, 96, 113, 117, 119) as each is
audited.

---

## 5. Finding 3 — The "~42 Orders of Magnitude" Figure Doesn't Reproduce on a First Check

[FLAGGED, not yet resolved] `phi_minus_local_mass_and_crossover.md` Sec 7
states that applying Convention B moves the Earth-surface phi_- mass
prediction from ~105 eV to ~4.5e14 GeV — described as "a ~42 order-of-
magnitude swing." A first-pass hand check, assuming only `m^2 = 2*g*Phi`
with `g -> omega_gap^2` replacing `g -> omega_gap` (holding Phi fixed),
gives:

```
m_new / m_old = sqrt(omega_gap^2 / omega_gap) = sqrt(omega_gap) ~ sqrt(1.86e43) ~ 4.3e21
```

That is a swing of ~21-22 orders of magnitude in mass, not ~42. Converting
the units (105 eV vs 4.5e14 GeV = 4.5e23 eV) gives a stated ratio of
~4.3e21 as well when computed directly from the two endpoint numbers —
so the **arithmetic between the two endpoint numbers is internally
consistent with a ~21-22 order swing, not the ~42 stated in the prose**.
[COMPUTED, first-pass only — not yet reconciled against the original
Part 131 calculation, which may rescale more than one factor (e.g. Phi
itself, or a different exponent) and could legitimately produce a larger
number; this is flagged as a discrepancy to resolve, not asserted as an
error in either direction.]

**Action for the audit:** when Part 131's Sec 6 formula is revisited,
redo this specific swing calculation from scratch with every substitution
shown, rather than carrying the "~42 orders" figure forward uncritically.

---

## 6. Three Candidate Hypotheses (Stated Explicitly, None Yet Selected)

1. **Global units-conversion slip** (Section 3): one physical coupling,
   dimension [mass]^2 in natural units; some Parts correctly converted to
   SI (1/s^2), others incorrectly substituted the SI frequency `omega_gap`
   (1/s) directly. Fix: a single, consistent conversion applied everywhere
   Convention A currently appears.
2. **Two genuinely distinct physical couplings sharing one symbol**
   (T68's original framing, echoed by Part 119/T51's separately-established
   `g_dyn != g_Lambda`, 122 orders apart): local/static formulas need one
   object, cosmological/dynamical formulas need a structurally different
   one, and "g" has been the wrong shared label for both. Fix: a formal
   symbol split (template: `g_Lambda` vs `g_dyn`, already on record from
   T51), with `term_glossary.md` updated to carry both.
3. **A single formula-specific error**, not a project-wide pattern: only
   Part 62/131's phi_- mass formula has the wrong power of g, and Parts
   33/94/96/113's own uses of `g = omega_gap` are each independently
   correct in their own context (i.e. Part 128's 1/s^2 result applies
   narrowly to the field-equation route, not universally). Fix: correct
   Part 62/131 alone; leave the rest.

**These are not mutually exclusive at the level of individual Parts** —
the resolution could turn out to be hypothesis 1 for some Parts and
hypothesis 3 for others. The per-Part checklist in Section 7 is designed
to distinguish them.

---

## 7. Proposed Checklist for the Careful, One-at-a-Time Audit

For each Part below: (a) write out the exact equation using `g`, in full,
with every symbol's declared units; (b) determine what `[g]` the equation
requires for dimensional closure, showing the algebra; (c) note whether
the Part's own text declares a unit convention (SI vs natural units)
explicitly, or is silent; (d) classify the finding against the three
hypotheses in Section 6; (e) note whether existing Sudoku checks for
that Part would have caught a units error of this kind (per Section 4's
blind-spot finding) or not.

- [x] **Part 33** (`vortex_winding_derivation.md`) — CLEAR: no bare "g" used;
  `G = hbar*c/m_cond^2` has zero dependence on g; immune to this audit's outcome.
- [x] **Part 94** (`coupling_constant_g.md`) — internally consistent GIVEN
  its own premise (`g = omega_gap`); that premise is superseded by the
  Part 95/128 finding below, not confirmed.
- [x] **Part 61/62** (`reversed_higgs.py`) — **RESOLVED, same bug as Part
  128**: corrected formula `E_rest = hbar*omega_gap*sqrt(2*Phi)`, exactly
  `sqrt(omega_gap) ~ 4.3e21` larger than the code's original ~105 eV, giving
  ~4.5e14 GeV at Earth's surface (matches the number already on record;
  only the "~42 orders" swing label was wrong -- actual: 21.6 orders).
  SymPy-verified: `t68_g_units_phi_minus_mass.py`. See Section 7b.
  **Downstream consequence flagged, not fixed**: falsifiable_predictions.md
  Eq F.12 (hollow-shell test) needs updating once the full checklist closes.
- [x] **Part 95/128** (`emergent_c.md` Result 7; `lambda_locking_fossil.md`
  Sec 11) — **RESOLVED, corrected**: `[g] = 1/length^2` (SI), not `1/time^2`
  as Part 128 stated. `g = omega_gap^2/c^2`, not `omega_gap^2` alone.
  Part 128's own Lambda_obs match (1.000000, 12/12 Sudoku) is UNAFFECTED --
  its working formula already carries the missing `/c^2` explicitly,
  elsewhere in its structure. SymPy-verified:
  `simulations/solver/t68_g_units_field_equation.py`. See Section 7a.
- [x] **Part 96** (`condensate_layer_optics.md`) — **CLEAR**: standard
  Part 94 dispersion identity; the speculative local-mass formula reuses
  Part 62's, same fix, no new mechanism. See Section 7e.
- [x] **Part 113** (`two_phase_tan.md`) — **CLEAR for T68's own question**
  (reuses Part 99's g, already-resolved bug); surfaced a SEPARATE,
  narrower question (Part 94's g=omega_gap vs Part 99's implied
  g=omega_gap^2/2 -- can't both hold generally), filed separately, not
  part of T68's scope. See Section 7e.
- [x] **Part 117** (`phi_minus_quartic.md`) — **CLEAR**: stays symbolic
  throughout, never substitutes a numeric g; independently confirms
  `[g]=1/length^2` via `kbar^2=2g` (kbar a genuine wavenumber). No fix
  needed. See Section 7c.
- [x] **Part 119** (`lambda_locking_fossil.md`) — **RESOLVED**: g_dyn
  traces to the SAME field equation and the SAME missing-c^2 reduction
  bug (found at its root in Part 99's Eq 99.1). g_dyn = c^2 x (bare
  coupling for phi_-'s present-epoch dynamics) -- Hypothesis 1 confirmed
  again. g_dyn's own numerical value and Part 119's EOS/freeze results
  are UNCHANGED (calibrated self-consistently against real DESI data).
  T51's g_Lambda != g_dyn finding is UNAFFECTED (shared mislabeling
  cancels in the ratio). See Section 7d.
- [x] ~~Part 128/T51 (re-verify the 1/s^2 anchor)~~ — folded into "Part
  95/128" above; already resolved there, listed twice in the original draft.
- [x] **Part 131** (`phi_minus_local_mass_and_crossover.md` Sec 6-9) —
  **DONE**: "~42 orders" corrected to 21.6 at the source (Sec 7 of that
  doc), pointer added to Sections 7a-7b here. Endpoint numbers unchanged.

**CHECKLIST COMPLETE: 9/9.** T68's own scope (resolve g's units, 1/s vs
1/s^2) is answered: neither is exactly right -- the correct SI dimension
is 1/length^2. One global bug (Hypothesis 1) confirmed across 3
independent chains, concrete fixes applied, no numerical result
invalidated (only one mislabeled swing figure corrected, and one
downstream falsifiable-prediction consequence flagged for its own future
pass). One new, narrower question (Part 94 vs Part 99's omega_gap
identity, Section 7e) surfaced during the audit and is filed separately.

Recommended order: Part 33 -> Part 94 -> Part 95 (settles Finding 1) ->
Part 61/62 -> Part 117 -> Part 119/128 (settles hypothesis 2 vs 1 for the
cosmological sector) -> Part 96/113 -> Part 131 (redo the swing last, once
every input to it is settled).

**Progress (2026-09-06):** Parts 33, 94, 95/128 done -- see Section 7a.
Hypothesis 1 (units-conversion slip, not two distinct couplings) CONFIRMED
for the cosmological sector (g_Lambda). Part 61/62 done -- see Section 7b:
SAME bug, fixed, endpoint numbers reconciled (105 eV / 4.5e14 GeV both
correct; "~42 orders" swing corrected to 21.6). Downstream consequence
flagged for falsifiable_predictions.md Eq F.12, not yet fixed. Part 117
done -- see Section 7c: CLEAR, no bug, independently confirms
[g]=1/length^2. Part 119/128's g_dyn done -- see Section 7d: SAME bug,
traced to its root in Part 99's Eq 99.1 (identical missing-c^2 field-
equation reduction). Central audit question RESOLVED: one global bug
(Hypothesis 1), not two distinct couplings. Remaining: Parts 96, 113,
131 (confirmatory/cleanup expected).

---

## 7a. Update (2026-09-06, same session) — Parts 33/94/95/128 Checked

Per the checklist order in Section 7, Parts 33, 94, and 95/128 were worked
through. This is no longer purely scoping for these three -- a concrete,
SymPy-verified finding came out of it.

### Part 33 — CLEAR, no dependency

Part 33's own derivation (`vortex_winding_derivation.md`) never uses the
bare Lagrangian coupling "g" -- only `omega_gap = m_cond*c^2/hbar` (a
well-defined, unambiguous frequency, from E=hbar*omega) and the vortex
winding chain `n -> a_0 -> G = hbar*c/m_cond^2`. **`G = hbar*c/m_cond^2`
contains no g at all.** [CONFIRMED, inspection] T68's own concern ("does
Part 33's central result survive?") is answered: it cannot be affected by
however the g-units question resolves, because it never depended on g in
the first place. Checked off.

### Part 94 — self-consistent, but its premise is exactly what's in question

Part 94 (`coupling_constant_g.md`) asserts `g = omega_gap = m_cond*c^2/hbar`
(Eq 94.1, citing Part 34) and derives `g = sqrt(c^5/(hbar*G)) = omega_P`
to machine precision from that premise. The algebra is correct and not in
doubt. **But the premise itself -- that the bare Lagrangian coupling g
literally equals the frequency omega_gap -- is asserted, not derived from
the field equation**, and Section 7b below shows it needs revision.
Checked off as "internally consistent given its assumption"; the
assumption itself is superseded, not confirmed.

### Part 95/128 — MAJOR FINDING: Part 128's own dimensional derivation has an unverified step

[DERIVED, SymPy-verified: `simulations/solver/t68_g_units_field_equation.py`]
Redid Part 128's field-equation dimensional analysis from scratch, in full
SI (kg, m, s as independent base dimensions, not assuming c=1 anywhere),
using the standard relativistic wave operator
`box = (1/c^2) d^2/dt^2 - Laplacian` and verifying BOTH terms' dimensions
independently rather than asserting they match:

```
[(1/c^2) d^2phi/dt^2] = (s^2/m^2) * (1/s^2) = 1/m^2        (both terms
[Laplacian phi]       = 1/m^2                                agree: 1/m^2)
=> [box(phi)] = 1/m^2 = 1/length^2   (NOT 1/time^2)
=> [g] = [box(phi)]/[sin(...)] = 1/length^2
```

**This does not match Part 128's own stated result.** Section 11.2 of
`lambda_locking_fossil.md` writes:

> `[box(phi)] = [d^2/dt^2] = 1/s^2   (c already folds space into time)`

This line only computes the *time* term and asserts, via the parenthetical
"(c already folds space into time)," that the spatial term matches without
showing the 1/c^2 bookkeeping. The independent re-derivation above shows
this parenthetical is where the discrepancy actually lives: done in full
SI, `box(phi)` comes out as **1/length^2, not 1/time^2**. Part 128's own
Section 11.3 correctly computes `[omega_gap] = 1/s`, then concludes
`[omega_gap^2] = 1/s^2` "matches" the (incorrectly derived) 1/s^2
requirement. In fact:

```
[omega_gap^2]        = 1/time^2     -- does NOT match 1/length^2 (SymPy: False)
[omega_gap^2 / c^2]  = 1/length^2   -- DOES match exactly (SymPy: True)
```

**Corrected result:** `[g] = 1/length^2` (SI), and `g = omega_gap^2/c^2`
is the dimensionally-correct identification -- not `g = omega_gap^2` alone
as Part 128/T51 stated. This resolves Finding 1 (Section 3): it is
**hypothesis 1 (Section 6)**, a units-conversion slip, not hypothesis 2
(two genuinely distinct physical couplings) -- confirmed, not just
suspected.

### Why Part 128's own Sudoku (12/12) and Lambda_obs match (1.000000) were NOT caught by this bug

Part 128's *working formula* for the cosmological constant already
contains an explicit `/c^2`:

```
Lambda = g_Lambda * phi_minus_vac^2 / c^2,   g_Lambda = 3*Omega_Lambda*omega_gap^2
```

Substituting `g_Lambda = 3*Omega_L*omega_gap^2` into this formula and
dividing by c^2 supplies, by coincidence of where the division was placed,
**exactly the missing c^2 factor** identified above. So T51's own
numerical result (Lambda_obs matched to 1.000000, 12/12 Sudoku) is
**correct and unaffected** -- the bug is in the general *label* attached
to "[g]" (stated as 1/time^2, should be 1/length^2), not in the specific
Lambda formula, which happens to already carry the compensating /c^2
in the right place. **This is exactly Finding 2's Sudoku-blind-spot
pattern (Section 4), now confirmed with a specific mechanism**: the
formula's own internal structure was right for reasons independent of
whether the "[g]" units label attached to it was correct.

**Consequence for the rest of the checklist:** any OTHER formula that uses
bare "g" WITHOUT its own explicit "/c^2" (Part 62/131's `m^2 = 2*g*Phi` is
the prime suspect -- there is no visible /c^2 in that formula as stated)
is a live candidate for the same missing-factor bug, and should be checked
for exactly this pattern first, before anything else.

---

## 7b. Update (2026-09-06, same pass) — Part 61/62 CONFIRMED as the Bug, Fixed, and Reconciled

[DERIVED, SymPy-verified: `simulations/solver/t68_g_units_phi_minus_mass.py`]
Traced the bug to its exact line in `reversed_higgs.py` (Part 62):

```
# For g = omega_P (Planck frequency) and Phi = G*M/(r*c^2):
# omega^2 = 2 * omega_P * Phi                    <- as literally coded
# m_eff = hbar * omega / c^2
omega = np.sqrt(2.0 * OMEGA_P * Phi)
m_eV = HBAR * omega / EV_J
```

This treats `OMEGA_P` (= ω_gap = m_P·c²/ħ, units 1/s, Part 94's value) as
if it already carried the units `g` needs, then takes `sqrt(2·OMEGA_P·Φ)`
and calls the result an angular frequency — but `2·OMEGA_P·Φ` has units
1/s (Φ dimensionless), so its square root has units of 1/√s, not 1/s.
**This is the identical bug found in Part 128 (Section 7a), now located
in a second, independent formula built from the same underlying `g`.**

**Corrected derivation**, using Section 7a's result that `[g] = 1/length^2`
(the SAME `g` as the field equation, since both come from the SAME
Lagrangian `L = g·cos(ψ−φ)` — this is not a coincidence, it is the same
symbol):

```
kappa^2 = 2*g*Phi = 2*(omega_gap^2/c^2)*Phi     [kappa = 1/length, reduced
                                                  Compton wavenumber]
E_rest  = hbar*c*kappa                          [NOT hbar*omega directly --
                                                  kappa isn't a frequency]
        = hbar * omega_gap * sqrt(2*Phi)         [c cancels algebraically]
```

**SymPy-verified exactly:** `E_correct / E_code = sqrt(omega_gap)`,
residual = 0 (symbolic, no approximation). Numerically, at Earth's
surface: `E_code = 105.8 eV` (matches the original "~105 eV" citation),
`E_correct = 4.56e14 GeV` (matches the "~4.5e14 GeV" citation already on
record) — **both endpoint numbers already in the project were right; only
the swing between them was mislabeled.**

**Correcting Finding 3 (Section 5):** the actual swing is
`log10(sqrt(omega_gap)) = 21.63 orders of magnitude`, not the "~42 orders"
stated in `phi_minus_local_mass_and_crossover.md` Sec 7. (42 ≈ 2×21 is a
plausible root cause -- consistent with computing the swing in *m²* terms,
which scales as `omega_gap` directly, ~43 orders, and mislabeling it as
the swing in *m*, which scales as `sqrt(omega_gap)`.) **This closes
Finding 3 -- it was a downstream symptom of the same bug found in Section
7a, not a separate, unresolved arithmetic error.**

**Independent sanity check:** `E_correct ~ E_Planck * sqrt(2*Phi_earth) ~
1.22e19 GeV * 3.7e-5 ~ 4.5e14 GeV` — matches via a completely different
route (direct Planck-energy scaling), independent confirmation the
corrected formula is right.

**Consequence flagged, not yet acted on:** `falsifiable_predictions.md`
Eq. F.12 (the hollow-shell test, `m_phi(inside) = sqrt(2*g*Phi)`) is
built on this exact formula. With the corrected mass ~21.6 orders heavier
than originally stated, the predicted Yukawa range collapses from a
sub-mm, laboratory-testable scale to something far too short to detect
with any known method — changing this from "clean, decisive, testable
with existing technology" to likely untestable. **Not fixed here** —
CLAUDE.md requires a plan-first pass before editing
`falsifiable_predictions.md`, and the fix should wait until the rest of
this checklist (Parts 96, 113, 119/128's g_dyn, and Part 131's own
downstream NS comparison) is settled, so the prediction is updated once,
correctly, rather than patched repeatedly as the audit continues.

**Checklist item closed:** Part 61/62 -- RESOLVED, same root cause as
Part 128, now fixed with an exact corrected formula.

---

## 7c. Update (2026-09-06, same pass) — Part 117 CLEAR; Part 119/128's g_dyn Opens a New, Different Question

### Part 117 — CLEAR, no bug, a nice confirming cross-check

`phi_minus_quartic.md`'s entire derivation (V(eta,phi_-) = -2g·sin(pi/2-
beta+eta)·sin(phi_-), Eq 117.9, through the induced quartic lambda_4 =
2g^2 sin^2(beta)/(3 kbar^2), Eq 117.16) stays **entirely symbolic/ratio-
based** -- it never substitutes a numeric SI value for g via omega_gap,
so it never had the opportunity to introduce the OMEGA_P-as-g bug found
in Sections 7a-7b. Better still, it independently **identifies kbar^2 = 2g
(the two-phase gap scale)**, where kbar is explicitly "a mode of momentum"
(a genuine spatial wavenumber, 1/length) from the phi_+ kinetic gradient
term -- i.e. `[kbar^2] = 1/length^2`, matching `[g] = 1/length^2` from
Section 7a **without any correction needed**. This is a real, independent
confirmation that [g]=1/length^2 is the right general answer, found by a
Part that never numerically applied the SI value and so was never at risk
of the bug. Part 117's own Section 6.1 explicitly defers the *absolute*
numerical application to "the cosmological g" (i.e. Part 119's g_dyn,
next) -- correctly recognizing this itself as a separate, undone step.
**Checklist item closed: no fix needed.**

### Part 119/128's g_dyn — a DIFFERENT, harder question than expected

Checking `g_dyn = 9*H0^2*eps_0/2` (Eq T51.3, `lambda_locking_fossil.md`
Sec 11.6) against the Section 7a correction raised something new: g_dyn
is built entirely from `H` (the Hubble RATE, genuinely 1/time) via
`eps = 2g/(9H^2)` [Part 25 + Part 99], and is always compared directly
against H itself (e.g. the freeze condition `m < H` iff `eps < 1/9`,
Eq 119.2/T46.12) -- a completely standard, self-consistent "is this field's
oscillation rate faster or slower than the Hubble rate" comparison, always
staying in 1/time units throughout, never mixing in a literal spatial
wavenumber the way Parts 62/117/128 do.

**This raises a real question Section 7a/7b did not settle:** is g_dyn
actually the SAME "g" as the bare Lagrangian coupling (in which case it
too needs the `/c^2` correction, hypothesis 1), or is it an independently
-motivated, self-consistently-1/time^2-dimensioned rate-scale from Part
25/99's own construction that only shares the bare letter "g" by
unfortunate naming (hypothesis 2 -- exactly what T51 Section 11.7 already
concluded for g_Lambda vs g_dyn specifically, on different grounds)?

**Not yet resolved.** A first attempt to trace this to Part 25's original
derivation (`loss_tangent_dark_energy.md`) did not turn up a clean
first-principles derivation of "g" in that file within this pass -- only
downstream usages. **Needs a dedicated read of Part 25 and Part 99
(`tan_critical_point.md`) to see whether their "g" is derived FROM the
bare Lagrangian coupling (needs correction) or introduced independently
as its own rate-scale (does not).** This is now the single most important
open sub-question in the whole audit, since it decides whether g_dyn
needs the same fix as g_Lambda and Part 62, or is legitimately exempt.

**Checklist item:** Part 119/128 (g_dyn) -- IN PROGRESS, not resolved;
narrowed to a specific, answerable question about Part 25/99's origin.

---

## 7d. Update (2026-09-06, same pass) — g_dyn's Origin Found: SAME Bug, Traced to Its Root

Read Part 99's own derivation directly (`loss_tangent_dark_energy.md` Sec
2.1, citing Part 99 `tan_critical_point.md`). It starts from **the exact
same field equations already analyzed in Section 7a**:

```
box(phi) = g sin(psi - phi)           (A)   [same g, same equation]
box(psi) = -g sin(psi - phi)          (B)
```

Subtracting and reducing to a homogeneous mode Delta(t) = psi - phi gives
Eq 99.1: `d^2Delta/dt^2 = -2g sin(Delta)`. **This is where the bug enters,
at the root of the whole g_dyn chain** -- not a different quantity, the
identical mechanism as Section 7a.

**SymPy check** (reducing box(Delta) for a spatially homogeneous mode,
so the Laplacian term vanishes and only `(1/c^2) d^2Delta/dt^2` survives):

```
(1/c^2) d^2Delta/dt^2 = -2*g*sin(Delta)     [correct, keeping c^2]
=> d^2Delta/dt^2 = -2*c^2*g*sin(Delta)      [SymPy: verified]
```

Part 99 (Eq 99.1) wrote `d^2Delta/dt^2 = -2g*sin(Delta)` -- **missing the
same c^2 factor as Part 128's box(phi) reduction (Section 7a), at the
same step (reducing box to a pure-time equation).** This "g" then
propagates unchanged through Part 25's slow-roll ε (Eq 102.1,
`eps = g(1+cos(Delta))/(9H^2)`), Part 102's DESI inversion, and Part
119/T51's `g_dyn = 9*H0^2*eps_0/2` -- **confirming Hypothesis 1 (a single
global units slip, not two distinct physical couplings) for the g_dyn
chain too.**

### Why this does NOT mean g_dyn's own number is wrong for its own purpose

`eps = g(1+cos(Delta))/(9H^2)` must be dimensionless (it feeds directly
into `w = (eps-1)/(eps+1)`), which REQUIRES `[g] = [H^2] = 1/time^2` in
this formula, structurally -- regardless of what the bare Lagrangian
coupling's own dimension is. Since g_dyn was calibrated by fitting THIS
formula to real DESI data (w_0 = -0.827), its numerical value
(2.03e-36 s^-2) is exactly what makes that fit work, and stays correct
**for computing ε, w(z), and the freeze condition** -- nothing in Part
119's own internal results (m/H = 3*sqrt(eps), freeze eps<1/9, etc.)
needs correcting.

**What the finding actually means:** g_dyn (like g_Λ) is really
`c^2 * g_bare` for whatever bare coupling governs phi_-'s present-epoch
dynamics -- it was never literally the same object as the field
equation's bare g (dimension 1/length^2), even though it was written
using the same bare symbol. **T51's own g_Lambda != g_dyn finding
(ratio 3.477e+122) is UNAFFECTED**: both g_Lambda and g_dyn carry the
identical missing-c^2 mislabeling (same power, same context of
derivation), so the erroneous factor **cancels exactly in their ratio**
-- confirmed by inspection (both are "c^2 x bare-coupling-for-their-own-
context", and the ratio of two such quantities is the ratio of the bare
couplings regardless of the shared c^2). T51's conclusion -- these are
two genuinely different physical quantities, not interchangeable -- is
correct and untouched by anything in this audit.

**Checklist item closed:** Part 119/128 (g_dyn) -- RESOLVED. Same root
cause as Sections 7a-7b (Hypothesis 1, confirmed project-wide now across
three independent chains: Part 62's local mass, Part 128's Lambda, and
Part 99/25/102/119's g_dyn). No numerical result changes for g_dyn's own
established use (Part 119's EOS/freeze results stand); the correction is
a labeling clarification (g_dyn is c^2 times a bare coupling, not the bare
coupling itself), consistent with and reinforcing T51's own prior finding.

---

## 7e. Update (2026-09-06, same pass) — Parts 96, 113, 131 Closed; One NEW, Separate Question Found

### Part 96 (`condensate_layer_optics.md`) — CLEAR / already-covered

Eq 89.2 (`omega_gap = m_cond*c^2/hbar`) is the same, uncontested Part
94 dispersion identity -- clean. Line 441-443's speculative
`omega_gap_C2(r) = sqrt(omega_gap_C2^2 + 2g*Phi(r)/hbar^2)` is the SAME
phi_- local-mass formula as Part 62, reused in a different Part -- same
root cause, same fix, no new mechanism. Already tagged [SPECULATIVE]
there. No independent action needed beyond Section 7b's correction.

### Part 113 (`two_phase_tan.md`) — CLEAR for T68's own question, but surfaces a DIFFERENT, separate inconsistency

Part 113 reuses Part 99's own pendulum construction directly (same `g`,
same Eq 99.1 lineage) -- consistent with Section 7d, no new c^2-mislabeling
bug here. **However**, while checking it, a different, previously-unnoted
inconsistency surfaced, unrelated to the 1/s-vs-1/s^2 question T68 was
scoped to answer:

- Part 94 asserts **g = omega_gap** (linear, Eq 94.1, citing Part 34's
  independent condensate self-consistency argument -- NOT derived from
  the pendulum equation).
- Part 99's own pendulum equation (Eq 99.1, linearized near Delta=0) gives
  angular frequency `omega = sqrt(2g)` for small oscillations -- i.e.
  `omega^2 = 2g`, a QUADRATIC relationship. Part 113 (lines 46, 228, 234,
  237) explicitly calls this pendulum frequency "omega_gap" and states
  `2g = omega_gap^2`.

**These two claims about the SAME symbols (g, omega_gap) cannot both be
literally true in general** -- `g=omega_gap` and `g=omega_gap^2/2`
together force `omega_gap = 2` in whatever units, which is not generically
true. This suggests Part 94's omega_gap (a quasiparticle energy-gap
frequency, m_cond*c^2/hbar) and Part 99/113's "omega_gap" (the pendulum's
own small-oscillation frequency) may be two DIFFERENT physical
frequencies that happen to share a name -- or Part 34's original
self-consistency argument (not read in this pass) independently forces
them equal for a reason not yet checked. **Not resolved here** -- this is
a genuinely separate question from T68's own scope (which was about SI
dimensions, 1/s vs 1/length^2, not about whether two same-named
quantities are numerically the same). Filed as a new, narrow follow-up
(see TODO note below) rather than expanding T68 further.

### Part 131 — swing corrected at the source

`phi_minus_local_mass_and_crossover.md` Section 7 updated directly: the
"~42 orders of magnitude" claim corrected to the SymPy-verified 21.6
orders, with a pointer to this doc's Sections 7a-7b. Both original
endpoint numbers (105 eV, 4.5e14 GeV) confirmed correct and left
unchanged; only the swing figure and its explanation were wrong.

**Checklist items closed: Parts 96, 113, 131 — all done. 9/9 checklist
items complete.**

---

## 8. What This Doesn't Change (Yet)

Nothing in this note resolves T68 — no formula is corrected, no doc other
than this one and TODO_05.md is touched. Part 131's own core conclusions
(existence and location of phi_-'s true minimum, absence of a pi/4
crossover) remain valid, as already noted in its own Sec 7 (they need
`g > 0`, not a specific value or units convention).

---

## 9. References

- Part 33 — `vortex_winding_derivation.md`
- Part 61/62 — two-phase Lagrangian, reversed Higgs (CLAUDE.md)
- Part 94 — `coupling_constant_g.md`
- Part 95 — `emergent_c.md` Result 7 (the natural-units caveat, Finding 1)
- Part 117 — `phi_minus_quartic.md`
- Part 119 — `lambda_locking_fossil.md`
- Part 128 (T51) — `lambda_locking_fossil.md` Sec 11 (the 1/s^2 derivation,
  corrected here in Section 7a to 1/length^2)
- `simulations/solver/t68_g_units_field_equation.py` — SymPy dimensional
  re-derivation supporting Section 7a's correction
- Part 62 — `simulations/solver/reversed_higgs.py` (`verify_mass_formula()`,
  the original phi_- mass computation corrected in Section 7b)
- `simulations/solver/t68_g_units_phi_minus_mass.py` — SymPy + numeric
  verification supporting Section 7b's correction
- `docs/research/falsifiable_predictions.md` Eq. F.12 — the hollow-shell
  test prediction flagged (not yet fixed) in Section 7b as a downstream
  consequence
- Part 99 — `tan_critical_point.md` (Eq 99.1, where the same missing-c^2
  reduction bug was found at the root of the g_dyn chain, Section 7d)
- Part 25 — `wz_dark_energy_pdtp.md`; Part 102 — `loss_tangent_dark_
  energy.md` (the g_dyn derivation chain traced in Section 7d)
- Part 96 — `condensate_layer_optics.md`; Part 113 — `two_phase_tan.md`
  (checked in Section 7e; Part 113 surfaced the separate g=omega_gap
  vs g=omega_gap^2/2 question, filed as TODO_05 T72)
- Part 131 (T18) — `phi_minus_local_mass_and_crossover.md` Sec 6-9 (where
  T68 originated; Findings 2 and 3 above are new to this note)
- TODO_05.md T68 — the tracked open item this note scopes

---

*Scoping notes only. Continues into TODO_05.md T68's per-Part checklist.*
