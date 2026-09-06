# phi_- Local Mass and the Delta_- Crossover Question (T18, Part 131)

**Source:** TODO_04 T18 (Priority 18); Part 99 open question 3
(`tan_critical_point.md` Sec 10.3); Part 62 (`reversed_higgs.py`); Part 119
(`lambda_locking_fossil.md` Sec 2.1, true vacuum at phi_- = pi/2).
**Script:** `simulations/solver/t18_delta_minus_crossover.py`. Log:
`simulations/solver/outputs/t18_delta_minus_crossover_run2.txt`. 13/13 Sudoku PASS.

## Plain English Summary

The two-phase Lagrangian (Part 61) has a second scalar field, phi_-, whose
behavior near matter was first worked out in Part 62 ("reversed Higgs"):
opposite of the ordinary Higgs field, phi_- is massless in empty space and
gains mass near a gravitating body. T17 asked whether the GRAVITY-channel
phase mismatch (Delta_+) has an observable "crossover" at 45 degrees near
compact objects. This note asks the analogous question for the SURFACE-mode
field: does phi_-'s own phase mismatch (Delta_-) ever reach a similar
45-degree crossover inside a neutron star?

Answering this required first resolving something the project's own history
had left slightly tangled: Part 62 (2026, early two-phase work) said phi_-'s
natural rest point ("vacuum") was at phi_- = 0. Part 119 (a later, separate
investigation into the cosmological constant) found the TRUE rest point is
actually phi_- = pi/2, and diagnosed phi_- = 0 as an unstable point the
field rolls away FROM, not a place it settles. This note shows that Part
119's correction was already fully contained in Part 61's own original
formula for the two-phase potential -- no cosmological machinery needed.
Directly finding where that formula is flattest (its true minimum) gives
phi_- = pi/2 immediately, for any nonzero gravity at all. This also exposes
exactly where Part 62's original mass-at-vacuum calculation went wrong: it
computed the curvature of the potential AT phi_-=0, a point that (once
gravity is present) is not even a rest point of the potential -- so that
number was never really describing a stable particle mass, it was
describing how fast phi_- starts rolling away from zero.

With the correct rest point established (phi_- = pi/2), the actual answer to
this note's central question is a clean **no**: there is no analogous 45-degree
crossover for phi_-. The gravity-channel Delta_+ has a real crossover at 45
degrees because it is a fundamentally different kind of variable -- a
monotonic "how decoupled are we" dial running from 0 (fully locked) to 90
degrees (fully decoupled), with 45 degrees marking where two different force
regimes swap dominance (Part 99). The surface-mode phi_- is not a dial like
that at all: it is a field sitting in a bowl-shaped potential with ONE
bottom (pi/2), and reaching a 45-degree displacement from that bottom is not
a special point -- it is simply some amount of (temporary) displacement on
the way to settling down, no different physically from being displaced 10
degrees or 80 degrees.

One further sub-question -- whether phi_-'s local mass near a neutron star
could resonate with real neutron-star oscillation modes -- could NOT be
answered with confidence. While scoping that calculation, this note found
that Part 62's mass formula uses a coupling constant "g" with a units
shortcut the project had already flagged and fixed in a different context
(T51/Part 128) -- but the fix does not obviously transfer here, and two
different "correct" numbers for g are already in circulation elsewhere in
the project, differing by roughly 60 orders of magnitude. Rather than
silently pick one and report a possibly-wrong number as fact, this note
reports the mode-frequency question as **open**, and files the underlying
units question as its own separate task (TODO_05 T68) for dedicated,
unhurried attention.

---

## 1. Setup: Part 61's Product-Form Potential [ESTABLISHED, re-derived]

The two-phase Lagrangian (Part 61, CLAUDE.md) is

  L = +g cos(psi - phi_b) - g cos(psi - phi_s)    [Part 61, established]

with phi_+ = (phi_b+phi_s)/2 (gravity mode) and phi_- = (phi_b-phi_s)/2
(surface mode). The standard trigonometric sum-to-product identity
cos(A) - cos(B) = -2 sin((A+B)/2) sin((A-B)/2), applied with A = psi-phi_b,
B = psi-phi_s (so (A+B)/2 = psi-phi_+ and (A-B)/2 = -phi_-), gives

  cos(psi-phi_b) - cos(psi-phi_s) = 2 sin(psi-phi_+) sin(phi_-)    [Part 61, established]

