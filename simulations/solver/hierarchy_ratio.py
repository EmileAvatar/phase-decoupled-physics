#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
hierarchy_ratio.py -- Phase 19: Hierarchy Ratio R = alpha_G / alpha_EM
=======================================================================
Part 44 of the PDTP solver.

QUESTION: Can R = alpha_G / alpha_EM ~ 8e-37 be derived from lattice topology?

PDTP IDENTITY (PDTP Original):
  alpha_G(p) = G m_p^2 / (hbar c) = (m_p / m_cond)^2 = 1 / n_p^2
  R = alpha_G / alpha_EM = 1 / (n_p^2 * alpha_EM)
  where n_p = m_cond / m_p (vortex winding number, Part 33)

THREE CANDIDATE PATHS:
  Path A: QCD string tension (G-free: sigma_QCD -> m_cond -> G -> R)
  Path B: Dirac large numbers (N_Eddington, N_Hubble as topological n)
  Path C: Dvali species counting (N_species = n_p^2 -> circular)

EXPECTED RESULT: NEGATIVE
  Path A: m_cond = Lambda_QCD (not m_P) -> G off by ~10^40
  Path B: No Dirac number gives n_p ~ 1.30e19
  Path C: N_required = 10^38, N_SM ~ 118 -> off by 10^36
  FINDING: R = 1/(n^2 * alpha_EM) -- hierarchy problem IS the winding problem

Called from main.py as Phase 19.

Usage (standalone):
    cd simulations/solver
    python hierarchy_ratio.py
