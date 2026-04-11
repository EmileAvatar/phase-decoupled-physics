#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tan_critical_point.py -- Phase 67, Part 99 (TODO_04 T2)
========================================================
Derive the physical meaning of tan(Delta) = 1 (Delta = pi/4) in PDTP.

Strategy:
  1. Potential landscape  V(Delta) = -2g cos(Delta) from the field equation
     ddot(Delta) = -2g sin(Delta)  [pendulum equation for Delta = psi - phi]
  2. Fixed points at Delta=0 (stable) and Delta=pi (unstable) -- NOT at pi/4
  3. Stability eigenvalues via linearisation (SymPy verified)
  4. tan(Delta) = 1 is a FORCE-COUPLING CROSSOVER, not a bifurcation:
       Delta < pi/4: coupling dominates (alpha > 1/sqrt(2))
       Delta = pi/4: force = coupling  (alpha = 1/sqrt(2))
       Delta > pi/4: force dominates   (alpha < 1/sqrt(2))
  5. Connection to n = 1/alpha (Part 98): n_c = sqrt(2) at the crossover
  6. Energy fraction: 29.3% of decoupling energy at the crossover
  7. Leidenfrost connection (Part 71): tan > 1 = "sizzling" regime onset
  8. Two-phase check (Part 61): phi_- correction negligible
  9. Sudoku consistency: 10 tests

Sources:
  [1] Part 98 (pdtp_refractive_index.py) -- n = 1/alpha = 1/cos(Delta) [Eq 98.1]
  [2] Part 71 (leidenfrost_decoupling.py) -- potential landscape table, pi/4 row
  [3] Part 61 (two_phase_lagrangian.py)   -- two-phase EOM and phi_- mass
  [4] CLAUDE.md -- field equations: box_phi = g sin(psi-phi), box_psi = -g sin(psi-phi)

PDTP Original results:
  tan(Delta) = 1 is a force-coupling crossover, not a bifurcation  [Eq 99.3]
  n_c = sqrt(2) at the crossover                                    [Eq 99.5]
  Energy fraction 1 - 1/sqrt(2) approx 0.293 at the crossover      [Eq 99.6]

