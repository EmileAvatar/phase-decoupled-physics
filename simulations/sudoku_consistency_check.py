#!/usr/bin/env python3
"""
SUDOKU CONSISTENCY CHECK
========================
Independent of PDTP. Pure calculation exercise.

Premise: We have one G-free result:
    K = hbar / (4*pi*c)   ("quantum of spring constant")

This uses ONLY hbar and c — no G.

To get G, we also need a lattice spacing 'a', since:
    kappa = K / a^2       (bulk modulus from spring constant and spacing)
    G = c^2 / (4*pi*kappa)  (bridge relation)

We test three candidates for 'a':
    A) a = Planck length  l_P = sqrt(hbar*G/c^3)  [circular — control case]
    B) a = electron reduced Compton wavelength  hbar/(m_e*c)
    C) a = proton reduced Compton wavelength    hbar/(m_p*c)

For each candidate, we:
    1. Compute G_predicted
    2. Propagate through ALL standard physics equations
    3. Compare every result to the known measured value
    4. Flag contradictions ("duplicate numbers" in the Sudoku)

If a candidate completes the puzzle (all results match reality), the
assumption was correct. If contradictions appear, it was wrong.
"""

import numpy as np

# ===========================================================================
# FUNDAMENTAL CONSTANTS (CODATA 2018, non-gravitational)
# ===========================================================================
hbar = 1.054571817e-34   # J·s      (reduced Planck constant)
c = 2.99792458e8         # m/s      (speed of light)
k_B = 1.380649e-23       # J/K      (Boltzmann constant)
m_e = 9.1093837015e-31   # kg       (electron mass)
m_p = 1.67262192369e-27  # kg       (proton mass)
M_sun = 1.98892e30       # kg       (solar mass)
alpha_EM = 1/137.035999  # dimensionless (fine-structure constant)
H_0_si = 2.1843e-18      # s^-1     (Hubble constant, 67.4 km/s/Mpc)
e_charge = 1.602176634e-19  # C     (elementary charge)

# Known G for comparison
G_known = 6.67430e-11    # m^3/(kg·s^2)

# ===========================================================================
# THE ASSUMED VALUE: K = hbar / (4*pi*c)
# ===========================================================================
K_assumed = hbar / (4 * np.pi * c)
print("=" * 80)
print("SUDOKU CONSISTENCY CHECK")
print("=" * 80)
print()
print(f"ASSUMED: K = hbar / (4*pi*c) = {K_assumed:.6e} J")
print(f"  (Uses ONLY hbar and c — no G)")
print()

# ===========================================================================
# THREE CANDIDATES FOR LATTICE SPACING
# ===========================================================================
# Planck length (uses G — circular, serves as control)
l_P = np.sqrt(hbar * G_known / c**3)

candidates = {
    "A: Planck length (CONTROL)": {
        "a": l_P,
        "formula": "sqrt(hbar*G/c^3)",
        "circular": True,
        "note": "Uses G — should recover everything exactly. Control case."
    },
    "B: Electron Compton wavelength": {
        "a": hbar / (m_e * c),
        "formula": "hbar/(m_e*c)",
        "circular": False,
        "note": "G-free. Uses only hbar, c, m_e."
    },
    "C: Proton Compton wavelength": {
        "a": hbar / (m_p * c),
        "formula": "hbar/(m_p*c)",
        "circular": False,
        "note": "G-free. Uses only hbar, c, m_p."
    },
}

