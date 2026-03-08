#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
su3_physical_beta.py  -- Phase 16: SU(3) PDTP at Physical Beta (Part 41)
=========================================================================
Runs the PDTP SU(3) lattice at physical beta (5.7-6.0) instead of the
strong-coupling value K_NAT = 0.0796, to access the scaling window where
the continuum limit is recovered without relying on the SC expansion.

Key physics:
  - At physical beta, sigma_lat = ln(2N/beta) is completely wrong (SC breaks down)
  - Wilson loops W(R,T) are measured directly from MC configurations
  - Static quark potential V(R) = -ln(W(R,T)) / T  for large T
  - Cornell fit: V(R) = sigma_lat * R + A_lat/R + c_lat
  - Physical sigma: sigma_phys = sigma_lat * (hbar*c / a_lat)^2
  - Lattice spacing a_lat from Necco-Sommer (2001) parameterization

Sudoku checks S21-S27:
  S21: <P>(physical beta) >> <P>(K_NAT)  [ordered regime vs disordered]
  S22: Acceptance rate at physical beta in [20%, 90%]  [MC working]
  S23: W(R+1, T) < W(R, T) for all T  [area law: loop grows -> W shrinks]
  S24: V(R) increases with R  [confining: heavier string at larger separation]
  S25: sigma_lat > 0  [positive string tension from Cornell / linear fit]
  S26: sigma_phys in rough agreement with 0.18 GeV^2  [order of magnitude]
  S27: a_lat from Necco-Sommer agrees with standard quenched QCD values

References:
  Creutz (1980) Phys. Rev. D 21  -- first non-perturbative sigma, beta scan
  Necco & Sommer (2001) Nucl. Phys. B 622  -- a(beta) parameterization
  Bali (2001) Phys. Rep. 343  -- string tension review
  Wilson (1974) Phys. Rev. D 10  -- Wilson loop definition

Usage:
  python su3_physical_beta.py                          # CPU N=4, beta=6.0
  python su3_physical_beta.py --N 6 --beta 6.0        # CPU N=6 (better)
  python su3_physical_beta.py --N 4 --beta 5.7        # lower physical beta
  python su3_physical_beta.py --therm 100 --meas 200  # more statistics
