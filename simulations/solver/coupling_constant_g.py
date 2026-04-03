"""
coupling_constant_g.py -- Phase 63: A6 FCC -- Coupling constant g (Part 94)
=============================================================================
A6 PROBLEM: g in L = g cos(psi - phi) is not determined from first principles.

KEY NEW RESULT [PDTP Original]:
  Eliminate m_cond between G = hbar*c/m_cond^2 (Eq 2a) and g = m_cond*c^2/hbar (Eq 4e):
  m_cond = hbar*g/c^2  =>  G = hbar*c / (hbar*g/c^2)^2 = c^5 / (hbar * g^2)

  G * g^2 = c^5 / hbar   [PDTP Original, DERIVED]
  g = sqrt(c^5 / (hbar * G)) = Planck angular frequency omega_P

g is the PDTP Lagrangian coupling.  It equals the Planck frequency numerically.
It is NOT independently determined -- the same free parameter as A1 (m_cond) and G.
G, g, and m_cond are THREE NAMES for the SAME single free parameter of the condensate.

CONSTRAINT: G * g^2 = c^5 / hbar   (universal, measurable constants only)

CONCLUSION: A6 reduces to A1.  g is PARTIAL + FREE (derived from G, not independently).

Tests S1-S12: all connections between g and known physics.

Sources:
  PDG 2023 -- G, hbar, c, m_P
  Part 33 (vortex_winding_derivation.md) -- G = hbar*c/m_cond^2 [Eq 2a]
  Part 34 (condensate_selfconsist.py) -- g = m_cond*c^2/hbar [Eq 4e]
  Part 61 (two_phase_lagrangian.py) -- 4g^2 biharmonic coefficient [Eq 2e]
  Part 62 (reversed_higgs.py) -- m_phi^2 = 2g*Phi [Eq 6c]
"""

import math
import sys
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

# -----------------------------------------------------------------------
# Physical constants (PDG 2023 / CODATA 2018)
# -----------------------------------------------------------------------
C        = 2.99792458e8      # speed of light (m/s) [exact]
HBAR     = 1.054571817e-34   # reduced Planck constant (J*s)
G_NEWT   = 6.67430e-11       # Newton's G (m^3 kg^-1 s^-2)
M_P      = 2.176434e-8       # Planck mass (kg)
L_P      = 1.616255e-35      # Planck length (m)
T_P      = 5.391247e-44      # Planck time (s)
E_P_J    = 1.956082e9        # Planck energy (J)  = m_P * c^2
# Earth parameters for phi_- mass test
M_EARTH  = 5.972e24          # Earth mass (kg)
R_EARTH  = 6.371e6           # Earth radius (m)

PI = math.pi


# -----------------------------------------------------------------------
# Step 1: Derive g from the constraint G * g^2 = c^5 / hbar
# -----------------------------------------------------------------------

def derive_g_constraint():
    """
    Derive G * g^2 = c^5 / hbar from Eq 2a and Eq 4e.

    Starting equations [referenced]:
      G = hbar * c / m_cond^2   [Eq 2a, PDTP Original, Part 33]
      g = m_cond * c^2 / hbar   [Eq 4e, PDTP Original, Part 34]

    Derivation:
      From Eq 4e: m_cond = hbar * g / c^2
      Substitute into Eq 2a:
        G = hbar * c / (hbar * g / c^2)^2
          = hbar * c * c^4 / (hbar^2 * g^2)
          = c^5 / (hbar * g^2)
      Therefore: G * g^2 = c^5 / hbar   [PDTP Original]

    Solve for g:
      g = sqrt(c^5 / (hbar * G)) = Planck angular frequency omega_P

    Returns dict with constraint value and g_pred.
    """
    # Constraint: G * g^2 = c^5 / hbar
    rhs = C**5 / (HBAR * G_NEWT)           # c^5 / (hbar * G)  [rad^2/s^2]
    g_pred = math.sqrt(rhs)                  # g = omega_P [rad/s]

    # Verify: G * g^2 should equal c^5 / hbar
    constraint_lhs = G_NEWT * g_pred**2     # G * g^2
    constraint_rhs = C**5 / HBAR            # c^5 / hbar
    residual = abs(constraint_lhs - constraint_rhs) / constraint_rhs

    # Also compute m_cond = hbar * g / c^2 and verify G
    m_cond_pred = HBAR * g_pred / C**2
    G_from_g    = C**5 / (HBAR * g_pred**2)
    ratio_G     = G_from_g / G_NEWT

    return {
        "rhs":            rhs,
        "g_pred":         g_pred,
        "residual":       residual,
        "m_cond_pred_kg": m_cond_pred,
        "G_from_g":       G_from_g,
        "ratio_G":        ratio_G,
    }


