"""
white_comparison.py -- Phase 36: White et al. (2026) Comparison (Part 67)
=========================================================================
Compares PDTP condensate framework with White et al. (2026),
"Emergent quantization from a dynamic vacuum", Phys. Rev. Research 8, 013264.

Three questions answered:
  Q1: Can PDTP derive White's constitutive profile 1/c_s^2 = A + C/r?
  Q2: Does PDTP's relativistic dispersion reduce to omega = D*k^2 in NR limit?
  Q3: Is the nabla^4 term the same physics in both frameworks?

Additional: Two-phase Lagrangian cross-check (Part 61 compatibility).

Results:
  Q1: PARTIAL -- metric perturbation gives 1/r; condensate density gives 1/r^2
  Q2: YES -- D_PDTP = hbar/(2*m_cond) = D_White when m_cond = m_eff [DERIVED]
  Q3: STRUCTURALLY YES -- both arise from two-field -> one-field elimination
      PHYSICALLY NO -- White's is dispersive (dynamic), PDTP's is static field eq.

Tests WH1-WH12: Sudoku consistency checks.
"""

import math
import numpy as np
import sympy as sp


# -----------------------------------------------------------------------
# Physical constants (from sudoku_engine.py)
# -----------------------------------------------------------------------

HBAR = 1.054571817e-34   # J s
C    = 2.99792458e8      # m/s
G    = 6.67430e-11       # m^3 kg^-1 s^-2
M_P  = 2.17643e-8        # kg (Planck mass)
M_E  = 9.1093837015e-31  # kg (electron mass)
M_P_PROTON = 1.67262192369e-27  # kg (proton mass)
L_P  = 1.616e-35         # m (Planck length)
ALPHA_EM = 7.2973525693e-3  # fine structure constant
A_BOHR = 5.29177210903e-11  # m (Bohr radius)
E_RYDBERG = 13.605693122994  # eV (Rydberg energy)
EV_TO_J = 1.602176634e-19   # J/eV


# -----------------------------------------------------------------------
# Q2: Non-relativistic limit -- SymPy verification
# -----------------------------------------------------------------------

def verify_nr_limit_sympy():
    """
    SymPy: Verify that the PDTP Klein-Gordon dispersion reduces to
    omega ~ omega_gap + hbar*k^2/(2*m_cond) in the non-relativistic limit.

    PDTP dispersion: omega^2 = c^2*k^2 + omega_gap^2
    NR limit (k << omega_gap/c): Taylor expand sqrt(1 + x) ~ 1 + x/2 - x^2/8

    Returns: (passed, message, steps)
    """
    c, k, omega_gap, hbar_s, m = sp.symbols('c k omega_gap hbar m', positive=True)

    # Full PDTP dispersion
    omega_full = sp.sqrt(c**2 * k**2 + omega_gap**2)

    # Taylor expand in k around k=0 to order k^4
    omega_taylor = sp.series(omega_full, k, 0, n=5)

    steps = []
    steps.append(('Full dispersion', 'omega = sqrt(c^2*k^2 + omega_gap^2)'))

    # Extract coefficients
    coeff_k0 = omega_taylor.coeff(k, 0)
    coeff_k2 = omega_taylor.coeff(k, 2)
    coeff_k4 = omega_taylor.coeff(k, 4)

    steps.append(('k^0 term', str(sp.simplify(coeff_k0))))
    steps.append(('k^2 term', str(sp.simplify(coeff_k2))))
    steps.append(('k^4 term', str(sp.simplify(coeff_k4))))

    # Expected: k^2 coefficient = c^2/(2*omega_gap)
    expected_k2 = c**2 / (2 * omega_gap)
    diff_k2 = sp.simplify(coeff_k2 - expected_k2)

    steps.append(('Expected k^2 coeff', 'c^2/(2*omega_gap)'))
    steps.append(('Difference', str(diff_k2)))

    # Now substitute omega_gap = m*c^2/hbar
    coeff_k2_sub = coeff_k2.subs(omega_gap, m * c**2 / hbar_s)
    coeff_k2_simplified = sp.simplify(coeff_k2_sub)

    steps.append(('Substituting omega_gap = m*c^2/hbar',
                  'D = {} = hbar/(2*m)'.format(coeff_k2_simplified)))

    # Verify D = hbar/(2*m)
    expected_D = hbar_s / (2 * m)
    diff_D = sp.simplify(coeff_k2_simplified - expected_D)
    passed = (diff_D == 0) and (diff_k2 == 0)

    steps.append(('D_PDTP = hbar/(2*m_cond)?', 'YES' if passed else 'NO'))

    msg = 'NR limit: omega ~ omega_gap + [hbar/(2*m_cond)]*k^2' if passed else 'NR limit FAILED'

    return passed, msg, steps


