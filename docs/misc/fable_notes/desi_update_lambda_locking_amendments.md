# DESI Update: Observational Targets and Amendments to the Lambda-Locking Plan

**Purpose:** Hand-off document for Claude Code. Summarizes the DESI DR1/DR2
evolving dark energy results (as of 2026-07), assesses Type Ia supernova
(standard candle) reliability, maps both onto PDTP, and lists concrete
amendments to `instruction_lambda_locking.md`.

**Status:** Observational summary is sourced from a live web search on
2026-07-04 (sources listed in Section 6). PDTP implications are [SPECULATIVE]
until derived and Sudoku-checked. Verify all framework claims against the full
repo. This session had access only to `term_glossary.md`, `CLAUDE.md`, and
`electricity_phase_terms.md`.

**Project rules apply:** Sudoku consistency check, SymPy verification, equation
tags, compute-only ASCII Python, user approval before commit/push or TODO edits.

---

## 1. DESI Findings Summary (DR1 -> DR2, Status 2026)

Description: DESI measures baryon acoustic oscillations (BAO) — a geometric
cosmic ruler. The evolving dark energy hint strengthened from DR1 to DR2 and
has not diminished.

* Data scale: DR1 used ~6 million redshifts (w several sigma from -1);
  DR2 uses ~14 million, giving strong hints of w changing with time.
  As of April 2026 DESI completed its planned 3D map and continues observing;
  DR3-era analyses are expected to tighten constraints.
* Core result: preference for dynamical dark energy persists in DR2 with
  larger statistics and wider redshift coverage. Multiple independent methods
  (shape-function, Bayesian w(z) reconstruction with Horndeski-derived prior,
  Gaussian process, crossing statistics) give a coherent picture: a mild,
  oscillatory departure from a cosmological constant.
* Dataset triangle: LCDM fits DESI+CMB tolerably but then mismatches the
  supernova data; fitting supernovae mismatches DESI+CMB. Agreement across
  all three currently requires w evolving with redshift.
* Best-fit shape (empirical targets for PDTP):
    * w_0 approx -0.7, w_a approx -1, at roughly 3 sigma in DESI BAO + CMB +
      SN combinations.
    * w rises from approx -1.7 at high redshift and crosses the phantom line
      (w = -1) near the present epoch.
    * Dark energy density peaks around z approx 0.5.
    * Some reconstructions show emergent behavior: negligible dark energy at
      z greater than approx 1.
* Counterweights (do not overclaim):
    * Prior-dependence critique: conclusions on evolution are strongly driven
      by assumed parameter priors; the phantom crossing lands suspiciously
      inside the observed window ("PhantomX coincidence").
    * The preferred w(z) does not correspond to any simple physical dark
      energy model (standard quintessence cannot produce it).
    * Cross-checks are mixed: DES Y6 lensing gives w = -1.12 with only
      0.9 sigma preference over LCDM, versus greater than 3 sigma in DESI
      combinations.
    * Part of the significance may sit in one displaced datapoint
      (z = 0.51 LRG distance ratio) per early critiques of DR1.

---

## 2. Standard Candle (Type Ia Supernova) Reliability Assessment

Description: Requested check on whether standard candles are reliable for
measuring acceleration. Three-tier verdict.

* What they are: "standardisable" candles, not standard ones.
    * Intrinsic luminosity scatter approx 0.8 mag, reduced to approx
      0.1 to 0.17 mag via empirical shape and color corrections (SALT
      light-curve fitting). Every correction is a place systematics can hide.
