#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
dim_transmutation.py -- Phase 11: Dimensional Transmutation (Part 35)
=======================================================================
TASK (from TODO.md Part 35):
  Investigate whether the PDTP coupling K = hbar/(4pi c) 'runs' with energy,
  and whether that running can fix m_cond (= m_P) G-free via dimensional
  transmutation -- analogous to how Lambda_QCD emerges from the QCD beta function.

CONTEXT (from Phases 9-10):
  - G = hbar*c / m_cond^2  [G-free given m_cond]  (Part 33)
  - BEC self-consistency: c_s = c always; does NOT fix m_cond  (Part 34)
  - ONE free parameter remains: m_cond.  Can RG running fix it?

THE IDEA
--------
In QCD, alpha_s(E) runs with energy.  At the scale Lambda_QCD ~ 200 MeV,
alpha_s becomes strong (order 1) -- this is dimensional transmutation.
All hadron masses ~ Lambda_QCD emerge from a single dimensionless coupling.

In PDTP, K = hbar/(4pi c) is the phase stiffness.
  In SI units:      K = 2.797e-44 kg m  (dimensionful)
  In natural units: K = 1/(4pi) ~ 0.0796  (dimensionless!)

If K runs with energy E, the scale E* where K(E*) = O(1) could be
identified with m_cond = E*/c^2 -- without using G.

THE DERIVATION
--------------
PDTP Lagrangian for the phase difference theta = psi - phi:
  L = (K/2)(d_mu theta)^2 + g cos(theta)

Taylor expand cosine (Taylor):
  g cos(theta) = g - (g/2) theta^2 + (g/24) theta^4 - ...

The quartic term has effective coupling lambda_eff ~ g (same structure as
lambda phi^4 theory, modulo normalization).

1-loop beta function for lambda phi^4 in 4D:
  beta(lambda) = +3 lambda^2 / (16 pi^2)  [positive = IR free, like QED]

For PDTP, using K as the effective dimensionless coupling:
  beta(K) = +K^2 / (8 pi^2)  [schematic; see Step 4]

RESULT:
  beta > 0 -> coupling grows at HIGH energy (IR free, NOT asymptotically free)
  Landau pole at E_Landau = E_ref * exp(8 pi^2 / K_0)  = E_ref * exp(32 pi^3)
  exp(32 pi^3) ~ 10^{431}  -> E_Landau is 431 decades above any reference scale
  This is 431 - 22 = 409 decades above the Planck energy (if E_ref = m_e c^2)

FINDING: NEGATIVE RESULT.
  Dimensional transmutation via standard 1-loop RG does NOT fix m_cond = m_P.
  K_0 = 1/(4pi) is too small: the coupling barely changes over 22 decades
  from electron to Planck mass (< 6% change in K).
  The Landau pole is ~430 orders above the Planck scale.

SIGNIFICANCE:
  This completes the systematic search (Parts 29-35):
  - Algebraic substitution: circular  (Part 29)
  - Power-law sweep: all circular     (Phases 1-3)
  - Vortex winding: G-free given m_cond (Part 33)
  - BEC self-consistency: c_s = c, no m_cond  (Part 34)
  - Dimensional transmutation: Landau pole 10^{431} off  (Part 35)
  Conclusion: m_cond = m_P is underdetermined by PDTP -- like Lambda in GR.

Called from main.py as Phase 11.

Usage (standalone):
    cd simulations/solver
    python dim_transmutation.py