# ===========================================================================
# KNOWN MEASURED VALUES (to compare against)
# ===========================================================================
r_s_sun_known = 2 * G_known * M_sun / c**2  # Schwarzschild radius of Sun
T_H_sun_known = hbar * c**3 / (8 * np.pi * G_known * M_sun * k_B)  # Hawking T of solar-mass BH
rho_crit_known = 3 * H_0_si**2 / (8 * np.pi * G_known)  # critical density
l_P_known = np.sqrt(hbar * G_known / c**3)  # Planck length
t_P_known = np.sqrt(hbar * G_known / c**5)  # Planck time
m_P_known = np.sqrt(hbar * c / G_known)     # Planck mass
E_P_known = m_P_known * c**2                # Planck energy
T_P_known = E_P_known / k_B                 # Planck temperature
alpha_G_known = G_known * m_p**2 / (hbar * c)  # gravitational coupling (proton)
S_BH_sun = 4 * np.pi * G_known * M_sun**2 / (hbar * c)  # BH entropy (solar mass)

# Earth surface gravity (for intuition)
R_earth = 6.371e6  # m
M_earth = 5.972e24  # kg
g_earth_known = G_known * M_earth / R_earth**2

# Orbital period of Earth around Sun
a_orbit_earth = 1.496e11  # m (1 AU)


print("=" * 80)
print("KNOWN VALUES (measured)")
print("=" * 80)
print(f"  G                = {G_known:.5e} m^3/(kg·s^2)")
print(f"  r_s(Sun)         = {r_s_sun_known:.4f} m")
print(f"  T_H(solar BH)   = {T_H_sun_known:.4e} K")
print(f"  rho_crit         = {rho_crit_known:.4e} kg/m^3")
print(f"  l_P              = {l_P_known:.6e} m")
print(f"  m_P              = {m_P_known:.6e} kg")
print(f"  alpha_G(proton)  = {alpha_G_known:.4e}")
print(f"  g_earth          = {g_earth_known:.4f} m/s^2")
print(f"  S_BH(solar)      = {S_BH_sun:.4e} (dimensionless)")
print()


def ratio_str(predicted, known):
    """Return a string showing the ratio and whether it's a match or contradiction."""
    if known == 0:
        return "KNOWN=0"
    ratio = predicted / known
    if 0.99 < ratio < 1.01:
        return f"ratio = {ratio:.6f}  [MATCH]"
    elif 0.9 < ratio < 1.1:
        return f"ratio = {ratio:.4f}  ~ CLOSE (within 10%)"
    elif 0.1 < ratio < 10:
        return f"ratio = {ratio:.4e}  [X] OFF by factor {abs(ratio):.2f}"
    else:
        log_ratio = np.log10(abs(ratio))
        return f"ratio = {ratio:.4e}  [XX] OFF by 10^{log_ratio:.1f}"


# ===========================================================================
# RUN EACH CANDIDATE
# ===========================================================================
results = {}

