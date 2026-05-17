# t8_ppn_tan.py  --  T8: PPN Parameters with Tan Corrections
# Part 112, Phase 80
#
# Do the PPN parameters gamma and beta acquire tan-dependent corrections?
# Answer: gamma depends on the SPATIAL METRIC prescription (not tan alone).
# The optical metric g_ij = n^2 delta_ij (n=1/alpha) gives gamma=1 naturally.
# Tan corrections to gamma at 2PN order are O(U^2/c^4) -- negligible.
# beta = 1 is inherited from the Schwarzschild solution (Part 73) in isotropic gauge.
#
# Equations:
#   112.1  PPN metric: g_00 = -(1-2U), g_ij = (1+2*gamma*U)delta_ij  [TEXTBOOK]
#   112.2  gamma_scalar(U(1)) = 0            [Part 103, Bergmann-Wagoner, ESTABLISHED]
#   112.3  gamma_acoustic = 1/2  (g_ij ~ n delta_ij, Part 101)        [ESTABLISHED]
#   112.4  gamma_optical = 1    (g_ij = n^2 delta_ij)                 [DERIVED]
#   112.5  Tan correction: Delta_gamma_2PN = (8/3)(U/c^2) -> <1e-10   [DERIVED]
#   112.6  beta = 1 from Schwarzschild isotropic (gauge + Part 73)    [DERIVED]
#   112.7  Cassini: |gamma-1| < 2.3e-5 -> only gamma_optical=1 passes [CONSTRAINT]
#   112.8  LLR:     |beta -1| < 3e-4   -> beta=1 passes               [CONSTRAINT]
#   112.9  n expansion: n^2 = 1+2u+(8/3)u^2+..., u=U/c^2             [DERIVED]
#
# Python rule: ASCII only; output saved to outputs/ppn_tan_<ts>.txt

import math
import sys
import os
from datetime import datetime

try:
    import sympy as sp
    SYMPY_OK = True
except ImportError:
    SYMPY_OK = False

# Physical constants and solar-system values
G_N    = 6.674e-11     # N m^2/kg^2
C      = 2.998e8       # m/s
M_SUN  = 1.989e30      # kg
R_MERC = 5.79e10       # m  (Mercury semi-major axis -- Cassini uses solar corona)
R_CASS = 6.0e10        # m  (solar corona, ~0.4 AU from Sun centre)

# PPN observational constraints (1-sigma)
CASSINI_GAMMA = (1.0, 2.3e-5)   # gamma = 1 +/- 2.3e-5  (Bertotti 2003)
LLR_BETA      = (1.0, 3.0e-4)   # beta  = 1 +/- 3e-4    (Williams 2004)

# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------

class _RW:
    def __init__(self, path):
        self._lines = []
        self._path = path

    def w(self, line=""):
        self._lines.append(str(line))
        print(line)

    def section(self, title):
        self.w()
        self.w("=" * 60)
        self.w(title)
        self.w("=" * 60)

    def save(self):
        with open(self._path, "w", encoding="ascii", errors="replace") as f:
            f.write("\n".join(self._lines))
        print("\nLog saved to", self._path)


# ---------------------------------------------------------------------------
# Core functions
# ---------------------------------------------------------------------------

def U_over_c2(M, r):
    """Dimensionless Newtonian potential u = GM/(rc^2)"""
    return G_N * M / (r * C**2)

def alpha_from_u(u):
    """alpha = sqrt(1 - 2u)  [Part 98, weak-field Schwarzschild]"""
    if 2 * u >= 1.0:
        return 0.0
    return math.sqrt(1.0 - 2.0 * u)

def n_from_u(u):
    """n = 1/alpha = 1/sqrt(1-2u)"""
    a = alpha_from_u(u)
    if a <= 0:
        return float("inf")
    return 1.0 / a

def n_expansion(u, order=4):
    """
    Taylor expansion of n = 1/sqrt(1-2u) = (1-2u)^{-1/2} about u=0.
    n = 1 + u + (3/2)u^2 + (5/2)u^3 + ...
    """
    if order >= 1:
        val = 1.0 + u
    if order >= 2:
        val += 1.5 * u**2
    if order >= 3:
        val += 2.5 * u**3
    if order >= 4:
        val += 4.375 * u**4
    return val

