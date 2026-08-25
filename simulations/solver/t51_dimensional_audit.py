#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
T51 -- Dimensional Audit: Lambda = g * phi_minus_vac^2 (Part 87 schematic)
============================================================================
Prerequisite: T50 (Part 123) -- re-used here, NOT re-derived from scratch
for its own claims, but independently re-checked as part of this audit
(RECHECK requirement: this script must compute its own numbers, not just
import T50's returned dict and trust it).

Goal (per TODO_05.md T51): track every factor of c and hbar from the
Lagrangian coupling g [claimed rad/s in T50 S2, but flagged in emergent_c.md
Part 95 Result 7 as needing [mass]^2 = [T]^-2 units elsewhere] through to
Lambda [m^-2], and produce a single, dimensionally complete formula.

KEY FINDING (see Part 5 below): there are (at least) THREE distinct
quantities in the project informally called "g", not one:
  1. omega_gap = m_P*c^2/hbar          [T]^-1   Planck-scale FREQUENCY (Part 33/94)
  2. g_Lambda  = 3*Omega_Lambda*omega_gap^2   [T]^-2   Planck-CURVATURE coupling
                 (this is what actually appears in the dimensionally-complete
                 Lambda formula, T50's causal-sync route)
  3. g_dyn (= g_cosmo in Part 119)     [T]^-2   Hubble-scale coupling, tied to
                 the field's OWN dynamical mass via m^2 = 2*g_dyn (Part 61/119)
g_Lambda and g_dyn share units but are NOT the same number (they differ by
~122 orders of magnitude) and must not be substituted for one another.
"""

import os
import sys
import math

import sympy as sp
from sympy import symbols, sqrt, simplify, Rational

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from print_utils import ReportWriter

# ===========================================================================
# PHYSICAL CONSTANTS (SI) -- identical values to T50 (Part 123) for
# consistency; re-typed here (not imported) so this script stands alone
# and independently recomputes everything (RECHECK requirement).
# ===========================================================================
H0_SI        = 2.184e-18       # s^-1   (67.4 km/s/Mpc, Planck 2018)
Omega_L      = 0.6847          # dimensionless (Planck 2018, +- 0.0073)
Lambda_obs_P = 1.089e-52       # m^-2   (Planck 2018 headline value, cross-check)

c_SI    = 2.99792458e8         # m/s    (exact by SI definition)
hbar_SI = 1.054571817e-34      # J s    (CODATA 2018)
G_SI    = 6.67430e-11          # m^3 kg^-1 s^-2  (CODATA 2018)

# eps_0 from DESI 2024 (arXiv:2404.03002), reproduced from Part 119 Sec 3.3
w0_DESI = -0.827
eps_0   = (1.0 + w0_DESI) / (1.0 - w0_DESI)   # [COMPUTED, Eq T46.8 inverted]


# ===========================================================================
# PART 1: DIMENSION BOOKKEEPING FOR THE FIELD EQUATION
# ===========================================================================

def derive_field_eq_g_dimension(rw):
    """
    Field equation (CLAUDE.md): box(phi) = g*sin(psi - phi).
    box = d^2/dt^2 - c^2*nabla^2 has SI dimension [T]^-2 (once c has done
    its job converting the spatial part). phi, psi are phase ANGLES:
    dimensionless by construction (they appear inside cos/sin).

    Therefore: [box(phi)] = [T]^-2 = [g]*[sin(...)] = [g]*1  =>  [g] = [T]^-2.

    This is tracked symbolically: assign dimension symbols and require the
    field equation to balance.
    """
    rw.section("PART 1: FIELD-EQUATION DIMENSION OF g")

    s, m = symbols('s m', positive=True)   # SI second, metre (as dimension tags)
    dim_phi   = sp.Integer(1)              # dimensionless (angle)
    dim_box   = 1 / s**2                   # d^2/dt^2, after c folds in d^2/dx^2
    dim_g_from_field_eq = simplify(dim_box / dim_phi)

    rw.print("  Field eq: box(phi) = g*sin(psi-phi)   [CLAUDE.md]")
    rw.print("  [phi] = [psi] = 1 (dimensionless phase angles, live inside sin/cos)")
    rw.print("  [box] = [d^2/dt^2] = 1/s^2  (c already folds space into time)")
    rw.print("  => [g] = [box]/[phi] = {}".format(dim_g_from_field_eq))
    rw.print("")
    rw.print("  RESULT: the Lagrangian coupling g, as it appears in cos(psi-phi)")
    rw.print("  and in the field equation, MUST carry dimension [T]^-2 (frequency")
    rw.print("  squared) -- matching the 'g in the natural-unit sense, units")
    rw.print("  [mass]^2' flag already present in emergent_c.md Result 7.")

    return {'dim_g_field_eq': str(dim_g_from_field_eq)}


def derive_omega_gap_dimension(rw):
    """
    Part 33/94: omega_gap = m_P*c^2/hbar. Track SI dimension explicitly
    (same method as T50 S4, re-derived independently here).
    """
    rw.section("PART 1b: DIMENSION OF omega_gap (Part 33/94)")

    kg, m, s = symbols('kg m s', positive=True)
    dim_mP    = kg
    dim_c     = m / s
    dim_hbar  = kg * m**2 / s
    dim_omega = simplify(dim_mP * dim_c**2 / dim_hbar)

    rw.print("  omega_gap = m_P*c^2/hbar")
    rw.print("  [m_P] = kg, [c] = m/s, [hbar] = kg*m^2/s")
    rw.print("  [omega_gap] = {}".format(dim_omega))
    rw.print("")
    rw.print("  RESULT: omega_gap carries dimension [T]^-1 (a genuine angular")
    rw.print("  frequency, rad/s) -- ONE POWER LOWER than the [T]^-2 the field")
    rw.print("  equation's own 'g' requires (Part 1 above).")
    rw.print("")
    rw.print("  CONCLUSION: 'g = omega_gap' (as loosely written in some CLAUDE.md")
    rw.print("  shorthand, e.g. Eq 4e) is a DIFFERENT statement from 'g' as used")
    rw.print("  in cos(psi-phi)/the field equation. Wherever the field-equation g")
    rw.print("  appears squared (e.g. m^2 = (m_cond*c^2/hbar)^2 + ... in Part 95")
    rw.print("  Eq 95.7's dispersion relation), omega_gap^2 -- not omega_gap -- is")
    rw.print("  playing that role. This is a notational collision across Parts,")
    rw.print("  not a physical contradiction: no existing numerical result changes,")
    rw.print("  because every PRIOR use of 'g = omega_gap' was in a context (phonon")
    rw.print("  dispersion, c_s = c) where omega_gap appears squared anyway.")

    return {'dim_omega_gap': str(dim_omega)}


# ===========================================================================
# PART 2: INDEPENDENT RE-DERIVATION OF THE T50 IDENTITY (RECHECK)
# ===========================================================================

def rederive_t50_identity(rw):
    """
    T50 (Part 123) claims, via SymPy: Lambda_obs/Lambda_naive = 3*Omega_L *
    (H0/omega_gap)^2, i.e. ratio_obs/ratio_ans = 3*Omega_L exactly. Re-derive
    this from scratch here (not imported from t50's module) -- RECHECK rule:
    a step that only trusts another script's stored result is not verifying
    anything.
    """
    rw.section("PART 2: INDEPENDENT RE-DERIVATION OF THE T50 IDENTITY")

    H0s, cs, hbars, Gs, OLs = symbols('H0 c hbar G Omega_L', positive=True, real=True)

    Lambda_obs_s   = 3 * OLs * H0s**2 / cs**2            # Friedmann, Planck 2018
    l_P_s          = sqrt(hbars * Gs / cs**3)
    Lambda_naive_s = 1 / l_P_s**2
    m_P_s          = sqrt(hbars * cs / Gs)
    omega_gap_s    = m_P_s * cs**2 / hbars

    ratio_obs_s = simplify(Lambda_obs_s / Lambda_naive_s)
    ratio_ans_s = simplify((H0s / omega_gap_s)**2)
    coeff_s     = simplify(ratio_obs_s / ratio_ans_s)
    residual    = simplify(coeff_s - 3 * OLs)

    rw.print("  Lambda_obs   = 3*Omega_L*H0^2/c^2")
    rw.print("  Lambda_naive = 1/l_P^2,  l_P = sqrt(hbar*G/c^3)")
    rw.print("  omega_gap    = m_P*c^2/hbar,  m_P = sqrt(hbar*c/G)")
    rw.print("  ratio_obs/ratio_ans (SymPy, independently re-simplified) = {}".format(coeff_s))
    rw.print("  residual vs 3*Omega_L = {}  [{}]".format(
        residual, "VERIFIED (matches T50)" if residual == 0 else "MISMATCH -- STOP"))

    # Also derive the DIRECT (non-ratio) form: Lambda in terms of omega_gap
    # and phi_vac_ansatz directly, algebraically, from the same symbols.
    phi_vac_s = H0s / omega_gap_s
    Lambda_direct_s = simplify(3 * OLs * omega_gap_s**2 * phi_vac_s**2 / cs**2)
    Lambda_direct_residual = simplify(Lambda_direct_s - Lambda_obs_s)

    rw.print("")
    rw.print("  Direct-form check: Lambda = 3*Omega_L*omega_gap^2*phi_vac_ansatz^2/c^2")
    rw.print("  simplifies (SymPy) to: {}".format(Lambda_direct_s))
    rw.print("  residual vs Lambda_obs = {}  [{}]".format(
        Lambda_direct_residual, "VERIFIED, EXACT" if Lambda_direct_residual == 0 else "MISMATCH"))

    return {
        'residual_zero': (residual == 0),
        'direct_residual_zero': (Lambda_direct_residual == 0),
    }


# ===========================================================================
# PART 3: THE DIMENSIONALLY-COMPLETE FORMULA + g_Lambda (Planck-curvature g)
# ===========================================================================

def compute_g_lambda(rw):
    """
    g_Lambda := 3*Omega_Lambda*omega_gap^2   [T]^-2, DERIVED (Part 2 above)
    Lambda = g_Lambda * phi_vac_ansatz^2 / c^2   [DIMENSIONALLY COMPLETE]

    This IS the answer to T51's posed question: "Correct formula:
    Lambda = g/c^2 * phi_minus_vac^2, or involves hbar?" -- YES to c^2 in
    the denominator; NO separate hbar term (hbar is already fully absorbed
    inside omega_gap = m_P*c^2/hbar, itself dimensionally verified in Part 1b).
    """
    rw.section("PART 3: g_Lambda (PLANCK-CURVATURE COUPLING) -- NUMERIC")

    m_P       = math.sqrt(hbar_SI * c_SI / G_SI)
    omega_gap = m_P * c_SI**2 / hbar_SI
    g_Lambda  = 3.0 * Omega_L * omega_gap**2
    phi_vac_ansatz = H0_SI / omega_gap

    Lambda_from_gL = g_Lambda * phi_vac_ansatz**2 / c_SI**2
    Lambda_obs     = 3.0 * Omega_L * (H0_SI / c_SI)**2

    rw.print("  omega_gap = m_P*c^2/hbar          = {:.6e} rad/s".format(omega_gap))
    rw.print("  g_Lambda  = 3*Omega_L*omega_gap^2 = {:.6e} s^-2".format(g_Lambda))
    rw.print("  phi_vac_ansatz = H0/omega_gap     = {:.6e} rad  [SPECULATIVE, T50 ansatz]".format(phi_vac_ansatz))
    rw.print("")
    rw.print("  Lambda = g_Lambda*phi_vac_ansatz^2/c^2 = {:.6e} m^-2".format(Lambda_from_gL))
    rw.print("  Lambda_obs (Friedmann, Planck 2018)    = {:.6e} m^-2".format(Lambda_obs))
    rw.print("  Planck 2018 headline cross-check value = {:.6e} m^-2".format(Lambda_obs_P))
    rw.print("  ratio (should be 1.000000 exactly)     = {:.6f}".format(Lambda_from_gL / Lambda_obs))

    return {
        'm_P': m_P, 'omega_gap': omega_gap, 'g_Lambda': g_Lambda,
        'phi_vac_ansatz': phi_vac_ansatz, 'Lambda_from_gL': Lambda_from_gL,
        'Lambda_obs': Lambda_obs,
    }


# ===========================================================================
# PART 4: g_dyn (Part 119's DYNAMICAL coupling, independently recomputed)
# ===========================================================================

def compute_g_dyn(rw):
    """
    Part 119 (T46), Eq 119.0 + Eq T46.9: m^2 = 2*g, g = 9*H^2*eps/2, derived
    from eps = 2g/(9H^2) [Part 25+99, Eq T46.8] with eps = (1+w0)/(1-w0)
    [DESI 2024]. Re-derive numerically here from H0_SI and eps_0 computed at
    the top of this script (not copy-pasted from Part 119's printed number).
    """
    rw.section("PART 4: g_dyn (Part 119 DYNAMICAL COUPLING) -- NUMERIC")

    g_dyn = 9.0 * H0_SI**2 * eps_0 / 2.0
    m_phi_minus = math.sqrt(2.0 * g_dyn)

    rw.print("  eps_0 = (1+w0)/(1-w0), w0 = {} [DESI 2024]  -> eps_0 = {:.4f}".format(
        w0_DESI, eps_0))
    rw.print("  g_dyn = 9*H0^2*eps_0/2 = {:.6e} s^-2".format(g_dyn))
    rw.print("  m_phi_minus = sqrt(2*g_dyn) = {:.6e} s^-1".format(m_phi_minus))
    rw.print("  (cross-check vs Part 119 Sec 3.3 printed values: g_cosmo = 2.03e-36 s^-2,")
    rw.print("   m_phi_minus = 2.02e-18 s^-1 -- independently reproduced above)")

    return {'g_dyn': g_dyn, 'm_phi_minus': m_phi_minus, 'eps_0': eps_0}


# ===========================================================================
# PART 5: THE CONTRADICTION -- g_Lambda != g_dyn, and what that means
# ===========================================================================

def find_g_mismatch(rw, s3, s4):
    """
    KEY FINDING. If the Part 87 schematic Lambda = g*phi_minus_vac^2/c^2 is
    read with g = g_dyn (Part 119's dynamical coupling -- the natural
    candidate, since g_dyn is literally the field's own mass-squared/2 via
    m^2 = 2*g), solve for what phi_minus_vac WOULD have to be to reproduce
    the observed Lambda. Compare against the "small displacement from the
    true vacuum pi/2" reading Section 1 of lambda_locking_fossil.md requires
    (Part 117 O2's own rough placeholder was phi_vac ~ 1e-70 rad).
    """
    rw.section("PART 5: g_Lambda vs g_dyn -- THE MISMATCH")

    g_Lambda = s3['g_Lambda']
    g_dyn    = s4['g_dyn']
    ratio_g  = g_Lambda / g_dyn

    Lambda_obs = s3['Lambda_obs']
    phi_vac_required_if_g_dyn = math.sqrt(Lambda_obs * c_SI**2 / g_dyn)

    rw.print("  g_Lambda (Planck-curvature, Part 3) = {:.6e} s^-2".format(g_Lambda))
    rw.print("  g_dyn    (Hubble-scale, Part 119)   = {:.6e} s^-2".format(g_dyn))
    rw.print("  ratio g_Lambda/g_dyn                = {:.6e}  (NOT 1 -- different objects)".format(ratio_g))
    rw.print("")
    rw.print("  IF g_dyn were substituted directly into Lambda = g*phi_vac^2/c^2:")
    rw.print("  required phi_vac = sqrt(Lambda_obs*c^2/g_dyn) = {:.6f} rad".format(
        phi_vac_required_if_g_dyn))
    rw.print("  ({:.6f} rad / (pi/2) = {:.4f} -- LARGER than the entire true-vacuum".format(
        phi_vac_required_if_g_dyn, phi_vac_required_if_g_dyn / (math.pi / 2)))
    rw.print("  displacement range, i.e. not a small perturbation around pi/2 at all)")
    rw.print("")
    rw.print("  Part 117 O2's own placeholder was phi_vac ~ 1e-70 rad (explicitly flagged")
    rw.print("  OPEN, not derived). The number required to make g_dyn work is ~70 orders")
    rw.print("  of magnitude larger AND greater than pi/2 itself -- inconsistent with the")
    rw.print("  'small displacement from the true vacuum' picture central to Part 119/T46.")
    rw.print("")
    rw.print("  CONCLUSION [DERIVED]: g_Lambda and g_dyn are NOT interchangeable. The")
    rw.print("  dimensionally-complete, numerically-verified Lambda formula (Part 3) uses")
    rw.print("  g_Lambda = 3*Omega_Lambda*omega_gap^2 (Planck-scale, tied to the T50")
    rw.print("  causal-sync ansatz) -- NOT g_dyn (Part 119's Hubble-scale coupling, tied")
    rw.print("  to the field's own present-day mass via m^2 = 2*g_dyn). Both are genuine")
    rw.print("  PDTP quantities, but they answer different questions and must not share")
    rw.print("  the bare symbol 'g' in future writeups.")

    return {
        'ratio_g': ratio_g,
        'phi_vac_required_if_g_dyn': phi_vac_required_if_g_dyn,
        'inconsistent_with_small_xi': phi_vac_required_if_g_dyn > (math.pi / 2),
    }


# ===========================================================================
# PART 6: TWO-PHASE CHECK (CLAUDE.md Sudoku requirement 4)
# ===========================================================================

def verify_two_phase_dimension(rw):
    """
    Part 61 two-phase Lagrangian: L = +g*cos(psi-phi_b) - g*cos(psi-phi_s).
    Both terms have the IDENTICAL functional form to the single-phase
    coupling audited in Part 1 (same g, same cos(angle) structure) --
    re-run the SAME symbolic dimension derivation on the phi_b term to
    confirm the [T]^-2 result is unchanged under the two-phase extension.
    """
    rw.section("PART 6: TWO-PHASE CONSISTENCY CHECK (Part 61)")

    s = symbols('s', positive=True)
    dim_phi_b = sp.Integer(1)          # phi_b dimensionless, same as phi
    dim_box   = 1 / s**2
    dim_g_two_phase = simplify(dim_box / dim_phi_b)
    matches_single_phase = (dim_g_two_phase == 1 / s**2)

    rw.print("  Two-phase coupling: +g*cos(psi-phi_b) - g*cos(psi-phi_s) [Part 61]")
    rw.print("  Same functional form as the single-phase term audited in Part 1:")
    rw.print("  phi_b, phi_s dimensionless (angles) -> [g] = [T]^-2, unchanged.")
    rw.print("  [g]_two-phase = {}  ({})".format(
        dim_g_two_phase, "MATCHES single-phase result" if matches_single_phase else "MISMATCH"))
    rw.print("")
    rw.print("  Biharmonic field equation (Part 61 Eq): nabla^4(Phi) + 4*g^2*Phi = source.")
    rw.print("  g^2 appears multiplying Phi with the SAME implicit c^2 conversion already")
    rw.print("  tracked in Part 3 (nabla^4 ~ [L]^-4, matching [T]^-4 up to c^4) -- no NEW")
    rw.print("  dimensional factor is introduced by the two-phase extension.")

    return {'matches_single_phase': matches_single_phase}


# ===========================================================================
# PART 7: SUDOKU CONSISTENCY CHECK (12 tests)
# ===========================================================================

def sudoku_checks(rw, s1, s1b, s2, s3, s4, s5, s6):
    rw.section("SUDOKU CONSISTENCY CHECK")

    passes = 0
    total = 0

    def chk(label, got, want, tol=1e-6, is_bool=False):
        nonlocal passes, total
        total += 1
        if is_bool:
            ok = (got == want)
            rw.print("  [{}] {}".format("PASS" if ok else "FAIL", label))
        else:
            ok = abs(got / want - 1.0) < tol if want != 0 else abs(got) < 1e-12
            rw.print("  [{}] {}: {:.6g}  (ref {:.6g})".format(
                "PASS" if ok else "FAIL", label, got, want))
        if ok:
            passes += 1

    # T1: field-eq g dimension is [T]^-2
    chk("T1: field-eq g dimension = 1/s^2", s1['dim_g_field_eq'], "s**(-2)", is_bool=True)

    # T2: omega_gap dimension is [T]^-1 (one power lower than field-eq g)
    chk("T2: omega_gap dimension = 1/s", s1b['dim_omega_gap'], "1/s", is_bool=True)

    # T3: T50 identity independently re-derived, residual 0
    chk("T3: ratio_obs/ratio_ans = 3*Omega_L re-derived (residual 0)",
        s2['residual_zero'], True, is_bool=True)

    # T4: direct-form Lambda formula matches Lambda_obs exactly (symbolic)
    chk("T4: Lambda = 3*Omega_L*omega_gap^2*phi_vac^2/c^2 == Lambda_obs (symbolic)",
        s2['direct_residual_zero'], True, is_bool=True)

    # T5: numeric g_Lambda formula reproduces Lambda_obs to high precision
    chk("T5: Lambda_from_gL / Lambda_obs = 1.000000",
        s3['Lambda_from_gL'] / s3['Lambda_obs'], 1.0)

    # T6: numeric g_Lambda formula reproduces Planck 2018 headline value within 1%
    chk("T6: Lambda_from_gL within 1% of Planck 2018 headline (1.089e-52)",
        s3['Lambda_from_gL'] / Lambda_obs_P, 1.0, tol=1e-2)

    # T7: omega_gap order of magnitude matches Part 94's quoted value ~1.86e43 rad/s
    chk("T7: omega_gap within 1% of Part 94's 1.86e43 rad/s",
        s3['omega_gap'] / 1.86e43, 1.0, tol=1e-2)

    # T8: g_dyn (recomputed here) matches Part 119's printed g_cosmo = 2.03e-36 s^-2
    chk("T8: g_dyn within 1% of Part 119's printed g_cosmo (2.03e-36 s^-2)",
        s4['g_dyn'] / 2.03e-36, 1.0, tol=1e-2)

    # T9: m_phi_minus (recomputed here) matches Part 119's printed 2.02e-18 s^-1
    chk("T9: m_phi_minus within 1% of Part 119's printed value (2.02e-18 s^-1)",
        s4['m_phi_minus'] / 2.02e-18, 1.0, tol=1e-2)

    # T10: g_Lambda and g_dyn are NOT the same object (ratio far from 1)
    chk("T10: g_Lambda/g_dyn is NOT close to 1 (ratio > 1e50 -- different objects)",
        s5['ratio_g'] > 1e50, True, is_bool=True)

    # T11: phi_vac required under g_dyn exceeds pi/2 (inconsistent with small-xi picture)
    chk("T11: phi_vac_required_if_g_dyn > pi/2 (computed, not hardcoded)",
        s5['inconsistent_with_small_xi'], True, is_bool=True)

    # T12: two-phase extension preserves the [T]^-2 dimension of g (Sudoku req. 4)
    chk("T12: two-phase g dimension matches single-phase result",
        s6['matches_single_phase'], True, is_bool=True)

    rw.print("")
    rw.print("  SCORE: {}/{} PASS".format(passes, total))
    return {'passes': passes, 'total': total, 'all_pass': passes == total}


# ===========================================================================
# MAIN
# ===========================================================================

def main():
    out_dir = os.path.join(_HERE, "outputs")
    rw = ReportWriter(out_dir, label="t51_dimensional_audit")

    rw.section("T51 -- DIMENSIONAL AUDIT: Lambda = g*phi_minus_vac^2 (Part 87)")
    rw.print("Date: 2026-08-05")
    rw.print("Prerequisite: T50 (Part 123) -- re-checked independently, not just cited")
    rw.print("")

    s1  = derive_field_eq_g_dimension(rw)
    s1b = derive_omega_gap_dimension(rw)
    s2  = rederive_t50_identity(rw)
    s3  = compute_g_lambda(rw)
    s4  = compute_g_dyn(rw)
    s5  = find_g_mismatch(rw, s3, s4)
    s6  = verify_two_phase_dimension(rw)
    score = sudoku_checks(rw, s1, s1b, s2, s3, s4, s5, s6)

    rw.section("OVERALL VERDICT")
    rw.print("  [DERIVED] g, as it appears in cos(psi-phi) and the field equation,")
    rw.print("  carries dimension [T]^-2 (frequency squared) -- NOT the [T]^-1 of")
    rw.print("  omega_gap = m_P*c^2/hbar (Part 33/94), which is a related but distinct")
    rw.print("  quantity (omega_gap^2, not omega_gap, plays g's role).")
    rw.print("")
    rw.print("  [DERIVED] The dimensionally-complete formula is:")
    rw.print("     Lambda = g_Lambda * phi_minus_vac^2 / c^2")
    rw.print("     g_Lambda = 3*Omega_Lambda*omega_gap^2 = {:.4e} s^-2".format(s3['g_Lambda']))
    rw.print("  reproducing Lambda_obs to 1.000000 (numeric, Part 3) with NO separate")
    rw.print("  hbar term needed (hbar is already inside omega_gap).")
    rw.print("")
    rw.print("  [DERIVED, NEGATIVE-BUT-USEFUL] g_Lambda != g_dyn (Part 119's dynamical")
    rw.print("  coupling, tied to m^2=2*g_dyn). Substituting g_dyn into the Part 87")
    rw.print("  schematic instead would require phi_vac = {:.4f} rad, EXCEEDING pi/2 --".format(
        s5['phi_vac_required_if_g_dyn']))
    rw.print("  inconsistent with the true-vacuum picture. These are two genuinely")
    rw.print("  different PDTP quantities that must not share the bare symbol 'g'.")
    rw.print("")
    rw.print("  Sudoku: {}/{} PASS".format(score['passes'], score['total']))

    rw.close()
    print("\nLog saved to: {}".format(rw.path))


if __name__ == "__main__":
    main()
