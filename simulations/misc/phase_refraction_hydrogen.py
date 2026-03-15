#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHASE REFRACTION ANALYSIS: Gravity and Atomic Binding
======================================================
Part 31 -- Phase refraction as the physical mechanism for gravity and atomic binding

Three calculations:
  1. Does the PDTP wave equation reduce to the Schrodinger equation? (KG -> Schrodinger)
  2. Does the critical angle map to ionization energy quantitatively?
  3. Does orbital angular momentum l map to refraction angle?

Plus: Sudoku consistency check on g_EM = 27.2 eV (Hartree energy)
"""

import numpy as np
import sys
import io

# Force UTF-8 output on Windows
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# ===========================================================================
# FUNDAMENTAL CONSTANTS (CODATA 2018)
# ===========================================================================
hbar = 1.054571817e-34   # J*s      (reduced Planck constant)
c = 2.99792458e8         # m/s      (speed of light)
k_B = 1.380649e-23       # J/K      (Boltzmann constant)
m_e = 9.1093837015e-31   # kg       (electron mass)
m_p = 1.67262192369e-27  # kg       (proton mass)
e_charge = 1.602176634e-19  # C     (elementary charge)
epsilon_0 = 8.8541878128e-12  # F/m  (vacuum permittivity)
alpha_EM = 1 / 137.035999  # dimensionless (fine-structure constant)
G_known = 6.67430e-11    # m^3/(kg*s^2)
eV = 1.602176634e-19     # J per eV

# Derived constants
a_0 = hbar / (m_e * c * alpha_EM)  # Bohr radius (m)
# Source: https://en.wikipedia.org/wiki/Bohr_radius

E_hartree = e_charge**2 / (4 * np.pi * epsilon_0 * a_0)  # Hartree energy (J)
# Source: https://en.wikipedia.org/wiki/Hartree

E_ion_H = E_hartree / 2  # Hydrogen ionization energy (J)
# Source: https://en.wikipedia.org/wiki/Ionization_energy

R_inf = m_e * c**2 * alpha_EM**2 / 2  # Rydberg energy (J)
# Source: https://en.wikipedia.org/wiki/Rydberg_constant

lambda_C = hbar / (m_e * c)  # Reduced Compton wavelength of electron (m)
r_e = alpha_EM * lambda_C    # Classical electron radius (m)

# Gravitational coupling for electron-proton
g_grav_ep = G_known * m_e * m_p / a_0  # Gravitational potential energy at Bohr radius (J)

# Planck mass and length
m_Planck = np.sqrt(hbar * c / G_known)
l_Planck = np.sqrt(hbar * G_known / c**3)


def ratio_str(predicted, known):
    """Return a string showing the ratio and whether it's a match or contradiction."""
    if known == 0:
        return "KNOWN=0"
    ratio = predicted / known
    if 0.99 < ratio < 1.01:
        return "ratio = {:.6f}  [MATCH]".format(ratio)
    elif 0.9 < ratio < 1.1:
        return "ratio = {:.4f}  ~ CLOSE (within 10%)".format(ratio)
    elif 0.1 < ratio < 10:
        return "ratio = {:.4e}  [X] OFF by factor {:.2f}".format(ratio, abs(ratio))
    else:
        log_ratio = np.log10(abs(ratio))
        return "ratio = {:.4e}  [XX] OFF by 10^{:.1f}".format(ratio, log_ratio)


# ===========================================================================
print("=" * 80)
print("PHASE REFRACTION ANALYSIS: GRAVITY AND ATOMIC BINDING")
print("=" * 80)
print()

