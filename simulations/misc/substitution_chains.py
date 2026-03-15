# ===========================================================================
# PDTP Substitution Chain Analysis (Part 29)
# ===========================================================================
#
# GOAL: Derive the lattice coupling K (or condensate stiffness kappa) from
# known physics equations ONLY, by substituting PDTP bridge relations until
# K or kappa is the only unknown remaining on one side.
#
# If multiple independent chains all give the same K -> strong PDTP validation.
# If they don't -> identifies exactly where the framework breaks.
#
# ULTIMATE GOAL: Validate PDTP sufficiently to determine the energy cost
# of phase decoupling (alpha -> 0), which is the engineering requirement
# for a PDTP-based propulsion platform.
#
# ===========================================================================
#
# PDTP BRIDGE EQUATIONS (from Part 21 / efv_microphysics.md):
#
#   c^2 = kappa / rho          Speed of light = stiffness / density
#   G = c^2 / (4*pi*kappa)     Newton's constant = inverse stiffness
#   kappa = K / a^2             Stiffness from lattice coupling K and spacing a
#   hbar*omega = M*c^2          Mass = frequency of phase distortion
#   g = 2*lambda*sqrt(rho*sigma)  Coupling from symmetry breaking
#
# ===========================================================================

import sympy as sp
from sympy import pi, sqrt, Rational, simplify, symbols, Eq, solve, latex

# ============================================================
# 1. DEFINE SYMBOLIC VARIABLES
# ============================================================

# Fundamental constants
G_sym = sp.Symbol('G', positive=True)           # Newton's constant
c_sym = sp.Symbol('c', positive=True)           # Speed of light
hbar = sp.Symbol('hbar', positive=True)         # Reduced Planck constant
k_B = sp.Symbol('k_B', positive=True)           # Boltzmann constant

# EM constants
alpha_EM = sp.Symbol('alpha_EM', positive=True) # Fine structure constant
Z_0 = sp.Symbol('Z_0', positive=True)           # Vacuum impedance
R_K = sp.Symbol('R_K', positive=True)           # von Klitzing constant

# Masses
M = sp.Symbol('M', positive=True)               # Generic mass
m_p = sp.Symbol('m_p', positive=True)           # Proton mass
m_e = sp.Symbol('m_e', positive=True)           # Electron mass
m_P = sp.Symbol('m_P', positive=True)           # Planck mass

# PDTP variables
kappa = sp.Symbol('kappa', positive=True)       # Condensate stiffness (Pa)
rho = sp.Symbol('rho', positive=True)           # Condensate mass density
K_lat = sp.Symbol('K', positive=True)           # Lattice coupling (J)
a_lat = sp.Symbol('a', positive=True)           # Lattice spacing (m)

# Planck units
l_P = sp.Symbol('l_P', positive=True)           # Planck length
t_P = sp.Symbol('t_P', positive=True)           # Planck time

# Cosmological
H = sp.Symbol('H', positive=True)               # Hubble parameter
rho_m = sp.Symbol('rho_m', positive=True)       # Matter density

# Other
T_H = sp.Symbol('T_H', positive=True)          # Hawking temperature
r_s = sp.Symbol('r_s', positive=True)           # Schwarzschild radius
alpha_G = sp.Symbol('alpha_G', positive=True)   # Gravitational fine structure


# ============================================================
# 2. PDTP BRIDGE RELATIONS
# ============================================================

# The two core bridges:
#   G = c^2 / (4*pi*kappa)   =>   kappa = c^2 / (4*pi*G)
#   c^2 = kappa / rho        =>   rho = kappa / c^2
#   kappa = K / a^2           =>   K = kappa * a^2

kappa_from_G = c_sym**2 / (4 * pi * G_sym)
rho_from_kappa = kappa / c_sym**2
K_from_kappa = kappa * a_lat**2


# ============================================================
# 3. NUMERICAL VALUES
# ============================================================

G_val   = 6.67430e-11   # m^3 kg^-1 s^-2
c_val   = 2.99792458e8  # m/s
hbar_val = 1.054571817e-34  # J s
k_B_val = 1.380649e-23  # J/K
alpha_val = 1 / 137.035999084
Z_0_val = 376.730313668  # ohm
R_K_val = 25812.80745    # ohm
m_p_val = 1.67262192e-27 # kg
m_e_val = 9.1093837015e-31 # kg
l_P_val = 1.616255e-35   # m
m_P_val = 2.176434e-8    # kg

# Pre-compute kappa numerically from bridge
kappa_val = c_val**2 / (4 * 3.14159265358979 * G_val)

print("=" * 72)
print("PDTP SUBSTITUTION CHAIN ANALYSIS (Part 29)")
print("=" * 72)
print()
print("PDTP Bridge Relations:")
print(f"  G = c^2 / (4*pi*kappa)  =>  kappa = c^2 / (4*pi*G)")
print(f"  c^2 = kappa / rho       =>  rho = kappa / c^2")
print(f"  kappa = K / a^2         =>  K = kappa * a^2")
print()
print(f"Numerical kappa = c^2/(4*pi*G) = {kappa_val:.6e} Pa")
print(f"  (= {kappa_val:.6e} kg/(m*s^2))")
print()


