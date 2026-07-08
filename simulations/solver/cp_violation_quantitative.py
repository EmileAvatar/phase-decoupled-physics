#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cp_violation_quantitative.py -- Phase 93: Quantitative B4 Revisit (Part 125)
=============================================================================
B4 quantitative pass (extends Phase 55 cp_violation.py, Part 85).

WHY A REVISIT: Part 85 derived the L5 vacuum shift around phi_- = 0, but
Parts 62/119 established the TRUE vacuum is phi_- = pi/2 (the Part 85
potential -2g*cos(phi_-) is the pre-Part-62 form). The TODO_03 B4 checklist
item "find shifted vacuum phi_- = pi/2 - delta" was therefore still open.
This script re-derives everything at the true vacuum and computes the
quantitative pieces (rate asymmetry, eta band, strong-CP relaxation).

RESULTS DERIVED HERE:
  S3 True-vacuum shift: V = -A*sin(phi_-) - eps*sin(2*phi_-), A = 2*g*Phi
     -> phi_-* = pi/2 - delta with delta = 2*eps/A + O(eps^3)
     -> with A = 2g: delta = eps/g -- Part 85 magnitude PRESERVED  [DERIVED]
     -> m^2 = A + O(eps^2): Part 119 Eq 119.0 preserved            [DERIVED]
  S4 KEY CORRECTION: the reflection x -> pi - x maps V(.;eps) to V(.;-eps)
     EXACTLY, so the CP-conjugate vacuum energies are EXACTLY DEGENERATE.
     Part 85's Sakharov-condition-2 argument (energy splitting V(delta) !=
     V(-delta)) does NOT survive at the true vacuum. CP violation instead
     enters through (a) vacuum ORIENTATION (CP|vac> = the other, degenerate
     vacuum: not self-conjugate) and (b) O(eps) RATE asymmetry along the
     roll path (pointwise path difference -2*eps*sin(2*x)).     [DERIVED]
  S5 Baryon asymmetry: eta = (1/g_*)*s*(2*eps/g) parametric band;
     central (g_*=100, s=0.1): required eps/g = 3.05e-7 (recovers 85.11);
     band over reasonable (g_*, s): [1.1e-8, 6.1e-6].          [COMPUTED]
     Sign: sign(eta) = sign(eps) -- convention, not predicted.  [DERIVED]
  S6 Strong CP: if theta is the DYNAMICAL condensate orientation, the
     vacuum energy E(theta) = K*(1 - cos(theta)) (dilute instanton gas;
     Vafa-Witten 1984 guarantees E(theta) >= E(0)) relaxes theta -> 0
     spontaneously -- condensate phase plays the axion role.
     U(1) limit: theta exactly removable (same algebra as L4). [DERIVED
     given the dynamical-theta premise, which is SPECULATIVE]
  S7 Two-phase compatibility is EXACT in the psi/phi_+ sector: the eps
     term depends only on phi_-, so Newton's 3rd law, Jeans eigenvalue,
     and biharmonic gravity are EXACTLY unchanged (not just O(eps^2)).
     The phi_- EOM gains the source +2*eps*cos(2*phi_-).       [DERIVED]

Sources:
  Sakharov (1967) JETP Lett. 5, 24 (three conditions)
  Kolb & Turner (1990) The Early Universe, Ch. 6 (eta estimate structure)
  Vafa & Witten (1984) Phys. Rev. Lett. 53, 535 (E(theta) >= E(0))
  Callan, Dashen & Gross (1976) Phys. Lett. B 63, 334 (instanton gas E(theta))
  Peccei & Quinn (1977) Phys. Rev. Lett. 38, 1440 (relaxation mechanism)
  PDG 2024: Jarlskog J = 3.08e-5 (CKM CP anchor); theta_QCD < 1e-10 (nEDM)
  Planck 2018: eta = 6.1e-10
  Part 61/62/63: two-phase Lagrangian, true vacuum pi/2
  Part 85: cp_violation.md (L4/L5/L6 classification)
  Part 117/119: tachyonic roll toward pi/2; locked vacuum m^2 = 2g

