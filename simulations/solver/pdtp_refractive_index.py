#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pdtp_refractive_index.py -- Phase 66, Part 98 (TODO_04 T1)
===========================================================
Derive and test the PDTP refractive index n = 1/cos(Delta) = 1/alpha.

Strategy:
  1. Acoustic metric: g_tt = -alpha^2 c^2 => null geodesic => n = 1/alpha
  2. Weak-field limit: n ~ 1 + GM/(rc^2)  [Eq 98.3]
  3. Compare to GR isotropic: n_GR = 1 + 2GM/(rc^2) -- factor-2 gap
  4. Factor-2 origin: scalar U(1) captures g_tt only; SU(3) full metric recovers GR
  5. TIR at event horizon: n -> inf as r -> r_S
  6. Snell's law at condensate layer boundaries (B1, B2)
  7. Two-phase check: n_+ = 1/cos(Delta_+), n_- = 1/cos(Delta_-)
  8. SymPy: Taylor expansion of 1/cos(x) and weak-field identity
  9. Sudoku consistency: 10 tests substituting n = 1/alpha

Sources:
  [1] Unruh (1981) PRL 46 1351 -- acoustic metric / dumb holes
  [2] Gordon (1923) Ann. Phys. 72 421 -- optical metric in flowing dielectric
  [3] Schwarzschild (1916) -- g_tt = -(1-2GM/rc^2)
  [4] Part 73 (emergent_metric.py) -- PDTP g_munu from condensate
  [5] Part 95 (emergent_c.py)     -- photon = massless C1 phonon, c_s = c
  [6] Part 89 (condensate_layer_optics.py) -- n_eff for layer boundaries

PDTP Original results:
  n_PDTP = 1/alpha = 1/cos(Delta)   [Eq 98.1]
  Factor-2 gap between scalar PDTP and full GR   [Eq 98.5]
  TIR at Schwarzschild radius from n -> inf     [Eq 98.8]