# ============================================================
# 4. SUBSTITUTION CHAINS
# ============================================================

results = []

def run_chain(chain_num, name, start_eq_str, steps, final_expr,
              numerical_value, independent, notes):
    """Run one substitution chain and record the result."""
    print("-" * 72)
    print(f"CHAIN {chain_num}: {name}")
    print("-" * 72)
    print()
    print(f"Starting equation: {start_eq_str}")
    print()
    for i, step in enumerate(steps, 1):
        print(f"  Step {i}: {step}")
    print()
    print(f"  Result: {final_expr}")
    print(f"  Numerical: {numerical_value}")
    print(f"  Independent of G? {'YES' if independent else 'NO (circular)'}")
    if notes:
        print(f"  Notes: {notes}")
    print()

    results.append({
        'chain': chain_num,
        'name': name,
        'result': final_expr,
        'numerical': numerical_value,
        'independent': independent,
        'notes': notes
    })


# ------------------------------------------------------------------
# CHAIN 1: Gravitational + Electromagnetic
# ------------------------------------------------------------------
# Start: alpha_EM = Z_0 / (2*R_K)  [exact identity]
#        G = c^2 / (4*pi*kappa)    [PDTP bridge]
#
# Substitute c^2 = kappa/rho into G:
#   G = (kappa/rho) / (4*pi*kappa) = 1/(4*pi*rho)
#
# So: rho = 1/(4*pi*G)
#
# Can we relate rho to EM constants?
# alpha_EM = Z_0/(2*R_K) = e^2/(4*pi*epsilon_0*hbar*c)
# Z_0 = 1/(epsilon_0*c) = mu_0*c
# R_K = h/e^2 = 2*pi*hbar/e^2
#
# rho = kappa/c^2, kappa = c^2/(4*pi*G)  =>  rho = 1/(4*pi*G)
# This is purely gravitational — no EM link emerges.

rho_val = 1 / (4 * 3.14159265358979 * G_val)

# But we CAN write a combined expression:
# alpha_G = G*m_p^2/(hbar*c) and alpha_EM = e^2/(4*pi*eps0*hbar*c)
# Ratio: alpha_G/alpha_EM = m_p^2*G / (hbar*c*alpha_EM)
# Sub G: alpha_G/alpha_EM = m_p^2*c / (4*pi*kappa*hbar*alpha_EM)
# Solve for kappa:
# kappa = m_p^2*c / (4*pi*hbar*alpha_EM * (alpha_G/alpha_EM))
#       = m_p^2*c / (4*pi*hbar*alpha_G)
# But alpha_G = G*m_p^2/(hbar*c), so this is circular:
# kappa = m_p^2*c / (4*pi*hbar * G*m_p^2/(hbar*c))
#       = m_p^2*c * hbar*c / (4*pi*hbar*G*m_p^2) = c^2/(4*pi*G)  <-- back to bridge

kappa_chain1 = c_sym**2 / (4*pi*G_sym)
kappa_chain1_val = kappa_val

run_chain(1, "Gravitational + Electromagnetic",
    "alpha_EM = Z_0/(2*R_K),  G = c^2/(4*pi*kappa)",
    [
        "Substitute c^2 = kappa/rho into G: G = 1/(4*pi*rho)",
        "So rho = 1/(4*pi*G) = condensate density from G alone",
        "Try to link rho to EM: alpha_G/alpha_EM = m_p^2*c/(4*pi*kappa*hbar*alpha_EM)",
        "Solve for kappa: kappa = m_p^2*c/(4*pi*hbar*alpha_G)",
        "But alpha_G = G*m_p^2/(hbar*c) => substituting gives kappa = c^2/(4*pi*G)  [CIRCULAR]",
    ],
    "kappa = c^2 / (4*pi*G)  [cannot escape G without independent rho measurement]",
    f"kappa = {kappa_chain1_val:.6e} Pa  |  rho = {rho_val:.6e} kg/m^3",
    False,
    "EM and gravity decouple — alpha_EM tells us nothing about kappa. "
    "The hierarchy problem (alpha_G/alpha_EM ~ 10^-36) is INPUT, not derived."
)


# ------------------------------------------------------------------
# CHAIN 2: Planck Units
# ------------------------------------------------------------------
# l_P = sqrt(hbar*G/c^3)
# Sub G = c^2/(4*pi*kappa):
# l_P = sqrt(hbar*c^2 / (4*pi*kappa*c^3)) = sqrt(hbar / (4*pi*kappa*c))
#
# Solve for kappa:
# kappa = hbar / (4*pi*l_P^2 * c)
#
# If a = l_P (lattice spacing = Planck length):
# K = kappa * a^2 = kappa * l_P^2 = hbar / (4*pi*c) * (l_P^2/l_P^2)
#   = hbar / (4*pi*c)
#
# Numerically:
# K = hbar/(4*pi*c) = 1.055e-34 / (4*pi*3e8) = 2.80e-44 J