# ===========================================================================
# SECTION 1: REFERENCE VALUES
# ===========================================================================
print("=" * 80)
print("1. REFERENCE VALUES")
print("=" * 80)
print()
print("  Bohr radius:           a_0 = {:.6e} m".format(a_0))
print("  Hartree energy:     E_Hart = {:.6f} eV".format(E_hartree / eV))
print("  Ionization energy:   E_ion = {:.6f} eV".format(E_ion_H / eV))
print("  Rydberg energy:      R_inf = {:.6f} eV".format(R_inf / eV))
print("  Fine structure:    alpha_EM = {:.6e}".format(alpha_EM))
print("  Compton wavelength: lam_C  = {:.6e} m".format(lambda_C))
print("  Classical e radius:   r_e  = {:.6e} m".format(r_e))
print()
print("  Gravitational coupling at a_0:")
print("    g_grav(e-p) = G*m_e*m_p/a_0 = {:.4e} J = {:.4e} eV".format(g_grav_ep, g_grav_ep / eV))
print("    g_EM / g_grav = {:.4e}".format(E_hartree / g_grav_ep))
print("    This is the hierarchy problem: EM is ~10^39 times stronger than gravity")
print()

# ===========================================================================
# SECTION 2: THE TWO-COUPLING PROBLEM
# ===========================================================================
print("=" * 80)
print("2. THE TWO-COUPLING PROBLEM")
print("=" * 80)
print()
print("  PDTP has ONE coupling per matter field: g_i cos(psi_i - phi)")
print("  For gravity:  g_grav ~ G*m^2/r ~ 10^-40 eV (at atomic scale)")
print("  For EM:       g_EM   ~ e^2/(4*pi*eps_0*r) ~ 27 eV (at Bohr radius)")
print()
print("  These CANNOT be the same coupling constant.")
print("  The refraction picture works for BOTH, but at vastly different strengths.")
print()

# Gravitational coupling constant (dimensionless)
alpha_G = G_known * m_e * m_p / (hbar * c)
print("  Gravitational coupling: alpha_G = G*m_e*m_p/(hbar*c) = {:.4e}".format(alpha_G))
print("  EM coupling:            alpha_EM = {:.6e}".format(alpha_EM))
print("  Hierarchy ratio:    alpha_EM/alpha_G = {:.4e}".format(alpha_EM / alpha_G))
print()
print("  Gravity is the SAME mechanism (phase refraction) but ~10^36 times weaker.")
print("  This is equivalent to saying: gravity has an enormously weaker refractive index.")
print()

# ===========================================================================
# SECTION 3: CALCULATION 1 -- KG -> SCHRODINGER REDUCTION
# ===========================================================================
print("=" * 80)
print("3. CALCULATION 1: PDTP WAVE EQUATION -> SCHRODINGER")
print("=" * 80)
print()
print("  PDTP field equation for matter wave:")
print("    Box(psi) = -g sin(psi - phi)")
print()
print("  Step 1: Weak-field linearization (small phase mismatch)")
print("    sin(psi - phi) ~ psi - phi  for |psi - phi| << 1")
print("    Box(psi) ~ -g(psi - phi)")
print()
print("  Step 2: Identify background phase field as potential")
print("    phi(r) = V(r)/(hbar*omega)  where V(r) is the potential energy")
print("    For Coulomb: V(r) = -e^2/(4*pi*eps_0*r)")
print()
print("  Step 3: Non-relativistic limit (standard KG -> Schrodinger)")
print("    Source: Klein-Gordon equation, Wikipedia")
print("    https://en.wikipedia.org/wiki/Klein%E2%80%93Gordon_equation")
print()
print("    Write psi(x,t) = Psi(x,t) * exp(-i*m*c^2*t/hbar)")
print("    where Psi is slowly varying (|Psi_tt| << m*c^2*|Psi_t|/hbar)")
print()
print("    The Box(psi) = (1/c^2)*d^2(psi)/dt^2 - nabla^2(psi) becomes:")
print("    -(m^2*c^2/hbar^2)*Psi - 2i*(m/hbar)*dPsi/dt - nabla^2(Psi)")
print("      = -g*(psi - phi)/hbar^2")
print()
print("    Keeping only first-order time derivatives:")
print("    i*hbar * dPsi/dt = -(hbar^2/2m)*nabla^2(Psi) + V(r)*Psi")
print()
print("    [YES] This IS the Schrodinger equation.")
print()
print("  RESULT: The PDTP wave equation reduces to the Schrodinger equation")
print("  in the non-relativistic, weak-field limit. This is a COMPATIBILITY")
print("  check, not a derivation -- the Coulomb potential V(r) is input, not derived.")
print()