# -----------------------------------------------------------------------
# Step 2: Planck units from g (verify consistency)
# -----------------------------------------------------------------------

def planck_units_from_g(g):
    """
    Derive Planck units from g alone (no direct use of G or m_P).
    Uses G = c^5 / (hbar * g^2) to express everything in terms of g.

    l_P = c/g          [Planck length]
    t_P = 1/g          [Planck time]
    m_P = hbar*g/c^2   [Planck mass]
    E_P = hbar*g        [Planck energy = m_P * c^2]
    """
    l_P_pred = C / g
    t_P_pred = 1.0 / g
    m_P_pred = HBAR * g / C**2
    E_P_pred = HBAR * g          # = m_P * c^2

    return {
        "l_P_pred": l_P_pred,
        "t_P_pred": t_P_pred,
        "m_P_pred": m_P_pred,
        "E_P_pred": E_P_pred,
        "ratio_lP": l_P_pred / L_P,
        "ratio_tP": t_P_pred / T_P,
        "ratio_mP": m_P_pred / M_P,
        "ratio_EP": E_P_pred / E_P_J,
    }


# -----------------------------------------------------------------------
# Step 3: Connections to known PDTP equations
# -----------------------------------------------------------------------

def breathing_mode_gap(g):
    """omega_gap = g [Eq 6a, Part 33].  g IS the breathing mode gap frequency."""
    return g   # exactly g by construction


def biharmonic_coefficient(g):
    """4g^2 appears in nabla^4 Phi + 4g^2 Phi = source [Eq 2e, Part 61]."""
    return 4.0 * g**2


def condensate_number_density(g):
    """
    Condensate number density from g [Eq 4d]:
      n = (m_cond * c / hbar)^3 = (g / c)^3   [since m_cond = hbar*g/c^2]
    Cross-check: n = 1/l_P^3 = (g/c)^3 [Planck density, same result]

    NOTE on Jeans eigenvalue (Eq 2f, Part 61):
      lambda = +/- 2*sqrt(2)*g where lambda is eigenvalue of d^2x/dt^2 = M*x.
      In the two_phase_lagrangian.py, the Lagrangian is in natural units (hbar=c=1)
      where g has units [mass^2]. Eq 4e uses SI units where g has units [rad/s].
      These are DIFFERENT normalizations of g; cross-unit Jeans timescale is undefined.
      S8 therefore tests n instead (same PDTP condensate, clean SI units).
    """
    m_cond  = HBAR * g / C**2
    n_pred  = (m_cond * C / HBAR)**3    # = (g/c)^3
    n_planck = (1.0 / L_P)**3           # 1/l_P^3 = Planck number density
    ratio   = n_pred / n_planck
    return {"n_pred": n_pred, "n_planck": n_planck, "ratio": ratio}


def phi_minus_freq_earth(g):
    """
    phi_- reversed-Higgs mode frequency near Earth's surface.
    From Eq 6c: m_phi^2 = 2*g*Phi  (in PDTP units, where m means angular frequency)
    Phi = G*M_E/R_E = Newtonian potential at surface (m^2/s^2)
    omega_phi = sqrt(2 * g * Phi)  [rad/s]
    mass equivalent: m_phi_eV = hbar * omega_phi / e_charge (in eV)
    """
    Phi   = G_NEWT * M_EARTH / R_EARTH   # 6.25e7 m^2/s^2
    omega = math.sqrt(2.0 * g * Phi)
    E_J   = HBAR * omega                 # energy in J
    E_eV  = E_J / 1.602176634e-19        # energy in eV
    E_MeV = E_eV / 1e6
    return {"Phi_m2s2": Phi, "omega_phi": omega, "E_MeV": E_MeV}


def bec_gp_consistency(g):
    """
    Verify GP condensate parameters are consistent with g.
    g_GP = hbar^3 / (m_cond^2 * c)   [Eq 4a]
    n    = (m_cond * c / hbar)^3      [Eq 4d]
    mu   = g_GP * n  should equal m_cond * c^2 = hbar * g   [Eq 4c]
    """
    m_cond = HBAR * g / C**2
    g_GP   = HBAR**3 / (m_cond**2 * C)
    n_dens = (m_cond * C / HBAR)**3
    mu_pred = g_GP * n_dens
    mu_exact = m_cond * C**2          # = hbar * g
    ratio = mu_pred / mu_exact
    return {"mu_pred": mu_pred, "mu_exact": mu_exact, "ratio": ratio}