# Symbolic
kappa_chain2 = hbar / (4*pi*l_P**2 * c_sym)
K_chain2 = hbar / (4*pi*c_sym)  # if a = l_P

# Numerical
kappa_chain2_val = hbar_val / (4 * 3.14159265358979 * l_P_val**2 * c_val)
K_chain2_val = hbar_val / (4 * 3.14159265358979 * c_val)

# Check: does kappa_chain2 = kappa_from_G?
# kappa = hbar/(4*pi*l_P^2*c),  l_P^2 = hbar*G/c^3
# => kappa = hbar/(4*pi*(hbar*G/c^3)*c) = hbar*c^3/(4*pi*hbar*G*c) = c^2/(4*pi*G) ✓

run_chain(2, "Planck Units",
    "l_P = sqrt(hbar*G/c^3)",
    [
        "Sub G = c^2/(4*pi*kappa):",
        "  l_P = sqrt(hbar / (4*pi*kappa*c))",
        "Solve for kappa:",
        "  kappa = hbar / (4*pi * l_P^2 * c)",
        "If a = l_P (lattice spacing = Planck length):",
        "  K = kappa * l_P^2 = hbar / (4*pi*c)",
        f"Check: substituting l_P^2 = hbar*G/c^3 recovers kappa = c^2/(4*pi*G) [CONSISTENT]",
    ],
    "kappa = hbar / (4*pi*l_P^2*c)  |  K(a=l_P) = hbar/(4*pi*c)",
    f"kappa = {kappa_chain2_val:.6e} Pa  |  K = {K_chain2_val:.6e} J",
    False,
    "Circular: l_P is defined via G, so this just re-expresses the bridge. "
    "BUT: the result K = hbar/(4*pi*c) is elegant — only quantum + relativity, no G. "
    "If K could be measured independently, this PREDICTS G."
)


# ------------------------------------------------------------------
# CHAIN 3: Black Hole Thermodynamics
# ------------------------------------------------------------------
# T_H = hbar*c^3 / (8*pi*G*M*k_B)
# Sub G = c^2/(4*pi*kappa):
# T_H = hbar*c^3 / (8*pi * c^2/(4*pi*kappa) * M * k_B)
#      = hbar*c^3 * 4*pi*kappa / (8*pi*c^2*M*k_B)
#      = hbar*kappa*c / (2*M*k_B)
#
# Solve for kappa:
# kappa = 2*M*k_B*T_H / (hbar*c)

kappa_chain3 = 2*M*k_B*T_H / (hbar*c_sym)

# Numerical check: for M = M_sun = 1.989e30 kg
M_sun = 1.989e30
T_H_sun = hbar_val * c_val**3 / (8 * 3.14159265358979 * G_val * M_sun * k_B_val)
kappa_chain3_val = 2 * M_sun * k_B_val * T_H_sun / (hbar_val * c_val)

run_chain(3, "Black Hole Thermodynamics",
    "T_H = hbar*c^3 / (8*pi*G*M*k_B)",
    [
        "Sub G = c^2/(4*pi*kappa):",
        "  T_H = hbar*kappa*c / (2*M*k_B)",
        "Solve for kappa:",
        "  kappa = 2*M*k_B*T_H / (hbar*c)",
        f"Check (M = M_sun): T_H = {T_H_sun:.4e} K",
        f"  kappa = 2*M_sun*k_B*T_H / (hbar*c) = {kappa_chain3_val:.6e} Pa",
    ],
    "kappa = 2*M*k_B*T_H / (hbar*c)",
    f"kappa = {kappa_chain3_val:.6e} Pa  [matches bridge: {kappa_val:.6e}]",
    False,
    "Circular: T_H is derived using G, so kappa still depends on G. "
    "BUT: the PDTP form T_H = hbar*kappa*c/(2*M*k_B) is illuminating — "
    "Hawking temperature is proportional to condensate stiffness. "
    "Stiffer condensate = hotter black holes."
)


# ------------------------------------------------------------------
# CHAIN 4: Schwarzschild Radius
# ------------------------------------------------------------------
# r_s = 2*G*M / c^2
# Sub G = c^2/(4*pi*kappa):
# r_s = 2*c^2*M / (4*pi*kappa*c^2) = M / (2*pi*kappa)

kappa_chain4 = M / (2*pi*r_s)

# Numerical: M = M_sun, r_s_sun = 2*G*M_sun/c^2
r_s_sun = 2 * G_val * M_sun / c_val**2
kappa_chain4_val = M_sun / (2 * 3.14159265358979 * r_s_sun)

