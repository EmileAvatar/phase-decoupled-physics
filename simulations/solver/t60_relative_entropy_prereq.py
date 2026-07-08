#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
t60_relative_entropy_prereq.py -- Phase 94: T60 Prerequisite Check (Part 126)
===============================================================================
T60 Task 3 (TODO_05 Group C): does the proposed phase-mismatch relative
entropy S_rel ~ 1 - cos(psi-phi) relate to the ALREADY-EXISTING PDTP
entropy S_PDTP = k_B*ln(2)*A/a_0^2 (Part 86, lattice cell counting)?
This is a prerequisite gate before any new derivation work (T60 Tasks 1,2,4).

Source of the candidate: docs/fable_notes/fable notes to check 02.md
(external ChatGPT session; did not have access to Part 86).

WHAT THIS SCRIPT DOES (all COMPUTED, RECHECK rule):
  S1: Algebraic identity S_rel = 1 - V/g = 1 - alpha        [SymPy, trivial
      but must be shown -- this is a RENAMING of the existing coupling,
      not yet a derivation of an entropy from first principles]
  S2: Monotonicity: dS_rel/dalpha = -1 exactly -> S_rel is monotonic
      DEcreasing in alpha (the notes' own stated test)       [SymPy]
  S3: Small-mismatch limit: 1-cos(x) = x^2/2 + O(x^4)        [SymPy series]
  S4: Horizon evaluation: alpha -> 0 at the horizon is an ALREADY-ESTABLISHED
      PDTP result (Part 98/T1, Eq T.7: n_PDTP = 1/alpha -> horizon = TIR,
      alpha -> 0). Substituting gives S_rel(horizon) = 1 exactly. [COMPUTED
      from an existing result, not new]
  S5: Compare S_rel(horizon) = 1 to Part 86's per-cell entropy s_cell =
      ln(2): these are DIFFERENT NUMBERS (ratio 1/ln(2) = 1.443).  S_rel as
      literally proposed is NOT the same quantity as Part 86's per-cell
      entropy.                                                [COMPUTED]
  S6: Construct the ONLY way to get an area law from S_rel: postulate an
      area integral S_rel_area = (k_B/a_0^2) * integral_horizon S_rel dA
      -- THIS IS A NEW, UNPROVEN ASSUMPTION (same TYPE Part 86 needed: one
      unit of entropy per a_0^2 patch). With S_rel(horizon)=1: matching to
      Bekenstein-Hawking gives a THIRD candidate lattice spacing a_0 = 2*l_P
      (vs Part 86's 1.665*l_P).                                [DERIVED
      given the new assumption, SymPy solve]
  S7: Three-way gap comparison (entropy-counting gap factor at a_0=l_P):
      S_rel route = 4, Part 86 (cell counting) = 4*ln(2) = 2.773,
      Sakharov N_eff (Part 83) = 3*pi/4 = 2.356. Report BOTH the raw gap
      factors (spread ~70%) and the a_0-space comparison (compressed by
      sqrt, ~20%) -- do not cherry-pick the flattering metric.  [COMPUTED]

VERDICT SHAPE (see main()): S_rel is NOT the same object as S_PDTP (local
continuum density vs discrete horizon-counted extensive entropy). It CANNOT
derive an area law on its own -- doing so requires the same kind of external
"one unit of information per a_0^2" postulate Part 86 already needed. But
evaluated at the horizon (using an independently-established PDTP result)
it lands in the SAME O(1)-uncertainty family as the two existing gap
factors -- a third, weakly-independent data point, not a new mechanism.

Sources:
  Part 86 -- docs/research/nonlinear_einstein.md (S_PDTP, Eqs 86.6-86.10)
  Part 98/T1 -- docs/research/tan_initial_investigation.md Eq T.7
      (n_PDTP = 1/alpha; alpha -> 0 at horizon = TIR)
  Part 83 -- neff_sakharov.py (Sakharov gap 3*pi/4)
  Bekenstein (1973) Phys. Rev. D 7, 2333; Hawking (1975) Comm. Math. Phys. 43, 199
  docs/fable_notes/fable notes to check 02.md (external proposal, 2026-07-08)

Output: simulations/solver/outputs/t60_relative_entropy_prereq_<timestamp>.txt

ALL returned values are COMPUTED -- no hardcoded results (RECHECK rule).
"""

import os
import sys
import math

import sympy as sp
from sympy import symbols, cos, sin, sqrt, log, diff, series, simplify, solve, ln

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from print_utils import ReportWriter

# ===========================================================================
# SYMPY SYMBOLS
# ===========================================================================
x, V_s, g_s, a_s, lP_s = symbols('x V g alpha l_P', real=True)
a_pos = symbols('alpha_pos', positive=True)


# ===========================================================================
# S1: ALGEBRAIC IDENTITY  S_rel = 1 - V/g = 1 - alpha
# ===========================================================================

def verify_identity(rw):
    """
    V = g*cos(psi-phi) = g*alpha  [existing PDTP coupling energy]
    S_rel := 1 - V/g = 1 - alpha                                  [ASSUMED
    identification -- this is a RENAMING, the Lagrangian does not by
    itself say 1-alpha is an entropy; flagged explicitly]
    """
    rw.section("S1: ALGEBRAIC IDENTITY  S_rel = 1 - V/g = 1 - alpha  [ASSUMED]")

    V_def   = g_s * a_s                      # V = g*alpha
    S_rel   = 1 - V_def / g_s
    resid   = simplify(S_rel - (1 - a_s))
    ok      = (resid == 0)

    rw.print("  V = g*alpha  [existing PDTP interaction energy, established]")
    rw.print("  S_rel := 1 - V/g = {}   residual vs (1-alpha): {}  [{}]".format(
        S_rel, resid, "VERIFIED" if ok else "FAIL"))
    rw.print("")
    rw.print("  HONESTY FLAG: this is a RENAMING of the existing coupling,")
    rw.print("  not a derivation. Nothing in the Lagrangian's variational")
    rw.print("  structure currently forces 1-alpha to be interpreted as an")
    rw.print("  entropy/distinguishability measure -- it is an external")
    rw.print("  ASSUMED identification borrowed from the analogy. [ASSUMED]")

    return {'identity_ok': ok}


# ===========================================================================
# S2: MONOTONICITY  dS_rel/dalpha
# ===========================================================================

def verify_monotonic(rw):
    """
    The notes' own stated test: 'test whether I(Delta_theta) is monotonic
    with alpha'. S_rel = 1 - alpha => dS_rel/dalpha = -1 exactly: constant,
    strictly negative -> S_rel is monotonically DEcreasing in alpha
    (maximal synchronization alpha=1 -> S_rel=0; full decoupling alpha=0
    -> S_rel=1 maximum). [SymPy]
    """
    rw.section("S2: MONOTONICITY TEST  dS_rel/dalpha")

    S_rel  = 1 - a_s
    dS     = diff(S_rel, a_s)
    ok     = simplify(dS + 1) == 0            # dS/dalpha == -1

    rw.print("  S_rel(alpha) = 1 - alpha")
    rw.print("  dS_rel/dalpha = {}  (constant, exactly -1: {})".format(dS, ok))
    rw.print("  -> monotonically DEcreasing in alpha for all alpha in [-1,1].")
    rw.print("     alpha=1 (locked):   S_rel = 0  (minimum, no distinguishability)")
    rw.print("     alpha=0 (decoupled): S_rel = 1  (maximum)")
    rw.print("  [VERIFIED -- passes the notes' own stated monotonicity test]")

    return {'monotonic_ok': ok}


# ===========================================================================
# S3: SMALL-MISMATCH LIMIT
# ===========================================================================

def derive_small_mismatch(rw):
    """
    S_rel(Delta_theta) = 1 - cos(Delta_theta); Taylor series around 0:
      1 - cos(x) = x^2/2 - x^4/24 + O(x^6)                       [SymPy]
    Leading order: S_rel ~ Delta_theta^2/2 -- a standard quadratic
    (harmonic) form, structurally the SAME quadratic that already appears
    as the leading term of V = g*cos(Delta_theta) expanded around lock
    (mass term of a phase oscillator). This is expected, not a new result:
    S_rel is built directly from V, so its small-x behavior mirrors V's.
    """
    rw.section("S3: SMALL-MISMATCH LIMIT  [SymPy Taylor series]")

    S_rel = 1 - cos(x)
    ser   = series(S_rel, x, 0, 6).removeO()
    quad_coeff = ser.coeff(x, 2)
    quartic_coeff = ser.coeff(x, 4)
    quad_ok = simplify(quad_coeff - sp.Rational(1, 2)) == 0

    rw.print("  1 - cos(x) series to O(x^6): {}".format(ser))
    rw.print("  x^2 coefficient = {}  (expected 1/2: {})".format(
        quad_coeff, quad_ok))
    rw.print("  x^4 coefficient = {}".format(quartic_coeff))
    rw.print("")
    rw.print("  S_rel ~ Delta_theta^2/2 at leading order -- same quadratic")
    rw.print("  form as the standard phase-oscillator mass term. Expected")
    rw.print("  (not independent new physics): S_rel is built directly from")
    rw.print("  V, so it inherits V's small-angle behavior exactly.")

    return {'quad_coeff_is_half': quad_ok}


# ===========================================================================
# S4: HORIZON EVALUATION -- USING AN ALREADY-ESTABLISHED PDTP RESULT
# ===========================================================================

def evaluate_at_horizon(rw):
    """
    Part 98 (T1), Eq T.7: n_PDTP = 1/cos(Delta) = 1/alpha; alpha -> 0 at the
    horizon corresponds to n -> infinity = total internal reflection (TIR),
    identified with the horizon in Part 28c. This is an EXISTING PDTP
    result, not re-derived here -- only substituted.

    S_rel(horizon) = 1 - alpha(horizon) = 1 - 0 = 1  exactly.  [COMPUTED]
    """
    rw.section("S4: HORIZON VALUE  [using Part 98/T1 alpha_horizon = 0]")

    alpha_horizon = 0.0     # Part 98 Eq T.7 (cited, not re-derived here)
    S_rel_horizon = 1.0 - alpha_horizon

    rw.print("  Part 98/T1 Eq T.7: n_PDTP = 1/alpha; alpha -> 0 at horizon (TIR)")
    rw.print("  [ESTABLISHED, cited from tan_initial_investigation.md, not")
    rw.print("   re-derived in this script]")
    rw.print("  S_rel(horizon) = 1 - alpha_horizon = 1 - {} = {}".format(
        alpha_horizon, S_rel_horizon))
    rw.print("  [COMPUTED] -- every cell at the horizon carries the MAXIMUM")
    rw.print("  possible value of the candidate S_rel.")

    return {'alpha_horizon': alpha_horizon, 'S_rel_horizon': S_rel_horizon}


# ===========================================================================
# S5: COMPARE TO PART 86 PER-CELL ENTROPY
# ===========================================================================

def compare_per_cell(rw, s4):
    """
    Part 86 Eq 86.7 per-cell entropy: s_cell = ln(2)  [from a 2-state
    (locked/anti-locked) Shannon-entropy counting argument].
    S_rel(horizon) = 1 (from S4). These are DIFFERENT NUMBERS -- S_rel as
    literally proposed is NOT the same quantity as Part 86's per-cell
    entropy. Ratio computed, not asserted.
    """
    rw.section("S5: COMPARISON TO PART 86 PER-CELL ENTROPY  [Eq 86.7]")

    s_cell_part86 = math.log(2.0)              # ln(2), Part 86 Eq 86.7
    ratio = s4['S_rel_horizon'] / s_cell_part86

    rw.print("  Part 86 per-cell entropy: s_cell = ln(2) = {:.6f}".format(
        s_cell_part86))
    rw.print("  S_rel(horizon) (S4)     = {:.6f}".format(s4['S_rel_horizon']))
    rw.print("  ratio S_rel(horizon)/s_cell = {:.6f}  (NOT 1: different numbers)".format(
        ratio))
    rw.print("")
    rw.print("  FINDING: S_rel as literally proposed (1-alpha, a continuum,")
    rw.print("  local scalar) is NOT numerically or structurally identical")
    rw.print("  to Part 86's per-cell entropy (a discrete 2-state Shannon")
    rw.print("  count). They are different TYPES of object: S_rel is a")
    rw.print("  point-wise field; s_cell is a per-microstate combinatorial")
    rw.print("  quantity. No limit of one reduces exactly to the other.")

    return {'s_cell_part86': s_cell_part86, 'ratio_to_part86': ratio}


# ===========================================================================
# S6: THE ONLY WAY TO GET AN AREA LAW -- A NEW, UNPROVEN ASSUMPTION
# ===========================================================================

def derive_area_law_attempt(rw, s4):
    """
    S_rel(x) alone is a LOCAL scalar -- it has no area dependence. To build
    an area-extensive entropy (needed for Jacobson's argument) requires
    POSTULATING an area integral:
      S_rel_area := (k_B/a_0^2) * integral_horizon S_rel(x) dA          (126.1)
    [NEW ASSUMPTION -- not provided by the fable notes; structurally the
    SAME TYPE of postulate Part 86 needed (one unit of entropy per a_0^2
    patch) -- this is NOT a free derivation of the area law from S_rel.]

    With S_rel(horizon) = 1 (S4, constant over the horizon by the same
    logic Part 98 used): S_rel_area = k_B*A/a_0^2.
    Matching to Bekenstein-Hawking S_BH = k_B*A/(4*l_P^2) (Part 86 Eq 86.8):
      a_0_new^2 = 4*l_P^2  =>  a_0_new = 2*l_P                          (126.2)
    """
    rw.section("S6: AREA-LAW ATTEMPT -- REQUIRES A NEW ASSUMPTION  [Eq 126.1-126.2]")

    S_rel_h = s4['S_rel_horizon']

    # SymPy: S_rel_area(a_0) = k_B*A*S_rel_h/a_0^2 = S_BH = k_B*A/(4*l_P^2)
    # both symbols must be declared positive or solve() returns the +/- pair
    # (or picks the negative branch first) instead of the physical root.
    a0_s, lP_pos = symbols('a_0 l_P_pos', positive=True)
    eq   = sp.Eq(S_rel_h / a0_s**2, 1 / (4 * lP_pos**2))
    sol  = solve(eq, a0_s)
    assert len(sol) == 1, "expected a unique positive root: {}".format(sol)
    a0_new_sym = simplify(sol[0])
    a0_new_num = a0_new_sym.subs(lP_pos, 1)     # numeric coefficient (in l_P units)

    a0_part86 = 2.0 * math.sqrt(math.log(2.0))     # Part 86 Eq 86.10, 1.665
    ratio_a0  = float(a0_new_num) / a0_part86

    rw.print("  S_rel_area = (k_B/a_0^2) * A * S_rel(horizon)  [Eq 126.1, NEW")
    rw.print("  ASSUMPTION -- structurally identical postulate to Part 86's")
    rw.print("  'one unit of entropy per a_0^2 patch'; S_rel alone does NOT")
    rw.print("  derive an area law without this external input.]")
    rw.print("")
    rw.print("  Matching S_rel_area = S_BH (SymPy solve): a_0 = {}".format(
        a0_new_sym))
    rw.print("  Numeric coefficient: a_0 = {:.6f} * l_P   [Eq 126.2]".format(
        float(a0_new_num)))
    rw.print("  Part 86 (cell counting) coefficient:      {:.6f} * l_P   [Eq 86.10]".format(
        a0_part86))
    rw.print("  Ratio (new/Part86) = {:.4f}  ({:.1f}% apart)".format(
        ratio_a0, abs(ratio_a0 - 1.0) * 100.0))

    return {'a0_new_coeff': float(a0_new_num), 'a0_part86_coeff': a0_part86,
            'ratio_a0': ratio_a0}


# ===========================================================================
# S7: THREE-WAY GAP COMPARISON -- HONEST, NOT CHERRY-PICKED
# ===========================================================================

def compare_three_gaps(rw, s6):
    """
    Raw entropy-GAP factor at a_0 = l_P (S_area(a_0=l_P)/S_BH(a_0=l_P)),
    for all three independent PDTP microstate-counting routes:
      S_rel route (S6):     S_rel_area(l_P)/S_BH = 1/(1/4) = 4          [COMPUTED]
      Part 86 (cell count): 4*ln(2) = 2.773                              [Eq 86.9]
      Sakharov (Part 83):   3*pi/4 = 2.356                               [Part 83]
    Report BOTH the raw gap spread (large) and the a_0-space spread
    (compressed by sqrt) -- do not cherry-pick the flattering metric.
    """
    rw.section("S7: THREE-WAY GAP COMPARISON  [honest, both metrics]")

    gap_rel    = 1.0 / 0.25                 # S_rel_area(l_P)/S_BH(l_P) = 1/(1/4)
    gap_part86 = 4.0 * math.log(2.0)        # Eq 86.9
    gap_sakh   = 3.0 * math.pi / 4.0        # Part 83

    gaps = {'S_rel route (this check)': gap_rel,
            'Part 86 (cell counting)': gap_part86,
            'Sakharov N_eff (Part 83)': gap_sakh}

    rw.print("  Raw entropy-gap factor (S_area(a_0=l_P) / S_BH):")
    for name, val in gaps.items():
        rw.print("    {:30s}: {:.4f}".format(name, val))

    max_gap, min_gap = max(gaps.values()), min(gaps.values())
    raw_spread = (max_gap - min_gap) / min_gap

    rw.print("  Raw spread: (max-min)/min = {:.1%}  -- NOT tightly clustered".format(
        raw_spread))
    rw.print("")
    rw.print("  In a_0-space (a_0 ~ sqrt(gap), so spread is compressed by sqrt):")
    a0_rel    = 2.0 * math.sqrt(0.25 * 1.0)      # placeholder recompute below
    a0_rel    = s6['a0_new_coeff']
    a0_part86 = s6['a0_part86_coeff']
    a0_sakh   = math.sqrt(gap_sakh)              # a_0/l_P = sqrt(gap) by construction
    a0_vals = {'S_rel route': a0_rel, 'Part 86': a0_part86, 'Sakharov': a0_sakh}
    for name, val in a0_vals.items():
        rw.print("    {:15s}: a_0 = {:.4f} * l_P".format(name, val))
    a0_max, a0_min = max(a0_vals.values()), min(a0_vals.values())
    a0_spread = (a0_max - a0_min) / a0_min
    rw.print("  a_0-space spread (3-way): (max-min)/min = {:.1%}  -- compressed".format(
        a0_spread))
    rw.print("  vs raw ({:.1%}), but WIDER than the Part 86 Sec 5.5 two-way".format(
        raw_spread))
    rw.print("  comparison (Part86 vs Sakharov alone: {:.1%}). Honest read:".format(
        abs(a0_part86 - a0_sakh) / a0_sakh))
    rw.print("  adding the S_rel route does not tighten the cluster, it")
    rw.print("  slightly widens it -- still same order of magnitude (all in")
    rw.print("  [1.5, 2.0]*l_P), not a new precision result.")

    return {'gap_rel': gap_rel, 'gap_part86': gap_part86, 'gap_sakh': gap_sakh,
            'raw_spread': raw_spread, 'a0_spread': a0_spread}


# ===========================================================================
# SUDOKU CONSISTENCY CHECKS (10 tests)
# ===========================================================================

def sudoku_checks(rw, s1, s2, s3, s4, s5, s6, s7):
    """10 checks; every 'got' read from a step dict (RECHECK trace path)."""
    rw.section("SUDOKU CONSISTENCY CHECKS")

    passes = 0
    total  = 0

    def chk(label, got, want, tol=0.005, is_bool=False):
        nonlocal passes, total
        total += 1
        if is_bool:
            ok = bool(got) == bool(want)
            rw.print("  [{}] {}: {}  (expected {})".format(
                "PASS" if ok else "FAIL", label, got, want))
        else:
            if want == 0.0:
                ok = abs(got) < 1e-9
            else:
                ok = abs(got / want - 1.0) < tol
            rw.print("  [{}] {}: {:.6g}  (ref {:.6g})".format(
                "PASS" if ok else "FAIL", label, got, want))
        if ok:
            passes += 1

    chk("T1: S_rel = 1-V/g = 1-alpha identity [SymPy]",
        s1['identity_ok'], True, is_bool=True)
    chk("T2: dS_rel/dalpha = -1 exactly (monotonic) [SymPy]",
        s2['monotonic_ok'], True, is_bool=True)
    chk("T3: small-x quadratic coeff = 1/2 [SymPy]",
        s3['quad_coeff_is_half'], True, is_bool=True)
    chk("T4: alpha_horizon = 0 (Part 98/T1, cited)",
        s4['alpha_horizon'], 0.0)
    chk("T5: S_rel(horizon) = 1 exactly",
        s4['S_rel_horizon'], 1.0)
    chk("T6: S_rel(horizon)/s_cell(Part86) != 1 (different objects, recorded)",
        abs(s5['ratio_to_part86'] - 1.0) > 0.01, True, is_bool=True)
    chk("T7: a_0_new (S_rel route) = 2*l_P exactly [SymPy solve]",
        s6['a0_new_coeff'], 2.0)
    chk("T8: a_0_new vs Part86 a_0 within 25% (same O(1) family)",
        s6['ratio_a0'], 1.0, tol=0.25)
    chk("T9: raw gap spread > a_0-space spread (sqrt compression demonstrated)",
        s7['raw_spread'] > s7['a0_spread'], True, is_bool=True)
    chk("T10: three-way a_0 spread < 25% (tighter than 2-way Part86/Sakharov)",
        s7['a0_spread'] < 0.25, True, is_bool=True)
    rw.print("     [recorded miss, not hidden: 3-way spread {:.1%} is WIDER".format(
        s7['a0_spread']))
    rw.print("      than the existing 2-way Part86-vs-Sakharov spread; adding")
    rw.print("      the S_rel route does not tighten the O(1) cluster]")

    rw.print("")
    rw.print("  SCORE: {}/{} PASS".format(passes, total))
    return {'passes': passes, 'total': total, 'all_pass': passes == total}


# ===========================================================================
# MAIN
# ===========================================================================

def main():
    out_dir = os.path.join(_HERE, "outputs")
    rw = ReportWriter(out_dir, label="t60_relative_entropy_prereq")

    rw.section("T60 TASK 3 -- PREREQUISITE CHECK (Part 126, Phase 94)")
    rw.print("Date: 2026-07-08")
    rw.print("Question: does S_rel ~ 1-cos(psi-phi) relate to Part 86's")
    rw.print("S_PDTP = k_B*ln(2)*A/a_0^2 in any limit?")
    rw.print("Source: docs/fable_notes/fable notes to check 02.md (external,")
    rw.print("did not have access to Part 86).")

    s1 = verify_identity(rw)
    s2 = verify_monotonic(rw)
    s3 = derive_small_mismatch(rw)
    s4 = evaluate_at_horizon(rw)
    s5 = compare_per_cell(rw, s4)
    s6 = derive_area_law_attempt(rw, s4)
    s7 = compare_three_gaps(rw, s6)
    score = sudoku_checks(rw, s1, s2, s3, s4, s5, s6, s7)

    rw.section("OVERALL VERDICT")
    rw.print("  [ASSUMED]  S_rel = 1-alpha is a RENAMING of the existing")
    rw.print("             coupling, not a derivation from the Lagrangian.")
    rw.print("  [VERIFIED] Monotonic decreasing in alpha (passes the notes'")
    rw.print("             own stated test).")
    rw.print("  [FINDING]  S_rel is NOT the same object as Part 86's S_PDTP:")
    rw.print("             S_rel is a LOCAL continuum scalar; S_PDTP is a")
    rw.print("             discrete, horizon-AREA-extensive counted entropy.")
    rw.print("             No limit of one reduces exactly to the other")
    rw.print("             (S5: ratio {:.4f}, not 1).".format(s5['ratio_to_part86']))
    rw.print("  [FINDING]  S_rel CANNOT derive an area law by itself. Doing")
    rw.print("             so requires the SAME TYPE of external postulate")
    rw.print("             Part 86 already needed (one unit of entropy per")
    rw.print("             a_0^2 patch) -- Eq 126.1 is a NEW assumption, not")
    rw.print("             a consequence of S_rel.")
    rw.print("  [COMPUTED] IF that assumption is added anyway, using the")
    rw.print("             independently-established alpha_horizon=0 result")
    rw.print("             (Part 98/T1), the matching a_0 = 2*l_P lands")
    rw.print("             within {:.0%} of Part 86's 1.665*l_P alone -- but".format(
        abs(s6['ratio_a0'] - 1.0)))
    rw.print("             the FULL three-way spread (S_rel, Part86, Sakharov)")
    rw.print("             is {:.0%}, WIDER than the existing Part86-vs-".format(
        s7['a0_spread']))
    rw.print("             Sakharov spread alone. Same O(1) family, but adding")
    rw.print("             the S_rel route does not tighten it -- an honest")
    rw.print("             miss, recorded (T10), not a new precision result.")
    rw.print("")
    rw.print("  SUDOKU: {}/{} PASS".format(score['passes'], score['total']))
    rw.print("")
    rw.print("  RECOMMENDATION FOR T60 TASKS 1/2/4:")
    rw.print("  Do NOT pursue 'S_rel derives the area law' as literally")
    rw.print("  proposed -- it does not, without adding an assumption PDTP")
    rw.print("  already has under a different name. The genuinely open,")
    rw.print("  worthwhile thread is T60 Task 2: whether phi_- (the EXISTING")
    rw.print("  two-phase surface mode, Part 61) can be shown -- not assumed")
    rw.print("  -- to reproduce Part 86's ln(2)-per-cell factor from its own")
    rw.print("  dynamics. That would be new; this check alone is not.")

    rw.close()
    print("")
    print("Log saved to: " + rw.path)
    return score


if __name__ == "__main__":
    score = main()
    sys.exit(0 if score['all_pass'] else 1)
