"""
Strider Model Test: +cos (phase-lock) vs -cos (surface tension) in Lagrangian.

The user's insight: the PDTP Lagrangian sign was corrected from -cos to +cos.
If the strider (surface tension) term enters as -cos, the two COMPETE.

Tests whether this competition explains why gravity is weak.
"""
import numpy as np

HBAR = 1.054571817e-34
C    = 2.99792458e8
G    = 6.67430e-11

M_P  = np.sqrt(HBAR * C / G)
L_P  = np.sqrt(HBAR * G / C**3)
M_E  = 9.1093837015e-31
M_MU = 1.883531627e-28
M_TAU = 3.16754e-27
M_PROT = 1.67262192369e-27

K = HBAR / (4 * np.pi * C)
a_0 = L_P
gamma = K / a_0

particles = [
    ("electron", M_E),
    ("muon", M_MU),
    ("tau", M_TAU),
    ("proton", M_PROT),
    ("Planck", M_P),
]

print("=" * 70)
print("  +cos (LOCK) vs -cos (STRIDER) IN THE LAGRANGIAN")
print("=" * 70)
print()
print("SIGN HISTORY:")
print("  Original:  L = ... - g*cos(psi-phi)  [WRONG: unstable]")
print("  Corrected: L = ... + g*cos(psi-phi)  [RIGHT: stable lock]")
print()
print("USER INSIGHT: add strider as -cos (opposite to lock):")
print()
print("  L = K*(d_mu phi)^2")
print("      + g_lock(m) * cos(psi-phi)      [pulls INTO condensate]")
print("      - g_strider(m) * cos(psi-phi)   [surface tension, FLOATS]")
print()
print("  = K*(d_mu phi)^2 + g_eff(m) * cos(psi-phi)")
print("  where g_eff = g_lock - g_strider")
print()
print("  Strider gave: g_strider ~ 1/m (lighter = longer legs = more float)")
print("  This is INVERTED from gravity: alpha_G ~ m^2")
print()
print("  The minus sign FLIPS the inversion:")
print("  g_eff = g_lock - (something/m)")
print()

# ============================================================
# MODEL A: g_lock = constant (condensate bulk coupling)
#          g_strider = C_s / m (from Compton contact length)
# ============================================================
print("=" * 70)
print("  MODEL A: g_lock = const, g_strider = C/m")
print("=" * 70)
print()
print("  g_lock = g_0 (same for all particles -- bulk condensate)")
print("  g_strider = (m_P / m) * g_0 / (4*pi)")
print("  g_eff = g_0 * [1 - m_P/(4*pi*m)]")
print()

fmt = "  %-10s  g_lock=%.2e  g_strid=%.2e  g_eff=%.2e  alpha_G=%.2e  sign=%s"
for name, m in particles:
    g_lock = 1.0
    g_strid = M_P / (4 * np.pi * m)
    g_eff = g_lock - g_strid
    alpha_G = (m / M_P) ** 2
    sign = "+" if g_eff > 0 else "NEG"
    print(fmt % (name, g_lock, g_strid, g_eff, alpha_G, sign))

print()
print("  Result: g_eff is NEGATIVE for all real particles (m << m_P).")
print("  Only Planck mass gives positive g_eff.")
print("  Meaning: strider overwhelms lock -> particles repelled. Wrong.")
print()

# ============================================================
# MODEL B: g_lock ~ m^3, g_strider ~ m (so difference ~ m^3 - m)
# For heavy: m^3 dominates. For light: m dominates.
# ============================================================
print("=" * 70)
print("  MODEL B: What mass dependence WOULD work?")
print("=" * 70)
print()
print("  We need: g_eff = g_lock - g_strider proportional to m^2.")
print("  (because alpha_G = g_eff / (m*c^2) should be (m/m_P)^2)")
print("  Actually: alpha_G = g_eff, so g_eff itself ~ (m/m_P)^2")
print()
print("  g_strider ~ 1/m (from strider equation, inverted)")
print("  g_lock - 1/m = m^2  (what we need)")
print("  g_lock = m^2 + 1/m")
print()
print("  For m << m_P: g_lock ~ 1/m (dominated by strider balance)")
print("  For m ~ m_P:  g_lock ~ m^2 + 1/m ~ m^2")
print()