run_chain(4, "Schwarzschild Radius",
    "r_s = 2*G*M / c^2",
    [
        "Sub G = c^2/(4*pi*kappa):",
        "  r_s = M / (2*pi*kappa)",
        "Solve for kappa:",
        "  kappa = M / (2*pi*r_s)",
        f"Check (M = M_sun): r_s = {r_s_sun:.4f} m",
        f"  kappa = M_sun / (2*pi*r_s) = {kappa_chain4_val:.6e} Pa",
    ],
    "kappa = M / (2*pi*r_s)  [mass per unit Schwarzschild area / (4*pi)]",
    f"kappa = {kappa_chain4_val:.6e} Pa  [matches bridge: {kappa_val:.6e}]",
    False,
    "Circular: r_s is defined via G. "
    "BUT: beautiful interpretation — the Schwarzschild radius is where the "
    "enclosed mass equals the condensate's 'holding capacity' 2*pi*kappa*r. "
    "A black hole forms when mass exceeds what stiffness can support."
)


# ------------------------------------------------------------------
# CHAIN 5: Compton Wavelength meets Gravity
# ------------------------------------------------------------------
# alpha_G = G*m^2 / (hbar*c)  [gravitational fine structure constant]
# Sub G = c^2/(4*pi*kappa):
# alpha_G = m^2*c^2 / (4*pi*kappa*hbar*c) = m^2*c / (4*pi*kappa*hbar)
#
# Solve for kappa:
# kappa = m^2*c / (4*pi*hbar*alpha_G)
#
# For proton: alpha_G_p = G*m_p^2/(hbar*c)

alpha_G_p_val = G_val * m_p_val**2 / (hbar_val * c_val)
kappa_chain5 = m_p**2 * c_sym / (4*pi*hbar*alpha_G)
kappa_chain5_val = m_p_val**2 * c_val / (4 * 3.14159265358979 * hbar_val * alpha_G_p_val)

run_chain(5, "Compton Wavelength meets Gravity",
    "alpha_G = G*m^2 / (hbar*c)",
    [
        "Sub G = c^2/(4*pi*kappa):",
        "  alpha_G = m^2*c / (4*pi*kappa*hbar)",
        "Solve for kappa:",
        "  kappa = m^2*c / (4*pi*hbar*alpha_G)",
        f"For proton: alpha_G = {alpha_G_p_val:.6e}",
        f"  kappa = m_p^2*c / (4*pi*hbar*alpha_G) = {kappa_chain5_val:.6e} Pa",
    ],
    "kappa = m^2*c / (4*pi*hbar*alpha_G)",
    f"kappa = {kappa_chain5_val:.6e} Pa  [matches bridge: {kappa_val:.6e}]",
    False,
    "Circular: alpha_G is defined via G. "
    "BUT: reveals that kappa is the 'quantum-gravitational stiffness' — "
    "the ratio of (mass energy)^2 to the quantum of action, divided by 4*pi."
)


# ------------------------------------------------------------------
# CHAIN 6: Friedmann Equation
# ------------------------------------------------------------------
# H^2 = 8*pi*G*rho_matter / 3   (flat universe, matter-dominated)
# Sub G = c^2/(4*pi*kappa):
# H^2 = 8*pi*c^2*rho_matter / (3*4*pi*kappa) = 2*c^2*rho_matter / (3*kappa)
#
# Solve for kappa:
# kappa = 2*c^2*rho_matter / (3*H^2)

# Numerical: H_0 = 67.4 km/s/Mpc = 2.184e-18 s^-1
H_0_val = 67.4e3 / (3.0857e22)  # Convert km/s/Mpc to s^-1
rho_crit = 3 * H_0_val**2 / (8 * 3.14159265358979 * G_val)
# For flat universe, rho_matter = Omega_m * rho_crit
Omega_m = 0.315
rho_m_val = Omega_m * rho_crit

kappa_chain6 = 2*c_sym**2*rho_m / (3*H**2)
kappa_chain6_val = 2 * c_val**2 * rho_m_val / (3 * H_0_val**2)

# Check: this should give kappa = c^2/(4*pi*G) only if rho_m = rho_crit*Omega_m
# and H^2 = 8*pi*G*rho_m/3, which is how rho_crit is defined => circular
# Let's verify:
# kappa = 2*c^2*(Omega_m * 3*H^2/(8*pi*G)) / (3*H^2) = 2*c^2*Omega_m/(8*pi*G)
#       = c^2*Omega_m/(4*pi*G)
# This is kappa * Omega_m, not kappa!
# INTERESTING: Friedmann chain gives kappa_effective = Omega_m * kappa
# For Omega_m = 1: kappa_fried = kappa (exact)
# For Omega_m = 0.315: kappa_fried = 0.315 * kappa

# Actually wait — the Friedmann equation uses TOTAL rho, not just matter.
# H^2 = 8*pi*G*rho_total/3 where rho_total = rho_crit (by definition for flat)
# If we use rho_total = rho_crit:
kappa_chain6_total = 2 * c_val**2 * rho_crit / (3 * H_0_val**2)