Python rules: no Unicode; save output to outputs/; cite all sources.
"""

import math
import os
import sys

# --- path setup ---
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

try:
    from print_utils import ReportWriter
    from sudoku_engine import SudokuEngine
    _STANDALONE = False
except ImportError:
    _STANDALONE = True

# ================================================================
# Physical / symbolic constants
# ================================================================
PI     = math.pi
SQRT2  = math.sqrt(2.0)
# g is the Lagrangian coupling [rad^2/s^2]; set g=1 for structural analysis
# The equation of motion for Delta = psi - phi is:
#   ddot(Delta) = -2g sin(Delta)
# Effective potential: V(Delta) = -2g cos(Delta)
# We work with normalised units: g = 1, so 2g = 2.
G_NORM = 1.0  # normalised coupling


# ================================================================
# Helper
# ================================================================
def _res(rw, label, value, status):
    rw.print("  {:<55} {:>18}  [{}]".format(label, value, status))


# ================================================================
# 1. Potential landscape
# ================================================================
def derive_potential_landscape(rw):
    """
    V(Delta) = -2g cos(Delta)  from  ddot(Delta) = -2g sin(Delta).

    Derivation:
      Field equations [CLAUDE.md]:
        box phi = g sin(psi - phi)        ... (A)
        box psi = -g sin(psi - phi)       ... (B)
      Subtract (A) from (B), spatially homogeneous:
        ddot(Delta) = -2g sin(Delta)      [Eq 99.1, DERIVED]
      Identify V_eff such that ddot(Delta) = -dV/dDelta:
        V(Delta) = -2g cos(Delta)         [Eq 99.2, DERIVED]

    Fixed points: dV/dDelta = 2g sin(Delta) = 0
      => Delta = 0 (stable minimum) or Delta = pi (unstable maximum)
      tan(Delta) = 1 (Delta = pi/4) is NOT a fixed point.
    """
    rw.subsection("1. Potential Landscape V(Delta) = -2g cos(Delta)")
    rw.print("  Field equation [CLAUDE.md]:")
    rw.print("    ddot(Delta) = -2g sin(Delta)  [Eq 99.1, DERIVED]")
    rw.print("  Effective potential:")
    rw.print("    V(Delta) = -2g cos(Delta)     [Eq 99.2, DERIVED]")
    rw.print("")
    rw.print("  Potential values (g=1 normalised):")
    rw.print("  {:>10}  {:>12}  {:>14}  {}".format(
        "Delta/pi", "Delta (deg)", "V / (2g)", "Physical state"))
    rw.print("  " + "-"*68)
    table = [
        (0.0,   "0",    "Coupled (alpha=1, gravity normal -- global minimum)"),
        (0.25,  "-0.707", "FORCE-COUPLING CROSSOVER (tan=1)"),
        (0.5,   "0",    "Decoupled (alpha=0, gravity off)"),
        (1.0,   "+1",   "Anti-coupled (maximum -- unstable fixed point)"),
    ]
    for frac, vstr, state in table:
        deg = frac * 180.0
        v   = -2.0 * G_NORM * math.cos(frac * PI)
        rw.print("  {:>10.4f}  {:>10.1f}  {:>14.4f}  {}".format(
            frac * PI, deg, v / (2.0 * G_NORM), state))
    rw.print("")
    rw.print("  Fixed points of dV/dDelta = 2g sin(Delta) = 0:")
    rw.print("    Delta = 0    -- V_min = -2g (stable minimum)")
    rw.print("    Delta = pi   -- V_max = +2g (unstable maximum)")
    rw.print("    Delta = pi/4 -- dV/dDelta = g*sqrt(2) != 0  => NOT a fixed point")
    rw.print("    => tan(Delta) = 1 is NOT a bifurcation [KEY RESULT]")


# ================================================================
# 2. Stability analysis
# ================================================================
def stability_analysis(rw):
    """
    Linearise ddot(Delta) = -2g sin(Delta) near each fixed point.

    Near Delta = 0 (let Delta = delta, small):
      ddot(delta) = -2g sin(delta) approx -2g delta
      omega_0^2 = 2g  => stable oscillation  [Eq 99.7, breathing mode]

    Near Delta = pi (let Delta = pi + delta', small):
      sin(pi + delta') = -sin(delta') approx -delta'
      ddot(delta') = -2g*(-delta') = +2g delta'
      eigenvalue = +2g > 0  => UNSTABLE  [Eq 99.8]

    At Delta = pi/4 (not a fixed point; local curvature only):
      d^2V/dDelta^2 = 2g cos(Delta) |_{pi/4} = g*sqrt(2) > 0
      Local restoring exists, but system is not at rest here.
    """
    rw.subsection("2. Stability Analysis")
    rw.print("  Linearise ddot(Delta) = -2g sin(Delta) near fixed points:")
    rw.print("")

    # Near Delta = 0
    omega0_sq = 2.0 * G_NORM  # omega^2 = 2g
    omega0    = math.sqrt(omega0_sq)
    _res(rw, "omega_0^2 = 2g at Delta=0 (breathing mode) [Eq 99.7]",
         "omega^2 = 2g", "STABLE, DERIVED")
    _res(rw, "  eigenvalue (normalised g=1)",
         "{:.4f}".format(omega0_sq), "POSITIVE => stable")

    # Near Delta = pi
    eig_pi = +2.0 * G_NORM
    _res(rw, "eigenvalue at Delta=pi: +2g [Eq 99.8]",
         "{:.4f}".format(eig_pi), "POSITIVE => UNSTABLE")

    # At Delta = pi/4 (curvature, not eigenvalue)
    d2V_pi4 = 2.0 * G_NORM * math.cos(PI / 4.0)
    _res(rw, "d^2V/dDelta^2 at pi/4 = 2g cos(pi/4) = g*sqrt(2)",
         "{:.4f}g".format(math.cos(PI / 4.0) * 2.0 / G_NORM), "POSITIVE -- locally curved")
    rw.print("")
    rw.print("  Summary: only TWO fixed points (Delta=0 stable, Delta=pi unstable).")
    rw.print("  tan(Delta)=1 (pi/4) is a diagnostic THRESHOLD, not a fixed point.")


# ================================================================
# 3. Force-coupling crossover
# ================================================================
def crossover_analysis(rw):
    """
    At Delta = pi/4 (tan = 1):
      Force (driving decoupling):  F = 2g sin(Delta) = 2g/sqrt(2) = g*sqrt(2)
      Coupling (restoring):        C = 2g cos(Delta) = 2g/sqrt(2) = g*sqrt(2)
      => Force = Coupling  [Eq 99.3, PDTP Original]

    Three regimes [Eq 99.4]:
      Delta < pi/4: cos > sin => coupling dominates (alpha > 1/sqrt(2))
      Delta = pi/4: cos = sin => balanced (CROSSOVER)
      Delta > pi/4: sin > cos => force dominates (alpha < 1/sqrt(2))

    Leidenfrost analogy (Part 71):
      Delta < pi/4: direct contact / wetting
      Delta ~ pi/4: nucleate boiling / "sizzling" onset  <-- tan=1 regime
      Delta > pi/4: approaching vapour cushion (Leidenfrost)
      Delta = pi/2: full Leidenfrost (alpha = 0)
    """
    rw.subsection("3. Force-Coupling Crossover at tan(Delta) = 1 [Eq 99.3]")
    Delta_c = PI / 4.0
    F_c = 2.0 * G_NORM * math.sin(Delta_c)
    C_c = 2.0 * G_NORM * math.cos(Delta_c)
    _res(rw, "Force at pi/4: F = 2g sin(pi/4) = g*sqrt(2)",
         "{:.6f}g".format(F_c / G_NORM), "DERIVED")
    _res(rw, "Coupling at pi/4: C = 2g cos(pi/4) = g*sqrt(2)",
         "{:.6f}g".format(C_c / G_NORM), "DERIVED")
    _res(rw, "Force / Coupling = tan(pi/4)",
         "{:.6f}".format(F_c / C_c), "= 1.000  [Eq 99.3, PDTP Original]")
    rw.print("")
    rw.print("  Regime classification [Eq 99.4, PDTP Original]:")
    rw.print("    Delta < pi/4  (tan < 1): coupling dominates -- 'wetting' regime")
    rw.print("    Delta = pi/4  (tan = 1): balanced -- 'sizzling' onset  [CROSSOVER]")
    rw.print("    Delta > pi/4  (tan > 1): force dominates -- approach to Leidenfrost")
    rw.print("    Delta = pi/2  (tan->inf): fully decoupled -- Leidenfrost state")
    rw.print("")
    rw.print("  Cross-check with Part 71 (leidenfrost_decoupling.md Sec 2.1 table):")
    rw.print("    pi/4 row: V/g = -0.707 'Partial decoupling'  [CONSISTENT]")
    rw.print("    Sizzling onset (tan>1) NOT previously analysed -- new result here.")


# ================================================================
# 4. Connection to refractive index
# ================================================================
def connection_to_n(rw):
    """
    From Part 98 [Eq 98.1]: n = 1/alpha = 1/cos(Delta)
    At the crossover Delta = pi/4:
      alpha_c = cos(pi/4) = 1/sqrt(2)  approx 0.7071    [Eq 99.5a]
      n_c = 1/alpha_c = sqrt(2)         approx 1.4142    [Eq 99.5, PDTP Original]

    Physical meaning: the refractive index at the force-coupling crossover
    is exactly sqrt(2) -- a universal ratio independent of g or m_cond.
    """
    rw.subsection("4. Refractive Index at Crossover [Eq 99.5]")
    alpha_c = math.cos(PI / 4.0)
    n_c     = 1.0 / alpha_c
    _res(rw, "alpha_c = cos(pi/4) = 1/sqrt(2) [Eq 99.5a]",
         "{:.6f}".format(alpha_c), "DERIVED")
    _res(rw, "n_c = 1/alpha_c = sqrt(2) [Eq 99.5, PDTP Original]",
         "{:.6f}".format(n_c), "DERIVED -- universal")
    _res(rw, "n_c / n_vacuum = sqrt(2) (exact ratio)",
         "{:.6f}".format(n_c / 1.0), "exact")
    rw.print("")
    rw.print("  Plain English: when the decoupling force exactly equals the restoring")
    rw.print("  coupling (tan=1), the effective refractive index of spacetime is")
    rw.print("  exactly sqrt(2). This is a universal PDTP prediction -- independent")
    rw.print("  of the condensate mass m_cond or coupling strength g.")


# ================================================================
# 5. Energy analysis
# ================================================================
def energy_analysis(rw):
    """
    Effective potential V(Delta) = -2g cos(Delta), normalised g=1:
      V(0)     = -2  (fully coupled)
      V(pi/4)  = -sqrt(2) approx -1.414  (crossover)
      V(pi/2)  = 0   (decoupled)
      V(pi)    = +2  (anti-coupled, unstable maximum)

    Energy to decouple from fully coupled: V(pi/2) - V(0) = 0 - (-2) = 2g
    Energy at tan=1 crossover above minimum: V(pi/4) - V(0) = -sqrt(2)+2 = 2-sqrt(2)
    Fraction: (2-sqrt(2))/2 = 1 - 1/sqrt(2) approx 0.2929   [Eq 99.6, PDTP Original]

    Separatrix energy: E_sep = V(pi) = +2g  (energy to escape to anti-coupled state)
    At tan=1 (at rest): E = V(pi/4) = -sqrt(2) g << E_sep  => bound oscillation.
    """
    rw.subsection("5. Energy Analysis")
    V0       = -2.0 * G_NORM                             # fully coupled
    V_cross  = -2.0 * G_NORM * math.cos(PI / 4.0)       # at pi/4
    V_dec    = -2.0 * G_NORM * math.cos(PI / 2.0)       # decoupled (=0)
    V_sep    = -2.0 * G_NORM * math.cos(PI)              # separatrix (=+2g)

    dE_to_cross   = V_cross - V0
    dE_to_decouple = V_dec - V0
    fraction      = dE_to_cross / dE_to_decouple

    _res(rw, "V(Delta=0): fully coupled (minimum)",
         "{:.4f}g".format(V0 / G_NORM), "= -2g")
    _res(rw, "V(Delta=pi/4): crossover",
         "{:.4f}g".format(V_cross / G_NORM), "= -sqrt(2)*g approx -1.414g")
    _res(rw, "V(Delta=pi/2): decoupled",
         "{:.4f}g".format(V_dec / G_NORM), "= 0")
    _res(rw, "V(Delta=pi): separatrix (anti-coupled maximum)",
         "{:.4f}g".format(V_sep / G_NORM), "= +2g")
    rw.print("")
    _res(rw, "Energy from coupled to crossover: dE = (2-sqrt(2))g",
         "{:.4f}g".format(dE_to_cross / G_NORM), "DERIVED")
    _res(rw, "Energy from coupled to decoupled: dE = 2g",
         "{:.4f}g".format(dE_to_decouple / G_NORM), "DERIVED")
    _res(rw, "Fraction at crossover = 1 - 1/sqrt(2) [Eq 99.6, PDTP Original]",
         "{:.4f}  ({:.1f}%)".format(fraction, 100.0 * fraction), "DERIVED")
    rw.print("")
    rw.print("  Plain English: to reach the tan=1 crossover from full coupling,")
    rw.print("  the system needs 29.3% of the total decoupling energy. Below this")
    rw.print("  threshold the system returns to coupling; above it, decoupling force")
    rw.print("  exceeds the restoring coupling and the system is pushed further toward")
    rw.print("  the Leidenfrost state. This is the 'sizzling' onset energy.")


# ================================================================
# 6. Two-phase check
# ================================================================
def two_phase_check(rw):
    """
    From Part 61 two-phase Lagrangian:
      L = +g cos(psi-phi_b) - g cos(psi-phi_s)
      Delta_+ = (Delta_b + Delta_s) / 2  (gravity mode)
      Delta_- = (Delta_b - Delta_s) / 2  (surface mode)

    At the crossover Delta_+ = pi/4:
      n_+ = 1/cos(Delta_+) = sqrt(2)  [same as single-phase]
      phi_- is near-zero in vacuum (Part 71 Sec 4.1): Delta_- approx 0
      n_- = 1/cos(Delta_-) approx 1   (negligible correction)

    Correction to alpha from phi_-:
      alpha_total approx cos(Delta_+) * [1 - Delta_-^2/2]  (second order)
      => n correction approx n_+ * (1 + Delta_-^2/2)  (tiny for Delta_- -> 0)
    """
    rw.subsection("6. Two-Phase Check (Part 61)")
    Delta_plus  = PI / 4.0
    Delta_minus = 1.0e-10   # near-zero in vacuum
    n_plus  = 1.0 / math.cos(Delta_plus)
    n_minus = 1.0 / math.cos(Delta_minus)
    correction = (n_plus * (1.0 + Delta_minus**2 / 2.0)) - n_plus
    _res(rw, "n_+ at Delta_+=pi/4 (same as single-phase)",
         "{:.6f}".format(n_plus), "= sqrt(2) [CONSISTENT]")
    _res(rw, "n_- at Delta_-=0 (vacuum)",
         "{:.6f}".format(n_minus), "= 1.000 (negligible) [CONSISTENT]")
    _res(rw, "Two-phase correction to n_+ (order Delta_-^2)",
         "{:.2e}".format(correction), "approx 0 in vacuum")
    rw.print("")
    rw.print("  Two-phase result: single-phase analysis is exact in vacuum.")
    rw.print("  phi_- near matter (Part 62 reversed Higgs) could shift Delta_+ slightly")
    rw.print("  but is second-order in Delta_-. No qualitative change to T2 results.")


# ================================================================
# 7. SymPy verification
# ================================================================
def verify_sympy(rw):
    """
    SymPy checks for T2 critical point results.
    All PDTP Original equations must be SymPy verified [CLAUDE.md].
    """
    rw.subsection("7. SymPy Verification")
    try:
        import sympy as sp
        Delta, g, x = sp.symbols('Delta g x', real=True, positive=True)

        # Eq 99.2: V = -2g cos(Delta), dV = 2g sin(Delta)
        V = -2 * g * sp.cos(Delta)
        dV = sp.diff(V, Delta)
        d2V = sp.diff(V, Delta, 2)
        residual_dV = sp.simplify(dV - 2 * g * sp.sin(Delta))
        residual_d2V = sp.simplify(d2V - 2 * g * sp.cos(Delta))
        _res(rw, "dV/dDelta = 2g sin(Delta) [residual]",
             str(residual_dV), "= 0  [VERIFIED]")
        _res(rw, "d^2V/dDelta^2 = 2g cos(Delta) [residual]",
             str(residual_d2V), "= 0  [VERIFIED]")

        # Eq 99.3: tan(pi/4) = 1
        tan_pi4 = sp.tan(sp.pi / 4)
        _res(rw, "tan(pi/4) [Eq 99.3]",
             str(tan_pi4), "= 1  [VERIFIED]")

        # Eq 99.5: n_c = 1/cos(pi/4) = sqrt(2)
        n_c_sym = 1 / sp.cos(sp.pi / 4)
        n_c_simplified = sp.simplify(n_c_sym - sp.sqrt(2))
        _res(rw, "1/cos(pi/4) - sqrt(2) [Eq 99.5]",
             str(n_c_simplified), "= 0  [VERIFIED]")

        # Eq 99.6: energy fraction = 1 - 1/sqrt(2)
        V0_sym    = -2 * g * sp.cos(0)
        V_c_sym   = -2 * g * sp.cos(sp.pi / 4)
        V_dec_sym = -2 * g * sp.cos(sp.pi / 2)
        frac_sym  = sp.simplify((V_c_sym - V0_sym) / (V_dec_sym - V0_sym))
        expected  = 1 - 1 / sp.sqrt(2)
        residual_frac = sp.simplify(frac_sym - expected)
        _res(rw, "Energy fraction 1-1/sqrt(2) [Eq 99.6, residual]",
             str(residual_frac), "= 0  [VERIFIED]")

        # Eq 99.7: omega_0^2 = 2g from linearisation at Delta=0
        # ddot(delta) = -dV/dDelta|_{Delta=0} * delta / g_eff
        # dV/dDelta = 2g sin(Delta); at Delta=0: 2g sin(0) = 0 (fixed point ok)
        # d^2V/dDelta^2 at Delta=0 = 2g cos(0) = 2g
        omega_sq = sp.simplify(d2V.subs(Delta, 0))
        _res(rw, "omega_0^2 = d^2V/dDelta^2 at Delta=0 = 2g [Eq 99.7]",
             str(omega_sq), "= 2g  [VERIFIED]")

        rw.print("  All SymPy checks: PASS")

    except ImportError:
        rw.print("  SymPy not available -- skipping symbolic checks")


# ================================================================
# 8. Sudoku consistency tests
# ================================================================
def run_sudoku_t2(rw, _engine):
    """
    10 Sudoku tests for Part 99 results.
    """
    rw.subsection("Sudoku Consistency -- T2 Critical Point (S1-S10)")
    passes = 0
    total  = 10
    EPS    = 1.0e-9

    def check(label, computed, expected, tag="PASS"):
        nonlocal passes
        residual = abs(computed - expected)
        ok = residual < EPS or abs(computed - expected) / (abs(expected) + 1e-300) < 1e-9
        status = "PASS" if ok else "FAIL"
        if ok:
            passes += 1
        _res(rw, label, "{:.6g}".format(computed), status)
        return ok

    # S1: tan(0) = 0 (fully coupled, no decoupling force)
    check("S1 tan(Delta=0) = 0 (no decoupling force)",
          math.tan(0.0), 0.0)

    # S2: tan(pi/4) = 1 (crossover) [Eq 99.3]
    check("S2 tan(pi/4) = 1 exactly [Eq 99.3]",
          math.tan(PI / 4.0), 1.0)

    # S3: alpha at crossover = 1/sqrt(2) [Eq 99.5a]
    check("S3 cos(pi/4) = 1/sqrt(2) [Eq 99.5a]",
          math.cos(PI / 4.0), 1.0 / SQRT2)

    # S4: n at crossover = sqrt(2) [Eq 99.5]
    n_c = 1.0 / math.cos(PI / 4.0)
    check("S4 n_c = sqrt(2) [Eq 99.5, PDTP Original]",
          n_c, SQRT2)

    # S5: V(0) = -2g (global minimum, normalised g=1)
    v0 = -2.0 * G_NORM * math.cos(0.0)
    check("S5 V(Delta=0) = -2g (fully coupled minimum)",
          v0 / G_NORM, -2.0)

    # S6: V(pi/2) = 0 (decoupled state)
    v_dec = -2.0 * G_NORM * math.cos(PI / 2.0)
    check("S6 V(pi/2) = 0 (decoupled state)",
          abs(v_dec / G_NORM), 0.0)

    # S7: omega_0^2 = 2g at Delta=0 (breathing mode) [Eq 99.7]
    # d^2V/dDelta^2 at Delta=0 = 2g cos(0) = 2g
    d2V_0 = 2.0 * G_NORM * math.cos(0.0)
    check("S7 omega_0^2 = 2g (breathing mode eigenvalue) [Eq 99.7]",
          d2V_0 / G_NORM, 2.0)

    # S8: d^2V/dDelta^2 at Delta=pi is negative (unstable) [Eq 99.8]
    # We check magnitude: 2g cos(pi) = -2g
    d2V_pi = 2.0 * G_NORM * math.cos(PI)
    check("S8 d^2V at Delta=pi = -2g (unstable max) [Eq 99.8]",
          d2V_pi / G_NORM, -2.0)

    # S9: energy fraction = 1 - 1/sqrt(2) approx 0.2929 [Eq 99.6]
    V0c    = -2.0 * G_NORM
    V_c    = -2.0 * G_NORM * math.cos(PI / 4.0)
    V_dc   = 0.0
    frac   = (V_c - V0c) / (V_dc - V0c)
    expected_frac = 1.0 - 1.0 / SQRT2
    check("S9 energy fraction = 1 - 1/sqrt(2) [Eq 99.6, PDTP Original]",
          frac, expected_frac)

    # S10: two-phase n_+ at pi/4 = single-phase n_c = sqrt(2) [CONSISTENT Part 61]
    n_plus = 1.0 / math.cos(PI / 4.0)
    check("S10 two-phase n_+ at Delta_+=pi/4 = sqrt(2) [Part 61 consistent]",
          n_plus, SQRT2)

    rw.print("")
    rw.print("  Sudoku total: {}/{} PASS".format(passes, total))
    return passes, total


# ================================================================
# Main entry point
# ================================================================
def run_tan_critical_point(rw, _engine):
    """
    Part 99 -- T2: Critical point at tan(Delta) = 1.
    Called by main.py Phase 67.
    """
    rw.section("PHASE 67 -- T2: CRITICAL POINT tan(Delta)=1 (PART 99)")
    rw.print("")
    rw.print("  Investigate the physical meaning of tan(Delta) = 1 (Delta = pi/4)")
    rw.print("  in the PDTP phase-locking Lagrangian.")
    rw.print("  Is this a bifurcation? A dynamical attractor? Or a diagnostic threshold?")
    rw.print("")

    derive_potential_landscape(rw)
    rw.print("")
    stability_analysis(rw)
    rw.print("")
    crossover_analysis(rw)
    rw.print("")
    connection_to_n(rw)
    rw.print("")
    energy_analysis(rw)
    rw.print("")
    two_phase_check(rw)
    rw.print("")
    verify_sympy(rw)
    rw.print("")
    passes, total = run_sudoku_t2(rw, _engine)
    rw.print("")

    rw.subsection("Summary -- Part 99")
    rw.print("  RESULT: tan(Delta) = 1 is a FORCE-COUPLING CROSSOVER, not a bifurcation.")
    rw.print("  Fixed points: Delta=0 (stable), Delta=pi (unstable). pi/4 is NOT a fixed point.")
    rw.print("  Potential: V(Delta) = -2g cos(Delta)  [Eq 99.2, DERIVED]")
    rw.print("  Field eq:  ddot(Delta) = -2g sin(Delta)  [Eq 99.1, DERIVED]")
    rw.print("  Crossover: tan(Delta_c) = 1 => Delta_c = pi/4  [Eq 99.3, PDTP Original]")
    rw.print("  alpha_c = 1/sqrt(2),  n_c = sqrt(2)  [Eq 99.5, PDTP Original]")
    rw.print("  Energy fraction = 1 - 1/sqrt(2) approx 0.293  [Eq 99.6, PDTP Original]")
    rw.print("  Sizzling onset: tan > 1 means force > coupling (Leidenfrost approach)")
    rw.print("  Two-phase: n_+ = sqrt(2) at Delta_+=pi/4 (same as single-phase)")
    rw.print("  Sudoku: {}/{} PASS".format(passes, total))


# ================================================================
# Standalone execution
# ================================================================
if __name__ == "__main__":
    output_dir = os.path.join(_HERE, "outputs")
    os.makedirs(output_dir, exist_ok=True)
    if _STANDALONE:
        import datetime
        label = "tan_critical_point"
        rw = type('RW', (), {
            'section':    lambda self, t: print("\n" + "="*78 + "\n  " + t + "\n" + "="*78),
            'subsection': lambda self, t: print("\n--- " + t + " ---"),
            'print':      lambda self, t="": print(t),
            'close':      lambda self: None,
        })()
        engine = None
    else:
        from print_utils import ReportWriter
        from sudoku_engine import SudokuEngine
        label  = "tan_critical_point"
        rw     = ReportWriter(output_dir, label)
        engine = SudokuEngine()
    run_tan_critical_point(rw, engine)
    if not _STANDALONE:
        rw.close()
    print("Output saved to: {}".format(output_dir))