fmt2 = "  %-10s  g_lock=%.4e  g_strid=%.4e  g_eff=%.4e  alpha_G=%.4e  MATCH"
for name, m in particles:
    x = m / M_P  # dimensionless mass
    g_strid = 1.0 / x  # ~ m_P / m
    g_lock = x**2 + g_strid  # engineered to give g_eff = x^2
    g_eff = g_lock - g_strid
    alpha_G = x**2
    print(fmt2 % (name, g_lock, g_strid, g_eff, alpha_G))

print()
print("  This WORKS but is circular: we engineered g_lock = m^2 + 1/m")
print("  to get g_eff = m^2. The strider term just adds and subtracts 1/m.")
print()

# ============================================================
# MODEL C: Two phases (bulk + surface) -- most physical
# ============================================================
print("=" * 70)
print("  MODEL C: Two phases -- bulk condensate + surface layer")
print("=" * 70)
print()
print("  PHYSICAL PICTURE (oil-water analogy):")
print("  - The condensate has a BULK phase (phi_bulk) and a SURFACE phase (phi_surf)")
print("  - Like water: the surface has different properties than the bulk")
print("  - Particle couples to BOTH but with opposite signs:")
print()
print("  L = + g * cos(psi - phi_bulk)     [sinks into bulk]")
print("      - g * cos(psi - phi_surface)  [floats on surface]")
print()
print("  Using: cos(A) - cos(B) = -2*sin((A+B)/2)*sin((A-B)/2)")
print()
print("  Let phi_avg = (phi_bulk + phi_surf)/2")
print("  Let Delta = (phi_bulk - phi_surf)/2 = half the phase gap")
print()
print("  g_eff = -2g * sin(psi - phi_avg) * sin(Delta)")
print()
print("  NEW VARIABLE: Delta = phase gap between bulk and surface")
print()
print("  If Delta is SMALL (bulk ~ surface): g_eff ~ -2g * Delta * sin(psi-phi)")
print("    -> weak coupling (gravity is weak because surface ~ bulk)")
print()
print("  If Delta = pi/2 (bulk perpendicular to surface): g_eff = max")
print("    -> strong coupling (like black hole)")
print()
print("  KEY QUESTION: Does Delta depend on mass?")
print()
print("  In ocean waves: deeper water has smaller wave amplitude.")
print("  Phase gap between surface and depth z:")
print("    Delta(z) ~ k*z for shallow (linear)")
print("    Delta(z) ~ exp(-k*z) decay for deep")
print()
print("  If particle 'depth' z ~ lambda_C (Compton wavelength):")
print("    Heavier particle -> smaller lambda_C -> shallower -> smaller Delta")
print("    -> WEAKER coupling?? Still backwards!")
print()
print("  BUT WAIT -- flip it:")
print("  If particle depth z ~ 1/lambda_C = m*c/hbar (inverse Compton):")
print("    Heavier particle -> deeper -> LARGER Delta -> stronger coupling")
print("    -> CORRECT direction!")
print()

print("  Testing: Delta(m) = k * m*c/hbar  (depth = inverse Compton)")
print("  g_eff = 2g * sin(Delta) ~ 2g * Delta for small Delta")
print("  g_eff ~ 2g * k * m * c / hbar")
print()
print("  For alpha_G = g_eff ~ (m/m_P)^2:")
print("  2g * k * m / hbar ~ m^2/m_P^2")
print("  -> k ~ m / (2*g*hbar*m_P^2)  ... k depends on m. Not good.")
print()
print("  For alpha_G ~ m^2, we need g_eff ~ m^2.")
print("  sin(Delta) ~ m^2 -> Delta ~ m^2 for small Delta.")
print("  Delta = (m/m_P)^2 * pi/2 would work!")
print()

fmt3 = "  %-10s  Delta=%.4e rad  sin(D)=%.4e  alpha_G=%.4e  ratio=%.4f"
for name, m in particles[:4]:
    x = m / M_P
    Delta = x**2 * np.pi / 2
    g_eff = np.sin(Delta)  # ~ Delta for small Delta
    alpha_G = x**2
    ratio = g_eff / alpha_G if alpha_G > 0 else 0
    print(fmt3 % (name, Delta, g_eff, alpha_G, ratio))