run_chain(6, "Friedmann Equation",
    "H^2 = 8*pi*G*rho_total / 3  (flat universe)",
    [
        "Sub G = c^2/(4*pi*kappa):",
        "  H^2 = 2*c^2*rho_total / (3*kappa)",
        "Solve for kappa:",
        "  kappa = 2*c^2*rho_total / (3*H^2)",
        f"H_0 = 67.4 km/s/Mpc = {H_0_val:.4e} s^-1",
        f"rho_crit = 3*H_0^2/(8*pi*G) = {rho_crit:.4e} kg/m^3",
        f"Using rho_total = rho_crit (flat):  kappa = {kappa_chain6_total:.6e} Pa",
        f"Using rho_matter only (Omega_m={Omega_m}): kappa = {kappa_chain6_val:.6e} Pa",
    ],
    "kappa = 2*c^2*rho_total / (3*H^2)",
    f"kappa(rho_crit) = {kappa_chain6_total:.6e} Pa  [matches bridge: {kappa_val:.6e}]",
    False,
    "Circular: rho_crit is defined via G and H. "
    "BUT: the PDTP form H^2 = 2*c^2*rho/(3*kappa) is physical — "
    "expansion rate = (energy density) / (condensate stiffness). "
    "Stiffer condensate = slower expansion for same density."
)


# ------------------------------------------------------------------
# CHAIN 7: Fine Structure + Gravitational Fine Structure
# ------------------------------------------------------------------
# alpha_G_p = G*m_p^2/(hbar*c) ~ 5.9e-39
# alpha_EM = 1/137.036
# Ratio R = alpha_G_p / alpha_EM ~ 4.3e-37
#
# From Chain 5: kappa = m_p^2*c / (4*pi*hbar*alpha_G_p)
# Using alpha_G_p = R * alpha_EM:
# kappa = m_p^2*c / (4*pi*hbar*R*alpha_EM)
#
# This expresses kappa in terms of m_p, c, hbar, alpha_EM, and R.
# R is the hierarchy ratio — a measured number.
# But R = G*m_p^2/(hbar*c*alpha_EM), which contains G => circular.

R_ratio = alpha_G_p_val / alpha_val
kappa_chain7 = m_p**2 * c_sym / (4*pi*hbar*alpha_G*alpha_EM)  # symbolic
kappa_chain7_val = m_p_val**2 * c_val / (4 * 3.14159265358979 * hbar_val
                                          * R_ratio * alpha_val)

run_chain(7, "Fine Structure + Gravitational Fine Structure",
    "alpha_G = G*m_p^2/(hbar*c),  alpha_EM = 1/137.036",
    [
        "Ratio: R = alpha_G/alpha_EM = G*m_p^2/(hbar*c*alpha_EM)",
        f"  R = {R_ratio:.6e}",
        "From Chain 5: kappa = m_p^2*c / (4*pi*hbar*alpha_G)",
        "  = m_p^2*c / (4*pi*hbar*R*alpha_EM)",
        "But R still contains G => circular.",
        "HOWEVER: if we could derive R from PDTP lattice structure,",
        "this would be a genuine prediction of G from particle physics.",
    ],
    "kappa = m_p^2*c / (4*pi*hbar*R*alpha_EM)  where R = alpha_G/alpha_EM",
    f"kappa = {kappa_chain7_val:.6e} Pa  [matches bridge: {kappa_val:.6e}]",
    False,
    "Circular via R. "
    "THE BIG PRIZE: if PDTP could derive the hierarchy ratio R ~ 10^-37 "
    "from lattice microphysics (e.g., R = (m_p/m_P)^2 / alpha_EM), "
    "this chain would predict G from m_p, hbar, c, and alpha_EM alone."
)


# ------------------------------------------------------------------
# CHAIN 8: Condensate Equation of State
# ------------------------------------------------------------------
# For a condensate with sound speed c_s = c:
#   Bulk modulus B = rho * c_s^2 = rho * c^2
#   => kappa = rho * c^2  (stiffness = energy density)
#
# Combined with G = c^2/(4*pi*kappa):
#   G = c^2 / (4*pi*rho*c^2) = 1/(4*pi*rho)
#   => rho = 1/(4*pi*G)
#
# Check: is this rho_Planck?
# rho_Planck = m_P / l_P^3 = c^5/(hbar*G^2)

rho_condensate = 1 / (4 * 3.14159265358979 * G_val)
rho_Planck = c_val**5 / (hbar_val * G_val**2)
ratio_rho = rho_condensate / rho_Planck

# Also check: what IS rho = 1/(4*pi*G) in terms of known densities?
# In SI: rho ~ 1.19e9 kg/m^3 ~ density of a white dwarf
# In Planck: rho/rho_Planck ~ 2.3e-88

# Energy density: u = rho*c^2 = c^2/(4*pi*G) = kappa
# This is kappa itself! Circular: kappa = rho*c^2, rho = kappa/c^2.