* The live controversy (directly relevant to the DESI claim):
    * The evolving dark energy preference requires relative calibration to
      within 0.01 mag across the full redshift range spanning multiple
      surveys (Efstathiou critique). Reported low-z vs high-z offsets
      averaging 0.04 mag common to Pantheon+ and DES-SN5YR.
    * A toy model (Dhawan, Popovic, Goobar 2025) shows SN systematics can
      produce a FALSE preference for evolving dark energy.
    * DES response (Vincenzi et al. 2025): the offset claim is unsubstantiated
      and traced to expected improvements in host-galaxy modeling, light-curve
      fitting, and selection-bias corrections; DES-SN5YR argued to carry LESS
      systematic risk than Pantheon+.
    * Structural weakness: independent SN analyses share the SAME low-redshift
      samples — a shared foundation is a shared failure mode. The DEBASS
      program (500+ new low-z SNe, 10 millimag calibration agreement) is being
      built specifically to replace it.
    * Forward-looking: even for Rubin/LSST, calibration systematics are
      expected to be a dominant uncertainty, and miscalibration can produce
      spurious evolving dark energy signals.
* Three-tier verdict:
    * Tier 1 — Acceleration exists: very reliable. Confirmed independently by
      SNe + BAO + CMB; no single calibration error kills all three.
    * Tier 2 — Precise w(z) history from SNe: genuinely contested right now;
      the 0.01 mag requirement is brutal and respected groups argue both sides.
    * Tier 3 — Relevance to DESI: the dynamical preference appears with three
      different SN compilations, and BAO is geometric (largely
      calibration-independent), so the hint is not purely a candle artifact —
      but SNe drive much of the statistical significance.

---

## 3. PDTP Implications: Qualitative Matches

Description: Comparison of DESI's empirical shape against the freeze-out /
beta(z) picture in `instruction_lambda_locking.md`. All [SPECULATIVE] until
the Kuramoto simulation and derivations exist.

* Match 1 — Late emergence: reconstructions with negligible dark energy at
  z greater than 1 fit the locking story (tilt suppressed while beta != 0;
  w = -1 plateau appears only as full lock completes). A true cosmological
  constant has no mechanism to "switch on" at z approx 0.5 to 1; a freeze-out
  does.
* Match 2 — Peak at z approx 0.5: sits inside the z_lock approx O(0.3 to 1)
  window guessed in the freeze-out section. Treat z approx 0.5 as the
  empirical target for z_lock in the Kuramoto simulation.
* Match 3 — "No simple model fits": a synchronization freeze-out is not a
  standard scalar-field model. An underdamped approach to lock (ringing as
  phases settle) could naturally produce the mild OSCILLATORY departure the
  reconstructions report. Candidate B (Kuramoto critical dynamics) is the
  natural home for this.

---

## 4. PDTP Implications: The Phantom Crossing Challenge

Description: The sharpest new problem DESI hands the framework.

* The data prefer w approx -1.7 at high z crossing to w greater than -1 today.
  Ordinary scalar fields cannot cross w = -1 without ghost instabilities.
* Candidate PDTP answer [SPECULATIVE, must be derived]: during active locking,
  energy flows between the matter sector and the condensate (alpha = cos Delta
  changing with time), so the dark energy sector is NOT closed. Non-closed
  sectors can exhibit effective w less than -1 without real ghosts.
* Required derivation (new Task 4b for the lambda-locking plan):
    * Derive the effective w(z) of a partially-locked phi_minus INCLUDING
      energy exchange with the matter sector.
    * Determine whether a phantom-to-quintessence crossing at lock completion
      is generic or requires tuning.
    * SymPy verification; check ghost-freedom explicitly; Sudoku check against
      the two-phase equations (Part 61) and EDE quartic (Part 117).

---

## 5. Amendments to instruction_lambda_locking.md

Description: Concrete edits Claude Code should apply (user approval first, per
project rules).

* Amendment 1 — Empirical targets for the Sudoku chain (Section 7 of that file):
    * w_0 approx -0.7, w_a approx -1 (DESI BAO + CMB + SN, approx 3 sigma).
    * Dark energy density peak at z approx 0.5 (target for z_lock).
    * Mild oscillatory w(z) departure (target shape for Candidate B ringing).
    * Flag all three as CONTESTED (Section 1 counterweights; Section 2 SN
      systematics fight). Do not hard-code them as truth.
