#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
condensate_selfconsist.py -- Phase 10: Condensate Self-Consistency (Part 34)
=============================================================================
TASK (from TODO.md Part 34):
  Investigate whether the BEC self-consistency equation
      omega_gap^2 = (g_coupling * rho_cond) / m_cond
  can fix m_cond (= m_P) from condensate micro-physics alone, without G.

CONTEXT (from Phase 9 / Part 33):
  - Particle = vortex with winding n = m_cond / m_particle  [PDTP Original]
  - G-free chain: m_cond -> n -> a_0 = hbar/(m_cond c) -> G = hbar*c/m_cond^2
  - Strategy A = Strategy B: omega_gap = m_cond c^2 / hbar  [unified]
  - ONE free parameter remains: m_cond.  Can BEC self-consistency fix it?

THE DERIVATION
--------------
We use the Gross-Pitaevskii (GP) framework for the PDTP vacuum condensate.

Key distinction:
  g_PDTP  = m_cond * c^2 / hbar   [Compton angular frequency -- the coupling
                                    in L = g cos(psi - phi); units: rad/s]
  g_GP    = hbar^3 / (m_cond^2 * c)  [GP interaction constant; units: J m^3]
            these are DIFFERENT quantities -- see Step 2 for the derivation.

The GP self-consistency:
  mu = g_GP * n = m_cond * c^2     [chemical potential = rest energy]
  c_s = sqrt(g_GP * n / m_cond) = c  [SPEED OF SOUND = c -- KEY RESULT]
  xi = hbar / sqrt(2 * m_cond * mu) = a_0 / sqrt(2)  [healing length ~ a_0]

RESULT:
  The PDTP condensate is internally consistent for ANY value of m_cond.
  The self-consistency gives c_s = c (always), not a unique m_cond.
  This is new: the condensate is exactly at the sonic limit.

REMAINING GAP:
  m_cond = m_P is still a free parameter.
  BEC self-consistency does not fix it -- a new equation is needed.
  The problem reduces to: what physical principle selects the Planck mass?

Called from main.py as Phase 10.

Usage (standalone):
    cd simulations/solver
    python condensate_selfconsist.py