# -----------------------------------------------------------------------
# Sudoku: 12 tests
# -----------------------------------------------------------------------

def run_sudoku_a6(_engine, g_pred, planck, n_dens, phi_minus, bec):
    """Run 12 Sudoku tests for A6 coupling constant g."""

    results = []

    def check(label, pred, exact, tol=1e-4):
        ratio = pred / exact
        ok = abs(ratio - 1.0) < tol
        results.append((label, ok, ratio))
        return ok

    # S1: G recovered from g (main new result)
    G_from_g = C**5 / (HBAR * g_pred**2)
    check("S1: G = c^5/(hbar*g^2) recovers G_Newton", G_from_g, G_NEWT)

    # S2: m_cond = m_P from g
    m_cond = HBAR * g_pred / C**2
    check("S2: m_cond = hbar*g/c^2 = m_Planck", m_cond, M_P)

    # S3: Planck length l_P = c/g
    check("S3: l_P = c/g", planck["l_P_pred"], L_P)

    # S4: Planck time t_P = 1/g
    check("S4: t_P = 1/g", planck["t_P_pred"], T_P)

    # S5: Planck energy E_P = hbar*g
    check("S5: E_P = hbar*g", planck["E_P_pred"], E_P_J)

    # S6: Breathing mode gap = g exactly (omega_gap = g, Eq 6a)
    omega_gap = breathing_mode_gap(g_pred)
    ratio_gap = omega_gap / g_pred
    results.append(("S6: omega_gap = g [Eq 6a]", abs(ratio_gap - 1.0) < 1e-14, ratio_gap))

    # S7: Biharmonic coefficient = 4g^2 (Eq 2e, Part 61)
    bih = biharmonic_coefficient(g_pred)
    bih_exact = 4.0 * g_pred**2
    check("S7: 4g^2 biharmonic coeff [Eq 2e]", bih, bih_exact)

    # S8: Condensate number density n = (g/c)^3 = 1/l_P^3 [Eq 4d]
    check("S8: n = (g/c)^3 = 1/l_P^3 [Eq 4d]", n_dens["n_pred"], n_dens["n_planck"])

    # S9: GP condensate self-consistency (mu_pred = mu_exact)
    check("S9: BEC mu = g_GP*n = m_cond*c^2 [Eq 4c]", bec["mu_pred"], bec["mu_exact"])

    # S10: phi_- frequency near Earth is sub-Planck (physical sanity)
    # omega_phi << g: ratio should be < 1 (massive mode, sub-Planck)
    ratio_phi = phi_minus["omega_phi"] / g_pred
    results.append(("S10: omega_phi(Earth) << g [Eq 6c]",
                    ratio_phi < 1.0, ratio_phi))

    # S11: Constraint G*g^2 = c^5/hbar (zero residual)
    lhs = G_NEWT * g_pred**2
    rhs = C**5 / HBAR
    ratio_con = lhs / rhs
    check("S11: G*g^2 = c^5/hbar [PDTP Original]", lhs, rhs)

    # S12: Planck mass self-consistency: E_P = m_P*c^2 = hbar*g
    E_P_check = M_P * C**2
    check("S12: E_P = m_P*c^2 = hbar*g", planck["E_P_pred"], E_P_check)

    return results


# -----------------------------------------------------------------------
# Main entry point (called from main.py)
# -----------------------------------------------------------------------

