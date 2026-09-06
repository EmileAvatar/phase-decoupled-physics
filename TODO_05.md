# TODO_05 — Lambda-Locking Deep Dive and Multi-Medium Framework

**Type:** Extended investigation — Lambda mechanism + multi-condensate structure
**Date opened:** 2026-07-04
**Source notes:** `docs/fable_notes/` (Fable session notes + DESI update, 2026-07-02/04)
**Previous roadmaps:** [TODO_01.md](TODO_01.md) (Parts 1-41) |
[TODO_02.md](TODO_02.md) (Parts 42-76) | [TODO_03.md](TODO_03.md) (Parts 77-83+) |
[TODO_04.md](TODO_04.md) (Parts 84-120+)

---

## Overview

Two investigation threads opened by Fable session notes (2026-07-02) and DESI
DR2 data analysis (2026-07-04):

**Thread A — Lambda-Locking Deep Dive (T46 extended)**
T46 (Part 119) proved phi_- = pi/2 is the true vacuum and derived the thawing EOS
w = -1+2*eps. The magnitude problem remains: the causal-sync ansatz
phi_minus_vac ~ H/omega_gap predicts (H_0/omega_gap)^2 ~ 1.4e-122, matching the
observed Lambda ratio within factor ~2. DESI DR2 adds empirical targets:
w_0 ~ -0.7, w_a ~ -1 (contested), dark energy peak at z ~ 0.5.

**Thread B — Multi-Medium Framework**
PDTP has at least three interpenetrating condensates (gravitational, EM, QCD).
The stiffness ratios between them are hard predictions, not free parameters.
Key open questions: Dvali-Gomez criticality as an attractor, QCD stiffness
cross-check, cross-medium coupling Sudoku, and weak-force placement.

**Thread C — Relative Entropy as Bridge to Einstein Equations**
External ChatGPT-session proposal (`docs/fable_notes/fable notes to check 02.md`,
2026-07-08): derive a relative-entropy functional directly from the phase mismatch
Delta_theta = psi - phi (candidate S_rel ~ 1 - cos(Delta_theta) = 1 - V/g), rather
than assuming an entropy-area law, then chain phase mismatch -> relative entropy ->
area variation -> Einstein equations (mirroring a recent semiclassical-gravity-from-
relative-entropy paper). NOTE: Part 86 already derived a DIFFERENT entropy-area law
(S_PDTP = k_B*ln(2)*A/a_0^2, lattice cell counting) and used Jacobson's argument to
recover full nonlinear GR at a_0 = 1.665*l_P — the ChatGPT session did not have
access to this. **UPDATE (Parts 126+127, 2026-07-08):** the prerequisite check
(Part 126) found the two are NOT complementary in the way hoped — S_rel cannot derive
an area law without the same postulate Part 86 already made. But pursuing the
rescoped question anyway (Part 127) found something real: phi_-'s own dynamics at
the horizon, combined with CP symmetry already established in Part 125, EXACTLY
reproduce the ln(2)-per-cell entropy Part 86 had to assume. Thread C is now closed
with a net positive (if modest) result. See T60 below for both findings.

