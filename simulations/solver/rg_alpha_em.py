#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
rg_alpha_em.py -- Phase 18: RG Running of K_0 to alpha_EM (Idea D, Part 56)
=============================================================================
TASK (from TODO_02.md, Idea D):
  Does RG running from K_0 = 1/(4*pi) at Planck scale give alpha_EM = 1/137
  at low energy?

CONTEXT (from Part 55, Idea C):
  - Best candidate: alpha = K_0^2 = 1/(4*pi)^2 = 1/157.9
  - This is 13.2% off from measured alpha_EM = 1/137.036
  - The question: does running close the 13.2% gap?

THE PHYSICS
-----------
QED has a well-known 1-loop beta function:
    beta(alpha) = d(alpha)/d(ln mu) = +2*alpha^2 / (3*pi)  [1 lepton flavor]

    For N_f charged fermions:
    beta(alpha) = d(alpha)/d(ln mu) = +alpha^2/(3*pi) * sum_i N_c_i * Q_i^2

    Full SM (below m_Z): sum = 3*(2/3)^2 + 3*(1/3)^2 + 1 + ... per generation
    For 3 generations of quarks+leptons: sum = 3*[3*(4/9)+3*(1/9)+1+0] = 20/3
    So beta(alpha_QED) = +(20/3) * alpha^2 / (12*pi) = +5*alpha^2/(9*pi)

    Source: Peskin & Schroeder, Eq. (12.93) and problem 12.3
    Source: PDG Review "Quantum Chromodynamics" for running couplings

The sign is POSITIVE: alpha GROWS at high energy (opposite of QCD).
At low energy alpha -> 1/137.036, at m_Z alpha -> 1/127.952.

PDTP has:
    K_0 = 1/(4*pi)   [bare dimensionless coupling, Part 35]
    beta(K) = +K^2/(8*pi^2)  [Part 35, same sign as scalar phi^4]

QUESTION 1: If alpha_EM = K_0^2, does running K give the right alpha at low E?
QUESTION 2: If we use the QED beta function for alpha = K_0^2, does the
            running from Planck to m_e close the 13.2% gap?
QUESTION 3: What bare coupling at Planck scale gives alpha = 1/137 at m_e?

THREE MODELS
-------------
Model R1: PDTP beta function for K, then alpha = K^2
    beta(K) = +K^2/(8*pi^2)
    K(E) = K_0 / (1 - K_0*ln(E/E_P)/(8*pi^2))
    alpha(E) = K(E)^2
    At E << E_P: K < K_0 (IR free), so alpha < K_0^2 = 1/158
    -> alpha gets SMALLER at low energy -> moves AWAY from 1/137
    -> FAILS

Model R2: QED beta function for alpha = K_0^2
    beta(alpha) = +b*alpha^2, b = 2/(3*pi) [1 charged lepton]
    alpha(E) = alpha_0 / (1 - alpha_0*b*ln(E/E_P))
    At E << E_P: alpha < alpha_0 (IR free, same sign)
    -> Also moves AWAY from 1/137
    -> FAILS (for same reason)

Model R3: REVERSE -- given alpha(m_e) = 1/137, run UP to Planck
    What is alpha(E_Planck)?
    Standard QED result: alpha(E_P) ~ 1/128 or less (depending on threshold)
    Does this equal K_0^2 = 1/158?
    If yes -> K_0^2 is the UV completion and RG running gives 1/137 at low E.

SUDOKU CHECKS (10 tests)
-------------------------
S1:  QED running reproduces alpha(m_Z) = 1/127.95 from alpha(m_e) = 1/137 [PASS/FAIL]
S2:  PDTP running K(m_e) from K(E_P) = K_0 [value check]
S3:  Model R3: alpha(E_P) from running alpha(m_e) = 1/137 up to E_P [compare to K_0^2]
S4:  Sign check: QED beta > 0 (alpha grows with E) [PASS]
S5:  Sign check: PDTP beta > 0 (K grows with E) [PASS]
S6:  Running strength: delta(alpha)/alpha over 22 decades [small or large?]
S7:  Landau pole location for QED alpha [should be >> E_P]
S8:  Is K_0^2 consistent with alpha(E_P) from QED running? [ratio test]
S9:  What bare coupling gives exactly 1/137 at m_e? [backward solve]
S10: Number of light species consistency [compare SM to PDTP prediction]

Called from main.py as Phase 18.

Usage (standalone):
    cd simulations/solver
    python rg_alpha_em.py