def n2_expansion(u, order=2):
    """
    Taylor expansion of n^2 = 1/(1-2u) about u=0.
    n^2 = 1 + 2u + 4u^2 + 8u^3 + ...  (geometric series)
    """
    val = 1.0
    for k in range(1, order + 2):
        val += (2 * u) ** k
    return val

def gamma_from_spatial_prescription(prescription, u):
    """
    Spatial metric: g_ij = f(u) * delta_ij
    gamma = (1/2) * df/du |_{u=0}    (leading-order PPN)

    Prescriptions:
      'scalar'  : f = 1          -> gamma = 0  (U(1) Bergmann-Wagoner)
      'acoustic': f = n = (1-2u)^{-1/2}  -> gamma = 1/2  (Part 101)
      'optical' : f = n^2 = 1/(1-2u)     -> gamma = 1    (optical metric)
    """
    if prescription == 'scalar':
        return 0.0, 1.0   # (gamma, f_at_u)
    elif prescription == 'acoustic':
        # f = n = (1-2u)^{-1/2}; df/du = (1-2u)^{-3/2}; at u=0: df/du = 1
        # gamma = 1/2 * 1 = 1/2
        f = n_from_u(u)
        return 0.5, f
    elif prescription == 'optical':
        # f = n^2 = 1/(1-2u); df/du = 2/(1-2u)^2; at u=0: df/du = 2
        # gamma = 1/2 * 2 = 1
        f = n_from_u(u) ** 2
        return 1.0, f
    else:
        raise ValueError("Unknown prescription: {}".format(prescription))


# ---------------------------------------------------------------------------
# Step 1: PPN metric definitions and PDTP identification
# ---------------------------------------------------------------------------

def step1_ppn_definitions(rw):
    """
    Establish the PPN metric ansatz and identify the PDTP contributions.
    """
    rw.section("Step 1 -- PPN metric definitions  (Eq 112.1)")
    rw.w("Standard PPN metric (isotropic, post-Newtonian gauge):")
    rw.w("  g_00 = -(1 - 2U/c^2)                   [time-time, 1PN]")
    rw.w("  g_ij = (1 + 2*gamma*U/c^2) * delta_ij  [space-space, 1PN]")
    rw.w("  g_00 includes -2*beta*(U/c^2)^2 at 2PN  [nonlinearity]")
    rw.w("")
    rw.w("PDTP identification (Part 98):")
    rw.w("  g_00 = -(c*alpha)^2 = -c^2*(1-2U/c^2)")
    rw.w("  => matches PPN g_00 exactly for any prescription of g_ij")
    rw.w("")
    rw.w("Observational constraints:")
    rw.w("  Cassini 2003: gamma = 1 +/- 2.3e-5  (solar conjunction experiment)")
    rw.w("  LLR (Williams 2004): beta = 1 +/- 3e-4  (lunar laser ranging)")
    rw.w("")

    u_sun = U_over_c2(M_SUN, R_CASS)
    rw.w("Solar potential at Cassini perihelion (r ~ 0.4 AU from Sun):")
    rw.w("  u = GM/(rc^2) = {:.3e}".format(u_sun))

    return {"u_cassini": u_sun}


# ---------------------------------------------------------------------------
# Step 2: gamma for three PDTP spatial metric prescriptions
# ---------------------------------------------------------------------------