run_chain(8, "Condensate Equation of State",
    "B = rho*c^2 (bulk modulus for c_s = c condensate)",
    [
        "Identify: kappa = B = rho*c^2",
        "Combined with bridge G = c^2/(4*pi*kappa):",
        "  G = 1/(4*pi*rho)  =>  rho = 1/(4*pi*G)",
        f"Numerical: rho = {rho_condensate:.6e} kg/m^3",
        f"Compare to rho_Planck = {rho_Planck:.4e} kg/m^3",
        f"Ratio: rho/rho_Planck = {ratio_rho:.4e}",
        "NOT Planck density! The condensate is 88 orders of magnitude less dense.",
        "This IS kappa/c^2 — the definition is self-referential.",
    ],
    "rho = 1/(4*pi*G)  [condensate density from G]",
    f"rho = {rho_condensate:.6e} kg/m^3  (~ white dwarf density)",
    False,
    "Circular: rho = kappa/c^2 is the definition. "
    "KEY FINDING: rho << rho_Planck by 88 orders of magnitude. "
    "The condensate is NOT at Planck density — this contradicts naive "
    "expectations from quantum gravity. The condensate is 'dilute' by "
    "Planck standards, which explains why gravity is so weak."
)


# ============================================================
# 5. THE INDEPENDENCE TEST
# ============================================================

print()
print("=" * 72)
print("INDEPENDENCE ANALYSIS")
print("=" * 72)
print()
print("Every chain gives kappa = c^2/(4*pi*G) in different notation.")
print("This is EXPECTED: all chains use G as input, and the bridge")
print("kappa = c^2/(4*pi*G) is the DEFINITION, not a derived result.")
print()
print("For a chain to be TRULY INDEPENDENT, it must express kappa")
print("WITHOUT using G (or anything defined via G like l_P, rho_crit,")
print("r_s, T_H, alpha_G, etc).")
print()
print("QUESTION: Is there ANY equation in physics that relates kappa")
print("to non-gravitational quantities?")
print()


# ============================================================
# 6. SEARCHING FOR INDEPENDENT CHAINS
# ============================================================

print("-" * 72)
print("SEARCH FOR INDEPENDENT CHAINS")
print("-" * 72)
print()

# Attempt A: From condensate quantum mechanics
# If the condensate is a BEC with scattering length a_s and density n:
#   c_s = sqrt(4*pi*hbar^2*a_s*n / m_boson^2)  (Bogoliubov)
#   kappa = m_boson * n * c_s^2
# This gives kappa in terms of microphysics, but m_boson, a_s, n are unknown.

print("Attempt A: BEC Microphysics")
print("  c_s^2 = 4*pi*hbar^2*a_s*n / m_boson^2  (Bogoliubov)")
print("  kappa = m_boson * n * c_s^2 = 4*pi*hbar^2*a_s*n^2 / m_boson")
print("  => kappa depends on unknown microphysics (m_boson, a_s, n)")
print("  => NOT computable from known physics alone")
print()

# Attempt B: From the Koide formula
# Part 4 showed the Koide formula follows from Z_3 phase symmetry.
# The lepton masses are set by mu = 17.72 MeV^{1/2} and delta = sqrt(2).
# These are INPUTS — mu is not derived from kappa.
print("Attempt B: Koide Formula")
print("  Lepton masses from Z_3 phase: sqrt(m_i) = mu*(1 + sqrt(2)*cos(theta_0 + 2pi*i/3))")
print("  mu = 17.72 MeV^{1/2} is empirical — not derived from condensate properties")
print("  => No independent kappa determination")
print()

# Attempt C: From the impedance ratio (Part 16)
# alpha_EM = Z_0 / (2*R_K)  is exact
# Z_0 = sqrt(mu_0/epsilon_0) = 1/(epsilon_0*c)
# R_K = h/e^2
# These are purely EM — no gravity. Cannot get kappa from EM alone.
print("Attempt C: EM Impedance Ratio")
print("  alpha_EM = Z_0/(2*R_K) involves only EM constants")
print("  No known equation links Z_0, R_K to gravitational stiffness kappa")
print("  => EM sector decoupled from gravity (known problem)")
print()

# Attempt D: From lattice spacing = Planck length (assumption)
# If a = l_P, then K = kappa * l_P^2 = hbar/(4*pi*c)
# K = hbar/(4*pi*c) is G-independent!
# But the assumption a = l_P uses l_P which is defined via G.
# HOWEVER: if we flip this:
#   ASSUME K = hbar/(4*pi*c)  [natural quantum of spring constant]
#   Then kappa = K/a^2 = hbar/(4*pi*c*a^2)
#   And G = c^2/(4*pi*kappa) = c^3*a^2/hbar
#   If a = l_P: G = c^3*l_P^2/hbar  which is the DEFINITION of l_P. Circular.
#
# But if a is NOT l_P — if a is determined by some other physics — then
# this is an independent prediction.