Using Delta_+ = psi - phi_+ (Part 98/99 notation), the interaction term is
L_int = 2g sin(Delta_+) sin(phi_-), and (standard L = T - V convention) the
effective potential for phi_- at fixed Delta_+ is

  **V_eff(phi_-; Delta_+) = -2g sin(Delta_+) sin(phi_-)    [Eq 131.1, re-derived from Part 61]**

**SymPy verification:** `derive_exact_potential_and_extrema()` constructs
Eq 131.1 directly from `sp.sin`/`sp.diff` (not hand-typed as a final answer)
and differentiates it symbolically for everything that follows.

---

## 2. Exact Extremization: the True Minimum Is Always at pi/2 [DERIVED, PDTP Original]

Differentiating Eq 131.1 with respect to phi_-:

  dV/dphi_- = -2g sin(Delta_+) cos(phi_-)    [Eq 131.2]

Setting this to zero (for sin(Delta_+) != 0, i.e. ANY nonzero gravitational
coupling at all): cos(phi_-) = 0, giving **phi_- = pi/2 or phi_- = 3pi/2
(equivalently -pi/2)** -- confirmed by `sp.solve` (Sudoku S1).

Classify with the second derivative, d^2V/dphi_-^2 = +2g sin(Delta_+) sin(phi_-):

| Point | d^2V/dphi_-^2 | V value | Classification |
|---|---|---|---|
| phi_- = pi/2 | **+2g sin(Delta_+)** (positive, S2) | -2g sin(Delta_+) | **stable minimum** |
| phi_- = -pi/2 | -2g sin(Delta_+) (negative, S3) | +2g sin(Delta_+) | unstable maximum |

Since sin(Delta_+) > 0 for any physical 0 < Delta_+ < pi/2 (Part 98/99), the
point phi_- = pi/2 has the strictly LOWER potential value (checked
numerically at a representative Delta_+=0.5 rad, Sudoku S4) -- it is not
merely a local minimum, it is the GLOBAL minimum.

  **phi_-_vac = pi/2, for any Delta_+ > 0    [Eq 131.3, DERIVED]**

**This independently reproduces Part 119's "true vacuum at pi/2" result**
(`lambda_locking_fossil.md` Sec 2.1, derived there via a cosmological
slow-roll/beta parametrization and the Part 117 induced-quartic term) --
but here it falls out directly from Part 61's own ORIGINAL, leading-order,
non-quartic potential, with no cosmological machinery required. **Independence
argument:** the two derivations start from different places (Part 119:
cosmological background dynamics with a quartic correction; here: static
extremization of the bare two-phase coupling) and land on the identical
answer -- a genuine cross-check, not a restatement.

---

## 3. Reconciling Part 62's Original Mass Claim [RESOLVED]

Part 62 (`reversed_higgs.py` docstring) states: "Near matter:
sin(psi-phi_+) ~ Phi_grav > 0 -> V''(0) = -2g*sin(psi-phi_+)" -- i.e. it
evaluates the curvature of V_eff AT phi_- = 0 and calls that the mass-squared.

Checking this directly against Eq 131.1 (`reconcile_with_part62_and_119()`):

  dV/dphi_- |_{phi_-=0} = -2g sin(Delta_+) cos(0) = **-2g sin(Delta_+)**    [Eq 131.2 evaluated at phi_-=0; nonzero for Delta_+>0, Sudoku S5]

  d^2V/dphi_-^2 |_{phi_-=0} = 2g sin(Delta_+) sin(0) = **0**    [Sudoku S6]

Two things follow immediately:

1. **phi_- = 0 is not a stationary point at all** once Delta_+ > 0 (any
   gravity present) -- dV/dphi_- is nonzero there. A "mass" is only a
   well-defined concept as the curvature AT an equilibrium; evaluating
   curvature at a non-equilibrium point does not give a particle mass.
2. **The actual curvature at phi_- = 0 is exactly zero**, not
   -2g sin(Delta_+) as Part 62's docstring claims (residual = +2g sin(Delta_+)
   != 0, Sudoku S7) -- Part 62's formula does not match its own stated potential.