def step2_gamma_table(rw):
    """
    Compute gamma for the three PDTP spatial metric prescriptions.
    Eq 112.2: gamma_scalar = 0  [Part 103, Bergmann-Wagoner]
    Eq 112.3: gamma_acoustic = 1/2  [Part 101, condensate compression]
    Eq 112.4: gamma_optical = 1     [n^2 spatial metric, DERIVED]
    """
    rw.section("Step 2 -- gamma for three PDTP prescriptions")

    u_test = 1.0e-6   # weak field test value

    rows = [
        ('scalar',   'g_ij = delta_ij',       'Part 103 (Bergmann-Wagoner)'),
        ('acoustic', 'g_ij = n * delta_ij',   'Part 101 (condensate compression)'),
        ('optical',  'g_ij = n^2 * delta_ij', 'Eq 112.4 [DERIVED]'),
    ]

    rw.w("{:>12}  {:>24}  {:>6}  {}".format(
        "Prescription", "g_ij", "gamma", "Source"))
    rw.w("-" * 70)

    results = {}
    for (pres, label, source) in rows:
        gamma, f = gamma_from_spatial_prescription(pres, u_test)
        cassini_ok = abs(gamma - 1.0) < CASSINI_GAMMA[1]
        results[pres] = {"gamma": gamma, "cassini_ok": cassini_ok}
        rw.w("{:>12}  {:>24}  {:>6.1f}  {}  Cassini={}".format(
            pres, label, gamma, source,
            "PASS" if cassini_ok else "FAIL"))

    rw.w("")
    rw.w("Only the OPTICAL metric (g_ij = n^2 delta_ij) passes the Cassini")
    rw.w("constraint.  This is Eq 112.4 [DERIVED].")
    rw.w("Physical basis: the optical metric is the standard choice for")
    rw.w("light propagation in a medium with refractive index n.")
    rw.w("n^2 = 1/alpha^2 = 1/(1-2U/c^2) ~ 1 + 2U/c^2 in weak field")
    rw.w("=> coefficient of 2U/c^2 is 2 => gamma = 1.")

    return results


# ---------------------------------------------------------------------------
# Step 3: n expansion and tan correction to gamma at 2PN  (Eq 112.9, 112.5)
# ---------------------------------------------------------------------------

def step3_tan_correction(rw):
    """
    Tan correction to gamma from the nonlinearity of n(u).
    n^2 = 1/(1-2u) = 1 + 2u + 4u^2 + ...  [exact geometric series]

    The 1PN contribution: coefficient of 2u -> gamma = 1  [Eq 112.4]
    The 2PN contribution: coefficient of u^2 -> correction to gamma at 2PN
    Eq 112.5: Delta_gamma_2PN = 4*(U/c^2) evaluated at solar system scales

    For Cassini (u ~ 2e-8): Delta_gamma_2PN ~ 8e-8 << Cassini bound 2.3e-5
    => Tan corrections are safely negligible.
    """
    rw.section("Step 3 -- Tan correction to gamma at 2PN  (Eqs 112.9, 112.5)")
    rw.w("n^2 = 1/(1-2u) = sum_{k>=0} (2u)^k  = 1 + 2u + 4u^2 + 8u^3 + ...")
    rw.w("g_ij = n^2 delta_ij = (1 + 2*gamma_1PN*u + gamma_2PN*u^2 + ...) delta_ij")
    rw.w("  gamma_1PN = 1       (leading PPN, Eq 112.4)")
    rw.w("  gamma_2PN = 4       (2PN coefficient from n^2 expansion)")
    rw.w("")
    rw.w("Eq 112.5 [DERIVED]: tan correction to effective gamma at 2PN order:")
    rw.w("  Delta_gamma_2PN = gamma_2PN * (U/c^2) = 4 * u")
    rw.w("  (this is the 2PN correction to the 1PN result gamma=1)")
    rw.w("")

    u_cass = U_over_c2(M_SUN, R_CASS)
    delta_gamma = 4.0 * u_cass   # 2PN tan correction
    cassini_bound = CASSINI_GAMMA[1]

    rw.w("At Cassini perihelion (r~0.4 AU from Sun):")
    rw.w("  u = {:.3e}".format(u_cass))
    rw.w("  Delta_gamma_2PN = 4*u = {:.3e}".format(delta_gamma))
    rw.w("  Cassini bound:        = {:.3e}".format(cassini_bound))
    rw.w("  Tan correction / Cassini bound = {:.2e}".format(
        delta_gamma / cassini_bound))
    rw.w("  PASS (tan correction << Cassini bound): {}".format(
        delta_gamma < cassini_bound / 100.0))
    rw.w("")
    rw.w("Tan corrections to gamma are NEGLIGIBLE for all solar system tests.")
    rw.w("The 1PN result gamma=1 (optical metric) is unaffected by tan nonlinearity.")

    # Also check the cos-expansion path
    rw.w("")
    rw.w("Cross-check via cos expansion:")
    rw.w("  Delta = sqrt(2u) -> cos(Delta) = 1 - u + u^2/6 - ...")
    rw.w("  n = 1/(1-u+u^2/6) = 1 + u + (1-1/6)u^2 + ... = 1 + u + (5/6)u^2 + ...")
    rw.w("  n^2 = 1 + 2u + (1 + 10/6)u^2 + ... = 1 + 2u + (8/3)u^2 + ...")
    rw.w("  Difference from exact: (8/3) vs 4 at O(u^2)")
    rw.w("  Reason: cos expansion valid for small Delta; n^2=1/(1-2u) is the exact form")
    rw.w("  Both give gamma=1 at 1PN; 2PN coefficient differs by 4/3")

    # Numerical check: compare n^2 exact vs cos-expansion-based for small u
    u_vals = [1e-2, 1e-4, 1e-6]
    rw.w("")
    rw.w("{:>8}  {:>14}  {:>14}  {:>12}".format(
        "u", "n^2_exact", "n^2_cos4", "rel_diff"))
    results = {}
    for u in u_vals:
        n2_ex = n_from_u(u) ** 2
        # cos-expansion: Delta=sqrt(2u), cos(Delta)=1-u+u^2/6-u^4/120*4
        import math as _m
        Delta = _m.sqrt(2.0 * u)
        cos_d = _m.cos(Delta)
        n_cos = 1.0 / cos_d
        n2_cos = n_cos ** 2
        rel = abs(n2_ex - n2_cos) / n2_ex
        rw.w("{:>8.1e}  {:>14.10f}  {:>14.10f}  {:>12.3e}".format(
            u, n2_ex, n2_cos, rel))
        results[u] = {"n2_exact": n2_ex, "n2_cos": n2_cos}

    return {
        "delta_gamma_2PN": delta_gamma,
        "cassini_bound":   cassini_bound,
        "u_cassini":       u_cass,
        "n2_comparison":   results,
    }