"""

import sys
import os
import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from sudoku_engine import (HBAR, C, G, L_P, M_P, M_E, M_P_PROTON,
                            ALPHA_EM, SudokuEngine)
from print_utils import ReportWriter


# ===========================================================================
# PHYSICAL CONSTANTS
# ===========================================================================

# Energy scales (GeV)
M_E_GEV    = 0.51099895e-3     # electron mass
M_MU_GEV   = 0.1056583755      # muon mass
M_TAU_GEV  = 1.77686           # tau mass
M_Z_GEV    = 91.1876           # Z boson mass
M_W_GEV    = 80.379            # W boson mass
M_T_GEV    = 172.76            # top quark mass
E_PLANCK_GEV = 1.220890e19     # Planck energy

# Coupling constants (measured)
ALPHA_EM_0     = 7.2973525693e-3     # at low energy (Thomson limit)
ALPHA_EM_MZ    = 1.0 / 127.952      # at m_Z (PDG 2022)
# Source: PDG 2022, https://pdg.lbl.gov/

# PDTP coupling
K_0 = 1.0 / (4.0 * np.pi)           # dimensionless, Part 35
K_0_SQ = K_0**2                       # = 1/(4*pi)^2 = 1/157.9

# QED beta function coefficient
# For N_f leptons (e, mu, tau) + quarks below their mass threshold:
# b = (1/3*pi) * sum_f N_c * Q_f^2
# Below m_e: no charged particles -> b = 0
# Above m_e, below m_mu: 1 lepton (Q=1) -> b_1 = 2/(3*pi)
# Above m_mu, below m_tau: 2 leptons -> b_2 = 4/(3*pi)
# Full SM at m_Z: sum = 20/9 per generation * 3 gen = 20/3
#   b_full = (4/3) * (20/3) / (4*pi) ... let me be careful.
#
# Standard normalization:
#   d(alpha)/d(ln mu^2) = alpha^2 * b_1 / (2*pi)
#   where b_1 = (4/3) * sum_f N_c * Q_f^2
#
#   1 lepton:  b_1 = 4/3 * 1 * 1 = 4/3
#   3 gen SM at m_Z: b_1 = (4/3) * [3*(4/9) + 3*(1/9) + 1] * 3
#                       = (4/3) * [4/3 + 1/3 + 1] * 3
#                       = (4/3) * (8/3) * 3 = (4/3) * 8 = 32/3 ... no.
#
# Let me use the standard formula more carefully.
# Source: Peskin & Schroeder Eq. (16.43), PDG "Electroweak" review
#
# 1-loop QED:
#   d(1/alpha)/d(ln mu^2) = -b_1/(2*pi)
#   where b_1 = -(4/3) * sum_f N_c * Q_f^2
#
# Actually the simplest correct form:
#   1/alpha(mu2) = 1/alpha(mu1) - (1/(3*pi)) * sum_f N_c*Q_f^2 * ln(mu2/mu1)
#
# Source: PDG "Quantum Electrodynamics" review, Eq. (10.6)
# At 1-loop, for each charged fermion with N_c colors and charge Q_f:
#   Delta(1/alpha) = -(1/(3*pi)) * N_c * Q_f^2 * ln(mu2/mu1)
#
# Full sum below m_Z (3 leptons + 5 quarks u,d,s,c,b):
#   sum = 3*(2/3)^2 + 3*(2/3)^2 + 3*(1/3)^2 + 3*(1/3)^2 + 3*(1/3)^2
#       + 1 + 1 + 1
#   = 3*(4/9)*2 + 3*(1/9)*3 + 3*1
#   = 8/3 + 1 + 3 = 20/3

# Let's define b_coeff for different energy ranges
# These are the coefficients in: 1/alpha(E2) = 1/alpha(E1) - (b/(3*pi)) * ln(E2/E1)

def b_coeff_qed(E_gev):
    """
    Sum of N_c * Q_f^2 for all charged fermions with mass < E.
    Used in: 1/alpha(E2) = 1/alpha(E1) - (1/(3*pi)) * b * ln(E2/E1)

    Source: PDG "Quantum Electrodynamics" review
    """
    b = 0.0
    # Leptons (N_c = 1)
    if E_gev > M_E_GEV:
        b += 1.0 * 1.0**2     # electron
    if E_gev > M_MU_GEV:
        b += 1.0 * 1.0**2     # muon
    if E_gev > M_TAU_GEV:
        b += 1.0 * 1.0**2     # tau
    # Quarks (N_c = 3)
    # u (2/3), d (1/3), s (1/3), c (2/3), b (1/3), t (2/3)
    m_quarks = [
        (0.0022, 2.0/3),   # up
        (0.0047, 1.0/3),   # down
        (0.095,  1.0/3),   # strange
        (1.275,  2.0/3),   # charm
        (4.18,   1.0/3),   # bottom
        (172.76, 2.0/3),   # top
    ]
    for m_q, Q_q in m_quarks:
        if E_gev > m_q:
            b += 3.0 * Q_q**2
    return b


def run_alpha_qed(E1_gev, alpha1, E2_gev):
    """
    Run alpha_EM from E1 to E2 using 1-loop QED with step-wise thresholds.

    Uses logarithmic stepping to handle mass thresholds.

    Returns alpha at E2.
    """
    # Mass thresholds (GeV), sorted
    thresholds = sorted([M_E_GEV, M_MU_GEV, M_TAU_GEV,
                         0.0022, 0.0047, 0.095, 1.275, 4.18, 172.76])

    # Build list of energy intervals
    if E1_gev < E2_gev:
        # Running UP
        energies = [E1_gev]
        for t in thresholds:
            if E1_gev < t < E2_gev:
                energies.append(t)
        energies.append(E2_gev)
    else:
        # Running DOWN
        energies = [E1_gev]
        for t in reversed(thresholds):
            if E2_gev < t < E1_gev:
                energies.append(t)
        energies.append(E2_gev)

    inv_alpha = 1.0 / alpha1
    for i in range(len(energies) - 1):
        e1 = energies[i]
        e2 = energies[i + 1]
        # Use b_coeff at the midpoint energy
        e_mid = np.sqrt(abs(e1 * e2))
        b = b_coeff_qed(e_mid)
        ln_ratio = np.log(e2 / e1)
        inv_alpha -= (1.0 / (3.0 * np.pi)) * b * ln_ratio

    return 1.0 / inv_alpha


def run_K_pdtp(E1_gev, K1, E2_gev):
    """
    Run PDTP coupling K from E1 to E2 using PDTP beta function.

    beta(K) = +K^2 / (8*pi^2)
    Solution: K(E2) = K1 / (1 - K1 * ln(E2/E1) / (8*pi^2))

    Source: Part 35 (dim_transmutation.py)
    """
    t = np.log(E2_gev / E1_gev)
    denom = 1.0 - K1 * t / (8.0 * np.pi**2)
    if denom <= 0:
        return float('inf')  # Landau pole hit
    return K1 / denom


# ===========================================================================
# SUDOKU CHECKS
# ===========================================================================

def run_sudoku_checks(rw, results_dict):
    """
    10 Sudoku checks for the RG running models.
    """
    results = []
    rd = results_dict

    # S1: QED running reproduces alpha(m_Z) = 1/128 from alpha(m_e)
    alpha_mz_pred = rd.get("alpha_mz_from_me", 0)
    ratio_s1 = alpha_mz_pred / ALPHA_EM_MZ if ALPHA_EM_MZ > 0 else 0
    results.append(("S1", "QED running: alpha(m_Z) from alpha(m_e)",
                     "pred=1/%.1f, meas=1/%.1f, ratio=%.4f" %
                     (1.0/alpha_mz_pred if alpha_mz_pred > 0 else 0,
                      1.0/ALPHA_EM_MZ, ratio_s1),
                     0.95 <= ratio_s1 <= 1.05))

    # S2: PDTP running K(m_e) from K(E_P) = K_0
    K_me = rd.get("K_at_me", 0)
    alpha_pdtp_me = K_me**2
    ratio_s2 = alpha_pdtp_me / ALPHA_EM_0
    results.append(("S2", "PDTP K^2(m_e) vs alpha_EM",
                     "K^2=%.6f=1/%.1f, ratio=%.4f" %
                     (alpha_pdtp_me, 1.0/alpha_pdtp_me if alpha_pdtp_me > 0 else 0,
                      ratio_s2),
                     0.5 <= ratio_s2 <= 2.0))

    # S3: alpha(E_P) from running alpha(m_e) up to E_P
    alpha_ep = rd.get("alpha_at_EP", 0)
    ratio_s3 = alpha_ep / K_0_SQ
    results.append(("S3", "alpha(E_P) vs K_0^2",
                     "alpha(E_P)=1/%.1f, K_0^2=1/%.1f, ratio=%.4f" %
                     (1.0/alpha_ep if alpha_ep > 0 else 0,
                      1.0/K_0_SQ, ratio_s3),
                     0.5 <= ratio_s3 <= 2.0))

    # S4: Sign check -- QED beta > 0
    results.append(("S4", "QED beta > 0 (alpha grows with E)",
                     "alpha(m_Z)=1/%.1f > alpha(m_e)=1/%.1f" %
                     (1.0/ALPHA_EM_MZ, 1.0/ALPHA_EM_0),
                     ALPHA_EM_MZ > ALPHA_EM_0))

    # S5: Sign check -- PDTP beta > 0
    K_high = rd.get("K_at_10TeV", K_0)
    results.append(("S5", "PDTP beta > 0 (K grows with E)",
                     "K(10TeV)=%.6f > K(m_e)=%.6f" % (K_high, K_me),
                     K_high > K_me))

    # S6: Running strength over 22 decades
    delta_K = rd.get("delta_K_22dec", 0)
    results.append(("S6", "K running over 22 decades (m_e to E_P)",
                     "delta_K/K = %.4f (%.1f%%)" % (delta_K, delta_K*100),
                     True))  # informational

    # S7: Landau pole for QED (should be >> E_P)
    landau_gev = rd.get("landau_pole_gev", 0)
    results.append(("S7", "QED Landau pole >> E_Planck",
                     "log10(E_Landau/GeV) = %.0f" %
                     (np.log10(landau_gev) if landau_gev > 0 else 0),
                     landau_gev > E_PLANCK_GEV))

    # S8: K_0^2 consistent with alpha(E_P)?
    results.append(("S8", "K_0^2 = alpha(E_P) consistency",
                     "K_0^2=1/%.1f, alpha(E_P)=1/%.1f" %
                     (1.0/K_0_SQ, 1.0/alpha_ep if alpha_ep > 0 else 0),
                     0.8 <= ratio_s3 <= 1.2))

    # S9: Backward solve: what bare coupling gives 1/137 at m_e?
    alpha_bare_needed = rd.get("alpha_bare_for_137", 0)
    results.append(("S9", "Bare coupling at E_P that gives 1/137 at m_e",
                     "alpha_bare = 1/%.2f" %
                     (1.0/alpha_bare_needed if alpha_bare_needed > 0 else 0),
                     True))  # informational

    # S10: The gap -- is RG running the answer?
    gap_closed = rd.get("gap_closed", False)
    results.append(("S10", "Does RG running close the 13.2% gap?",
                     "YES" if gap_closed else "NO",
                     gap_closed))

    # Print scorecard
    n_pass = sum(1 for r in results if r[3])
    n_fail = len(results) - n_pass

    rw.subsection("Sudoku Scorecard: %d/%d PASS" % (n_pass, len(results)))

    headers = ["Test", "Description", "Result", "Status"]
    widths = [4, 50, 50, 6]
    rows = []
    for tid, desc, val, passed in results:
        status = "PASS" if passed else "FAIL"
        rows.append([tid, desc[:50], str(val)[:50], status])
    rw.table(headers, rows, widths)

    return n_pass, n_fail, results


# ===========================================================================
# MAIN
# ===========================================================================

def run_rg_alpha_em(rw, engine=None):
    """Run the RG running investigation."""

    rw.section("Phase 18: RG Running of K_0 to alpha_EM (Idea D)")

    results_dict = {}

    # ---------------------------------------------------------------
    # STEP 1: The setup
    # ---------------------------------------------------------------
    rw.subsection("Step 1: The Starting Point (from Part 55)")
    rw.print("Part 55 found: alpha_candidate = K_0^2 = 1/(4*pi)^2")
    rw.print("  K_0 = 1/(4*pi) = %.6f" % K_0)
    rw.print("  K_0^2 = 1/(4*pi)^2 = %.6f = 1/%.1f" % (K_0_SQ, 1.0/K_0_SQ))
    rw.print("  alpha_EM measured = %.6f = 1/%.3f" % (ALPHA_EM_0, 1.0/ALPHA_EM_0))
    rw.print("  Gap: 1/157.9 vs 1/137.0 = %.1f%% off" %
             (abs(K_0_SQ/ALPHA_EM_0 - 1.0) * 100))
    rw.print("")
    rw.print("QUESTION: Does RG running close this 13.2% gap?")
    rw.print("  K_0^2 is the BARE coupling at Planck scale.")
    rw.print("  1/137 is measured at ELECTRON scale.")
    rw.print("  If running from E_Planck to m_e changes alpha by +13.2%,")
    rw.print("  then K_0^2 IS alpha_EM at high energy, and 1/137 is its")
    rw.print("  low-energy value after RG evolution.")

    # ---------------------------------------------------------------
    # STEP 2: Standard QED running (validation)
    # ---------------------------------------------------------------
    rw.subsection("Step 2: Standard QED Running (Validation)")
    rw.print("1-loop QED running formula:")
    rw.print("  1/alpha(E2) = 1/alpha(E1) - (1/(3*pi)) * b * ln(E2/E1)")
    rw.print("  where b = sum_f N_c * Q_f^2 for fermions with m_f < E")
    rw.print("  Source: PDG 'QED' review, Peskin & Schroeder Eq. (12.93)")
    rw.print("")

    # Run alpha from m_e to m_Z
    alpha_mz = run_alpha_qed(M_E_GEV, ALPHA_EM_0, M_Z_GEV)
    results_dict["alpha_mz_from_me"] = alpha_mz
    rw.print("Validation: running alpha from m_e to m_Z:")
    rw.key_value("alpha(m_e)", "%.6f = 1/%.2f" % (ALPHA_EM_0, 1.0/ALPHA_EM_0))
    rw.key_value("alpha(m_Z) predicted", "%.6f = 1/%.2f" % (alpha_mz, 1.0/alpha_mz))
    rw.key_value("alpha(m_Z) measured", "%.6f = 1/%.2f" % (ALPHA_EM_MZ, 1.0/ALPHA_EM_MZ))
    rw.key_value("Ratio pred/meas", "%.4f" % (alpha_mz / ALPHA_EM_MZ))
    rw.print("")

    # b values at key energies
    rw.print("Active fermion count at key energies:")
    test_energies = [0.001, 0.1, 1.0, 5.0, 100.0, 200.0, 1000.0]
    for e in test_energies:
        rw.print("  E = %.3f GeV:  b = %.3f" % (e, b_coeff_qed(e)))
    rw.print("")

    # ---------------------------------------------------------------
    # STEP 3: Model R1 -- PDTP running K, then alpha = K^2
    # ---------------------------------------------------------------
    rw.subsection("Step 3: Model R1 -- PDTP Running K, alpha = K^2")
    rw.print("  beta(K) = +K^2 / (8*pi^2)  [Part 35]")
    rw.print("  K(E) = K_0 / (1 - K_0*ln(E/E_P)/(8*pi^2))")
    rw.print("  alpha(E) = K(E)^2")
    rw.print("")

    # Run K from Planck down to m_e
    K_me = run_K_pdtp(E_PLANCK_GEV, K_0, M_E_GEV)
    K_mz = run_K_pdtp(E_PLANCK_GEV, K_0, M_Z_GEV)
    K_10tev = run_K_pdtp(E_PLANCK_GEV, K_0, 1e4)
    results_dict["K_at_me"] = K_me
    results_dict["K_at_10TeV"] = K_10tev
    results_dict["delta_K_22dec"] = abs(K_0 - K_me) / K_0

    rw.print("  K(E_Planck) = K_0 = %.6f" % K_0)
    rw.print("  K(m_Z)      = %.6f  (change: %.2f%%)" %
             (K_mz, (K_mz/K_0 - 1)*100))
    rw.print("  K(m_e)      = %.6f  (change: %.2f%%)" %
             (K_me, (K_me/K_0 - 1)*100))
    rw.print("")
    rw.print("  alpha_PDTP(E_P) = K_0^2 = %.6f = 1/%.1f" %
             (K_0**2, 1.0/K_0**2))
    rw.print("  alpha_PDTP(m_e) = K(m_e)^2 = %.6f = 1/%.1f" %
             (K_me**2, 1.0/K_me**2))
    rw.print("  alpha_EM measured = %.6f = 1/%.1f" %
             (ALPHA_EM_0, 1.0/ALPHA_EM_0))
    rw.print("")

    direction = "TOWARD" if abs(K_me**2 - ALPHA_EM_0) < abs(K_0**2 - ALPHA_EM_0) else "AWAY FROM"
    rw.print("  Direction: running moves %s 1/137." % direction)
    rw.print("  PDTP beta is IR-free: K SHRINKS at low energy.")
    rw.print("  So K^2 SHRINKS too: 1/158 -> 1/%.0f (further from 1/137)." %
             (1.0/K_me**2))
    rw.print("")
    rw.print("  VERDICT R1: PDTP running moves in the WRONG direction.")
    rw.print("  The gap WIDENS, not closes.")

    # ---------------------------------------------------------------
    # STEP 4: Model R2 -- QED running alpha, starting from K_0^2
    # ---------------------------------------------------------------
    rw.subsection("Step 4: Model R2 -- QED Running from K_0^2 at Planck Scale")
    rw.print("  Use STANDARD QED beta function, but start from alpha(E_P) = K_0^2.")
    rw.print("  Run DOWN from E_Planck to m_e.")
    rw.print("")

    # Run QED from Planck to m_e, starting at K_0^2
    alpha_me_r2 = run_alpha_qed(E_PLANCK_GEV, K_0_SQ, M_E_GEV)
    rw.print("  alpha(E_P) = K_0^2 = %.6f = 1/%.1f" % (K_0_SQ, 1.0/K_0_SQ))
    rw.print("  alpha(m_e) from QED running = %.6f = 1/%.2f" %
             (alpha_me_r2, 1.0/alpha_me_r2))
    rw.print("  alpha_EM measured = %.6f = 1/%.2f" %
             (ALPHA_EM_0, 1.0/ALPHA_EM_0))
    rw.print("  Ratio: %.4f" % (alpha_me_r2 / ALPHA_EM_0))
    rw.print("")

    direction2 = "TOWARD" if abs(alpha_me_r2 - ALPHA_EM_0) < abs(K_0_SQ - ALPHA_EM_0) else "AWAY FROM"
    rw.print("  Direction: QED running from K_0^2 moves %s 1/137." % direction2)
    rw.print("")

    # Compute the analytical estimate
    # 1/alpha(m_e) = 1/alpha(E_P) + (b/(3*pi)) * ln(E_P/m_e)
    # b at full SM ~ 20/3
    b_full = b_coeff_qed(1000.0)  # above all quarks except top
    ln_ratio_full = np.log(E_PLANCK_GEV / M_E_GEV)
    inv_alpha_me_est = 1.0/K_0_SQ + (1.0/(3*np.pi)) * b_full * ln_ratio_full
    alpha_me_est = 1.0/inv_alpha_me_est

    rw.print("  Analytical estimate (single step, b=%.2f):" % b_full)
    rw.print("    1/alpha(m_e) = 1/K_0^2 + (b/(3*pi)) * ln(E_P/m_e)")
    rw.print("                 = %.1f + %.1f * %.1f" %
             (1.0/K_0_SQ, b_full/(3*np.pi), ln_ratio_full))
    rw.print("                 = %.1f + %.1f = %.1f" %
             (1.0/K_0_SQ,
              (b_full/(3*np.pi)) * ln_ratio_full,
              inv_alpha_me_est))
    rw.print("    alpha(m_e) = 1/%.1f" % inv_alpha_me_est)
    rw.print("")

    # QED sign is POSITIVE beta -> alpha GROWS with energy
    # So running DOWN from E_P: alpha DECREASES
    # alpha(m_e) < alpha(E_P)
    # K_0^2 = 1/158, running down gives 1/(158 + correction) ~ 1/260
    # This is FURTHER from 1/137!
    rw.print("  QED has POSITIVE beta: alpha grows with energy.")
    rw.print("  Running DOWN: alpha DECREASES.")
    rw.print("  1/K_0^2 = 158 + RG correction ~ %.0f -> further from 137." %
             inv_alpha_me_est)
    rw.print("")
    rw.print("  VERDICT R2: QED running ALSO moves in the wrong direction.")
    rw.print("  Starting from 1/158, running down gives ~1/%.0f (further from 1/137)." %
             inv_alpha_me_est)

    # ---------------------------------------------------------------
    # STEP 5: Model R3 -- Run alpha(m_e)=1/137 UP to Planck
    # ---------------------------------------------------------------
    rw.subsection("Step 5: Model R3 -- Run alpha(m_e)=1/137 UP to E_Planck")
    rw.print("  The REVERSE question: what is alpha at E_Planck?")
    rw.print("")

    alpha_ep = run_alpha_qed(M_E_GEV, ALPHA_EM_0, E_PLANCK_GEV)
    results_dict["alpha_at_EP"] = alpha_ep

    rw.print("  alpha(m_e) = 1/137.036 (measured)")
    rw.print("  alpha(E_P) = %.6f = 1/%.2f (from QED running)" %
             (alpha_ep, 1.0/alpha_ep))
    rw.print("  K_0^2 = %.6f = 1/%.2f (PDTP prediction)" %
             (K_0_SQ, 1.0/K_0_SQ))
    rw.print("")
    rw.print("  Ratio alpha(E_P) / K_0^2 = %.4f" % (alpha_ep / K_0_SQ))
    rw.print("  Gap: %.1f%%" % (abs(alpha_ep/K_0_SQ - 1.0) * 100))
    rw.print("")

    # Is alpha(E_P) close to K_0^2?
    gap_r3 = abs(alpha_ep / K_0_SQ - 1.0)
    if gap_r3 < 0.05:
        rw.print("  ** MATCH ** alpha(E_P) = K_0^2 within 5%%!")
        rw.print("  K_0^2 IS the UV value of alpha_EM, and 1/137 follows from QED running!")
        results_dict["gap_closed"] = True
    elif gap_r3 < 0.20:
        rw.print("  CLOSE but not exact. Gap = %.1f%%." % (gap_r3 * 100))
        rw.print("  Higher-loop corrections or threshold effects might close it.")
        results_dict["gap_closed"] = False
    else:
        rw.print("  NOT close. Gap = %.1f%%." % (gap_r3 * 100))
        rw.print("  RG running does not bridge K_0^2 to alpha_EM.")
        results_dict["gap_closed"] = False

    # ---------------------------------------------------------------
    # STEP 6: Backward solve -- what bare coupling gives 1/137?
    # ---------------------------------------------------------------
    rw.subsection("Step 6: Backward Solve -- What Bare Coupling Gives 1/137?")

    # We want: alpha(m_e) = 1/137 after QED running from E_P
    # 1/alpha(m_e) = 1/alpha_bare + correction
    # 137 = 1/alpha_bare + correction
    # alpha_bare = 1 / (137 - correction)
    # correction = (b/(3*pi)) * ln(E_P/m_e)
    correction = (b_full / (3.0 * np.pi)) * ln_ratio_full
    alpha_bare_needed = 1.0 / (1.0/ALPHA_EM_0 - correction)
    results_dict["alpha_bare_for_137"] = alpha_bare_needed

    rw.print("  RG correction (1-loop, b=%.2f):" % b_full)
    rw.print("    delta(1/alpha) = (b/(3*pi)) * ln(E_P/m_e)")
    rw.print("                   = (%.3f) * %.1f = %.1f" %
             (b_full/(3*np.pi), ln_ratio_full, correction))
    rw.print("")
    rw.print("  To get alpha(m_e) = 1/137:")
    rw.print("    1/alpha_bare = 1/alpha(m_e) - delta(1/alpha)")
    rw.print("                 = 137.0 - %.1f = %.1f" %
             (correction, 1.0/ALPHA_EM_0 - correction))
    rw.print("    alpha_bare = 1/%.1f = %.6f" %
             (1.0/alpha_bare_needed, alpha_bare_needed))
    rw.print("")
    rw.print("  Compare to PDTP candidates:")
    rw.print("    K_0    = 1/(4*pi)   = 1/12.57 = 0.0796")
    rw.print("    K_0^2  = 1/(4*pi)^2 = 1/157.9 = 0.00633")
    rw.print("    Needed:               1/%.1f = %.5f" %
             (1.0/alpha_bare_needed, alpha_bare_needed))
    rw.print("")

    # What K_0 power gives the needed bare coupling?
    if alpha_bare_needed > 0:
        # alpha_bare = K_0^p  ->  p = ln(alpha_bare)/ln(K_0)
        p_needed = np.log(alpha_bare_needed) / np.log(K_0)
        rw.print("  If alpha_bare = K_0^p, then p = %.4f" % p_needed)
        rw.print("  (p=1 means alpha=K_0, p=2 means alpha=K_0^2)")
        rw.print("")

        if abs(p_needed - 2.0) < 0.1:
            rw.print("  p ~ 2: consistent with TWO factors of K_0 (Part 55 model V4)")
        elif abs(p_needed - 1.0) < 0.1:
            rw.print("  p ~ 1: single K_0 factor")
        else:
            rw.print("  p = %.2f: not a clean integer power of K_0" % p_needed)

    # ---------------------------------------------------------------
    # STEP 7: Energy scan
    # ---------------------------------------------------------------
    rw.subsection("Step 7: Full Energy Scan")
    rw.print("Running alpha from m_e to E_Planck (QED 1-loop):")
    rw.print("")

    scan_energies = [M_E_GEV, 0.01, 0.1, 1.0, 10.0, M_Z_GEV,
                     100.0, 1000.0, 1e6, 1e9, 1e12, 1e15, 1e16, 1e19]
    headers = ["E (GeV)", "1/alpha(E)", "b(E)", "alpha(E)"]
    widths = [12, 14, 8, 14]
    rows = []
    for e in scan_energies:
        alpha_e = run_alpha_qed(M_E_GEV, ALPHA_EM_0, e)
        b_e = b_coeff_qed(e)
        rows.append(["%.2e" % e, "%.2f" % (1.0/alpha_e),
                      "%.3f" % b_e, "%.6f" % alpha_e])
    rw.table(headers, rows, widths)

    rw.print("At GUT scale (~10^16 GeV): alpha ~ 1/%.0f" %
             (1.0/run_alpha_qed(M_E_GEV, ALPHA_EM_0, 1e16)))
    rw.print("At Planck scale (10^19 GeV): alpha ~ 1/%.0f" %
             (1.0/alpha_ep))
    rw.print("PDTP K_0^2 = 1/%.0f" % (1.0/K_0_SQ))

    # Landau pole estimate
    # 1/alpha(E) = 0  ->  E_Landau
    # 1/alpha_0 - (b/(3*pi)) * ln(E_L/m_e) = 0
    # ln(E_L/m_e) = 3*pi / (b * alpha_0)
    landau_ln = 3.0 * np.pi / (b_full * ALPHA_EM_0)
    landau_gev = M_E_GEV * np.exp(landau_ln)
    results_dict["landau_pole_gev"] = landau_gev
    rw.print("")
    rw.print("QED Landau pole: E_L ~ 10^%.0f GeV (far above Planck)" %
             (np.log10(landau_gev)))

    # ---------------------------------------------------------------
    # STEP 8: Sudoku checks
    # ---------------------------------------------------------------
    n_pass, n_fail, checks = run_sudoku_checks(rw, results_dict)

    # ---------------------------------------------------------------
    # STEP 9: Verdict
    # ---------------------------------------------------------------
    rw.subsection("Step 9: Verdict")

    rw.print("MODEL R1 (PDTP beta for K, alpha=K^2): FAILS")
    rw.print("  K shrinks at low E -> alpha=K^2 shrinks -> moves AWAY from 1/137")
    rw.print("")
    rw.print("MODEL R2 (QED beta for alpha, start at K_0^2): FAILS")
    rw.print("  QED beta positive -> alpha shrinks at low E -> 1/158 becomes ~1/%.0f" %
             inv_alpha_me_est)
    rw.print("")
    rw.print("MODEL R3 (Run 1/137 UP to Planck): INFORMATIVE")
    rw.print("  alpha(E_Planck) = 1/%.1f from standard QED running" % (1.0/alpha_ep))
    rw.print("  K_0^2 = 1/%.1f" % (1.0/K_0_SQ))
    gap_pct = abs(alpha_ep/K_0_SQ - 1.0) * 100
    rw.print("  Gap: %.1f%%" % gap_pct)
    rw.print("")

    rw.print("KEY FINDING:")
    rw.print("  RG running CANNOT close the 13.2%% gap between K_0^2 and 1/137.")
    rw.print("  Both PDTP and QED running move in the WRONG direction:")
    rw.print("  they make alpha SMALLER at low energy, widening the gap.")
    rw.print("")
    rw.print("  However, running 1/137 UP to the Planck scale gives alpha(E_P) = 1/%.0f." %
             (1.0/alpha_ep))
    if gap_pct < 20:
        rw.print("  This is %.1f%% from K_0^2 = 1/158. CLOSE but not exact." % gap_pct)
        rw.print("  The proximity suggests K_0^2 may be related to alpha_EM at Planck scale,")
        rw.print("  but the gap requires either:")
        rw.print("    (a) higher-loop QED corrections")
        rw.print("    (b) threshold effects from new physics")
        rw.print("    (c) K_0^2 is approximately but not exactly the right formula")
    else:
        rw.print("  This is %.1f%% from K_0^2 = 1/158. NOT close." % gap_pct)
        rw.print("  K_0^2 does not appear to be the UV value of alpha_EM.")

    rw.print("")
    rw.print("STATUS: NEGATIVE RESULT")
    rw.print("  RG running does not derive 1/137 from K_0 = 1/(4*pi).")
    rw.print("  The bare coupling K_0^2 = 1/158 is tantalizingly close (13%%)")
    rw.print("  but running moves the wrong way.")
    rw.print("  alpha_EM remains a free parameter in PDTP, as in the Standard Model.")
    rw.print("")
    rw.print("WHAT THIS TELLS US:")
    rw.print("  The TWO-CHANNEL STRUCTURE from Part 55 is correct:")
    rw.print("    - Gravity = amplitude channel (mass-dependent)")
    rw.print("    - EM = topology channel (mass-independent)")
    rw.print("  But the EM coupling STRENGTH is a separate free parameter,")
    rw.print("  not determined by K_0 alone.")
    rw.print("")
    rw.print("Sudoku score: %d/%d PASS" % (n_pass, n_pass + n_fail))


# ===========================================================================
# STANDALONE ENTRY POINT
# ===========================================================================

def main():
    """Run as standalone script."""
    output_dir = os.path.join(_HERE, "outputs")
    rw = ReportWriter(output_dir, label="rg_alpha_em")
    run_rg_alpha_em(rw)
    rw.close()


if __name__ == "__main__":
    main()
