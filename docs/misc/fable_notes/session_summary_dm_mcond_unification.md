# Session Summary: Dark Matter, m_cond, Multi-Medium Picture, and QM/GR Unification

**Purpose:** Hand-off summary for Claude Code. Captures a claude.ai discussion that
walked through the PDTP dark matter candidate, routes to determining m_cond, the
multi-condensate ("multi-medium") picture, and how PDTP addresses the GR/quantum
merge. Includes proposed next steps and honest gaps to verify against the full repo.

**Source basis:** `term_glossary.md`, `CLAUDE.md`, `electricity_phase_terms.md` only.
The full repo was NOT available in this session — verify all claims against
TODO_04.md and the research docs before acting on anything here.

**Status of this document:** [SPECULATIVE] discussion notes. Nothing here is a new
derivation. All tags ([DERIVED], [VERIFIED], etc.) are quoted from the uploaded files.

---

## 1. Dark Matter in PDTP (Planck Vortex Relic, Part 116)

Description: DM is not a new particle species. It is a topological defect (winding
n=1 vortex) in the gravitational condensate itself — the gravitational analogue of
the Charge Carrier (charge-vortex in the EM condensate).

* What it is: A winding n=1 vortex in the spacetime phase field (phi)
    * Topological defect: walking any loop around the core, phi winds by a full
      2*pi. This winding cannot be smoothed away by any continuous adjustment —
      removal would require a discontinuous phase jump (infinite cost).
    * Core: phi is undefined at the exact center; condensate density drops to
      zero there (same structure as a superfluid vortex core).
    * Mass: energy of the forced phase misalignment = one condensate quantum.
      m_DM = m_cond = m_P [DERIVED, Part 116] via two independent arguments
      (vortex stability energy argument + Kibble-Zurek Monte Carlo, n=1 at ~96%).
* Why it is dark: made of the medium, not of matter
    * A phi-vortex has no charge-phase orientation (no U(1)_EM winding), so it
      cannot couple to Light Messengers. Zero EM interaction; gravitational only.
* Formation: Kibble-Zurek mechanism at the cosmological phase transition
    * Causally disconnected regions chose phases independently; mismatched
      patches trapped windings when they met.
* Self-interaction: sigma/m = 4*pi*G^2*m_DM/v^4 (Part 118 erratum, NOT G/c^4)
* Known problems (already tracked in the files)
    * Abundance gap: KZ production is ~50 orders of magnitude too low; requires
      a post-inflation production channel (open problem).
    * Kill test: CMB tensor modes (r) at LiteBIRD / CMB-S4. No r signal = the
      Planck vortex relic candidate is dead.

---

## 2. m_cond: What Can and Cannot Be Calculated

Description: The Part 115 no-go theorem [proven, per glossary] blocks any internal
derivation — every internally constructible observable scales as a pure power of
m_cond, so no internal ratio can pin it down. Routes split into calibration vs
external derivation.

* Route 1 — Calibration by measurement (current, legitimate)
    * From G = hbar*c/m_cond^2 [Part 33], invert: m_cond = sqrt(hbar*c/G)
    * Numerically: sqrt(3.162e-26 / 6.674e-11) = 2.176e-8 kg = m_P (matches glossary)
    * This is calibration, not derivation. Per the no-go theorem, this is the
      ceiling for internal methods.
* Route 2 — External derivation (the only loophole the no-go theorem leaves)
    * Dvali-Gomez criticality as a physical principle: alpha_gr = 1 (each
      condensate quantum marginally its own black hole; Schwarzschild radius
      approx equals Compton wavelength). All Part 77/78 bounds saturated at
      exactly this condition — circumstantial evidence it is the real answer.
      If criticality can be shown to be an ATTRACTOR of condensate dynamics
      (not an input), m_cond = m_P becomes explained rather than fitted.
    * QCD ladder: m_cond_QCD approx 367 MeV (Part 37) and Koide M_0 approx
      313.84 MeV approx m_p/3 (0.3% match; origin open). If the SU(3)
      condensate quantum mass is derivable from QCD (which has no free gravity
      parameter) and the same formula structure applies to the gravitational
      condensate, the stiffness ratio between condensates might be computable —
      giving m_cond from measured QCD quantities. Most promising
      internal-adjacent route.
    * Experimental via omega_gap: m_cond = hbar*omega_gap/c^2. The JPD testbed
      (Nb ring + Josephson array, ~6 ppm predicted signal) measures omega_gap
      harmonics without routing through G. Agreement with sqrt(hbar*c/G) would
      be a non-circular consistency test.
    * DM back-door: since m_DM = m_cond [Part 116], any astrophysical
      measurement of the DM particle mass (halo cores via sigma/m, or
      microlensing limits on ~22 microgram objects) is a measurement of m_cond.