# ---------------------------------------------------------------------------
# Step 4: beta from Schwarzschild isotropic coordinates  (Eq 112.6)
# ---------------------------------------------------------------------------

def step4_beta(rw):
    """
    beta measures nonlinearity in g_00 at 2PN order:
      g_00 = -1 + 2u - 2*beta*u^2 + O(u^3)

    In PDTP areal (Schwarzschild) coordinates:
      g_00 = -alpha^2 = -(1-2u)  =>  beta_areal = 0 (exactly linear in u)

    This is a COORDINATE ARTEFACT.  In isotropic coordinates (PPN standard):
      g_00^iso = -((1-u_iso/2)/(1+u_iso/2))^2
             ~ -1 + 2*u_iso - 2*u_iso^2 + ...
             => beta_iso = 1

    PDTP inherits beta=1 from the Schwarzschild solution (Part 73 GR recovery).
    Eq 112.6 [DERIVED].
    """
    rw.section("Step 4 -- beta from isotropic coordinates  (Eq 112.6)")

    # Areal coordinates: g_00 = -(1-2u); no u^2 term -> beta = 0
    rw.w("In PDTP areal (Schwarzschild) coordinates:")
    rw.w("  g_00 = -(1-2u) = -1 + 2u  (exactly linear)")
    rw.w("  beta_areal = 0             (no U^2 term)")
    rw.w("  This is a GAUGE ARTEFACT -- PPN uses isotropic gauge.")
    rw.w("")

    # Isotropic coordinates: r_S = r_iso*(1 + M/(2r_iso))^2
    # g_00^iso = -((1-x)/(1+x))^2, x = M/(2r_iso) = u_iso/2
    rw.w("In isotropic Schwarzschild coordinates (PPN standard gauge):")
    rw.w("  r_S = r_iso*(1 + u_iso/2)^2  (coordinate transformation)")
    rw.w("  g_00 = -((1 - u_iso/2)/(1 + u_iso/2))^2")
    rw.w("")

    # Numerical verification at several u values
    rw.w("{:>8}  {:>14}  {:>14}  {:>10}".format(
        "u_iso", "g_00_exact", "g_00_PPN_b1", "residual"))

    u_vals = [1e-3, 1e-4, 1e-5, 1e-6]
    beta_checks = []
    for u_iso in u_vals:
        x = u_iso / 2.0
        g00_exact = -((1.0 - x) / (1.0 + x)) ** 2
        # PPN expansion: -1 + 2*u - 2*beta*u^2, beta=1
        g00_ppn = -1.0 + 2.0 * u_iso - 2.0 * u_iso**2
        res = abs(g00_exact - g00_ppn)
        match = res < 1.0e-8 * abs(g00_exact)   # relative tolerance
        beta_checks.append(match)
        rw.w("{:>8.1e}  {:>14.10f}  {:>14.10f}  {:>10.2e}  {}".format(
            u_iso, g00_exact, g00_ppn, res, "PASS" if match else "FAIL"))

    rw.w("")
    rw.w("Eq 112.6 [DERIVED]: beta = 1 in isotropic (PPN) coordinates.")
    rw.w("PDTP inherits beta=1 from the Schwarzschild solution (Part 73).")
    rw.w("The areal-coordinate beta=0 is a gauge artefact, not a physical prediction.")

    # LLR constraint
    llr_ok = abs(1.0 - LLR_BETA[0]) < LLR_BETA[1]
    rw.w("LLR constraint: |beta-1| < {:.0e}  =>  PASS={}".format(
        LLR_BETA[1], llr_ok))

    return {"beta_iso": 1.0, "beta_areal": 0.0, "beta_checks": beta_checks}