for name, info in candidates.items():
    a = info["a"]
    print()
    print("=" * 80)
    print(f"CANDIDATE {name}")
    print("=" * 80)
    print(f"  a = {info['formula']} = {a:.6e} m")
    print(f"  Circular: {info['circular']}")
    print(f"  Note: {info['note']}")
    print()

    # -----------------------------------------------------------------------
    # STEP 1: Derive G
    # -----------------------------------------------------------------------
    kappa = K_assumed / a**2
    G_pred = c**2 / (4 * np.pi * kappa)

    print(f"  STEP 1: Derive G")
    print(f"    kappa = K/a^2 = {kappa:.6e} Pa")
    print(f"    G_pred = c^2/(4*pi*kappa) = {G_pred:.6e} m^3/(kg·s^2)")
    print(f"    {ratio_str(G_pred, G_known)}")
    print()

    # -----------------------------------------------------------------------
    # STEP 2: Condensate density
    # -----------------------------------------------------------------------
    rho_cond = kappa / c**2  # = 1/(4*pi*G_pred)
    rho_cond_check = 1 / (4 * np.pi * G_pred)
    rho_cond_known = 1 / (4 * np.pi * G_known)

    print(f"  STEP 2: Condensate density")
    print(f"    rho = kappa/c^2 = {rho_cond:.6e} kg/m^3")
    print(f"    check: 1/(4*pi*G) = {rho_cond_check:.6e} (should match: {np.isclose(rho_cond, rho_cond_check)})")
    print(f"    Known rho = {rho_cond_known:.6e} kg/m^3")
    print(f"    {ratio_str(rho_cond, rho_cond_known)}")
    print()

    # -----------------------------------------------------------------------
    # STEP 3: Planck units
    # -----------------------------------------------------------------------
    l_P_pred = np.sqrt(hbar * G_pred / c**3)
    m_P_pred = np.sqrt(hbar * c / G_pred)
    t_P_pred = np.sqrt(hbar * G_pred / c**5)
    E_P_pred = m_P_pred * c**2
    T_P_pred = E_P_pred / k_B

    print(f"  STEP 3: Planck units")
    print(f"    l_P  = {l_P_pred:.6e} m       {ratio_str(l_P_pred, l_P_known)}")
    print(f"    m_P  = {m_P_pred:.6e} kg      {ratio_str(m_P_pred, m_P_known)}")
    print(f"    t_P  = {t_P_pred:.6e} s       {ratio_str(t_P_pred, t_P_known)}")
    print(f"    E_P  = {E_P_pred:.6e} J       {ratio_str(E_P_pred, E_P_known)}")
    print(f"    T_P  = {T_P_pred:.6e} K       {ratio_str(T_P_pred, T_P_known)}")
    print()

    # -----------------------------------------------------------------------
    # STEP 4: Schwarzschild radius (Sun)
    # -----------------------------------------------------------------------
    r_s_pred = 2 * G_pred * M_sun / c**2

    print(f"  STEP 4: Schwarzschild radius of Sun")
    print(f"    r_s  = 2*G*M_sun/c^2 = {r_s_pred:.6e} m")
    print(f"    Known: {r_s_sun_known:.4f} m")
    print(f"    {ratio_str(r_s_pred, r_s_sun_known)}")
    print()

    # -----------------------------------------------------------------------
    # STEP 5: Hawking temperature (solar-mass BH)
    # -----------------------------------------------------------------------
    T_H_pred = hbar * c**3 / (8 * np.pi * G_pred * M_sun * k_B)

    # Also the PDTP form: T_H = hbar*kappa*c / (2*M*k_B)
    T_H_pdtp = hbar * kappa * c / (2 * M_sun * k_B)

    print(f"  STEP 5: Hawking temperature (solar-mass BH)")
    print(f"    T_H (standard) = {T_H_pred:.6e} K")
    print(f"    T_H (from kappa) = {T_H_pdtp:.6e} K")
    print(f"    Internal consistency: {np.isclose(T_H_pred, T_H_pdtp)}")
    print(f"    Known: {T_H_sun_known:.4e} K")
    print(f"    {ratio_str(T_H_pred, T_H_sun_known)}")
    print()

    # -----------------------------------------------------------------------
    # STEP 6: Gravitational coupling constant
    # -----------------------------------------------------------------------
    alpha_G_pred = G_pred * m_p**2 / (hbar * c)

    print(f"  STEP 6: Gravitational coupling (proton)")
    print(f"    alpha_G = G*m_p^2/(hbar*c) = {alpha_G_pred:.6e}")
    print(f"    Known: {alpha_G_known:.4e}")
    print(f"    {ratio_str(alpha_G_pred, alpha_G_known)}")
    print()

    # -----------------------------------------------------------------------
    # STEP 7: Critical density (Friedmann)
    # -----------------------------------------------------------------------
    rho_crit_pred = 3 * H_0_si**2 / (8 * np.pi * G_pred)

    print(f"  STEP 7: Critical density of universe")
    print(f"    rho_crit = 3*H^2/(8*pi*G) = {rho_crit_pred:.6e} kg/m^3")
    print(f"    Known: {rho_crit_known:.4e} kg/m^3")
    print(f"    {ratio_str(rho_crit_pred, rho_crit_known)}")
    print()

    # -----------------------------------------------------------------------
    # STEP 8: Earth surface gravity
    # -----------------------------------------------------------------------
    g_earth_pred = G_pred * M_earth / R_earth**2

    print(f"  STEP 8: Earth surface gravity")
    print(f"    g = G*M_earth/R_earth^2 = {g_earth_pred:.6e} m/s^2")
    print(f"    Known: {g_earth_known:.4f} m/s^2")
    print(f"    {ratio_str(g_earth_pred, g_earth_known)}")
    print()

    # -----------------------------------------------------------------------
    # STEP 9: Orbital period of Earth
    # -----------------------------------------------------------------------
    T_orbit_pred = 2 * np.pi * np.sqrt(a_orbit_earth**3 / (G_pred * M_sun))
    T_orbit_known = 365.25 * 24 * 3600  # seconds

    print(f"  STEP 9: Earth orbital period")
    print(f"    T = 2*pi*sqrt(a^3/(G*M_sun)) = {T_orbit_pred:.6e} s")
    print(f"    = {T_orbit_pred / (24*3600):.2f} days")
    print(f"    Known: {T_orbit_known:.6e} s (365.25 days)")
    print(f"    {ratio_str(T_orbit_pred, T_orbit_known)}")
    print()

    # -----------------------------------------------------------------------
    # STEP 10: Black hole entropy (solar mass)
    # -----------------------------------------------------------------------
    S_BH_pred = 4 * np.pi * G_pred * M_sun**2 / (hbar * c)

    print(f"  STEP 10: Black hole entropy (solar mass)")
    print(f"    S_BH = 4*pi*G*M^2/(hbar*c) = {S_BH_pred:.6e}")
    print(f"    Known: {S_BH_sun:.4e}")
    print(f"    {ratio_str(S_BH_pred, S_BH_sun)}")
    print()

    # -----------------------------------------------------------------------
    # STEP 11: Hierarchy ratio
    # -----------------------------------------------------------------------
    R_hierarchy = alpha_G_pred / alpha_EM

    print(f"  STEP 11: Hierarchy ratio")
    print(f"    R = alpha_G/alpha_EM = {R_hierarchy:.6e}")
    print(f"    Known: {alpha_G_known/alpha_EM:.4e}")
    print(f"    {ratio_str(R_hierarchy, alpha_G_known/alpha_EM)}")
    print()

    # -----------------------------------------------------------------------
    # STEP 12: Relationship between a and l_P
    # -----------------------------------------------------------------------
    ratio_a_lP = a / l_P_known
    print(f"  STEP 12: Lattice spacing vs Planck length")
    print(f"    a / l_P = {ratio_a_lP:.6e}")
    print(f"    a / l_P_pred = {a / l_P_pred:.6e}")
    print()

    # -----------------------------------------------------------------------
    # STEP 13: What correction factor would fix G?
    # -----------------------------------------------------------------------
    correction = G_known / G_pred
    correction_sqrt = np.sqrt(correction)

    print(f"  STEP 13: Correction factor needed")
    print(f"    G_known / G_pred = {correction:.6e}")
    print(f"    sqrt(correction) = {correction_sqrt:.6e}")
    print(f"    Meaning: a_correct = a * {correction_sqrt:.6e} to get exact G")
    print(f"    a_correct = {a * correction_sqrt:.6e} m")
    print(f"    l_P = {l_P_known:.6e} m (for comparison)")
    print()

    # -----------------------------------------------------------------------
    # STEP 14: Can the correction be expressed as known constants?
    # -----------------------------------------------------------------------
    print(f"  STEP 14: Is the correction a known ratio?")

    # Check if correction = (m_e/m_p)^n for some n
    mass_ratio = m_e / m_p
    if correction > 0:
        n_mass = np.log(correction) / np.log(mass_ratio)
        print(f"    correction = (m_e/m_p)^n  =>  n = {n_mass:.4f}")

    # Check if correction = alpha_EM^n for some n
    n_alpha = np.log(correction) / np.log(alpha_EM)
    print(f"    correction = alpha_EM^n   =>  n = {n_alpha:.4f}")

    # Check if correction = (m/m_P)^n for some n
    n_planck_e = np.log(correction) / np.log(m_e / m_P_known)
    n_planck_p = np.log(correction) / np.log(m_p / m_P_known)
    print(f"    correction = (m_e/m_P)^n  =>  n = {n_planck_e:.4f}")
    print(f"    correction = (m_p/m_P)^n  =>  n = {n_planck_p:.4f}")

    # Check if sqrt(correction) is close to simple fractions of known constants
    print(f"    sqrt(correction) / alpha_EM = {correction_sqrt / alpha_EM:.6e}")
    print(f"    sqrt(correction) * alpha_EM = {correction_sqrt * alpha_EM:.6e}")
    print(f"    correction * alpha_EM = {correction * alpha_EM:.6e}")
    print(f"    correction / alpha_EM = {correction / alpha_EM:.6e}")
    print(f"    correction / alpha_EM^2 = {correction / alpha_EM**2:.6e}")

    # For electron: check if correction = m_e^2 * c / (hbar * something)
    print(f"    correction = {correction:.6e}")
    print(f"    (m_e*c/hbar)^2 * l_P^2 = {(m_e*c/hbar * l_P_known)**2:.6e}")
    print()

    # -----------------------------------------------------------------------
    # STEP 15: Decoupling energy (PDTP application)
    # -----------------------------------------------------------------------
    g_surface = G_pred * M_earth / R_earth**2
    E_decouple_per_kg = g_surface  # J/kg
    E_decouple_ton = g_surface * 1000  # J for 1 ton

    print(f"  STEP 15: Decoupling energy (1 ton, Earth surface)")
    print(f"    g_surface = {g_surface:.6e} m/s^2")
    print(f"    E/kg = {E_decouple_per_kg:.6e} J/kg")
    print(f"    E(1 ton) = {E_decouple_ton:.6e} J")
    print(f"    Power(1s) = {E_decouple_ton:.2f} W = {E_decouple_ton/1000:.2f} kW")
    print()

    # -----------------------------------------------------------------------
    # CONTRADICTION COUNT
    # -----------------------------------------------------------------------
    tests = [
        ("G", G_pred, G_known),
        ("r_s(Sun)", r_s_pred, r_s_sun_known),
        ("T_H(Sun)", T_H_pred, T_H_sun_known),
        ("alpha_G", alpha_G_pred, alpha_G_known),
        ("rho_crit", rho_crit_pred, rho_crit_known),
        ("g_earth", g_earth_pred, g_earth_known),
        ("T_orbit", T_orbit_pred, T_orbit_known),
        ("S_BH", S_BH_pred, S_BH_sun),
        ("l_P", l_P_pred, l_P_known),
        ("m_P", m_P_pred, m_P_known),
    ]

    matches = 0
    contradictions = 0
    for tname, pred, known in tests:
        r = pred / known
        if 0.99 < r < 1.01:
            matches += 1
        else:
            contradictions += 1

    print(f"  -----------------------------------------------")
    print(f"  SUDOKU SCORECARD: {matches} matches, {contradictions} contradictions out of {len(tests)} tests")
    print(f"  -----------------------------------------------")
    print()

    results[name] = {
        "G_pred": G_pred,
        "matches": matches,
        "contradictions": contradictions,
        "correction": correction,
        "a": a,
    }


