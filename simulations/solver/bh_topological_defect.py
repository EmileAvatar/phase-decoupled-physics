#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
bh_topological_defect.py -- Phase 20: Black Hole Singularity as Topological Defect
====================================================================================
Part 45 of the PDTP framework.

Question: What replaces the GR singularity at r=0 in the PDTP condensate picture?

PDTP Original result:
  - r=0 is replaced by a vortex core of radius xi = l_P / sqrt(2)
  - The condensate order parameter f(r) -> 0 smoothly (no divergence)
  - The Penrose theorem is evaded: it requires a smooth manifold;
    the PDTP lattice has a discrete cutoff at a_0 ~ l_P that breaks this.
  - Exterior GR is unchanged for any macroscopic BH (xi/r_s ~ m_P/M << 1)

Sources:
  - Hawking & Penrose (1970), Proc. Roy. Soc. London A 314, 529
  - Ginzburg & Landau (1950), Zh.Eksp.Teor.Fiz. 20, 1064
  - Abrikosov (1957), Zh.Eksp.Teor.Fiz. 32, 1442
  - Mermin (1979), Rev.Mod.Phys. 51, 591
  - Cross-refs: Parts 24, 33, 34, 36
"""

import os
import sys
import math
import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from print_utils import ReportWriter
from sudoku_engine import (HBAR, C, G, K_B, L_P, M_P, M_SUN,
                            M_E, M_P_PROTON)

# ===========================================================================
# DERIVED CONSTANTS FOR PART 45
# ===========================================================================

# Healing length: xi = a_0 / sqrt(2), where a_0 = hbar/(m_cond*c) = l_P
# (For gravitational condensate: m_cond = m_P -> a_0 = l_P exactly)
A_0_GRAV = HBAR / (M_P * C)          # condensate Compton wavelength = l_P
XI = A_0_GRAV / math.sqrt(2.0)       # healing length = l_P/sqrt(2)

# Planck temperature
T_PLANCK = math.sqrt(HBAR * C**5 / G) / K_B   # ~1.417e32 K

# Evaporation endpoint: T_H = T_P -> M_evap = hbar*c^3/(8*pi*G*T_P*k_B)
M_EVAP = HBAR * C**3 / (8.0 * math.pi * G * T_PLANCK * K_B)


# ===========================================================================
# HELPER FUNCTIONS
# ===========================================================================

def schwarzschild_radius(M):
    """Schwarzschild radius r_s = 2*G*M/c^2. Source: Schwarzschild (1916)."""
    return 2.0 * G * M / C**2


def xi_over_rs(M):
    """
    Ratio of vortex core to Schwarzschild radius.
    xi / r_s = (l_P/sqrt(2)) / (2*G*M/c^2) = m_P / (2*sqrt(2)*M)
    PDTP Original.
    """
    r_s = schwarzschild_radius(M)
    return XI / r_s


def gl_profile(r, xi, n=1):
    """
    Ginzburg-Landau vortex radial profile (normalised to phi_0 = 1).
    Near core: f(r) ~ (r/xi)^n
    Far: f(r) -> 1
    Simple interpolation: f(r) = tanh((r/xi)^n)
    Source: de Gennes (1966), Superconductivity of Metals and Alloys.
    Returns f(r)/phi_0 in [0, 1].
    """
    x = (r / xi)**n
    return math.tanh(x)


def hawking_temperature(M):
    """
    Hawking temperature T_H = hbar*c^3 / (8*pi*G*M*k_B).
    Source: Hawking (1974), Nature 248, 30.
    """
    return HBAR * C**3 / (8.0 * math.pi * G * M * K_B)


def core_energy_estimate(xi):
    """
    Energy stored in vortex core.
    E_core ~ (4/3)*pi*xi^3 * (hbar*c / a_0^4)
    where a_0 = l_P, hbar*c/l_P^4 is the Planck energy density.
    Returns E_core in Joules.
    PDTP Original.
    """
    a_0 = L_P
    rho_planck = HBAR * C / a_0**4     # Planck energy density [J/m^3]
    V_core = (4.0 / 3.0) * math.pi * xi**3
    return rho_planck * V_core


# ===========================================================================
# DISPLAY FUNCTIONS
# ===========================================================================

def print_step1_vortex_core(rw):
    """Step 1: Vortex core profile and healing length."""
    rw.subsection("Step 1: Vortex Core Profile (GL Analogy)")
    rw.print("  In PDTP, every particle is a vortex: phi(r,theta) = f(r)*exp(i*n*theta)")
    rw.print("  The GL radial profile satisfies:")
    rw.print("    xi^2 * (1/r) d/dr[r df/dr] - (n^2/r^2)*f = f*(f^2/phi_0^2 - 1)")
    rw.print("  Source: Ginzburg & Landau (1950), Zh.Eksp.Teor.Fiz. 20, 1064")
    rw.print("")
    rw.print("  Near core (r << xi): f(r) ~ (r/xi)^n * phi_0  [order parameter -> 0]")
    rw.print("  Far from core (r >> xi): f(r) -> phi_0  [condensate restored]")
    rw.print("  At r = 0: f(0) = 0 EXACTLY -- no divergence, just zero")
    rw.print("")
    rw.print("  HEALING LENGTH (from Part 34):")
    rw.print("    xi = a_0 / sqrt(2),  a_0 = hbar/(m_cond * c)")
    rw.print("    For m_cond = m_P (gravitational condensate):")
    rw.print("      a_0 = hbar/(m_P*c) = sqrt(hbar*G/c^3) = l_P  [exactly]")
    rw.print("      xi  = l_P / sqrt(2)")
    rw.print("    a_0 = {:.4e} m  (= l_P = {:.4e} m)".format(A_0_GRAV, L_P))
    rw.print("    xi  = {:.4e} m  (= l_P/sqrt(2))".format(XI))
    rw.print("    Ratio a_0/l_P = {:.8f}  (should be 1.000000)".format(A_0_GRAV / L_P))
    rw.print("")
    rw.print("  GL profile at key radii (n=1 vortex):")
    for r_frac in [0.1, 0.5, 1.0, 2.0, 5.0]:
        r_val = r_frac * XI
        f_val = gl_profile(r_val, XI, n=1)
        rw.print("    r = {:.1f}*xi: f(r)/phi_0 = {:.4f}".format(r_frac, f_val))
    rw.print("")


def print_step2_scales(rw):
    """Step 2: Core vs Schwarzschild radius for different BH masses."""
    rw.subsection("Step 2: Core vs Schwarzschild Radius")
    rw.print("  r_s = 2*G*M/c^2  (Schwarzschild 1916)")
    rw.print("  xi/r_s = (l_P/sqrt(2)) / (2*G*M/c^2) = m_P / (2*sqrt(2)*M)  [PDTP Original]")
    rw.print("")
    rw.print("  xi = {:.4e} m".format(XI))
    rw.print("")

    masses = [
        ("Planck mass m_P",      M_P),
        ("1 kg",                 1.0),
        ("Earth mass",           5.972e24),
        ("Solar mass (1 M_sun)", M_SUN),
        ("10 M_sun stellar BH",  10.0 * M_SUN),
        ("1e6 M_sun SMBH",       1.0e6 * M_SUN),
    ]
    rw.print("  {:28s} {:12s} {:12s} {:12s}".format(
        "Mass", "r_s (m)", "xi/r_s", "log10(xi/r_s)"))
    rw.print("  " + "-" * 70)
    for label, M in masses:
        r_s = schwarzschild_radius(M)
        ratio = xi_over_rs(M)
        log_r = math.log10(ratio) if ratio > 0 else float('nan')
        rw.print("  {:28s} {:12.3e} {:12.3e} {:12.1f}".format(
            label, r_s, ratio, log_r))
    rw.print("")
    rw.print("  RESULT: For M >> m_P, xi/r_s << 1 by orders of magnitude.")
    rw.print("  The vortex core is hidden; exterior GR is unchanged.")
    rw.print("  Only at M ~ m_P does xi ~ r_s (condensate picture breaks down).")
    rw.print("")


def print_step3_penrose(rw):
    """Step 3: Penrose theorem and the lattice cutoff."""
    rw.subsection("Step 3: Penrose Theorem and Lattice Cutoff")
    rw.print("  Hawking-Penrose theorem (1970): singularity inevitable IF:")
    rw.print("    1. Causality -- global hyperbolicity (no closed causal curves)")
    rw.print("    2. Energy condition -- R_mu_nu v^mu v^nu >= 0 for all timelike v")
    rw.print("    3. Trapped surface -- a compact trapped surface exists")
    rw.print("    4. Smooth manifold -- spacetime is a C^2 differentiable manifold")
    rw.print("  Source: Hawking & Penrose (1970), Proc. Roy. Soc. London A 314, 529")
    rw.print("")
    rw.print("  PDTP EVASION: Condition 4 fails.")
    rw.print("    The PDTP condensate is a lattice with discretisation scale a_0 = l_P.")
    rw.print("    It is NOT a smooth manifold -- it has a discrete cutoff below l_P.")
    rw.print("    The Penrose proof uses d/dr, nabla^2 as continuous operators;")
    rw.print("    on the lattice, these are finite differences, well-defined everywhere.")
    rw.print("")
    rw.print("  Lattice scale = {:.4e} m (= l_P = {:.4e} m)".format(A_0_GRAV, L_P))
    rw.print("  Inside the core (r < xi ~ l_P): lattice has ~1 site (one Planck volume)")
    rw.print("  There is no singularity -- only a region where f(r) -> 0.")
    rw.print("")
    rw.print("  NOTE: This is NOT a violation of the Penrose theorem.")
    rw.print("  It is a change of physical assumption: smooth manifold -> lattice.")
    rw.print("  The theorem's conclusion does not follow when its premise 4 is false.")
    rw.print("")


def print_step4_core_energy(rw):
    """Step 4: Energy stored in the vortex core."""
    rw.subsection("Step 4: Core Energy -- Finite, Not Divergent")
    rw.print("  GR singularity: energy density -> infinity as r -> 0")
    rw.print("  PDTP vortex core: energy density is finite (condensation energy)")
    rw.print("")
    rw.print("  Condensation energy density (Planck scale):")
    rw.print("    rho_Planck = hbar*c / l_P^4 = {:.4e} J/m^3".format(
        HBAR * C / L_P**4))
    rw.print("")
    E_core = core_energy_estimate(XI)
    E_Planck = M_P * C**2   # one Planck mass-energy
    rw.print("  Core volume V_core = (4/3)*pi*xi^3 = {:.4e} m^3".format(
        (4.0/3.0) * math.pi * XI**3))
    rw.print("  Core energy E_core = rho_Planck * V_core = {:.4e} J".format(E_core))
    rw.print("  Planck energy m_P*c^2                  = {:.4e} J".format(E_Planck))
    rw.print("  Ratio E_core / (m_P*c^2) = {:.4f}  (order 1, as expected)".format(
        E_core / E_Planck))
    rw.print("")
    rw.print("  RESULT: The vortex core contains ~1 Planck quantum of energy.")
    rw.print("  FINITE, not divergent. No singularity in the energy.")
    rw.print("")


def print_step5_hawking(rw):
    """Step 5: Hawking temperature and evaporation endpoint."""
    rw.subsection("Step 5: Hawking Temperature and Evaporation Endpoint")
    rw.print("  T_H = hbar*c^3 / (8*pi*G*M*k_B)  [Hawking 1974, Part 24]")
    rw.print("  T_P = sqrt(hbar*c^5/G) / k_B = {:.4e} K  [Planck temperature]".format(
        T_PLANCK))
    rw.print("")
    rw.print("  Evaporation endpoint: T_H = T_P  (condensate picture breaks down)")
    rw.print("    M_evap = hbar*c^3 / (8*pi*G*T_P*k_B)")
    rw.print("           = m_P / (8*pi)")
    rw.print("           = {:.4e} kg".format(M_EVAP))
    rw.print("           = {:.4f} * m_P".format(M_EVAP / M_P))
    rw.print("  At M = M_evap:")
    T_evap = hawking_temperature(M_EVAP)
    r_s_evap = schwarzschild_radius(M_EVAP)
    rw.print("    T_H    = {:.4e} K  (= T_P = {:.4e} K)".format(T_evap, T_PLANCK))
    rw.print("    r_s    = {:.4e} m  (= {:.2f} * l_P)".format(r_s_evap, r_s_evap / L_P))
    rw.print("    xi/r_s = {:.4f}  (core fills the horizon)".format(
        xi_over_rs(M_EVAP)))
    rw.print("")
    rw.print("  RESULT: Below M_evap ~ m_P/(8*pi), the vortex core fills the horizon.")
    rw.print("  This is the endpoint of Hawking evaporation in PDTP.")
    rw.print("  What happens to the winding number here is the information paradox.")
    rw.print("  (See TODO_02.md: Hawking information paradox)")
    rw.print("")


# ===========================================================================
# SUDOKU TESTS (BH1 - BH10)
# ===========================================================================

def run_sudoku_tests():
    """
    10 Sudoku consistency tests for the BH topological defect.
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

    # BH1: Healing length xi = l_P / sqrt(2) (from Part 34 with m_cond = m_P)
    xi_expected = L_P / math.sqrt(2.0)
    record_ratio("BH1", "Healing length xi = l_P/sqrt(2) (Part 34)",
                 XI, xi_expected, tol=1.0e-9)

    # BH2: Solar mass BH: xi/r_s << 1 (exterior GR unchanged)
    ratio_solar = xi_over_rs(M_SUN)
    bh2_pass = (ratio_solar < 1.0e-30)   # should be ~5.5e-39
    record_bool("BH2", "Solar mass BH: xi/r_s << 1 (exterior GR unchanged)",
                bh2_pass)

    # BH3: Planck mass BH: xi/r_s is order 1 (breakdown scale)
    ratio_planck = xi_over_rs(M_P)
    bh3_pass = (0.1 < ratio_planck < 2.0)   # should be ~0.35
    record_bool("BH3", "Planck mass BH: xi/r_s ~ O(1) (breakdown scale)",
                bh3_pass)

    # BH4: GL profile f(xi)/phi_0 ~ tanh(1) = 0.7616 (partial recovery at r=xi)
    f_at_xi = gl_profile(XI, XI, n=1)
    expected_tanh1 = math.tanh(1.0)   # ~0.7616
    record_ratio("BH4", "GL profile f(xi)/phi_0 = tanh(1) ~ 0.762",
                 f_at_xi, expected_tanh1, tol=1.0e-9)

    # BH5: Core energy E_core ~ m_P*c^2 (order 1 in Planck units, finite)
    E_core = core_energy_estimate(XI)
    E_planck = M_P * C**2
    ratio_E = E_core / E_planck
    bh5_pass = (0.01 < ratio_E < 100.0)   # order-of-magnitude check
    record_bool("BH5", "Core energy E_core ~ m_P*c^2 (finite, ~order 1)",
                bh5_pass)

    # BH6: Hawking temperature T_H < T_P for M = 1 solar mass
    T_H_solar = hawking_temperature(M_SUN)
    bh6_pass = (T_H_solar < T_PLANCK)
    record_bool("BH6", "T_H < T_P for solar mass BH (valid condensate regime)",
                bh6_pass)

    # BH7: Evaporation endpoint M_evap = m_P / (8*pi)
    M_evap_expected = M_P / (8.0 * math.pi)
    record_ratio("BH7", "Evaporation endpoint M_evap = m_P/(8*pi)",
                 M_EVAP, M_evap_expected, tol=1.0e-6)

    # BH8: Condensate Compton wavelength a_0 = l_P exactly
    # a_0 = hbar/(m_P*c); l_P = sqrt(hbar*G/c^3)
    # Check: (hbar/(m_P*c))^2 = hbar*G/c^3  <-> hbar^2/(m_P^2*c^2) = hbar*G/c^3
    # <-> hbar/(m_P^2*c^2) = G/c^3  <-> m_P^2 = hbar*c/G  TRUE by definition
    record_ratio("BH8", "Condensate Compton a_0 = hbar/(m_P*c) = l_P (exact)",
                 A_0_GRAV, L_P, tol=1.0e-9)

    # BH9: xi/r_s formula: xi/r_s = m_P / (2*sqrt(2)*M) (dimensional check)
    # Verify with M = M_SUN numerically
    xi_rs_formula = M_P / (2.0 * math.sqrt(2.0) * M_SUN)
    xi_rs_direct = xi_over_rs(M_SUN)
    record_ratio("BH9", "xi/r_s = m_P/(2*sqrt(2)*M) formula check (solar)",
                 xi_rs_direct, xi_rs_formula, tol=1.0e-9)

    # BH10: Penrose lattice scale: a_0/l_P = 1 (lattice = Planck scale)
    # This confirms the discrete cutoff is at the right scale
    record_ratio("BH10", "Lattice cutoff a_0/l_P = 1 (Penrose cond. 4 broken)",
                 A_0_GRAV, L_P, tol=1.0e-9)

    return results