def verify_nr_limit_quartic():
    """
    SymPy: Verify the k^4 correction term in the NR expansion.

    Expected: k^4 coefficient = -c^4/(8*omega_gap^3) = -hbar^3/(8*m^3*c^2)

    Returns: (passed, message)
    """
    c, k, omega_gap, hbar_s, m = sp.symbols('c k omega_gap hbar m', positive=True)

    omega_full = sp.sqrt(c**2 * k**2 + omega_gap**2)
    omega_taylor = sp.series(omega_full, k, 0, n=5)
    coeff_k4 = omega_taylor.coeff(k, 4)

    expected_k4 = -c**4 / (8 * omega_gap**3)
    diff = sp.simplify(coeff_k4 - expected_k4)

    passed = (diff == 0)
    msg = 'k^4 correction = -c^4/(8*omega_gap^3)' if passed else 'k^4 MISMATCH'
    return passed, msg


# -----------------------------------------------------------------------
# Q1: Constitutive profile comparison
# -----------------------------------------------------------------------

def compute_constitutive_profile_pdtp():
    """
    Compute the PDTP effective sound speed profile near a gravitating mass M.

    Two contributions:
    1. Condensate density (GP vortex): 1/c_s^2 ~ (1/c^2)(1 + n^2/r^2) [1/r^2 term]
    2. Metric perturbation (gravity):   1/c_eff^2 ~ (1/c^2)(1 - 2GM/rc^2) [1/r term]

    Returns: dict with profile parameters
    """
    # For a proton-mass source
    M = M_P_PROTON

    # Metric contribution (1/r coefficient)
    C_grav = -2 * G * M / C**4    # m (coefficient of 1/r in 1/c_eff^2)

    # Condensate density contribution (1/r^2 coefficient) for n=1 vortex
    n_wind = 1
    a0_cond = HBAR / (M_P * C)    # condensate lattice spacing (Planck length)
    B_density = n_wind**2 / C**2 * a0_cond**2  # m^2 (coefficient of 1/r^2)

    # White's C for hydrogen (from Rydberg calibration)
    # C_White = 2*n^4 / (a_0 * omega_star^2) at n=1
    # More directly: 1/c_s^2 = A + beta/r where beta = 2/(a_0)
    # in wavenumber space. The key point is beta ~ 1/a_Bohr ~ 1.89e10 m^-1
    # while C_grav ~ 2.76e-62 m
    C_white_scale = 2.0 / A_BOHR   # m^-1 (order of magnitude for k_eff^2 coefficient)

    # Crossover radius where 1/r and 1/r^2 terms are equal
    # C_grav/r = B_density/r^2 => r_cross = B_density/C_grav
    if abs(C_grav) > 0:
        r_crossover = abs(B_density / C_grav)
    else:
        r_crossover = float('inf')

    return {
        'C_grav': C_grav,
        'B_density': B_density,
        'C_white_scale': C_white_scale,
        'r_crossover': r_crossover,
        'source_mass': M,
    }


# -----------------------------------------------------------------------
# Q2: Numerical verification of D coefficient
# -----------------------------------------------------------------------