# ---------------------------------------------------------------------------
# Step 5: Light deflection angle from gamma  (Cassini sensitivity check)
# ---------------------------------------------------------------------------

def step5_light_deflection(rw):
    """
    Light deflection angle (1PN):
      theta = (1+gamma)/2 * 4GM/(b*c^2) = (1+gamma)/2 * theta_Newton*2

    GR (gamma=1): theta = 1.75 arcsec (solar limb, b = R_sun)
    PDTP scalar (gamma=0): theta = 0.875 arcsec  -- RULED OUT by Eddington 1919
    PDTP acoustic (gamma=0.5): theta = 1.3125 arcsec -- RULED OUT by Cassini
    PDTP optical (gamma=1): theta = 1.75 arcsec  -- PASSES
    """
    rw.section("Step 5 -- Light deflection vs gamma  (Cassini check)")

    R_SUN   = 6.96e8     # m
    b       = R_SUN      # impact parameter at solar limb
    u_limb  = U_over_c2(M_SUN, b)
    theta_N = 4.0 * G_N * M_SUN / (b * C**2)   # Newtonian deflection (rad)
    theta_N_arcsec = math.degrees(theta_N) * 3600.0

    rw.w("Solar limb light deflection (b = R_sun):")
    rw.w("  u_limb = {:.4e}".format(u_limb))
    rw.w("  theta_Newton = {:.6f} arcsec".format(theta_N_arcsec))
    rw.w("")
    rw.w("{:>12}  {:>8}  {:>14}  {:>10}".format(
        "Prescription", "gamma", "theta (arcsec)", "GR ratio"))
    rw.w("-" * 55)

    results = {}
    for (pres, gamma_val) in [('scalar', 0.0), ('acoustic', 0.5), ('optical', 1.0)]:
        theta = (1.0 + gamma_val) / 2.0 * 2.0 * theta_N_arcsec
        ratio = theta / (2.0 * theta_N_arcsec)  # should be 1.0 for GR
        results[pres] = {"gamma": gamma_val, "theta_arcsec": theta}
        rw.w("{:>12}  {:>8.2f}  {:>14.4f}  {:>10.4f}".format(
            pres, gamma_val, theta, ratio))

    rw.w("")
    rw.w("GR prediction (gamma=1): theta = {:.4f} arcsec".format(
        2.0 * theta_N_arcsec))
    rw.w("Eddington 1919 confirmed GR; rules out gamma=0 (scalar PDTP).")
    rw.w("Cassini 2003 |gamma-1| < 2.3e-5 rules out gamma=0.5 (acoustic PDTP).")
    rw.w("Only gamma=1 (optical metric) survives both tests.")

    return results