"""

import os
import sys
import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from sudoku_engine import (HBAR, C, G, L_P, M_P, M_E, M_P_PROTON,
                            ALPHA_EM, SudokuEngine)
from print_utils import ReportWriter


# ===========================================================================
# CONSTANTS
# ===========================================================================

# Gravitational fine-structure constants
ALPHA_G_PROTON = G * M_P_PROTON**2 / (HBAR * C)    # ~ 5.9e-39
ALPHA_G_ELECTRON = G * M_E**2 / (HBAR * C)          # ~ 1.75e-45

# Hierarchy ratios R = alpha_G / alpha_EM
R_PROTON = ALPHA_G_PROTON / ALPHA_EM     # ~ 8.1e-37
R_ELECTRON = ALPHA_G_ELECTRON / ALPHA_EM # ~ 2.4e-43

# Vortex winding numbers (Part 33: n = m_cond / m, m_cond = M_P)
N_PROTON = M_P / M_P_PROTON    # ~ 1.30e19
N_ELECTRON = M_P / M_E         # ~ 2.39e22

# QCD string tension (Part 38): sigma_QCD = 0.18 GeV^2 in natural units
# Convert to SI [J/m]: sigma_SI = sigma_nat * (1 GeV)^2 / (hbar * c)
GEV_TO_J = 1.602e-10                                     # 1 GeV in Joules
SIGMA_QCD_SI = 0.18 * GEV_TO_J**2 / (HBAR * C)          # J/m ~ 1.46e5

# Strong coupling factor from Part 38 (SU(3), N=3, beta = K_NAT = 1/(4*pi))
# F_SC = ln(2N/beta) = ln(6 * 4*pi) ~ 4.32
F_SC = np.log(6.0 * 4.0 * np.pi)

# QCD-inferred condensate mass (from sigma_QCD via Part 38 formula)
# sigma = F_SC * m_cond^2 * c^3 / hbar  ->  m_cond = sqrt(sigma * hbar / (F_SC * c^3))
M_COND_QCD = np.sqrt(SIGMA_QCD_SI * HBAR / (F_SC * C**3))  # kg ~ 3.6e-28

# Lambda_QCD reference: 200 MeV/c^2
LAMBDA_QCD = 200.0e-3 * GEV_TO_J / C**2   # kg ~ 3.56e-28

# Dirac / cosmological large numbers
T_PLANCK = L_P / C              # Planck time ~ 5.39e-44 s
T_HUBBLE = 4.35e17              # age of universe ~ 13.8 Gyr in seconds
N_EDDINGTON = 1.0e80            # protons in observable universe (Eddington number)
N_HUBBLE = T_HUBBLE / T_PLANCK  # ratio of cosmic to Planck time ~ 8.1e60

# Dvali species counting
# SM degrees of freedom (quarks x3 colors x2 chirality + leptons + bosons, approx)
N_SM_DOF = 118.0   # approximate SM species count


# ===========================================================================
# STEP 1 -- DEFINE AND COMPUTE R
# ===========================================================================

def print_step1_definition(rw):
    """Print the definition and numerical value of R."""
    rw.subsection("Step 1: Definition and Numerical Value")
    rw.print("  Gravitational fine-structure constant (proton):")
    rw.print("    alpha_G(p) = G m_p^2 / (hbar c)")
    rw.print("    alpha_G(p) = {:.4e}".format(ALPHA_G_PROTON))
    rw.print("")
    rw.print("  Electromagnetic fine-structure constant:")
    rw.print("    alpha_EM = e^2 / (4*pi*eps_0*hbar*c) = 1/137.036")
    rw.print("    alpha_EM = {:.4e}".format(ALPHA_EM))
    rw.print("")
    rw.print("  Hierarchy ratio R = alpha_G(p) / alpha_EM:")
    rw.print("    R = {:.4e}".format(R_PROTON))
    rw.print("    log10(R) = {:.2f}".format(np.log10(R_PROTON)))
    rw.print("    This means: gravity is 10^{:.0f} times weaker than EM at proton mass scale"
             .format(abs(np.log10(R_PROTON))))
    rw.print("")
    rw.print("  Same ratio for electron:")
    rw.print("    alpha_G(e) = {:.4e},  R_electron = {:.4e}".format(
        ALPHA_G_ELECTRON, R_ELECTRON))
    rw.print("")


# ===========================================================================
# STEP 2 -- PDTP IDENTITY R = 1 / (n^2 * alpha_EM)
# ===========================================================================

def print_step2_pdtp_identity(rw):
    """Derive and verify the PDTP hierarchy identity."""
    rw.subsection("Step 2: PDTP Identity (PDTP Original)")
    rw.print("  From Part 33: G = hbar*c / m_cond^2  (with m_cond = m_P)")
    rw.print("")
    rw.print("  Substituting into alpha_G(p) = G m_p^2 / (hbar c):")
    rw.print("    alpha_G(p) = (hbar*c / m_cond^2) * m_p^2 / (hbar*c)")
    rw.print("               = (m_p / m_cond)^2")
    rw.print("               = 1 / n_p^2     [where n_p = m_cond / m_p]")
    rw.print("")
    rw.print("  Therefore:")
    rw.print("    R = alpha_G(p) / alpha_EM = 1 / (n_p^2 * alpha_EM)   [PDTP Original]")
    rw.print("")
    rw.print("  VERIFICATION:")
    rw.print("    n_proton  = m_P / m_p = {:.4e}  (vortex winding number)".format(N_PROTON))
    rw.print("    1/(n_p^2 * alpha_EM) = {:.4e}".format(
        1.0 / (N_PROTON**2 * ALPHA_EM)))
    rw.print("    R (direct) = {:.4e}".format(R_PROTON))
    rw.print("    Ratio (identity check) = {:.8f}".format(
        (1.0 / (N_PROTON**2 * ALPHA_EM)) / R_PROTON))
    rw.print("")
    rw.print("    n_electron = m_P / m_e = {:.4e}".format(N_ELECTRON))
    rw.print("    1/(n_e^2 * alpha_EM) = {:.4e}".format(
        1.0 / (N_ELECTRON**2 * ALPHA_EM)))
    rw.print("    R_electron (direct) = {:.4e}".format(R_ELECTRON))
    rw.print("")
    rw.print("  SIGNIFICANCE (PDTP Original):")
    rw.print("    The hierarchy problem (R ~ 10^-37) reduces to ONE open question:")
    rw.print("    WHY IS n_p = m_P / m_p ~ 10^19?")
    rw.print("    If n_p can be derived from topology, BOTH G and R are determined.")
    rw.print("    The two mysteries (weak gravity + large G) are actually the same mystery.")
    rw.print("")


# ===========================================================================
# STEP 3 -- PATH A: QCD STRING TENSION CHAIN
# ===========================================================================

def print_step3_path_a(rw):
    """Path A: QCD string tension -> m_cond -> G -> R (G-free in structure)."""
    rw.subsection("Step 3: Path A -- QCD String Tension Chain")
    rw.print("  Idea: use sigma_QCD (measured, G-free) to infer m_cond, then G.")
    rw.print("  Source: Part 38 strong coupling formula sigma = F_SC * m_cond^2 * c^3 / hbar")
    rw.print("  F_SC = ln(2N/beta) = ln(6 * 4*pi) = {:.4f}".format(F_SC))
    rw.print("")
    rw.print("  INPUT (G-free): sigma_QCD = 0.18 GeV^2 = {:.4e} J/m".format(SIGMA_QCD_SI))
    rw.print("")
    rw.print("  CHAIN:")
    rw.print("    m_cond^2 = sigma_QCD * hbar / (F_SC * c^3)")
    rw.print("    m_cond   = {:.4e} kg".format(M_COND_QCD))
    m_cond_MeV = M_COND_QCD * C**2 / (GEV_TO_J * 1.0e-3)
    rw.print("             = {:.1f} MeV/c^2  (cf. Lambda_QCD ~ 200 MeV)".format(m_cond_MeV))
    rw.print("    Lambda_QCD (ref) = {:.4e} kg = {:.1f} MeV/c^2".format(
        LAMBDA_QCD, 200.0))
    rw.print("    Ratio m_cond / Lambda_QCD = {:.4f}  (~1 = consistent)".format(
        M_COND_QCD / LAMBDA_QCD))
    rw.print("")
    G_pred_A = HBAR * C / M_COND_QCD**2
    alpha_G_A = G_pred_A * M_P_PROTON**2 / (HBAR * C)
    R_pred_A = alpha_G_A / ALPHA_EM
    rw.print("    G_pred = hbar*c / m_cond^2 = {:.4e}  (G_known = {:.4e})".format(
        G_pred_A, G))
    rw.print("    G_pred / G_known = {:.4e}  (off by ~10^40)".format(G_pred_A / G))
    rw.print("")
    rw.print("    alpha_G_pred = {:.4e}  (alpha_G_known = {:.4e})".format(
        alpha_G_A, ALPHA_G_PROTON))
    rw.print("    R_pred = {:.4e}  (R_known = {:.4e})".format(R_pred_A, R_PROTON))
    rw.print("    R_pred / R_known = {:.4e}".format(R_pred_A / R_PROTON))
    rw.print("")
    rw.print("  RESULT: PATH A FAILS for G and R.")
    rw.print("    Path A correctly finds m_cond ~ Lambda_QCD (QCD scale, ~200 MeV).")
    rw.print("    But G requires m_cond = m_P (Planck scale, ~1.22e19 GeV).")
    rw.print("    Gap = (m_P / Lambda_QCD)^2 = ({:.2e})^2 ~ {:.2e}".format(
        M_P / LAMBDA_QCD, (M_P / LAMBDA_QCD)**2))
    rw.print("    This gap IS the hierarchy problem: two condensate scales,")
    rw.print("    QCD (Lambda_QCD) and gravitational (m_P), not yet connected.")
    rw.print("")


# ===========================================================================
# STEP 4 -- PATH B: DIRAC LARGE NUMBERS
# ===========================================================================

def print_step4_path_b(rw):
    """Path B: Dirac large numbers as topological candidates for n_p."""
    rw.subsection("Step 4: Path B -- Dirac Large Numbers")
    rw.print("  Idea: maybe n_p ~ 10^19 has a topological origin in a large cosmic number.")
    rw.print("  Source: Dirac (1937), Nature 139, 323 -- large numbers hypothesis.")
    rw.print("")
    rw.print("  n_p actual = M_P / m_p = {:.4e}".format(N_PROTON))
    rw.print("")

    # Eddington number
    n_edd = np.sqrt(N_EDDINGTON)
    rw.print("  Candidate 1: N_Eddington ~ 10^80 (protons in observable universe)")
    rw.print("    n_pred = sqrt(N_Edd) = sqrt(1e80) = {:.4e}".format(n_edd))
    rw.print("    n_pred / n_p = {:.4e}  (off by {:.1f} orders)".format(
        n_edd / N_PROTON, np.log10(n_edd / N_PROTON)))
    rw.print("")

    # Hubble ratio
    n_hub = np.sqrt(N_HUBBLE)
    rw.print("  Candidate 2: N_Hubble = t_H / t_P = {:.4e}".format(N_HUBBLE))
    rw.print("    n_pred = sqrt(N_Hubble) = {:.4e}".format(n_hub))
    rw.print("    n_pred / n_p = {:.4e}  (off by {:.1f} orders)".format(
        n_hub / N_PROTON, np.log10(n_hub / N_PROTON)))
    rw.print("")

    # cube root of Eddington
    n_edd_cbrt = N_EDDINGTON**(1.0/3.0)
    rw.print("  Candidate 3: N_Eddington^(1/3) ~ 10^27")
    rw.print("    n_pred = N_Edd^(1/3) = {:.4e}".format(n_edd_cbrt))
    rw.print("    n_pred / n_p = {:.4e}  (off by {:.1f} orders)".format(
        n_edd_cbrt / N_PROTON, np.log10(n_edd_cbrt / N_PROTON)))
    rw.print("")
    rw.print("  RESULT: PATH B FAILS.")
    rw.print("    No standard large number gives n_p ~ 1.30e19 without extra assumptions.")
    rw.print("    Dirac hypothesis also predicts G ~ 1/t (G time-varying), which is")
    rw.print("    constrained: |dG/dt| / G < 1e-12 per year (lunar laser ranging).")
    rw.print("")


# ===========================================================================
# STEP 5 -- PATH C: DVALI SPECIES COUNTING
# ===========================================================================

def print_step5_path_c(rw):
    """Path C: Dvali species mechanism -- show circularity."""
    rw.subsection("Step 5: Path C -- Dvali Species Counting")
    rw.print("  Idea (Dvali 2007): G_eff = G_bare / N_species.")
    rw.print("  If N_species derivable from topology, G follows without G input.")
    rw.print("  Source: Dvali (2007), arXiv:0706.1075.")
    rw.print("")
    N_required = N_PROTON**2
    rw.print("  For G_eff = G_measured, need N_species = n_p^2 = {:.4e}".format(N_required))
    rw.print("  SM degrees of freedom: N_SM ~ {:.0f}".format(N_SM_DOF))
    rw.print("  Ratio N_required / N_SM = {:.4e}  (off by {:.1f} orders)".format(
        N_required / N_SM_DOF, np.log10(N_required / N_SM_DOF)))
    rw.print("")
    rw.print("  CIRCULARITY: N_required = n_p^2 = (M_P/m_p)^2 requires knowing M_P,")
    rw.print("  which requires knowing G. The Dvali mechanism is G-free only if")
    rw.print("  N_species is counted independently (e.g. from string landscape).")
    rw.print("  With SM alone: N_SM ~ 118, requires 10^36 additional species.")
    rw.print("")
    rw.print("  RESULT: PATH C IS CIRCULAR (uses G to define N_required).")
    rw.print("")


# ===========================================================================
# SUDOKU TESTS (H1 - H10)
# ===========================================================================

def run_sudoku_tests():
    """
    10 Sudoku consistency tests for the hierarchy ratio.
    Returns list of (label, description, value, ok) tuples.
    """
    results = []

    def record_ratio(label, desc, computed, expected, tol=1.0e-4):
        if abs(expected) < 1.0e-300:
            passed = abs(computed) < 1.0e-300
            ratio = 0.0 if passed else float('inf')
        else:
            ratio = computed / expected
            passed = abs(ratio - 1.0) < tol
        results.append((label, desc, ratio, passed))

    def record_bool(label, desc, ok):
        results.append((label, desc, 1.0 if ok else 0.0, ok))

    # H1: R_proton = alpha_G(p) / alpha_EM (verify value in expected range)
    R_expected = 8.1e-37   # approximate known value
    record_ratio("H1", "R = alpha_G(p)/alpha_EM ~ 8e-37 (numerical)",
                 R_PROTON, R_expected, tol=0.10)

    # H2: PDTP identity n_p^2 * R * alpha_EM = 1 (proton)
    identity_p = N_PROTON**2 * R_PROTON * ALPHA_EM
    record_ratio("H2", "PDTP identity: n_p^2 * R * alpha_EM = 1 (proton)",
                 identity_p, 1.0, tol=1.0e-9)

    # H3: PDTP identity n_e^2 * R_e * alpha_EM = 1 (electron)
    identity_e = N_ELECTRON**2 * R_ELECTRON * ALPHA_EM
    record_ratio("H3", "PDTP identity: n_e^2 * R_e * alpha_EM = 1 (electron)",
                 identity_e, 1.0, tol=1.0e-9)

    # H4: alpha_G(p) = 1/n_p^2 exactly (PDTP identity)
    alpha_G_from_n = 1.0 / N_PROTON**2
    record_ratio("H4", "alpha_G(p) = 1/n_p^2  (PDTP identity, exact)",
                 alpha_G_from_n, ALPHA_G_PROTON, tol=1.0e-9)

    # H5: Path A -- m_cond from sigma_QCD matches Lambda_QCD within ~1%
    record_ratio("H5", "Path A: m_cond from sigma_QCD ~ Lambda_QCD",
                 M_COND_QCD, LAMBDA_QCD, tol=0.10)

    # H6: Path A -- G_pred from QCD chain is NOT G_known (expect huge ratio)
    G_pred_A = HBAR * C / M_COND_QCD**2
    ratio_G_A = G_pred_A / G
    # H6 PASSES if ratio is huge (confirms hierarchy gap)
    h6_pass = (ratio_G_A > 1.0e35)   # off by at least 10^35
    record_bool("H6", "Path A: G_pred/G_known >> 1 (hierarchy gap ~ 10^40)",
                h6_pass)

    # H7: Path B -- Eddington: n_pred = sqrt(N_Edd) vs n_p (expect large ratio)
    n_edd_pred = np.sqrt(N_EDDINGTON)
    ratio_n_edd = n_edd_pred / N_PROTON   # should be ~7.7e20 (fails badly)
    h7_pass = (ratio_n_edd > 1.0e15)     # confirms Eddington fails
    record_bool("H7", "Path B: Eddington n_pred >> n_p (off by ~10^21)",
                h7_pass)

    # H8: Path B -- Hubble: n_pred = sqrt(t_H/t_P) vs n_p (expect large ratio)
    n_hub_pred = np.sqrt(N_HUBBLE)
    ratio_n_hub = n_hub_pred / N_PROTON   # should be ~2.2e11 (fails)
    h8_pass = (ratio_n_hub > 1.0e5)      # confirms Hubble fails
    record_bool("H8", "Path B: Hubble n_pred != n_p (off by ~10^11)",
                h8_pass)

    # H9: Path C -- Dvali N_required = n_p^2 >> N_SM (confirms circular gap)
    N_required = N_PROTON**2
    ratio_dvali = N_required / N_SM_DOF   # ~ 1.4e36
    h9_pass = (ratio_dvali > 1.0e30)     # confirms species gap
    record_bool("H9", "Path C: Dvali N_required >> N_SM (gap ~ 10^36)",
                h9_pass)

    # H10: Two-parameter count -- R = 1/(n^2 * alpha_EM) needs BOTH alpha_EM AND n
    # Structural: if alpha_EM were 1 (hypothetically), R would be just 1/n^2
    # This test verifies the identity is exact and neither parameter is redundant
    # Check: R * alpha_EM * n_p^2 = 1 AND R * 1 * n_p^2 != 1
    identity_exact = abs(R_PROTON * ALPHA_EM * N_PROTON**2 - 1.0) < 1.0e-9
    identity_without_alpha = abs(R_PROTON * 1.0 * N_PROTON**2 - 1.0) < 0.01
    h10_pass = identity_exact and (not identity_without_alpha)
    record_bool("H10", "Two-param: R needs alpha_EM AND n (both indispensable)",
                h10_pass)

    return results


def print_sudoku_results(rw, results):
    """Print the Sudoku scorecard."""
    rw.subsection("Sudoku Scorecard (H1-H10)")
    passed = 0
    total = len(results)
    for label, desc, value, ok in results:
        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        rw.print("  [{:3s}] {:56s} {}".format(label, desc[:56], status))
    rw.print("")
    rw.print("  Score: {}/{} pass".format(passed, total))
    return passed, total


# ===========================================================================
# PHASE RUNNER
# ===========================================================================

def run_hierarchy_phase(rw, engine):
    """
    Phase 19: Hierarchy Ratio R = alpha_G / alpha_EM.
    Derives the PDTP identity, tests three candidate paths, runs Sudoku tests.
    """
    rw.section("Phase 19 -- Hierarchy Ratio R = alpha_G / alpha_EM (Part 44)")

    rw.print("  QUESTION: Can R = alpha_G / alpha_EM ~ 8e-37 be derived from")
    rw.print("  PDTP lattice topology without using G as input?")
    rw.print("")
    rw.print("  PDTP IDENTITY (PDTP Original):")
    rw.print("    R = 1 / (n^2 * alpha_EM)   where n = m_cond / m_particle")
    rw.print("  Hierarchy problem = winding number problem: WHY is n_p ~ 10^19?")
    rw.print("")

    print_step1_definition(rw)
    print_step2_pdtp_identity(rw)
    print_step3_path_a(rw)
    print_step4_path_b(rw)
    print_step5_path_c(rw)

    results = run_sudoku_tests()
    passed, total = print_sudoku_results(rw, results)

    rw.subsection("Summary")
    rw.print("  RESULT 1 (PDTP Original): R = 1/(n^2 * alpha_EM).")
    rw.print("    The hierarchy problem reduces to ONE dimensionless ratio: n = m_cond/m.")
    rw.print("    Both G and R are determined if n is derived from topology.")
    rw.print("")
    rw.print("  RESULT 2 (negative): No path from pure lattice topology derives n.")
    rw.print("    Path A: m_cond = Lambda_QCD (not m_P); G off by ~ 3.6e39.")
    rw.print("    Path B: Dirac numbers off by 10^11 to 10^21.")
    rw.print("    Path C: Dvali N_species = n^2 is circular (needs G to define N).")
    rw.print("")
    rw.print("  RESULT 3: Two free parameters block the derivation.")
    rw.print("    Need: m_cond (currently undetermined -- exhausted in Parts 33-35)")
    rw.print("    Need: alpha_EM (known from measurement, not derived in PDTP)")
    rw.print("")
    rw.print("  OPEN PATH: Sakharov route (TODO_02) -- determine N_eff from lattice")
    rw.print("  symmetry AND a from breathing mode measurement independently.")
    rw.print("  If both are measured, G follows without circularity.")
    rw.print("")
    rw.print("  Score: {}/{} Sudoku tests pass.".format(passed, total))
    rw.print("")


# ===========================================================================
# STANDALONE RUNNER
# ===========================================================================

if __name__ == "__main__":
    output_dir = os.path.join(_HERE, "outputs")
    rw = ReportWriter(output_dir, label="hierarchy_ratio")
    engine = SudokuEngine()
    run_hierarchy_phase(rw, engine)
    rw.close()
    print("Done. Report written to:", rw.path)