**Reconciliation:** what Part 62's quantity -2g sin(Delta_+) actually IS, is
the SLOPE dV/dphi_- at phi_-=0 (Eq above), not a curvature. A negative
slope at a point where the field starts (phi_- begins near 0, having no
reason to be anywhere else before gravity switches on) means the field is
pushed AWAY from 0 -- this is precisely the tachyonic instability Part 119
Sec 2.1 already diagnosed ("the tachyonic instability... pushing phi_- away
from 0... simply means you are at the wrong point; roll toward pi/2").
Part 62's number describes the INITIAL push, not the final rest state.
Part 62's physical conclusion (phi_- gains mass near matter) is not wrong --
the true stable mass just lives at phi_- = pi/2, not phi_- = 0 (Sec 4 below).

---

## 4. The Correct Stable Mass Formula and Delta_- [DERIVED, PDTP Original]

Define **Delta_- = pi/2 - phi_-** (displacement from the TRUE vacuum,
matching Part 119's own xi variable and the "surface mode offset from pi/2
equilibrium" language already used in `pdtp_refractive_index.md` Sec 8).

The stable mass is the curvature at the true minimum:

  **m^2(Delta_+) = d^2V/dphi_-^2 |_{phi_-=pi/2} = 2g sin(Delta_+)    [Eq 131.4, DERIVED]**

Cross-checked a second, independent way: substituting phi_- = pi/2 - Delta_-
into Eq 131.1 and Taylor-expanding in Delta_- to second order
(`derive_stable_mass_and_delta_minus()`, `sp.series`):

  V_eff = -2g sin(Delta_+) + g sin(Delta_+) Delta_-^2 + O(Delta_-^3)

matching the standard SHM form V = const + (1/2) m^2 Delta_-^2 with
m^2 = 2g sin(Delta_+) -- **identical to Eq 131.4** (residual = 0, Sudoku S8-S9).
Two independent routes (direct 2nd derivative; series-expansion coefficient)
agree exactly.

**Plain English:** near its true rest point, phi_- behaves like a mass on a
spring, oscillating in Delta_- with a restoring strength set by 2g sin(Delta_+)
-- stronger gravity (larger Delta_+) means a stiffer spring means a heavier
effective particle. This is structurally the same story Part 62 always told
(mass grows with gravitational coupling), just anchored at the correct point.

---

## 5. Is Delta_- = pi/4 a Crossover? [NEGATIVE, PDTP Original]

T17 found a real crossover for Delta_+ at pi/4 (Part 99: tan(Delta_+)=1,
from comparing the first and second derivatives of the SINGLE-PHASE
potential V(Delta_+) = -2g cos(Delta_+), Eq 99.2-99.3). Does an analogous
special point exist for Delta_- at pi/4?

Checking dV/dphi_- (Eq 131.2) at phi_- = pi/4:

  dV/dphi_- |_{phi_-=pi/4} = -2g sin(Delta_+) cos(pi/4) = **-sqrt(2) g sin(Delta_+)**

nonzero for any Delta_+ > 0 (`check_delta_minus_pi4_crossover()`, Sudoku
S10) -- phi_- = pi/4 is not a critical point, not an inflection point, not
distinguished in any way by V_eff. It is simply some amount of displacement
along the roll toward the true minimum at pi/2.

**Why the two cases differ (structural explanation):** Delta_+'s pi/4
crossover and Delta_-'s absence of one come from genuinely different kinds
of potentials:

| | Delta_+ (Part 99) | Delta_- (this note) |
|---|---|---|
| Potential | V(Delta_+) = -2g cos(Delta_+) | V(phi_-; Delta_+) = -2g sin(Delta_+) sin(phi_-) |
| Role of the variable | monotonic "how decoupled" dial, 0 (locked) to pi/2 (decoupled) | displacement from a stable equilibrium |
| Special point? | pi/4: where \|dV/dDelta_+\| = \|d^2V/dDelta_+^2\| (Eq 99.4, force = coupling) | pi/2 (=Delta_-=0): the potential's own minimum; no other special point |
| Physical meaning of the special point | regime boundary within the SAME field's own dynamics | not applicable -- there is no analogous boundary |

The Part 99 tan(pi/4)=1 criterion is reproduced exactly as an internal
cross-check (`sp.tan(sp.pi/4) - 1` residual = 0, Sudoku S11), confirming the
CONTRAST is not due to an error in reproducing Part 99, but a genuine
structural difference between the two potentials.

**Answers to T18's original Key Questions:**
- **(a) Is there a stable Delta_- = pi/4 crossover state inside dense
  objects? NO** -- V_eff has exactly one critical point (phi_- = pi/2,
  Delta_- = 0) for any Delta_+ > 0; pi/4 is not distinguished.
- **(c) Is the Part 62 equilibrium (pi/2) the same thing as the crossover
  (pi/4)? NO, and they are not even the same TYPE of concept** -- pi/2 is
  the potential's genuine global minimum (Sec 2); the "crossover" language
  only applies to Delta_+'s different, non-equilibrium monotonic-dial
  structure (Part 99), which Delta_- does not share.

---

## 6. Neutron-Star Mass/Mode Comparison [OPEN -- see caveat]

T18's remaining Key Question ((b): would n_- = sqrt(2) inside a NS affect
f-modes/g-modes?) requires converting Eq 131.4 into an actual frequency,
which needs a numerical value for g with units of 1/s^2 (as T51/Part 128
established the field equation requires).

**A units issue was found while scoping this, not fixed here** (see Sec 7).
Two candidate values are shown, both explicitly caveated
(`numeric_ns_mass_and_modes()`):

Using a realistic 1.4 solar-mass neutron star (R=11-12 km, r_S=4.14 km,
Delta_+ = 36-38 degrees, reusing T17/Part 130's numbers):

| Candidate | Value | m(Delta_+) at NS surface | vs. NS f-mode band (1-3 kHz) |
|---|---|---|---|
| A: g = omega_gap^2 = (m_P c^2/hbar)^2 | 3.44e86 s^-2 | ~3.2e42 Hz | ~39 orders of magnitude ABOVE |
| B: Part 119's g_dyn (cosmological, reference only -- NOT combined with NS Delta_+) | ~2e-36 s^-2 | ~3e-19 Hz (its own native, cosmological-epoch value) | ~20+ orders of magnitude BELOW |

Candidate A is the literal, dimensionally-forced placeholder from T51's own
resolution ("omega_gap^2 plays g's role wherever squared elsewhere") --
tied to the framework's single free parameter m_cond=m_P, but NOT
independently validated for THIS specific formula. Candidate B is Part
119's own already-established coupling for phi_-'s mass, but it was derived
for a completely different regime (the present-day cosmological background,
near-exact vacuum) -- substituting a neutron-star-scale sin(Delta_+) into it
would repeat exactly the kind of unjustified g-mixing T51 already warned
against for g_Lambda vs g_dyn, so it is deliberately NOT done here.

**Verdict: OPEN / INCONCLUSIVE.** The two candidates bracket the neutron-star
oscillation-mode band (10 Hz - 3 kHz) by roughly 60 orders of magnitude
combined -- this is not a "the effect is too small" or "too large" negative
result, it is a "the calculation cannot be trusted yet" result. Reported
honestly as open rather than picking one candidate and presenting a
possibly-wrong number as fact.

---

## 7. A Units Inconsistency, Flagged Here and RESOLVED in TODO_05 T68

While scoping Sec 6, this note found that Part 62's coupling g is used as
g = omega_gap = m_P c^2/hbar directly (units 1/s, a frequency) -- consistent
with how Parts 33/94 use g elsewhere (t_P = 1/g, E_P = hbar*g, all treating
g as a frequency). But T51 (Part 128) separately established, from the
field equation's own structure (box(phi) = g sin(psi-phi), phi dimensionless),
that g must carry units 1/s^2 -- ONE POWER MORE than a frequency. Applying
T51's own stated fix ("omega_gap^2, not omega_gap, plays g's role") to Part
62's formula was estimated here to move its predicted phi_- mass at Earth's
surface from ~105 eV (Part 62's original number) to ~4.5e14 GeV -- stated
at the time as "a ~42 order-of-magnitude swing."

**UPDATE (T68, 2026-09-06, `docs/research/g_units_audit_scoping.md` Sec
7a-7b):** this was investigated fully. Both endpoint numbers above (105 eV,
4.5e14 GeV) were confirmed correct -- but the swing between them is
**21.6 orders of magnitude, not ~42** (SymPy-verified:
`E_correct/E_code = sqrt(omega_gap)` exactly, `simulations/solver/
t68_g_units_phi_minus_mass.py`). T68 traced this to the same root-cause
bug across three independent chains (Part 62's local mass here, Part
128's Lambda, Part 99/119's g_dyn): reducing the covariant field equation
`box(phi)=g*sin(psi-phi)` to a pure-time equation while dropping the
1/c^2 that `box` requires. The correct SI dimension is `[g]=1/length^2`
(not 1/s or 1/s^2 as either convention informally assumed), and
`g_bare = omega_gap^2/c^2`. T68's audit is essentially complete; see the
scoping doc for the full trace across Parts 33/61/62/94/95/99/117/119/128.

This was, at the time, a genuine, previously-unflagged inconsistency in
how "g" had been dimensioned across the project's history (at minimum
touching Parts 33, 61, 62, 94, 96, 113, 117-119, 128) -- bigger than T18's
original scope and correctly deferred rather than resolved here. T18's own
core conclusions (Sec 2, 4, 5 -- existence and location of the true
minimum, absence of a Delta_- = pi/4 crossover) never depended on
resolving this, since they only require g > 0, not a specific numerical
value or units convention -- confirmed unaffected by T68's resolution.

---

## 8. Sudoku Consistency Check

13 tests (`sudoku_checks()` in `t18_delta_minus_crossover.py`).

| Test | Check | Result |
|------|-------|--------|
| S1 | cos(phi_-)=0 critical points include pi/2 (and its 3pi/2=-pi/2 twin) | PASS |
| S2 | d^2V/dphi_-^2 at pi/2 is +2g sin(Delta_+) (stable minimum) | PASS |
| S3 | d^2V/dphi_-^2 at -pi/2 is -2g sin(Delta_+) (unstable maximum) | PASS |
| S4 | V(pi/2) < V(-pi/2) at a representative Delta_+ -- pi/2 is the GLOBAL min | PASS |
| S5 | phi_-=0 is NOT stationary for Delta_+>0 | PASS |
| S6 | d^2V/dphi_-^2 at phi_-=0 is exactly 0 (not Part 62's claimed -2g sin(Delta_+)) | PASS |
| S7 | Residual vs Part 62's claimed curvature is nonzero (confirms the mismatch) | PASS |
| S8 | Mass from 2nd derivative matches mass from series expansion (residual=0) | PASS |
| S9 | m^2(Delta_+) = 2g sin(Delta_+) exactly | PASS |
| S10 | phi_-=pi/4 is NOT a critical point of V_eff for Delta_+>0 | PASS |
| S11 | Part 99's tan(pi/4)=1 criterion reproduced (residual=0) | PASS |
| S12 | Candidate A's NS mass is many orders of magnitude above the f-mode band (computed, not asserted) | PASS |
| S13 | g_dyn reference value matches Part 119's own order of magnitude | PASS |

**13/13 PASS.**

---

## 9. New Results Summary

| Equation | Status | Description |
|----------|--------|-------------|
| V_eff(phi_-;Delta_+) = -2g sin(Delta_+) sin(phi_-) [Eq 131.1] | [DERIVED] (from established Part 61 identity) | re-derived directly, not hand-typed |
| phi_-_vac = pi/2 for any Delta_+ > 0 [Eq 131.3] | [DERIVED, PDTP Original] | independently reproduces Part 119, via a simpler static route |
| m^2(Delta_+) = 2g sin(Delta_+) at true minimum [Eq 131.4] | [DERIVED, PDTP Original] | corrects Part 62's V''(0)-at-wrong-point formula |
| Delta_- = pi/2 - phi_- has no pi/4 crossover | [NEGATIVE, PDTP Original] | structurally different potential from Delta_+'s |
| NS mode-frequency comparison | [OPEN] | blocked on TODO_05 T68 (g-units), two candidates shown, ~60 OoM apart |

---

## 10. Open Questions / Follow-up

1. **TODO_05 T68 (new, filed from this note):** resolve which numerical
   value of g (units 1/s^2, per T51/Part128) is the physically correct
   coupling for LOCAL/static formulas like Eq 131.4, as distinct from
   g_Lambda (cosmological-constant-specific, Part 128) and g_dyn
   (present-epoch background value, Part 119). Needed before Sec 6's NS
   mode-frequency comparison (or any other local phi_- mass prediction,
   e.g. Part 82's Yukawa screening length) can be trusted numerically.
2. **Relaxation-time check** (not done here): even with g resolved, does
   phi_- actually reach its true minimum on astrophysically-relevant
   timescales inside a real (not idealized-static) neutron star, or could
   it be kinetically stuck partway? Left for a follow-up once T68 is
   resolved.

---

## 11. References

**Source:** Part 61 (two-phase Lagrangian, CLAUDE.md) -- product-form
coupling identity, established.
**Source:** Part 62, `simulations/solver/reversed_higgs.py` -- original
phi_- mass claim, reconciled (not overturned) here.
**Source:** Part 98/99, `docs/research/tan_critical_point.md` -- Delta_+
crossover (tan(Delta_+)=1) used for contrast in Sec 5.
**Source:** Part 119, `docs/research/lambda_locking_fossil.md` Sec 2.1 --
true vacuum at phi_-=pi/2, independently reproduced here.
**Source:** Part 128 (T51), `docs/research/lambda_locking_fossil.md` Sec 11
-- g-units dimensional audit; its "omega_gap^2 plays g's role" resolution
is the Candidate A value used (caveated) in Sec 6.
**Cross-reference:** T17/Part 130 (`docs/research/pdtp_refractive_index.md`
Sec 12) -- the analogous Delta_+ investigation this note parallels and
contrasts against.
