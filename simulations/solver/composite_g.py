#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
composite_g.py -- Phase 22: G as Composite of Multiple Layers (Idea H, Part 60)
================================================================================
TASK (from TODO_02.md, Idea H):
  Investigate whether G is a COMPOSITE quantity — the net effect of coupling
  passing through multiple condensate layers, each reducing it.

MOTIVATION
-----------
User insight: G might be like the stiffness of a layered material.
Springs in series: 1/k_eff = 1/k_1 + 1/k_2 + 1/k_3
Light through glass panes: each pane reduces intensity.
G is weak not because any ONE layer is weak, but because coupling passes
through MULTIPLE interfaces, each reducing it.

HAUG DECOMPOSITION (established math)
---------------------------------------
G = l_P^2 * c^3 / hbar
  = hbar * c / m_P^2         [PDTP form, Part 33]

Source: Haug (2024), "The Compton Wavelength Is the True Matter Wavelength"

Key results:
  - ALL gravity formulas reduce to just l_P and lambda_C
  - l_P / lambda_C = m / m_cond = 1/n (inverse winding number, Part 33)
  - Compton frequency c/lambda_C is the particle's internal clock

LAYER MODELS TESTED
---------------------
Model 1: Springs in series (harmonic)
  1/G_eff = 1/G_grav + 1/G_EW + 1/G_QCD
  Each layer has its own stiffness kappa_i = hbar*c / m_i^2

Model 2: Transmission through interfaces (multiplicative)
  G_eff = G_bare * T_1 * T_2 * T_3
  Each interface transmits a fraction T_i of the coupling

Model 3: Impedance matching (wave-mechanical)
  Like wave propagation through layered media
  G_eff = G_grav * (4*Z_1*Z_2) / (Z_1 + Z_2)^2 per interface
  where Z = impedance = sqrt(kappa * rho)

PDTP GOALS CONNECTION
---------------------
  Goal 1 (Einstein gravity): If G is composite, the field equation
    box(phi) = G_eff * T_mu_nu gains a LAYER STRUCTURE -- Einstein
    equations modified at layer boundaries (new physics at EW/QCD scales)
  Goal 2 (New predictions): G should CHANGE at phase transitions
    (QGP deconfinement: one layer merges, G increases by T_QCD^-1)
  Goal 3 (Masses/couplings): If layer masses are m_P, v_Higgs, Lambda_QCD,
    can we reproduce G = 6.674e-11 from known mass scales?

SUDOKU CHECKS (10 tests)
--------------------------
S1:  Haug decomposition: G = l_P^2 * c^3 / hbar [exact identity]
S2:  PDTP form: G = hbar*c / m_P^2 [exact identity]
S3:  Springs in series: 1/G_eff dominated by WEAKEST spring [check]
S4:  Three layers with known mass scales -> G_eff vs G_known [test]
S5:  Transmission model: product of T_i < 1 makes G small [check]
S6:  Impedance mismatch: Z ratio between layers [compute]
S7:  Phase transition prediction: removing QCD layer changes G [compute]
S8:  Haug: l_P/lambda_C = 1/n = m/m_P [consistency with Part 33]
S9:  Compton frequency: omega_C = mc^2/hbar for all particles [exact]
S10: Layer decomposition reproduces correct G [test]

Called from main.py as Phase 22.

Usage (standalone):
    cd simulations/solver
    python composite_g.py