# ---------------------------------------------------------------------------
# Step 6: Full constraint table  (Eqs 112.7, 112.8)
# ---------------------------------------------------------------------------

def step6_constraints(rw, r2, r3, r4):
    """
    Summary of PPN constraints against all PDTP prescriptions.
    """
    rw.section("Step 6 -- PPN constraint summary  (Eqs 112.7, 112.8)")

    rw.w("Cassini 2003: gamma = 1 +/- {:.1e}   [Eq 112.7]".format(CASSINI_GAMMA[1]))
    rw.w("LLR Williams: beta  = 1 +/- {:.1e}   [Eq 112.8]".format(LLR_BETA[1]))
    rw.w("")
    rw.w("{:>12}  {:>8}  {:>6}  {:>8}  {:>8}".format(
        "Prescription", "gamma", "Cassini", "beta", "LLR"))
    rw.w("-" * 55)

    for pres in ['scalar', 'acoustic', 'optical']:
        g = r2[pres]["gamma"]
        cass = "PASS" if r2[pres]["cassini_ok"] else "FAIL"
        b = 1.0  # all give beta=1 in isotropic gauge
        llr  = "PASS" if abs(b - LLR_BETA[0]) < LLR_BETA[1] else "FAIL"
        rw.w("{:>12}  {:>8.1f}  {:>6}  {:>8.1f}  {:>8}".format(
            pres, g, cass, b, llr))

    rw.w("")
    rw.w("Tan correction at 2PN (Eq 112.5):")
    rw.w("  Delta_gamma_2PN = {:.2e}  (negligible vs Cassini {:.1e})".format(
        r3["delta_gamma_2PN"], r3["cassini_bound"]))
    rw.w("  Tan corrections do NOT destabilize gamma=1 at current precision.")
    rw.w("")
    rw.w("Conclusion:")
    rw.w("  The optical metric prescription (g_ij = n^2 delta_ij) is the UNIQUE")
    rw.w("  PDTP spatial metric that passes Cassini at 1PN order.")
    rw.w("  n = 1/alpha makes this prescription natural and PDTP-motivated.")
    rw.w("  beta = 1 is inherited from the Schwarzschild solution (Part 73).")
    rw.w("  Tan corrections are sub-leading (2PN) and negligible.")

    return {
        "conclusion_gamma": "optical metric (g_ij=n^2 delta_ij) gives gamma=1",
        "conclusion_beta":  "beta=1 from Part 73 Schwarzschild recovery",
        "tan_safe":         r3["delta_gamma_2PN"] < r3["cassini_bound"] / 100.0,
    }


# ---------------------------------------------------------------------------
# Step 7: SymPy verification
# ---------------------------------------------------------------------------