# ===========================================================================
# FINAL COMPARISON
# ===========================================================================
print()
print("=" * 80)
print("FINAL COMPARISON: ALL CANDIDATES")
print("=" * 80)
print()
print(f"{'Candidate':<40} {'G_pred':>12} {'Ratio':>12} {'Matches':>8} {'Contradictions':>15}")
print("-" * 90)
for name, r in results.items():
    ratio = r["G_pred"] / G_known
    print(f"{name:<40} {r['G_pred']:>12.4e} {ratio:>12.4e} {r['matches']:>8} {r['contradictions']:>15}")

print()
print("=" * 80)
print("KEY INSIGHT: WHAT CORRECTION FACTOR FIXES EACH CANDIDATE?")
print("=" * 80)
print()
for name, r in results.items():
    if r["correction"] != 1.0:
        print(f"{name}:")
        print(f"  Need to multiply G_pred by {r['correction']:.6e} to get G_known")
        print(f"  Or multiply 'a' by {np.sqrt(r['correction']):.6e}")
        # Express the needed 'a' in terms of known quantities
        a_needed = r["a"] * np.sqrt(r["correction"])
        print(f"  a_needed = {a_needed:.6e} m  (= l_P = {l_P_known:.6e} m)")
        print(f"  a_needed / l_P = {a_needed / l_P_known:.6f}")
        print()