**Thread D — Millennium Prize Problem Connections**
Opened 2026-07-11 after reviewing an external paper that misappropriated the
Yang-Mills Millennium Problem's name (see `docs/technical/The Seven Millennium Prize
Problems.md` for the full reference doc). Of the seven problems, three (P vs NP, Hodge
Conjecture, Birch-Swinnerton-Dyer) have no plausible PDTP connection and are not filed
as TODO items. Four have at least an indirect link worth a scoping look: Riemann
Hypothesis (dormant TODO_03 Category H), Yang-Mills mass gap (PDTP's own internal
"mass gap" language vs. the actual axiomatic QFT problem — needs an explicit
non-overclaiming statement), Navier-Stokes (superfluid condensate analogy, likely
negative), and the Poincaré Conjecture's solution METHOD (Ricci flow with surgery) as
a possible tool, not the theorem itself, for PDTP's topological-defect stability
questions.

---

## Open Items — Quick Reference

New additions go on top. One line per item. Full details below.

- [ ] T72 — Reconcile Part 94's g=omega_gap (linear, from Part 34's
  condensate self-consistency) against Part 99's pendulum equation, which
  implies g=omega_gap^2/2 (quadratic, from linearizing d^2Delta/dt^2=
  -2g*sin(Delta) near Delta=0 and calling the result "omega_gap", Part
  113 lines 46/228/234/237). These cannot both hold generally for the
  same g and omega_gap -- surfaced while auditing Part 113 for T68, but
  a SEPARATE question from T68's own SI-dimension scope (this is about
  whether two same-named quantities are the same NUMBER, not about units).
  Needs Part 34 (`condensate_selfconsist.py`) read directly to see if its
  self-consistency argument independently forces the two frequencies
  equal, or whether they are actually different physical frequencies that
  happen to share a name [PENDING, filed 2026-09-06; see docs/research/
  g_units_audit_scoping.md Sec 7e]
- [x] T68 — Resolve g's units project-wide (1/s vs 1/s^2): Parts 33/94 use g as
  a frequency (t_P=1/g, E_P=hbar*g); T51/Part128 independently derived [g]=1/s^2
  from the field equation's own structure. Part 62's phi_- mass formula uses the
  frequency convention directly; applying T51's fix moves its Earth-surface
  prediction by ~42 orders of magnitude (105 eV -> ~1e14 GeV) -- THIS SPECIFIC
  NUMBER FLAGGED, does not reproduce on a first-pass hand check (~21-22 OoM
  found instead; see scoping doc Sec 5). Two "correct" candidates (omega_gap^2
  vs Part 119's g_dyn) already differ by ~60 OoM for a neutron-star context.
  Touches Parts 33/61/62/94/96/113/117-119/128 -- bigger than any single
  T-item, needs its own dedicated pass [IN PROGRESS, HIGH -- blocks any
  numerical phi_- local-mass prediction; filed 2026-08-09 from TODO_04 T18;
  Step 1 (enumeration) done 2026-09-06, found a 3rd candidate hypothesis
  (natural-units-vs-SI conversion slip, not necessarily two distinct physical
  couplings) plus a Sudoku blind-spot (internal-consistency checks can PASS
  even with the wrong absolute units). CONFIRMED same day: SymPy re-derivation
  of the field equation's dimension (full SI, both terms of box(phi) verified
  independently) shows [g] = 1/length^2, NOT 1/time^2 as Part 128 stated --
  g = omega_gap^2/c^2, not omega_gap^2 alone. Part 128's own Lambda_obs match
  (1.000000, 12/12 Sudoku) is UNAFFECTED -- its working formula already
  carries the missing /c^2 elsewhere in its structure. Parts 33/94/95/128
  checked off. SAME bug found+fixed in Part 61/62 (reversed_higgs.py):
  corrected phi_- local mass E_rest=hbar*omega_gap*sqrt(2*Phi), exactly
  sqrt(omega_gap)~4.3e21 above the code's original ~105 eV, giving
  ~4.5e14 GeV at Earth's surface -- BOTH endpoint numbers already on
  record were right, only the "~42 orders" swing label was wrong (actual:
  21.6 orders). Downstream consequence flagged: falsifiable_predictions.md
  Eq F.12 (hollow-shell test) needs updating once the checklist closes
  (own plan-first pass required, not done yet). Part 117 CLEAR (no bug,
  independently confirms [g]=1/length^2). Part 119/128's g_dyn RESOLVED:
  traces to the SAME missing-c^2 bug at its root in Part 99's Eq 99.1
  (SymPy-verified); g_dyn = c^2 x bare coupling; its own number and Part
  119's results UNCHANGED; T51's g_Lambda != g_dyn finding UNAFFECTED
  (shared mislabeling cancels in the ratio). **CENTRAL AUDIT QUESTION
  RESOLVED: one global units bug (Hypothesis 1), not two distinct
  physical couplings, confirmed across 3 independent chains (Part 62
  local mass, Part 128 Lambda, Part 99/119 g_dyn).** Parts 96/113/131
  closed (confirmatory, as expected -- Part 131's "~42 orders" corrected
  to 21.6 at the source). CHECKLIST COMPLETE 9/9. One new, narrower,
  separate question surfaced (Part 94's g=omega_gap vs Part 99's implied
  g=omega_gap^2/2) -- filed separately as T72. See docs/research/
  g_units_audit_scoping.md Sec 7a-7e]
- [ ] T67 — Galactic disk "flapping" as DM-wake phenomenology: Milky Way warp actively driven by Magellanic Cloud dark-matter wake (Weinberg & Blitz 2006); initial findings written up with a tiered, honestly-scoped PDTP connection (structural compatibility / open question re: Part 116 topological DM / speculative variable-c wake idea stacked on T57) [PENDING, LOW PRIORITY, filed 2026-08-05; see docs/research/galactic_disk_dynamics_note.md]
- [ ] T64 — Poincaré/geometrization method scoping: could Ricci-flow-with-surgery-style geometric relaxation inform PDTP's own condensate-defect stability analysis (e.g. Hopf-link vs Y-junction energy comparison, Part 106)? Tool, not theorem -- Poincaré itself has no direct PDTP content [PENDING, SPEC, LOW PRIORITY]
- [ ] T63 — Navier-Stokes / superfluid condensate scoping: does PDTP's Gross-Pitaevskii-style condensate description have any bearing on classical NS existence/smoothness, or is this purely a loose analogy? Expected NEGATIVE (different equations/regime) but must be stated explicitly, not just assumed [PENDING, SPEC, LOW PRIORITY]
- [ ] T62 — Yang-Mills mass gap non-overclaiming statement: PDTP has internal "mass gap" results (m^2=2g for phi_-, omega_gap) and runs actual lattice SU(3) gauge theory (Parts 37-41) -- write an explicit scoping note distinguishing these from the axiomatic Clay Millennium Problem (rigorous QFT construction + gap proof), so PDTP never overclaims here the way the external paper reviewed 2026-07-11 did [PENDING, MEDIUM -- integrity/scoping task, not new physics]
- [ ] T61 — Riemann Hypothesis connection revisit: TODO_03 Category H (H1-H4) is dormant SPECULATION with no calculation started; consolidate references with the new Millennium Problems doc; scope whether any PDTP structure (condensate mode density, phase spectrum) could relate to zeta zero statistics (Hilbert-Polya style) -- low priority, no concrete starting point identified yet [PENDING, SPEC, LOW PRIORITY]
- [x] T60 — Relative entropy from phase mismatch: **DONE (Part 126 + Part 127, Phase 94-95, 2026-07-08).** Task 3 (prereq check): S_rel=1-alpha is NOT the same object as Part 86's S_PDTP; the external proposal cannot derive an area law without Part 86's same postulate (9/10 Sudoku). Task 2 (rescoped): phi_-'s OWN dynamics DO reproduce Part 86's ln(2)-per-cell entropy EXACTLY -- two CP-conjugate horizon branches of D+ (Part 98) source exactly-degenerate phi_- vacua (Part 61 coupling), giving S_cell=k_B*ln(2) matching Part 86 Eq 86.7 to ratio 1.000000 (12/12 Sudoku). Tasks 1/4/5 closed (not needed / not recommended). Net: external proposal literally fails, but the question it raised upgraded one Part 86 input from ASSUMED to DERIVED. [DONE]
- [ ] T59 — Weak force placement: SU(2) extension vs riding existing condensate; even deferred answer must be tracked per Open Problem Tracking Rule [PENDING, SPEC, LOW PRIORITY]
- [ ] T58 — EM condensate quantum mass: locate or derive m_cond_EM giving the 1e36 grav/EM ratio; add to term_glossary.md if missing [PENDING, LOW PRIORITY, one-row addition]
- [ ] T57 — Cross-medium coupling Sudoku: verify PDTP reproduces "EM energy gravitates" (GR requirement); explain what suppresses condensate-condensate direct locking [PENDING, MEDIUM; 5+ Sudoku tests]
- [ ] T56 — QCD/gravitational stiffness ratio: compute ratio from same formula structure as m_cond_QCD = 367 MeV (Part 37); investigate M_0 ~ m_p/3 ~ m_cond_QCD coincidence; link to hierarchy problem [PENDING, HIGH]
- [x] T55 — Dvali-Gomez criticality as attractor: **PARTIAL (Part 124, Phase 92, 2026-07-07)** — energy route NEGATIVE (barrier not minimum, Eq 124.1); entropy route NEGATIVE (minimum at criticality, Eq 124.2); dissipative flow POSITIVE one-sided: alpha_gr=1 is a stability boundary/evaporation endpoint (Eq 124.3), cascade terminates at E_final = m_P*c^2 EXACTLY (Eq 124.4); m_cond <= m_P*O(1) DERIVED (ceiling); equality step (maximal packing) OPEN as 124-O1; no-go 115.4 intact; 12/12 Sudoku [PARTIAL]
- [ ] T54 — Prior art section: cite Zel'dovich, running vacuum, holographic DE; state what PDTP adds (mechanism + freeze-out); needed to survive peer review [PENDING, MEDIUM; research doc section]
- [ ] T53 — Phantom crossing derivation: derive effective w(z) of partially-locked phi_minus INCLUDING energy exchange with matter sector; check w < -1 without ghost instability; SymPy + Sudoku [PENDING, HIGH; Task 4b from DESI update]
- [ ] T52 — Kuramoto expanding-lattice simulation: 2D Kuramoto grid with shrinking coupling range mimicking H(t); measure <phi_minus^2> vs H/K; extract beta(z); triple Sudoku chain (EDE + Lambda + w_0/w_a) [PENDING, HIGH; jackpot sim]
- [x] T51 — Dimensional audit: **DONE (2026-08-05)** — dimensionally-complete formula Lambda = g_Lambda*phi_minus_vac^2/c^2, g_Lambda = 3*Omega_Lambda*omega_gap^2 = 7.067e+86 s^-2 (reproduces Lambda_obs to 1.000000, no hbar needed beyond what's already inside omega_gap); KEY FINDING: g_Lambda != g_dyn (Part 119's dynamical coupling) by 122 orders of magnitude -- two different quantities were sharing the bare symbol "g"; substituting g_dyn directly gives an inconsistent phi_vac > pi/2 (negative-but-useful cross-check); O4 in lambda_locking_fossil.md RESOLVED; Sudoku 12/12 PASS [DONE]
- [x] T50 — Lambda causal-sync numerical check: **DONE (Part 123, Phase 91, 2026-07-07)** — O(1) coefficient derived in CLOSED FORM: C = 3*Omega_Lambda = 2.054 +- 0.022 (SymPy identity, residual 0); closest candidate = 2 (Part 61 G_eff = 2*G_bare) at 2.7%; C = 2 exactly <=> Omega_Lambda = 2/3 <=> z_lock ~ 0.03; two-phase bare-G gives C_bare = 6*Omega_Lambda = 4.11 ~ 4; Sudoku 11/11 PASS [DONE]

**Natural next picks:** T51 (dimensional audit, prerequisite for T52); T56 (QCD stiffness ratio, highest-priority PENDING item in Thread B, now that T55 is PARTIAL); T60 Task 2 (phi_- dynamics vs Part 86 entropy, if you want to continue Thread C).

---

### [x] T68 — Resolve g's Units Project-Wide (1/s vs 1/s^2) — DONE [HIGH]

**Status:** DONE (2026-09-06). Full per-Part audit (`docs/research/
g_units_audit_scoping.md`, Sections 7a-7e) resolved the central question:
neither "1/s" nor "1/s^2" was exactly right -- the correct SI dimension of
the bare Lagrangian coupling g is **1/length^2**, and one single
project-wide units-conversion slip (dropping the 1/c^2 when reducing the
covariant field equation to a pure-time equation) explains every instance
found, confirmed independently across three separate derivation chains
(Part 62's local phi_- mass, Part 128's Lambda, Part 99/119's g_dyn) --
not two genuinely distinct physical couplings as originally framed. One
numerical result corrected (phi_- local mass swing: 21.6 orders of
magnitude, not the ~42 originally stated; both endpoint numbers, 105 eV
and 4.5e14 GeV, were already right and are unchanged). No other numerical
result in the project changes -- g_Lambda and g_dyn's own established
uses are unaffected because the shared mislabeling cancels in any ratio
between quantities built the same way. One downstream consequence
flagged but deliberately not fixed here: `falsifiable_predictions.md`
Eq F.12 (hollow-shell test) needs its own plan-first update, since its
predicted force range collapses once the corrected mass is used. One new,
narrower, separate question surfaced during the audit (Part 94's
g=omega_gap vs Part 99's implied g=omega_gap^2/2) and is filed separately
as **T72**, not folded into T68.
**Estimated effort:** unknown -- likely a multi-Part audit, not a single calculation
**Source:** discovered while scoping TODO_04 T18, 2026-08-09; see
`docs/research/phi_minus_local_mass_and_crossover.md` Sec 7.

**Step 1 findings (2026-09-06, `g_units_audit_scoping.md`) -- read before
continuing:**
1. A blind repo-wide grep for "g" returns 73 files, almost all noise
   (gravitational acceleration, Gell-Mann index g_i, metric g_mu_nu). Do
   NOT repeat this -- work through the per-Part checklist below instead.
2. **Third candidate hypothesis found**, not in the original framing:
   `emergent_c.md` Result 7 already flags that its formula "uses g in the
   natural-unit sense (units [mass]^2)" vs Part 94's SI value (1/s). This
   raises the possibility that Convention A and B are not two distinct
   physical couplings at all, but one coupling inconsistently converted
   between natural units and SI -- which would change the fix from "split
   the symbol" to "apply one consistent conversion everywhere." Not yet
   verified either way.
3. **Sudoku blind spot found:** Part 131's S9 (`m^2=2g*sin(Delta_+)`,
   PASS) checks internal algebraic consistency (does the formula match an
   independently re-derived series expansion?), not absolute dimensional
   correctness -- it would PASS even with the wrong units for g. Every
   existing "PASS" cited for a g-dependent formula needs re-reading to
   check which kind of consistency it actually verifies before being used
   as evidence.
4. **The "~42 orders of magnitude" figure itself doesn't reproduce** on a
   first-pass hand check (a ~21-22 order swing was found instead, from
   `sqrt(omega_gap^2/omega_gap) = sqrt(omega_gap)`). Flagged, not resolved
   -- redo this calculation from scratch, with every substitution shown,
   once the per-Part checklist below has settled what g should actually be.

**Per-Part checklist (work through IN ORDER, one at a time; for each:
write the exact equation with every symbol's units, solve for what [g] it
requires, note whether the Part declares SI or natural units explicitly,
and classify against the 3 hypotheses in the scoping doc Sec 6):**

- [x] Part 33 (`vortex_winding_derivation.md`) -- CLEAR: no bare g used;
  G = hbar*c/m_cond^2 has zero dependence on g
- [x] Part 94 (`coupling_constant_g.md`) -- internally consistent given its
  own premise (g=omega_gap); premise superseded by Part 95/128 finding
- [x] Part 95/128 (`emergent_c.md` Result 7; `lambda_locking_fossil.md` Sec
  11) -- **CORRECTED**: [g] = 1/length^2 (SI), not 1/time^2; g =
  omega_gap^2/c^2, not omega_gap^2 alone. Lambda_obs match UNAFFECTED
  (already had a compensating /c^2 elsewhere). SymPy: `t68_g_units_field_
  equation.py`. Full writeup: g_units_audit_scoping.md Sec 7a.
- [x] Part 61/62 (`reversed_higgs.py`) -- **RESOLVED, same bug as Part
  128**: corrected E_rest = hbar*omega_gap*sqrt(2*Phi), exactly
  sqrt(omega_gap)~4.3e21 above the code's original, giving ~4.5e14 GeV at
  Earth's surface (matches the number already on record; swing corrected
  from "~42 orders" to 21.6). SymPy: `t68_g_units_phi_minus_mass.py`.
  Downstream consequence flagged, NOT fixed: falsifiable_predictions.md
  Eq F.12 (hollow-shell test) needs its own plan-first update once the
  full checklist closes. Full writeup: g_units_audit_scoping.md Sec 7b.
- [x] Part 117 (`phi_minus_quartic.md`) -- **CLEAR**: stays symbolic
  throughout, never plugs in numeric g; independently confirms
  [g]=1/length^2 via kbar^2=2g (kbar a genuine wavenumber). No fix needed.
- [x] Part 119/128 (`lambda_locking_fossil.md` Sec 11, T51) -- g_dyn.
  **RESOLVED**: traces to the SAME field equation and the SAME missing-c^2
  reduction bug, found at its root in Part 99's Eq 99.1
  (`d^2Delta/dt^2=-2g*sin(Delta)` drops the c^2 that box(Delta)'s (1/c^2)
  d^2/dt^2 term requires -- SymPy-verified). g_dyn = c^2 x (bare coupling
  for phi_-'s present-epoch dynamics). g_dyn's own number and Part 119's
  EOS/freeze results UNCHANGED (self-consistently calibrated against real
  DESI data). T51's g_Lambda != g_dyn finding UNAFFECTED (shared
  mislabeling cancels in the ratio). **Central audit question now
  RESOLVED: one global bug (Hypothesis 1), not two distinct couplings.**
  See g_units_audit_scoping.md Sec 7d.
- [x] Part 96 (`condensate_layer_optics.md`) -- **CLEAR**: standard Part 94
  dispersion identity; speculative local-mass formula reuses Part 62's,
  same fix, no new mechanism
- [x] Part 113 (`two_phase_tan.md`) -- **CLEAR for T68's own question**
  (reuses Part 99's g, already-resolved bug); surfaced the separate T72
  question (g=omega_gap vs g=omega_gap^2/2), not part of T68's scope
- [x] Part 131 (`phi_minus_local_mass_and_crossover.md` Sec 6-9) --
  **DONE**: "~42 orders" corrected to 21.6 at the source; endpoint
  numbers unchanged

**CHECKLIST COMPLETE: 9/9.**

**What:**
Two incompatible conventions for the bare Lagrangian coupling "g" (as in
L = g cos(psi-phi)) are both live in the project, apparently never reconciled:

1. **Frequency convention** (Parts 33, 94, and by extension 61/62/96/113):
   g is identified directly with omega_gap = m_cond*c^2/hbar (units 1/s).
   Part 94 Eq 94.6-94.7 builds t_P=1/g, E_P=hbar*g, and "omega_gap=g" on this.
2. **1/s^2 convention** (Part 128/T51): derived independently from the field
   equation's own structure -- box(phi) = g sin(psi-phi) with phi dimensionless
   forces [g] = 1/s^2, one power more than a frequency. T51's own stated fix
   ("omega_gap^2, not omega_gap, plays g's role") was applied to the Part 87
   cosmological-constant schematic (giving g_Lambda) but not audited against
   every other formula using bare "g".

**Concrete impact found so far:** applying convention 2's fix to Part 62's
phi_- local mass formula (m^2=2g*Phi) moves its Earth-surface prediction from
~105 eV (as literally coded, convention 1) to ~4.5e14 GeV (convention 2) --
a ~42 order-of-magnitude swing. Separately, Part 119's own g_dyn (already
established specifically for phi_-'s present-day cosmological mass,
correctly dimensioned at 1/s^2) differs from the T51 placeholder omega_gap^2
by another ~60+ orders of magnitude for a neutron-star-scale comparison
(T18/Part 131, Sec 6) -- these are not obviously the same "g" either.

**Key questions:**
- Is "g" in Parts 33/94's derivation (giving G=hbar*c/m_cond^2, l_P=c/g,
  t_P=1/g) actually a DIFFERENT physical object from the Lagrangian coupling
  in box(phi)=g*sin(...) -- e.g. is Parts 33/94's "g" really E/hbar for some
  energy E, with a hidden extra hbar or c factor separating it from the
  literal Lagrangian-coupling g? Or is one of the two conventions simply
  wrong and needs correcting throughout?
- Does G=hbar*c/m_cond^2 (Part 33, THE central circularity-tested result)
  survive unchanged if g is redefined? (It doesn't explicitly use "g" as an
  input in its final form, but was originally derived via the frequency
  convention -- check for hidden dependence.)
- Which convention (if either, unmodified) is the physically correct one for
  LOCAL/static formulas (Part 62's phi_- mass, Part 82's Yukawa length) as
  opposed to the cosmological g_Lambda (Part 128) and g_dyn (Part 119)?
- Sudoku re-check: does EITHER convention, substituted consistently
  everywhere "g" appears project-wide, pass 10+ established equations, or do
  they split into a "these equations need convention 1" / "these need
  convention 2" pattern that itself points at two genuinely different
  physical couplings hiding under one symbol?

**Cross-check with:** Part 33 (G derivation), Part 94 (A6 FCC, g identification),
Part 61-62 (two-phase Lagrangian, phi_- mass), Part 96.7a, Part 113.5 (horizon
mass formula, also uses "2g"), Part 117 (induced quartic, uses g),
Part 119 (g_dyn), Part 128/T51 (the 1/s^2 derivation and g_Lambda).
**Effort:** Unknown, likely HIGH -- this is a project-wide bookkeeping audit,
not a single new derivation. Recommend starting with a **plan** (per
CLAUDE.md's Problem-Solving Protocol) before any code: list every Part/formula
that uses bare "g", classify each by which convention it actually needs
dimensionally, and only then decide whether this is a uniform fix, a
"these are two different objects" reframe, or something else.

---

### [ ] T72 — Reconcile Part 94's g=omega_gap vs Part 99's Implied g=omega_gap^2/2

**Status:** PENDING. Filed 2026-09-06, surfaced while auditing Part 113
for T68 (`docs/research/g_units_audit_scoping.md` Sec 7e).

**What:** Two claimed relationships between the same symbols cannot both
be generally true:

1. **Part 94** (`coupling_constant_g.md`, Eq 94.1, citing Part 34's
   condensate self-consistency): `g = omega_gap = m_cond*c^2/hbar` --
   LINEAR relationship, derived independently of the pendulum equation.
2. **Part 99** (`tan_critical_point.md`, Eq 99.1): the pendulum equation
   `d^2Delta/dt^2 = -2g*sin(Delta)`, linearized near Delta=0, gives small-
   oscillation angular frequency `omega = sqrt(2g)`, i.e. `omega^2 = 2g`
   -- QUADRATIC. Part 113 (`two_phase_tan.md`, lines 46, 228, 234, 237)
   explicitly calls this pendulum frequency "omega_gap" and states
   `2g = omega_gap^2`.

If both `g = omega_gap` and `g = omega_gap^2/2` held for the same g and
omega_gap, it would force `omega_gap = 2` in whatever units -- not
generically true. Either Part 94's omega_gap (a quasiparticle energy-gap
frequency) and Part 99/113's "omega_gap" (the pendulum's own natural
oscillation frequency) are two DIFFERENT physical frequencies that happen
to share a name, or Part 34's original self-consistency argument
independently forces them equal for a reason not yet checked.

**This is explicitly NOT the same question as T68** (which was about SI
dimensions, 1/s vs 1/length^2, and is now resolved) -- this is about
whether two same-named, same-dimensioned quantities are actually the same
NUMBER.

**Proposed step:** read Part 34 (`condensate_selfconsist.py` and its
underlying derivation) directly to see whether it derives g=omega_gap
from the SAME field equation Part 99 uses (in which case the two claims
should already be reconcilable and the discrepancy is a real error to
fix) or from an independent physical argument (in which case they may
simply be two different, correctly-coexisting frequencies that should be
renamed to avoid the collision).

**Effort:** Low-Medium -- reading one Part's original derivation and
checking one algebraic consistency condition.
**Priority:** Medium -- doesn't block anything currently active, but is
exactly the kind of unresolved symbol collision T68 was filed to catch,
now found one level deeper.

---

## Rules

Same as TODO_04:
- One Part at a time
- Every new equation: Sudoku consistency check (10+ tests)
- Every PDTP Original result: SymPy verification
- Every research .md: complete derivation (show your work)
- Python: no Unicode, save output to `simulations/solver/outputs/`
- Plain English explanations for every key result
- Commit after user approval

---

## Group A — Lambda-Locking Deep Dive (T46 Extended)

**Context:** T46 (Part 119, Phase 87) established the Lambda-locking mechanism:
phi_- = pi/2 is the true vacuum; freeze condition eps < 1/9 [Eq 119.2]; thawing
EOS w = -1+2*eps [Eq 119.3]; mechanism consistent; magnitude of phi_minus_vac
remains open. The causal-sync ansatz from the Fable session proposes the resolution.

### [x] T50 — Lambda Causal-Sync Numerical Check — DONE (Part 123, Phase 91)

**Status:** DONE (2026-07-07). Sudoku 11/11 PASS.
**Result:** The O(1) coefficient is EXACT: Lambda_obs/Lambda_naive =
3*Omega_Lambda * (H_0/omega_gap)^2 — algebraic identity (SymPy residual 0),
so C = 3*Omega_Lambda = 2.054 +- 0.022. Closest candidate: the DERIVED Part 61
factor 2, at 2.7% (2.5 sigma). C = 2 exactly <=> Omega_Lambda = 2/3 <=>
freeze-out at z_lock ~ 0.03 (Eq 123.2). Bare-G convention: C_bare = 6*Omega_Lambda
= 4.11 ~ candidate 4 (same 2.7%). New question O5: is the 2.7% gap epoch
dependence (T52 D1 decides)?
**Script:** `simulations/solver/t50_lambda_causal_sync.py`
**Log:** `simulations/solver/outputs/t50_lambda_causal_sync_20260707_191216.txt`
**Doc:** `docs/research/lambda_locking_fossil.md` Section 10
**Source:** `docs/fable_notes/instruction_lambda_locking.md` Section 3

**What:**
Reproduce the order-of-magnitude check from the Fable session using only known
constants. No fitting. Script must be compute-only with no hardcoded return values.

**Core ansatz [SPECULATIVE]:**
phi_minus_vac ~ H / omega_gap
Lambda ~ (H_0 / omega_gap)^2

**Compute targets:**
- Lambda_obs = 3 * Omega_Lambda * (H_0/c)^2 ~ 1.1e-52 m^-2  [Planck 2018]
- Lambda_naive = 1/l_P^2 ~ 3.8e69 m^-2
- Ratio: Lambda_obs / Lambda_naive ~ 2.9e-122
- omega_gap = m_P*c^2/hbar ~ 1.86e43 rad/s  [G-free: uses m_P from calibration]
- Ansatz: (H_0 / omega_gap)^2 ~ 1.4e-122

**Key Sudoku check:**
Is the O(1) coefficient exactly 2 (from G_eff = 2*G_bare, Part 61)?
Or 4*pi? Or 4? Any of these is a Sudoku MATCH of high value. An arbitrary
large number is a problem.

**No-go compatibility note (must be stated in the doc):**
H_0 is an external cosmological input, not an internal PDTP quantity. Using it
does NOT violate the Part 115 no-go theorem (which blocks internal circular
derivations only). The ansatz ties Lambda to expansion history -- genuinely external.

**Sudoku (5 minimum for a cheap check):**
- S1: Lambda_obs / Lambda_naive matches (H_0/omega_gap)^2 within 1 OoM
- S2: omega_gap formula is G-free (verify: omega_gap = m_P*c^2/hbar uses only hbar, c, m_P)
- S3: ratio is dimensionless (dimensional check)
- S4: O(1) coefficient identified and checked against 2, 4, 4*pi
- S5: two-phase check -- G_eff = 2*G_bare shifts prediction by factor sqrt(2); still within OoM

**Deliverables:**
- Script: `simulations/solver/t50_lambda_causal_sync.py`
- Result added as a section to `docs/research/lambda_locking_fossil.md` (extend T46 doc, not new file)

---

### [x] T51 — Dimensional Audit: Lambda = g * phi_minus_vac^2 — DONE [2026-08-05]

**Status:** DONE
**Source:** `docs/fable_notes/instruction_lambda_locking.md` Section 6 kill tests
**Prerequisite:** T50 (re-checked independently, not just imported -- RECHECK rule)
**Script:** `simulations/solver/t51_dimensional_audit.py`
**Log:** `simulations/solver/outputs/t51_dimensional_audit_20260809_193749.txt`
**Doc:** `docs/research/lambda_locking_fossil.md` Section 11 (new)
**Sudoku:** 12/12 PASS

**Result:**
Field equation box(phi) = g*sin(psi-phi) with phi dimensionless forces
[g] = 1/s^2 (frequency squared) -- confirming the "g in the natural-unit sense,
units [mass]^2" flag already present in emergent_c.md Result 7. omega_gap =
m_P*c^2/hbar (Part 33/94) carries dimension 1/s -- ONE POWER SHORT of what g
needs, meaning "g = omega_gap" (CLAUDE.md Eq 4e) and "g" in cos(psi-phi) are
NOT literally the same statement (omega_gap^2, not omega_gap, plays g's role
wherever it appears squared elsewhere, e.g. Part 95 Eq 95.7 -- no existing
numerical result is affected).

**Dimensionally-complete formula [DERIVED]:**
```
Lambda = g_Lambda * phi_minus_vac^2 / c^2
g_Lambda = 3*Omega_Lambda*omega_gap^2 = 7.067e+86 s^-2
```
Reproduces Lambda_obs to 1.000000 using phi_vac_ansatz = H0/omega_gap (the T50
causal-sync ansatz) -- no separate hbar term needed (already inside omega_gap).
Answers T51's own posed question: YES to c^2 in the denominator, NO extra hbar.

**KEY FINDING [NEGATIVE-BUT-USEFUL]:** g_Lambda != g_dyn (Part 119's dynamical
coupling, tied to m^2 = 2*g_dyn) -- they differ by 122 orders of magnitude.
Substituting g_dyn directly into the schematic instead requires phi_vac =
2.196 rad, EXCEEDING pi/2 itself -- inconsistent with the "small displacement
from the true vacuum" picture (Part 119/T46). These are two genuinely distinct
PDTP quantities that were sharing the bare symbol "g" across Parts 87/94 vs 119;
both remain valid for their own purposes, but must not be substituted for each
other. lambda_locking_fossil.md's Open Question O4 (unit reconciliation) is
RESOLVED.

**T52 dependency:** T52's triple-Sudoku chain must use g_Lambda explicitly
(not the bare Part 87 schematic) when feeding measured phi_vac into the Lambda
prediction step.

---

### [ ] T52 — Kuramoto Expanding-Lattice Simulation — PENDING [HIGH, large task]

**Status:** PENDING
**Estimated effort:** several days (build + run + analysis)
**Source:** `docs/fable_notes/instruction_lambda_locking.md` Section 7

**What:**
The decisive numerical experiment for the lambda-locking mechanism. Turns the
ansatz phi_minus_vac ~ H/omega_gap into measured data instead of guesswork.

**Setup:**
- 2D Kuramoto oscillator grid (extend to 3D if 2D shows clear signal)
- Mimic expansion: dilute coupling strength K(t) per an H(t) schedule
  (matter + Lambda + radiation phases)
- Sweep H/K over several decades (H/omega_gap from 1e-60 to 1e-40)

**Measurements:**
- D1: residual phase variance <phi_minus^2> vs H/K
  -- confirm or refute phi_minus_vac ~ H/g; extract O(1) coefficient
- D2: order parameter r(t) -- compute beta(z) = arccos(r) directly from data
- D3: freeze-out verdict -- sharp (laser-threshold like) or gradual?

**Triple Sudoku chain (jackpot structure -- 3 observables, 1 simulation):**
- Feed measured beta(z) into lambda_4 = 2g^2 sin^2(beta)/(3 kbar^2) [Part 117]
  -- predict EDE amplitude; check <= 10% bound
- Feed phi_minus_vac into Lambda = g*phi_minus_vac^2 [Part 87]
  -- predict Lambda today; compare to 1.1e-52 m^-2
- Feed beta(z) into Part 102 loss tangent
  -- predict w_0/w_a; compare to DESI targets (CONTESTED; see T53)

**Candidate B preference:**
Kuramoto critical dynamics gives sharp recent lock -- matches freeze-out story and
Part 110 laser-threshold critical exponents (beta=1, nu=1/2). Start with Candidate B.

**LCDM branch requirement (from DESI update):**
Report which H/K regions give sharp freeze-out (DESI branch) vs early gradual lock
(pure LCDM branch). Do NOT assume the DESI w_a hint is real.

**Script:** `simulations/solver/t52_kuramoto_expansion.py`
**Doc:** new `docs/research/kuramoto_expansion.md`

---

### [ ] T53 — Phantom Crossing Derivation — PENDING [HIGH, new from DESI update]

**Status:** PENDING
**Estimated effort:** half-day to 1 day
**Source:** `docs/fable_notes/desi_update_lambda_locking_amendments.md` Section 4

**What:**
DESI best-fit: w ~ -1.7 at high z, crossing to w > -1 today. Ordinary scalar
fields cannot cross w = -1 without ghost instabilities. PDTP candidate (Task 4b):
the dark energy sector is NOT closed during active locking (alpha = cos(Delta)
evolving means energy flows between matter and condensate), so effective w < -1
may be possible without real ghosts.

**Required derivation:**
1. Derive effective w(z) of partially-locked phi_minus INCLUDING energy exchange
   with matter sector (Part 61 two-phase equations as starting point)
2. Determine if phantom-to-quintessence crossing at lock completion is generic
   or requires tuning
3. Verify ghost-freedom (kinetic term positive definite in the two-phase Lagrangian)

**Sudoku:**
- S1: w(z_lock) = -1 exactly (phi_minus frozen -> pure cosmological constant)
- S2: w at z >> z_lock -- compatible with matter domination (dark energy subdominant)
- S3: ghost check -- kinetic term positive definite throughout
- S4: two-phase check -- consistent with Part 61 equations
- S5: DESI target -- can w_0 ~ -0.7, w_a ~ -1 be reproduced without tuning?

**If ghost-free crossing derived:** major result; full Sudoku suite + SymPy.
**If it fails:** document as NEGATIVE (ghost instability, requires new mechanism);
the failure tells us where DESI signal cannot come from.

**Script:** `simulations/solver/t53_phantom_crossing.py`
**Doc:** section appended to `docs/research/lambda_locking_fossil.md`

---

### [ ] T54 — Prior Art Section — PENDING [MEDIUM, research doc]

**Status:** PENDING
**Estimated effort:** ~2 hours (literature review + writing)
**Source:** `docs/fable_notes/instruction_lambda_locking.md` Section 6

**What:**
Lambda ~ H_0^2 proposals have a long history. The PDTP doc must cite prior art
and state precisely what PDTP adds (mechanism + freeze-out), not just the number.

**Prior art to cite:**
- Zel'dovich (1968): Lambda ~ (G*m_p^2/hbar*c)^6 * m_p^2*c/hbar^3 -- numerology
- Running vacuum models: Shapiro & Sola -- Lambda running as H^2
- Holographic dark energy: Li (2004) -- L = c^2/L_H^2 from causal horizon
- Cohen-Kaplan-Nelson (CKN) bound (already in T46 doc)

**What PDTP adds (explicit statement required):**
1. MECHANISM: causal sync limit from cos(psi-phi) coupling -- not numerology
2. FREEZE-OUT history: explains structure formation, coincidence problem, DESI hint
3. Falsifiable output: beta(z) shape from T52 simulation

**Deliverables:**
- Section "Prior Art and Comparison" appended to `docs/research/lambda_locking_fossil.md`
- All URLs verified (run check_urls.py)

---

## Group B — Multi-Medium Framework

**Context:** PDTP has (at minimum) three interpenetrating condensates: gravitational
(m_P), EM (m_cond_EM unknown), QCD (~367 MeV, Part 37). Same Lagrangian structure;
only stiffness differs. Stiffness ratios are hard predictions (not free parameters).
Session source: `docs/fable_notes/session_summary_dm_mcond_unification.md`

### [x] T55 — Dvali-Gomez Criticality as Attractor — PARTIAL (Part 124, Phase 92)

**Status:** PARTIAL (2026-07-07). Sudoku 12/12 PASS.
**Result:** alpha_gr = 1 is NOT an equilibrium attractor — energy landscape has a
BARRIER at criticality (d2E/dm2 < 0, Eq 124.1) and entropy has a MINIMUM there
(Eq 124.2); both extremum routes NEGATIVE, as required by no-go 115.4. But the
dissipative flow works one-sided: horizon grains evaporate in finite time
t = 5120*pi*G^2*m^3/(hbar*c^4) while subcritical grains are stable, and the
cascade terminates at E_final = m_P*c^2 exactly (Part 47 re-verified, Eq 124.4).
So alpha_gr = 1 is a stability boundary / evaporation endpoint: m_cond <= m_P*O(1)
DERIVED (dynamical ceiling). Equality step (why AT the ceiling: maximal packing /
KZ formation bias) remains OPEN (124-O1) — the hierarchy problem reduces to
"why does the condensate saturate its own stability bound?" Character = driven
criticality (laser-threshold pattern, Part 110, qualitative; exponents OPEN 124-O2).
**Script:** `simulations/solver/t55_dvali_gomez_attractor.py`
**Log:** `simulations/solver/outputs/t55_dvali_gomez_attractor_20260707_193711.txt`
**Doc:** `docs/research/dvali_gomez_attractor.md`; C4 update in
`docs/research/hierarchy_problem_reframe.md`
**Source:** `docs/fable_notes/session_summary_dm_mcond_unification.md` TC1

**What:**
Part 115 proved the no-go theorem: m_cond is externally underdetermined. But Part 115
also found Dvali-Gomez criticality (alpha_gr = 1, every condensate grain is marginally
its own black hole) is satisfied at EXACTLY m_cond = m_P with ALL bounds simultaneously
saturated. The question: is alpha_gr = 1 an ATTRACTOR of condensate dynamics (not
an assumed input)?

If yes, m_cond = m_P is the stable fixed point of the self-organization dynamics --
the only no-go-compatible route to "derive" m_cond.

**Derivation strategy:**
1. Write condensate self-energy as a function of m_cond (Lagrangian structure fixed,
   grain mass varied)
2. Compute d(alpha_gr)/d(m_cond); find fixed points
3. Check stability: d^2E/d(m_cond)^2 > 0 at alpha_gr = 1? (energy minimum = attractor)
4. Link to Part 110 laser-threshold universality class (beta=1, nu=1/2) -- same class?

**No-go compatibility (must be stated explicitly):**
The no-go theorem blocks internal ALGEBRAIC ratios pinning m_cond. An attractor
argument derives m_cond from DYNAMICS (energy minimization), not from algebra. These
are different: one is circular substitution, the other is a stability condition.

**Sudoku (if attractor confirmed):**
- S1: alpha_gr computed FROM m_cond = m_P (not assumed); verify = 1.000
- S2: r_S = 2*a_0 (Schwarzschild = 2*Compton) at the fixed point
- S3: G = hbar*c/m_cond^2 gives G_pred = G_known at the fixed point
- S4: all Part 115 bounds saturated simultaneously at the fixed point

**Script:** `simulations/solver/t55_dvali_gomez_attractor.py`
**Doc:** `docs/research/dvali_gomez_attractor.md`

---

### [ ] T56 — QCD/Gravitational Stiffness Ratio — PENDING [HIGH]

**Status:** PENDING
**Estimated effort:** 1 day (analytical + Sudoku)
**Source:** `docs/fable_notes/session_summary_dm_mcond_unification.md` TC2

**What:**
m_cond_QCD ~ 367 MeV (Part 37) and M_0 ~ 313.84 MeV ~ m_p/3 (Part 32, 0.3%)
arise from the same Lagrangian structure. If the formula giving m_cond_QCD extends
to the gravitational condensate, the stiffness ratio m_P / m_cond_QCD might be
computable from QCD running couplings -- giving m_cond_grav from measured QCD data.

**Key quantities:**
- m_cond_QCD ~ Lambda_QCD ~ 200 MeV (Part 37: 367 MeV from sigma fit)
- m_P = sqrt(hbar*c/G) ~ 2.176e-8 kg
- Ratio: m_P / m_cond_QCD ~ 3.6e19
- Candidate derivation: does this ratio = exp(8*pi^2/g_s^2) or similar from
  the QCD running coupling? (SU(3) beta function is negative -- asymptotically
  free; U(1) PDTP beta function is positive -- IR free. Different structure.)

**Sudoku:**
- S1: m_cond_QCD from formula within 10% of Part 37 value (367 MeV)
- S2: stiffness ratio dimensionless (dimensional check)
- S3: ratio from QCD running coupling -- does it match 3.6e19?
- S4: if ratio derivable, compute m_P prediction; verify vs known value

**Script:** `simulations/solver/t56_stiffness_ratio.py`
**Doc:** `docs/research/stiffness_ratio.md`

---

### [ ] T57 — Cross-Medium Coupling Sudoku — PENDING [MEDIUM]

**Status:** PENDING
**Estimated effort:** half-day (Sudoku checks; no new derivation required)
**Source:** `docs/fable_notes/session_summary_dm_mcond_unification.md` TC3

**What:**
GR requires: EM field energy gravitates. PDTP must reproduce this. In PDTP, psi_EM
locks to phi_grav (like any matter), so photon energy does gravitate. But: what
prevents phi_grav from directly phase-locking to A_mu (the EM condensate field)?

**Sudoku tests:**
- S1: photon gravitational lensing -- psi_photon locking gives 1.75" deflection
  (Part 112 GR recovery); verify it comes from psi-phi coupling, not condensate-condensate
- S2: Shapiro delay for light -- consistent with GR gamma=1 (Part 112)?
- S3: EM stress-energy source -- does PDTP's picture produce the GR T_mu_nu^EM source term?
- S4: condensate-condensate coupling amplitude -- what suppresses phi_grav locking to A_mu?
  (Expected suppression: the coupling constant ratio m_cond_grav/m_cond_EM ~ sqrt(1e36))
- S5: Lorentz invariance -- EM condensate must not introduce a preferred frame;
  c_s = c must hold independently (Part 34) -- **DONE (conversational check,
  2026-08-01), PASS but TAUTOLOGICAL.** SymPy re-derivation of Part 95 Result 1
  (Eqs 4a/4d closure ansatz) confirms c_s^2 = c^2 is an exact algebraic identity
  for ANY m_cond -- residual = 0 even for an independent m_cond_EM. Numeric check
  using T58's own candidate m_cond_EM = sqrt(4*pi*eps0*hbar*c) ~= 1.876e-18 kg
  (11.6 billion times lighter than m_P) still gives c_s_EM/c = 1 to machine
  precision (deviation ~2e-16). Cross-check via standard EM (c = 1/sqrt(mu0*eps0))
  also exact by 2019 SI definition. GW170817's real bound (Abbott et al. 2017,
  ApJL 848, L13: -3e-15 <= delta <= +7e-16) was translated into a fractional
  stiffness-ratio window eps_EM = (Xi_EM/Xi_grav - 1) in [-1.4e-15, +6e-15] --
  a genuine, sharp number, but ONLY relevant if a future refinement gives the EM
  condensate an independently-motivated stiffness parameter not cloned from
  gravity's closure ansatz. As currently formulated, the multi-medium framework
  has no free parameter GW170817 could have falsified -- same tautological
  flavor as Result 2's "circular in isolation" note in emergent_c.md. S5 PASSES;
  S1-S4 remain PENDING (T57 overall status unchanged).

**Doc:** section in new `docs/research/multi_medium_framework.md`

---

### [ ] T58 — EM Condensate Quantum Mass — PENDING [LOW PRIORITY]

**Status:** PENDING
**Estimated effort:** ~1 hour (one glossary row or short scoping note)
**Source:** `docs/fable_notes/session_summary_dm_mcond_unification.md` TC4

**What:**
The 1e36 grav/EM ratio is stated in PDTP but no explicit m_cond_EM appears in
the current docs. Either locate it in the repo (Parts 22, 28b, 36) or compute it:

If G_EM analogue = k_e = 1/(4*pi*eps_0), then by G = hbar*c/m_cond^2:
m_cond_EM = sqrt(hbar*c*4*pi*eps_0) -- compute and add to term_glossary.md.

**Cross-check:**
- m_P / m_cond_EM should equal sqrt(k_e/G) = sqrt(alpha * m_P^2/m_e^2) -- verify
- Is m_cond_EM related to m_e (electron mass) or the fine structure constant?

**Deliverable:** one row in term_glossary.md + one sentence in multi_medium_framework.md

---

### [ ] T67 — Galactic Disk "Flapping" as DM-Wake Phenomenology — PENDING [LOW PRIORITY]

**Status:** PENDING (initial findings only, filed 2026-08-05; deeper pass deferred)
**Estimated effort:** unknown -- no calculation attempted yet, scoping note only
**Source:** conversational review, 2026-08-05; see `docs/research/galactic_disk_dynamics_note.md`

**What:**
The Milky Way's disk is warped and actively driven, not static -- the Large/Small
Magellanic Clouds orbiting through the dark matter halo excite a gravitational
wake (Weinberg & Blitz 2006, "A Magellanic Origin for the Warp of the Galaxy",
ApJ 641, L33) that resonantly couples to and drives the disk's vertical bending
modes; press coverage at the time called this "flapping." Initial findings
(mainstream mechanism + a tiered, honestly-scoped PDTP connection) are written
up in the new doc above. Three tiers, in order of how derived they are:
1. Structural compatibility only (PDTP's condensate already supports waves and
   has its own natural modes -- same ontology as any dark-matter-as-medium
   picture, nothing new)
2. Genuinely open question: does Part 116's Planck-vortex DM (topological, not
   collisionless-particle) change the wake's propagation/dissipation compared
   to standard LCDM? Not computed anywhere.
3. Speculative, unquantified idea: a wake-driven local condensate density dip
   could leave a trailing variable-c signature (Part 95 Result 5), IF gravity
   and EM condensates are coupled -- stacks on T57's still-open, still-
   tautological multi-medium question, so flagged as an idea, not a prediction.

**Deliverable so far:** `docs/research/galactic_disk_dynamics_note.md` (initial
findings, explicitly marked preliminary/exploratory, not Sudoku-checked).

**Next steps (not started):** quantify tier 2 (does topological vortex DM wake
differently than collisionless DM?); quantify tier 3 only after T57 gets an
actual free stiffness parameter to hang it on.

---

### [ ] T59 — Weak Force Placement Note — PENDING [LOW PRIORITY]

**Status:** PENDING
**Estimated effort:** ~1 hour (scoping doc; deferred answer acceptable)
**Source:** `docs/fable_notes/session_summary_dm_mcond_unification.md` TC5

**What:**
No SU(2) extension or fourth condensate appears in current PDTP docs. The weak
force must go somewhere. Two candidate routes:
(a) SU(2) condensate with its own m_cond_weak (analogous to the SU(3) extension, Part 37)
(b) Weak force rides an existing condensate with Higgs-like symmetry breaking from
    phi_minus (phi_minus is a "reversed Higgs", Part 62)

Per the Open Problem Tracking Rule, even "not yet investigated" must be recorded.

**Deliverables:**
- `docs/research/weak_force_placement.md` (< 1 page; scoping only)
- Add as OPEN question to equation_reference.md

---

## Group C — Relative Entropy as Bridge to Einstein Equations

**Context:** External proposal, not a Fable session — a ChatGPT session reviewing a
paper that derives semiclassical Einstein equations from quantum relative entropy
(chain: quantum state difference -> relative entropy -> horizon area variation ->
Raychaudhuri equation -> Einstein equations) rather than assuming them. The session
noticed this chain is structurally close to PDTP's own phase-locking -> gravity
chain and proposed replacing "quantum state difference" with the PDTP phase mismatch
Delta_theta = psi - phi. Per the External AI Reviews rule (CLAUDE.md): this session
only had `term_glossary.md`, `CLAUDE.md`, and general knowledge — it did NOT have
access to Part 86, which already built a (different) entropy-area law inside PDTP.
Source: `docs/fable_notes/fable notes to check 02.md`.

**IMPORTANT PRIOR ART WITHIN PDTP (the proposal did not know this):**
Part 86 (`docs/research/nonlinear_einstein.md`) already derived an entropy-area law
by counting condensate lattice cells inside a horizon:
```
   S_PDTP = k_B * ln(2) * A / a_0^2                    [Part 86, Eq 86.7, DERIVED]