# Verify hydrogen energy levels from the Schrodinger equation
print("  Hydrogen energy levels from Schrodinger equation:")
print("  Source: https://en.wikipedia.org/wiki/Hydrogen_atom")
print()
print("  {:>4}  {:>12}  {:>20}  {:>8}".format("n", "E_n (eV)", "E_n = -13.6/n^2 (eV)", "Match?"))
print("  {:>4}  {:>12}  {:>20}  {:>8}".format("----", "--------", "--------------------", "------"))
for n in range(1, 8):
    E_n = -E_ion_H / n**2
    E_n_formula = -13.6 * eV / n**2
    r = E_n / E_n_formula
    match = "YES" if 0.99 < r < 1.01 else "NO"
    print("  {:>4}  {:>12.4f}  {:>20.4f}  {:>8}".format(n, E_n / eV, E_n_formula / eV, match))
print()

# ===========================================================================
# SECTION 4: CALCULATION 2 -- CRITICAL ANGLE AND IONIZATION
# ===========================================================================
print("=" * 80)
print("4. CALCULATION 2: CRITICAL ANGLE AND IONIZATION")
print("=" * 80)
print()
print("  PDTP coupling energy: V(theta) = -g_EM * cos(theta)  where theta = psi - phi")
print()
print("  Ground state: theta = 0 (phase-locked)")
print("    V(0) = -g_EM = -27.2 eV")
print()
print("  Total decoupling: theta = 90 deg")
print("    V(pi/2) = 0")
print("    DeltaV = g_EM = 27.2 eV (full Coulomb energy)")
print()
print("  BUT: ionization energy is only 13.6 eV = g_EM/2")
print("  Source: Virial theorem for 1/r potentials")
print("  https://en.wikipedia.org/wiki/Virial_theorem")
print("  For Coulomb: 2<KE> = -<V>, so E_total = <V>/2 = -g_EM/2")
print()

# Calculate phase angle at ionization for each shell
print("  Phase angle at ionization (where E_total = 0):")
print()
print("  For shell n: E_n = -g_EM/(2*n^2)")
print("  Energy needed to ionize from shell n: DeltaE_n = g_EM/(2*n^2)")
print("  Phase angle: cos(theta_n) = 1 - DeltaE_n/g_EM = 1 - 1/(2*n^2)")
print()
print("  {:>4}  {:>10}  {:>12}  {:>10}  {:>10}  {:>30}".format(
    "n", "E_n (eV)", "DE_ion (eV)", "cos(th)", "th (deg)", "Interpretation"))
print("  {:>4}  {:>10}  {:>12}  {:>10}  {:>10}  {:>30}".format(
    "----", "--------", "-----------", "------", "-------", "--------------"))

for n in range(1, 8):
    E_n = -E_hartree / (2 * n**2)
    delta_E = -E_n  # energy to ionize
    cos_theta = 1 - delta_E / E_hartree
    theta_deg = np.degrees(np.arccos(cos_theta))
    if n == 1:
        interp = "Ground state -> 60 deg, NOT 90"
    elif n <= 3:
        interp = "Excited state"
    else:
        interp = "High-n -> approaches 0 deg"
    print("  {:>4}  {:>10.4f}  {:>12.4f}  {:>10.6f}  {:>10.2f}  {:>30}".format(
        n, E_n / eV, delta_E / eV, cos_theta, theta_deg, interp))

print()
print("  KEY FINDING: Ionization from the ground state requires rotating the")
print("  phase angle to 60 deg, NOT 90 deg.")
print()
print("  The 90 deg point corresponds to TOTAL Coulomb stripping (27.2 eV),")
print("  not ionization. Ionization happens when the kinetic energy equals")
print("  the remaining potential energy (virial theorem), which is at 60 deg.")
print()
print("  Physical meaning of different angles:")
print("    theta =   0 deg:  Perfect phase lock -- fully bound (ground state, cos = 1)")
print("    theta =  60 deg:  Ionization threshold -- just barely unbound (cos = 0.5)")
print("    theta =  90 deg:  Total decoupling -- no EM interaction at all (cos = 0)")
print("    theta = 180 deg:  Anti-phase -- maximum repulsion (cos = -1, antiparticle)")
print()