---

## 3. Multi-Medium Picture (Confirmed Against Uploaded Files)

Description: PDTP as documented is a multi-condensate framework. The condensates
occupy the SAME space (interpenetrating), differing in stiffness. User analogy:
oil / water / air — corrected to "three transparent jellies mixed through the same
room" since the media do not stack spatially.

* Medium 1: Gravitational condensate (phi) — stiffest, stiffness set by m_cond = m_P
    * Carries gravity via phase-locking. Vortices = Planck vortex relic (DM).
    * Note: the Part 61 phi_b / phi_s split is one medium with bulk + surface
      structure (like one droplet), NOT a second medium.
* Medium 2: EM condensate (U(1)_EM / A_mu) — far softer
    * Softness is the stated explanation for EM being 1e36 times stronger than
      gravity (Part 36 two-condensate model). Vortices = Charge Carriers
      (electrons). Messengers = Light Messengers (photons).
* Medium 3: SU(3)/QCD condensate (Part 37, in development)
    * Z_3 fractional vortices (winding 1/3) = quarks; 8 gluons = messengers;
      m_cond_QCD approx 367 MeV.
* NOT media: matter phase fields psi_i
    * Per glossary, each particle has its own psi — individual clocks/waves that
      ride on and lock to the media, not fluids themselves.
* Particle identity = which media a structure grips
    * Electron: IS a vortex in the EM medium AND has a psi locking to the
      gravitational medium (charge + weight; no color).
    * Quark: grips all three (color + charge + weight).
    * DM vortex: knot in the gravitational medium only (weight only; dark).
    * Side benefit: all electrons identical because they are identical knots in
      one shared medium.
* Strategic payoff for the confirmation goal
    * PDTP asserts identical phase-locking mechanics (cos(psi-phi) coupling,
      vortices, gradients, Kuramoto synchronization) in every medium; only
      stiffness differs. Confirming the mechanics in the soft, lab-accessible
      EM medium (superconductors, Josephson junctions, BECs) confirms the
      MECHANISM of gravity, with only the stiffness scaling left to bridge.
      This is what the JPD testbed exploits. Quote from electricity doc:
      "EM systems act as engineering precursors to spacetime phase control."
    * The cross-medium stiffness ratios (1e36; QCD scale vs m_P) are hard
      predictions, not free knobs — each ratio is a Sudoku check candidate.

---

## 4. QM / GR Unification: The PDTP Position

Description: The mainstream merge fails because it quantizes gravity (gravitons,
non-renormalizable infinities) while the two theories disagree about what
spacetime is (fixed stage vs dynamic actor). PDTP inverts the problem.

* Core move: gravity was never fundamental, so there is nothing to quantize
    * The medium is already quantum: spacetime = a BEC of m_cond grains,
      pre-quantized by construction.
    * Gravity = emergent collective phase-locking (alpha = cos(Delta)) between
      matter clocks (psi) and medium clocks (phi) — statistical, like sound
      or temperature.
* Decisive analogy: sound in water
    * Nobody unifies QM with sound; sound is what quantum molecules do
      collectively. Quantizing sound gives phonons — emergent quasiparticles,
      not fundamentals. The graviton hunt is the same category error:
      quantizing the wave instead of identifying the water.
* Where GR comes from: the long-wavelength fluid limit
    * Per the uploaded files, PDTP claims: Hawking temperature [VERIFIED,
      Part 111], PPN gamma=1 beta=1 (Part 112), Newton's laws derived not
      assumed (3rd law: psi_ddot = -2*phi_+_ddot, Part 61), c_s = c exactly
      [DERIVED, Part 34].
* Where the infinities go: the grain cuts them off
    * GR singularities and QG infinities both come from trusting smooth
      spacetime to zero size. Below the healing length the fluid description
      simply ends (like hydrodynamics at atomic scale). A black hole
      "singularity" becomes a finite region of dropped condensate density
      (vortex-core-like), not an infinite point.