Output: simulations/solver/outputs/cp_violation_quantitative_<timestamp>.txt

ALL returned values are COMPUTED -- no hardcoded results (RECHECK rule).
"""

import os
import sys
import math

import sympy as sp
from sympy import (symbols, sin, cos, sqrt, atan, pi, simplify, diff,
                   series, nsolve, Rational, Function)

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from print_utils import ReportWriter

# ===========================================================================
# CONSTANTS
# ===========================================================================
ETA_OBS   = 6.1e-10          # Planck 2018 baryon-to-photon ratio
JARLSKOG  = 3.08e-5          # PDG 2024 CKM CP-violation invariant
THETA_MAX = 1e-10            # neutron EDM bound on theta_QCD

# SymPy symbols
x, e_s, g_s, A_s, d_s, K_s, th_s = symbols(
    'x eps g A delta K theta', real=True)
psi_s, phip_s, phim_s = symbols('psi phi_plus phi_minus', real=True)


# ===========================================================================
# S1: CP TRANSFORMATION RULES (re-verification)
# ===========================================================================

def verify_cp_rules(rw):
    """
    CP on real scalars: phi_b -> -phi_b, phi_s -> -phi_s, psi -> -psi
    => (psi - phi) -> -(psi - phi) and phi_- -> -phi_-.
    cos is CP-even, sin is CP-odd. L5's eps*sin(2*phi_-) is CP-odd;
    the two-phase g-term 2g*sin(psi-phi_+)*sin(phi_-) is CP-EVEN
    (both factors flip -> product invariant).
    """
    rw.section("S1: CP TRANSFORMATION RULES [SymPy]")

    cos_even = simplify(cos(-x) - cos(x)) == 0
    sin_odd  = simplify(sin(-x) + sin(x)) == 0

    # two-phase g-term: product of two sines -> CP-even
    Dp = psi_s - phip_s
    g_term    = 2 * g_s * sin(Dp) * sin(phim_s)
    g_term_cp = g_term.subs({psi_s: -psi_s, phip_s: -phip_s,
                             phim_s: -phim_s})
    g_even    = simplify(g_term_cp - g_term) == 0

    # eps-term: sin(2*phi_-) -> -sin(2*phi_-) -> CP-odd
    e_term    = e_s * sin(2 * phim_s)
    e_term_cp = e_term.subs(phim_s, -phim_s)
    e_odd     = simplify(e_term_cp + e_term) == 0

    rw.print("  cos(-x) = cos(x)  (CP-even): {}".format(cos_even))
    rw.print("  sin(-x) = -sin(x) (CP-odd):  {}".format(sin_odd))
    rw.print("  2g*sin(psi-phi_+)*sin(phi_-) CP-EVEN (both flip): {}".format(g_even))
    rw.print("  eps*sin(2*phi_-)             CP-ODD:              {}".format(e_odd))
    rw.print("")
    rw.print("  L5 = (CP-even g-sector) + (CP-odd eps-term): CP is broken")
    rw.print("  explicitly by eps != 0. [DERIVED, re-verifies Part 85 S2]")

    return {'cos_even': cos_even, 'sin_odd': sin_odd,
            'g_term_even': g_even, 'eps_term_odd': e_odd}


# ===========================================================================
# S2: L4 REMOVABILITY (phasor identity, SymPy exact)
# ===========================================================================

def verify_l4_removable(rw):
    """
    g*cos(x) + eps*sin(x) = R*cos(x - d), R = sqrt(g^2+eps^2), d = atan(eps/g).
    The sin term is absorbed by the shift x -> x + d (field redefinition
    psi' = psi - d): U(1)+sin is FAKE CP violation.
    [Source: phasor addition, standard trigonometry]
    """
    rw.section("S2: L4 REMOVABILITY -- U(1)+sin IS FAKE [SymPy]")

    # positive symbols required so cos(atan(e/g)) = g/sqrt(g^2+e^2) resolves
    gp, ep = symbols('g_pos eps_pos', positive=True)
    R   = sqrt(gp**2 + ep**2)
    d   = atan(ep / gp)
    lhs = gp * cos(x) + ep * sin(x)
    rhs = R * cos(x - d)
    resid = simplify(sp.expand_trig(rhs) - lhs)
    ok = (resid == 0)

    rw.print("  g*cos(x) + eps*sin(x) - sqrt(g^2+eps^2)*cos(x - atan(eps/g))")
    rw.print("  residual = {}   [{}]".format(resid, "VERIFIED" if ok else "FAIL"))
    rw.print("  -> absorbed by psi' = psi - atan(eps/g): L4 CP-FAKE. [DERIVED]")

    return {'l4_residual_zero': ok}


# ===========================================================================
# S3: TRUE-VACUUM SHIFT  phi_-* = pi/2 - delta  [KEY DERIVATION]
# ===========================================================================

def derive_true_vacuum_shift(rw):
    """
    True-vacuum potential (Parts 62/119: vacuum at pi/2, NOT 0):
      V(phi_-) = -A*sin(phi_-) - eps*sin(2*phi_-),  A = 2*g*Phi > 0
      (A = 2*g*cos(beta) in the cosmological background, T46.3)

    Substitute phi_- = pi/2 - d:
      sin(phi_-) = cos(d);  sin(2*phi_-) = sin(pi - 2d) = sin(2d)
      V(d) = -A*cos(d) - eps*sin(2d)
    Minimum: dV/dd = A*sin(d) - 2*eps*cos(2d) = 0
      => d = 2*eps/A + O(eps^3)                        (125.1)
      With A = 2g:  d = eps/g  -- Part 85 magnitude preserved.
    Mass: d2V/dd2 = A*cos(d) + 4*eps*sin(2d) = A + O(eps^2)  (125.2)
      -- Part 119 Eq 119.0 (m^2 = 2g at A = 2g) preserved.
    """
    rw.section("S3: TRUE-VACUUM SHIFT phi_-* = pi/2 - delta  [Eq 125.1]")

    V = -A_s * cos(d_s) - e_s * sin(2 * d_s)      # V in the d variable
    dV  = diff(V, d_s)
    d2V = diff(V, d_s, 2)

    # leading-order shift: series solve dV = 0 around d = 0
    dV_lin = dV.series(d_s, 0, 2).removeO()       # A*d - 2*eps + O(d^2)
    d_lead = solve_ok = None
    sols = sp.solve(sp.Eq(dV_lin, 0), d_s)
    d_lead = simplify(sols[0])
    solve_ok = simplify(d_lead - 2 * e_s / A_s) == 0

    # numeric root check at A = 1, eps = 1e-3 (nsolve full equation)
    A_num, e_num = 1.0, 1.0e-3
    d_root = float(nsolve(dV.subs({A_s: A_num, e_s: e_num}), d_s, 2e-3))
    d_pred = 2.0 * e_num / A_num

    # A = 2g reading
    d_2g = simplify(d_lead.subs(A_s, 2 * g_s))    # expect eps/g
    d_2g_ok = simplify(d_2g - e_s / g_s) == 0

    # mass at shifted vacuum: m^2 - A should scale as eps^2 (ratio 4 test)
    def m2(eps_val):
        droot = float(nsolve(dV.subs({A_s: A_num, e_s: eps_val}), d_s,
                             2 * eps_val / A_num))
        return float(d2V.subs({A_s: A_num, e_s: eps_val, d_s: droot}))
    dm2_e  = m2(e_num) - A_num
    dm2_2e = m2(2 * e_num) - A_num
    quad_ratio = dm2_2e / dm2_e                   # expect ~4 (O(eps^2))

    rw.print("  V(d) = -A*cos(d) - eps*sin(2d);  dV/dd = A*sin(d) - 2*eps*cos(2d)")
    rw.print("  Leading shift: d = {}  [= 2*eps/A: {}]".format(d_lead, solve_ok))
    rw.print("  Numeric root (A=1, eps=1e-3): d = {:.6e}  (pred {:.6e})".format(
        d_root, d_pred))
    rw.print("  A = 2g reading: d = {}  [= eps/g: {}]".format(d_2g, d_2g_ok))
    rw.print("    -> |delta| = eps/g: Part 85 magnitude PRESERVED at the")
    rw.print("       true vacuum (Eq 85.7 form corrected, value robust).")
    rw.print("  Mass: m^2(eps) - A = {:.4e}; m^2(2*eps) - A = {:.4e}".format(
        dm2_e, dm2_2e))
    rw.print("    ratio = {:.3f}  (4.0 expected: correction is O(eps^2))".format(
        quad_ratio))
    rw.print("    -> Part 119 Eq 119.0 (m^2 = 2g) preserved at O(eps^2). [Eq 125.2]")

    return {'d_lead_is_2eps_over_A': solve_ok, 'd_root': d_root,
            'd_pred': d_pred, 'd_2g_is_eps_over_g': d_2g_ok,
            'quad_ratio': quad_ratio}


# ===========================================================================
# S4: EXACT CP DEGENERACY -- correction to Part 85  [KEY RESULT]
# ===========================================================================

def derive_cp_degeneracy(rw):
    """
    Part 85 argued Sakharov condition 2 via vacuum ENERGY splitting
    V(delta) != V(-delta). At the true vacuum this argument FAILS:

    Reflection identity: substituting x -> pi - x in
      V(x; eps) = -A*sin(x) - eps*sin(2x)
    gives  V(pi - x; eps) = -A*sin(x) + eps*sin(2x) = V(x; -eps).
    So V(.; eps) and V(.; -eps) have EXACTLY the same minimum value:
    the CP-conjugate vacua are EXACTLY DEGENERATE.          (125.3)

    What survives:
    (a) ORIENTATION asymmetry: CP maps the vacuum onto the OTHER
        degenerate vacuum (displacement 2*delta in phi_-), so
        CP|vac> != |vac> -- the vacuum is not CP-invariant.
    (b) RATE asymmetry: the two roll paths differ POINTWISE at O(eps):
        V(x; eps) - V(pi - x; eps) = -2*eps*sin(2x)          (125.4)
        so transition rates toward the two orientations differ at
        O(eps/g) -- this is what feeds baryogenesis (condition 3
        carries the weight; condition 2 = CP-odd term in the rates).
    """
    rw.section("S4: EXACT CP DEGENERACY AT TRUE VACUUM  [Eq 125.3-125.4]")

    Vx = -A_s * sin(x) - e_s * sin(2 * x)

    # reflection identity (SymPy exact)
    V_ref  = Vx.subs(x, pi - x)
    resid1 = simplify(V_ref - Vx.subs(e_s, -e_s))
    refl_ok = (resid1 == 0)

    # numeric: minimize both branches, compare minimum values
    A_num, e_num = 1.0, 1.0e-2
    dVx = diff(Vx, x)
    x1 = float(nsolve(dVx.subs({A_s: A_num, e_s: e_num}), x,
                      math.pi / 2 - 2 * e_num))
    x2 = float(nsolve(dVx.subs({A_s: A_num, e_s: -e_num}), x,
                      math.pi / 2 + 2 * e_num))
    V1 = float(Vx.subs({A_s: A_num, e_s: e_num, x: x1}))
    V2 = float(Vx.subs({A_s: A_num, e_s: -e_num, x: x2}))
    degeneracy_gap = abs(V1 - V2)

    # orientation displacement between vac and CP image = 2*delta
    displacement = abs(x1 - (math.pi - x2))  # should be ~0 (mirror pair)
    two_delta    = abs(2.0 * (math.pi / 2 - x1))

    # pointwise path difference -2*eps*sin(2x)
    path_diff = simplify(Vx - Vx.subs(x, pi - x))
    path_ok   = simplify(path_diff + 2 * e_s * sin(2 * x)) == 0

    rw.print("  Reflection: V(pi - x; eps) - V(x; -eps) = {}  [{}]".format(
        resid1, "VERIFIED" if refl_ok else "FAIL"))
    rw.print("  Numeric minima (A=1, eps=1e-2):")
    rw.print("    V_min(+eps) = {:.12f}".format(V1))
    rw.print("    V_min(-eps) = {:.12f}".format(V2))
    rw.print("    |gap| = {:.3e}  -> EXACTLY DEGENERATE  [Eq 125.3]".format(
        degeneracy_gap))
    rw.print("    mirror check |x1 - (pi - x2)| = {:.3e}".format(displacement))
    rw.print("  Orientation: CP image displaced by 2*delta = {:.4e} rad".format(
        two_delta))
    rw.print("  Path difference: V(x) - V(pi-x) = -2*eps*sin(2x)  [{}]".format(
        "VERIFIED" if path_ok else "FAIL"))
    rw.print("")
    rw.print("  CORRECTION TO PART 85: Sakharov condition 2 is NOT an energy")
    rw.print("  splitting of the vacua (they are exactly degenerate). It is")
    rw.print("  the CP-odd term entering the TRANSITION RATES (O(eps) path")
    rw.print("  asymmetry, Eq 125.4) + non-CP-invariant vacuum orientation.")
    rw.print("  Baryogenesis weight shifts to condition 3 (non-equilibrium).")

    return {'reflection_ok': refl_ok, 'degeneracy_gap': degeneracy_gap,
            'mirror_displacement': displacement, 'two_delta': two_delta,
            'path_diff_ok': path_ok}


# ===========================================================================
# S5: BARYON ASYMMETRY -- PARAMETRIC BAND
# ===========================================================================

def compute_eta_band(rw):
    """
    Rate-asymmetry chain [Kolb & Turner 1990 structure, as Part 85 Eq 85.10]:
      eta ~ (1/g_*) * s * (DGamma/Gamma),   DGamma/Gamma ~ 2*eps/g
    with g_* = relativistic DOF at the transition, s = transition strength.
    Required eps/g = eta_obs * g_* / (2*s) over a reasonable (g_*, s) grid.
    Sign: eta flips with eps (Eq 125.4 is odd in eps); PDTP does not
    predict the sign -- 'matter' labels the abundant species. [DERIVED]
    """
    rw.section("S5: BARYON ASYMMETRY -- REQUIRED eps/g BAND")

    gstar_grid = [10.75, 100.0, 200.0]
    s_grid     = [0.01, 0.1, 0.3]

    vals = {}
    rw.print("  required eps/g = eta_obs * g_* / (2*s),  eta_obs = {:.2e}".format(
        ETA_OBS))
    rw.print("")
    rw.print("  {:>8s} | {:>7s} | {:>12s}".format("g_*", "s", "eps/g req."))
    rw.print("  " + "-" * 34)
    for gs in gstar_grid:
        for s in s_grid:
            v = ETA_OBS * gs / (2.0 * s)
            vals[(gs, s)] = v
            rw.print("  {:>8.2f} | {:>7.2f} | {:>12.3e}".format(gs, s, v))

    central  = vals[(100.0, 0.1)]
    band_min = min(vals.values())
    band_max = max(vals.values())
    part85   = 3.05e-7                     # Eq 85.11 reference value
    central_vs_85 = central / part85

    # plausibility anchors
    within_anchors = (THETA_MAX < band_min) and (band_max < JARLSKOG)

    rw.print("")
    rw.print("  Central (g_*=100, s=0.1): eps/g = {:.3e}".format(central))
    rw.print("    vs Part 85 Eq 85.11 (3.05e-7): ratio = {:.4f}".format(
        central_vs_85))
    rw.print("  Band: [{:.2e}, {:.2e}]  (spans {:.1f} decades)".format(
        band_min, band_max, math.log10(band_max / band_min)))
    rw.print("  Anchors: theta_QCD < {:.0e}  <  band  <  Jarlskog J = {:.2e}: {}".format(
        THETA_MAX, JARLSKOG, within_anchors))
    rw.print("    -> the required CP parameter sits BETWEEN the two known CP")
    rw.print("       scales of nature: physically reasonable magnitude.")
    rw.print("  Sign: sign(eta) = sign(eps) [Eq 125.4 odd in eps]; not predicted.")
    rw.print("")
    rw.print("  HONESTY: g_* and s are NOT computed from PDTP (conditions 1")
    rw.print("  and 3 rates still open) -- this is a parametric requirement,")
    rw.print("  not a first-principles prediction of eta. [ESTIMATED]")

    return {'central': central, 'central_vs_85': central_vs_85,
            'band_min': band_min, 'band_max': band_max,
            'within_anchors': within_anchors,
            'band_decades': math.log10(band_max / band_min)}


# ===========================================================================
# S6: STRONG CP -- CONDENSATE RELAXATION OF THETA
# ===========================================================================

def derive_strong_cp_relaxation(rw):
    """
    Why is theta_QCD ~ 0? PDTP mechanism (Part 85 candidate 3, made concrete):
    In PDTP, theta is not a fixed coupling -- it is the ORIENTATION of the
    dynamical condensate field U(x). The theta-vacuum energy is
      E(theta) = K*(1 - cos(theta))                             (125.5)
    [dilute instanton gas: Callan-Dashen-Gross 1976; and Vafa-Witten 1984
    guarantees E(theta) >= E(0) in any vector-like theory].
    A dynamical orientation relaxes to the minimum: theta -> 0.
    This is the Peccei-Quinn mechanism with the CONDENSATE PHASE playing
    the axion role -- no new field added.
    [DERIVED given the dynamical-theta premise; the premise itself is
     SPECULATIVE until the SU(3) condensate EOM for the orientation is
     solved explicitly.]

    U(1) limit cross-check: theta is exactly removable by a field shift
    (same phasor algebra as L4) -- matches L4 FAKE verdict.

    Residual theta from L5 cross-feed: with eps/g ~ 3e-7 in the
    gravitational surface sector and theta < 1e-10 in QCD, any cross-feed
    must be suppressed by < 1e-10/(3e-7) ~ 3e-4. PDTP's separate
    condensates (no direct coupling term in the Lagrangian) make this
    natural but unproven. [COMPUTED requirement; mechanism SPECULATIVE]
    """
    rw.section("S6: STRONG CP -- THETA RELAXES TO 0  [Eq 125.5]")

    E_th = K_s * (1 - cos(th_s))
    dE   = diff(E_th, th_s)
    d2E  = diff(E_th, th_s, 2)
    min_at_zero  = simplify(dE.subs(th_s, 0)) == 0
    curv_at_zero = simplify(d2E.subs(th_s, 0) - K_s) == 0   # E'' = K > 0
    E_nonneg     = simplify(E_th.subs(th_s, 0)) == 0

    # U(1) limit: g*cos(x + theta) = g*cos(x') with x' = x + theta (shift)
    u1_resid = simplify(g_s * cos(x + th_s)
                        - g_s * cos(x + th_s))              # trivial identity
    # the substantive check: the shifted Lagrangian has identical extrema
    u1_removable = simplify(
        diff(g_s * cos(x + th_s), x).subs(x, -th_s)) == 0   # min at x=-theta

    # cross-feed suppression requirement
    suppression_req = THETA_MAX / 3.05e-7

    rw.print("  E(theta) = K*(1 - cos(theta))  [instanton gas; Vafa-Witten]")
    rw.print("    dE/dtheta|_0 = 0: {};  d2E/dtheta^2|_0 = K > 0: {}".format(
        min_at_zero, curv_at_zero))
    rw.print("    E(0) = 0 (global minimum, E >= 0): {}".format(E_nonneg))
    rw.print("  -> dynamical orientation relaxes theta -> 0 [DERIVED given")
    rw.print("     premise]; condensate phase = axion role (PQ without axion).")
    rw.print("  U(1) limit: minimum shifts to x = -theta (theta absorbed): {}".format(
        u1_removable))
    rw.print("  Cross-feed requirement: theta_induced/(eps/g) < {:.1e}".format(
        suppression_req))
    rw.print("    [COMPUTED requirement; separate-condensate suppression is")
    rw.print("     SPECULATIVE -- open question 125-O1]")

    return {'min_at_zero': min_at_zero, 'curv_positive': curv_at_zero,
            'E_zero_is_zero': E_nonneg, 'u1_removable': u1_removable,
            'suppression_req': suppression_req}


# ===========================================================================
# S7: TWO-PHASE COMPATIBILITY -- EXACT IN THE psi/phi_+ SECTOR
# ===========================================================================

def verify_two_phase_exact(rw):
    """
    The eps term depends ONLY on phi_-:
      L_eps = eps*sin(phi_b - phi_s) = eps*sin(2*phi_-)
    Functional derivatives:
      dL_eps/dpsi    = 0   EXACTLY
      dL_eps/dphi_+  = 0   EXACTLY
      dL_eps/dphi_-  = 2*eps*cos(2*phi_-)   (new source, phi_- EOM only)
    => Newton's 3rd law (psi/phi_+ sector), Jeans eigenvalue (psi/phi_+),
       and biharmonic gravity (phi_+) are EXACTLY unchanged -- stronger
       than Part 85's O(eps^2) statement.                       (125.6)
    """
    rw.section("S7: TWO-PHASE COMPATIBILITY -- EXACT (psi/phi_+ SECTOR)")

    L_eps = e_s * sin(2 * phim_s)
    d_psi  = simplify(diff(L_eps, psi_s))
    d_phip = simplify(diff(L_eps, phip_s))
    d_phim = simplify(diff(L_eps, phim_s))

    psi_zero  = (d_psi == 0)
    phip_zero = (d_phip == 0)
    phim_src_ok = simplify(d_phim - 2 * e_s * cos(2 * phim_s)) == 0

    rw.print("  dL_eps/dpsi   = {}  (EXACTLY 0: {})".format(d_psi, psi_zero))
    rw.print("  dL_eps/dphi_+ = {}  (EXACTLY 0: {})".format(d_phip, phip_zero))
    rw.print("  dL_eps/dphi_- = {}  (= 2*eps*cos(2*phi_-): {})".format(
        d_phim, phim_src_ok))
    rw.print("")
    rw.print("  => psi and phi_+ EOMs are EXACTLY those of Part 61:")
    rw.print("     Newton's 3rd law psi_ddot = -2*phi_+_ddot   EXACT")
    rw.print("     Jeans eigenvalue +2*sqrt(2)*g               EXACT")
    rw.print("     Biharmonic nabla^4 + 4g^2 (phi_+ sector)    EXACT")
    rw.print("  Only the phi_- EOM gains the source 2*eps*cos(2*phi_-).")
    rw.print("  [Eq 125.6 -- upgrades Part 85's O(eps^2) statement]")

    return {'psi_exact': psi_zero, 'phip_exact': phip_zero,
            'phim_source_ok': phim_src_ok}


# ===========================================================================
# SUDOKU CONSISTENCY CHECKS (14 tests)
# ===========================================================================

def sudoku_checks(rw, s1, s2, s3, s4, s5, s6, s7):
    """
    14 checks; every 'got' is read from a step dict (RECHECK trace path).
    """
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

    chk("T1: cos CP-even + sin CP-odd [SymPy]",
        s1['cos_even'] and s1['sin_odd'], True, is_bool=True)
    chk("T2: two-phase g-term CP-EVEN (product of two flips)",
        s1['g_term_even'], True, is_bool=True)
    chk("T3: eps*sin(2*phi_-) CP-ODD",
        s1['eps_term_odd'], True, is_bool=True)
    chk("T4: L4 phasor identity residual = 0 [SymPy]",
        s2['l4_residual_zero'], True, is_bool=True)
    chk("T5: true-vacuum shift delta = 2*eps/A (leading) [SymPy]",
        s3['d_lead_is_2eps_over_A'], True, is_bool=True)
    chk("T6: numeric root matches 2*eps/A (A=1, eps=1e-3)",
        s3['d_root'], s3['d_pred'], tol=0.01)
    chk("T7: A=2g reading gives delta = eps/g (Part 85 magnitude)",
        s3['d_2g_is_eps_over_g'], True, is_bool=True)
    chk("T8: mass shift is O(eps^2): m2(2e)-A / m2(e)-A = 4",
        s3['quad_ratio'], 4.0, tol=0.02)
    chk("T9: reflection identity V(pi-x;eps) = V(x;-eps) [SymPy]",
        s4['reflection_ok'], True, is_bool=True)
    chk("T10: CP-conjugate vacua EXACTLY degenerate (numeric gap < 1e-12)",
        s4['degeneracy_gap'] < 1e-12, True, is_bool=True)
    chk("T11: path difference = -2*eps*sin(2x) [SymPy, Eq 125.4]",
        s4['path_diff_ok'], True, is_bool=True)
    chk("T12: central required eps/g matches Part 85 Eq 85.11",
        s5['central_vs_85'], 1.0, tol=0.01)
    chk("T13: E(theta) minimum at theta=0 with E''=K>0 [SymPy]",
        s6['min_at_zero'] and s6['curv_positive'], True, is_bool=True)
    chk("T14: psi & phi_+ EOMs EXACTLY unchanged [SymPy, Eq 125.6]",
        s7['psi_exact'] and s7['phip_exact'] and s7['phim_source_ok'],
        True, is_bool=True)

    rw.print("")
    rw.print("  SCORE: {}/{} PASS".format(passes, total))
    return {'passes': passes, 'total': total, 'all_pass': passes == total}


# ===========================================================================
# MAIN
# ===========================================================================

def main():
    out_dir = os.path.join(_HERE, "outputs")
    rw = ReportWriter(out_dir, label="cp_violation_quantitative")

    rw.section("B4 QUANTITATIVE REVISIT -- CP VIOLATION (Part 125, Phase 93)")
    rw.print("Date: 2026-07-07")
    rw.print("Extends Part 85 (Phase 55). Reason: Part 85 used the pre-Part-62")
    rw.print("vacuum phi_- = 0; true vacuum is pi/2 (Parts 62/119).")

    s1 = verify_cp_rules(rw)
    s2 = verify_l4_removable(rw)
    s3 = derive_true_vacuum_shift(rw)
    s4 = derive_cp_degeneracy(rw)
    s5 = compute_eta_band(rw)
    s6 = derive_strong_cp_relaxation(rw)
    s7 = verify_two_phase_exact(rw)
    score = sudoku_checks(rw, s1, s2, s3, s4, s5, s6, s7)

    rw.section("OVERALL VERDICT")
    rw.print("  [DERIVED]  True-vacuum shift: phi_-* = pi/2 - 2*eps/A;")
    rw.print("             with A = 2g: |delta| = eps/g (Part 85 value robust).")
    rw.print("  [DERIVED]  CORRECTION: CP-conjugate vacua EXACTLY degenerate")
    rw.print("             (reflection x -> pi - x). Sakharov condition 2 acts")
    rw.print("             through O(eps) RATE asymmetry (path difference")
    rw.print("             -2*eps*sin(2x)), not vacuum energetics.")
    rw.print("  [COMPUTED] Required eps/g: central 3.05e-7 (g_*=100, s=0.1);")
    rw.print("             band [{:.1e}, {:.1e}] between theta_QCD and".format(
        s5['band_min'], s5['band_max']))
    rw.print("             Jarlskog J -- physically reasonable magnitude.")
    rw.print("  [DERIVED given premise] Strong CP: dynamical condensate")
    rw.print("             orientation relaxes theta -> 0 (E = K(1-cos theta),")
    rw.print("             Vafa-Witten); PQ mechanism without adding an axion.")
    rw.print("  [DERIVED]  Two-phase psi/phi_+ sector EXACTLY unchanged.")
    rw.print("")
    rw.print("  STILL OPEN (B4): condition 1 rate (vortex nucleation),")
    rw.print("  condition 3 rate (transition strength s from PDTP), CKM phase,")
    rw.print("  cross-feed suppression proof (125-O1), dynamical-theta EOM.")
    rw.print("")
    rw.print("  SUDOKU: {}/{} PASS".format(score['passes'], score['total']))
    rw.print("  VERDICT: B4 upgraded PARTIAL -> LARGELY RESOLVED (mechanism +")
    rw.print("  magnitudes at true vacuum); eta remains parametric until the")
    rw.print("  two rate calculations are done.")

    rw.close()
    print("")
    print("Log saved to: " + rw.path)
    return score


if __name__ == "__main__":
    score = main()
    sys.exit(0 if score['all_pass'] else 1)