print()
print("=" * 80)
print("BONUS: WHAT IF WE COMBINE ELECTRON AND PROTON?")
print("=" * 80)
print()

# Geometric mean of electron and proton Compton wavelengths
a_geom = np.sqrt((hbar/(m_e*c)) * (hbar/(m_p*c)))
kappa_geom = K_assumed / a_geom**2
G_geom = c**2 / (4 * np.pi * kappa_geom)
print(f"Geometric mean: a = sqrt(lambda_e * lambda_p) = {a_geom:.6e} m")
print(f"  G_pred = {G_geom:.6e}   {ratio_str(G_geom, G_known)}")
print()

# Harmonic mean
a_harm = 2 / (m_e*c/hbar + m_p*c/hbar) * 1  # 2/(1/a_e + 1/a_p) ... actually
a_e = hbar/(m_e*c)
a_p = hbar/(m_p*c)
a_harm = 2 * a_e * a_p / (a_e + a_p)
kappa_harm = K_assumed / a_harm**2
G_harm = c**2 / (4 * np.pi * kappa_harm)
print(f"Harmonic mean: a = 2*a_e*a_p/(a_e+a_p) = {a_harm:.6e} m")
print(f"  G_pred = {G_harm:.6e}   {ratio_str(G_harm, G_known)}")
print()