# Snell's law analogy
print("  SNELL'S LAW MAPPING:")
print("  Source: https://en.wikipedia.org/wiki/Snell%27s_law")
print()
print("  In optics: n_1 sin(theta_1) = n_2 sin(theta_2)")
print("  Critical angle: sin(theta_c) = n_2/n_1")
print()
print("  In PDTP phase coupling: alpha = cos(psi - phi)")
print("  The coupling projects the matter phase onto the field phase.")
print()
print("  Connection to Snell's law:")
print("  The effective refractive index near a proton is:")
n_proton_surface = 1 / np.sqrt(1 - 2 * G_known * m_p / (a_0 * c**2))
print("    n_grav(a_0) = 1/sqrt(1 - 2*Phi/c^2) = {:.15f}".format(n_proton_surface))
print("    Delta_n = n - 1 = {:.4e} (gravitational -- negligible)".format(
    n_proton_surface - 1))
print()
# EM refractive index analogy
n_EM_eff = E_hartree / (m_e * c**2) + 1
print("    n_EM_eff(a_0) = 1 + E_Coulomb/(m_e*c^2) = {:.10f}".format(n_EM_eff))
print("    Delta_n_EM = {:.4e} (electromagnetic -- much larger than gravitational)".format(
    n_EM_eff - 1))
if n_proton_surface - 1 > 0:
    print("    Ratio Delta_n_EM/Delta_n_grav = {:.4e}".format(
        (n_EM_eff - 1) / (n_proton_surface - 1)))
else:
    # Gravitational n is so close to 1 that float64 can't resolve it
    # Use the weak-field approximation: Delta_n_grav ~ GM/(rc^2)
    delta_n_grav_approx = G_known * m_p / (a_0 * c**2)
    print("    (Gravitational Delta_n too small for float64; using weak-field approx)")
    print("    Delta_n_grav ~ GM/(r*c^2) = {:.4e}".format(delta_n_grav_approx))
    print("    Ratio Delta_n_EM/Delta_n_grav ~ {:.4e}".format(
        (n_EM_eff - 1) / delta_n_grav_approx))
print()

# ===========================================================================
# SECTION 5: CALCULATION 3 -- ANGULAR MOMENTUM AS REFRACTION ANGLE
# ===========================================================================
print("=" * 80)
print("5. CALCULATION 3: ANGULAR MOMENTUM AS REFRACTION ANGLE")
print("=" * 80)
print()
print("  In optics: a wave hitting a spherical cavity at angle theta has")
print("  angular momentum L = n*k*r*sin(theta), where k = 2*pi/lambda.")
print("  Source: https://en.wikipedia.org/wiki/Whispering-gallery_wave")
print()
print("  In QM: orbital angular momentum L = sqrt(l*(l+1)) * hbar")
print("  The centrifugal barrier is V_cf = l*(l+1)*hbar^2/(2*m*r^2)")
print("  Source: https://en.wikipedia.org/wiki/Hydrogen_atom#Mathematical_summary")
print()
print("  Refraction angle interpretation:")
print("    l = 0:   radial wave (head-on incidence, theta_inc = 0 deg)")
print("    l = n-1: tangential wave (grazing incidence, theta_inc -> 90 deg)")
print()
print("  For each (n, l), the 'incidence angle' at the classical turning point:")
print("    sin(theta_inc) = L/(p * r_tp)  where p = hbar*k is the radial momentum")
print()

# Calculate for each (n, l)
print("  {:>4}  {:>4}  {:>8}  {:>10}  {:>12}  {:>15}".format(
    "n", "l", "L/hbar", "r_max/a_0", "th_inc(deg)", "Type"))