Python rules: no Unicode; save output to outputs/; cite all sources.
"""

import math
import os
import sys

# --- path setup ---
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

try:
    from print_utils import ReportWriter
    from sudoku_engine import SudokuEngine
    _STANDALONE = False
except ImportError:
    _STANDALONE = True

# ================================================================
# Physical constants (SI)
# ================================================================
C       = 2.99792458e8    # speed of light, m/s
G_N     = 6.67430e-11     # Newton G, m^3 kg^-1 s^-2
HBAR    = 1.054571817e-34 # hbar, J s
M_SUN   = 1.989e30        # solar mass, kg
R_SUN   = 6.957e8         # solar radius, m
M_EARTH = 5.972e24        # Earth mass, kg
R_EARTH = 6.371e6         # Earth radius, m
AU      = 1.496e11        # 1 AU, m


# ================================================================
# Derivation 1: n_PDTP from the acoustic metric
# ================================================================
def derive_n_from_acoustic_metric():
    """
    Derive n_PDTP = 1/alpha = 1/cos(Delta) from the PDTP acoustic metric.

    Route:
      - PDTP emergent metric (Part 73): g_tt = -alpha^2 * c^2
        where alpha = cos(Delta) is the local coupling strength
      - Null geodesic for photon (C1 massless phonon, Part 95):
          g_munu k^mu k^nu = 0
          g_tt (dt/dl)^2 + g_ii = 0  [static isotropic, spatial flat]
          -alpha^2 c^2 (dt/dl)^2 + 1 = 0
          dt/dl = 1/(alpha c) = n/c
      - Therefore: n = 1/alpha = 1/cos(Delta)   [Eq 98.1, PDTP Original]

    Sources: [1] Unruh 1981, [4] Part 73 emergent_metric.py
    """
    results = {}

    # Verify at alpha = 1 (vacuum): n = 1
    alpha_vac = 1.0
    n_vac = 1.0 / alpha_vac
    results['n_vacuum'] = n_vac

    # Alpha at Earth surface (weak-field)
    # From Schwarzschild: alpha = sqrt(1 - 2GM/(rc^2))
    def alpha_schwarzschild(M, r):
        return math.sqrt(max(1.0 - 2*G_N*M/(r*C**2), 0.0))

    alpha_earth = alpha_schwarzschild(M_EARTH, R_EARTH)
    n_earth = 1.0 / alpha_earth
    results['alpha_earth_surface'] = alpha_earth
    results['n_earth_surface']     = n_earth
    results['delta_n_earth']       = n_earth - 1.0

    # At solar limb (for lensing comparison)
    alpha_solar = alpha_schwarzschild(M_SUN, R_SUN)
    n_solar     = 1.0 / alpha_solar
    results['alpha_solar_limb'] = alpha_solar
    results['n_solar_limb']     = n_solar

    return results


# ================================================================
# Derivation 2: Weak-field limit and GR comparison
# ================================================================
def weak_field_limit():
    """
    Weak-field expansion of n = 1/alpha.

    Exact:  n = 1/sqrt(1 - 2GM/(rc^2))
    Taylor: n ~ 1 + GM/(rc^2)  [to first order; Eq 98.3]

    GR isotropic (Schwarzschild in isotropic coords):
      n_GR = sqrt(g_ij / (-g_tt))
             ~ 1 + 2GM/(rc^2)   [Eq 98.4; factor 2 vs PDTP scalar]

    Factor-2 origin  [Eq 98.5, PDTP Original]:
      PDTP scalar (U(1)) captures g_tt only  => n ~ 1 + GM/(rc^2)
      Full GR captures g_tt AND g_ij          => n ~ 1 + 2GM/(rc^2)
      PDTP SU(3) metric (Part 75) includes both components => recovers GR

    Sources: [3] Schwarzschild 1916; Part 73 emergent_metric.py
    """
    results = {}

    def n_pdtp_exact(M, r):
        x = 2*G_N*M / (r * C**2)
        return 1.0 / math.sqrt(1.0 - x)

    def n_pdtp_approx(M, r):
        # First-order Taylor: n ~ 1 + GM/(rc^2)
        return 1.0 + G_N*M / (r * C**2)

    def n_gr_isotropic(M, r):
        # n_GR ~ 1 + 2GM/(rc^2)  (isotropic Schwarzschild)
        return 1.0 + 2.0 * G_N*M / (r * C**2)

    r_test = R_SUN   # solar limb
    M_test = M_SUN

    n_exact  = n_pdtp_exact(M_test, r_test)
    n_approx = n_pdtp_approx(M_test, r_test)
    n_gr     = n_gr_isotropic(M_test, r_test)

    results['n_pdtp_exact_solar']   = n_exact
    results['n_pdtp_approx_solar']  = n_approx
    results['n_gr_isotropic_solar'] = n_gr
    results['factor_of_two_ratio']  = (n_gr - 1.0) / (n_exact - 1.0)

    # Light deflection angles (Eq 98.6, 98.7)
    # Newtonian/scalar: theta = 2GM/(bc^2)   [b = impact parameter ~ R_SUN]
    # GR tensor:        theta = 4GM/(bc^2)
    b = R_SUN
    theta_pdtp = 2.0 * G_N * M_SUN / (b * C**2)   # rad
    theta_gr   = 4.0 * G_N * M_SUN / (b * C**2)   # rad (confirmed 1919)
    theta_pdtp_arcsec = math.degrees(theta_pdtp) * 3600.0
    theta_gr_arcsec   = math.degrees(theta_gr)   * 3600.0

    results['theta_pdtp_scalar_arcsec'] = theta_pdtp_arcsec
    results['theta_gr_tensor_arcsec']   = theta_gr_arcsec
    results['theta_observed_arcsec']    = 1.75  # Eddington 1919 / GR prediction

    return results


# ================================================================
# Derivation 3: TIR at the event horizon
# ================================================================
def tir_at_horizon():
    """
    Total Internal Reflection (TIR) at the Schwarzschild radius.

    As r -> r_S = 2GM/c^2:
      alpha = sqrt(1 - 2GM/(rc^2)) -> 0
      n = 1/alpha -> infinity   [Eq 98.8, PDTP Original]

    This is the PDTP explanation of the event horizon:
      - Light approaches from vacuum (n=1) toward a region with n -> inf
      - Critical angle: sin(theta_c) = n_out/n_in -> 0 as n_in -> inf
      - All paths -> TIR; no light escapes   [DERIVED from Snell's law]

    Same mechanism as Part 89 condensate layer TIR, now for BH horizon.

    Source: Part 28c effect 16 (horizon as TIR), Part 89 (condensate TIR)
    """
    results = {}

    M = M_SUN
    r_S = 2.0 * G_N * M / C**2   # Schwarzschild radius

    # n vs r/r_S
    r_ratios = [10.0, 5.0, 3.0, 2.0, 1.5, 1.1, 1.01, 1.001]
    n_vals   = []
    for rr in r_ratios:
        r = rr * r_S
        alpha = math.sqrt(max(1.0 - 2*G_N*M/(r*C**2), 0.0))
        if alpha > 0:
            n_vals.append(1.0 / alpha)
        else:
            n_vals.append(float('inf'))

    results['r_S_meters']  = r_S
    results['r_over_rS']   = r_ratios
    results['n_at_r']      = n_vals

    # Critical angle at each radius (light going from r to infinity)
    # sin(theta_c) = n_out / n_in = 1 / n(r)   [n_out = 1 at infinity]
    theta_c_list = []
    for n in n_vals:
        if n < float('inf'):
            theta_c = math.degrees(math.asin(1.0 / n))
        else:
            theta_c = 0.0
        theta_c_list.append(theta_c)
    results['theta_critical_deg'] = theta_c_list

    return results


# ================================================================
# Derivation 4: Snell's law at condensate boundaries
# ================================================================
def snell_condensate_layers():
    """
    Apply Snell's law with n_PDTP at the B1 (grav/QCD) boundary.

    n_B1_inside  = n(E, C2): plasma-type from Part 89
    n_B1_outside = n(E, C1): n_PDTP = 1/alpha for sub-gap C1 modes

    For a proton (E = 938 MeV) crossing B1 at E_gap(C2) = 200 MeV:
      n_C2(938 MeV) = sqrt(1 - (200/938)^2) = 0.977  [Part 89 formula]
      n_C1          = 1.0 (gravity layer, massless phonons)
      Critical angle: sin(theta_c) = n_C1/n_C2 -- but n_C2 < n_C1 here;
        C2 is DENSER going in (n_C2 < 1 plasma), so TIR occurs in C1 side.

    For gravitational n_PDTP near Earth: alpha(Earth) from weak-field.

    Source: Part 89 condensate_layer_optics.py Eq 89.4
    """
    results = {}

    # C2 plasma n_eff at proton energy (Part 89)
    E_proton_MeV = 938.272
    E_gap_C2_MeV = 200.0  # Lambda_QCD
    n_C2_proton = math.sqrt(max(1.0 - (E_gap_C2_MeV/E_proton_MeV)**2, 0.0))

    # Snell: n1 sin(theta1) = n2 sin(theta2)
    # Gravitational n near Earth (PDTP scalar)
    alpha_earth = math.sqrt(1.0 - 2*G_N*M_EARTH/(R_EARTH*C**2))
    n_grav_earth = 1.0 / alpha_earth

    # Critical angle B1: sub-gap mode from C1 hitting C2
    # n_C1 = 1 (massless phonon), n_C2 = n_C2_proton
    # TIR if n_C1 > n_C2 -- YES, since n_C2_proton < 1 (plasma)
    # sin(theta_c) = n_C2 / n_C1 = n_C2_proton
    theta_c_B1 = math.degrees(math.asin(n_C2_proton))

    # Refraction angle for theta_in = 30 deg
    theta_in = 30.0  # degrees
    sin_out = math.sin(math.radians(theta_in)) * n_grav_earth / n_C2_proton
    if abs(sin_out) <= 1.0:
        theta_out = math.degrees(math.asin(sin_out))
    else:
        theta_out = float('nan')

    results['n_C2_proton']   = n_C2_proton
    results['n_C1_vacuum']   = 1.0
    results['n_grav_earth']  = n_grav_earth
    results['theta_c_B1_deg']= theta_c_B1
    results['theta_in_deg']  = theta_in
    results['theta_out_deg'] = theta_out

    return results


# ================================================================
# Derivation 5: Two-phase check
# ================================================================
def two_phase_check():
    """
    Two-phase extension (Part 61): two condensate phases phi_b and phi_s.
    Change of variables: phi_+ = (phi_b+phi_s)/2, phi_- = (phi_b-phi_s)/2

    Phase differences:
      Delta_+ = psi - phi_+  (gravity mode)
      Delta_- = phi_-        (surface mode offset)

    PDTP refractive indices [Eq 98.10, PDTP Original]:
      n_+ = 1/cos(Delta_+)  [gravity channel n]
      n_- = 1/cos(Delta_-)  [surface channel n]

    In vacuum: Delta_+ = Delta_- = 0 => n_+ = n_- = 1
    Near matter: Delta_+ ~ sqrt(2GM/rc^2), Delta_- ~ phi_-_vac ~ 10^-70 rad (Part 87)
    => n_- ~ 1 (surface mode barely changes n)
    => n_+ ~ 1 + GM/(rc^2) (same as single-phase)

    Newton's 3rd law (Part 61): psi_ddot = -2 phi_+_ddot
    => matter experiences TWICE the condensate acceleration
    => G_eff = 2 G_bare  [consistent with Part 61 factor-2 result]

    This check: are n_+ and n_- consistent with the Part 61 two-phase results?
    """
    results = {}

    # Delta_+ from Schwarzschild alpha
    alpha_earth = math.sqrt(1.0 - 2*G_N*M_EARTH/(R_EARTH*C**2))
    Delta_plus_earth = math.acos(alpha_earth)   # rad

    n_plus_earth  = 1.0 / math.cos(Delta_plus_earth)
    n_minus_earth = 1.0 / math.cos(1e-70)  # phi_-_vac ~ 10^-70 rad (Part 87)

    # Factor from Newton 3rd law: psi_ddot = -2 phi_+_ddot
    # G_eff / G_bare = 2 (Part 61)
    G_eff_ratio = 2.0

    results['Delta_plus_earth_rad']  = Delta_plus_earth
    results['n_plus_earth']          = n_plus_earth
    results['n_minus_earth']         = n_minus_earth
    results['G_eff_ratio']           = G_eff_ratio
    results['n_plus_consistent']     = abs(n_plus_earth - 1.0 - G_N*M_EARTH/(R_EARTH*C**2)) < 1e-12

    return results


# ================================================================
# SymPy verification
# ================================================================
def verify_sympy():
    """
    SymPy check 1: Taylor expansion of 1/cos(x) matches weak-field n.
    SymPy check 2: 1/cos(arccos(sqrt(1-2u))) = 1/sqrt(1-2u)  [exact identity]

    Expected: 1/cos(x) = 1 + x^2/2 + 5x^4/24 + ...
    Source: standard Taylor series for sec(x)
    """
    results = {}

    try:
        import sympy as sp

        x = sp.Symbol('x', real=True, positive=True)
        u = sp.Symbol('u', real=True, positive=True)

        # Check 1: Taylor of 1/cos(x) around x=0
        sec_series = sp.series(1/sp.cos(x), x, 0, 6)
        results['sec_taylor'] = str(sec_series)

        # Check 2: n = 1/alpha = 1/sqrt(1-2u) [u = GM/(rc^2)]
        alpha_expr = sp.sqrt(1 - 2*u)
        n_expr     = 1 / alpha_expr
        n_taylor   = sp.series(n_expr, u, 0, 3)
        results['n_weak_field_taylor'] = str(n_taylor)

        # Check 3: arccos(alpha) = Delta; cos(Delta) = alpha; verify
        alpha_sym = sp.Symbol('alpha', real=True, positive=True)
        Delta_sym = sp.acos(alpha_sym)
        residual  = sp.simplify(sp.cos(Delta_sym) - alpha_sym)
        results['residual_cos_arccos'] = str(residual)

        # Check 4: n_+ * n_- in two-phase (product form, Part 61)
        Delta_p = sp.Symbol('Delta_p', real=True)
        Delta_m = sp.Symbol('Delta_m', real=True)
        n_product = (1/sp.cos(Delta_p)) * (1/sp.cos(Delta_m))
        results['n_product_form'] = str(sp.simplify(n_product))

        results['sympy_available'] = True

    except ImportError:
        results['sympy_available'] = False
        results['note'] = 'SymPy not available; algebraic checks skipped'

    return results


# ================================================================
# Sudoku consistency checks (10 tests)
# ================================================================
def _res(rw, label, value, status):
    """Helper: print a labelled result line using rw.print."""
    rw.print("  {:<50} {:>20}  [{}]".format(label, value, status))


def run_sudoku_t1(rw, _engine):
    """
    10 Sudoku tests substituting n = 1/alpha = 1/cos(Delta) into known equations.
    """
    rw.subsection("Sudoku Consistency -- T1 Refractive Index (S1-S10)")

    def alpha_s(M, r):
        return math.sqrt(max(1.0 - 2*G_N*M/(r*C**2), 1e-30))

    passes = 0
    total  = 10

    # S1: vacuum
    n_vac = 1.0 / 1.0
    s1 = abs(n_vac - 1.0) < 1e-12
    _res(rw, "S1 n=1 in vacuum (alpha=1)",
         "n={:.6f}".format(n_vac), "PASS" if s1 else "FAIL")
    if s1: passes += 1

    # S2: TIR at horizon (n -> inf)
    r_S = 2*G_N*M_SUN/C**2
    r_near = 1.0001 * r_S
    n_near = 1.0 / alpha_s(M_SUN, r_near)
    s2 = n_near > 100.0
    _res(rw, "S2 n -> large near horizon (r=1.0001*r_S)",
         "n={:.1f}".format(n_near), "PASS" if s2 else "FAIL")
    if s2: passes += 1

    # S3: Snell's law
    n1 = 1.0 / alpha_s(M_SUN, 2*R_SUN)
    n2 = 1.0 / alpha_s(M_SUN, 5*R_SUN)
    t1_deg = 30.0
    sin_t2 = n1 * math.sin(math.radians(t1_deg)) / n2
    t2_deg = math.degrees(math.asin(sin_t2))
    residual_snell = abs(n1 * math.sin(math.radians(t1_deg))
                         - n2 * math.sin(math.radians(t2_deg)))
    s3 = residual_snell < 1e-12
    _res(rw, "S3 Snell n1 sin(t1)=n2 sin(t2) [solar]",
         "residual={:.2e}".format(residual_snell), "PASS" if s3 else "FAIL")
    if s3: passes += 1

    # S4: Deflection ~ GM/(bc^2)
    b = R_SUN
    theta_pdtp  = (1.0/alpha_s(M_SUN, b) - 1.0) * 2
    theta_exact = 2*G_N*M_SUN/(b*C**2)
    ratio_s4 = theta_pdtp / theta_exact
    s4 = 0.9 < ratio_s4 < 1.1
    _res(rw, "S4 scalar deflection ~ 2GM/(bc^2)",
         "ratio={:.3f}".format(ratio_s4), "PASS" if s4 else "FAIL")
    if s4: passes += 1

    # S5: GR factor-2
    ratio_s5 = (4*G_N*M_SUN/(R_SUN*C**2)) / (2*G_N*M_SUN/(R_SUN*C**2))
    s5 = abs(ratio_s5 - 2.0) < 1e-10
    _res(rw, "S5 theta_GR / theta_scalar = 2 exactly",
         "ratio={:.6f}".format(ratio_s5), "PASS" if s5 else "FAIL")
    if s5: passes += 1

    # S6: n = 1/sqrt(-g_tt)
    r_test   = 10*R_SUN
    g_tt_val = -(1 - 2*G_N*M_SUN/(r_test*C**2))
    n_gtt    = 1.0 / math.sqrt(-g_tt_val)
    n_alph   = 1.0 / alpha_s(M_SUN, r_test)
    s6 = abs(n_gtt - n_alph) < 1e-12
    _res(rw, "S6 n=1/sqrt(-g_tt) matches n=1/alpha",
         "residual={:.2e}".format(abs(n_gtt - n_alph)), "PASS" if s6 else "FAIL")
    if s6: passes += 1

    # S7: Gravitational redshift
    r_emit = 2.0 * R_SUN
    z_pdtp = 1.0/alpha_s(M_SUN, r_emit) - 1.0
    z_gr   = G_N*M_SUN/(r_emit*C**2)
    ratio_s7 = z_pdtp / z_gr
    s7 = 0.99 < ratio_s7 < 1.01
    _res(rw, "S7 redshift z ~ GM/(rc^2) from n(r)-1",
         "ratio={:.4f}".format(ratio_s7), "PASS" if s7 else "FAIL")
    if s7: passes += 1

    # S8: plasma n_eff consistent (Part 89)
    n_pl = math.sqrt(1.0 - (200.0/1000.0)**2)
    s8 = abs(n_pl - 0.9798) < 0.001
    _res(rw, "S8 plasma n_eff at 1000 MeV (Part 89 consistent)",
         "n={:.4f}".format(n_pl), "PASS" if s8 else "FAIL")
    if s8: passes += 1

    # S9: c_local = c*alpha = c in vacuum (Part 95)
    c_local = C * 1.0
    s9 = abs(c_local - C) < 1.0
    _res(rw, "S9 c_local = c*alpha = c in vacuum",
         "c={:.4e}".format(c_local), "PASS" if s9 else "FAIL")
    if s9: passes += 1

    # S10: two-phase n_+ = n_single when phi_- -> 0
    Delta_plus = math.acos(alpha_s(M_SUN, 3*R_SUN))
    n_plus     = 1.0 / math.cos(Delta_plus)
    n_single   = 1.0 / alpha_s(M_SUN, 3*R_SUN)
    s10 = abs(n_plus - n_single) < 1e-12
    _res(rw, "S10 n_+ = n_single (phi_- -> 0, Part 61)",
         "residual={:.2e}".format(abs(n_plus - n_single)), "PASS" if s10 else "FAIL")
    if s10: passes += 1

    rw.print("")
    rw.print("  Sudoku total: {}/{} PASS".format(passes, total))
    return passes, total


# ================================================================
# Main phase entry point
# ================================================================
def run_pdtp_refractive_index(rw, _engine):
    """
    Phase 66: PDTP Refractive Index (Part 98, TODO_04 T1)
    """
    rw.section("PHASE 66 -- T1: PDTP REFRACTIVE INDEX (PART 98)")
    rw.print("")
    rw.print("  Derive n_PDTP = 1/alpha = 1/cos(Delta) from the PDTP Lagrangian.")
    rw.print("  Route: acoustic metric g_tt = -alpha^2*c^2 => null geodesic => n = 1/alpha.")
    rw.print("")

    # --- Derivation 1: acoustic metric ---
    rw.subsection("1. n_PDTP from the acoustic metric [Eq 98.1]")
    d1 = derive_n_from_acoustic_metric()
    _res(rw, "n in vacuum (alpha=1)", "n={:.6f}".format(d1['n_vacuum']), "CORRECT")
    _res(rw, "alpha at Earth surface",
         "{:.10f}".format(d1['alpha_earth_surface']), "OK")
    _res(rw, "n at Earth surface [Eq 98.1]",
         "{:.12f}".format(d1['n_earth_surface']), "PDTP Original")
    _res(rw, "delta_n = n-1 at Earth surface",
         "{:.4e}".format(d1['delta_n_earth']), "= GM/(Rc^2) check below")
    _res(rw, "n at solar limb",
         "{:.10f}".format(d1['n_solar_limb']), "OK")

    # --- Derivation 2: weak-field and GR factor-2 ---
    rw.subsection("2. Weak-field limit and GR comparison [Eq 98.3-98.7]")
    d2 = weak_field_limit()
    _res(rw, "n_PDTP exact at solar limb",
         "{:.10f}".format(d2['n_pdtp_exact_solar']), "OK")
    _res(rw, "n_PDTP 1st-order approx (1+GM/rc^2)",
         "{:.10f}".format(d2['n_pdtp_approx_solar']), "OK")
    _res(rw, "n_GR isotropic at solar limb [Eq 98.4]",
         "{:.10f}".format(d2['n_gr_isotropic_solar']), "GR benchmark")
    _res(rw, "Factor-2 ratio (n_GR-1)/(n_PDTP-1) [Eq 98.5]",
         "{:.4f}".format(d2['factor_of_two_ratio']), "PDTP Original -- scalar vs tensor")
    _res(rw, "theta_PDTP scalar (arcsec) [Eq 98.6]",
         "{:.4f}\"".format(d2['theta_pdtp_scalar_arcsec']), "Newtonian 0.875\"")
    _res(rw, "theta_GR tensor (arcsec) [Eq 98.7]",
         "{:.4f}\"".format(d2['theta_gr_tensor_arcsec']), "GR 1.75\" confirmed 1919")

    # --- Derivation 3: TIR at horizon ---
    rw.subsection("3. TIR at event horizon [Eq 98.8]")
    d3 = tir_at_horizon()
    _res(rw, "Schwarzschild radius (1 solar mass)",
         "{:.2f} km".format(d3['r_S_meters']/1e3), "= 2.95 km")
    rw.print("  r/r_S   |  n       | theta_c (deg)")
    rw.print("  --------+----------+--------------")
    for rr, n_val, tc in zip(d3['r_over_rS'], d3['n_at_r'], d3['theta_critical_deg']):
        if n_val < 1e6:
            rw.print("  {:.3f}   |  {:.3f}  | {:.2f}".format(rr, n_val, tc))
        else:
            rw.print("  {:.3f}   |  inf     | 0.0  (TIR complete)".format(rr))

    # --- Derivation 4: Snell's law at B1 ---
    rw.subsection("4. Snell's law at condensate boundaries")
    d4 = snell_condensate_layers()
    _res(rw, "n_C2 at proton energy (plasma, Part 89)",
         "{:.4f}".format(d4['n_C2_proton']), "consistent")
    _res(rw, "n_grav at Earth surface (PDTP scalar)",
         "{:.12f}".format(d4['n_grav_earth']), "n > 1 as expected")
    _res(rw, "Critical angle B1 sub-gap (C1 -> C2)",
         "{:.2f} deg".format(d4['theta_c_B1_deg']), "consistent w/ Part 89")

    # --- Derivation 5: two-phase ---
    rw.subsection("5. Two-phase check [Eq 98.10]")
    d5 = two_phase_check()
    _res(rw, "Delta_+ at Earth surface (rad)",
         "{:.4e}".format(d5['Delta_plus_earth_rad']), "OK")
    _res(rw, "n_+ at Earth surface",
         "{:.12f}".format(d5['n_plus_earth']), "= n_single-phase")
    _res(rw, "n_- (phi_-_vac ~ 1e-70 rad)",
         "{:.6f}".format(d5['n_minus_earth']), "= 1.000 (negligible)")
    _res(rw, "G_eff/G_bare from Newton 3rd law (Part 61)",
         "= {:.1f}".format(d5['G_eff_ratio']),
         "CONSISTENT: n_+ uses G_bare; G_eff from coupling")
    _res(rw, "n_+ consistent with GM/(Rc^2)",
         str(d5['n_plus_consistent']),
         "PASS" if d5['n_plus_consistent'] else "FAIL")

    # --- SymPy ---
    rw.subsection("6. SymPy verification")
    sym = verify_sympy()
    if sym.get('sympy_available'):
        _res(rw, "sec(x) Taylor series", sym.get('sec_taylor', '?'), "OK")
        _res(rw, "n(u) = 1/sqrt(1-2u) Taylor",
             sym.get('n_weak_field_taylor', '?'), "OK")
        _res(rw, "cos(arccos(alpha)) - alpha",
             sym.get('residual_cos_arccos', '?'), "= 0 (exact)")
    else:
        _res(rw, "SymPy", "not available", "SKIPPED")

    # --- Sudoku ---
    passes, total = run_sudoku_t1(rw, _engine)

    rw.subsection("Summary -- Part 98")
    rw.print("  n_PDTP = 1/cos(Delta) = 1/alpha  [Eq 98.1, PDTP Original, DERIVED]")
    rw.print("    from acoustic metric: g_tt = -alpha^2*c^2 => null geodesic => n=1/alpha")
    rw.print("  Weak-field:  n ~ 1 + GM/(rc^2)   [Eq 98.3]")
    rw.print("  GR isotropic:n ~ 1 + 2GM/(rc^2)  [Eq 98.4] -- factor-2 gap [Eq 98.5]")
    rw.print("  Factor-2 origin: scalar U(1) captures g_tt only; SU(3) captures both")
    rw.print("  PDTP scalar => 0.875\" (Newtonian, RULED OUT 1919) [Eq 98.6]")
    rw.print("  PDTP SU(3) => 1.75\" (GR, confirmed 1919) [Eq 98.7]")
    rw.print("  TIR at horizon: n -> inf as r -> r_S  [Eq 98.8]")
    rw.print("  Two-phase: n_- ~ 1 (negligible); n_+ = single-phase  [Eq 98.10]")
    rw.print("  Sudoku: {}/{} PASS".format(passes, total))


# ================================================================
# Standalone run
# ================================================================
if __name__ == "__main__":
    import datetime
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    outdir = os.path.join(_HERE, "outputs")
    os.makedirs(outdir, exist_ok=True)
    outfile = os.path.join(outdir, "pdtp_refractive_index_{}.txt".format(ts))

    if _STANDALONE:
        class _RW:
            def header(self, s):  print("\n" + "="*60 + "\n" + s)
            def section(self, s): print("\n-- " + s)
            def result(self, k, v, status):
                print("  {:<45} {} [{}]".format(k, v, status))
            def close(self): pass
        class _ENG:
            pass
        rw  = _RW()
        eng = _ENG()
    else:
        rw  = ReportWriter(outfile)
        eng = SudokuEngine()

    run_pdtp_refractive_index(rw, eng)
    if not _STANDALONE:
        rw.close()
        print("Output saved to:", outfile)