# What about a = alpha_EM * a_e (electron Compton * fine structure)?
a_alpha_e = alpha_EM * a_e
kappa_alpha_e = K_assumed / a_alpha_e**2
G_alpha_e = c**2 / (4 * np.pi * kappa_alpha_e)
print(f"a = alpha_EM * lambda_e = {a_alpha_e:.6e} m  (= Bohr radius!)")
print(f"  G_pred = {G_alpha_e:.6e}   {ratio_str(G_alpha_e, G_known)}")
print()

# What about a = alpha_EM * a_p?
a_alpha_p = alpha_EM * a_p
kappa_alpha_p = K_assumed / a_alpha_p**2
G_alpha_p = c**2 / (4 * np.pi * kappa_alpha_p)
print(f"a = alpha_EM * lambda_p = {a_alpha_p:.6e} m")
print(f"  G_pred = {G_alpha_p:.6e}   {ratio_str(G_alpha_p, G_known)}")
print()

# a = alpha_EM^2 * a_e ?
a_alpha2_e = alpha_EM**2 * a_e
kappa_alpha2_e = K_assumed / a_alpha2_e**2
G_alpha2_e = c**2 / (4 * np.pi * kappa_alpha2_e)
print(f"a = alpha_EM^2 * lambda_e = {a_alpha2_e:.6e} m")
print(f"  G_pred = {G_alpha2_e:.6e}   {ratio_str(G_alpha2_e, G_known)}")
print()