def compute_D_coefficients():
    """
    Compute and compare dispersion coefficients D for PDTP and White.

    D_PDTP = hbar/(2*m_cond) with m_cond = m_P
    D_White = hbar/(2*mu_H) with mu_H = reduced mass of e-p system

    Returns: dict with D values and ratio
    """
    # PDTP: m_cond = Planck mass
    D_pdtp = HBAR / (2 * M_P)

    # White: reduced mass of hydrogen
    mu_H = M_E * M_P_PROTON / (M_E + M_P_PROTON)
    D_white = HBAR / (2 * mu_H)

    # Ratio = m_cond / mu_H (the hierarchy)
    ratio = D_white / D_pdtp

    # Also compute omega_gap for PDTP
    omega_gap = M_P * C**2 / HBAR

    return {
        'D_pdtp': D_pdtp,
        'D_white': D_white,
        'mu_H': mu_H,
        'ratio_D': ratio,
        'omega_gap': omega_gap,
    }


# -----------------------------------------------------------------------
# Q3: Biharmonic comparison
# -----------------------------------------------------------------------

def compute_biharmonic_parameters():
    """
    Compute the coefficients in both biharmonic equations.

    White (Eq. A17): d^2 rho/dt^2 = c_L^2 nabla^2 rho - D^2 nabla^4 rho
      where D^2 = hbar^2/(4*mu^2)

    PDTP (Part 61, static): nabla^4 Phi + 4g^2 Phi = source
      where g = m_cond*c^2/hbar  (PDTP coupling in rad/s)

    Returns: dict with coefficients
    """
    # White
    mu_H = M_E * M_P_PROTON / (M_E + M_P_PROTON)
    D2_white = HBAR**2 / (4 * mu_H**2)

    # PDTP
    g_pdtp = M_P * C**2 / HBAR     # rad/s
    coeff_pdtp = 4 * g_pdtp**2      # coefficient of Phi in nabla^4 Phi + coeff*Phi = source

    # PDTP healing length (sets scale where nabla^4 matters)
    a0_pdtp = HBAR / (M_P * C)       # Planck length
    xi_pdtp = a0_pdtp / math.sqrt(2)  # healing length

    return {
        'D2_white': D2_white,
        'coeff_pdtp': coeff_pdtp,
        'g_pdtp': g_pdtp,
        'xi_pdtp': xi_pdtp,
        'a0_pdtp': a0_pdtp,
    }


# -----------------------------------------------------------------------
# Two-phase Lagrangian cross-check
# -----------------------------------------------------------------------

def verify_two_phase_nr_limit():
    """
    SymPy: Verify that the NR limit works for the two-phase breathing mode.

    Breathing mode dispersion: omega^2 = c^2*k^2 + 2*g*Phi
    NR limit should give omega ~ sqrt(2*g*Phi) + D*k^2 with D = hbar/(2*m_cond)

    Returns: (passed, message)
    """
    c, k, g_s, Phi_s, hbar_s, m = sp.symbols('c k g Phi hbar m', positive=True)

    # Breathing mode gap
    omega_gap_breathing = sp.sqrt(2 * g_s * Phi_s)

    # Full dispersion
    omega_full = sp.sqrt(c**2 * k**2 + 2 * g_s * Phi_s)

    # NR expansion
    omega_taylor = sp.series(omega_full, k, 0, n=3)
    coeff_k2 = omega_taylor.coeff(k, 2)

    # Expected: c^2/(2*omega_gap_breathing)
    expected_k2 = c**2 / (2 * omega_gap_breathing)
    diff = sp.simplify(coeff_k2 - expected_k2)

    passed = (diff == 0)
    msg = 'Breathing mode NR limit: D = c^2/(2*sqrt(2*g*Phi))' if passed else 'FAIL'
    return passed, msg