* MOND: PDTP does not need it
    * MOND modifies gravity at low accelerations to avoid DM. PDTP keeps
      gravity and supplies DM (vortex relics) instead.
    * PDTP DOES modify gravity, but at SHORT range: biharmonic equation
      nabla^4 Phi + 4*g^2*Phi = source [DERIVED, Part 61], reducing to
      Poisson at long range. Roughly the opposite regime from MOND — a
      distinguishable, testable prediction.
    * Unification bonus: DM and gravity become one medium doing two things;
      MOND cannot offer that.
* Academic context (for grounding, not validation)
    * Emergent/analog gravity has real pedigree (Unruh sonic black holes,
      Volovik superfluid vacuum). Hawking-analogue radiation has been measured
      in lab BECs. PDTP is a specific, falsifiable member of this family.

---

## 5. Honest Gaps (Not Settled by the Three Uploaded Files)

Description: Items flagged during discussion where the uploaded files were silent
or incomplete. Verify against the full repo; do not invent answers.

* Weak force: no fourth condensate or SU(2) extension appears in the uploaded
  files. Does the weak interaction get its own medium or ride an existing one?
* EM condensate stiffness value: the 1e36 ratio is stated, but no explicit
  "m_cond_EM" (EM medium quantum mass) appears. Derived somewhere, or inferred?
* Cross-medium locking: what prevents the gravitational and EM condensates from
  phase-locking to each other directly? Related check: EM field energy DOES
  gravitate in GR — PDTP must reproduce this. Sudoku check candidate.
* Lorentz invariance: any medium framework risks a preferred frame; experimental
  constraints are severe. The stated defense is c_s = c exact from
  self-consistency [Part 34] — must be confirmed to survive every extension
  (two-phase, SU(3), EDE quartic).
* Back-reaction completeness: analog-gravity models historically recover the
  metric but struggle with full Einstein dynamics (matter curving spacetime).
  The claimed answer is psi_ddot = -2*phi_+_ddot (Part 61). This is the crown
  jewel — keep stress-testing it.
* Experimental status: not validated. Pending kill tests: CMB tensor modes (r)
  for the DM candidate; biharmonic short-range deviation; JPD ~6 ppm signal.
* DM abundance: KZ production ~50 orders of magnitude short — the
  post-inflation production channel is an open problem.

---

## 6. Proposed Next Steps (For TODO_04 Consideration)

Description: Candidate tasks surfaced during the discussion, ordered by estimated
value toward the confirmation goal (gravity as emergent phase-locking). User to
approve before any are added to TODO_04.md per project rules.

* Task candidate 1: Dvali-Gomez criticality as an attractor [highest value]
    * Formalize "the condensate self-organizes to alpha_gr = 1" as a
      stability/extremum argument (possible link to the non-equilibrium
      laser-threshold class from Part 110).
    * Then run the full Sudoku suite. If criticality is an attractor of the
      dynamics rather than an input, m_cond stops being a free parameter and
      becomes a fixed point — the only no-go-compatible way to "derive" m_cond.
* Task candidate 2: QCD ladder cross-check
    * Attempt to compute the gravitational/QCD condensate stiffness ratio from
      the same formula structure that gives m_cond_QCD = 367 MeV. Investigate
      the M_0 approx m_p/3 approx m_cond_QCD coincidence (currently open).
* Task candidate 3: Cross-medium coupling Sudoku check
    * Verify PDTP reproduces "EM energy gravitates" (GR requirement) and
      explain what suppresses direct condensate-to-condensate locking.
* Task candidate 4: EM medium stiffness bookkeeping
    * Locate or derive the explicit EM condensate quantum mass / stiffness that
      yields the 1e36 ratio; add it to term_glossary.md if missing (one row).
* Task candidate 5: Weak force placement note
    * Short scoping doc: SU(2) extension vs riding an existing condensate.
      Even a negative/deferred answer should be tracked per the Open Problem
      Tracking Rule.

---

## 7. Workflow Reminders (From CLAUDE.md, For the Coding Session)

* Work from TODO_04.md, one point at a time; user approves before commit/push.
* Every new result: step-by-step derivation in the .md, SymPy verification (or
  written reason why not), equation tags, plain English explanation.
* Sudoku consistency check for any new equation/value: 10+ known equations,
  SM compatibility, two-phase compatibility, Newton's laws check, scorecard.
* Python: ASCII only, DATA output only (no interpretation in code), no
  hardcoded return values (RECHECK checklist), log output to
  simulations/solver/outputs/.
* Problem-solving: plan from docs/Methodology.md before coding; escalate to
  Forced Checklist Check after 3+ failed standard approaches.

---

*Generated 2026-07-02 from a claude.ai session. Verify against the full repository
before acting on any claim above.*