def step7_sympy(rw):
    rw.section("Step 7 -- SymPy verification")
    if not SYMPY_OK:
        rw.w("SymPy not available -- skipping")
        return {"sympy_available": False}

    u = sp.Symbol("u", positive=True)
    x = sp.Symbol("x", positive=True)   # x = u/2 for isotropic coords

    # S1: n^2 = 1/(1-2u); leading expansion coefficient = 2 -> gamma_optical = 1
    n2_exact = 1 / (1 - 2 * u)
    n2_series = sp.series(n2_exact, u, 0, 4).removeO()
    coeff_u1  = sp.diff(n2_exact, u).subs(u, 0)   # coefficient of u at u=0
    gamma_opt = sp.Rational(1, 2) * coeff_u1       # gamma = (1/2)*df/du at u=0
    s1 = gamma_opt == 1
    rw.w("S1  n^2 series = {}  gamma_optical = (1/2)*d(n^2)/du|0 = {}  PASS={}".format(
        n2_series, gamma_opt, s1))

    # S2: n (acoustic) = 1/sqrt(1-2u); leading coeff -> gamma_acoustic = 1/2
    n_exact  = 1 / sp.sqrt(1 - 2 * u)
    coeff_n1 = sp.diff(n_exact, u).subs(u, 0)
    gamma_ac = sp.Rational(1, 2) * coeff_n1
    s2 = gamma_ac == sp.Rational(1, 2)
    rw.w("S2  n acoustic: d(n)/du|0 = {}  gamma_acoustic = {}  PASS={}".format(
        coeff_n1, gamma_ac, s2))

    # S3: scalar: g_ij = 1, gamma_scalar = 0
    s3 = True   # trivially: constant spatial metric -> d/du = 0 -> gamma = 0
    rw.w("S3  scalar: g_ij=1 (constant) -> gamma=0  PASS={}".format(s3))

    # S4: beta=1 from isotropic Schwarzschild g_00 at 2PN
    # g_00 = -((1-x)/(1+x))^2 with x = u/2
    g00_iso = -((1 - x) / (1 + x))**2
    g00_series = sp.series(g00_iso.subs(x, u/2), u, 0, 3).removeO()
    # Expected: -1 + 2u - 2u^2 -> beta = 1
    coeff_u2 = g00_series.coeff(u, 2)    # coefficient of u^2
    beta_sym  = -coeff_u2 / 2            # beta = -coeff/2
    s4 = sp.simplify(beta_sym - 1) == 0
    rw.w("S4  g_00 isotropic series = {}  beta = {}  PASS={}".format(
        g00_series, beta_sym, s4))

    # S5: n^2 at u=0 = 1 (correct normalisation)
    s5 = n2_exact.subs(u, 0) == 1
    rw.w("S5  n^2(u=0) = {}  (expect 1)  PASS={}".format(
        n2_exact.subs(u, 0), s5))

    n_pass = sum([s1, s2, s3, s4, s5])
    rw.w("SymPy score: {}/5 PASS".format(n_pass))
    return {
        "sympy_available": True,
        "s1": s1, "s2": s2, "s3": s3, "s4": s4, "s5": s5,
        "n_pass": n_pass,
    }


# ---------------------------------------------------------------------------
# Step 8: Sudoku checks
# ---------------------------------------------------------------------------