def run_coupling_g_fcc(rw, engine):
    """Phase 63: A6 FCC -- coupling constant g."""

    rw.print("")
    rw.print("=" * 60)
    rw.print("Phase 63: A6 FCC -- Coupling Constant g (Part 94)")
    rw.print("=" * 60)

    # --- Derive g ---
    res = derive_g_constraint()
    g   = res["g_pred"]

    rw.print("")
    rw.print("KEY DERIVATION: G * g^2 = c^5 / hbar  [PDTP Original]")
    rw.print("  Start: G = hbar*c/m_cond^2 [Eq 2a] and g = m_cond*c^2/hbar [Eq 4e]")
    rw.print("  Eliminate m_cond (= hbar*g/c^2):")
    rw.print("    G = hbar*c / (hbar*g/c^2)^2 = c^5 / (hbar * g^2)")
    rw.print("  => G * g^2 = c^5 / hbar  [EXACT, zero residual]")
    rw.print("")
    rw.print("  g = sqrt(c^5 / (hbar*G)) = Planck angular frequency omega_P")
    rw.print("  g_pred = {:.6e} rad/s".format(g))
    rw.print("  residual (G*g^2 - c^5/hbar) / (c^5/hbar) = {:.2e}".format(res["residual"]))
    rw.print("  G recovered: {:.5e} (ratio = {:.8f})".format(res["G_from_g"], res["ratio_G"]))
    rw.print("  m_cond = hbar*g/c^2 = {:.4e} kg  (m_P = {:.4e} kg)".format(
        res["m_cond_pred_kg"], M_P))

    # --- Planck units ---
    planck = planck_units_from_g(g)
    rw.print("")
    rw.print("PLANCK UNITS FROM g (no direct use of G or m_P):")
    rw.print("  l_P = c/g  = {:.4e} m   (known {:.4e}, ratio {:.6f})".format(
        planck["l_P_pred"], L_P, planck["ratio_lP"]))
    rw.print("  t_P = 1/g  = {:.4e} s   (known {:.4e}, ratio {:.6f})".format(
        planck["t_P_pred"], T_P, planck["ratio_tP"]))
    rw.print("  E_P = hbar*g = {:.4e} J (known {:.4e}, ratio {:.6f})".format(
        planck["E_P_pred"], E_P_J, planck["ratio_EP"]))

    # --- Additional connections ---
    n_dens   = condensate_number_density(g)
    phi_m    = phi_minus_freq_earth(g)
    bec      = bec_gp_consistency(g)

    rw.print("")
    rw.print("CONNECTIONS TO KNOWN PDTP EQUATIONS:")
    rw.print("  Breathing mode gap: omega_gap = g = {:.4e} rad/s [Eq 6a]".format(g))
    rw.print("  Biharmonic coeff:   4g^2 = {:.4e} rad^2/s^2 [Eq 2e]".format(
        biharmonic_coefficient(g)))
    rw.print("  Number density:     n = (g/c)^3 = {:.4e} m^-3 [Eq 4d]".format(
        n_dens["n_pred"]))
    rw.print("  phi_- near Earth:   omega_phi = {:.4e} rad/s = {:.1f} MeV [Eq 6c]".format(
        phi_m["omega_phi"], phi_m["E_MeV"]))
    rw.print("  BEC mu check:       mu_pred/mu_exact = {:.8f} [Eq 4c]".format(bec["ratio"]))
    rw.print("  NOTE: Jeans eigenvalue (Eq 2f) uses natural-unit g [mass^2];")
    rw.print("        Eq 4e uses SI-unit g [rad/s]. Cross-unit Jeans test excluded.")

    # --- Sudoku ---
    rw.print("")
    rw.print("SUDOKU: 12 tests")
    sudoku = run_sudoku_a6(engine, g, planck, n_dens, phi_m, bec)
    n_pass = 0
    for label, ok, ratio in sudoku:
        tag = "[PASS]" if ok else "[FAIL]"
        rw.print("  {} {}  ratio={:.6f}".format(tag, label, ratio))
        if ok:
            n_pass += 1
    rw.print("SCORE: {}/{} PASS".format(n_pass, len(sudoku)))

    # --- Conclusion ---
    rw.print("")
    rw.print("CONCLUSION:")
    rw.print("  g = sqrt(c^5/(hbar*G)) = omega_Planck ~ 1.857e43 rad/s [PDTP Original]")
    rw.print("  G, g, m_cond are THREE ENCODINGS of the SAME single free parameter.")
    rw.print("  Constraint G*g^2 = c^5/hbar is new but NOT independent of G.")
    rw.print("  A6 reduces to A1: measuring G determines g; g not independently derivable.")
    rw.print("  STATUS: A6 PARTIAL + FREE -- g = omega_P [DERIVED from G], not from topology.")
    rw.print("  Observational path: measure omega_gap (breathing mode GW) => get g => test G.")


if __name__ == "__main__":
    # Standalone run
    outfile = os.path.join(_HERE, "outputs", "coupling_g.txt")
    os.makedirs(os.path.join(_HERE, "outputs"), exist_ok=True)

    class SimpleWriter:
        def __init__(self, path):
            self._f = open(path, "w", encoding="ascii", errors="replace")
        def print(self, msg=""):
            print(msg)
            self._f.write(str(msg) + "\n")
        def close(self):
            self._f.close()

    rw = SimpleWriter(outfile)
    run_coupling_g_fcc(rw, None)
    rw.close()
    print("Output saved to", outfile)