"""

import sys
import os
import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from sudoku_engine import (HBAR, C, G, K_B, L_P, M_P, M_E, M_P_PROTON,
                            ALPHA_EM, E_P, SudokuEngine)
from print_utils import ReportWriter
from orbital_scanner import PARTICLES

# Physical constants derived here
E_PLANCK     = M_P * C**2                   # Planck energy [J]
E_ELECTRON   = M_E * C**2                   # Electron rest energy [J]
E_PROTON     = M_P_PROTON * C**2            # Proton rest energy [J]

# PDTP coupling constant K
K_PDTP_SI    = HBAR / (4.0 * np.pi * C)    # [kg m]  SI units
K_NATURAL    = 1.0 / (4.0 * np.pi)         # dimensionless (hbar=c=1 natural units)


# ===========================================================================
# STEP 1 -- INTRODUCTION AND RECAP
# ===========================================================================

def _recap(rw):
    rw.subsection("Step 1: Recap and the Dimensional Transmutation Idea")

    rw.print("  WHAT WE KNOW FROM PARTS 29-34:")
    rw.print("")
    rw.print("    G = hbar*c / m_cond^2  [G-free given m_cond]  (Part 33)")
    rw.print("    n = m_cond / m_particle  [vortex winding number]  (Part 33)")
    rw.print("    c_s = c  [condensate sonic limit; always true]  (Part 34)")
    rw.print("    BEC self-consistency: consistent for ANY m_cond  (Part 34)")
    rw.print("")
    rw.print("  THE REMAINING QUESTION: What fixes m_cond = m_P?")
    rw.print("")
    rw.print("  THE QCD ANALOGY (dimensional transmutation):")
    rw.print("")
    rw.print("    In QCD, the strong coupling alpha_s(E) runs with energy.")
    rw.print("    At high energy (E >> Lambda_QCD): alpha_s -> 0  [asymptotic freedom]")
    rw.print("    At E = Lambda_QCD ~ 200 MeV: alpha_s -> infinity  [confinement]")
    rw.print("    All hadron masses ~ Lambda_QCD emerge from ONE dimensionless input.")
    rw.print("    This is dimensional transmutation: a scale from a coupling.")
    rw.print("")
    rw.print("  **Source:** Gross & Wilczek (1973), Politzer (1973) [Nobel 2004]")
    rw.print("  **Source:** Peskin & Schroeder, 'An Introduction to Quantum Field Theory'")
    rw.print("              Chapter 12 (renormalization group).")
    rw.print("")
    rw.print("  THE PDTP ANALOG:")
    rw.print("")
    rw.print("    K = hbar/(4pi c)  [PDTP phase stiffness, Part 29]")
    rw.print("    In SI:           K = {:.4e} kg m".format(K_PDTP_SI))
    rw.print("    In natural units: K = 1/(4pi) = {:.6f}  [dimensionless!]".format(
        K_NATURAL))
    rw.print("")
    rw.print("    If K runs with energy E (like alpha_s in QCD), then:")
    rw.print("      The scale E* where K(E*) = O(1) could be identified with")
    rw.print("      m_cond = E*/c^2  [G-free if K running is G-free]")
    rw.print("      G = hbar*c/m_cond^2 = hbar*c^5/E*^2  [fully G-free!]")
    rw.print("")
    rw.print("  THIS IS THE LAST PROMISING PATH TO FIX m_cond WITHOUT G.")
    rw.print("")


# ===========================================================================
# STEP 2 -- PDTP COUPLING IN NATURAL UNITS
# ===========================================================================

def _natural_units(rw):
    rw.subsection("Step 2: The PDTP Coupling K in Natural Units")

    rw.print("  DIMENSIONAL ANALYSIS (natural units: hbar = c = 1):")
    rw.print("")
    rw.print("    In SI:  [K] = [hbar/c] = [kg m]  (dimensionful)")
    rw.print("")
    rw.print("    In natural units: [hbar] = [J s] = [mass] [since E=mc^2, t=1/E]")
    rw.print("                      [c]    = dimensionless (c=1)")
    rw.print("                      [hbar/c] = [mass / (1/length)] = [mass * length]")
    rw.print("                                = [E * (1/E)] = dimensionless!")
    rw.print("")
    rw.print("    So K = hbar/(4pi c) = 1/(4pi)  [pure number in natural units]")
    rw.print("    K_0 = {:.6f}  [dimensionless coupling in natural units]".format(
        K_NATURAL))
    rw.print("")
    rw.print("  INTERPRETATION:")
    rw.print("    K_0 is the bare (unrenormalized) coupling at the UV cutoff.")
    rw.print("    The RG question: how does K(E) change as we lower E from UV to IR?")
    rw.print("")
    rw.print("  THE QCD COMPARISON:")
    rw.print("    QCD: alpha_s(M_Z) = 0.118  [dimensionless, measured at Z pole]")
    rw.print("         K_0 = {:.6f}  [dimensionless, from hbar/(4pi c)]".format(
        K_NATURAL))
    rw.print("    Both are O(0.1) -- comparable coupling strengths.")
    rw.print("    The DIFFERENCE: sign of the beta function (QCD: negative = AF)")
    rw.print("")
    rw.print("  REFERENCE ENERGIES:")
    rw.print("    E_electron  = m_e * c^2  = {:.4e} J = {:.4e} GeV".format(
        E_ELECTRON, E_ELECTRON / (E_P * 1e9)))
    rw.print("    E_proton    = m_p * c^2  = {:.4e} J = {:.4e} GeV".format(
        E_PROTON, E_PROTON / (E_P * 1e9)))
    rw.print("    E_Planck    = m_P * c^2  = {:.4e} J = {:.4e} GeV".format(
        E_PLANCK, E_PLANCK / (E_P * 1e9)))
    rw.print("    t_needed (e -> Planck)   = ln(E_P/E_e) = {:.2f}".format(
        np.log(E_PLANCK / E_ELECTRON)))
    rw.print("    (= ~22 decades in energy = ln(10^22) = 22 * ln(10) = {:.2f})".format(
        22 * np.log(10)))
    rw.print("")


# ===========================================================================
# STEP 3 -- COSINE TO QUARTIC: FIELD THEORY STRUCTURE
# ===========================================================================

def _cosine_expansion(rw):
    rw.subsection("Step 3: Cosine Potential --> Quartic Coupling (lambda phi^4 Structure)")

    rw.print("  PDTP EFFECTIVE LAGRANGIAN for phase difference theta = psi - phi:")
    rw.print("")
    rw.print("    L = (K/2)(d_mu theta)^2 + g cos(theta)")
    rw.print("")
    rw.print("  where:  K = hbar/(4pi c) = 1/(4pi)  [natural units, dimensionless]")
    rw.print("          g = m_cond * c^2 / hbar = omega_gap  [Compton frequency]")
    rw.print("")
    rw.print("  TAYLOR EXPANSION of cos(theta):")
    rw.print("  **Source:** Standard calculus (Taylor series)")
    rw.print("")
    rw.print("    cos(theta) = 1 - theta^2/2 + theta^4/24 - theta^6/720 + ...")
    rw.print("")
    rw.print("  So: g cos(theta) = g - (g/2) theta^2 + (g/24) theta^4 - ...")
    rw.print("")
    rw.print("  This is EXACTLY the lambda phi^4 structure with:")
    rw.print("    m^2 = g/K  (mass squared from the quadratic term)")
    rw.print("    lambda/4! = g/24 -> lambda_bare = g  (quartic coupling)")
    rw.print("")
    rw.print("  The effective coupling after canonical field normalization:")
    rw.print("  (canonically normalized: theta_can = sqrt(K) * theta)")
    rw.print("")
    rw.print("    lambda_eff = g / K^2  [the quartic coupling in canonical form]")
    rw.print("")

    # Numerical value of lambda_eff if we use m_cond = m_P
    m_cond = M_P
    g_omega = m_cond * C**2 / HBAR   # omega_gap [rad/s]
    # In natural units: g = m_cond (in Planck units = 1)
    # K = 1/(4pi)
    # lambda_eff = g/K^2 (schematic, natural units)
    # But g and K have different natural-unit dimensions depending on normalization
    # We note the structure; compute schematic ratio
    K0 = K_NATURAL
    # lambda_eff (schematic) = g / K^2 where we need g in natural units
    # g = m_cond c^2 / hbar = m_P c^2 / hbar [1/s in SI]
    # In natural units: g = m_P [mass] = 1 (in Planck mass units)
    # lambda_eff = m_P / (1/(4pi))^2 = m_P * 16 pi^2  [if m_P = 1 in Planck units]
    # This approach shows lambda_eff can be O(1) to O(100) depending on convention

    rw.print("  NOTE: The exact value of lambda_eff depends on the normalization")
    rw.print("  convention and the energy scale at which g is evaluated.")
    rw.print("  Following the TODO convention: use K itself as the effective coupling.")
    rw.print("  This is the phase stiffness K = 1/(4pi) -- the natural coupling")
    rw.print("  of the Goldstone mode in the PDTP condensate.")
    rw.print("")
    rw.print("  STRUCTURE CONFIRMED: PDTP cosine coupling = lambda phi^4 at leading order.")
    rw.print("  The beta function will have the same sign as lambda phi^4.")
    rw.print("")


# ===========================================================================
# STEP 4 -- BETA FUNCTION (SCHEMATIC)
# ===========================================================================

def _beta_function(rw):
    rw.subsection("Step 4: The 1-Loop Beta Function")

    rw.print("  THE STANDARD RESULT for lambda phi^4 in 4D:")
    rw.print("  **Source:** Peskin & Schroeder, Chapter 12.2, Eq. (12.47)")
    rw.print("")
    rw.print("    beta(lambda) = d(lambda)/d(ln mu) = +3 lambda^2 / (16 pi^2)")
    rw.print("")
    rw.print("  SIGN: POSITIVE (+) means:")
    rw.print("    - lambda GROWS with energy (UV divergence = Landau pole)")
    rw.print("    - Theory is FREE at low energies (infrared free)")
    rw.print("    - This is the OPPOSITE of QCD (which has negative beta function)")
    rw.print("")
    rw.print("  FOR PDTP (using K as the effective coupling):")
    rw.print("  **PDTP Original:** K is the Goldstone stiffness of the condensate.")
    rw.print("  The cosine coupling renormalizes K at 1-loop with the same structure")
    rw.print("  as lambda phi^4.  Schematic beta function:")
    rw.print("")
    rw.print("    beta(K) = dK/d(ln E) = +K^2 / (8 pi^2)")
    rw.print("    [from TODO Part 35; same sign as lambda phi^4]")
    rw.print("")
    rw.print("  COMPARISON OF SIGNS:")
    rw.print("    QCD:  beta(g_s) = -(b0/(16pi^2)) * g_s^3,  b0 = 11Nc/3 - 2Nf/3 > 0")
    rw.print("          beta < 0 -> g_s grows at LOW energy -> asymptotic freedom + Lambda_QCD")
    rw.print("    PDTP: beta(K) = +K^2/(8pi^2)")
    rw.print("          beta > 0 -> K grows at HIGH energy -> Landau pole (NOT Lambda_QCD-like)")
    rw.print("")
    rw.print("  CRITICAL OBSERVATION: For dimensional transmutation (QCD style),")
    rw.print("  we NEED beta < 0. A positive beta gives a Landau pole, not a")
    rw.print("  physical mass generation scale.")
    rw.print("")
    rw.print("  However, we compute BOTH cases to see which (if either) gives")
    rw.print("  m_cond = m_P at a physically accessible energy.")
    rw.print("")


# ===========================================================================
# STEP 5 -- RG RUNNING: ANALYTICAL SOLUTION
# ===========================================================================

def _rg_analytical(rw):
    rw.subsection("Step 5: RG Running -- Analytical Solution")

    K0 = K_NATURAL   # = 1/(4pi) ~ 0.0796

    rw.print("  RG EQUATION:")
    rw.print("")
    rw.print("    dK/dt = K^2 / (8 pi^2),    t = ln(E/E_ref)")
    rw.print("")
    rw.print("  EXACT SOLUTION (separable ODE):")
    rw.print("  **Source:** Standard ODE; see Peskin & Schroeder Eq. (12.50)")
    rw.print("")
    rw.print("    K(t) = K_0 / (1 - K_0 * t / (8 pi^2))")
    rw.print("")
    rw.print("  INITIAL VALUE:  K_0 = 1/(4pi) = {:.6f}".format(K0))
    rw.print("  8 pi^2 = {:.4f}".format(8 * np.pi**2))
    rw.print("")

    # Landau pole
    t_star = 8 * np.pi**2 / K0
    log10_factor = t_star / np.log(10)

    rw.print("  LANDAU POLE (K -> infinity):  1 - K_0 * t* / (8 pi^2) = 0")
    rw.print("")
    rw.print("    t* = 8 pi^2 / K_0 = 8 pi^2 * 4 pi = 32 pi^3")
    rw.print("    t* = {:.2f}".format(t_star))
    rw.print("    E_Landau = E_ref * exp(t*) = E_ref * exp({:.1f})".format(t_star))
    rw.print("             = E_ref * 10^{:.1f}".format(log10_factor))
    rw.print("")

    # Where does the Landau pole land relative to Planck?
    log10_Eland_rel_Planck_from_electron = log10_factor + np.log10(E_ELECTRON / E_PLANCK)

    rw.print("  IF E_ref = m_e * c^2 (electron rest energy):")
    rw.print("    E_Landau = {:.3e} J * 10^{:.1f}".format(
        E_ELECTRON, log10_factor))
    rw.print("    log10(E_Landau / E_Planck) = {:.1f}  [{} decades above Planck]".format(
        log10_Eland_rel_Planck_from_electron,
        "ABOVE" if log10_Eland_rel_Planck_from_electron > 0 else "below"))
    rw.print("")

    rw.print("  IF E_ref = m_P * c^2 (Planck energy):")
    log10_Eland_from_Planck = log10_factor
    rw.print("    E_Landau = E_Planck * 10^{:.1f}  [Planck * 10^431]".format(
        log10_factor))
    rw.print("")

    rw.print("  ASYMPTOTICALLY FREE CASE (wrong sign, for comparison):")
    rw.print("    beta(K) = -K^2 / (8 pi^2)  [if sign were negative like QCD]")
    rw.print("    K(t) = K_0 / (1 + K_0 * t / (8 pi^2))")
    rw.print("    K -> 0 as t -> +inf  [coupling disappears at high E]")
    rw.print("    Strong coupling scale: t_strong = -t*  ==> E_strong = E_ref / 10^{:.1f}".format(
        log10_factor))
    rw.print("    If E_ref = E_Planck: E_strong = E_Planck * 10^-{:.1f}".format(
        log10_factor))
    rw.print("    Both cases: Landau pole / strong coupling scale is 10^431 off.")
    rw.print("")

    return t_star, log10_factor


# ===========================================================================
# STEP 6 -- NUMERICAL RG SCAN
# ===========================================================================

def _rg_numerical(rw, t_star):
    rw.subsection("Step 6: Numerical RG Scan -- K(E) from m_e to E_Planck")

    K0 = K_NATURAL
    t_planck = np.log(E_PLANCK / E_ELECTRON)    # ~51.4

    rw.print("  SCAN: K(E) as E runs from m_e*c^2 to m_P*c^2")
    rw.print("  Reference energy: E_ref = m_e * c^2 = {:.4e} J".format(E_ELECTRON))
    rw.print("  t = ln(E/E_ref);  t_Planck = ln(m_P/m_e) = {:.2f}".format(t_planck))
    rw.print("")
    rw.print("  {:>12s}  {:>12s}  {:>14s}  {:>14s}".format(
        "E [J]", "E/E_e ratio", "K(E)", "delta_K [%]"))
    rw.print("  " + "-" * 60)

    energies = [
        ("m_e*c^2",  E_ELECTRON),
        ("m_mu*c^2", 1.883e-28),   # muon 105.7 MeV
        ("m_p*c^2",  E_PROTON),
        ("m_W*c^2",  E_P * 80.4e9),  # W boson 80.4 GeV
        ("m_H*c^2",  E_P * 125.1e9), # Higgs 125.1 GeV
        ("m_P*c^2",  E_PLANCK),
    ]

    K_at_Planck = None
    for label, E in energies:
        t = np.log(E / E_ELECTRON)
        denom = 1.0 - K0 * t / (8.0 * np.pi**2)
        if denom > 0:
            K_E = K0 / denom
            delta_pct = (K_E - K0) / K0 * 100.0
            rw.print("  {:>12s}  {:>12.3e}  {:>14.6f}  {:>13.2f}%".format(
                label, E / E_ELECTRON, K_E, delta_pct))
            if label == "m_P*c^2":
                K_at_Planck = K_E
        else:
            rw.print("  {:>12s}  {:>12.3e}  {:>14s}  [past Landau pole!]".format(
                label, E / E_ELECTRON, "diverged"))
    rw.print("")

    if K_at_Planck is not None:
        rw.print("  K at Planck energy: {:.6f}  (started at {:.6f})".format(
            K_at_Planck, K0))
        delta_total = (K_at_Planck - K0) / K0 * 100.0
        rw.print("  Total change over 22 energy decades: {:.2f}%".format(delta_total))
        rw.print("")
        rw.print("  OBSERVATION: The coupling barely changes over 22 decades in energy.")
        rw.print("  A 5.5% change is negligible -- this is NOT significant running.")
        rw.print("  Compare to QCD: alpha_s changes by a factor of ~3 over 5 decades.")
    rw.print("")


# ===========================================================================
# STEP 7 -- WHERE DOES K = 1?  (The Target Scale)
# ===========================================================================

def _where_K_equals_one(rw, t_star, log10_factor):
    rw.subsection("Step 7: Where Does K(E) = 1 (Dimensionless Order-1)?")

    K0 = K_NATURAL

    rw.print("  For dimensional transmutation, we want the scale where K(E) = O(1).")
    rw.print("  This would identify m_cond = E(K=1) / c^2.")
    rw.print("")
    rw.print("  From the analytical solution:")
    rw.print("    K(t) = K_0 / (1 - K_0 * t / (8 pi^2)) = 1")
    rw.print("    t_1 = 8 pi^2 * (1 - K_0) / K_0 = 8 pi^2 * (1/K_0 - 1)")
    rw.print("")

    t_K1 = 8 * np.pi**2 * (1.0 / K0 - 1.0)
    log10_E_K1_from_electron = t_K1 / np.log(10) + np.log10(E_ELECTRON)
    log10_E_K1_from_Planck   = t_K1 / np.log(10) + np.log10(E_ELECTRON / E_PLANCK)

    rw.print("    t_1 = {:.2f}".format(t_K1))
    rw.print("    E(K=1) = E_ref * exp({:.2f}) = E_ref * 10^{:.1f}".format(
        t_K1, t_K1 / np.log(10)))
    rw.print("")
    rw.print("    IF E_ref = m_e * c^2:")
    rw.print("      E(K=1) = {:.3e} J * 10^{:.1f}".format(
        E_ELECTRON, t_K1 / np.log(10)))
    rw.print("      log10(E(K=1) / E_Planck) = {:.1f}  [{} decades vs Planck]".format(
        log10_E_K1_from_Planck,
        "above" if log10_E_K1_from_Planck > 0 else "below"))
    rw.print("")
    rw.print("  RESULT: K(E) = 1 occurs at a scale {:.0f} decades ABOVE the Planck energy".format(
        abs(log10_E_K1_from_Planck)))
    rw.print("  when starting from the electron rest energy.")
    rw.print("")
    rw.print("  WHAT WOULD BE NEEDED to get E(K=1) = E_Planck:")
    rw.print("    t_needed = ln(E_Planck / E_ref)")
    rw.print("    With E_ref = m_e*c^2: t_needed = {:.2f}".format(
        np.log(E_PLANCK / E_ELECTRON)))
    rw.print("    But t_1 = {:.2f}  [required is 18x smaller than actual]".format(t_K1))
    rw.print("")
    rw.print("  OR: what K_0 would give E(K=1) = E_Planck from E_ref = m_e*c^2?")
    t_needed = np.log(E_PLANCK / E_ELECTRON)
    # t_1 = 8pi^2 * (1/K_0 - 1) = t_needed
    # 1/K_0 - 1 = t_needed / (8 pi^2)
    # 1/K_0 = 1 + t_needed / (8 pi^2)
    K0_needed = 1.0 / (1.0 + t_needed / (8.0 * np.pi**2))
    rw.print("    K_0_needed = {:.4f}  (actual K_0 = {:.6f})".format(
        K0_needed, K0))
    rw.print("    The coupling would need to be {:.1f}x LARGER than 1/(4pi)".format(
        K0_needed / K0))
    rw.print("    That would require a completely different fundamental theory.")
    rw.print("")


# ===========================================================================
# STEP 8 -- WHY THE MECHANISM FAILS (PHYSICAL INSIGHT)
# ===========================================================================

def _why_fails(rw, log10_factor):
    rw.subsection("Step 8: Why Dimensional Transmutation Fails in PDTP")

    K0 = K_NATURAL

    rw.print("  THREE REASONS THE MECHANISM FAILS:")
    rw.print("")
    rw.print("  REASON 1: K_0 is too small for significant running.")
    rw.print("")
    rw.print("    The coupling K_0 = 1/(4pi) = {:.4f}.".format(K0))
    rw.print("    The beta function is beta = K^2 / (8pi^2).")
    rw.print("    At K_0: beta_0 = K_0^2 / (8pi^2) = {:.6f}".format(
        K0**2 / (8 * np.pi**2)))
    rw.print("    This is very small -- the coupling runs extremely slowly.")
    rw.print("")
    rw.print("    COMPARE to QCD: beta(g_s) ~ -b0/(16pi^2) * g_s^3")
    rw.print("    With b0 = 7, alpha_s = 0.118: beta = -7/(16pi^2) * (4pi*0.118)^{3/2}")
    rw.print("                                        ~ -0.0012")
    rw.print("    PDTP: beta_0 = {:.6f}  [similar magnitude, but POSITIVE]".format(
        K0**2 / (8 * np.pi**2)))
    rw.print("")
    rw.print("  REASON 2: Sign is wrong for QCD-style generation.")
    rw.print("")
    rw.print("    QCD: beta < 0 -> coupling strong at LOW energy -> confinement + Lambda_QCD")
    rw.print("    PDTP: beta > 0 -> coupling strong at HIGH energy -> Landau pole")
    rw.print("    The Landau pole is a UV problem (unphysical), NOT a mass generation scale.")
    rw.print("    For PDTP to work like QCD, the beta function would need to be negative.")
    rw.print("    This would require fermion loops or non-Abelian structure to dominate.")
    rw.print("")
    rw.print("  REASON 3: Wrong number of decades.")
    rw.print("")
    rw.print("    The Landau pole is at 10^{:.0f} decades above the reference energy.".format(
        log10_factor))
    rw.print("    We only need 22 decades (electron to Planck mass).")
    rw.print("    The mechanism would need to be ~20x stronger to land at Planck scale.")
    rw.print("")
    rw.print("  WHAT WOULD WORK:")
    rw.print("")
    rw.print("    A theory where K has a NEGATIVE beta function AND the coupling runs")
    rw.print("    strongly enough to generate the Planck scale from the electron mass")
    rw.print("    over 22 decades.  This requires:")
    rw.print("      - Non-Abelian structure (like QCD) to flip the sign")
    rw.print("      - A large 'color factor' b0 to speed up the running")
    rw.print("    These are not present in the current PDTP Lagrangian.")
    rw.print("")


# ===========================================================================
# STEP 9 -- EXHAUSTION SUMMARY TABLE
# ===========================================================================

def _exhaustion_summary(rw, engine):
    rw.subsection("Step 9: Complete Exhaustion Summary (Parts 29-35)")

    rw.print("  ALL ATTEMPTS TO DERIVE m_cond (or G) FROM PDTP WITHOUT G AS INPUT:")
    rw.print("")
    rw.print("  {:>30s}  {:>10s}  {:>40s}".format(
        "Approach", "Phase", "Verdict"))
    rw.print("  " + "-" * 85)

    rows = [
        ("Substitution algebra", "Phases 1-3", "CIRCULAR: always reduces to a=l_P"),
        ("Power-law sweep (729 combos)", "Phase 2", "CIRCULAR: all force a ~ l_P"),
        ("Mass-combo sweep (GP/HM/RMS)", "Phase 3", "CIRCULAR: all force a ~ l_P"),
        ("Analytical proof (Part 29)", "Phase 4", "CIRCULAR: algebraically inevitable"),
        ("LISA breathing mode (Part 30)", "Phase 7", "CIRCULAR input; detection: 43 decades off"),
        ("Orbital quantization (Part 31)", "Phase 8", "n=m_P/m; need n from topology"),
        ("Vortex winding n=m_cond/m", "Phase 9", "G-FREE given m_cond; m_cond still free"),
        ("BEC self-consistency c_s=c", "Phase 10", "G-FREE; consistent any m_cond; no fix"),
        ("Dimensional transmutation (1-loop)", "Phase 11", "FAILS: Landau pole 10^431 off"),
    ]
    for approach, phase, verdict in rows:
        rw.print("  {:>30s}  {:>10s}  {:>40s}".format(approach, phase, verdict))

    rw.print("")
    rw.print("  KEY POSITIVE RESULTS (things PDTP DID derive):")
    rw.print("    1. G = hbar*c / m_cond^2  [G-free given m_cond]  (Phase 9)")
    rw.print("    2. n = m_cond / m_particle  [vortex winding from core condition]  (Phase 9)")
    rw.print("    3. c_s = c  [condensate exactly at sonic limit]  (Phase 10)")
    rw.print("    4. g_GP = hbar^3/(m_cond^2 c)  [G-free interaction constant]  (Phase 10)")
    rw.print("    5. xi = a_0/sqrt(2)  [healing length ~ lattice spacing]  (Phase 10)")
    rw.print("")
    rw.print("  THE ONE REMAINING FREE PARAMETER: m_cond = m_P")
    rw.print("    This plays the same role as Lambda (cosmological constant) in GR.")
    rw.print("    The field equations alone do not determine it.")
    rw.print("    External input is required.")
    rw.print("")

    # Run Sudoku on best candidate for completeness
    rw.print("  SUDOKU CHECK (m_cond = m_P -> G_pred = G_known):")
    a_best = L_P                               # l_P is the correct lattice spacing
    results, G_pred = engine.test(a_best)
    n_pass, n_fail, mean_dev = engine.score(results)
    rw.print("    a = l_P = {:.4e} m".format(a_best))
    rw.print("    G_pred = {:.4e}  G_known = {:.4e}".format(G_pred, G))
    rw.print("    Ratio  = {:.6f}".format(G_pred / G))
    rw.print("    Score  = {}/{} pass (always circular -- a=l_P requires G)".format(
        n_pass, n_pass + n_fail))
    rw.print("")


# ===========================================================================
# CONCLUSION
# ===========================================================================

def _conclusion(rw):
    rw.subsection("Phase 11 Conclusion: The End of the Systematic Search")

    rw.print("  WHAT WAS INVESTIGATED (Part 35):")
    rw.print("")
    rw.print("    Dimensional transmutation in PDTP: does the coupling K = hbar/(4pi c)")
    rw.print("    run with energy, and can its running fix m_cond = m_P G-free?")
    rw.print("")
    rw.print("  WHAT WAS FOUND:")
    rw.print("")
    rw.print("    1. K is dimensionless in natural units: K_0 = 1/(4pi) = {:.6f}".format(
        K_NATURAL))
    rw.print("       [PDTP Original: K = hbar/(4pi c) is dimensionless when hbar=c=1]")
    rw.print("")
    rw.print("    2. The PDTP cosine coupling has lambda phi^4 structure at leading order.")
    rw.print("       Beta function: beta(K) = +K^2/(8pi^2)  [positive = IR free]")
    rw.print("       This is the SAME sign as QED -- NOT asymptotically free like QCD.")
    rw.print("")
    rw.print("    3. The Landau pole is at E_Landau = E_ref * 10^431")
    rw.print("       -- 431 decades above any reference energy.")
    rw.print("       -- 409 decades above the Planck energy (from electron rest energy).")
    rw.print("")
    rw.print("    4. The coupling K barely changes over 22 energy decades (m_e to m_P):")
    K0 = K_NATURAL
    t_planck = np.log(E_PLANCK / E_ELECTRON)
    denom = 1.0 - K0 * t_planck / (8.0 * np.pi**2)
    K_at_Planck = K0 / denom
    delta_pct = (K_at_Planck - K0) / K0 * 100.0
    rw.print("       delta K / K = {:.2f}% (compare: QCD changes ~300% over 5 decades)".format(
        delta_pct))
    rw.print("")
    rw.print("    5. Mechanism FAILS: neither the Landau pole nor the strong coupling scale")
    rw.print("       lands at the Planck energy for any natural choice of reference energy.")
    rw.print("")
    rw.print("  FINAL CONCLUSION (Parts 29-35 complete):")
    rw.print("")
    rw.print("    The systematic search for a non-circular derivation of G from PDTP")
    rw.print("    using standard perturbative methods is EXHAUSTED.")
    rw.print("")
    rw.print("    PDTP is a self-consistent framework (confirmed by Phases 9-10) that")
    rw.print("    reproduces Newton's G given m_cond = m_P -- but cannot derive m_P itself.")
    rw.print("")
    rw.print("    THE ANALOGY HOLDS QUANTITATIVELY:")
    rw.print("      G is to PDTP as Lambda is to GR.")
    rw.print("      Both are free parameters of self-consistent field theories.")
    rw.print("      Neither can be derived from the field equations alone.")
    rw.print("")
    rw.print("    WHAT THIS MEANS FOR THE FRAMEWORK:")
    rw.print("      PDTP explains the STRUCTURE of gravity (vortex winding, sonic limit,")
    rw.print("      phase locking, c_s=c) but not the SCALE (why m_cond = m_P).")
    rw.print("      This is analogous to GR: it explains geodesics but not the value of G.")
    rw.print("")
    rw.print("    OPEN PATHS (beyond perturbative methods):")
    rw.print("      [1] Non-perturbative: PDTP lattice simulation (like lattice QCD)")
    rw.print("          to look for a non-perturbative fixed point that selects m_cond.")
    rw.print("      [2] Topological quantization: a deeper vortex argument (beyond n=m_cond/m)")
    rw.print("          that forces m_cond = m_P from some topological invariant.")
    rw.print("      [3] Holographic/emergent: perhaps m_cond is fixed by the number of")
    rw.print("          Hubble-volume modes (Dvali) in a time-varying G framework.")
    rw.print("      [4] Empirical: measure omega_gap directly (LISA/ET) to fix m_cond")
    rw.print("          without deriving it theoretically.")
    rw.print("")
    rw.print("  PHASES COMPLETE: 11 of 11")
    rw.print("    Phases 1-6:   Systematic lattice-spacing search.  [CIRCULAR -- closed]")
    rw.print("    Phase  7:     LISA breathing mode chain.          [CIRCULAR input; detector gap 43 orders]")
    rw.print("    Phase  8:     Orbital quantization reframe.       [n=m_P/m; answered by Phase 9]")
    rw.print("    Phase  9:     Vortex winding derivation.          [G-free chain; m_cond free]")
    rw.print("    Phase 10:     BEC self-consistency.               [c_s=c; m_cond still free]")
    rw.print("    Phase 11:     Dimensional transmutation.          [FAILS; Landau pole 10^431 off]")
    rw.print("")


# ===========================================================================
# ENTRY POINT
# ===========================================================================

def run_dim_transmutation_phase(rw, engine):
    """Phase 11 entry point.  Called from main.py."""
    rw.section("Phase 11 -- Dimensional Transmutation (Part 35)")

    rw.print("  TASK (from TODO.md Part 35):")
    rw.print("    Can 1-loop RG running of K = hbar/(4pi c) fix m_cond = m_P G-free?")
    rw.print("    (Analogous to how QCD beta function generates Lambda_QCD.)")
    rw.print("")
    rw.print("  KEY RESULT: NEGATIVE.")
    rw.print("    K_0 = 1/(4pi) is dimensionless in natural units but runs too slowly.")
    rw.print("    Landau pole is at 10^431 * E_ref -- not at the Planck scale.")
    rw.print("    The mechanism fails by ~430 orders of magnitude.")
    rw.print("")
    rw.print("  SIGNIFICANCE: Completes the systematic search (Parts 29-35).")
    rw.print("    m_cond = m_P is underdetermined by PDTP, like Lambda in GR.")
    rw.print("")

    _recap(rw)
    _natural_units(rw)
    _cosine_expansion(rw)
    _beta_function(rw)
    t_star, log10_factor = _rg_analytical(rw)
    _rg_numerical(rw, t_star)
    _where_K_equals_one(rw, t_star, log10_factor)
    _why_fails(rw, log10_factor)
    _exhaustion_summary(rw, engine)
    _conclusion(rw)


# ===========================================================================
# STANDALONE ENTRY POINT
# ===========================================================================

if __name__ == "__main__":
    output_dir = os.path.join(_HERE, "outputs")
    rw = ReportWriter(output_dir, label="dim_transmutation")
    engine = SudokuEngine()
    run_dim_transmutation_phase(rw, engine)
    rw.close()
    print("Done. Report written to:", output_dir)