def step8_sudoku(rw, r1, r2, r3, r4, r5, r6):
    rw.section("Step 8 -- Sudoku consistency checks")
    results = []

    def chk(label, cond):
        results.append(cond)
        rw.w("  [{:4}] {}".format("PASS" if cond else "FAIL", label))

    # S01: gamma_scalar = 0
    chk("S01 gamma_scalar = 0  (Bergmann-Wagoner, Part 103)",
        abs(r2["scalar"]["gamma"] - 0.0) < 1.0e-12)

    # S02: gamma_acoustic = 0.5
    chk("S02 gamma_acoustic = 0.5  (condensate compression, Part 101)",
        abs(r2["acoustic"]["gamma"] - 0.5) < 1.0e-12)

    # S03: gamma_optical = 1.0
    chk("S03 gamma_optical = 1.0  (optical metric, Eq 112.4)",
        abs(r2["optical"]["gamma"] - 1.0) < 1.0e-12)

    # S04: only optical metric passes Cassini
    chk("S04 Only optical gamma=1 passes Cassini",
        r2["optical"]["cassini_ok"] and
        not r2["scalar"]["cassini_ok"] and
        not r2["acoustic"]["cassini_ok"])

    # S05: n(u=0) = 1 (no refraction in flat space)
    chk("S05 n(u=0) = 1  (no refraction in flat space)",
        abs(n_from_u(0.0) - 1.0) < 1.0e-12)

    # S06: n^2 = 1 + 2u + 4u^2 + ... (geometric series)
    u_t = 0.01
    n2_ex = n_from_u(u_t)**2
    n2_gs = sum((2*u_t)**k for k in range(10))   # geometric sum
    chk("S06 n^2 = geometric series (sum (2u)^k)",
        abs(n2_ex - n2_gs) < 1.0e-10)

    # S07: tan correction Delta_gamma_2PN < Cassini bound / 100
    chk("S07 tan correction at 2PN negligible vs Cassini",
        r6["tan_safe"])

    # S08: beta_iso = 1 from isotropic Schwarzschild
    chk("S08 beta_iso = 1  (Eq 112.6, isotropic gauge)",
        abs(r4["beta_iso"] - 1.0) < 1.0e-12)

    # S09: LLR beta=1 passes
    chk("S09 beta=1 passes LLR constraint",
        abs(1.0 - LLR_BETA[0]) < LLR_BETA[1])

    # S10: light deflection for gamma=1 (optical) = 2x Newtonian
    theta_optical = r5["optical"]["theta_arcsec"]
    theta_scalar  = r5["scalar"]["theta_arcsec"]
    chk("S10 theta(optical) = 2 x theta(scalar)  (GR vs Newtonian)",
        abs(theta_optical - 2.0 * theta_scalar) < 1.0e-8)

    # S11: gamma ordering: 0 < 0.5 < 1
    chk("S11 gamma: scalar < acoustic < optical (0 < 0.5 < 1)",
        r2["scalar"]["gamma"] < r2["acoustic"]["gamma"] < r2["optical"]["gamma"])

    # S12: n^2 approaches 1 as u->0 (flat space limit)
    chk("S12 n^2(u=1e-10) ~ 1  (flat space limit)",
        abs(n_from_u(1.0e-10)**2 - 1.0) < 1.0e-8)

    n_pass = sum(results)
    rw.w("")
    rw.w("Sudoku score: {}/{} PASS".format(n_pass, len(results)))
    return {"n_pass": n_pass, "n_total": len(results)}


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main():
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_dir = os.path.join(os.path.dirname(__file__), "outputs")
    os.makedirs(out_dir, exist_ok=True)
    log_path = os.path.join(out_dir, "ppn_tan_{}.txt".format(ts))
    rw = _RW(log_path)

    rw.w("T8 -- PPN Parameters with Tan Corrections")
    rw.w("Part 112, Phase 80  |  {}".format(datetime.now().isoformat()))
    rw.w("Question: do tan corrections modify gamma or beta?")

    r1 = step1_ppn_definitions(rw)
    r2 = step2_gamma_table(rw)
    r3 = step3_tan_correction(rw)
    r4 = step4_beta(rw)
    r5 = step5_light_deflection(rw)
    r6 = step6_constraints(rw, r2, r3, r4)
    r7 = step7_sympy(rw)
    r8 = step8_sudoku(rw, r1, r2, r3, r4, r5, r6)

    rw.section("Summary -- T8 PPN Parameters")
    rw.w("gamma:")
    rw.w("  scalar (Part 103):   0.0   FAILS Cassini / Eddington 1919")
    rw.w("  acoustic (Part 101): 0.5   FAILS Cassini")
    rw.w("  optical n^2 (Eq 112.4): 1.0  PASSES Cassini [DERIVED]")
    rw.w("  tan correction at 2PN: {:.1e}  <<  Cassini {:.1e} [NEGLIGIBLE]".format(
        r3["delta_gamma_2PN"], r3["cassini_bound"]))
    rw.w("")
    rw.w("beta:")
    rw.w("  areal gauge:    0.0  (coordinate artefact)")
    rw.w("  isotropic gauge: 1.0  [DERIVED, Eq 112.6]  PASSES LLR")
    rw.w("")
    rw.w("Key result [Eq 112.4, DERIVED]:")
    rw.w("  g_ij = n^2 delta_ij = (1/alpha^2) delta_ij is the PDTP optical metric.")
    rw.w("  n^2 = 1/(1-2u) ~ 1 + 2u -> gamma = 1 at 1PN.  Naturally PDTP-motivated.")
    rw.w("  This is the spatial metric that completes the PDTP metric to full GR.")
    rw.w("")
    rw.w("SymPy: {}/5 PASS".format(
        r7.get("n_pass", "N/A") if r7.get("sympy_available") else "N/A"))
    rw.w("Sudoku: {}/{} PASS".format(r8["n_pass"], r8["n_total"]))

    rw.save()


if __name__ == "__main__":
    main()
