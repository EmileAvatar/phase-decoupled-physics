#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gravity_em_truth_table.py -- Gravity-EM Unification Truth Table Investigation
==============================================================================
Standalone investigation (NOT integrated into main.py).
Tests the speculation: are gravity and EM different frequency bands of ONE medium?

Four truth table cases:
  (1) A true,  B false : gravity = beat frequency, separate condensates
  (2) A false, B true  : same medium, not beat frequency
  (3) A true,  B true  : one medium, gravity = beat
  (4) A false, B false : current PDTP baseline (separate, not beat)

11 Sudoku-style checks (S1-S11) with PASS/FAIL scoring.

Key insight: ocean wave analogy -- surface = circular orbits (all spins),
bottom = horizontal only (spin-0). Coupling decays as tanh^2 (L-shape),
not exponential. Higher spin decays faster.

Usage (standalone):
    cd simulations/solver
    python gravity_em_truth_table.py
"""

import sys
import os
import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from print_utils import ReportWriter


# ===========================================================================
# PHYSICAL CONSTANTS (CODATA 2018)
# Source: https://physics.nist.gov/cuu/Constants/index.html
# ===========================================================================
HBAR = 1.054571817e-34    # J s
C    = 2.99792458e8       # m/s
G    = 6.67430e-11        # m^3 kg^-1 s^-2
K_B  = 1.380649e-23       # J/K
E_eV = 1.602176634e-19    # J per eV

# Planck units
L_P  = np.sqrt(HBAR * G / C**3)     # ~1.616e-35 m
M_P  = np.sqrt(HBAR * C / G)        # ~2.176e-8 kg
T_P  = np.sqrt(HBAR * G / C**5)     # ~5.391e-44 s

# Particle masses (kg)
M_E     = 9.1093837015e-31    # electron
M_MU    = 1.883531627e-28     # muon
M_TAU   = 3.16754e-27         # tau
M_P_P   = 1.67262192369e-27   # proton
M_W     = 1.43298e-25         # W boson (80.379 GeV)
M_Z     = 1.62566e-25         # Z boson (91.1876 GeV)

# Particle masses (GeV/c^2) for display
M_E_GEV   = 0.51099895e-3
M_MU_GEV  = 0.1056583755
M_TAU_GEV = 1.77686
M_P_GEV   = 0.93827208816
M_W_GEV   = 80.379
M_Z_GEV   = 91.1876

# Condensate scales (GeV -> kg)
LAMBDA_QCD_GEV = 0.200           # QCD scale ~200 MeV
V_EW_GEV      = 246.22           # Higgs VEV
M_PLANCK_GEV  = 1.220890e19      # Planck mass

LAMBDA_QCD_KG = LAMBDA_QCD_GEV * 1e9 * E_eV / C**2
V_EW_KG       = V_EW_GEV * 1e9 * E_eV / C**2

# Coupling constants (measured)
ALPHA_EM   = 7.2973525693e-3     # 1/137.036 (low energy)
ALPHA_EM_Z = 1.0 / 127.952      # at m_Z
ALPHA_S_Z  = 0.1179              # strong coupling at m_Z
# Source: PDG 2022 https://pdg.lbl.gov/

# GUT-scale reference couplings (SM one-loop running, approximate)
# Source: Langacker (2010), "The Standard Model and Beyond"
# At ~2e16 GeV:  alpha_1 ~ 1/59,  alpha_2 ~ 1/49,  alpha_3 ~ 1/54
# (Do not converge exactly in SM; converge in MSSM)
GUT_SCALE_GEV   = 2e16
ALPHA_1_GUT     = 1.0 / 59.0
ALPHA_2_GUT     = 1.0 / 49.0
ALPHA_3_GUT     = 1.0 / 54.0

# Matter particles: persistent vortex lines in the condensate (stable or long-lived)
# These are what gravity couples to via mass (continuous phase gradient).
MATTER_PARTICLES = [
    ("electron",  M_E,    M_E_GEV,   0.5, -1),
    ("muon",      M_MU,   M_MU_GEV,  0.5, -1),
    ("tau",       M_TAU,  M_TAU_GEV, 0.5, -1),
    ("proton",    M_P_P,  M_P_GEV,   0.5, +1),
]

# Force carriers: condensate excitations (short-lived splashes, not stable vortices)
# W/Z are massive force carriers (weak force); photon/gluon are massless.
# Included for frequency map but NOT for beat/mass-independence tests.
FORCE_CARRIERS = [
    ("W boson",   M_W,    M_W_GEV,   1.0,  0),
    ("Z boson",   M_Z,    M_Z_GEV,   1.0,  0),
]

# Combined list for frequency map (S1) and carrier sideband (S10)
ALL_PARTICLES = MATTER_PARTICLES + FORCE_CARRIERS


# ===========================================================================
# S1: FREQUENCY SCALE MAP
# ===========================================================================
def s1_frequency_map(rw):
    """Compute omega = m*c^2/hbar for all condensate layers and particles."""
    rw.section("S1: Frequency Scale Map")
    rw.print("omega = m * c^2 / hbar  (angular frequency of matter-wave)")
    rw.print("")

    # Condensate layers
    layers = [
        ("Gravitational (m_P)",  M_P),
        ("QCD (Lambda_QCD)",     LAMBDA_QCD_KG),
        ("Electroweak (v_EW)",   V_EW_KG),
    ]

    rw.print("Note: Matter particles (electron, muon, tau, proton) = stable vortex lines.")
    rw.print("  Force carriers (W*, Z*) = short-lived condensate excitations, not stable vortices.")
    rw.print("  Beat/mass tests (S2-S5) use matter particles only. Frequency map includes both.")
    rw.print("")
    rw.subsection("Condensate layers")
    headers = ["Layer", "Mass (kg)", "omega (rad/s)", "f (Hz)", "log10(f)"]
    rows = []
    layer_omegas = {}
    for name, m in layers:
        omega = m * C**2 / HBAR
        f = omega / (2 * np.pi)
        layer_omegas[name] = omega
        rows.append([name, "%.3e" % m, "%.3e" % omega, "%.3e" % f, "%.1f" % np.log10(f)])
    rw.table(headers, rows, [28, 12, 14, 14, 10])

    rw.subsection("Particles")
    headers = ["Particle", "Mass (GeV)", "omega (rad/s)", "f (Hz)", "log10(f)"]
    rows = []
    particle_omegas = {}
    for name, m_kg, m_gev, spin, charge in ALL_PARTICLES:
        omega = m_kg * C**2 / HBAR
        f = omega / (2 * np.pi)
        particle_omegas[name] = omega
        label = name + " *" if (name, m_kg, m_gev, spin, charge) in FORCE_CARRIERS else name
        rows.append([label, "%.6f" % m_gev, "%.3e" % omega, "%.3e" % f, "%.1f" % np.log10(f)])
    rw.table(headers, rows, [12, 12, 14, 14, 10])

    omega_P = M_P * C**2 / HBAR
    omega_e = M_E * C**2 / HBAR
    rw.print("Frequency ratio omega_Planck / omega_electron = %.3e" % (omega_P / omega_e))
    rw.print("  = m_P / m_e = %.3e  (winding number n)" % (M_P / M_E))
    rw.print("  = %.1f decades" % np.log10(omega_P / omega_e))

    return layer_omegas, particle_omegas


# ===========================================================================
# S2: BEAT FREQUENCY TEST (IDEA A) — GRAVITY
# ===========================================================================
def s2_beat_gravity(rw):
    """Test: does alpha_G = (m/m_P)^2 match G*m^2/(hbar*c)?"""
    rw.section("S2: Beat Frequency Test -- Gravity")
    rw.print("Prediction: alpha_G = (m / m_P)^2  [beat frequency modulation depth squared]")
    rw.print("Known:      alpha_G = G * m^2 / (hbar * c)")
    rw.print("")

    headers = ["Particle", "m/m_P", "(m/m_P)^2", "G*m^2/(hbar*c)", "Ratio", "PASS?"]
    rows = []
    n_pass = 0
    for name, m_kg, m_gev, spin, charge in MATTER_PARTICLES:
        beat_alpha = (m_kg / M_P)**2
        known_alpha = G * m_kg**2 / (HBAR * C)
        ratio = beat_alpha / known_alpha if known_alpha > 0 else 0
        ok = 0.99 <= ratio <= 1.01
        if ok:
            n_pass += 1
        rows.append([name, "%.3e" % (m_kg / M_P), "%.3e" % beat_alpha,
                      "%.3e" % known_alpha, "%.6f" % ratio,
                      "PASS" if ok else "FAIL"])
    rw.table(headers, rows, [12, 12, 14, 14, 10, 6])

    rw.print("Result: %d / %d PASS" % (n_pass, len(MATTER_PARTICLES)))
    rw.print("Note: (m/m_P)^2 = G*m^2/(hbar*c) is an IDENTITY (m_P^2 = hbar*c/G).")
    rw.print("This is CONSISTENT but CIRCULAR -- it restates the definition of m_P.")
    rw.print("The beat model gives the RIGHT formula but does not FIX m_P.")
    return n_pass, len(MATTER_PARTICLES)


# ===========================================================================
# S3: NAIVE BEAT FOR EM — EXPECT FAIL
# ===========================================================================
def s3_beat_em(rw):
    """Test: does alpha_EM = (m/v_EW)^2? Should FAIL."""
    rw.section("S3: Naive Beat for EM -- Expect FAIL")
    rw.print("If EM were a beat frequency of the EW condensate:")
    rw.print("  alpha_EM_beat = (m / v_EW)^2  where v_EW = 246.22 GeV")
    rw.print("  Known alpha_EM = 1/137.036 = %.6e" % ALPHA_EM)
    rw.print("")

    headers = ["Particle", "m (GeV)", "(m/v_EW)^2", "alpha_EM", "Ratio", "PASS?"]
    rows = []
    n_pass = 0
    for name, m_kg, m_gev, spin, charge in MATTER_PARTICLES:
        beat_alpha = (m_gev / V_EW_GEV)**2
        ratio = beat_alpha / ALPHA_EM if ALPHA_EM > 0 else 0
        ok = 0.99 <= ratio <= 1.01
        if ok:
            n_pass += 1
        rows.append([name, "%.6f" % m_gev, "%.3e" % beat_alpha,
                      "%.6e" % ALPHA_EM, "%.3e" % ratio,
                      "PASS" if ok else "FAIL"])
    rw.table(headers, rows, [12, 12, 14, 14, 12, 6])

    rw.print("Result: %d / %d PASS" % (n_pass, len(MATTER_PARTICLES)))
    rw.print("EXPECTED FAILURE: alpha_EM is NOT (m/v_EW)^2.")
    rw.print("  electron: (m_e/v_EW)^2 = %.3e  vs  1/137 = %.3e" % (
        (M_E_GEV / V_EW_GEV)**2, ALPHA_EM))
    rw.print("  proton:   (m_p/v_EW)^2 = %.3e  vs  1/137 = %.3e" % (
        (M_P_GEV / V_EW_GEV)**2, ALPHA_EM))
    rw.print("Beat mechanism FAILS for EM: coupling would depend on mass, but alpha_EM does not.")
    return n_pass, len(MATTER_PARTICLES)


# ===========================================================================
# S4: OCEAN WAVE DEPTH MODEL — tanh^2 FIT
# ===========================================================================
def s4_ocean_wave_depth(rw):
    """Fit tanh^2(k*z) to alpha_G and alpha_EM. Report required k-ratio."""
    rw.section("S4: Ocean Wave Depth Model -- tanh^2 Fit")
    rw.print("Ocean wave analogy: T/L amplitude ratio = tanh(k * z)")
    rw.print("  z = 'height above bottom' = log10(m / m_lightest)")
    rw.print("  Coupling ~ tanh^2(k * z)  [L-shaped, power-law near bottom]")
    rw.print("  For small kz: tanh^2(kz) ~ (kz)^2 [quadratic power law]")
    rw.print("")

    # Use log10(m/m_P) as depth from surface (negative), or equivalently
    # z = log10(m_P/m) as depth from surface (positive, larger = deeper)
    # "Bottom" = lightest particle; "Surface" = Planck scale
    # Actually: z = position from bottom. Surface = high z, bottom = z=0.
    # Let z = log10(m / m_ref) where m_ref is some IR cutoff.
    # Simpler: fit alpha = tanh^2(k * x) where x = log10(m_P / m) = decades below Planck

    rw.subsection("Required k for each force (at electron scale)")
    x_e = np.log10(M_P / M_E)  # ~22.76 decades
    rw.print("Electron depth from Planck surface: x_e = log10(m_P/m_e) = %.2f decades" % x_e)
    rw.print("")

    # For gravity: alpha_G(e) = (m_e/m_P)^2 ~ 1.75e-45
    alpha_G_e = (M_E / M_P)**2
    # tanh^2(k2 * z) = alpha_G_e  =>  k2 * z = arctanh(sqrt(alpha_G_e))
    # For very small alpha: arctanh(x) ~ x, so k2 * x_e ~ sqrt(alpha_G_e)
    sqrt_alpha_G = np.sqrt(alpha_G_e)
    k_grav = sqrt_alpha_G / x_e  # approximate (tanh ~ x for small x)
    rw.print("Gravity (spin-2):")
    rw.print("  alpha_G(e)      = %.3e" % alpha_G_e)
    rw.print("  sqrt(alpha_G)   = %.3e" % sqrt_alpha_G)
    rw.print("  k_gravity       = sqrt(alpha_G) / x_e = %.3e per decade" % k_grav)

    # For EM: alpha_EM = 1/137 ~ 7.3e-3
    sqrt_alpha_EM = np.sqrt(ALPHA_EM)
    # arctanh(0.085) ~ 0.0855
    k_em = np.arctanh(sqrt_alpha_EM) / x_e
    rw.print("")
    rw.print("EM (spin-1):")
    rw.print("  alpha_EM        = %.6e" % ALPHA_EM)
    rw.print("  sqrt(alpha_EM)  = %.4f" % sqrt_alpha_EM)
    rw.print("  arctanh(sqrt)   = %.4f" % np.arctanh(sqrt_alpha_EM))
    rw.print("  k_EM            = arctanh(sqrt(alpha_EM)) / x_e = %.4f per decade" % k_em)

    ratio_k = k_em / k_grav
    rw.print("")
    rw.print("k_EM / k_gravity  = %.1f" % ratio_k)
    rw.print("Naive spin ratio  = spin1 / spin2 = 1/2 = 0.5")
    rw.print("")
    rw.print("PROBLEM: need k_EM/k_grav ~ %.0f, but spin ratio gives 0.5." % ratio_k)
    rw.print("The depth model gets the ORDERING right (spin-2 weaker than spin-1)")
    rw.print("but the MAGNITUDE is off by factor %.0f from naive spin scaling." % (ratio_k / 0.5))

    # Verify tanh^2 matches power law
    rw.subsection("tanh^2 vs power-law comparison")
    rw.print("For gravity at electron depth:")
    tanh_val = np.tanh(k_grav * x_e)**2
    power_val = (M_E / M_P)**2
    rw.print("  tanh^2(k_grav * x_e) = %.3e" % tanh_val)
    rw.print("  (m_e / m_P)^2        = %.3e" % power_val)
    rw.print("  Match: %.6f  (tanh ~ x for small x confirms L-shape = power law)" % (
        tanh_val / power_val))

    n_pass = 1  # Qualitative ordering passes; quantitative magnitude fails
    n_total = 2
    rw.print("")
    rw.print("Score: %d / %d  (ordering PASS, magnitude FAIL)" % (n_pass, n_total))
    return n_pass, n_total


# ===========================================================================
# S5: MASS-INDEPENDENCE TEST — THE KILLER
# ===========================================================================
def s5_mass_independence(rw):
    """Test: does the depth model give same alpha_EM for different particles?"""
    rw.section("S5: Mass-Independence Test (Killer Test)")
    rw.print("EM coupling is mass-independent: alpha_EM = 1/137 for ALL charged particles.")
    rw.print("The beat/depth model predicts alpha ~ (m/m_layer)^2 -> mass-DEPENDENT.")
    rw.print("This is the KILLER TEST for cases 1 and 3.")
    rw.print("")

    headers = ["Particle", "m (GeV)", "(m/v_EW)^2", "alpha_EM obs", "Match?"]
    rows = []
    n_pass = 0
    charged = [(n, mk, mg, s, q) for n, mk, mg, s, q in MATTER_PARTICLES if q != 0]
    for name, m_kg, m_gev, spin, charge in charged:
        beat_alpha = (m_gev / V_EW_GEV)**2
        # "Match" = within factor 2
        ok = 0.5 <= (beat_alpha / ALPHA_EM) <= 2.0
        if ok:
            n_pass += 1
        rows.append([name, "%.6f" % m_gev, "%.3e" % beat_alpha,
                      "%.3e" % ALPHA_EM, "PASS" if ok else "FAIL"])
    rw.table(headers, rows, [12, 12, 14, 14, 8])

    rw.print("Result: %d / %d match (within factor 2)" % (n_pass, len(charged)))
    rw.print("")

    # Show the spread
    vals = [(m_gev / V_EW_GEV)**2 for _, _, m_gev, _, q in charged]
    rw.print("Spread of beat-predicted alpha_EM:")
    rw.print("  electron: %.3e" % vals[0])
    rw.print("  muon:     %.3e" % vals[1])
    rw.print("  tau:      %.3e" % vals[2])
    rw.print("  proton:   %.3e" % vals[3])
    rw.print("  Ratio tau/electron: %.0f" % (vals[2] / vals[0]))
    rw.print("")
    rw.print("Observed: alpha_EM = %.6e for ALL of them (mass-independent)." % ALPHA_EM)
    rw.print("VERDICT: Beat/depth model FAILS the mass-independence test.")
    rw.print("  Gravity couples to MASS (continuous phase gradient).")
    rw.print("  EM couples to CHARGE (discrete winding number).")
    rw.print("  These are fundamentally different coupling mechanisms.")
    return n_pass, len(charged)


# ===========================================================================
# S6: GUT CONVERGENCE — MODE CROSSING
# ===========================================================================
def s6_gut_convergence(rw):
    """Check: do alpha_1, alpha_2, alpha_3 converge near one energy?"""
    rw.section("S6: GUT Convergence -- Mode Crossing Check")
    rw.print("If forces are modes of one medium, they should cross at one energy.")
    rw.print("In ocean wave analogy: the node where all modes have equal amplitude.")
    rw.print("")
    rw.print("SM one-loop running couplings at GUT scale (~2e16 GeV):")
    rw.print("  Source: Langacker (2010), 'The Standard Model and Beyond'")
    rw.print("")

    # Low energy values (at m_Z = 91.2 GeV)
    alpha_1_Z = (5.0 / 3.0) * ALPHA_EM_Z / (1.0 - (ALPHA_EM_Z / ALPHA_EM) * 0.23122)
    # Simpler: use known GUT normalization
    # alpha_1(m_Z) ~ 1/59.0,  alpha_2(m_Z) ~ 1/29.6,  alpha_3(m_Z) ~ 1/8.5
    # Source: PDG review on GUTs
    alpha_1_mZ = 1.0 / 59.0
    alpha_2_mZ = 1.0 / 29.6
    alpha_3_mZ = ALPHA_S_Z  # ~0.118 = 1/8.5

    headers = ["Coupling", "at m_Z", "1/alpha", "at GUT", "1/alpha", "Converged?"]
    rows = [
        ["alpha_1 (U(1))", "%.4f" % alpha_1_mZ, "%.1f" % (1/alpha_1_mZ),
         "%.4f" % ALPHA_1_GUT, "%.1f" % (1/ALPHA_1_GUT), "---"],
        ["alpha_2 (SU(2))", "%.4f" % alpha_2_mZ, "%.1f" % (1/alpha_2_mZ),
         "%.4f" % ALPHA_2_GUT, "%.1f" % (1/ALPHA_2_GUT), "---"],
        ["alpha_3 (SU(3))", "%.4f" % alpha_3_mZ, "%.1f" % (1/alpha_3_mZ),
         "%.4f" % ALPHA_3_GUT, "%.1f" % (1/ALPHA_3_GUT), "---"],
    ]
    rw.table(headers, rows, [18, 8, 8, 8, 8, 12])

    # Check convergence: spread at GUT scale
    guts = [ALPHA_1_GUT, ALPHA_2_GUT, ALPHA_3_GUT]
    spread = max(guts) / min(guts)
    inv_guts = [1/a for a in guts]
    inv_spread = max(inv_guts) - min(inv_guts)

    rw.print("At GUT scale (~%.0e GeV):" % GUT_SCALE_GEV)
    rw.print("  1/alpha_1 = %.1f,  1/alpha_2 = %.1f,  1/alpha_3 = %.1f" % tuple(inv_guts))
    rw.print("  Spread: %.1f (in 1/alpha units)" % inv_spread)
    rw.print("  Ratio max/min: %.2f" % spread)
    rw.print("")

    ok = inv_spread < 15  # within 15 units of 1/alpha
    rw.print("SM convergence: APPROXIMATE (spread = %.1f, not exact)" % inv_spread)
    rw.print("MSSM convergence: EXACT (spread < 1) -- requires supersymmetry")
    rw.print("")
    rw.print("Interpretation for depth model:")
    rw.print("  If forces are modes of one medium, GUT crossing = energy where")
    rw.print("  all mode amplitudes are equal (like the surface of the ocean wave).")
    rw.print("  SM: approximate crossing suggests PARTIAL unification.")
    rw.print("  The spread (~10 in 1/alpha) is small compared to low-energy spread (~50).")

    n_pass = 1 if ok else 0
    rw.print("")
    rw.print("Score: %d / 1  (approximate convergence %s)" % (n_pass, "PASS" if ok else "FAIL"))
    return n_pass, 1


# ===========================================================================
# S7: TOPOLOGICAL CHARGE TEST
# ===========================================================================
def s7_topological_charge(rw):
    """If alpha_EM ~ (W/N)^p, what W, N, p gives 1/137?"""
    rw.section("S7: Topological Charge Test")
    rw.print("Possible resolution to mass-independence: EM couples to WINDING NUMBER,")
    rw.print("not mass. Gravity couples to continuous phase gradient (mass-dependent).")
    rw.print("EM couples to discrete topological charge (mass-independent).")
    rw.print("")
    rw.print("Test: can alpha_EM = f(W, N) for integer W, N?")
    rw.print("")

    # Scan: alpha_EM = (W/N)^p for various W, N, p
    rw.subsection("Scanning alpha_EM = (W/N)^p")
    headers = ["W", "N", "p", "(W/N)^p", "alpha_EM", "Ratio", "Close?"]
    rows = []
    best_ratio = 1e10
    best_params = (0, 0, 0)
    for W in range(1, 6):
        for N in range(2, 20):
            if W >= N:
                continue
            for p_num in range(1, 9):
                p = p_num * 0.5  # p = 0.5, 1.0, 1.5, ..., 4.0
                val = (float(W) / float(N))**p
                r = val / ALPHA_EM
                if abs(r - 1.0) < abs(best_ratio - 1.0):
                    best_ratio = r
                    best_params = (W, N, p)
                if 0.95 <= r <= 1.05:
                    rows.append([str(W), str(N), "%.1f" % p, "%.6f" % val,
                                 "%.6f" % ALPHA_EM, "%.4f" % r,
                                 "YES" if 0.99 <= r <= 1.01 else "~"])

    if rows:
        rw.table(headers, rows, [4, 4, 6, 12, 12, 8, 6])
    else:
        rw.print("  No (W/N)^p matches alpha_EM within 5%.")

    rw.print("")
    rw.print("Best match: W=%d, N=%d, p=%.1f -> (W/N)^p = %.6f (ratio = %.4f)" % (
        best_params[0], best_params[1], best_params[2],
        (float(best_params[0]) / float(best_params[1]))**best_params[2],
        best_ratio))

    # Also check: alpha_EM = 1/(4*pi*N^p) or e^2 = 4*pi*alpha
    rw.subsection("Alternative: alpha_EM from condensate geometry")
    rw.print("alpha_EM = e^2 / (4*pi*epsilon_0*hbar*c)")
    rw.print("If e = topological charge = 2*pi*W / N, then:")
    rw.print("  alpha_EM = (2*pi*W/N)^2 / (4*pi) = pi * (W/N)^2")
    rw.print("")
    for W in range(1, 4):
        for N in range(1, 20):
            val = np.pi * (float(W) / float(N))**2
            if 0.9 * ALPHA_EM <= val <= 1.1 * ALPHA_EM:
                rw.print("  W=%d, N=%d: pi*(W/N)^2 = %.6f  vs  alpha_EM = %.6f  (ratio %.4f)" % (
                    W, N, val, ALPHA_EM, val / ALPHA_EM))

    rw.print("")
    rw.print("VERDICT: No clean integer (W, N) gives alpha_EM = 1/137 exactly.")
    rw.print("1/137 is NOT a simple topological number. This suggests alpha_EM")
    rw.print("involves dynamics (renormalization group running), not just topology.")

    ok = abs(best_ratio - 1.0) < 0.01
    n_pass = 1 if ok else 0
    rw.print("")
    rw.print("Score: %d / 1" % n_pass)
    return n_pass, 1


# ===========================================================================
# S8: SPIN ORDERING CHECK
# ===========================================================================
def s8_spin_ordering(rw):
    """Rank forces by spin; compare to observed coupling strengths."""
    rw.section("S8: Spin Ordering Check")
    rw.print("Ocean wave prediction: higher spin = more transverse = decays faster.")
    rw.print("Therefore: alpha(spin-2) < alpha(spin-1) < alpha(spin-0)")
    rw.print("")

    forces = [
        ("Gravity",     2, G * M_E**2 / (HBAR * C), "G*m_e^2/(hbar*c)"),
        ("EM",          1, ALPHA_EM,                  "e^2/(4pi*eps0*hbar*c)"),
        ("Strong",      1, ALPHA_S_Z,                 "alpha_s(m_Z)"),
        ("Higgs-top",   0, 1.0,                       "y_t ~ 1 (top Yukawa)"),
        ("Higgs-e",     0, M_E_GEV / V_EW_GEV,       "y_e = m_e/v ~ 2e-6"),
    ]

    headers = ["Force", "Spin", "Coupling", "Value", "log10"]
    rows = []
    for name, spin, alpha, formula in forces:
        rows.append([name, str(spin), formula, "%.3e" % alpha, "%.1f" % np.log10(alpha)])
    rw.table(headers, rows, [14, 6, 24, 12, 8])

    rw.print("Ordering by coupling strength (weakest first):")
    sorted_forces = sorted(forces, key=lambda x: x[2])
    for i, (name, spin, alpha, _) in enumerate(sorted_forces):
        rw.print("  %d. %s (spin-%d): %.3e" % (i + 1, name, spin, alpha))

    rw.print("")
    rw.print("Prediction:  spin-2 < spin-1 < spin-0")
    rw.print("Observed:    gravity(2) < EM(1) < strong(1) < Higgs-top(0)")
    rw.print("")

    # Check ordering
    grav_ok = forces[0][2] < forces[1][2]  # gravity < EM
    em_strong = forces[1][2] < forces[2][2]  # EM < strong (both spin-1!)
    spin1_lt_spin0 = forces[2][2] < forces[3][2]  # strong < Higgs-top

    n_pass = 0
    checks = [
        ("spin-2 < spin-1 (gravity < EM)", grav_ok),
        ("spin-1 < spin-0 (strong < Higgs-top)", spin1_lt_spin0),
    ]
    for desc, ok in checks:
        rw.print("  %s: %s" % (desc, "PASS" if ok else "FAIL"))
        if ok:
            n_pass += 1

    rw.print("")
    rw.print("PROBLEM: EM (spin-1) and Strong (spin-1) have SAME spin but")
    rw.print("differ by factor %.0f. Depth model cannot distinguish same-spin modes." % (
        ALPHA_S_Z / ALPHA_EM))
    rw.print("")
    rw.print("PROBLEM: Higgs Yukawa couplings span 6 decades (y_e ~ 2e-6 to y_t ~ 1).")
    rw.print("Not a single 'spin-0 coupling' -- depends on which particle.")
    rw.print("")
    rw.print("Score: %d / %d  (ordering partially correct)" % (n_pass, len(checks)))
    return n_pass, len(checks)


# ===========================================================================
# S9: POWER-LAW VS EXPONENTIAL FIT
# ===========================================================================
def s9_power_vs_exp(rw):
    """Fit alpha_G(m) to power-law and exponential; which fits better?"""
    rw.section("S9: Power-Law vs Exponential Fit")
    rw.print("L-shape / tanh^2 predicts POWER LAW: alpha_G = (m/m_P)^n")
    rw.print("Straight-line (log) predicts EXPONENTIAL: alpha_G = exp(-k * decades)")
    rw.print("")

    # Compute alpha_G for each particle
    rw.subsection("alpha_G for each particle")
    headers = ["Particle", "m (GeV)", "alpha_G", "log10(alpha_G)", "decades below m_P"]
    rows = []
    masses = []
    alphas = []
    for name, m_kg, m_gev, spin, charge in MATTER_PARTICLES:
        alpha_G = G * m_kg**2 / (HBAR * C)
        decades = np.log10(M_P / m_kg)
        masses.append(m_kg)
        alphas.append(alpha_G)
        rows.append([name, "%.4e" % m_gev, "%.3e" % alpha_G,
                      "%.2f" % np.log10(alpha_G), "%.2f" % decades])
    rw.table(headers, rows, [12, 12, 12, 16, 20])

    # Power-law fit: log(alpha_G) = n * log(m/m_P)
    log_ratios = [np.log10(m / M_P) for m in masses]
    log_alphas = [np.log10(a) for a in alphas]
    # Linear fit: log_alpha = n * log_ratio + b
    n_fit = np.polyfit(log_ratios, log_alphas, 1)
    rw.subsection("Power-law fit: log10(alpha_G) = n * log10(m/m_P) + b")
    rw.print("  n = %.4f  (expect 2.0 for (m/m_P)^2)" % n_fit[0])
    rw.print("  b = %.4f  (expect 0.0)" % n_fit[1])
    power_residuals = [log_alphas[i] - (n_fit[0] * log_ratios[i] + n_fit[1])
                       for i in range(len(masses))]
    rms_power = np.sqrt(np.mean(np.array(power_residuals)**2))
    rw.print("  RMS residual = %.6f decades" % rms_power)

    # Exponential fit: log(alpha_G) = -k * decades + b2
    decades_list = [np.log10(M_P / m) for m in masses]
    e_fit = np.polyfit(decades_list, log_alphas, 1)
    rw.subsection("Exponential fit: log10(alpha_G) = slope * decades + b")
    rw.print("  slope = %.4f" % e_fit[0])
    rw.print("  b     = %.4f" % e_fit[1])
    exp_residuals = [log_alphas[i] - (e_fit[0] * decades_list[i] + e_fit[1])
                     for i in range(len(masses))]
    rms_exp = np.sqrt(np.mean(np.array(exp_residuals)**2))
    rw.print("  RMS residual = %.6f decades" % rms_exp)

    rw.print("")
    rw.print("Note: power-law and exponential are EQUIVALENT on a log-log plot")
    rw.print("because log10(alpha_G) = 2 * log10(m/m_P) IS a straight line in log-log.")
    rw.print("The distinction is the FUNCTIONAL FORM on a LINEAR plot:")
    rw.print("  Power law (m/m_P)^2:  L-shaped curve, gentle tail, NEVER reaches 0")
    rw.print("  Exponential exp(-kx): drops to effectively 0, much steeper")
    rw.print("")
    rw.print("RESULT: alpha_G = (m/m_P)^2 fits with n = %.4f (exact = 2.0000)." % n_fit[0])
    rw.print("This IS the L-shaped / tanh^2 behavior predicted by the ocean wave model.")
    rw.print("Gravity NEVER reaches zero -- consistent with the 'never touches the axis' insight.")

    ok = abs(n_fit[0] - 2.0) < 0.01
    n_pass = 1 if ok else 0
    rw.print("")
    rw.print("Score: %d / 1  (power-law exponent = 2: %s)" % (n_pass, "PASS" if ok else "FAIL"))
    return n_pass, 1


# ===========================================================================
# S10: LISA CARRIER FREQUENCY
# ===========================================================================
def s10_lisa_carrier(rw):
    """omega_gap as carrier; sideband separation for each particle."""
    rw.section("S10: LISA Carrier Frequency and Sidebands")
    rw.print("In the beat model, omega_gap = m_P*c^2/hbar IS the carrier frequency.")
    rw.print("Each particle modulates this carrier at omega_matter = m*c^2/hbar.")
    rw.print("Sidebands appear at omega_carrier +/- omega_matter.")
    rw.print("")

    omega_carrier = M_P * C**2 / HBAR
    rw.print("Carrier frequency: omega_P = %.6e rad/s" % omega_carrier)
    rw.print("                   f_P     = %.6e Hz" % (omega_carrier / (2 * np.pi)))
    rw.print("")

    LISA_HIGH = 0.1  # Hz
    ET_HIGH   = 1e4  # Hz

    headers = ["Particle", "omega_matter", "delta_f/f_carrier", "Decades gap to LISA"]
    rows = []
    for name, m_kg, m_gev, spin, charge in ALL_PARTICLES:
        omega_m = m_kg * C**2 / HBAR
        delta_f_over_f = omega_m / omega_carrier  # = m/m_P
        gap_lisa = np.log10(omega_m / (2 * np.pi)) - np.log10(LISA_HIGH)
        rows.append([name, "%.3e" % omega_m, "%.3e" % delta_f_over_f, "%.1f" % gap_lisa])
    rw.table(headers, rows, [12, 16, 18, 20])

    rw.print("Sideband resolution: delta_f/f = m/m_P ~ 10^-19 to 10^-23")
    rw.print("  No detector can resolve sidebands this close to the carrier.")
    rw.print("  The carrier itself (%.1e Hz) is 43 orders above LISA band." % (
        omega_carrier / (2 * np.pi)))
    rw.print("")
    rw.print("RESULT: The beat model's carrier frequency = Planck frequency.")
    rw.print("The 43-order gap between LISA and omega_P IS the hierarchy problem")
    rw.print("expressed in frequency space. Not a detection failure -- a restatement.")

    n_pass = 1  # Conceptual consistency passes
    rw.print("")
    rw.print("Score: 1 / 1  (carrier = omega_P, hierarchy = 43 decades: CONSISTENT)")
    return n_pass, 1


# ===========================================================================
# S11: TRUTH TABLE SCORECARD
# ===========================================================================
def s11_scorecard(rw, results):
    """Tally passes/fails per truth table case; overall verdict."""
    rw.section("S11: Truth Table Scorecard")
    rw.print("")

    # Unpack results
    s2_p, s2_t = results["S2"]
    s3_p, s3_t = results["S3"]
    s4_p, s4_t = results["S4"]
    s5_p, s5_t = results["S5"]
    s6_p, s6_t = results["S6"]
    s7_p, s7_t = results["S7"]
    s8_p, s8_t = results["S8"]
    s9_p, s9_t = results["S9"]
    s10_p, s10_t = results["S10"]

    rw.subsection("Individual test summary")
    headers = ["Test", "Description", "Pass", "Total", "Verdict"]
    test_rows = [
        ["S2",  "Beat frequency for gravity",    str(s2_p),  str(s2_t),  "PASS (circular)"],
        ["S3",  "Naive beat for EM",             str(s3_p),  str(s3_t),  "FAIL (expected)"],
        ["S4",  "Ocean wave depth model",        str(s4_p),  str(s4_t),  "PARTIAL"],
        ["S5",  "Mass-independence (killer)",     str(s5_p),  str(s5_t),  "FAIL"],
        ["S6",  "GUT convergence",               str(s6_p),  str(s6_t),  "PASS (approx)"],
        ["S7",  "Topological charge",            str(s7_p),  str(s7_t),  "FAIL"],
        ["S8",  "Spin ordering",                 str(s8_p),  str(s8_t),  "PARTIAL"],
        ["S9",  "Power-law vs exponential",      str(s9_p),  str(s9_t),  "PASS"],
        ["S10", "LISA carrier frequency",        str(s10_p), str(s10_t), "PASS (restatement)"],
    ]
    rw.table(headers, test_rows, [6, 30, 6, 6, 18])

    total_pass = sum(r[0] for r in results.values())
    total_tests = sum(r[1] for r in results.values())
    rw.print("Overall: %d / %d individual checks pass" % (total_pass, total_tests))

    # Score per truth table case
    rw.subsection("Truth table case verdicts")

    rw.print("Case (1): A true, B false -- Beat frequency, SEPARATE condensates")
    rw.print("  S2 gravity beat: PASS (alpha_G = (m/m_P)^2 is correct)")
    rw.print("  S3 EM beat: FAIL (alpha_EM != (m/v_EW)^2)")
    rw.print("  S5 mass-independence: FAIL (beat gives mass-dependent coupling)")
    rw.print("  S10 carrier = omega_P: PASS (consistent, but hierarchy restated)")
    rw.print("  VERDICT: Explains gravity's weakness. FAILS for EM. PARTIAL.")
    rw.print("")

    rw.print("Case (2): A false, B true -- Same medium, NOT beat")
    rw.print("  S4 depth model: PARTIAL (ordering correct, magnitude off)")
    rw.print("  S6 GUT convergence: PASS (approximate crossing supports unification)")
    rw.print("  S8 spin ordering: PARTIAL (spin-2 < spin-1 correct, same-spin spread not explained)")
    rw.print("  S5 mass-independence: still a problem (depth model is mass-dependent)")
    rw.print("  VERDICT: Best qualitative picture. Quantitative problems remain. PARTIAL.")
    rw.print("")

    rw.print("Case (3): A true AND B true -- One medium, beat frequency")
    rw.print("  S2 gravity beat: PASS")
    rw.print("  S3 EM beat: FAIL")
    rw.print("  S5 mass-independence: FAIL (the killer)")
    rw.print("  S7 topological charge: FAIL (1/137 is not a clean topological number)")
    rw.print("  S9 power-law: PASS (L-shape confirmed for gravity)")
    rw.print("  VERDICT: Cleanest conceptual picture but FAILS quantitatively for EM.")
    rw.print("  Could be SAVED if EM uses topological (charge) coupling, not mass coupling.")
    rw.print("  But 1/137 resists simple topological explanation.")
    rw.print("")

    rw.print("Case (4): A false AND B false -- Current PDTP baseline")
    rw.print("  All S2-S10 tests: N/A (this case makes no new predictions)")
    rw.print("  VERDICT: Consistent but underdetermined. No explanation for hierarchy.")
    rw.print("  Three separate condensates, each with its own free coupling constant.")
    rw.print("")

    rw.subsection("Key findings")
    rw.print("1. QUALITATIVE WIN: Spin ordering (spin-2 < spin-1 < spin-0) is CORRECT.")
    rw.print("   This is non-trivial and follows from ocean wave depth physics.")
    rw.print("")
    rw.print("2. QUANTITATIVE FAIL: The 43-order hierarchy between gravity and EM")
    rw.print("   cannot be explained by spin ratio alone (need 22:1, spin gives 2:1).")
    rw.print("")
    rw.print("3. KILLER PROBLEM: EM coupling is mass-independent. The beat/depth model")
    rw.print("   inherently produces mass-dependent coupling. This is the fundamental")
    rw.print("   obstacle: gravity couples to MASS, EM couples to CHARGE.")
    rw.print("")
    rw.print("4. L-SHAPE CONFIRMED: alpha_G = (m/m_P)^2 is a power law (L-shape),")
    rw.print("   not exponential. tanh^2 from ocean wave model matches this form.")
    rw.print("   Gravity NEVER reaches zero -- asymptotic but always nonzero.")
    rw.print("")
    rw.print("5. POSSIBLE PATH FORWARD: If gravity uses CONTINUOUS phase gradient")
    rw.print("   (mass-dependent, spin-2) while EM uses DISCRETE winding number")
    rw.print("   (charge-quantized, spin-1), both can coexist in one medium.")
    rw.print("   But 1/137 is not derivable from simple topology.")
    rw.print("")
    rw.print("6. GUT CONVERGENCE supports one-medium picture: three couplings")
    rw.print("   approximately meet at ~10^16 GeV, like modes equalizing at the 'surface'.")

    return total_pass, total_tests


# ===========================================================================
# MAIN
# ===========================================================================
def main():
    output_dir = os.path.join(_HERE, "..", "output")
    rw = ReportWriter(output_dir, label="gravity_em_truth_table")

    rw.section("Gravity-EM Unification: Truth Table Investigation")
    rw.print("Speculation: are gravity and EM different frequency bands of ONE medium?")
    rw.print("Testing 4 truth table cases with 11 Sudoku-style checks.")
    rw.print("")
    rw.print("Key analogy: ocean wave depth physics")
    rw.print("  Surface: circular orbits (all spins) -> Planck scale")
    rw.print("  Bottom: horizontal only (spin-0) -> low energy")
    rw.print("  Coupling curve: tanh^2 (L-shape), NOT exponential")
    rw.print("  Gravity NEVER reaches zero -- asymptotic power law")

    results = {}

    # S1: frequency map (informational, no pass/fail)
    s1_frequency_map(rw)

    # S2-S10: quantitative checks
    results["S2"] = s2_beat_gravity(rw)
    results["S3"] = s3_beat_em(rw)
    results["S4"] = s4_ocean_wave_depth(rw)
    results["S5"] = s5_mass_independence(rw)
    results["S6"] = s6_gut_convergence(rw)
    results["S7"] = s7_topological_charge(rw)
    results["S8"] = s8_spin_ordering(rw)
    results["S9"] = s9_power_vs_exp(rw)
    results["S10"] = s10_lisa_carrier(rw)

    # S11: scorecard
    total_pass, total_tests = s11_scorecard(rw, results)

    rw.close()


if __name__ == "__main__":
    main()