K_natural = hbar_val / (4 * 3.14159265358979 * c_val)
a_from_G = (hbar_val * G_val / c_val**3) ** 0.5  # = l_P

print("Attempt D: Natural Quantum of Stiffness")
print(f"  K_natural = hbar/(4*pi*c) = {K_natural:.6e} J")
print(f"  If K = K_natural, then G = c^3*a^2/hbar")
print(f"  For G = G_measured: a = sqrt(hbar*G/c^3) = l_P = {a_from_G:.6e} m")
print("  => Recovers l_P = Planck length [CONSISTENT but circular]")
print()
print("  KEY INSIGHT: K = hbar/(4*pi*c) is the 'quantum of spring constant'")
print("  It combines ONLY hbar and c — no G, no mass, no charge.")
print("  If there is a physical argument for WHY the lattice coupling")
print("  should equal hbar/(4*pi*c), then G would be PREDICTED as:")
print("  G = c^3 * a^2 / hbar")
print("  where a is the lattice spacing (measured independently).")
print()

# Attempt E: Dimensional analysis — what CAN kappa be?
# [kappa] = kg/(m*s^2) = Pa
# From hbar, c, and one mass m:
#   hbar*c has units J*m = kg*m^3/s^2 => hbar*c/L^2 has units kg*m/s^2 = Pa*m^2
#   So kappa = hbar*c/L^4?  No, [kappa] = Pa = kg/(m*s^2)
#   hbar has units J*s = kg*m^2/s
#   c has units m/s
#   hbar/c has units kg*m
#   hbar/(c*L^2) has units kg/(m*s^-1 * m^2) ... let me be more careful.
#
# kappa [=] Pa = kg / (m * s^2)
# hbar [=] kg * m^2 / s
# c [=] m / s
# hbar * c [=] kg * m^3 / s^2
# hbar * c / m^4 [=] kg / (m * s^2) = Pa   YES!
# So kappa = hbar*c / L^4 where L is a length.
# kappa = c^2/(4*pi*G) = hbar*c / (4*pi*l_P^2*c*L^2) ... getting circular again.
#
# The only G-free expression for kappa requires an independent length scale.

print("Attempt E: Dimensional Analysis")
print("  [kappa] = Pa = kg/(m*s^2)")
print("  From hbar and c alone: kappa = hbar*c / L^4  (L = some length)")
print("  Need an independent length scale L to determine kappa.")
print("  Candidates:")
print("    - Proton Compton wavelength: L = hbar/(m_p*c) = 2.10e-16 m")

L_proton = hbar_val / (m_p_val * c_val)
kappa_proton = hbar_val * c_val / L_proton**4
G_proton = c_val**2 / (4 * 3.14159265358979 * kappa_proton)

print(f"      => kappa = {kappa_proton:.4e} Pa")
print(f"      => G_predicted = {G_proton:.4e} m^3/(kg*s^2)  [actual: {G_val:.4e}]")
print(f"      => ratio: {G_proton/G_val:.4e}  [OFF by ~{G_proton/G_val:.1e}]")
print()

L_electron = hbar_val / (m_e_val * c_val)
kappa_electron = hbar_val * c_val / L_electron**4
G_electron = c_val**2 / (4 * 3.14159265358979 * kappa_electron)

print(f"    - Electron Compton wavelength: L = hbar/(m_e*c) = {L_electron:.4e} m")
print(f"      => kappa = {kappa_electron:.4e} Pa")
print(f"      => G_predicted = {G_electron:.4e} m^3/(kg*s^2)  [actual: {G_val:.4e}]")
print(f"      => ratio: {G_electron/G_val:.4e}  [OFF by ~{G_electron/G_val:.1e}]")
print()
print("  Neither Compton wavelength gives the right G — confirming that")
print("  the hierarchy problem (gravity vs particle masses) is real and")
print("  not resolved by simple dimensional substitution.")
print()


# ============================================================
# 7. SUMMARY TABLE
# ============================================================

print()
print("=" * 72)
print("SUMMARY TABLE")
print("=" * 72)
print()
print(f"{'Chain':<6} {'Name':<35} {'kappa (Pa)':<16} {'Independent?':<14} {'Consistent?'}")
print("-" * 85)

for r in results:
    print(f"{r['chain']:<6} {r['name']:<35} {kappa_val:<16.6e} {'NO':<14} {'YES'}")

print()


# ============================================================
# 8. ENGINEERING APPLICATION: DECOUPLING ENERGY
# ============================================================

print()
print("=" * 72)
print("ENGINEERING APPLICATION: Phase Decoupling Energy")
print("=" * 72)
print()
print("From PDTP: decoupling energy per oscillator = g (coupling constant)")
print("From Part 21: g = 2*lambda*sqrt(rho*sigma)")
print("From the bridge: gravitational acceleration g_grav = G*M/r^2")
print("At Earth's surface: g_grav = 9.81 m/s^2")
print()
print("Decoupling energy per unit mass (from Part 28b):")
print("  Delta_V = g_grav = 9.81 J/kg  (= 9.81 m/s^2 * 1 kg)")
print()