```
and fed it into Jacobson's (1995) thermodynamic argument (Clausius relation across
local Rindler horizons) to recover the FULL nonlinear Einstein equation, exactly
matching Bekenstein-Hawking at lattice spacing a_0 = 1.665*l_P (Eq 86.10-86.15,
Sudoku 12/12 PASS, Part 86 Section 5.3). So the BOTTOM half of the proposed chain
(area variation -> Einstein equations) is already done in PDTP via Jacobson + cell
counting. What is NEW in the ChatGPT proposal is the TOP half: deriving entropy
directly from the phase-mismatch/coupling-energy V = g*cos(psi-phi), rather than
from counting cells. T60 is scoped to check whether the two entropy formulas are
consistent (same physics, two derivations) before treating this as a new area-law
derivation.

### [x] T60 — Relative Entropy From Phase Mismatch — DONE (Parts 126 + 127)

**Status:** DONE (2026-07-08). Task 3 (Part 126): Sudoku 9/10. Task 2 (Part 127): Sudoku 12/12.
**Result (Task 3):** S_rel := 1-alpha (the proposal's candidate) is NOT the same object
as Part 86's S_PDTP = k_B*ln(2)*A/a_0^2 -- S_rel is a local continuum scalar (a renaming
of the existing V=g*cos(psi-phi) coupling, [ASSUMED] not derived); S_PDTP is a discrete,
horizon-area-extensive counted entropy. No limit of one reduces to the other (ratio
1.4427, Eq 126.2). S_rel CANNOT derive an area law by itself -- doing so requires
postulating an area integral (Eq 126.3) that is structurally the SAME TYPE of assumption
Part 86 already made via cell counting; it is not a free derivation. Using the
independently-established alpha_horizon=0 result (Part 98/T1, TIR), the postulated area
integral gives a THIRD candidate lattice spacing a_0 = 2*l_P (Eq 126.4) -- within 20% of
Part 86's 1.665*l_P pairwise, but the FULL three-way spread (adding Sakharov N_eff,
Part 83) is 30.3%, WIDER than the existing two-way 18% spread (Part 86 Sec 5.5). Honest
finding, not hidden (Sudoku T10 recorded miss).
**Recommendation:** Tasks 1 and 4 (derive S_rel from the Lagrangian; attempt the full
area-law chain) NOT RECOMMENDED as literally proposed -- would restate existing content.
**Task 2 DONE (Part 127, Phase 95):** phi_-'s own dynamics DO reproduce Part 86's
ln(2)-per-cell factor EXACTLY -- see Task 2 checklist item below for the full result.
T60 net verdict: the external proposal as literally stated does not work, but the
question it raised, pursued seriously, upgraded one Part 86 input from ASSUMED to
DERIVED. No further T60 work planned (Task 5 not needed -- Task 2's result reproduces
an EXISTING number rather than introducing a new one requiring the full Sudoku suite).
**Scripts:** `simulations/solver/t60_relative_entropy_prereq.py` (Task 3, Part 126);
`simulations/solver/t60_task2_horizon_degeneracy.py` (Task 2, Part 127)
**Logs:** `simulations/solver/outputs/t60_relative_entropy_prereq_20260708_171626.txt`;
`simulations/solver/outputs/t60_task2_horizon_degeneracy_20260708_181131.txt`
**Docs:** `docs/research/nonlinear_einstein.md` Sections 10 (Part 126) and 11 (Part 127)
**Source:** `docs/fable_notes/fable notes to check 02.md` (external ChatGPT session, 2026-07-08)

**Candidate hypothesis [SPECULATIVE, from the notes]:**
```
   S_rel ~ 1 - cos(Delta_theta) = 1 - V/g   ,   Delta_theta = psi - phi   (candidate)