print()
print("  sin(Delta) ~ Delta ~ (m/m_P)^2 * pi/2")
print("  ratio = pi/2 = 1.5708 for all particles (constant!)")
print()
print("  THIS WORKS! The ratio is constant = pi/2.")
print("  Off by a geometric factor of pi/2 which could be absorbed into g.")
print()

# ============================================================
# THE STRIDER-CORRECTED LAGRANGIAN
# ============================================================
print("=" * 70)
print("  THE STRIDER-CORRECTED LAGRANGIAN")
print("=" * 70)
print()
print("  L = K*(d_mu phi_b)^2 + K*(d_mu phi_s)^2")
print("      + Sigma_i g_i * [cos(psi_i - phi_bulk) - cos(psi_i - phi_surf)]")
print()
print("  = K*(d_mu phi_b)^2 + K*(d_mu phi_s)^2")
print("      - 2 * Sigma_i g_i * sin(psi_i - phi_avg) * sin(Delta)")
print()
print("  where Delta = (phi_bulk - phi_surf)/2")
print()
print("  The effective coupling is: g_eff_i = 2*g_i*sin(Delta_i)")
print()
print("  If Delta_i = (m_i/m_P)^2 * pi/2 then:")
print("    g_eff_i ~ g_i * (m_i/m_P)^2")
print("    alpha_G = g_eff_i / g_i = (m_i/m_P)^2  [CORRECT!]")
print()
print("  NEW FREE PARAMETER: Delta replaces g_i")
print("  But Delta has a PHYSICAL meaning: phase gap between bulk and surface")
print()
print("  The hierarchy problem becomes: WHY is Delta so small?")
print("  Delta(electron) = (m_e/m_P)^2 * pi/2 = %.4e radians" %
      ((M_E/M_P)**2 * np.pi/2))
print("  = nearly zero phase gap between bulk and surface")
print("  = the two layers are ALMOST in sync")
print()
print("  PHYSICAL MEANING:")
print("  The gravitational condensate bulk and surface are nearly identical.")
print("  Particles float on a surface that ALMOST matches the bulk below.")
print("  The tiny mismatch (Delta ~ 10^-45) IS gravity.")
print()
print("  Like a water strider on VERY still water:")
print("  The surface barely differs from the bulk below.")
print("  The strider dimples it by a tiny amount.")
print("  That tiny dimple = gravitational coupling.")
print()

print("=" * 70)
print("  STATUS")
print("=" * 70)
print()
print("  POSITIVE:")
print("  - +cos vs -cos competition gives correct mass dependence")
print("    if Delta = (m/m_P)^2 (phase gap between bulk and surface)")
print("  - Physical picture: particle floats between two nearly-identical phases")
print("  - Black hole = Delta -> pi/2 (bulk and surface fully out of phase)")
print("  - Introduces bulk/surface distinction (new testable physics)")
print()
print("  NEGATIVE:")
print("  - Delta(m) = (m/m_P)^2 is ASSUMED, not derived")
print("  - Replaces one free parameter (g_i) with another (Delta)")
print("  - Does not determine m_cond")
print()
print("  OPEN QUESTION:")
print("  Can Delta = (m/m_P)^2 be DERIVED from the depth of the vortex core?")
print("  Vortex core depth z ~ r_core = lambda_C = hbar/(mc)")
print("  Condensate thickness ~ a_0 = l_P = hbar/(m_P*c)")
print("  z/a_0 = m_P/m = 1/sqrt(alpha_G)")
print("  (z/a_0)^2 = (m_P/m)^2 = 1/alpha_G  ... inverted again!")
print("  Need (a_0/z)^2 = (m/m_P)^2 = alpha_G. This is just the definition.")
print()
print("  VERDICT: Model C is the most PHYSICALLY MOTIVATED of all models tested.")
print("  The +cos/-cos competition is real physics (like MIT bag model).")
print("  But it REORGANISES the hierarchy problem, does not solve it.")
print("  Worth adding as Idea G in TODO_02.md.")