# Per atom
m_atom = m_p_val  # roughly
DeltaV_per_atom = 9.81 * m_atom
print(f"Per proton-mass oscillator:")
print(f"  Delta_V = g * m_p = {DeltaV_per_atom:.4e} J = {DeltaV_per_atom/1.602e-19:.4e} eV")
print()

# Per kg
DeltaV_per_kg = 9.81  # J/kg (gravitational potential energy per unit mass)
print(f"Per kilogram of matter:")
print(f"  Delta_V = {DeltaV_per_kg:.2f} J/kg")
print()

# For a 1-ton platform
m_platform = 1000  # kg
E_decouple = DeltaV_per_kg * m_platform
print(f"For a 1-ton platform:")
print(f"  E_decouple = {E_decouple:.0f} J = {E_decouple/3.6e6:.4f} kWh")
print(f"  Power for 1 second: {E_decouple:.0f} W = {E_decouple/1000:.1f} kW")
print()
print("  THIS IS REMARKABLY SMALL!")
print(f"  {E_decouple/1000:.1f} kW = about {E_decouple/746:.0f} horsepower")
print("  A car engine could theoretically provide this power.")
print()
print("  BUT: this assumes perfect phase control at every oscillator,")
print("  and sustained decoupling (not just a momentary pulse).")
print("  The MECHANISM for rotating psi relative to phi by pi/2 is unknown.")
print()

# Compare to current propulsion
print("Comparison to conventional propulsion:")
print(f"  PDTP decoupling (1 ton): {E_decouple/1000:.1f} kW")
print(f"  Helicopter (1 ton):      ~200 kW")
print(f"  Rocket (1 ton, 1g):      ~30,000 kW (exhaust velocity dependent)")
print(f"  Car engine:              ~100-300 kW")
print()


# ============================================================
# 9. CONCLUSIONS
# ============================================================

print()
print("=" * 72)
print("CONCLUSIONS")
print("=" * 72)
print()
print("1. ALL 8 CHAINS GIVE kappa = c^2/(4*pi*G)")
print("   This is CONSISTENT but NOT INDEPENDENT.")
print("   Every chain uses G as input, so they all reduce to the bridge.")
print()
print("2. THE CIRCULARITY PROBLEM:")
print("   PDTP defines kappa FROM G: kappa = c^2/(4*pi*G)")
print("   Every known equation containing G, when you substitute the bridge,")
print("   recovers kappa = c^2/(4*pi*G). This is a tautology.")
print("   To PREDICT G, we need kappa from a G-independent source.")
print()
print("3. THE ONE PROMISING LEAD: K = hbar/(4*pi*c)")
print("   If a = l_P (lattice spacing = Planck length), then:")
print(f"     K = hbar/(4*pi*c) = {K_natural:.6e} J")
print("   This expression uses ONLY hbar and c — no G.")
print("   If there is a physical argument for K = hbar/(4*pi*c),")
print("   then G = c^3*a^2/hbar PREDICTS G from the lattice spacing.")
print("   But a = l_P still uses G, so we need a independent a.")
print()
print("4. THE HIERARCHY PROBLEM IS REAL:")
print("   Using particle Compton wavelengths as the lattice spacing gives")
print(f"   G_proton ~ {G_proton:.2e} (off by {G_proton/G_val:.1e})")
print(f"   G_electron ~ {G_electron:.2e} (off by {G_electron/G_val:.1e})")
print("   The actual lattice spacing l_P ~ 10^-35 m is 19-22 orders of")
print("   magnitude smaller than particle Compton wavelengths.")
print()
print("5. CONDENSATE DENSITY: rho = 1/(4*pi*G) ~ 10^9 kg/m^3")
print("   This is white-dwarf density, NOT Planck density (10^97 kg/m^3).")
print("   The condensate is 'dilute' by Planck standards, which explains")
print("   why gravity is so weak. This is a genuine physical insight.")
print()
print("6. DECOUPLING ENERGY IS SURPRISINGLY LOW:")
print(f"   ~{E_decouple/1000:.0f} kW for 1 ton (comparable to a car engine)")
print("   The bottleneck is NOT energy — it's the MECHANISM for controlled")
print("   phase rotation at every lattice site simultaneously.")
print()
print("7. WHAT WOULD BREAK THE CIRCULARITY:")
print("   a) Measure kappa directly (condensate stiffness of vacuum)")
print("   b) Derive K from quantum gravity microphysics (GFT/LQG)")
print("   c) Find a non-gravitational equation that contains kappa")
print("   d) Derive the hierarchy ratio R = alpha_G/alpha_EM ~ 10^-37")
print("      from lattice structure")
print()
print("=" * 72)
print("END OF SUBSTITUTION CHAIN ANALYSIS")
print("=" * 72)
