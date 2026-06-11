#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
phi_minus_quartic.py -- Phase 85: Origin of a Positive phi_-^4 Term (Part 117)
==============================================================================
Part 88 (Hubble tension FCC) identified the missing physics for Early Dark
Energy in PDTP: a POSITIVE quartic term lambda_4 * phi_-^4 with lambda_4 ~ g.
The tree-level cosine gives the WRONG sign (-g/12).  Part 88 listed three
speculative origins.  This phase TESTS them by direct computation:

  S1: Verify the exact Part 61 product identity
      cos(psi - phi_b) - cos(psi - phi_s) = 2 sin(psi - phi_+) sin(phi_-)
  S2: Tree-level quartic around the joint vacuum -> reproduce -g/12 (Part 88)
  S3: Zero-point (one-loop) channel -> sign of the generated quartic
  S4: Induced channel -- integrate out the gravity mode phi_+ at second
      order around a PARTIALLY LOCKED background (psi - phi_+ = pi/2 - beta)
      -> V_ind = -(2 g^2 sin^2(beta) / kbar^2) * sin^2(phi_-)
      -> quartic = + 2 g^2 sin^2(beta) / (3 kbar^2)   [POSITIVE]
  S5: Magnitude check -- lambda_4 / g at kbar^2 = 2g; required ~ g (Part 88)
  S6: Two-phase compatibility -- induced term vanishes identically at
      beta = 0 (full lock): Part 61/63 results untouched today
  S7: Sudoku consistency check (reads computed values from S1-S6)

Background convention (Parts 61/63): the locked vacuum has
psi - phi_+ = pi/2 (chi = phi_+ + pi/2 maps two-phase to single phase).
"Partial locking" beta != 0 means the matter phase has not yet reached
the locked configuration -- the generic early-universe state.

Methodology.md checklist items: 2 (scaffolding term, Maxwell-style),
6 (work backwards: what generates the required term?), 3 (Sudoku),
5 (negative results documented per channel).

Prerequisites:
  Part 61: two_phase_lagrangian.py -- product coupling, joint vacuum
  Part 62: reversed_higgs.py -- m^2_phi- = 2 g Phi near matter
  Part 88: hubble_tension_c1.py -- EDE needs positive quartic ~ g

Sources:
  Coleman & Weinberg (1973), Phys. Rev. D 7, 1888 (one-loop effective
      potential from zero-point energies)
  Peskin & Schroeder (1995), "An Introduction to QFT", ch. 11
      (integrating out a field at tree level: V_eff = V - J^2/(2M))
  Poland et al. / standard EFT matching: integrating out a heavy or
      stiff mode generates -(coupling)^2/(2 stiffness) corrections
  Part 88 Eq 88.13: -2g cos(phi_-) = -2g + g phi_-^2 - g phi_-^4/12 + ...

Research doc: docs/research/phi_minus_quartic.md (Part 117)
Output log:   simulations/solver/outputs/phi_minus_quartic_<ts>.txt