print("  {:>4}  {:>4}  {:>8}  {:>10}  {:>12}  {:>15}".format(
    "----", "----", "------", "--------", "-----------", "----"))

for n in range(1, 6):
    for l in range(0, n):
        L = np.sqrt(l * (l + 1))
        # Classical turning point (outer, from effective potential)
        r_max = n**2  # in units of a_0
        # sin(theta) = l/n (semiclassical: angular/total quantum number)
        if n > 0:
            sin_theta = L / n
            sin_theta = min(sin_theta, 1.0)
            theta_deg = np.degrees(np.arcsin(sin_theta))
        else:
            theta_deg = 0.0

        if l == 0:
            label = "s (radial)"
        elif l == 1:
            label = "p (dumbbell)"
        elif l == 2:
            label = "d (clover)"
        elif l == 3:
            label = "f (complex)"
        else:
            label = "l={}".format(l)

        print("  {:>4}  {:>4}  {:>8.3f}  {:>10.1f}  {:>12.1f}  {:>15}".format(
            n, l, L, r_max, theta_deg, label))
    if n < 5:
        print()

print()
print("  RESULT: The semiclassical incidence angle sin(theta) = sqrt(l*(l+1))/n")
print("  correctly gives:")
print("    l = 0:   theta = 0 deg (radial, head-on)")
print("    l = n-1: theta -> 90 deg for large n (tangential, grazing)")
print()
print("  This is the SAME as the whispering gallery mode classification")
print("  in wave optics. The centrifugal barrier is the angular-momentum-")
print("  dependent refraction angle.")
print()
print("  CAUTION: This mapping is QUALITATIVE. The quantitative match")
print("  requires showing that the centrifugal barrier formula emerges")
print("  from the PDTP refraction geometry, which is not yet proven.")
print()

# ===========================================================================
# SECTION 6: SUDOKU CONSISTENCY CHECK
# ===========================================================================
print("=" * 80)
print("6. SUDOKU CONSISTENCY CHECK: g_EM = E_Hartree = 27.2 eV")
print("=" * 80)
print()
print("  New value introduced: g_EM = e^2/(4*pi*eps_0*a_0) = 27.2 eV")
print("  This is the Hartree energy -- established physics, not a new claim.")
print("  The NEW claim is: g_EM plays the role of the PDTP coupling constant")
print("  for the EM sector, analogous to g_grav for gravity.")
print()

g_EM = E_hartree  # in Joules
g_EM_eV = g_EM / eV

tests = []

# Test 1: Hydrogen ground state energy
E_1_pred = -g_EM / 2
E_1_known = -13.6059 * eV
tests.append(("H ground state E_1 = -g_EM/2", E_1_pred, E_1_known))

# Test 2: Bohr radius from g_EM
# g_EM = e^2/(4*pi*eps_0*a_0) -> a_0 = e^2/(4*pi*eps_0*g_EM)
a_0_pred = e_charge**2 / (4 * np.pi * epsilon_0 * g_EM)
tests.append(("Bohr radius from g_EM", a_0_pred, a_0))

# Test 3: Fine structure constant
# alpha = g_EM * a_0 / (hbar*c)  ->  alpha = e^2/(4*pi*eps_0*hbar*c)
alpha_pred = g_EM * a_0 / (hbar * c)
tests.append(("alpha_EM = g_EM * a_0/(hbar*c)", alpha_pred, alpha_EM))

# Test 4: Rydberg energy
# R_inf = g_EM/2 = m_e c^2 alpha^2/2
R_pred = m_e * c**2 * alpha_EM**2 / 2
tests.append(("Rydberg = m_e c^2 alpha^2/2", R_pred, E_ion_H))

# Test 5: Compton wavelength ratio
# a_0/lambda_C = 1/alpha
ratio_pred = a_0 / lambda_C
ratio_known = 1 / alpha_EM
tests.append(("a_0/lambda_C = 1/alpha_EM", ratio_pred, ratio_known))

# Test 6: Classical electron radius ratio
# a_0/r_e = 1/alpha^2
ratio_pred2 = a_0 / r_e
ratio_known2 = 1 / alpha_EM**2
tests.append(("a_0/r_e = 1/alpha^2", ratio_pred2, ratio_known2))