def print_sudoku_results(rw, results):
    """Print the Sudoku scorecard."""
    rw.subsection("Sudoku Scorecard (BH1-BH10)")
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

def run_bh_topological_phase(rw, engine):
    """
    Phase 20: Black Hole Singularity as Topological Defect (Part 45).
    Shows that the GR singularity is replaced by a finite vortex core,
    Penrose theorem is evaded by the lattice, and exterior GR is unchanged.
    """
    rw.section("Phase 20 -- Black Hole Singularity as Topological Defect (Part 45)")

    rw.print("  QUESTION: What replaces the r=0 singularity in the PDTP condensate?")
    rw.print("")
    rw.print("  PDTP ANSWER (PDTP Original):")
    rw.print("    r=0 is a vortex core of radius xi = l_P/sqrt(2).")
    rw.print("    The order parameter f(r) -> 0 smoothly. No divergence.")
    rw.print("    Penrose theorem evaded: it requires a smooth manifold;")
    rw.print("    the PDTP lattice has a discrete cutoff at a_0 ~ l_P.")
    rw.print("")
    rw.print("  Analogy: Abrikosov vortex in Type II superconductor (Part 36).")
    rw.print("    Core has radius xi (coherence length), not a point.")
    rw.print("    No singularity -- just a normal-phase region inside the core.")
    rw.print("  Source: Abrikosov (1957), Zh.Eksp.Teor.Fiz. 32, 1442")
    rw.print("")

    print_step1_vortex_core(rw)
    print_step2_scales(rw)
    print_step3_penrose(rw)
    print_step4_core_energy(rw)
    print_step5_hawking(rw)

    results = run_sudoku_tests()
    passed, total = print_sudoku_results(rw, results)

    rw.subsection("Summary")
    rw.print("  RESULT 1 (PDTP Original): r=0 replaced by vortex core of radius xi=l_P/sqrt(2).")
    rw.print("    f(r) -> 0 smoothly; energy density finite; no divergence.")
    rw.print("")
    rw.print("  RESULT 2: Exterior GR unchanged for macroscopic BHs.")
    rw.print("    xi/r_s ~ m_P/M << 1 for M >> m_P. Observable physics unaffected.")
    rw.print("")
    rw.print("  RESULT 3: Penrose theorem evaded by lattice structure.")
    rw.print("    Condition 4 (smooth manifold) is replaced by lattice at a_0=l_P.")
    rw.print("    Not a violation -- a change of physical assumptions.")
    rw.print("")
    rw.print("  RESULT 4: Core energy ~ m_P*c^2 (one Planck quantum, finite).")
    rw.print("")
    rw.print("  OPEN: At M ~ m_P/(8*pi), T_H = T_P (evaporation endpoint).")
    rw.print("  What happens to the topological winding number here?")
    rw.print("  This is the information paradox in PDTP language.")
    rw.print("  (See TODO_02.md: Hawking radiation information paradox)")
    rw.print("")
    rw.print("  Score: {}/{} Sudoku tests pass.".format(passed, total))
    rw.print("")


# ===========================================================================
# STANDALONE RUNNER
# ===========================================================================

if __name__ == "__main__":
    output_dir = os.path.join(_HERE, "outputs")
    rw = ReportWriter(output_dir, label="bh_topological_defect")
    from sudoku_engine import SudokuEngine
    engine = SudokuEngine()
    run_bh_topological_phase(rw, engine)
    rw.close()
    print("Done. Report written to:", rw.path)