ALL returned values are COMPUTED (RECHECK rule) -- no hardcoded results.
"""

import os
import sys

import numpy as np
import sympy as sp
from sympy import (symbols, Rational, sqrt, pi, cos, sin, series, simplify,
                   solve, limit, diff, trigsimp)

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from print_utils import ReportWriter
from sympy_checks import check_equal, check_sign

# symbols used throughout
psi, phi_p, phi_m, g, beta, kbar2, eta, chi = symbols(
    'psi phi_plus phi_minus g beta kbar2 eta chi', real=True)
g_pos, k_pos = symbols('g_p k_p', positive=True)


def quartic_coeff(expr, var):
    """Coefficient of var**4 in the series expansion of expr about var=0.
    COMPUTED via sympy series extraction -- never typed in by hand."""
    s = sp.series(expr, var, 0, 6).removeO()
    return sp.expand(s).coeff(var, 4)


# ===========================================================================
# S1: EXACT PRODUCT IDENTITY (Part 61)
# ===========================================================================

def verify_product_identity(rw):
    """cos(psi-phi_b) - cos(psi-phi_s) = 2 sin(psi-phi_+) sin(phi_-)
    with phi_b = phi_+ + phi_-, phi_s = phi_+ - phi_-."""
    rw.subsection("S1: Part 61 product identity [SymPy]")

    phi_b = phi_p + phi_m
    phi_s = phi_p - phi_m
    lhs = cos(psi - phi_b) - cos(psi - phi_s)
    rhs = 2 * sin(psi - phi_p) * sin(phi_m)
    ok, msg = check_equal(lhs, rhs, label="Part 61 product coupling identity")
    rw.print("  " + msg)
    return {'identity_ok': ok,
            'residual': simplify(lhs - rhs)}


# ===========================================================================
# S2: TREE-LEVEL QUARTIC AROUND THE JOINT VACUUM
# ===========================================================================

def derive_tree_quartic(rw):
    """
    Joint vacuum (Part 61/63): psi - phi_+ = pi/2 and phi_- = pi/2.
    Expand V = -2g sin(psi - phi_+) sin(phi_-) about it:
        psi - phi_+ = pi/2 + delta,   phi_- = pi/2 + chi
        V = -2g cos(delta) cos(chi)
    The chi^4 coefficient must come out as -g/12 (Part 88 Eq 88.13 form).
    """
    rw.subsection("S2: Tree-level quartic at the joint vacuum")

    delta = symbols('delta', real=True)
    V = -2 * g * sin(pi / 2 + delta) * sin(pi / 2 + chi)
    V_simpl = trigsimp(V)
    rw.print("  V(delta, chi) = " + str(V_simpl) + "   [exact]")

    V_chi = V.subs(delta, 0)               # delta integrated to its minimum 0
    c4 = quartic_coeff(V_chi, chi)
    c2 = sp.expand(sp.series(V_chi, chi, 0, 6).removeO()).coeff(chi, 2)
    rw.print("  V(0, chi) = -2g cos(chi)")
    rw.print("  series: mass term coeff = " + str(c2) + " (= +g, stable)")
    rw.print("  quartic coeff = " + str(c4) + "   [DERIVED]")
    rw.print("  -> matches Part 88 Eq 88.13: NEGATIVE quartic -g/12.")
    rw.print("     Tree level CANNOT supply the EDE term.  [NEGATIVE]")

    return {'tree_quartic': c4,
            'tree_quartic_is_negative': bool(sp.simplify(c4 / g) < 0
                                             if (c4 / g).is_number else
                                             sp.simplify(c4) == -g / 12),
            'matches_88_13': simplify(c4 - (-g / 12)) == 0}


# ===========================================================================
# S3: ZERO-POINT (ONE-LOOP) CHANNEL
# ===========================================================================

def derive_zeropoint_quartic(rw):
    """
    The locked matter mode delta has chi-dependent mass:
        V = -2g cos(delta) cos(chi)  ->  (1/2) m_delta^2 delta^2 with
        m_delta^2 = 2 g cos(chi)            [from the delta^2 coefficient]
    Zero-point energy of the delta oscillator (Coleman-Weinberg in the
    single-mode approximation):
        V_zp(chi) = (1/2) omega = (1/2) sqrt(2 g cos(chi))    [hbar = 1]
    Sign of the chi^4 coefficient is COMPUTED from the series.
    """
    rw.subsection("S3: Zero-point (one-loop) channel")

    delta = symbols('delta', real=True)
    V = -2 * g_pos * cos(delta) * cos(chi)
    m2_delta = sp.expand(sp.series(V, delta, 0, 3).removeO()).coeff(
        delta, 2) * 2
    rw.print("  m_delta^2(chi) = " + str(m2_delta))

    V_zp = sqrt(m2_delta) / 2
    c4_zp = quartic_coeff(V_zp, chi)
    c2_zp = sp.expand(sp.series(V_zp, chi, 0, 6).removeO()).coeff(chi, 2)
    rw.print("  V_zp = (1/2) sqrt(2 g cos chi)")
    rw.print("  mass correction coeff = " + str(sp.simplify(c2_zp)))
    rw.print("  quartic coeff = " + str(sp.simplify(c4_zp)))

    c4_num = float(c4_zp.subs(g_pos, 1.0))
    verdict = "NEGATIVE" if c4_num < 0 else "POSITIVE"
    rw.print("  numeric at g=1: {:.5f} -> {} quartic".format(c4_num, verdict))
    rw.print("  -> Zero-point channel also gives the WRONG sign. [NEGATIVE]")

    return {'zp_quartic': sp.simplify(c4_zp), 'zp_quartic_num': c4_num,
            'zp_is_negative': c4_num < 0}


# ===========================================================================
# S4: INDUCED CHANNEL -- INTEGRATING OUT phi_+ AT PARTIAL LOCK
# ===========================================================================

def derive_induced_quartic(rw):
    """
    Background: psi - phi_+ = pi/2 - beta (PARTIAL lock, beta != 0; the
    generic pre-locked early-universe state).  Let eta be the phi_+
    fluctuation, so psi - phi_+ -> pi/2 - beta + eta... (sign convention:
    eta shifts the argument).  Exact potential:

        V(eta, phi_-) = -2 g sin(pi/2 - beta + eta) sin(phi_-)

    Expand to O(eta^2), add gradient stiffness (1/2) kbar2 eta^2 from the
    phi_+ kinetic term (mode of momentum kbar), integrate eta out exactly
    (Gaussian / tree-level matching, Peskin & Schroeder ch. 11):

        V(eta) = (M/2) eta^2 - J eta + V_0
        eta*   = J/M
        V_min  = V_0 - J^2/(2M)        [exact for quadratic action]

    Then extract the phi_-^4 coefficient of V_min in the gradient-
    dominated regime M ~ kbar2.
    """
    rw.subsection("S4: Induced channel -- integrate out phi_+ at partial lock")

    V_exact = -2 * g * sin(pi / 2 - beta + eta) * sin(phi_m)
    V_ser = sp.expand(sp.series(V_exact, eta, 0, 3).removeO())
    V0 = V_ser.coeff(eta, 0)
    J = -V_ser.coeff(eta, 1)            # V = ... - J*eta
    M_pot = V_ser.coeff(eta, 2) * 2     # potential part of stiffness
    rw.print("  V_0   = " + str(sp.trigsimp(V0)))
    rw.print("  J     = " + str(sp.trigsimp(J)) + "   [linear source]")
    rw.print("  M_pot = " + str(sp.trigsimp(M_pot)) + "   [potential stiffness]")

    # exact Gaussian minimisation, COMPUTED with full stiffness M = kbar2 + M_pot
    M_full = kbar2 + M_pot
    V_eta = (M_full / 2) * eta**2 - J * eta + V0
    eta_star = solve(diff(V_eta, eta), eta)[0]
    V_min = simplify(V_eta.subs(eta, eta_star))
    V_expected = simplify(V0 - J**2 / (2 * M_full))
    ok_gauss, msg_gauss = check_equal(
        V_min, V_expected, label="V_min = V_0 - J^2/(2M) (exact Gaussian)")
    rw.print("  " + msg_gauss)

    # gradient-dominated regime: M -> kbar2
    V_ind = simplify(-J**2 / (2 * kbar2))
    rw.print("")
    rw.print("  gradient-dominated (kbar2 >> M_pot):")
    rw.print("  V_ind = " + str(V_ind))
    rw.print("        = -(2 g^2 sin^2(beta)/kbar2) * sin^2(phi_-)")

    sin2_form = -(2 * g**2 * sin(beta)**2 / kbar2) * sin(phi_m)**2
    ok_form, msg_form = check_equal(V_ind, sin2_form,
                                    label="V_ind closed form")
    rw.print("  " + msg_form)

    c4_ind = quartic_coeff(V_ind, phi_m)
    c2_ind = sp.expand(sp.series(V_ind, phi_m, 0, 6).removeO()).coeff(phi_m, 2)
    lam4_expected = 2 * g**2 * sin(beta)**2 / (3 * kbar2)
    ok_c4, msg_c4 = check_equal(
        c4_ind, lam4_expected,
        label="lambda_4 = 2 g^2 sin^2(beta)/(3 kbar2)")
    rw.print("")
    rw.print("  induced mass coeff   = " + str(sp.simplify(c2_ind)))
    rw.print("  induced quartic      = " + str(sp.simplify(c4_ind)))
    rw.print("  " + msg_c4)

    # sign check with positive symbols
    c4_pos = c4_ind.subs([(g, g_pos), (kbar2, k_pos)])
    ok_sign, msg_sign = check_sign(
        c4_pos.subs(sin(beta)**2, Rational(1, 2)),
        expected_positive=True,
        label="lambda_4 > 0 at partial lock")
    rw.print("  " + msg_sign)
    rw.print("")
    rw.print("  *** POSITIVE quartic GENERATED at partial lock ***")
    rw.print("  [PDTP Original, DERIVED algebra; mechanism SPECULATIVE]")
    rw.print("  Note: it comes with a negative (tachyonic) mass term that")
    rw.print("  drives phi_- away from 0 toward the locked value pi/2 --")
    rw.print("  the full induced potential -c sin^2(phi_-) has minima at")
    rw.print("  phi_- = +/- pi/2.  The transient rolling energy is the")
    rw.print("  EDE candidate.  [SPECULATIVE]")

    return {'J': J, 'V_ind': V_ind, 'c2_ind': sp.simplify(c2_ind),
            'lambda4': sp.simplify(c4_ind),
            'gaussian_exact': ok_gauss,
            'closed_form_ok': ok_form,
            'lambda4_matches': ok_c4,
            'sign_positive': ok_sign}


# ===========================================================================
# S5: MAGNITUDE CHECK
# ===========================================================================

def compute_magnitude(rw, s4):
    """
    Part 88 requirement: lambda_4 ~ g.  Evaluate lambda_4/g for the
    natural stiffness kbar2 = 2g (mode at the condensate gap scale,
    Part 61: mass^2 of the locked modes = 2g) at several beta.
    """
    rw.subsection("S5: Magnitude check vs Part 88 requirement")

    lam4 = s4['lambda4']
    lam4_at_gap = simplify(lam4.subs(kbar2, 2 * g))
    ratio_expr = simplify(lam4_at_gap / g)
    rw.print("  at kbar2 = 2g:  lambda_4/g = " + str(ratio_expr))

    rows = []
    vals = {}
    for b_deg in (5, 30, 45, 90):
        b = np.deg2rad(b_deg)
        v = float(ratio_expr.subs(beta, b))
        vals[b_deg] = v
        rows.append([str(b_deg), "{:.4f}".format(v)])
    rw.table(["beta [deg]", "lambda_4 / g"], rows)

    rw.print("  Part 88 requires lambda_4 ~ g (order unity ratio).")
    rw.print("  At order-unity partial lock (beta ~ 45-90 deg):")
    rw.print("  lambda_4/g = {:.3f} - {:.3f}  -> within a factor ~6 of".format(
        vals[45], vals[90]))
    rw.print("  the requirement.  SHAPE and ORDER OF MAGNITUDE supplied.")
    rw.print("  The absolute EDE energy density still depends on the")
    rw.print("  cosmological g and beta(z) evolution -- NOT derived here.")
    rw.print("  [PARTIAL]")

    return {'ratio_expr': ratio_expr, 'ratio_45': vals[45],
            'ratio_90': vals[90],
            'order_unity': 0.01 < vals[45] and vals[90] <= 1.0}


# ===========================================================================
# S6: TWO-PHASE COMPATIBILITY (beta -> 0 LIMIT)
# ===========================================================================

def verify_locked_limit(rw, s4):
    """
    Sudoku rule 4 (CLAUDE.md): new results must not break the two-phase
    structure.  The induced term must vanish IDENTICALLY at full lock
    (beta = 0), leaving Part 61/63 results (Newton's 3rd law, biharmonic
    equation, Jeans eigenvalue) untouched today.
    """
    rw.subsection("S6: Locked limit beta -> 0 (today)")

    V_ind_locked = simplify(s4['V_ind'].subs(beta, 0))
    lam4_locked = simplify(s4['lambda4'].subs(beta, 0))
    J_locked = simplify(s4['J'].subs(beta, 0))
    rw.print("  V_ind(beta=0)    = " + str(V_ind_locked))
    rw.print("  lambda_4(beta=0) = " + str(lam4_locked))
    rw.print("  J(beta=0)        = " + str(J_locked))
    ok = (V_ind_locked == 0) and (lam4_locked == 0) and (J_locked == 0)
    rw.print("  -> induced term vanishes identically at full lock: "
             + ("YES" if ok else "NO"))
    rw.print("  Part 61/63 derivations (Newton 3rd law psi_dd = -2 phi_+_dd,")
    rw.print("  biharmonic nabla^4 + 4g^2, Jeans +2 sqrt(2) g) are all")
    rw.print("  evaluated AT the locked background -> unchanged. [VERIFIED]")
    return {'vanishes_at_lock': ok}


# ===========================================================================
# S7: SUDOKU CONSISTENCY CHECK
# ===========================================================================

def sudoku_check(rw, s1, s2, s3, s4, s5, s6):
    """Reads computed values from the step dicts (RECHECK trace path)."""
    rw.section("S7: Sudoku consistency check")

    tests = []

    def add(name, value, condition, note):
        tests.append((name, value, "PASS" if condition else "FAIL", note))

    add("T1 product identity residual = 0",
        str(s1['residual']), s1['identity_ok'] and s1['residual'] == 0,
        "Part 61 reproduced")

    add("T2 tree quartic = -g/12 (Part 88 Eq 88.13)",
        str(s2['tree_quartic']), s2['matches_88_13'],
        "tree channel NEGATIVE sign")

    add("T3 zero-point quartic < 0",
        "{:.5f}*g".format(s3['zp_quartic_num']), s3['zp_is_negative'],
        "one-loop channel NEGATIVE sign")

    add("T4 Gaussian V_min = V0 - J^2/(2M) exact",
        "exact", s4['gaussian_exact'], "textbook matching formula")

    add("T5 V_ind closed form -c sin^2(phi_-)",
        "match", s4['closed_form_ok'], "induced potential")

    add("T6 lambda_4 = 2g^2 sin^2(beta)/(3 kbar2)",
        "match", s4['lambda4_matches'], "series = closed form")

    add("T7 lambda_4 > 0 for beta != 0",
        "positive", s4['sign_positive'],
        "REQUIRED sign achieved [PDTP Original]")

    add("T8 magnitude lambda_4/g order unity at lock scale",
        "{:.3f} at beta=90deg".format(s5['ratio_90']), s5['order_unity'],
        "Part 88 requirement ~g within factor ~3-6")

    add("T9 induced term vanishes at beta = 0",
        "all zero", s6['vanishes_at_lock'],
        "w = -1 today recovered; Parts 61/63/87 intact")

    add("T10 induced mass^2 < 0 at partial lock (tachyonic roll)",
        str(s4['c2_ind']),
        simplify(s4['c2_ind'].subs([(g, 1), (kbar2, 2),
                                    (beta, sp.pi / 4)])) < 0,
        "phi_- driven 0 -> pi/2; transient EDE [SPECULATIVE]")

    rows = [[t[0], t[1], t[2]] for t in tests]
    rw.table(["test", "computed value", "verdict"], rows)
    n_pass = sum(1 for t in tests if t[2] == "PASS")
    rw.print("")
    rw.print("  Score: {}/{} PASS".format(n_pass, len(tests)))
    return {'n_pass': n_pass, 'n_total': len(tests)}


# ===========================================================================
# MAIN
# ===========================================================================

def main():
    rw = ReportWriter(os.path.join(_HERE, "outputs"),
                      label="phi_minus_quartic")
    rw.section("Phase 85 (Part 117): origin of a positive phi_-^4 term")
    rw.print("Part 88 gap: EDE needs lambda_4 ~ +g; cosine gives -g/12.")
    rw.print("Three channels tested by direct computation.")

    s1 = verify_product_identity(rw)
    s2 = derive_tree_quartic(rw)
    s3 = derive_zeropoint_quartic(rw)
    s4 = derive_induced_quartic(rw)
    s5 = compute_magnitude(rw, s4)
    s6 = verify_locked_limit(rw, s4)
    s7 = sudoku_check(rw, s1, s2, s3, s4, s5, s6)

    rw.section("Verdict (Part 117)")
    rw.print("  Channel 1 (tree cosine):    quartic -g/12      [NEGATIVE]")
    rw.print("  Channel 2 (zero-point):     quartic < 0        [NEGATIVE]")
    rw.print("  Channel 3 (induced, partial lock):")
    rw.print("      lambda_4 = 2 g^2 sin^2(beta) / (3 kbar2) > 0")
    rw.print("      = (g/3) sin^2(beta) at the gap scale kbar2 = 2g")
    rw.print("      [PDTP Original -- POSITIVE quartic of the required")
    rw.print("       order, present ONLY while locking is incomplete]")
    rw.print("  EDE switches itself off as the universe locks (beta -> 0):")
    rw.print("  transient early dark energy, w -> -1 today automatically.")
    rw.print("  Amplitude/redshift profile beta(z): OPEN (needs cosmological")
    rw.print("  locking history).")
    rw.print("  Sudoku: {}/{} PASS".format(s7['n_pass'], s7['n_total']))
    rw.close()


if __name__ == "__main__":
    main()