* Amendment 2 — Add Task 4b (phantom crossing derivation, Section 4 above)
  after Task 4 (effective coupling at horizon scales).
* Amendment 3 — Add to kill tests / referee list:
    * Branch check: if the DESI signal is a supernova calibration artifact
      (Efstathiou scenario), the framework must remain consistent with pure
      LCDM — i.e., a beta(z) that locked earlier with no observable w_a.
      Both branches must be viable; do NOT bet the framework on the DESI hint
      being real. The Kuramoto simulation should report which parameter
      regions produce each branch.
* Amendment 4 — Watch list (data that will settle things within a few years;
  register PDTP predictions BEFORE they report):
    * DESI DR3-era analyses (full planned map completed April 2026).
    * DEBASS low-z supernova replacement sample (kills or confirms the shared
      low-z systematic).
    * Rubin/LSST first supernova cosmology.
    * Plus the existing kill test: CMB tensor modes (LiteBIRD / CMB-S4) for
      the Planck vortex relic.

---

## 6. Sources (Web Search, 2026-07-04)

Description: For citation in the research doc's prior-art and data sections.

* DESI collaboration, DR2 BAO cosmology: Phys. Rev. D 112 083515 (2025),
  arXiv:2503.14738.
* Dynamical dark energy in light of DESI DR2 BAO, Nature Astronomy (2025),
  s41550-025-02669-6 (DR1 -> DR2 persistence; multi-method coherence).
* CERN Courier, "DESI hints at evolving dark energy" (May 2025) — DR1 vs DR2
  scale, dataset-triangle tension summary.
* desi.lbl.gov — planned map completed 2026-04-15.
* "DESI Dark Secrets", arXiv:2502.08876 — best-fit w_0 approx -0.7,
  w_a approx -1, peak z approx 0.5, "no simple physical model" critique.
* Cortes and Liddle, "Interpreting DESI's evidence for evolving dark energy",
  JCAP 12 (2024) 007, arXiv:2404.08056 — prior-dependence and PhantomX
  coincidence critique.
* Calderon et al., DESI 2024 Crossing Statistics, JCAP 10 (2024) 048,
  arXiv:2405.04216 — emergent dark energy, negligible at z greater than 1.
* S_8 tension review, arXiv:2602.12238 — DES Y6 w = -1.12 at 0.9 sigma vs
  DESI greater than 3 sigma contrast.
* DES SN reanalysis with updated calibration, MNRAS (2026), stag632 —
  Efstathiou 0.01 mag requirement, 0.04 mag offsets, Dhawan/Popovic/Goobar
  false-preference toy model, Vincenzi response.
* "Dynamic or Systematic?" Bayesian model selection, MNRAS (2026), stag615
  and arXiv:2509.13220 — "standardisable candles" framing, Notari/Redi/Tesi
  offset test.
* DEBASS program, arXiv:2508.10877 — shared low-z sample weakness, 10 millimag
  cross-calibration.
* LSST calibration systematics, arXiv:2605.12401 — miscalibration can produce
  spurious evolving dark energy; SALT3 training systematics arXiv:2604.19746
  (0.8 mag raw scatter, 0.1 to 0.17 mag standardized).

---

## 7. One-Line Summary

DESI DR2 strengthens the case that dark energy emerged late, peaked near
z approx 0.5, and is drifting — three features a locking freeze-out predicts
naturally and a bare cosmological constant does not — but the supernova
calibration fight means PDTP must stay viable on BOTH branches (evolving and
pure LCDM), with the phantom-crossing derivation (Task 4b) as the new
must-solve problem.

---

*Generated 2026-07-04 from a claude.ai session with live web search.
[SPECULATIVE] framework claims throughout. Verify against the full repository
and original papers before acting.*