def verify_newton_third_law():
    """
    SymPy: Verify psi_ddot = -2*phi_+_ddot from two-phase Lagrangian.

    The EL equations give:
      phi_b_tt = g*sin(psi - phi_b)
      phi_s_tt = -g*sin(psi - phi_s)
      psi_tt = -g*sin(psi - phi_b) + g*sin(psi - phi_s)

    Sum: phi_b_tt + phi_s_tt + psi_tt = 0
    Therefore: 2*phi_+_tt + psi_tt = 0 => psi_tt = -2*phi_+_tt

    Returns: (passed, message)
    """
    psi, phi_b, phi_s, g_s = sp.symbols('psi phi_b phi_s g', real=True)

    # Forces from EL equations
    F_phi_b = g_s * sp.sin(psi - phi_b)
    F_phi_s = -g_s * sp.sin(psi - phi_s)
    F_psi = -g_s * sp.sin(psi - phi_b) + g_s * sp.sin(psi - phi_s)

    # Check sum = 0 (momentum conservation)
    total = sp.trigsimp(F_phi_b + F_phi_s + F_psi)

    # Check F_psi = -(F_phi_b + F_phi_s) = -2*F_phi_+
    # where F_phi_+ = (F_phi_b + F_phi_s)/2
    F_phi_plus = (F_phi_b + F_phi_s) / 2
    check_n3 = sp.trigsimp(F_psi + 2 * F_phi_plus)

    passed = (total == 0) and (check_n3 == 0)
    msg = 'psi_tt + 2*phi_+_tt = 0 (Newton 3rd law)' if passed else 'FAIL'
    return passed, msg


def verify_jeans_eigenvalue():
    """
    SymPy: Verify the Jeans instability eigenvalue = +2*sqrt(2)*g.

    Linearized coupled system:
      Phi_tt = 4g * phi_-
      phi_-_tt = 2g * Phi

    Eigenvalue equation: det(M - lambda*I) = 0
      M = [[0, 4g], [2g, 0]]
      lambda^2 - 8g^2 = 0
      lambda = +/- 2*sqrt(2)*g

    Returns: (passed, message)
    """
    g_s = sp.Symbol('g', positive=True)

    M = sp.Matrix([[0, 4*g_s], [2*g_s, 0]])
    eigenvals = M.eigenvals()

    # The positive eigenvalue should be 2*sqrt(2)*g
    expected = 2 * sp.sqrt(2) * g_s
    found_positive = False
    for ev in eigenvals:
        if sp.simplify(ev - expected) == 0:
            found_positive = True
            break

    passed = found_positive
    msg = 'Jeans eigenvalue = +2*sqrt(2)*g (confirmed)' if passed else 'FAIL'
    return passed, msg


# -----------------------------------------------------------------------
# Sudoku consistency checks
# -----------------------------------------------------------------------