# What value of alpha_EM^n * a_e gives correct G?
# G = c^2/(4*pi*K/(alpha^n * a_e)^2) = c^2 * alpha^(2n) * a_e^2 / (4*pi*K)
# So alpha^(2n) = G * 4*pi*K / (c^2 * a_e^2)
target = G_known * 4 * np.pi * K_assumed / (c**2 * a_e**2)
n_needed_e = np.log(target) / (2 * np.log(alpha_EM))
print(f"For a = alpha_EM^n * lambda_e to give correct G:")
print(f"  n = {n_needed_e:.6f}")
print(f"  (Not a clean integer or simple fraction)")
print()

# Same for proton
target_p = G_known * 4 * np.pi * K_assumed / (c**2 * a_p**2)
n_needed_p = np.log(target_p) / (2 * np.log(alpha_EM))
print(f"For a = alpha_EM^n * lambda_p to give correct G:")
print(f"  n = {n_needed_p:.6f}")
print()

# What about a = (m_e/m_p)^n * a_e ?
target_mass = G_known * 4 * np.pi * K_assumed / (c**2 * a_e**2)
# a = (m_e/m_p)^n * a_e => a^2 = (m_e/m_p)^(2n) * a_e^2
# kappa = K/a^2 = K/((m_e/m_p)^(2n) * a_e^2)
# G = c^2 * (m_e/m_p)^(2n) * a_e^2 / (4*pi*K)
# So (m_e/m_p)^(2n) = target
n_mass_needed = np.log(target) / (2 * np.log(m_e/m_p))
print(f"For a = (m_e/m_p)^n * lambda_e to give correct G:")
print(f"  n = {n_mass_needed:.6f}")
print()

print("=" * 80)
print("REVERSE ENGINEERING: What 'a' gives exact G?")
print("=" * 80)
a_exact = np.sqrt(K_assumed * 4 * np.pi * G_known / c**2)
# Simplify: a = sqrt(K * 4*pi*G/c^2) = sqrt(hbar/(4*pi*c) * 4*pi*G/c^2)
#          = sqrt(hbar*G/c^3) = l_P
print(f"  a_exact = sqrt(4*pi*G*K/c^2) = {a_exact:.6e} m")
print(f"  l_P     = {l_P_known:.6e} m")
print(f"  a_exact / l_P = {a_exact/l_P_known:.10f}")
print()
print(f"  CONCLUSION: a_exact = l_P exactly.")
print(f"  This is mathematically guaranteed: K = hbar/(4*pi*c) combined with")
print(f"  G = c^2/(4*pi*kappa) and kappa=K/a^2 gives a = sqrt(hbar*G/c^3) = l_P.")
print(f"  The circularity is algebraic identity, not coincidence.")
print()
print(f"  BUT: the Sudoku test still reveals useful information:")
print(f"  - The RATIO of each candidate 'a' to l_P tells us the 'correction factor'")
print(f"  - For electron: a_e/l_P = {a_e/l_P_known:.6e} = m_P/m_e = {m_P_known/m_e:.6e}")
print(f"  - For proton:   a_p/l_P = {a_p/l_P_known:.6e} = m_P/m_p = {m_P_known/m_p:.6e}")
print(f"  - These are just the HIERARCHY RATIOS in disguise!")
print()
print(f"  The hierarchy ratio m_P/m_e = {m_P_known/m_e:.6e}")
print(f"  The hierarchy ratio m_P/m_p = {m_P_known/m_p:.6e}")
print(f"  G_electron / G_known = (a_e/l_P)^2 = (m_P/m_e)^2 = {(m_P_known/m_e)**2:.6e}")
print(f"  G_proton / G_known   = (a_p/l_P)^2 = (m_P/m_p)^2 = {(m_P_known/m_p)**2:.6e}")
print()
print(f"  INSIGHT: The Sudoku 'error' IS the hierarchy problem itself!")
print(f"  Deriving G from particle masses requires solving the hierarchy problem.")