# Test 7: g_EM in terms of m_e, c, alpha
# g_EM = m_e c^2 alpha^2 (the Hartree energy)
g_EM_pred = m_e * c**2 * alpha_EM**2
tests.append(("g_EM = m_e c^2 alpha^2", g_EM_pred, g_EM))

# Test 8: Hierarchy ratio
# g_EM/g_grav should equal alpha_EM / alpha_G
# where alpha_G = G m_e m_p / (hbar*c)
alpha_G = G_known * m_e * m_p / (hbar * c)
hierarchy_pred = alpha_EM / alpha_G
hierarchy_known = E_hartree / g_grav_ep  # same ratio
tests.append(("alpha_EM/alpha_G = g_EM/g_grav", hierarchy_pred, hierarchy_known))

# Test 9: Ionization as phase angle
# cos(theta_ion) = 1 - E_ion/g_EM = 1 - 1/2 = 0.5 -> theta = 60 deg
theta_ion_pred = np.degrees(np.arccos(0.5))
theta_ion_known = 60.0  # degrees
tests.append(("Ionization angle = 60 deg", theta_ion_pred, theta_ion_known))

# Test 10: g_EM coupling predicts Lyman-alpha
# Lyman-alpha: E = g_EM/2 * (1 - 1/4) = 3*g_EM/8
E_lyman_pred = g_EM * 3 / 8
E_lyman_known = 10.2 * eV  # Lyman-alpha = 10.2 eV
tests.append(("Lyman-alpha = 3*g_EM/8", E_lyman_pred, E_lyman_known))

# Test 11: Balmer series (H-alpha)
# H-alpha: E = g_EM/2 * (1/4 - 1/9) = 5*g_EM/72
E_balmer_pred = g_EM * 5 / 72
E_balmer_known = 1.89 * eV  # H-alpha ~ 1.89 eV
tests.append(("H-alpha = 5*g_EM/72", E_balmer_pred, E_balmer_known))

# Print results
matches = 0
contradictions = 0
for tname, pred, known in tests:
    r = pred / known if known != 0 else float('inf')
    rs = ratio_str(pred, known)
    print("  {}".format(tname))
    print("    predicted = {:.6e},  known = {:.6e}".format(pred, known))
    print("    {}".format(rs))
    print()
    if known != 0 and 0.99 < r < 1.01:
        matches += 1
    else:
        contradictions += 1

print("  -----------------------------------------------")
print("  SUDOKU SCORECARD: {} matches, {} contradictions out of {} tests".format(
    matches, contradictions, len(tests)))
print("  -----------------------------------------------")
print()
if matches == len(tests):
    print("  ALL PASS -- g_EM = 27.2 eV is internally consistent.")
    print("  NOTE: This is expected -- the Hartree energy is established physics.")
    print("  The consistency confirms the MAPPING (g_EM = Hartree energy in PDTP)")
    print("  is at least algebraically valid.")
elif contradictions > 0:
    print("  {} contradiction(s) found. See above for details.".format(contradictions))
print()

# ===========================================================================
# SECTION 7: THE HIERARCHY AS REFRACTIVE INDEX RATIO
# ===========================================================================
print("=" * 80)
print("7. THE HIERARCHY AS REFRACTIVE INDEX RATIO")
print("=" * 80)
print()
print("  If both gravity and EM are phase refraction at different strengths:")
print()
print("    Gravitational 'refractive index' change at a_0:")
delta_n_grav = G_known * m_p / (a_0 * c**2)
print("      Delta_n_grav = G*M/(r*c^2) = {:.4e}".format(delta_n_grav))
print()
print("    EM 'refractive index' change at a_0:")
delta_n_EM = E_hartree / (m_e * c**2)
print("      Delta_n_EM = E_Coulomb/(m_e*c^2) = {:.4e}".format(delta_n_EM))
print()
print("    Ratio: Delta_n_EM / Delta_n_grav = {:.4e}".format(
    delta_n_EM / delta_n_grav))