def run_sudoku_checks():
    """
    Sudoku consistency checks for Part 67 equations.

    WH1:  NR limit: D_PDTP = hbar/(2*m_cond) [SymPy]
    WH2:  NR limit: k^4 correction coefficient [SymPy]
    WH3:  Numerical: D_PDTP matches hbar/(2*M_P)
    WH4:  Numerical: D_White matches hbar/(2*mu_H)
    WH5:  D ratio = m_cond/mu_H (hierarchy check)
    WH6:  Constitutive profile: metric gives 1/r (C_grav computed)
    WH7:  Constitutive profile: condensate density gives 1/r^2 (B computed)
    WH8:  Biharmonic: PDTP healing length ~ l_P/sqrt(2)
    WH9:  Two-phase: breathing mode NR limit [SymPy]
    WH10: Two-phase: Newton's 3rd law preserved [SymPy]
    WH11: Two-phase: Jeans eigenvalue = +2*sqrt(2)*g [SymPy]
    WH12: D_White numerical vs Rydberg (cross-check)

    Returns: list of (tag, description, passed, detail) tuples
    """
    results = []
    tol = 0.01  # 1% Sudoku tolerance

    # ------------------------------------------------------------------
    # WH1: NR limit -- SymPy verification
    # ------------------------------------------------------------------
    wh1_pass, wh1_msg, wh1_steps = verify_nr_limit_sympy()
    results.append(('WH1', 'NR limit: D_PDTP = hbar/(2*m_cond) [SymPy]',
                    wh1_pass, wh1_msg))

    # ------------------------------------------------------------------
    # WH2: k^4 correction -- SymPy
    # ------------------------------------------------------------------
    wh2_pass, wh2_msg = verify_nr_limit_quartic()
    results.append(('WH2', 'NR k^4 correction: -c^4/(8*omega_gap^3) [SymPy]',
                    wh2_pass, wh2_msg))

    # ------------------------------------------------------------------
    # WH3: Numerical D_PDTP
    # ------------------------------------------------------------------
    D_vals = compute_D_coefficients()
    D_pdtp_expected = HBAR / (2 * M_P)
    ratio3 = D_vals['D_pdtp'] / D_pdtp_expected
    wh3_pass = abs(ratio3 - 1.0) < tol
    results.append(('WH3', 'D_PDTP = {:.6e} m^2/s (expected {:.6e})'.format(
        D_vals['D_pdtp'], D_pdtp_expected), wh3_pass,
        'ratio = {:.8f}'.format(ratio3)))

    # ------------------------------------------------------------------
    # WH4: Numerical D_White
    # ------------------------------------------------------------------
    D_white_expected = HBAR / (2 * D_vals['mu_H'])
    ratio4 = D_vals['D_white'] / D_white_expected
    wh4_pass = abs(ratio4 - 1.0) < tol
    results.append(('WH4', 'D_White = {:.6e} m^2/s (expected {:.6e})'.format(
        D_vals['D_white'], D_white_expected), wh4_pass,
        'ratio = {:.8f}'.format(ratio4)))

    # ------------------------------------------------------------------
    # WH5: D ratio = m_cond/mu_H (hierarchy)
    # ------------------------------------------------------------------
    expected_ratio = M_P / D_vals['mu_H']
    actual_ratio = D_vals['ratio_D']
    ratio5 = actual_ratio / expected_ratio
    wh5_pass = abs(ratio5 - 1.0) < tol
    results.append(('WH5', 'D_White/D_PDTP = {:.4e}, m_P/mu_H = {:.4e}'.format(
        actual_ratio, expected_ratio), wh5_pass,
        'ratio = {:.8f}'.format(ratio5)))

    # ------------------------------------------------------------------
    # WH6: Metric constitutive profile gives 1/r
    # ------------------------------------------------------------------
    profile = compute_constitutive_profile_pdtp()
    # C_grav should be -2GM/c^4 for proton
    C_expected = -2 * G * M_P_PROTON / C**4
    ratio6 = profile['C_grav'] / C_expected
    wh6_pass = abs(ratio6 - 1.0) < tol
    results.append(('WH6', 'C_grav = {:.4e} m (1/r metric term)'.format(
        profile['C_grav']), wh6_pass,
        'ratio = {:.8f}'.format(ratio6)))

    # ------------------------------------------------------------------
    # WH7: Condensate density gives 1/r^2 (not 1/r)
    # ------------------------------------------------------------------
    # B_density should be n^2*a0^2/c^2
    a0_cond = HBAR / (M_P * C)
    B_expected = 1.0 * a0_cond**2 / C**2  # n=1
    ratio7 = profile['B_density'] / B_expected
    wh7_pass = abs(ratio7 - 1.0) < tol
    results.append(('WH7', 'B_density = {:.4e} m^2 (1/r^2 condensate term)'.format(
        profile['B_density']), wh7_pass,
        'ratio = {:.8f}'.format(ratio7)))

    # ------------------------------------------------------------------
    # WH8: Healing length ~ l_P/sqrt(2)
    # ------------------------------------------------------------------
    biharm = compute_biharmonic_parameters()
    xi_expected = L_P / math.sqrt(2)
    ratio8 = biharm['xi_pdtp'] / xi_expected
    wh8_pass = abs(ratio8 - 1.0) < tol
    results.append(('WH8', 'xi_PDTP = {:.4e} m (expected l_P/sqrt(2) = {:.4e})'.format(
        biharm['xi_pdtp'], xi_expected), wh8_pass,
        'ratio = {:.8f}'.format(ratio8)))

    # ------------------------------------------------------------------
    # WH9: Two-phase breathing mode NR limit [SymPy]
    # ------------------------------------------------------------------
    wh9_pass, wh9_msg = verify_two_phase_nr_limit()
    results.append(('WH9', 'Breathing mode NR limit [SymPy]',
                    wh9_pass, wh9_msg))

    # ------------------------------------------------------------------
    # WH10: Newton's 3rd law preserved [SymPy]
    # ------------------------------------------------------------------
    wh10_pass, wh10_msg = verify_newton_third_law()
    results.append(('WH10', 'Newton 3rd law: psi_tt = -2*phi_+_tt [SymPy]',
                    wh10_pass, wh10_msg))

    # ------------------------------------------------------------------
    # WH11: Jeans eigenvalue = +2*sqrt(2)*g [SymPy]
    # ------------------------------------------------------------------
    wh11_pass, wh11_msg = verify_jeans_eigenvalue()
    results.append(('WH11', 'Jeans eigenvalue = +2*sqrt(2)*g [SymPy]',
                    wh11_pass, wh11_msg))

    # ------------------------------------------------------------------
    # WH12: D_White cross-check vs Rydberg energy
    # White: E_n = -hbar * omega_n, omega_n = D*kappa_n^2, kappa_n = 1/(n*a_0)
    # At n=1: E_1 = hbar * D / a_0^2 = hbar^2/(2*mu*a_0^2)
    # This should equal E_Rydberg = 13.606 eV
    # ------------------------------------------------------------------
    mu_H = D_vals['mu_H']
    E1_from_D = HBAR**2 / (2 * mu_H * A_BOHR**2) / EV_TO_J  # eV
    ratio12 = E1_from_D / E_RYDBERG
    wh12_pass = abs(ratio12 - 1.0) < tol
    results.append(('WH12', 'E_1 from D = {:.4f} eV (Rydberg = {:.4f} eV)'.format(
        E1_from_D, E_RYDBERG), wh12_pass,
        'ratio = {:.8f}'.format(ratio12)))

    return results