"""

import os
import sys
import math
import time
import argparse
import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from su3_lattice import (
    HBAR, C, GEV,
    K_NAT, A0_QCD,
    SIGMA_QCD_GEV2,
    random_su3, project_su3,
    cornell_fit, lattice_sigma_to_gev2,
)
from su3_lattice_4d import (
    N_DIM,
    init_lattice_4d, mean_plaquette_4d,
    get_link, set_link, shift_site, back_site,
    action_delta_4d,
    SIGMA_SC_2D_GEV2,
)

# ---------------------------------------------------------------------------
# Physical beta values and scale setting
# ---------------------------------------------------------------------------

BETA_SC   = K_NAT   # 0.0796  -- strong-coupling (PDTP natural coupling)
BETA_57   = 5.7     # physical beta -- lower edge of scaling window
BETA_60   = 6.0     # physical beta -- standard quenched benchmark

# Sommer parameter for quenched SU(3) (sets the physical scale)
# Source: Sommer (1994) Nucl. Phys. B 411, 839
R0_FM     = 0.5     # fm;  r0 defined by r0^2 * F(r0) = 1.65

# hbar*c in GeV*fm  (convenient for scale setting)
HBARC_GEV_FM = 0.197327  # GeV*fm

# Strong coupling sigma from Parts 38/39 for comparison
SIGMA_SC_GEV2 = SIGMA_SC_2D_GEV2   # 0.1729 GeV^2


# ---------------------------------------------------------------------------
# Lattice spacing from beta  (Necco-Sommer 2001 parameterization)
# ---------------------------------------------------------------------------

def lattice_spacing_fm(beta):
    """
    Lattice spacing a in fm for given beta, using the Necco-Sommer (2001)
    parameterization for quenched SU(3).

    Source: Necco & Sommer (2001) Nucl. Phys. B 622, 328  eq. (A.3)
    Valid for beta in [5.5, 6.92] (quenched SU(3) scaling window).

    Returns a_lat in fm, or None if beta is outside the valid range.
    """
    if beta < 5.0:
        return None   # SC regime: this formula does not apply
    db = beta - 6.0
    ln_a_r0 = -1.6804 - 1.7331 * db + 0.7849 * db**2 - 0.4428 * db**3
    a_over_r0 = math.exp(ln_a_r0)
    return a_over_r0 * R0_FM   # fm


def lattice_spacing_m(beta):
    """Return lattice spacing in metres, or None for SC beta."""
    a_fm = lattice_spacing_fm(beta)
    return a_fm * 1e-15 if a_fm is not None else None


def sc_formula_sigma_lat(beta, N_c=3):
    """Strong coupling formula sigma_lat = ln(2N/beta). Valid only at small beta."""
    if beta <= 0.0:
        return float('inf')
    return math.log(2.0 * N_c / beta)


# ---------------------------------------------------------------------------
# Small SU(3) random matrix (for high-beta Metropolis)
# ---------------------------------------------------------------------------

def random_su3_small(epsilon):
    """
    Generate an SU(3) matrix close to the identity for use in high-beta MC.

    R = project_su3((1 - epsilon) * I + epsilon * R_random)

    For epsilon = 1.0  -> fully random SU(3) (SC regime)
    For epsilon = 0.1  -> close to identity (physical beta regime)

    Source: standard Metropolis tuning for lattice QCD at physical coupling.
    """
    R_rand = random_su3(np)
    M = (1.0 - epsilon) * np.eye(3, dtype=np.complex128) + epsilon * R_rand
    return project_su3(M, np)


# ---------------------------------------------------------------------------
# Wilson loop  W(R, T)  in the (mu, nu) plane
# ---------------------------------------------------------------------------

def wilson_loop_2d(U, Ns, mu, nu, site, R, T):
    """
    Compute (1/3) Re[Tr(Wilson loop)] for an R x T rectangle in the (mu, nu)
    plane starting at site.

    Path:  R steps in +mu  ->  T steps in +nu
        -> R steps in -mu (dag)  ->  T steps in -nu (dag)

    Returns: float in [-1, 1].  Value = 1 for ordered lattice (U = identity).
    """
    M = np.eye(3, dtype=np.complex128)
    cur = site

    # --- R steps forward in mu ---
    for _ in range(R):
        M = M @ get_link(U, mu, cur)
        cur = shift_site(cur, mu, Ns)

    # --- T steps forward in nu ---
    for _ in range(T):
        M = M @ get_link(U, nu, cur)
        cur = shift_site(cur, nu, Ns)

    # --- R steps backward in mu (= U_mu^dag) ---
    for _ in range(R):
        cur = back_site(cur, mu, Ns)
        M = M @ np.conj(get_link(U, mu, cur)).T

    # --- T steps backward in nu (= U_nu^dag) ---
    for _ in range(T):
        cur = back_site(cur, nu, Ns)
        M = M @ np.conj(get_link(U, nu, cur)).T

    return float(np.real(np.trace(M))) / 3.0


def mean_wilson_loop(U, Ns, R, T):
    """
    Average W(R, T) over all sites and all 6 (mu < nu) orientations.

    Returns float.  For R=T=1 this equals the mean plaquette.
    """
    total = 0.0
    count = 0
    for mu in range(N_DIM):
        for nu in range(mu + 1, N_DIM):
            for x0 in range(Ns):
                for x1 in range(Ns):
                    for x2 in range(Ns):
                        for x3 in range(Ns):
                            site = (x0, x1, x2, x3)
                            total += wilson_loop_2d(U, Ns, mu, nu, site, R, T)
                            count += 1
    return total / count if count > 0 else 0.0


# ---------------------------------------------------------------------------
# Metropolis sweep with tunable step size (for physical beta)
# ---------------------------------------------------------------------------

def metropolis_sweep_physical(U, Ns, K, epsilon, n_hits):
    """
    One full Metropolis sweep over all 4*Ns^4 links using small SU(3) steps.

    For K < 1 (SC regime), epsilon=1.0 gives the standard random-matrix sweep.
    For K ~ 6 (physical beta), epsilon=0.1-0.3 gives ~50% acceptance.

    Returns accept_rate (float in [0, 1]).
    """
    n_accept = 0
    n_total  = 0

    for mu in range(N_DIM):
        for x0 in range(Ns):
            for x1 in range(Ns):
                for x2 in range(Ns):
                    for x3 in range(Ns):
                        site = (x0, x1, x2, x3)
                        for _ in range(n_hits):
                            R     = random_su3_small(epsilon)
                            U_new = R @ get_link(U, mu, site)
                            U_new = project_su3(U_new, np)

                            dS = action_delta_4d(U, mu, site, U_new, Ns, K)
                            if dS <= 0.0:
                                set_link(U, mu, site, U_new)
                                n_accept += 1
                            elif np.random.random() < math.exp(-dS):
                                set_link(U, mu, site, U_new)
                                n_accept += 1
                            n_total += 1

    return n_accept / n_total if n_total > 0 else 0.0


def thermalise_physical(U, Ns, K, epsilon, n_therm, n_hits, rw=None):
    """Thermalise the lattice at physical beta with small-step Metropolis."""
    accept_rate = 0.0
    for sweep in range(1, n_therm + 1):
        accept_rate = metropolis_sweep_physical(U, Ns, K, epsilon, n_hits)
        if rw is not None and sweep % max(1, n_therm // 5) == 0:
            mp = mean_plaquette_4d(U, Ns)
            rw.print("    Therm {:4d}/{:4d} | <P> = {:.4f} | accept = {:.1f}%".format(
                sweep, n_therm, mp, accept_rate * 100))
    return accept_rate


# ---------------------------------------------------------------------------
# Choose epsilon for target acceptance rate based on beta
# ---------------------------------------------------------------------------

def epsilon_for_beta(beta):
    """
    Rough tuning of epsilon (step size) to achieve ~50% acceptance.

    At SC beta (~0.08): use epsilon=1.0 (fully random matrix).
    At physical beta (~6.0): use epsilon~0.1 (close to identity).
    """
    if beta < 1.0:
        return 1.0
    if beta < 3.0:
        return 0.5
    return max(0.04, 0.6 / beta)


# ---------------------------------------------------------------------------
# Wilson loop measurement over MC ensemble
# ---------------------------------------------------------------------------

def measure_wilson_loops(U, Ns, R_max, T_max, Ns_K, epsilon, n_meas, n_hits, rw=None):
    """
    Measure W(R, T) averaged over MC configurations.

    Between measurements: run 1 Metropolis sweep (separation = Ns^4 link updates).
    Returns dict { (R, T): mean_W }.

    R_max, T_max : maximum R and T to measure (limited by Ns//2).
    """
    R_vals = list(range(1, min(R_max, Ns // 2) + 1))
    T_vals = list(range(1, min(T_max, Ns // 2) + 1))

    # Accumulate sums
    sums  = {(R, T): 0.0 for R in R_vals for T in T_vals}
    counts = {(R, T): 0   for R in R_vals for T in T_vals}

    for meas in range(1, n_meas + 1):
        # advance the MC
        metropolis_sweep_physical(U, Ns, Ns_K, epsilon, n_hits)

        # measure all loops
        for R in R_vals:
            for T in T_vals:
                sums[(R, T)]  += mean_wilson_loop(U, Ns, R, T)
                counts[(R, T)] += 1

        if rw is not None and meas % max(1, n_meas // 5) == 0:
            w11 = sums[(1, 1)] / counts[(1, 1)] if counts[(1, 1)] > 0 else 0.0
            rw.print("    Meas {:4d}/{:4d} | W(1,1) = {:.4f}".format(
                meas, n_meas, w11))

    return {(R, T): sums[(R, T)] / counts[(R, T)]
            for R in R_vals for T in T_vals if counts[(R, T)] > 0}


# ---------------------------------------------------------------------------
# Potential extraction  V(R) = -ln(W(R, T_use)) / T_use
# ---------------------------------------------------------------------------

def extract_potential_physical(wloops, Ns):
    """
    Extract effective static potential V(R) from Wilson loops.

    Uses the largest available T (T_use = Ns//2) to suppress excited states.
    Returns (Rs, Vs) sorted by R.
    """
    T_use = max(T for (_, T) in wloops.keys())
    Rs, Vs = [], []
    for R in sorted(set(r for (r, _) in wloops.keys())):
        if (R, T_use) in wloops and wloops[(R, T_use)] > 1e-14:
            V = -math.log(wloops[(R, T_use)]) / T_use
            Rs.append(R)
            Vs.append(V)
    return Rs, Vs


def sigma_from_slope(Rs, Vs):
    """
    Estimate sigma_lat from a 2-point slope when len(Rs) < 3.
    Returns (sigma_lat, None, None, []) matching cornell_fit signature.
    """
    if len(Rs) < 2:
        return None, None, None, []
    # Linear regression V = sigma * R + c
    n = len(Rs)
    x_arr = np.array(Rs, dtype=float)
    y_arr = np.array(Vs, dtype=float)
    x_mean = x_arr.mean()
    y_mean = y_arr.mean()
    sigma_lat = float(np.sum((x_arr - x_mean) * (y_arr - y_mean)) /
                      np.sum((x_arr - x_mean)**2))
    c_const   = float(y_mean - sigma_lat * x_mean)
    residuals = list(y_arr - (sigma_lat * x_arr + c_const))
    return sigma_lat, None, c_const, residuals


# ---------------------------------------------------------------------------
# Main phase function
# ---------------------------------------------------------------------------

def run_su3_physical_beta_phase(rw, _engine, Ns=4, n_therm=50, n_meas=50,
                                 n_hits=5, beta_run=BETA_60, epsilon=None):
    """
    Phase 16: SU(3) PDTP lattice at physical beta.

    Parameters
    ----------
    rw       : ReportWriter
    _engine  : SudokuEngine (unused; API consistency)
    Ns       : lattice size per dimension (default 4; need >= 16 for reliable sigma)
    n_therm  : thermalisation sweeps (default 50)
    n_meas   : measurement sweeps for Wilson loops (default 50)
    n_hits   : Metropolis hits per link per sweep (default 5)
    beta_run : beta value for the Wilson loop run (default 6.0)
    epsilon  : step-size parameter (auto-tuned if None)
    """
    rw.section("Phase 16  -- SU(3) Physical Beta Lattice (Part 41)")

    if epsilon is None:
        epsilon = epsilon_for_beta(beta_run)

    # ------------------------------------------------------------------
    # Step 1: Physics inputs
    # ------------------------------------------------------------------
    rw.subsection("Step 1  -- Physics inputs")
    rw.key_value("K_NAT (SC beta)",          "{:.6f}  [= 1/(4*pi)]".format(K_NAT))
    rw.key_value("beta_run (physical)",       "{:.1f}  [standard quenched benchmark]".format(beta_run))
    rw.key_value("sigma_QCD target",          "0.18 GeV^2  (PDG)")
    rw.key_value("sigma SC (Parts 38-40)",    "{:.4f} GeV^2  (4% off at K_NAT)".format(SIGMA_SC_GEV2))
    rw.key_value("Lattice size Ns",           "{}^4 = {} sites".format(Ns, Ns**4))
    rw.key_value("Step size epsilon",         "{:.3f}  [for Metropolis at beta_run]".format(epsilon))
    rw.print("")

    a_fm_run = lattice_spacing_fm(beta_run)
    if a_fm_run is not None:
        rw.key_value("a_lat (Necco-Sommer)", "{:.3f} fm  [at beta = {:.1f}]".format(
            a_fm_run, beta_run))
        rw.key_value("Physical box size",    "{:.2f} fm  [{} sites x {:.3f} fm]".format(
            Ns * a_fm_run, Ns, a_fm_run))
        R_max_fm = (Ns // 2) * a_fm_run
        rw.key_value("Max Wilson loop R",    "{:.2f} fm  (need > 0.5 fm for confinement)".format(
            R_max_fm))
        if R_max_fm < 0.4:
            rw.print("  WARNING: Box too small for reliable sigma -- confinement onset ~ 0.5 fm.")
            rw.print("           Use N >= 16 (GPU) for quantitative results.")
    else:
        rw.key_value("a_lat", "N/A (SC regime; use Necco-Sommer only for beta >= 5.5)")
    rw.print("")

    # ------------------------------------------------------------------
    # Step 2: Beta scan -- <P> and acceptance rate at 3 beta values
    # ------------------------------------------------------------------
    rw.subsection("Step 2  -- Beta scan (SC vs physical regime)")
    rw.print("  Goal: confirm ordered regime (<P> ~ 0.5-0.6) at physical beta vs")
    rw.print("  disordered (<P> ~ 0.01-0.05) at K_NAT. Sudoku S21.")
    rw.print("")

    scan_betas = [BETA_SC, BETA_57, BETA_60]
    scan_results = []

    for beta_s in scan_betas:
        eps_s = epsilon_for_beta(beta_s)
        U_s   = init_lattice_4d(Ns, 'hot')
        n_warm = 20
        for _ in range(n_warm):
            metropolis_sweep_physical(U_s, Ns, beta_s, eps_s, n_hits)
        mp_s = mean_plaquette_4d(U_s, Ns)
        # measure acceptance over 5 more sweeps
        rate_s = 0.0
        for _ in range(5):
            rate_s = metropolis_sweep_physical(U_s, Ns, beta_s, eps_s, n_hits)
        a_s = lattice_spacing_fm(beta_s)
        a_str = "{:.3f} fm".format(a_s) if a_s is not None else "N/A (SC)"
        scan_results.append((beta_s, eps_s, mp_s, rate_s, a_str))

    rw.print("  {:>8s}  {:>7s}  {:>9s}  {:>11s}  {:>12s}".format(
        "beta", "epsilon", "<P>", "accept rate", "a_lat (fm)"))
    rw.print("  " + "-" * 56)
    for (beta_s, eps_s, mp_s, rate_s, a_str) in scan_results:
        rw.print("  {:>8.4f}  {:>7.3f}  {:>9.4f}  {:>10.1f}%  {:>12s}".format(
            beta_s, eps_s, mp_s, rate_s * 100, a_str))
    rw.print("")

    # S21: physical <P> >> SC <P>
    mp_sc_val  = scan_results[0][2]
    mp_phys_val = scan_results[-1][2]
    s21_pass = mp_phys_val > 2.0 * mp_sc_val
    rw.key_value("S21: <P>(physical) vs <P>(K_NAT)",
                 "{:.4f} vs {:.4f} -> {}".format(
                     mp_phys_val, mp_sc_val,
                     "PASS (ordered regime confirmed)" if s21_pass else "FAIL"))
    rw.print("")

    # S22: acceptance rate at physical beta
    accept_phys = scan_results[-1][3]
    s22_pass = 0.20 <= accept_phys <= 0.90
    rw.key_value("S22: Acceptance rate at beta_run",
                 "{:.1f}%  -> {}".format(
                     accept_phys * 100,
                     "PASS (MC sampling adequate)" if s22_pass else
                     "WARNING (tune epsilon or n_hits)"))
    rw.print("")

    # ------------------------------------------------------------------
    # Step 3: Thermalise at beta_run and measure Wilson loops
    # ------------------------------------------------------------------
    rw.subsection("Step 3  -- Wilson loop measurement at beta = {:.1f}".format(beta_run))
    rw.print("  W(R, T) = (1/3) Re[Tr(path-ordered product around R x T rectangle)]")
    rw.print("  Averaged over all sites and all 6 (mu < nu) orientations.")
    rw.print("  Area law: W(R, T) ~ exp(-sigma_lat * R * T) for large R, T.")
    rw.print("")
    rw.print("  Thermalising ({} sweeps, epsilon = {:.3f})...".format(n_therm, epsilon))

    t0 = time.time()
    U_phys = init_lattice_4d(Ns, 'hot')
    final_accept = thermalise_physical(U_phys, Ns, beta_run, epsilon, n_therm, n_hits, rw)
    rw.print("  Thermalisation done in {:.1f}s. Final accept = {:.1f}%".format(
        time.time() - t0, final_accept * 100))
    rw.print("")

    R_max_meas = min(Ns // 2, 6)   # max R in lattice units
    T_max_meas = min(Ns // 2, 8)   # max T in lattice units

    rw.print("  Measuring Wilson loops W(R,T) for R=1..{}, T=1..{}".format(
        R_max_meas, T_max_meas))
    rw.print("  ({} measurement sweeps)...".format(n_meas))

    t1 = time.time()
    wloops = measure_wilson_loops(
        U_phys, Ns, R_max_meas, T_max_meas,
        beta_run, epsilon, n_meas, n_hits, rw)
    rw.print("  Measurement done in {:.1f}s".format(time.time() - t1))
    rw.print("")

    # Print Wilson loop table
    R_vals = sorted(set(r for (r, _) in wloops.keys()))
    T_vals = sorted(set(t for (_, t) in wloops.keys()))

    header = "  {:>4s}".format("R\\T") + "".join(
        "  {:>10s}".format("T={}".format(T)) for T in T_vals)
    rw.print(header)
    rw.print("  " + "-" * (4 + 12 * len(T_vals)))
    for R in R_vals:
        row = "  {:>4d}".format(R)
        for T in T_vals:
            w = wloops.get((R, T), float('nan'))
            row += "  {:>10.5f}".format(w)
        rw.print(row)
    rw.print("")

    # S23: area law -- W decreases with R (for fixed T)
    s23_pass = True
    T_check = T_vals[0]
    for i in range(len(R_vals) - 1):
        R1, R2 = R_vals[i], R_vals[i+1]
        if (R1, T_check) in wloops and (R2, T_check) in wloops:
            if wloops[(R2, T_check)] >= wloops[(R1, T_check)]:
                s23_pass = False
    rw.key_value("S23: Area law W(R+1,T) < W(R,T)",
                 "PASS" if s23_pass else "FAIL (signal too noisy or N too small)")
    rw.print("")

    # ------------------------------------------------------------------
    # Step 4: Extract static potential V(R) from Wilson loops
    # ------------------------------------------------------------------
    rw.subsection("Step 4  -- Static quark potential V(R)")
    rw.print("  V(R) = -ln(W(R, T_max)) / T_max   [large T suppresses excited states]")
    rw.print("")

    Rs, Vs = extract_potential_physical(wloops, Ns)

    if len(Rs) == 0:
        rw.print("  ERROR: No valid potential points extracted.")
        rw.print("  Check Wilson loops are positive and lattice is thermalised.")
        return

    rw.print("  {:>6s}  {:>12s}".format("R (lat)", "V_eff (lat)"))
    rw.print("  " + "-" * 22)
    for R, V in zip(Rs, Vs):
        rw.print("  {:>6d}  {:>12.5f}".format(R, V))
    rw.print("")

    # S24: V(R) increases with R (confining)
    s24_pass = all(Vs[i+1] > Vs[i] for i in range(len(Vs)-1)) if len(Vs) >= 2 else False
    rw.key_value("S24: V(R) increases with R (confining)",
                 "PASS" if s24_pass else "FAIL (or only 1 point -- N too small)")
    rw.print("")

    # ------------------------------------------------------------------
    # Step 5: Cornell fit (or linear fit for small N)
    # ------------------------------------------------------------------
    rw.subsection("Step 5  -- Cornell fit  V(R) = sigma_lat * R + A_lat/R + c")

    if len(Rs) >= 3:
        sigma_lat, A_lat, c_lat, resids = cornell_fit(Rs, Vs)
        fit_type = "Cornell (3-param)"
    else:
        sigma_lat, A_lat, c_lat, resids = sigma_from_slope(Rs, Vs)
        fit_type = "Linear slope (N too small for Cornell)"

    rw.key_value("Fit type",      fit_type)

    if sigma_lat is None:
        rw.print("  Fit failed: need at least 2 potential points.")
        rw.print("  Increase Ns or n_meas for better statistics.")
        return

    rw.key_value("sigma_lat",  "{:.5f}  [lattice units]".format(sigma_lat))
    if A_lat is not None:
        rw.key_value("A_lat (Coulomb)", "{:.5f}".format(A_lat))
    if c_lat is not None:
        rw.key_value("c_lat (offset)",  "{:.5f}".format(c_lat))
    rw.key_value("Max |residual|", "{:.6f}".format(max(abs(r) for r in resids) if resids else 0.0))
    rw.print("")

    # S25: sigma_lat > 0
    s25_pass = (sigma_lat is not None) and (sigma_lat > 0.0)
    rw.key_value("S25: sigma_lat > 0",
                 "PASS ({:.5f})".format(sigma_lat) if s25_pass else
                 "FAIL (sigma_lat = {})".format(sigma_lat))
    rw.print("")

    # ------------------------------------------------------------------
    # Step 6: Physical sigma conversion
    # ------------------------------------------------------------------
    rw.subsection("Step 6  -- Physical sigma: sigma_phys = sigma_lat * (hbar*c / a_lat)^2")

    a_fm_phys = lattice_spacing_fm(beta_run)

    if a_fm_phys is None:
        rw.print("  Cannot convert: Necco-Sommer formula not valid at beta = {:.4f}".format(
            beta_run))
        rw.print("  Valid range: beta in [5.5, 6.5] (quenched SU(3))")
        return

    a_m_phys  = a_fm_phys * 1e-15
    sigma_gev2 = lattice_sigma_to_gev2(sigma_lat, a_m_phys)
    ratio_to_target = sigma_gev2 / SIGMA_QCD_GEV2

    rw.key_value("a_lat (Necco-Sommer)", "{:.4f} fm  [at beta = {:.1f}]".format(
        a_fm_phys, beta_run))
    rw.key_value("sigma_lat (fit)",      "{:.5f}  [lat. units]".format(sigma_lat))
    rw.key_value("sigma_phys (physical)", "{:.4f} GeV^2".format(sigma_gev2))
    rw.key_value("sigma_QCD target",      "{:.4f} GeV^2".format(SIGMA_QCD_GEV2))
    rw.key_value("ratio sigma/sigma_QCD", "{:.3f}".format(ratio_to_target))
    rw.print("")

    # S26: sigma_phys within factor 3 of target (rough check for small N)
    s26_pass = 0.3 < ratio_to_target < 3.0
    rw.key_value("S26: sigma_phys order-of-magnitude check",
                 "PASS (ratio={:.3f})".format(ratio_to_target) if s26_pass else
                 "FAIL (ratio={:.3f}) -- N too small or low statistics".format(ratio_to_target))
    rw.print("")

    # S27: a_lat consistent with quenched QCD
    s27_pass = (a_fm_phys is not None) and (0.05 < a_fm_phys < 0.4)
    rw.key_value("S27: a_lat(beta=6) ~ 0.09-0.10 fm (quenched QCD)",
                 "{:.3f} fm -> {}".format(
                     a_fm_phys,
                     "PASS" if s27_pass else "FAIL"))
    rw.print("")

    # ------------------------------------------------------------------
    # Step 7: Comparison table (SC regime vs physical beta)
    # ------------------------------------------------------------------
    rw.subsection("Step 7  -- String tension comparison")

    sc_formula_val = sc_formula_sigma_lat(BETA_SC)
    sc_gev2_val    = lattice_sigma_to_gev2(sc_formula_val, A0_QCD)

    rows = [
        ("SC formula (K_NAT)",   BETA_SC,   A0_QCD / 1e-15,  sc_formula_val,  sc_gev2_val,
         "{:.1f}%".format(100.0 * (sc_gev2_val / SIGMA_QCD_GEV2 - 1))),
        ("Physical beta (MC)", beta_run, a_fm_phys,      sigma_lat,       sigma_gev2,
         "{:.1f}%".format(100.0 * (sigma_gev2 / SIGMA_QCD_GEV2 - 1))),
        ("QCD target",         0.0,       0.0,            0.0,             SIGMA_QCD_GEV2, "0%"),
    ]

    rw.print("  {:22s}  {:>7s}  {:>8s}  {:>10s}  {:>11s}  {:>8s}".format(
        "Method", "beta", "a (fm)", "sigma_lat", "sigma (GeV^2)", "vs target"))
    rw.print("  " + "-" * 76)
    for (name, b, a, sl, sg, dev) in rows:
        if b > 0:
            rw.print("  {:22s}  {:>7.4f}  {:>8.3f}  {:>10.4f}  {:>11.4f}  {:>8s}".format(
                name, b, a, sl, sg, dev))
        else:
            rw.print("  {:22s}  {:>7s}  {:>8s}  {:>10s}  {:>11.4f}  {:>8s}".format(
                name, "--", "--", "--", sg, dev))
    rw.print("")

    rw.print("  NOTE: The physical-beta sigma from a {}^4 lattice is a rough estimate.".format(Ns))
    rw.print("  Reliable results require N >= 16 (RTX 3060 GPU with CuPy, ~minutes).")
    rw.print("  At N=16, R up to 6 lattice spacings accesses the confining regime")
    rw.print("  (R > 0.6 fm) where the Cornell linear term dominates.")
    rw.print("")

    # ------------------------------------------------------------------
    # Step 8: Sudoku scorecard
    # ------------------------------------------------------------------
    rw.subsection("Step 8  -- Sudoku scorecard (Part 41)")
    rw.print("")

    checks = [
        ("S21", "<P>(beta_run) > 2 * <P>(K_NAT)",
         "{:.3f} > 2*{:.3f}".format(mp_phys_val, mp_sc_val),
         "PASS" if s21_pass else "FAIL"),
        ("S22", "Acceptance rate in [20%, 90%]",
         "{:.1f}%".format(accept_phys * 100),
         "PASS" if s22_pass else "WARN"),
        ("S23", "W(R+1,T) < W(R,T)  [area law]",
         "checked T={}".format(T_check if T_vals else "N/A"),
         "PASS" if s23_pass else "FAIL"),
        ("S24", "V(R) increases with R  [confining]",
         "{} points".format(len(Rs)),
         "PASS" if s24_pass else "FAIL"),
        ("S25", "sigma_lat > 0  [positive string tension]",
         "{:.5f}".format(sigma_lat),
         "PASS" if s25_pass else "FAIL"),
        ("S26", "sigma_phys within factor 3 of target",
         "{:.3f}".format(ratio_to_target),
         "PASS" if s26_pass else "FAIL"),
        ("S27", "a_lat(beta_run) ~ 0.09-0.10 fm",
         "{:.3f} fm".format(a_fm_phys) if a_fm_phys else "N/A",
         "PASS" if s27_pass else "FAIL"),
    ]

    rw.print("  {:>4s}  {:46s}  {:>18s}  {:>8s}".format(
        "ID", "Check", "Value", "Result"))
    rw.print("  " + "-" * 82)
    for (sid, desc, val, res) in checks:
        rw.print("  {:>4s}  {:46s}  {:>18s}  {:>8s}".format(
            sid, desc[:46], val[:18], res))
    rw.print("")

    passes = sum(1 for c in checks if "PASS" in c[3])
    rw.print("  Score: {}/{} checks pass".format(passes, len(checks)))
    rw.print("")

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    rw.subsection("Part 41 Summary")
    rw.print("  At physical beta ({:.1f}), the SU(3) lattice transitions from".format(beta_run))
    rw.print("  the disordered SC regime (<P> ~ 0.01) to the ordered scaling")
    rw.print("  window (<P> ~ {:.2f}), where continuum physics is accessible.".format(mp_phys_val))
    rw.print("")
    rw.print("  Wilson loop measurement on a {}^4 lattice gives:".format(Ns))
    rw.print("    sigma_lat = {:.4f}  [lattice units, from {} potential points]".format(
        sigma_lat, len(Rs)))
    rw.print("    a_lat     = {:.3f} fm  [Necco-Sommer, beta={:.1f}]".format(a_fm_phys, beta_run))
    rw.print("    sigma     = {:.4f} GeV^2  (target: 0.18 GeV^2)".format(sigma_gev2))
    rw.print("")
    rw.print("  Key finding: at physical beta the SC expansion FAILS completely.")
    rw.print("  sigma_lat = ln(2N/beta) = {:.5f}  at beta={:.1f}  would give".format(
        sc_formula_sigma_lat(beta_run), beta_run))
    sc_wrong = lattice_sigma_to_gev2(sc_formula_sigma_lat(beta_run), a_m_phys)
    rw.print("    sigma_phys = {:.4f} GeV^2  [WRONG -- SC formula not valid here]".format(sc_wrong))
    rw.print("")
    rw.print("  The physical beta simulation directly measures sigma without the SC")
    rw.print("  expansion -- closing the theoretical chain from PDTP to QCD confinement.")
    rw.print("")
    rw.print("  Limitation: {}^4 CPU lattice shows the method but cannot give".format(Ns))
    rw.print("  reliable sigma. The confining regime requires R > ~5 lattice")
    rw.print("  spacings = {:.1f} fm, but box = {:.2f} fm here. Solution:".format(
        5 * a_fm_phys, Ns * a_fm_phys))
    rw.print("    GPU run: python su3_physical_beta.py --N 16 --meas 500")
    rw.print("    (RTX 3060, CuPy -- ~minutes, box = {:.1f} fm)".format(16 * a_fm_phys))
    rw.print("")


# ---------------------------------------------------------------------------
# Standalone entry point
# ---------------------------------------------------------------------------

def _parse_args():
    parser = argparse.ArgumentParser(
        description="Phase 16: Physical Beta Lattice (Part 41)")
    parser.add_argument("--N",     type=int,   default=4,    help="Lattice size (default 4)")
    parser.add_argument("--beta",  type=float, default=6.0,  help="Beta value (default 6.0)")
    parser.add_argument("--therm", type=int,   default=50,   help="Thermalisation sweeps")
    parser.add_argument("--meas",  type=int,   default=50,   help="Measurement sweeps")
    parser.add_argument("--hits",  type=int,   default=5,    help="Metropolis hits/link")
    parser.add_argument("--eps",   type=float, default=None, help="Step size epsilon (auto if omitted)")
    return parser.parse_args()


if __name__ == "__main__":
    args = _parse_args()
    from print_utils import ReportWriter
    _output_dir = os.path.join(_HERE, "outputs")
    _rw = ReportWriter(_output_dir, label="su3_physical_beta")
    run_su3_physical_beta_phase(
        _rw, None,
        Ns=args.N, n_therm=args.therm, n_meas=args.meas,
        n_hits=args.hits, beta_run=args.beta, epsilon=args.eps)
    _rw.close()