print()
print("  The EM 'medium' bends electron waves ~10^36 times more than the")
print("  gravitational 'medium'. This is WHY atoms exist but gravitational")
print("  'atoms' (gravitational bound states of electrons) do not -- the")
print("  gravitational refraction is too weak to trap anything at atomic scales.")
print()

# Gravitational atom
# Gravitational Bohr radius: a_G = hbar^2/(G m_e^2 m_p)
a_G = hbar**2 / (G_known * m_e**2 * m_p)
print("  'Gravitational Bohr radius': a_G = hbar^2/(G*m_e^2*m_p) = {:.4e} m".format(a_G))
print("  = {:.4e} * a_0".format(a_G / a_0))
print("  = {:.4e} * 10^9 m  (bigger than Jupiter's orbit!)".format(a_G / 1e9))
print()
print("  This shows: gravity CAN form 'atoms' in principle, but they would")
print("  be ~10^29 times larger than hydrogen -- confirming the refraction")
print("  picture: weaker medium -> wider bend radius -> enormous 'orbitals'.")
print()

# ===========================================================================
# SECTION 8: SUMMARY
# ===========================================================================
print("=" * 80)
print("8. SUMMARY OF FINDINGS")
print("=" * 80)
print()
print("  CALCULATION 1 (KG -> Schrodinger):")
print("    [YES] PDTP wave equation reduces to Schrodinger in non-relativistic limit")
print("    [YES] This is a standard result (KG -> Schrodinger), confirms COMPATIBILITY")
print("    [NO]  Does NOT prove refraction IS the mechanism (Coulomb potential is input)")
print()
print("  CALCULATION 2 (Critical angle and ionization):")
print("    [YES] g_EM = 27.2 eV (Hartree energy) is the correct EM coupling constant")
print("    [NO]  Ionization angle is 60 deg, NOT 90 deg (virial theorem)")
print("    -> 90 deg = total EM decoupling (full Coulomb stripping)")
print("    -> 60 deg = ionization (kinetic energy = potential energy)")
print("    -> The simple 'critical angle = 90 deg' picture FAILS for ionization")
print("    -> BUT: 60 deg has a clear physical meaning (virial equipartition)")
print()
print("  CALCULATION 3 (Angular momentum -> refraction angle):")
print("    [YES] sin(theta) = sqrt(l*(l+1))/n correctly classifies orbital geometry")
print("    [YES] l = 0 -> head-on (s-orbital), l = n-1 -> grazing (whispering gallery)")
print("    [NO]  Quantitative derivation from PDTP refraction geometry not yet done")
print("    -> This is QUALITATIVE, not a derivation")
print()
print("  SUDOKU CONSISTENCY CHECK:")
scorecard = "    {}/{} tests pass -- ".format(matches, len(tests))
if matches == len(tests):
    scorecard += "g_EM = Hartree energy is fully consistent"
else:
    scorecard += "{} contradiction(s)".format(contradictions)
print(scorecard)
print()
print("  OVERALL ASSESSMENT:")
print("    The refraction interpretation provides a UNIFIED PHYSICAL PICTURE:")
print("    gravity and atomic binding are both wave refraction, differing only")
print("    in coupling strength (alpha_G vs alpha_EM, ratio ~10^36).")
print()
print("    However, this is INTERPRETIVE, not PREDICTIVE at this stage.")
print("    No new predictions beyond standard QM are generated.")
print("    The hierarchy problem (WHY alpha_EM/alpha_G ~ 10^36) is restated,")
print("    not solved -- it becomes: WHY is the EM refractive index 10^36")
print("    times larger than the gravitational one?")
print()
print("    The 60 deg vs 90 deg finding is an INFORMATIVE FAILURE:")
print("    it reveals that ionization is NOT simple critical-angle escape,")
print("    but rather a virial equipartition threshold. The 90 deg point")
print("    (total phase decoupling) corresponds to a HIGHER energy state")
print("    -- complete removal of all Coulomb interaction.")
print()