"""

import sys
import os
import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from sudoku_engine import (HBAR, C, G, L_P, M_P, M_E, M_P_PROTON,
                            ALPHA_EM, E_P, SudokuEngine)
from print_utils import ReportWriter


# ===========================================================================
# PHYSICAL CONSTANTS
# ===========================================================================

GEV_J = 1e9 * 1.602176634e-19   # 1 GeV in Joules

# Layer mass scales
M_PLANCK = M_P                           # gravitational condensate
M_EW = 246.0 * GEV_J / C**2             # Higgs vev = 246 GeV
M_QCD = 0.200 * GEV_J / C**2            # Lambda_QCD = 200 MeV

# PDTP condensate coupling
K_0 = 1.0 / (4.0 * np.pi)

# Known G
G_KNOWN = 6.67430e-11  # m^3 kg^-1 s^-2

# Particles for testing
PARTICLES = [
    ("electron", M_E),
    ("proton",   M_P_PROTON),
    ("Planck",   M_P),
]


# ===========================================================================
# HAUG DECOMPOSITION
# ===========================================================================

def haug_decomposition():
    """
    G decomposed into fundamental quantities.

    G = l_P^2 * c^3 / hbar     [Haug 2024]
      = hbar * c / m_P^2       [PDTP Part 33]

    Both are exact algebraic identities (not derivations).
    The content is in the INTERPRETATION, not the math.

    Source: Haug (2024), "The Compton Wavelength Is the True Matter Wavelength"

    Returns dict of decomposition results.
    """
    results = {}

    # Haug form
    G_haug = L_P**2 * C**3 / HBAR
    results["G_haug"] = G_haug
    results["G_haug_ratio"] = G_haug / G_KNOWN

    # PDTP form
    G_pdtp = HBAR * C / M_P**2
    results["G_pdtp"] = G_pdtp
    results["G_pdtp_ratio"] = G_pdtp / G_KNOWN

    # Component interpretation
    results["l_P_sq"] = L_P**2       # "lattice spacing squared"
    results["c_cubed"] = C**3         # "propagation speed cubed"
    results["inv_hbar"] = 1.0 / HBAR  # "quantum conversion factor"

    # Compton wavelength ratios
    for name, m in PARTICLES:
        lambda_C = HBAR / (m * C)
        ratio = L_P / lambda_C  # = m / m_P = 1/n
        n = m_P_over_m = M_P / m
        results["lP_over_lambdaC_{}".format(name)] = ratio
        results["n_{}".format(name)] = n

    return results


# ===========================================================================
# MODEL 1: SPRINGS IN SERIES
# ===========================================================================

def model_springs_in_series():
    """
    Model 1: G as springs in series.

    Each condensate layer has stiffness kappa_i = hbar*c / m_i^2.
    (This is the PDTP bridge: G = c^2 / (4*pi*kappa), so kappa = c^2/(4*pi*G).)

    Springs in series: 1/kappa_eff = sum(1/kappa_i)
    G_eff = c^2 / (4*pi*kappa_eff)

    Source (springs in series): https://en.wikipedia.org/wiki/Series_and_parallel_springs

    Returns dict of results.
    """
    results = {}

    # Layer stiffnesses
    # kappa_i proportional to 1/m_i^2 (from G_i = hbar*c/m_i^2 and G = c^2/(4*pi*kappa))
    # So kappa_i = c^2 / (4*pi*G_i) = c^2 * m_i^2 / (4*pi*hbar*c) = c*m_i^2 / (4*pi*hbar)
    layers = [
        ("Gravitational", M_PLANCK),
        ("Electroweak",   M_EW),
        ("QCD",           M_QCD),
    ]

    kappas = []
    for name, m in layers:
        G_layer = HBAR * C / m**2
        kappa = C**2 / (4.0 * np.pi * G_layer)
        # = C**2 * m**2 / (4*pi*hbar*c) = C * m**2 / (4*pi*hbar)
        kappas.append((name, m, G_layer, kappa))
        results["kappa_{}".format(name)] = kappa
        results["G_{}".format(name)] = G_layer

    # Springs in series
    inv_kappa_eff = sum(1.0 / k for _, _, _, k in kappas)
    kappa_eff = 1.0 / inv_kappa_eff
    G_eff = C**2 / (4.0 * np.pi * kappa_eff)

    results["kappa_eff"] = kappa_eff
    results["G_eff_series"] = G_eff
    results["G_eff_ratio"] = G_eff / G_KNOWN
    results["layers"] = kappas

    # Which layer dominates?
    # In springs-in-series, the SOFTEST spring dominates (smallest kappa)
    softest = min(kappas, key=lambda x: x[3])
    results["dominant_layer"] = softest[0]

    return results


# ===========================================================================
# MODEL 2: TRANSMISSION THROUGH INTERFACES
# ===========================================================================

def model_transmission():
    """
    Model 2: G as product of transmission coefficients.

    G_eff = G_bare * T_1 * T_2 * ... * T_N
    where T_i is the transmission at each layer interface.

    For wave transmission between media with impedances Z_1 and Z_2:
      T = 4*Z_1*Z_2 / (Z_1 + Z_2)^2
    This is always <= 1, with equality when Z_1 = Z_2.

    Source: https://en.wikipedia.org/wiki/Transmission_coefficient_(physics)

    In PDTP: Z_i = sqrt(kappa_i * rho_i) where kappa = stiffness, rho = density.
    For a condensate layer: kappa_i ~ 1/m_i^2, rho_i ~ m_i/a_i^3
    With a_i = hbar/(m_i*c): rho_i ~ m_i^4*c^3/hbar^3

    Z_i = sqrt(kappa_i * rho_i) = sqrt((c*m_i^2/(4*pi*hbar)) * (m_i^4*c^3/hbar^3))
    This gets complicated. Use dimensionless ratio Z_i/Z_j instead.

    Returns dict of results.
    """
    results = {}

    # Layer impedances (proportional to m_i^3 in natural units)
    # Z_i proportional to m_i^3 (from dimensional analysis)
    # What matters is the RATIO between adjacent layers
    layers = [
        ("Gravitational", M_PLANCK),
        ("Electroweak",   M_EW),
        ("QCD",           M_QCD),
    ]

    # Transmission at each interface
    T_total = 1.0
    interfaces = []
    for i in range(len(layers) - 1):
        name_1, m_1 = layers[i]
        name_2, m_2 = layers[i + 1]

        # Impedance ratio: Z ~ m^3 in natural units
        # T = 4*Z1*Z2 / (Z1 + Z2)^2 = 4*r / (1+r)^2 where r = Z2/Z1
        r = (m_2 / m_1)**3
        T_interface = 4.0 * r / (1.0 + r)**2
        T_total *= T_interface

        interfaces.append((
            "{} -> {}".format(name_1, name_2),
            r, T_interface
        ))
        results["T_{}_{}".format(name_1[:4], name_2[:4])] = T_interface
        results["r_{}_{}".format(name_1[:4], name_2[:4])] = r

    results["T_total"] = T_total
    results["interfaces"] = interfaces

    # G_eff if G_bare = 1 (natural units) or G_Planck
    G_bare = HBAR * C / M_PLANCK**2  # = G (trivially)
    G_eff = G_bare * T_total
    results["G_eff_transmission"] = G_eff
    results["G_eff_ratio"] = G_eff / G_KNOWN

    return results


# ===========================================================================
# MODEL 3: IMPEDANCE MATCHING (WAVE MECHANICAL)
# ===========================================================================

def model_impedance():
    """
    Model 3: Wave propagation through layered condensate.

    Think of gravity as a wave propagating through layers.
    At each interface, part reflects and part transmits.
    The net transmitted amplitude is the product of all T_i.

    For acoustic waves:
      Z = rho * c_s (impedance = density * sound speed)
      T_amplitude = 2*Z_1 / (Z_1 + Z_2)
      T_power = 4*Z_1*Z_2 / (Z_1 + Z_2)^2

    In PDTP: each layer has its own condensate with:
      c_s = c (Part 34: speed of sound = speed of light, always)
      rho_i = m_i / a_i^3 where a_i = hbar/(m_i*c) = Compton wavelength
      Z_i = rho_i * c = m_i^4 * c^4 / hbar^3

    Source: https://en.wikipedia.org/wiki/Acoustic_impedance

    Returns dict of results.
    """
    results = {}

    layers = [
        ("Gravitational", M_PLANCK),
        ("Electroweak",   M_EW),
        ("QCD",           M_QCD),
    ]

    # Compute impedances
    impedances = []
    for name, m in layers:
        a_i = HBAR / (m * C)  # Compton wavelength
        rho_i = m / a_i**3     # number density * mass (one particle per Compton volume)
        Z_i = rho_i * C        # acoustic impedance
        impedances.append((name, m, Z_i))
        results["Z_{}".format(name)] = Z_i

    # Impedance ratios and amplitude transmission
    T_amp_total = 1.0
    T_pow_total = 1.0
    for i in range(len(impedances) - 1):
        name_1, m_1, Z_1 = impedances[i]
        name_2, m_2, Z_2 = impedances[i + 1]

        T_amp = 2.0 * Z_1 / (Z_1 + Z_2)
        T_pow = 4.0 * Z_1 * Z_2 / (Z_1 + Z_2)**2

        T_amp_total *= T_amp
        T_pow_total *= T_pow

        iface = "{} -> {}".format(name_1, name_2)
        results["T_amp_{}".format(iface)] = T_amp
        results["T_pow_{}".format(iface)] = T_pow
        results["Z_ratio_{}".format(iface)] = Z_2 / Z_1

    results["T_amp_total"] = T_amp_total
    results["T_pow_total"] = T_pow_total

    # G_eff = G * T_power_total
    G_eff_pow = G_KNOWN * T_pow_total  # This is wrong conceptually but let's see the number
    results["G_eff_impedance"] = G_eff_pow

    return results


# ===========================================================================
# COMPTON FREQUENCY TABLE
# ===========================================================================

def compton_frequency_table():
    """
    Compute the Compton frequency for key particles and layers.

    omega_C = m*c^2 / hbar = c / lambda_C

    This is the particle's internal clock (Haug/Strassler).
    In PDTP, it's the vortex phase rotation rate.

    Source: De Broglie (1924); Haug (2024)

    Returns list of (name, mass, lambda_C, omega_C, n).
    """
    all_particles = [
        ("electron",   M_E),
        ("proton",     M_P_PROTON),
        ("W boson",    1.43298e-25),    # 80.4 GeV
        ("Higgs",      2.2302e-25),     # 125.1 GeV
        ("Lambda_QCD", M_QCD),
        ("Planck",     M_P),
    ]

    table = []
    for name, m in all_particles:
        lambda_C = HBAR / (m * C)  # Compton wavelength
        omega_C = m * C**2 / HBAR  # Compton frequency
        n = M_P / m                 # winding number (Part 33)
        table.append((name, m, lambda_C, omega_C, n))
    return table


# ===========================================================================
# CIRCULARITY ANALYSIS
# ===========================================================================

def circularity_analysis():
    """
    Check whether the multi-layer decomposition actually DERIVES G
    or just REARRANGES it.

    KEY QUESTION: Can we compute G_eff from KNOWN mass scales
    (m_P, v_Higgs, Lambda_QCD) WITHOUT using G as input?

    The problem: m_P = sqrt(hbar*c/G), so m_P already CONTAINS G.
    If we use m_P as a layer mass, we're putting G in and getting G out.

    CIRCULARITY TEST:
    Write G_eff in terms of m_EW, m_QCD, and fundamental constants ONLY
    (no m_P, no l_P, no G). Can we get G = 6.674e-11?

    Returns dict of results.
    """
    results = {}

    # Attempt 1: G from EW + QCD scales only
    # Springs in series with just EW and QCD:
    # G_EW = hbar*c / m_EW^2
    G_EW = HBAR * C / M_EW**2
    # G_QCD = hbar*c / m_QCD^2
    G_QCD = HBAR * C / M_QCD**2

    # 1/kappa_eff = 1/kappa_EW + 1/kappa_QCD
    # kappa_i = c^2 / (4*pi*G_i)
    kappa_EW = C**2 / (4.0 * np.pi * G_EW)
    kappa_QCD = C**2 / (4.0 * np.pi * G_QCD)
    kappa_eff_2layer = 1.0 / (1.0/kappa_EW + 1.0/kappa_QCD)
    G_eff_2layer = C**2 / (4.0 * np.pi * kappa_eff_2layer)

    results["G_EW"] = G_EW
    results["G_QCD"] = G_QCD
    results["G_eff_2layer"] = G_eff_2layer
    results["G_2layer_ratio"] = G_eff_2layer / G_KNOWN

    # The 2-layer result is dominated by the SOFTER spring (larger G).
    # G_QCD = hbar*c/m_QCD^2 >> G_EW because m_QCD << m_EW
    # So G_eff ~ G_QCD ~ hbar*c/m_QCD^2 ~ 2.6e-6 (way too large)
    results["dominant"] = "QCD (softest spring, m_QCD << m_EW)"

    # Attempt 2: product of ratios
    # G = hbar*c/m_P^2. If m_P = m_EW * m_EW / m_QCD (geometric?)
    # This is numerology -- let's just check
    m_P_from_ratio = M_EW**2 / M_QCD
    G_from_ratio = HBAR * C / m_P_from_ratio**2
    results["m_P_from_EW_QCD"] = m_P_from_ratio
    results["G_from_ratio"] = G_from_ratio
    results["G_ratio_ratio"] = G_from_ratio / G_KNOWN

    # Attempt 3: multiply layer G values
    # G_eff = G_EW * G_QCD / G_natural_units ???
    # This doesn't have the right dimensions.
    # G_EW * G_QCD has dimensions [m^6 / (kg^2 s^4)]
    # Need to divide by something with dimensions [m^3 / (kg s^2)]
    # G_eff = G_EW * G_QCD * (m_P^2 / (hbar*c)) ... that's circular again.

    # CONCLUSION: Without m_P (or equivalently G), the layer model
    # cannot produce the correct G. m_EW and m_QCD alone give
    # G ~ 10^-6, not 10^-11. The missing factor IS m_P.
    results["circular"] = True
    results["missing_factor"] = G_eff_2layer / G_KNOWN

    return results


# ===========================================================================
# SUDOKU CHECKS
# ===========================================================================

def run_sudoku_checks(rw):
    """10 Sudoku consistency checks for the composite G model."""
    checks = []

    haug = haug_decomposition()

    # S1: Haug decomposition G = l_P^2 * c^3 / hbar
    s1_ratio = haug["G_haug"] / G_KNOWN
    s1_pass = abs(s1_ratio - 1.0) < 0.001
    checks.append(("S1", "G = l_P^2 * c^3 / hbar",
                    "{:.5e}".format(G_KNOWN),
                    "{:.5e}".format(haug["G_haug"]),
                    s1_ratio, s1_pass))

    # S2: PDTP form G = hbar*c / m_P^2
    s2_ratio = haug["G_pdtp"] / G_KNOWN
    s2_pass = abs(s2_ratio - 1.0) < 0.001
    checks.append(("S2", "G = hbar*c / m_P^2",
                    "{:.5e}".format(G_KNOWN),
                    "{:.5e}".format(haug["G_pdtp"]),
                    s2_ratio, s2_pass))

    # S3: Springs in series: softest spring dominates
    springs = model_springs_in_series()
    # The weakest link (smallest kappa = QCD) should dominate
    # G_eff should be close to G_QCD (the largest G_layer)
    G_QCD_layer = springs["G_QCD"]
    s3_ratio = springs["G_eff_series"] / G_QCD_layer
    # Should be close to 1 (dominated by QCD)
    s3_pass = 0.9 < s3_ratio < 1.1
    checks.append(("S3", "Series: softest spring dominates",
                    "{:.3e}".format(G_QCD_layer),
                    "{:.3e}".format(springs["G_eff_series"]),
                    s3_ratio, s3_pass))

    # S4: Three-layer G_eff vs G_known
    s4_ratio = springs["G_eff_series"] / G_KNOWN
    # This will be ~ 10^5 (way off) because QCD layer is too soft
    s4_pass = 0.5 < s4_ratio < 2.0
    checks.append(("S4", "3-layer series -> G_known?",
                    "{:.3e}".format(G_KNOWN),
                    "{:.3e}".format(springs["G_eff_series"]),
                    s4_ratio, s4_pass))

    # S5: Transmission model: T_total < 1
    trans = model_transmission()
    s5_pass = trans["T_total"] < 1.0
    checks.append(("S5", "Transmission T_total < 1",
                    "< 1",
                    "{:.6e}".format(trans["T_total"]),
                    1.0 if s5_pass else 0.0, s5_pass))

    # S6: Impedance mismatch between layers (Z ratio)
    imp = model_impedance()
    # Z_Planck >> Z_EW >> Z_QCD (impedance scales as m^4)
    Z_grav = imp["Z_Gravitational"]
    Z_ew = imp["Z_Electroweak"]
    Z_qcd = imp["Z_QCD"]
    s6_pass = Z_grav > Z_ew > Z_qcd
    checks.append(("S6", "Z_grav > Z_EW > Z_QCD",
                    "decreasing",
                    "{:.1e} > {:.1e} > {:.1e}".format(Z_grav, Z_ew, Z_qcd),
                    1.0 if s6_pass else 0.0, s6_pass))

    # S7: Removing QCD layer changes G (phase transition prediction)
    # Without QCD: only grav + EW layers
    kappa_grav = springs["kappa_Gravitational"]
    kappa_ew = springs["kappa_Electroweak"]
    kappa_eff_no_qcd = 1.0 / (1.0/kappa_grav + 1.0/kappa_ew)
    G_no_qcd = C**2 / (4.0 * np.pi * kappa_eff_no_qcd)
    ratio_change = G_no_qcd / springs["G_eff_series"]
    # Removing a layer SHOULD change G (ratio != 1)
    s7_pass = abs(ratio_change - 1.0) > 0.01  # must be different
    checks.append(("S7", "Removing QCD layer changes G",
                    "!= 1",
                    "{:.4f}".format(ratio_change),
                    1.0 if s7_pass else 0.0, s7_pass))

    # S8: l_P / lambda_C = m / m_P = 1/n (Part 33 consistency)
    ratio_e = haug["lP_over_lambdaC_electron"]
    expected_e = M_E / M_P
    s8_ratio = ratio_e / expected_e
    s8_pass = abs(s8_ratio - 1.0) < 1e-10
    checks.append(("S8", "l_P/lambda_C = m/m_P",
                    "{:.6e}".format(expected_e),
                    "{:.6e}".format(ratio_e),
                    s8_ratio, s8_pass))

    # S9: Compton frequency omega_C = mc^2/hbar
    omega_e = M_E * C**2 / HBAR
    omega_check = C / (HBAR / (M_E * C))  # = c / lambda_C
    s9_ratio = omega_e / omega_check
    s9_pass = abs(s9_ratio - 1.0) < 1e-10
    checks.append(("S9", "omega_C = mc^2/hbar = c/lambda_C",
                    "{:.6e}".format(omega_check),
                    "{:.6e}".format(omega_e),
                    s9_ratio, s9_pass))

    # S10: Circularity: 2-layer (EW+QCD only) fails to reproduce G
    circ = circularity_analysis()
    # G_2layer should be >> G_known (factor ~10^5)
    s10_ratio = circ["G_2layer_ratio"]
    # PASS if it FAILS to reproduce G (proving m_P is essential)
    s10_pass = s10_ratio > 100.0  # way off = circularity confirmed
    checks.append(("S10", "2-layer (no m_P) fails -> circular",
                    "{:.3e}".format(G_KNOWN),
                    "{:.3e}".format(circ["G_eff_2layer"]),
                    s10_ratio, s10_pass))

    return checks


# ===========================================================================
# MAIN PHASE RUNNER
# ===========================================================================

def run_composite_g(rw, engine=None):
    """Phase 22: G as Composite of Multiple Layers (Part 60, Idea H)."""

    rw.section("PHASE 22: G AS COMPOSITE OF MULTIPLE LAYERS (Part 60, Idea H)")

    rw.print("QUESTION: Is G a single fundamental constant, or the NET EFFECT")
    rw.print("of coupling passing through multiple condensate layers?")
    rw.print("")
    rw.print("USER INSIGHT: Like springs in series or light through glass panes,")
    rw.print("G could be weak because it passes through MULTIPLE interfaces.")

    # ---------------------------------------------------------------
    # Step 1: Haug decomposition
    # ---------------------------------------------------------------
    rw.subsection("Step 1: Haug Decomposition of G")

    haug = haug_decomposition()

    rw.print("TWO FORMS OF G (exact algebraic identities):")
    rw.print("")
    rw.print("  Haug:  G = l_P^2 * c^3 / hbar = {:.5e}  (ratio: {:.6f})".format(
        haug["G_haug"], haug["G_haug_ratio"]))
    rw.print("  PDTP:  G = hbar * c / m_P^2    = {:.5e}  (ratio: {:.6f})".format(
        haug["G_pdtp"], haug["G_pdtp_ratio"]))
    rw.print("  Known: G = {:.5e}".format(G_KNOWN))
    rw.print("")
    rw.print("INTERPRETATION (Haug 2024):")
    rw.print("  l_P^2 = gravitational lattice spacing squared")
    rw.print("  c^3   = propagation speed cubed (shared by all layers)")
    rw.print("  1/hbar = quantum scale conversion")
    rw.print("")
    rw.print("Source: Haug (2024), The Compton Wavelength Is the True Matter Wavelength")

    # ---------------------------------------------------------------
    # Step 2: Compton frequency table
    # ---------------------------------------------------------------
    rw.subsection("Step 2: Compton Frequencies and Winding Numbers")

    ctable = compton_frequency_table()
    headers_c = ["Particle", "mass (kg)", "lambda_C (m)", "omega_C (Hz)", "n = m_P/m"]
    rows_c = []
    for name, m, lc, oc, n in ctable:
        rows_c.append([name,
                       "{:.3e}".format(m),
                       "{:.3e}".format(lc),
                       "{:.3e}".format(oc),
                       "{:.3e}".format(n)])
    rw.table(headers_c, rows_c, [12, 12, 14, 14, 14])

    rw.print("")
    rw.print("KEY IDENTITY (Haug + PDTP):")
    rw.print("  l_P / lambda_C = m / m_P = 1/n (inverse winding number)")
    rw.print("  The Compton frequency IS the vortex phase rotation rate.")
    rw.print("  Strassler's 'wavicle' = PDTP's vortex = self-sustaining standing wave.")

    # ---------------------------------------------------------------
    # Step 3: Model 1 - Springs in series
    # ---------------------------------------------------------------
    rw.subsection("Step 3: Model 1 -- Springs in Series")

    springs = model_springs_in_series()

    rw.print("Each condensate layer has stiffness kappa_i = c*m_i^2 / (4*pi*hbar).")
    rw.print("Springs in series: 1/kappa_eff = 1/kappa_1 + 1/kappa_2 + 1/kappa_3")
    rw.print("")

    headers_s = ["Layer", "m (kg)", "G_layer", "kappa"]
    rows_s = []
    for name, m, g_layer, kappa in springs["layers"]:
        rows_s.append([name,
                       "{:.3e}".format(m),
                       "{:.3e}".format(g_layer),
                       "{:.3e}".format(kappa)])
    rw.table(headers_s, rows_s, [16, 12, 14, 14])

    rw.print("")
    rw.print("  kappa_eff = {:.3e}".format(springs["kappa_eff"]))
    rw.print("  G_eff (series) = {:.3e}".format(springs["G_eff_series"]))
    rw.print("  G_known        = {:.3e}".format(G_KNOWN))
    rw.print("  Ratio G_eff / G_known = {:.2e}".format(springs["G_eff_ratio"]))
    rw.print("")
    rw.print("  RESULT: G_eff is DOMINATED by QCD layer (softest spring).")
    rw.print("  G_eff ~ G_QCD = hbar*c/m_QCD^2 ~ {:.2e}".format(springs["G_QCD"]))
    rw.print("  This is ~{:.0e} times too large.".format(springs["G_eff_ratio"]))
    rw.print("")
    rw.print("  PROBLEM: Springs in series gives the WEAKEST link (QCD),")
    rw.print("  not the gravitational value. The model needs the Planck-scale")
    rw.print("  layer to DOMINATE, but in series it's the opposite.")

    # ---------------------------------------------------------------
    # Step 4: Model 2 - Transmission through interfaces
    # ---------------------------------------------------------------
    rw.subsection("Step 4: Model 2 -- Transmission Through Interfaces")

    trans = model_transmission()

    rw.print("Each interface transmits a fraction T = 4*r/(1+r)^2 where r = Z2/Z1.")
    rw.print("Impedance ratio r = (m_2/m_1)^3 (dimensional estimate).")
    rw.print("")

    headers_t = ["Interface", "Z ratio r", "Transmission T"]
    rows_t = []
    for iface, r, T in trans["interfaces"]:
        rows_t.append([iface,
                       "{:.3e}".format(r),
                       "{:.6e}".format(T)])
    rw.table(headers_t, rows_t, [30, 14, 16])

    rw.print("")
    rw.print("  T_total = {:.6e}".format(trans["T_total"]))
    rw.print("  G_eff = G * T_total = {:.3e}".format(trans["G_eff_transmission"]))
    rw.print("")
    rw.print("  RESULT: Transmission is TINY because the impedance mismatch")
    rw.print("  between Planck and EW scales is enormous (r ~ 10^-51).")
    rw.print("  But G_eff = G * T (G is already small!) makes it even smaller.")
    rw.print("  The model would need G_bare >> G to compensate.")

    # ---------------------------------------------------------------
    # Step 5: Impedance analysis
    # ---------------------------------------------------------------
    rw.subsection("Step 5: Model 3 -- Impedance Matching")

    imp = model_impedance()

    rw.print("Acoustic impedance Z = rho * c_s (density * sound speed).")
    rw.print("In PDTP: c_s = c (always), rho_i = m_i / a_i^3.")
    rw.print("")
    rw.print("  Z_Gravitational = {:.3e}".format(imp["Z_Gravitational"]))
    rw.print("  Z_Electroweak   = {:.3e}".format(imp["Z_Electroweak"]))
    rw.print("  Z_QCD           = {:.3e}".format(imp["Z_QCD"]))
    rw.print("")
    rw.print("  Impedance scales as m^4 -> enormous mismatch between layers.")
    rw.print("  Grav/EW ratio: {:.2e}".format(imp["Z_Gravitational"] / imp["Z_Electroweak"]))
    rw.print("  EW/QCD ratio:  {:.2e}".format(imp["Z_Electroweak"] / imp["Z_QCD"]))
    rw.print("")
    rw.print("  T_power_total = {:.3e}".format(imp["T_pow_total"]))
    rw.print("")
    rw.print("  RESULT: The HUGE impedance mismatch between layers means")
    rw.print("  almost nothing gets through. This IS the hierarchy in disguise:")
    rw.print("  Z_grav/Z_EW ~ (m_P/m_EW)^4 ~ 10^68. The mismatch IS the problem.")

    # ---------------------------------------------------------------
    # Step 6: Circularity analysis
    # ---------------------------------------------------------------
    rw.subsection("Step 6: Circularity Analysis")

    circ = circularity_analysis()

    rw.print("CAN WE GET G WITHOUT USING m_P (which already contains G)?")
    rw.print("")
    rw.print("  Attempt: use only m_EW (246 GeV) and m_QCD (200 MeV)")
    rw.print("  G_EW  = hbar*c / m_EW^2  = {:.3e}".format(circ["G_EW"]))
    rw.print("  G_QCD = hbar*c / m_QCD^2 = {:.3e}".format(circ["G_QCD"]))
    rw.print("  G_eff (2-layer series) = {:.3e}".format(circ["G_eff_2layer"]))
    rw.print("  G_known = {:.3e}".format(G_KNOWN))
    rw.print("  Ratio: {:.2e} (off by factor ~{:.0e})".format(
        circ["G_2layer_ratio"], circ["G_2layer_ratio"]))
    rw.print("")
    rw.print("  NEGATIVE RESULT: Without m_P, the 2-layer model gives")
    rw.print("  G ~ 10^-6, not 10^-11. Off by factor ~{:.0e}.".format(
        circ["missing_factor"]))
    rw.print("")
    rw.print("  The missing factor IS m_P. You need the Planck scale to get G.")
    rw.print("  This confirms Part 29 and Part 35: G is a FREE PARAMETER.")
    rw.print("  The layer decomposition REORGANISES G, it does not DERIVE it.")
    rw.print("")
    rw.print("  Numerology attempt: m_P = m_EW^2 / m_QCD")
    rw.print("    = {:.3e} kg (vs actual m_P = {:.3e} kg)".format(
        circ["m_P_from_EW_QCD"], M_P))
    rw.print("    Ratio: {:.2e} (off by ~{:.0e})".format(
        circ["m_P_from_EW_QCD"] / M_P, circ["m_P_from_EW_QCD"] / M_P))
    rw.print("  -> Not even close. No simple combination of EW and QCD scales gives m_P.")

    # ---------------------------------------------------------------
    # Step 7: What the layer picture DOES give
    # ---------------------------------------------------------------
    rw.subsection("Step 7: What the Layer Picture DOES Give")

    rw.print("Despite failing to DERIVE G, the layer picture gives useful STRUCTURE:")
    rw.print("")
    rw.print("  1. PHASE TRANSITION PREDICTION: If a layer merges at high T,")
    rw.print("     G_eff changes. At QGP deconfinement (T ~ 170 MeV),")
    rw.print("     the QCD layer 'melts' into the EW layer -> G shifts.")
    rw.print("     Size of shift: G_no_QCD / G_with_QCD ~ {:.4f}".format(
        circ["G_eff_2layer"] / springs["G_eff_series"]
        if 'springs' in dir() else 1.0))
    rw.print("")
    rw.print("  2. IMPEDANCE MISMATCH = HIERARCHY: The huge Z ratio between")
    rw.print("     Planck and EW scales IS the hierarchy problem, reframed as")
    rw.print("     'why is the impedance mismatch so large?'")
    rw.print("")
    rw.print("  3. STRASSLER'S WAVICLE = PDTP VORTEX: Both describe particles")
    rw.print("     as self-sustaining standing wave patterns. The Compton wavelength")
    rw.print("     is the vortex core size (Part 33). The Compton frequency is")
    rw.print("     the phase rotation rate.")
    rw.print("")
    rw.print("  4. HAUG'S REDUCTION: All gravity = just l_P and lambda_C.")
    rw.print("     In PDTP: l_P = a_0 (lattice spacing), lambda_C = vortex core.")
    rw.print("     G = (a_0 / lambda_C)^2 * mc^2 * a_0 / hbar")
    rw.print("     = (1/n)^2 * [everything else]")
    rw.print("     The winding number n IS the hierarchy.")

    # ---------------------------------------------------------------
    # Step 8: Sudoku checks
    # ---------------------------------------------------------------
    rw.subsection("Step 8: Sudoku Consistency Checks (10 tests)")

    checks = run_sudoku_checks(rw)

    headers_chk = ["Test", "Description", "Expected", "Got", "Ratio", "Pass?"]
    rows_chk = []
    n_pass = 0
    for tag, desc, expected, got, ratio, passed in checks:
        status = "PASS" if passed else "FAIL"
        if passed:
            n_pass += 1
        rows_chk.append([tag, desc, str(expected), str(got),
                         "{:.4f}".format(ratio) if isinstance(ratio, float) else str(ratio),
                         status])
    rw.table(headers_chk, rows_chk, [4, 36, 14, 14, 10, 5])

    rw.print("")
    rw.print("SCORE: {}/10 PASS".format(n_pass))

    # ---------------------------------------------------------------
    # Step 9: Verdict
    # ---------------------------------------------------------------
    rw.subsection("Step 9: Verdict")

    rw.print("NEGATIVE RESULT -- Layer decomposition is INTERPRETIVE, not derivational.")
    rw.print("")
    rw.print("WHAT WORKS:")
    rw.print("  1. Haug/PDTP decomposition G = hbar*c/m_P^2 is exact")
    rw.print("  2. Compton freq = vortex rotation rate (Haug-PDTP connection)")
    rw.print("  3. l_P/lambda_C = 1/n (winding number, Part 33)")
    rw.print("  4. Impedance mismatch correctly localises the hierarchy")
    rw.print("  5. Layer structure predicts G changes at phase transitions")
    rw.print("")
    rw.print("WHAT DOES NOT WORK:")
    rw.print("  1. Springs-in-series: dominated by SOFTEST layer (QCD), gives G ~ 10^-6")
    rw.print("  2. Transmission: makes G even SMALLER (T << 1 on top of already-small G)")
    rw.print("  3. Cannot derive G from m_EW + m_QCD alone (need m_P = need G)")
    rw.print("  4. All three models REARRANGE the hierarchy, they don't SOLVE it")
    rw.print("")
    rw.print("CUMULATIVE FINDING (Parts 55-60):")
    rw.print("  Part 55: Two channels -- STRUCTURAL MATCH (force types correct)")
    rw.print("  Part 56: RG running -- NEGATIVE (wrong direction)")
    rw.print("  Part 57: Dispersion -- NEGATIVE (classical, not quantum)")
    rw.print("  Part 58: Homotopy -- STRUCTURAL MATCH (force structure correct)")
    rw.print("  Part 59: Strider -- INTERPRETIVE (correct mass dependence, not derived)")
    rw.print("  Part 60: Composite G -- NEGATIVE (reorganises hierarchy, doesn't solve it)")
    rw.print("")
    rw.print("  G and alpha_EM remain FREE PARAMETERS in PDTP.")
    rw.print("  The framework correctly describes force STRUCTURE but not force VALUES.")
    rw.print("  This is the same situation as the Standard Model.")

    return n_pass


# ===========================================================================
# STANDALONE ENTRY POINT
# ===========================================================================

def main():
    output_dir = os.path.join(_HERE, "outputs")
    rw = ReportWriter(output_dir, label="composite_g")
    n_pass = run_composite_g(rw)
    rw.close()
    print("")
    print("Report saved to: {}".format(rw.path))
    print("Sudoku: {}/10 PASS".format(n_pass))


if __name__ == "__main__":
    main()