"""

import sys
import os
import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from sudoku_engine import (HBAR, C, G, K_B, L_P, M_P, M_E, M_P_PROTON,
                            ALPHA_EM, SudokuEngine)
from print_utils import ReportWriter
from orbital_scanner import PARTICLES


# ===========================================================================
# STEP 1 -- RECAP: WHAT PHASE 9 GAVE US
# ===========================================================================

def _recap(rw):
    """Recap Phase 9 results and state the Part 34 question."""
    rw.subsection("Step 1: Recap of Phase 9 and the Part 34 Question")

    rw.print("  PHASE 9 RESULTS (Part 33 -- Vortex Winding):")
    rw.print("    n = m_cond / m_particle  [winding number, PDTP Original]")
    rw.print("    a_0 = hbar / (m_cond * c)  [lattice spacing = Compton wavelength of condensate]")
    rw.print("    G = hbar * c / m_cond^2   [G-free given m_cond]")
    rw.print("    omega_gap = m_cond * c^2 / hbar  [breathing mode gap = quasiparticle mass]")
    rw.print("    Result: G_pred / G_known = 1.000000 for all 11 SM particles")
    rw.print("")
    rw.print("  THE ONE REMAINING QUESTION:")
    rw.print("    m_cond = m_P = 2.176e-8 kg is the free parameter.")
    rw.print("    Can the PDTP condensate's OWN micro-physics fix m_cond,")
    rw.print("    without using G as input?")
    rw.print("")
    rw.print("  APPROACH (from TODO.md Part 34):")
    rw.print("    Use the Gross-Pitaevskii (GP) framework for a weakly interacting BEC.")
    rw.print("    Three candidate self-consistency equations:")
    rw.print("    (a) Thermodynamic: m_cond from BEC critical temperature T_crit")
    rw.print("    (b) GP chemical potential: mu = g_GP * n = m_cond * c^2")
    rw.print("    (c) Speed of sound: c_s = sqrt(g_GP * n / m_cond) = c (?)  <-- test this")
    rw.print("")
    rw.print("  NOTE: The coupling in L = g cos(psi-phi) is g_PDTP = m c^2 / hbar [rad/s].")
    rw.print("  The GP interaction constant g_GP [J m^3] is DIFFERENT -- see Step 2.")
    rw.print("")


# ===========================================================================
# STEP 2 -- G-FREE EXPRESSIONS FOR THE CONDENSATE
# ===========================================================================

def _gfree_expressions(rw):
    """Derive G-free expressions: n, g_GP, mu."""
    rw.subsection("Step 2: G-Free Expressions for the PDTP Condensate")

    rw.print("  GIVEN (all G-free, from Part 33):")
    rw.print("    m_cond  = condensate quasiparticle mass  [free parameter]")
    rw.print("    a_0     = hbar / (m_cond * c)            [lattice spacing, G-free]")
    rw.print("")
    rw.print("  NUMBER DENSITY (quasiparticles per cubic lattice spacing):")
    rw.print("    n = 1 / a_0^3 = (m_cond * c / hbar)^3   [units: m^-3, G-free]")
    rw.print("")
    rw.print("  CHEMICAL POTENTIAL (GP condition: mu = rest energy of condensate quasiparticle):")
    rw.print("    mu = m_cond * c^2                        [units: J, G-free]")
    rw.print("    This sets the energy scale of the condensate.")
    rw.print("")
    rw.print("  GP INTERACTION CONSTANT (from mu = g_GP * n):")
    rw.print("    g_GP = mu / n")
    rw.print("         = m_cond * c^2 / (m_cond * c / hbar)^3")
    rw.print("         = m_cond * c^2 * hbar^3 / (m_cond^3 * c^3)")
    rw.print("         = hbar^3 / (m_cond^2 * c)           [units: J m^3, G-free]")
    rw.print("")
    rw.print("  COMPARISON WITH g_PDTP:")
    rw.print("    g_PDTP = m_cond * c^2 / hbar  [rad/s -- the Lagrangian coupling]")
    rw.print("    g_GP   = hbar^3 / (m_cond^2 * c)  [J m^3 -- GP interaction strength]")
    rw.print("    These are DIFFERENT quantities with different units.")
    rw.print("    g_GP is what enters the BEC speed-of-sound formula.")
    rw.print("")
    rw.print("  NUMERICAL VALUES (for m_cond = m_P = Planck mass):")

    m_cond = M_P   # test with Planck mass
    a_0    = HBAR / (m_cond * C)             # lattice spacing [m]
    n_0    = (m_cond * C / HBAR)**3          # number density [m^-3]
    mu     = m_cond * C**2                   # chemical potential [J]
    g_GP   = HBAR**3 / (m_cond**2 * C)      # GP coupling [J m^3]

    rw.print("    m_cond = m_P   = {:.4e} kg".format(m_cond))
    rw.print("    a_0            = {:.4e} m   (= l_P = {:.4e} m)".format(a_0, L_P))
    rw.print("    n_0            = {:.4e} m^-3".format(n_0))
    rw.print("    mu             = {:.4e} J   (= m_P c^2)".format(mu))
    rw.print("    g_GP           = {:.4e} J m^3".format(g_GP))
    rw.print("")
    rw.print("  CHECK: g_GP * n_0 = mu?")
    check = g_GP * n_0
    rw.print("    g_GP * n_0     = {:.6e} J  (should be {:.6e} J)".format(check, mu))
    rw.print("    Ratio          = {:.8f}  [should be 1.0]".format(check / mu))
    rw.print("")


# ===========================================================================
# STEP 3 -- SPEED OF SOUND: THE KEY RESULT
# ===========================================================================

def _speed_of_sound(rw):
    """Derive and verify c_s = c."""
    rw.subsection("Step 3: Speed of Sound in the PDTP Condensate")

    rw.print("  BOGOLIUBOV SPEED OF SOUND (BEC, weakly interacting):")
    rw.print("    c_s^2 = g_GP * n / m_cond")
    rw.print("")
    rw.print("  SUBSTITUTING G-FREE EXPRESSIONS:")
    rw.print("    g_GP = hbar^3 / (m_cond^2 * c)")
    rw.print("    n    = (m_cond * c / hbar)^3 = m_cond^3 * c^3 / hbar^3")
    rw.print("")
    rw.print("    g_GP * n = [hbar^3 / (m_cond^2 * c)] * [m_cond^3 * c^3 / hbar^3]")
    rw.print("             = m_cond * c^2")
    rw.print("")
    rw.print("    c_s^2 = (g_GP * n) / m_cond")
    rw.print("          = m_cond * c^2 / m_cond")
    rw.print("          = c^2")
    rw.print("")
    rw.print("    c_s   = c   [EXACTLY]")
    rw.print("")
    rw.print("  *** KEY RESULT: The PDTP condensate has speed of sound = c ***")
    rw.print("  *** This is true for ANY value of m_cond -- it is universal. ***")
    rw.print("")
    rw.print("  INTERPRETATION:")
    rw.print("    In a standard BEC: c_s << c (non-relativistic condensate).")
    rw.print("    In the PDTP condensate: c_s = c (relativistic condensate).")
    rw.print("    This means the PDTP condensate is at the quantum critical point")
    rw.print("    where the quasiparticle velocity equals the speed of light.")
    rw.print("    The condensate is a 'sonic black hole' -- perturbations propagate at c.")
    rw.print("")
    rw.print("  NUMERICAL VERIFICATION (all 11 SM particles as m_cond):")

    headers = ["Particle", "m_cond (kg)", "c_s (m/s)", "c_s / c", "Matches c?"]
    widths  = [12, 16, 16, 10, 12]
    rows = []
    all_match = True
    for name, mass, _, _ in PARTICLES:
        m_cond = mass
        n_0    = (m_cond * C / HBAR)**3
        g_GP   = HBAR**3 / (m_cond**2 * C)
        c_s    = np.sqrt(g_GP * n_0 / m_cond)
        ratio  = c_s / C
        match  = "YES" if abs(ratio - 1.0) < 1e-6 else "NO"
        if match == "NO":
            all_match = False
        rows.append([
            name[:12],
            "{:.4e}".format(m_cond),
            "{:.6e}".format(c_s),
            "{:.6f}".format(ratio),
            match,
        ])

    rw.table(headers, rows, widths)
    rw.print("")
    if all_match:
        rw.print("  All 11 particles give c_s = c exactly.  [Analytical result confirmed]")
    else:
        rw.print("  WARNING: Some particles did not give c_s = c.  Check the derivation.")
    rw.print("")


# ===========================================================================
# STEP 4 -- HEALING LENGTH
# ===========================================================================

def _healing_length(rw):
    """Compute the condensate healing length."""
    rw.subsection("Step 4: Healing Length of the PDTP Condensate")

    rw.print("  HEALING LENGTH (BEC, from GP theory):")
    rw.print("    xi = hbar / sqrt(2 * m_cond * mu)")
    rw.print("")
    rw.print("  SUBSTITUTING mu = m_cond * c^2:")
    rw.print("    xi = hbar / sqrt(2 * m_cond * m_cond * c^2)")
    rw.print("       = hbar / (m_cond * c * sqrt(2))")
    rw.print("       = a_0 / sqrt(2)")
    rw.print("       ~ 0.7071 * a_0")
    rw.print("")
    rw.print("  INTERPRETATION:")
    rw.print("    The healing length xi is the distance over which the condensate")
    rw.print("    'heals' a perturbation (e.g., vortex core).  In PDTP:")
    rw.print("    xi = a_0 / sqrt(2) ~ 0.707 * a_0  [about equal to lattice spacing]")
    rw.print("")
    rw.print("    This is internally consistent: the condensate 'knows about' the")
    rw.print("    lattice scale within an O(1) factor.  A factor of sqrt(2) is normal")
    rw.print("    in BEC theory (it appears in the Bogoliubov transformation).")
    rw.print("")
    rw.print("  PHONON FREQUENCY AT k = 1/xi (the characteristic BEC frequency):")
    rw.print("    omega_phonon = c_s / xi")
    rw.print("                = c / (a_0 / sqrt(2))")
    rw.print("                = sqrt(2) * c / a_0")
    rw.print("                = sqrt(2) * m_cond * c^2 / hbar")
    rw.print("                = sqrt(2) * omega_gap")
    rw.print("                ~ 1.414 * omega_gap")
    rw.print("")
    rw.print("    The Bogoliubov phonon is sqrt(2) ~ 1.41 times the PDTP breathing")
    rw.print("    mode gap.  This O(1) factor is the Bogoliubov renormalization.")
    rw.print("")
    rw.print("  NUMERICAL VALUES (m_cond = m_P):")

    m_cond = M_P
    a_0    = HBAR / (m_cond * C)
    mu     = m_cond * C**2
    xi     = HBAR / np.sqrt(2 * m_cond * mu)
    omega_gap = m_cond * C**2 / HBAR
    omega_ph  = C / xi

    rw.print("    a_0         = {:.4e} m".format(a_0))
    rw.print("    xi          = {:.4e} m".format(xi))
    rw.print("    xi / a_0    = {:.6f}  (should be 1/sqrt(2) = {:.6f})".format(
        xi / a_0, 1.0 / np.sqrt(2)))
    rw.print("    omega_gap   = {:.4e} rad/s".format(omega_gap))
    rw.print("    omega_phonon= {:.4e} rad/s".format(omega_ph))
    rw.print("    ratio       = {:.6f}  (should be sqrt(2) = {:.6f})".format(
        omega_ph / omega_gap, np.sqrt(2)))
    rw.print("")


# ===========================================================================
# STEP 5 -- THE CUBIC EQUATION (TODO Analysis)
# ===========================================================================

def _cubic_analysis(rw):
    """Analyze the cubic equation from the TODO and clarify the correct form."""
    rw.subsection("Step 5: The Cubic Equation -- Analysis and Resolution")

    rw.print("  THE TODO PROPOSED:")
    rw.print("    omega_gap^2 = (g_coupling * rho_cond) / m_cond")
    rw.print("    -> m_cond^3 = hbar^2 * g_coupling * rho_cond / c^4")
    rw.print("")
    rw.print("  WHERE (from TODO Part 34):")
    rw.print("    g_coupling = m_cond * c^2 / hbar  [g_PDTP: Compton frequency, rad/s]")
    rw.print("    rho_cond   = m_cond^2 / (4pi * hbar * c)  [PDTP phase density]")
    rw.print("")
    rw.print("  DIMENSIONAL CHECK of omega_gap^2 = g_coupling * rho_cond / m_cond:")
    rw.print("    LHS: omega_gap^2 = [rad^2/s^2]")
    rw.print("    RHS: g_coupling [rad/s] * rho_cond [kg s^2/m^3] / m_cond [kg]")
    rw.print("       = [rad/s] * [s^2/m^3]")
    rw.print("       = [rad s / m^3]   <-- not [rad^2/s^2]")
    rw.print("")
    rw.print("  RESULT: The formula as written has a dimensional mismatch.")
    rw.print("  The PDTP g_coupling [rad/s] is NOT the GP interaction constant g_GP [J m^3].")
    rw.print("  The PDTP rho_cond [kg s^2/m^3] is NOT the number density n [m^-3].")
    rw.print("")
    rw.print("  CORRECT FORMULATION (from GP theory, Step 2-3):")
    rw.print("    c_s^2 = g_GP * n / m_cond  [Bogoliubov, dimensionally consistent]")
    rw.print("    with g_GP [J m^3] and n [m^-3]")
    rw.print("")
    rw.print("  This closes correctly with c_s = c (Step 3).  The 'cubic equation'")
    rw.print("  does not arise -- the self-consistency IS the condition c_s = c.")
    rw.print("")
    rw.print("  WHAT THE CUBIC WOULD GIVE (if forced, in natural units hbar=c=1):")
    rw.print("    In natural units: n = m_cond^3, g_GP = 1/m_cond^2")
    rw.print("    g_GP * n / m_cond = (1/m_cond^2) * m_cond^3 / m_cond = 1 = c^2 = c_s^2")
    rw.print("    -> c_s = 1 = c  [same result: tautological, c_s = c for any m_cond]")
    rw.print("")
    rw.print("  CONCLUSION FROM STEP 5:")
    rw.print("    The BEC self-consistency equation closes into c_s = c.")
    rw.print("    This is always satisfied for any m_cond -- NOT a unique solution.")
    rw.print("    The cubic equation reduces to a tautology in the correct GP framework.")
    rw.print("")


# ===========================================================================
# STEP 6 -- ONE-PARAMETER FAMILY SCAN
# ===========================================================================

def _one_parameter_family(rw, engine):
    """Scan m_cond values and show the family of consistent condensates."""
    rw.subsection("Step 6: The One-Parameter Family of Self-Consistent Condensates")

    rw.print("  The BEC self-consistency (c_s = c) holds for any m_cond.")
    rw.print("  This means there is a one-parameter FAMILY of consistent condensates.")
    rw.print("  Each m_cond gives a consistent condensate with a different G.")
    rw.print("")

    # Scan m_cond from 0.001 m_P to 1000 m_P
    log_range = np.linspace(-3, 3, 7)  # 7 values: m_P * 10^(-3..+3)
    m_cond_values = M_P * 10**log_range

    headers = ["m_cond / m_P", "m_cond (kg)", "G_pred (m^3/kg/s^2)", "G_pred/G_known",
               "a_0 (m)", "c_s / c"]
    widths  = [12, 14, 24, 14, 14, 10]
    rows = []

    for m_cond in m_cond_values:
        a_0    = HBAR / (m_cond * C)
        G_pred = HBAR * C / m_cond**2
        n_0    = (m_cond * C / HBAR)**3
        g_GP   = HBAR**3 / (m_cond**2 * C)
        c_s    = np.sqrt(g_GP * n_0 / m_cond)

        rows.append([
            "{:.3f}".format(m_cond / M_P),
            "{:.4e}".format(m_cond),
            "{:.4e}".format(G_pred),
            "{:.4e}".format(G_pred / G),
            "{:.4e}".format(a_0),
            "{:.6f}".format(c_s / C),
        ])

    rw.table(headers, rows, widths)
    rw.print("")
    rw.print("  OBSERVATIONS:")
    rw.print("    - c_s / c = 1.000000 for EVERY m_cond -- universal, not a constraint")
    rw.print("    - G_pred varies as m_cond^-2 -- a wide range of G values is consistent")
    rw.print("    - Only m_cond = m_P gives G_pred = G_known")
    rw.print("    - The BEC self-consistency does NOT select m_cond = m_P")
    rw.print("")
    rw.print("  THERMODYNAMIC APPROACH (from TODO option a):")
    rw.print("    BEC critical temperature: T_crit ~ hbar^2 n^(2/3) / (m_cond * k_B)")
    rw.print("    Setting m_cond * c^2 = k_B * T_crit:")
    rw.print("      m_cond * c^2 = hbar^2 * n^(2/3) / m_cond")
    rw.print("      m_cond^2 = hbar^2 * n^(2/3) / c^2")
    rw.print("    With n = (m_cond * c / hbar)^3: n^(2/3) = (m_cond * c / hbar)^2")
    rw.print("      m_cond^2 = hbar^2 * (m_cond * c / hbar)^2 / c^2 = m_cond^2  [TAUTOLOGY]")
    rw.print("    Thermodynamic approach: satisfied for any m_cond.  No constraint.")
    rw.print("")


# ===========================================================================
# STEP 7 -- WHAT COULD FIX m_cond?
# ===========================================================================

def _what_fixes_m_cond(rw):
    """Survey what external principle could fix m_cond."""
    rw.subsection("Step 7: What Could Fix m_cond? Paths Forward")

    rw.print("  DIAGNOSIS:")
    rw.print("    The PDTP condensate is self-consistent for any m_cond.")
    rw.print("    This is analogous to GR: the cosmological constant Lambda can be")
    rw.print("    any value -- the Einstein equations don't fix it.")
    rw.print("    Similarly, m_cond (or equivalently G) needs an external principle.")
    rw.print("")

    rw.print("  ANALOGY WITH KNOWN PHYSICS:")
    rw.print("    Standard Model:  m_W = g_weak * v / 2  [Higgs vev v fixes W mass]")
    rw.print("    PDTP:            G = hbar*c / m_cond^2  [m_cond plays the role of v]")
    rw.print("    The question: what is the 'PDTP Higgs' that fixes m_cond?")
    rw.print("")

    rw.print("  CANDIDATE MECHANISMS (with current assessment):")
    rw.print("")
    rw.print("  [A] EXPERIMENTAL MEASUREMENT (Strategy A, most immediate):")
    rw.print("      If LISA/ET measures omega_gap directly:")
    rw.print("        m_cond = hbar * omega_gap / c^2  [G-free]")
    rw.print("        G = c^5 / (hbar * omega_gap^2)   [non-circular]")
    rw.print("      Required omega_gap = m_P c^2/hbar = {:.3e} rad/s".format(
        M_P * C**2 / HBAR))
    rw.print("      = {:.3e} Hz  [Planck frequency -- 43 orders above LISA band]".format(
        M_P * C**2 / (HBAR * 2 * np.pi)))
    rw.print("      Status: Correct in principle; unreachable in practice.")
    rw.print("")
    rw.print("  [B] SYMMETRY BREAKING / RENORMALIZATION GROUP:")
    rw.print("      Perhaps m_cond = m_P is the FIXED POINT of some RG flow.")
    rw.print("      In analogy with the Higgs: the condensate forms at a specific scale")
    rw.print("      determined by dimensional transmutation (like Lambda_QCD).")
    rw.print("      Concretely: the PDTP Lagrangian has coupling K = hbar/(4pi c).")
    rw.print("      At energy scale E, K runs.  The scale where K(E) = 1 (dimensionless)")
    rw.print("      might select m_cond = E/c^2.  This requires a running coupling study.")
    rw.print("      Status: Speculative but well-motivated.  Needs Part 35.")
    rw.print("")
    rw.print("  [C] TOPOLOGICAL QUANTIZATION:")
    rw.print("      From Part 33: n = m_cond / m_particle.  For the condensate itself")
    rw.print("      (m_particle = m_cond): n_self = 1.")
    rw.print("      This says the condensate is its own unit vortex -- but doesn't")
    rw.print("      pick m_cond.  A higher-level topological argument is needed.")
    rw.print("      Status: Circular at this level; needs additional structure.")
    rw.print("")
    rw.print("  [D] DVALI SPECIES MECHANISM (from Phase 8):")
    rw.print("      G = G_bare / N_species  [Dvali et al.]")
    rw.print("      N_species = (m_P / m_fundamental)^2 = n^2")
    rw.print("      If N_species = 1 (no dilution), G_bare = G and m_cond = m_P.")
    rw.print("      The condensate IS the fundamental unit -- G is the bare coupling.")
    rw.print("      Status: This is a restatement, not a derivation.")
    rw.print("")
    rw.print("  BEST PATH FORWARD:")
    rw.print("    Mechanism [B] (RG fixed point) is the most promising.")
    rw.print("    It connects to dimensional transmutation (how QCD generates Lambda_QCD")
    rw.print("    from a dimensionless coupling -- and gravity from K = hbar/(4pi c)).")
    rw.print("    This would make the Planck scale as 'natural' as Lambda_QCD in QCD.")
    rw.print("    NEXT: Part 35 -- Dimensional transmutation in PDTP.")
    rw.print("")


# ===========================================================================
# CONCLUSION
# ===========================================================================

def _conclusion(rw):
    rw.subsection("Phase 10 Conclusion: What Was Achieved")

    rw.print("  WHAT WAS DERIVED (new in Phase 10):")
    rw.print("")
    rw.print("    1. G-free interaction constant [PDTP Original]:")
    rw.print("       g_GP = hbar^3 / (m_cond^2 * c)")
    rw.print("       Derived from mu = g_GP * n = m_cond * c^2 (GP condition)")
    rw.print("       This is G-free and unique -- given m_cond.")
    rw.print("")
    rw.print("    2. Speed of sound = c  [KEY RESULT, PDTP Original]:")
    rw.print("       c_s = sqrt(g_GP * n / m_cond) = c  EXACTLY")
    rw.print("       Verified analytically and numerically for all 11 SM particles.")
    rw.print("       The PDTP condensate is at the relativistic sonic limit.")
    rw.print("       This is ALWAYS true -- independent of m_cond.")
    rw.print("")
    rw.print("    3. Healing length ~ lattice spacing [consistent]:")
    rw.print("       xi = a_0 / sqrt(2) ~ 0.707 * a_0")
    rw.print("       Internally consistent; O(1) Bogoliubov factor expected.")
    rw.print("")
    rw.print("    4. Clarification of 'g_coupling' vs 'g_GP':")
    rw.print("       The PDTP Lagrangian coupling g_PDTP [rad/s] is NOT the GP")
    rw.print("       interaction constant g_GP [J m^3].  Confusing these leads to")
    rw.print("       dimensional inconsistency in the cubic equation from the TODO.")
    rw.print("")
    rw.print("    5. The cubic is a tautology [PDTP finding]:")
    rw.print("       The self-consistency equation reduces to c_s = c,")
    rw.print("       which holds for any m_cond.  No unique m_cond is selected.")
    rw.print("")
    rw.print("  WHAT REMAINS:")
    rw.print("    m_cond = m_P is STILL the free parameter.")
    rw.print("    The condensate is self-consistent for any m_cond with G = hbar*c/m_cond^2.")
    rw.print("    The 'cubic equation' does not fix m_cond -- it confirms c_s = c always.")
    rw.print("")
    rw.print("  PHASE PROGRESS SUMMARY:")
    rw.print("    Phase 1-6:  No particle-physics candidate for a gives G.  [closed]")
    rw.print("    Phase 7:    omega_gap = Planck freq -- outside LISA by 43 orders.  [closed]")
    rw.print("    Phase 8:    n = m_P/m -- vortex topology gives this.  [answered in Phase 9]")
    rw.print("    Phase 9:    n = m_cond/m from vortex core.  G = hbar*c/m_cond^2.  [done]")
    rw.print("    Phase 10:   c_s = c (condensate at sonic limit).  m_cond still free.  [done]")
    rw.print("")
    rw.print("  NEXT THEORETICAL STEP (Part 35):")
    rw.print("    Dimensional transmutation in PDTP.")
    rw.print("    The PDTP coupling K = hbar/(4pi c) [units: kg m] is dimensionful.")
    rw.print("    Does it 'run' with energy scale like alpha_QCD?")
    rw.print("    If K(E) becomes dimensionless at some scale E*, then:")
    rw.print("      m_cond = E* / c^2  [G-free if E* derived from running K alone]")
    rw.print("    This mirrors how Lambda_QCD emerges from the QCD beta function.")
    rw.print("    If it works: G = hbar*c/m_cond^2 = hbar*c^5/E*^2 -- fully G-free!")
    rw.print("")


# ===========================================================================
# ENTRY POINT
# ===========================================================================

def run_condensate_phase(rw, engine):
    """Phase 10 entry point.  Called from main.py."""
    rw.section("Phase 10 -- Condensate Self-Consistency (Part 34)")

    rw.print("  TASK (from TODO.md Part 34):")
    rw.print("    Can BEC self-consistency fix m_cond without G as input?")
    rw.print("")
    rw.print("  KEY RESULT (derived in this phase):")
    rw.print("    c_s = c  [speed of sound in PDTP condensate = speed of light]")
    rw.print("    This is ALWAYS true -- not a constraint on m_cond.")
    rw.print("")
    rw.print("  FINDING: BEC self-consistency confirms PDTP is internally consistent,")
    rw.print("  but does NOT fix m_cond.  A new principle is needed (see Step 7).")
    rw.print("")

    _recap(rw)
    _gfree_expressions(rw)
    _speed_of_sound(rw)
    _healing_length(rw)
    _cubic_analysis(rw)
    _one_parameter_family(rw, engine)
    _what_fixes_m_cond(rw)
    _conclusion(rw)


# ===========================================================================
# STANDALONE EXECUTION
# ===========================================================================

if __name__ == "__main__":
    output_dir = os.path.join(_HERE, "outputs")
    rw = ReportWriter(output_dir, label="condensate_selfconsist")
    engine = SudokuEngine()
    run_condensate_phase(rw, engine)
    rw.close()