```
Small-mismatch limit: 1 - cos(x) ~ x^2/2, so S_rel ~ (Delta_theta)^2 -- a standard
quadratic information-geometry form. At Delta_theta = 0 (full lock): S_rel = 0. At
Delta_theta = pi/2 (alpha = 0, full decoupling): S_rel maximal.

**Task checklist (from the notes, triaged against Part 86 by Task 3):**
1. [ ] CLOSED / NOT RECOMMENDED — derive an entropy functional directly from the
   existing U(1) Lagrangian. Part 126 found S_rel=1-alpha is [ASSUMED] (a renaming),
   not derivable from the Lagrangian's variational structure; no further work planned.
2. [x] DONE (Part 127, Phase 95) — repeat for the two-phase Lagrangian; investigate
   whether phi_- (surface mode) corresponds to boundary/horizon information. RESCOPED
   by Part 126: can phi_-'s OWN dynamics reproduce/refine Part 86's ln(2)-per-cell
   factor, rather than assuming 2-state counting? ANSWER: YES, EXACTLY. cos(D+)=0 at
   the horizon (Part 98) has exactly 2 roots (D+=+-pi/2); each sources a phi_- vacuum
   (+pi/2 or -pi/2) via the Part 61 coupling, both at V_min=-2g EXACTLY (degenerate);
   the two branches are CP-conjugate (Part 125's already-proved CP-evenness); ground-
   state degeneracy=2 gives S_cell=k_B*ln(2) EXACTLY matching Part 86 Eq 86.7's
   ASSUMED value (ratio=1.000000). Mass m^2=2g branch-independent (consistent w/
   Part 113). CP-violation (Part 125) splits degeneracy by ~1e-13 (negligible,
   [SPECULATIVE] magnitude only). Does NOT determine a_0 (Part 86 Sec 8.3 still OPEN).
   12/12 Sudoku (1 representation bug found+fixed during work, not a physics error).
3. [x] DONE (Part 126) — **PREREQUISITE CHECK:** does S_rel reduce to, or relate
   to, S_PDTP = k_B*ln(2)*A/a_0^2 (Part 86) in any limit? Answer: NO, they are
   different kinds of object (local continuum scalar vs discrete horizon-counted
   entropy); no limit connects them. See Result summary above.
4. [ ] CLOSED / NOT RECOMMENDED — attempt the chain phase mismatch -> relative
   entropy -> area variation -> Einstein equations. Part 126 found this requires
   the same postulate Part 86 already made (Eq 126.3) and does not tighten the
   existing O(1) uncertainty (Section 10.6); would restate existing content.
5. [ ] PENDING, contingent on Task 2 — full Sudoku suite: two-phase compatibility
   (Part 61/63), Newton's laws, GR recovery (Part 112), Hawking derivation
   (Part 24/111), PPN (Part 112), massive breathing mode (Part 62/119). Only
   relevant if Task 2 produces a new result to test.

**Deliverables (once scoped):**
- Script: `simulations/solver/t60_relative_entropy.py` (if the prerequisite check
  in task 3 finds new content beyond Part 86)
- Doc: section in `docs/research/nonlinear_einstein.md` (extend Part 86, do not
  duplicate) OR new `docs/research/relative_entropy_bridge.md` if genuinely distinct

---

## Group D — Millennium Prize Problem Connections

**Context:** Opened 2026-07-11 while reviewing an external paper (Klingman, "The Origin
of Quarks in Quantum Gravity," JMP 2024) that invoked the Yang-Mills Millennium Problem's
NAME to lend credibility to an unrelated, self-contained derivation. That review prompted
a full pass over all seven Millennium Prize Problems to check honestly which (if any)
PDTP actually touches. Reference doc:
`docs/technical/The Seven Millennium Prize Problems.md` (all seven, with type,
plain-English description, and an explicit relevance verdict for each).

**Screened out, not filed as TODO items (no plausible PDTP connection):**
P vs NP, Hodge Conjecture, Birch and Swinnerton-Dyer Conjecture. Filing these anyway
would be exactly the kind of unearned-connection padding this project's rigor rules
exist to prevent.

**Filed below (all indirect; none claim to solve or contribute to the actual problem):**

### [ ] T61 — Riemann Hypothesis Connection Revisit — PENDING [SPEC, LOW PRIORITY]

**Status:** PENDING
**Source:** `docs/technical/The Seven Millennium Prize Problems.md` #3; cross-ref
TODO_03.md Category H (H1-H4, all SPECULATION, no calculation started)

**What:** TODO_03's Riemann-zeta thread has sat dormant with no concrete starting point.
Consolidate its references with the new Millennium Problems doc, and scope (not
attempt) whether any PDTP structure -- condensate mode density, the phase spectrum of
psi/phi excitations, or the biharmonic dispersion relation -- could plausibly relate to
zeta zero statistics in a Hilbert-Polya sense (zeros as eigenvalues of a physical
Hermitian operator). This is a genuinely hard, unsolved problem in pure mathematics;
the honest expectation is that this stays speculative indefinitely unless a concrete
operator candidate emerges from PDTP's own equations, not the reverse.

**Deliverable:** short scoping note only (no script) -- either a candidate operator
worth writing up, or an explicit NEGATIVE ("no candidate identified") filed back to
TODO_03 Category H.

---

### [ ] T62 — Yang-Mills Mass Gap Non-Overclaiming Statement — PENDING [MEDIUM, integrity/scoping]

**Status:** PENDING
**Source:** `docs/technical/The Seven Millennium Prize Problems.md` #4; direct trigger
for opening Thread D

**What:** PDTP already uses "mass gap" language internally (m^2 = 2g for phi_- at full
lock, Part 62/119; omega_gap = m_P*c^2/hbar throughout) and runs real lattice SU(3)
gauge theory calculations (Parts 37-41: Wilson action, Metropolis Monte Carlo, string
tension). Both are genuinely useful PDTP results. Neither is a contribution to the
axiomatic Clay Millennium Problem (rigorous constructive QFT existence + proof of a
mass gap satisfying the Wightman/Osterwalder-Schrader axioms). The risk: future
sessions (or external readers) could conflate the two, exactly as the external paper
reviewed 2026-07-11 conflated its own private "mass-gap existence theorem" with the
real, unsolved problem.

**Deliverable:** a short, explicit scoping paragraph -- added to
`docs/research/equation_reference.md` or a new short note -- stating plainly what
PDTP's mass-gap results are (effective-theory results internal to the PDTP Lagrangian)
and are NOT (no claim on the Clay problem). No new derivation required; this is a
documentation/integrity task.

---

### [ ] T63 — Navier-Stokes / Superfluid Condensate Scoping — PENDING [SPEC, LOW PRIORITY]

**Status:** PENDING
**Source:** `docs/technical/The Seven Millennium Prize Problems.md` #5

**What:** PDTP's spacetime condensate is described in Gross-Pitaevskii/superfluid terms
(Part 34: c_s = c exactly; general wave-effects catalog, Part 28c). Classical
Navier-Stokes governs viscous fluid flow -- a different regime (classical, dissipative,
3D PDE) from PDTP's quantum phase-field equations (dispersive, non-dissipative at the
level considered so far). Scope whether there is ANY legitimate bridge, or whether this
is purely a loose surface-level analogy (superfluid vs. viscous fluid) not worth
pursuing further.

**Expected outcome:** NEGATIVE -- but must be stated explicitly with reasoning, not
silently assumed, per the Open Problem Tracking Rule.

**Deliverable:** short scoping note only (no script).

---

### [ ] T64 — Poincaré/Geometrization Method Scoping — PENDING [SPEC, LOW PRIORITY]

**Status:** PENDING
**Source:** `docs/technical/The Seven Millennium Prize Problems.md` #7

**What:** The Poincaré Conjecture itself is solved and has no direct PDTP content. But
Perelman's SOLUTION METHOD -- Ricci flow (∂g/∂t = -2*Ric(g), a geometric relaxation
equation) combined with "surgery" to handle singularities -- is a general mathematical
TOOL, independent of the specific theorem it was used to prove. PDTP already compares
competing topological defect configurations by energy (Part 106: Hopf-link vs.
Y-junction baryon, E_H/E_Y = 2*pi). Scope whether a Ricci-flow-like relaxation dynamic
could offer a more systematic (rather than case-by-case) way to identify PDTP's
topological ground states, or whether the existing energy-comparison approach is
already sufficient and this would add complexity without new results.

**Deliverable:** short scoping note only (no script) -- proceed to a full investigation
only if a concrete, tractable formulation emerges.

---

## Previously Open — Now Resolved

| Item | Resolution | Part | Key result |
|------|-----------|------|-----------|
| T50 — Lambda causal-sync check | DONE, 11/11 Sudoku | Part 123 (Phase 91) | C = 3*Omega_Lambda = 2.054 (closed form); 2.7% from derived factor 2; z_lock ~ 0.03 if C = 2 |
| T55 — Dvali-Gomez attractor | PARTIAL, 12/12 Sudoku | Part 124 (Phase 92) | alpha_gr=1 = stability boundary (one-sided attractor); m_cond <= m_P*O(1) DERIVED; equality step OPEN (124-O1) |
| T60 Task 3 — Relative entropy prerequisite check | DONE, 9/10 Sudoku | Part 126 (Phase 94) | S_rel != S_PDTP (different object types); cannot derive area law without Part 86's same postulate; Tasks 1/4 closed |
| T60 Task 2 — phi_- horizon degeneracy | DONE, 12/12 Sudoku | Part 127 (Phase 95) | Two CP-conjugate horizon branches source exactly-degenerate phi_- vacua; S_cell=k_B*ln(2) EXACTLY matches Part 86 Eq 86.7 (ASSUMED -> DERIVED); a_0 still open |

---

## Assets

**HTML Visualizations (Gemini, 2026-07-04):**
- `assets/visualizations/gemini-code-1783012329313.html` -- Planck Vortex Relic (n=1) animation
- `assets/visualizations/pdtp_spacetime_and_matter.html` -- Spacetime phase-locking animation
Open in any browser.

**Source notes (Fable sessions):**
- `docs/fable_notes/session_summary_dm_mcond_unification.md` -- DM/m_cond session (2026-07-02)
- `docs/fable_notes/instruction_lambda_locking.md` -- T46 attack plan (2026-07-02)
- `docs/fable_notes/desi_update_lambda_locking_amendments.md` -- DESI DR2 update (2026-07-04)