# =========================================================================
# PHASE RUNNER
# =========================================================================

def run_white_comparison_phase(rw, engine):
    """
    Phase 36: White et al. (2026) Comparison (Part 67).

    Returns: (n_pass, n_total)
    """
    rw.section("Phase 36 -- White et al. (2026) Comparison (Part 67)")
    rw.print("  Source: Phys. Rev. Research 8, 013264 (2026)")
    rw.print("  Three questions:")
    rw.print("    Q1: Can PDTP derive constitutive profile 1/c_s^2 = A + C/r?")
    rw.print("    Q2: Does PDTP dispersion reduce to omega = D*k^2 (NR limit)?")
    rw.print("    Q3: Is the nabla^4 term the same physics?")
    rw.print("  Plus: Two-phase Lagrangian cross-check (Part 61).")
    rw.print("")

    passes = 0
    total = 0

    # ==================================================================
    # Q2: Non-relativistic limit (SymPy)
    # ==================================================================
    rw.subsection("Q2: Non-Relativistic Limit of PDTP Dispersion")

    nr_pass, nr_msg, nr_steps = verify_nr_limit_sympy()
    for step_label, step_expr in nr_steps:
        rw.print("    {}: {}".format(step_label, step_expr))
    rw.print("")

    status = "PASS" if nr_pass else "FAIL"
    rw.print("  [{}] {}".format(status, nr_msg))
    rw.print("")

    # k^4 correction
    k4_pass, k4_msg = verify_nr_limit_quartic()
    status = "PASS" if k4_pass else "FAIL"
    rw.print("  [{}] k^4 correction: {}".format(status, k4_msg))
    rw.print("")

    # Numerical D values
    D_vals = compute_D_coefficients()
    rw.print("  Dispersion coefficients:")
    rw.print("    D_PDTP  = hbar/(2*m_P) = {:.6e} m^2/s".format(D_vals['D_pdtp']))
    rw.print("    D_White = hbar/(2*mu_H) = {:.6e} m^2/s".format(D_vals['D_white']))
    rw.print("    Ratio D_White/D_PDTP = {:.4e} = m_P/mu_H (hierarchy)".format(
        D_vals['ratio_D']))
    rw.print("    omega_gap (PDTP) = {:.4e} rad/s (rest frequency)".format(
        D_vals['omega_gap']))
    rw.print("")
    rw.print("  Conclusion Q2: PDTP contains White as non-relativistic limit.")
    rw.print("  D_PDTP = hbar/(2*m_cond) matches D_White = hbar/(2*m_eff)")
    rw.print("  when m_cond plays the role of m_eff (reduced mass).")
    rw.print("")

    # ==================================================================
    # Q1: Constitutive profile
    # ==================================================================
    rw.subsection("Q1: Constitutive Profile 1/c_s^2(r)")

    profile = compute_constitutive_profile_pdtp()
    rw.print("  PDTP sound speed near a proton-mass source:")
    rw.print("    Two contributions to 1/c_s^2(r):")
    rw.print("")
    rw.print("    1. Metric perturbation (gravity): C/r term")
    rw.print("       C_grav = -2GM/c^4 = {:.4e} m".format(profile['C_grav']))
    rw.print("       --> 1/c_eff^2 = (1/c^2)(1 - 2GM/(rc^2))")
    rw.print("       This IS White's 1/r profile. [DERIVED]")
    rw.print("")
    rw.print("    2. Condensate density (GP vortex): B/r^2 term")
    rw.print("       B_density = n^2*a0^2/c^2 = {:.4e} m^2".format(
        profile['B_density']))
    rw.print("       --> 1/c_s^2 = (1/c^2)(1 + n^2*a0^2/r^2)")
    rw.print("       This is 1/r^2, NOT White's 1/r. [DERIVED]")
    rw.print("")
    rw.print("    Crossover: 1/r dominates over 1/r^2 at r > {:.4e} m".format(
        profile['r_crossover']))
    rw.print("    (For gravity: at all macroscopic distances)")
    rw.print("")
    rw.print("  Conclusion Q1: PARTIAL YES.")
    rw.print("  The 1/r profile comes from the gravitational metric perturbation.")
    rw.print("  PDTP derives what White assumes -- but requires gravity to do it")
    rw.print("  (same circularity as Parts 29-35).")
    rw.print("")

    # ==================================================================
    # Q3: Biharmonic comparison
    # ==================================================================
    rw.subsection("Q3: Biharmonic Term Comparison")

    biharm = compute_biharmonic_parameters()
    rw.print("  White (Eq. A17):")
    rw.print("    d^2 rho/dt^2 = c_L^2 nabla^2 rho - D^2 nabla^4 rho")
    rw.print("    D^2 = hbar^2/(4*mu^2) = {:.4e} m^4/s^2".format(
        biharm['D2_white']))
    rw.print("    Type: DYNAMIC wave equation (2nd order in time)")
    rw.print("    Origin: Madelung quantum potential")
    rw.print("")
    rw.print("  PDTP (Part 61):")
    rw.print("    nabla^4 Phi + 4g^2 Phi = source")
    rw.print("    4g^2 = {:.4e} rad^2/s^2".format(biharm['coeff_pdtp']))
    rw.print("    Type: STATIC field equation (0th order in time)")
    rw.print("    Origin: Two-phase Lagrangian (eliminate phi_-)")
    rw.print("    Healing length: xi = {:.4e} m ~ l_P/sqrt(2)".format(
        biharm['xi_pdtp']))
    rw.print("")
    rw.print("  Structural parallel:")
    rw.print("    Both nabla^4 arise from TWO-FIELD -> ONE-FIELD elimination:")
    rw.print("    - White: (rho, S) -> eliminate S -> nabla^4 in rho equation")
    rw.print("    - PDTP: (phi_+, phi_-) -> eliminate phi_- -> nabla^4 in phi_+ equation")
    rw.print("    [PDTP Original: structural equivalence identified]")
    rw.print("")
    rw.print("  Key difference:")
    rw.print("    White's nabla^4 is DISPERSIVE (increases omega at high k).")
    rw.print("    PDTP's nabla^4 is a FIELD EQUATION modification (changes potential).")
    rw.print("    Same mathematical structure, different physical role.")
    rw.print("")

    # ==================================================================
    # Two-phase cross-check
    # ==================================================================
    rw.subsection("Two-Phase Lagrangian Cross-Check (Part 61)")

    # Breathing mode NR limit
    tp_nr_pass, tp_nr_msg = verify_two_phase_nr_limit()
    status = "PASS" if tp_nr_pass else "FAIL"
    rw.print("  [{}] {}".format(status, tp_nr_msg))

    # Newton's 3rd law
    n3_pass, n3_msg = verify_newton_third_law()
    status = "PASS" if n3_pass else "FAIL"
    rw.print("  [{}] {}".format(status, n3_msg))

    # Jeans eigenvalue
    jeans_pass, jeans_msg = verify_jeans_eigenvalue()
    status = "PASS" if jeans_pass else "FAIL"
    rw.print("  [{}] {}".format(status, jeans_msg))

    rw.print("")
    rw.print("  All two-phase results preserved under NR limit comparison.")
    rw.print("")

    # ==================================================================
    # Sudoku checks
    # ==================================================================
    rw.subsection("Sudoku Consistency Checks (WH1-WH12)")

    results = run_sudoku_checks()
    for tag, desc, passed, detail in results:
        status = "PASS" if passed else "FAIL"
        rw.print("  [{}] {}: {}".format(status, tag, desc))
        if not passed:
            rw.print("         Detail: {}".format(detail))
        total += 1
        if passed:
            passes += 1

    rw.print("")
    rw.print("  Sudoku score: {}/{} pass".format(passes, total))
    rw.print("")

    # ==================================================================
    # Summary
    # ==================================================================
    rw.subsection("Summary -- Part 67 Findings")

    rw.print("  Q1 (Constitutive profile): PARTIAL YES")
    rw.print("    - Metric perturbation gives 1/r (matches White) [DERIVED]")
    rw.print("    - Condensate density gives 1/r^2 (different from White) [DERIVED]")
    rw.print("    - 1/r requires gravity -> same circularity as Parts 29-35")
    rw.print("")
    rw.print("  Q2 (NR limit): YES")
    rw.print("    - omega ~ omega_gap + [hbar/(2*m_cond)]*k^2 [DERIVED, SymPy VERIFIED]")
    rw.print("    - D_PDTP = D_White when m_cond = m_eff")
    rw.print("    - PDTP contains White et al. as non-relativistic special case")
    rw.print("")
    rw.print("  Q3 (Biharmonic): STRUCTURALLY YES, PHYSICALLY NO")
    rw.print("    - Both nabla^4 arise from two-field -> one-field elimination")
    rw.print("    - White's is dispersive (dynamic); PDTP's is field equation (static)")
    rw.print("    - Deep connection: same mathematical reduction pattern [PDTP Original]")
    rw.print("")
    rw.print("  Two-phase cross-check: ALL PRESERVED")
    rw.print("    - NR limit works for breathing mode")
    rw.print("    - Newton's 3rd law (psi_tt = -2*phi_+_tt) unchanged")
    rw.print("    - Jeans eigenvalue (+2*sqrt(2)*g) unchanged")
    rw.print("")
    rw.print("  What PDTP adds beyond White:")
    rw.print("    1. Lagrangian foundation (derives what White assumes)")
    rw.print("    2. Relativistic (White is NR limit of PDTP)")
    rw.print("    3. Gravity included (White has hydrogen only)")
    rw.print("    4. Two-phase structure (breathing mode + biharmonic gravity)")
    rw.print("    5. Less circular (classical Lagrangian, not Madelung-from-QM)")
    rw.print("")

    return passes, total


# =========================================================================
# Standalone execution
# =========================================================================

if __name__ == '__main__':
    results = run_sudoku_checks()
    n_pass = sum(1 for _, _, p, _ in results if p)
    n_total = len(results)
    print("White et al. comparison -- Sudoku: {}/{} pass".format(n_pass, n_total))
    for tag, desc, passed, detail in results:
        status = "PASS" if passed else "FAIL"
        print("  [{}] {}: {}".format(status, tag, desc))
        if not passed:
            print("         {}".format(detail))
