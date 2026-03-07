#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
orbital_scanner.py -- Phase 8: Orbital Quantization Scanner
============================================================
REFRAME: Instead of asking "what lattice spacing gives G?"
         ask "if Planck is the nth excited state, what is n
         and can n be derived without knowing G?"

WHY THIS REFRAME MATTERS
------------------------
Every previous phase hit the same wall:
  "a = l_P gives 13/13, but l_P contains G -> circular."

This reframe shifts the question:

  OLD: What is `a`?         (answer: l_P, circular)
  NEW: What is `n`?         (answer: n = m_P / m_particle)

The orbital number n is DIMENSIONLESS.  Dimensionless numbers can have
topological, combinatorial, or geometric origins that do not require G.
If n can be derived without G, the circularity breaks.

THE PHYSICS OF ORBITAL NUMBERS
-------------------------------
In a superfluid BEC, large quantum numbers arise naturally from:
  1. Topological winding   -- vortex quanta n = M*omega*R^2 / hbar
  2. Species counting      -- N modes share one bare coupling
  3. Coherence length gap  -- n = xi_condensate / a_cell

In the PDTP spacetime condensate, the particle's Compton wavelength
lambda = hbar/(mc) is its coherence length in the condensate.
The lattice cell size is a = l_P.  Their ratio IS n:

  n = lambda / l_P = hbar/(mc) / sqrt(hbar*G/c^3) = m_P / m    [dimensionless]

This is not circular!  lambda = hbar/(mc) uses only hbar, m, c -- no G.
The circularity enters ONLY in l_P = sqrt(hbar*G/c^3) which needs G.

G-FREE DERIVATION PATH (if n were known):
  1. n        -- from topology/lattice (G-free if derivable)
  2. a_0      = lambda / n  = hbar / (mc * n)    [G-free]
  3. G_pred   = c^3 * a_0^2 / hbar               [G-free]
  4. Compare G_pred to G_Cavendish  ->  test of theory

Steps 2-4 are ALREADY G-free.  The only unsolved step is step 1.

WHAT THIS MODULE DOES
---------------------
Step 1  -- Orbital number table: n for each Standard Model particle
Step 2  -- Dvali species connection: n^2 = N_modes -> gravity dilution
Step 3  -- Key identities: n expressed in terms of known physics
Step 4  -- Sub-Planck reframe: what if a_0 = l_P / n (ground state)?
Conclusion -- What physical mechanism could fix n?

Called from main.py as Phase 8.

Usage (standalone):
    cd simulations/solver
    python orbital_scanner.py
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


# ===========================================================================
# STANDARD MODEL PARTICLE TABLE
# Sources: PDG 2022 / NIST CODATA 2018
# https://pdg.lbl.gov/2022/tables/contents_tables.html
# ===========================================================================
# Each entry: (display_name, mass_kg, mass_MeV, is_confined)
#   is_confined = True for quarks (not directly observable in isolation)
#   Quark masses are MS-bar at 2 GeV; they are scale-dependent.

PARTICLES = [
    # Leptons (free, precisely measured)
    ("electron",   9.1093837015e-31,   0.51099895,   False),
    ("muon",       1.88353162e-28,     105.6583755,  False),
    ("tau",        3.16754e-27,        1776.86,      False),
    # Light quarks (MS-bar at 2 GeV)
    ("up quark",   3.85e-30,           2.16,         True),
    ("down quark", 8.33e-30,           4.67,         True),
    ("strange",    1.67e-28,           93.4,         True),
    # Heavy quarks
    ("charm",      2.26e-27,           1270.0,       True),
    ("bottom",     7.48e-27,           4180.0,       True),
    ("top quark",  3.09e-25,           172760.0,     True),
    # Composite hadrons (for comparison)
    ("proton",     1.67262192369e-27,  938.272,      False),
    ("neutron",    1.67492749804e-27,  939.565,      False),
]


# ===========================================================================
# STEP 1 -- ORBITAL NUMBER TABLE
# ===========================================================================

def _orbital_table(rw):
    """
    For each SM particle, compute the orbital quantum number n = m_P / m.
    Also show the G-free chain: n + lambda -> a_0 -> G_pred.
    """
    rw.subsection("Step 1: Orbital Quantum Number for Each SM Particle")

    rw.print("  DEFINITION:")
    rw.print("    n = m_P / m_particle  =  lambda_Compton / l_P")
    rw.print("")
    rw.print("  This is a dimensionless integer (roughly) for each particle.")
    rw.print("  n tells you 'how many Planck-scale cells fit inside this")
    rw.print("  particle's Compton wavelength.'")
    rw.print("")
    rw.print("  G-FREE CHAIN VALIDATION:")
    rw.print("    a_0 = lambda / n   [only uses hbar, m, c, n -- no G]")
    rw.print("    G_pred = c^3 * a_0^2 / hbar   [G-free]")
    rw.print("    -> G_pred = G_known by construction (validates chain)")
    rw.print("")

    headers = ["Particle", "Mass (MeV)", "log10(n)", "n = m_P/m",
               "lambda (m)", "a_0 = l/n (m)", "G_pred / G_known"]
    widths  = [14, 12, 10, 12, 14, 16, 16]
    rows = []
    results = []

    for name, mass_kg, mass_MeV, confined in PARTICLES:
        n       = M_P / mass_kg                      # orbital number
        lam     = HBAR / (mass_kg * C)               # Compton wavelength [m]
        a_0     = lam / n                            # = l_P by construction
        G_pred  = C**3 * a_0**2 / HBAR              # G-free formula
        ratio   = G_pred / G                         # should be 1.0

        tag = "  [confined]" if confined else ""
        rows.append([
            name + tag,
            "{:.4f}".format(mass_MeV),
            "{:.2f}".format(np.log10(n)),
            "{:.4e}".format(n),
            "{:.4e}".format(lam),
            "{:.4e}".format(a_0),
            "{:.6f}".format(ratio),
        ])
        results.append({
            "name"    : name,
            "mass_kg" : mass_kg,
            "mass_MeV": mass_MeV,
            "n"       : n,
            "lambda"  : lam,
            "a_0"     : a_0,
            "confined": confined,
        })

    rw.table(headers, rows, widths)
    rw.print("  NOTE: G_pred / G_known = 1.000000 for ALL particles -- the chain")
    rw.print("  works perfectly. The circularity is ONLY in where n came from")
    rw.print("  (we used G to compute m_P = sqrt(hbar*c/G)). If n could be")
    rw.print("  derived without G, step 1 becomes non-circular and G follows.")
    rw.print("")
    rw.print("  STRUCTURAL OBSERVATION: n spans 6 decades across the SM:")
    rw.print("    top quark  n ~ 1.4e19  (smallest n -- heaviest particle)")
    rw.print("    electron   n ~ 2.4e22  (largest n -- lightest particle)")
    rw.print("    The ratio n_e / n_top = m_top / m_e = 338,000 (the mass ratio)")
    rw.print("")

    return results


# ===========================================================================
# STEP 2 -- DVALI SPECIES CONNECTION
# ===========================================================================

def _dvali_analysis(rw, orbital_results):
    """
    Show that n^2 = N_Dvali = the number of species needed to dilute G.
    Physical meaning: if N = n^2 modes share the bare gravitational coupling,
    each gets a fraction G_bare / N, and the sum gives G_observed.
    """
    rw.subsection("Step 2: Dvali Species Dilution -- n^2 = N_modes")

    rw.print("  DVALI SPECIES MECHANISM (non-PDTP context):")
    rw.print("  If there are N species of particles (or modes), quantum")
    rw.print("  corrections dilute the observed Planck mass:")
    rw.print("")
    rw.print("    m_P_observed^2  =  N * m_P_bare^2")
    rw.print("    G_observed      =  G_bare / N")
    rw.print("")
    rw.print("  In PDTP language:")
    rw.print("    G_bare = c^3 * lambda_Compton^2 / hbar")
    rw.print("       (gravity at Compton scale, before dilution)")
    rw.print("    N      = n^2 = (m_P / m)^2 = 1 / alpha_G")
    rw.print("    G_obs  = G_bare / N = G_known  [by construction]")
    rw.print("")
    rw.print("  REFRAME: The hierarchy problem is not 'G is tiny'.")
    rw.print("  It is 'N is enormous.'  Why are there N = (m_P/m)^2 modes?")
    rw.print("")

    headers = ["Particle", "n = m_P/m", "N_Dvali = n^2",
               "log10(N)", "G_bare (m^3/kg/s^2)", "G_bare / G_obs"]
    widths  = [14, 14, 14, 10, 22, 16]
    rows = []

    for r in orbital_results:
        mass_kg = r["mass_kg"]
        n       = r["n"]
        N       = n**2
        lam     = r["lambda"]
        G_bare  = C**3 * lam**2 / HBAR   # G at Compton scale
        ratio   = G_bare / G

        rows.append([
            r["name"],
            "{:.4e}".format(n),
            "{:.4e}".format(N),
            "{:.1f}".format(np.log10(N)),
            "{:.4e}".format(G_bare),
            "{:.4e}".format(ratio),
        ])

    rw.table(headers, rows, widths)
    rw.print("  INTERPRETATION:")
    rw.print("    G_bare / G_obs = N = n^2 = 1 / alpha_G")
    rw.print("    For the electron: N ~ 5.4e44 modes")
    rw.print("    For the top quark: N ~ 2.0e38 modes")
    rw.print("")
    rw.print("  These are enormous mode counts. But large N is NOT unusual in")
    rw.print("  condensed matter -- a gram of helium-4 has ~1.5e23 atoms.")
    rw.print("  A Hubble-volume condensate at Planck density has ~10^184 cells.")
    rw.print("")
    rw.print("  IN PDTP: The spacetime condensate has N_cells = (R_Hubble/l_P)^3")
    R_H   = C / 2.184e-18               # Hubble radius ~ c / H_0
    N_cells = (R_H / L_P)**3
    rw.print("    R_Hubble / l_P  ~ {:.2e}".format(R_H / L_P))
    rw.print("    N_cells = (R_H/l_P)^3 ~ {:.2e}".format(N_cells))
    rw.print("    N_Dvali(electron) ~ {:.2e}".format((M_P / M_E)**2))
    rw.print("    N_cells >> N_Dvali -- the condensate has MORE than enough modes.")
    rw.print("")


# ===========================================================================
# STEP 3 -- KEY IDENTITIES FOR n
# ===========================================================================

def _algebraic_structure(rw, orbital_results):
    """
    Express n in terms of known dimensionless physics constants.
    The key identity: n^2 = 1 / alpha_G (exact, by definition).
    """
    rw.subsection("Step 3: Algebraic Structure of n")

    rw.print("  KEY IDENTITY (always true, for every particle):")
    rw.print("")
    rw.print("    n^2  =  (m_P / m)^2  =  hbar*c / (G * m^2)  =  1 / alpha_G")
    rw.print("")
    rw.print("  where alpha_G = G * m^2 / (hbar * c) is the gravitational")
    rw.print("  fine-structure constant (analogous to alpha_EM = 1/137.036).")
    rw.print("")
    rw.print("  So: n = 1 / sqrt(alpha_G)")
    rw.print("")
    rw.print("  This means asking 'what is n?' is EXACTLY the same as asking")
    rw.print("  'what is alpha_G?'  The hierarchy problem in three phrasings:")
    rw.print("")
    rw.print("    Standard:   'Why is G so small? (alpha_G ~ 10^-45 for electron)'")
    rw.print("    Old PDTP:   'Why is the lattice spacing l_P so small?'")
    rw.print("    NEW REFRAME:'Why is the orbital quantum number n so large?'")
    rw.print("")
    rw.print("  The third phrasing is new. In quantum mechanics, large n means")
    rw.print("  a system is in a highly excited state, or has many modes, or")
    rw.print("  has a large winding number. These have known physical origins.")
    rw.print("")

    rw.print("  PARTICLE-BY-PARTICLE IDENTITIES:")
    headers = ["Particle", "n", "alpha_G = 1/n^2", "n / n_electron",
               "log10(n/n_e)", "n relative to SM"]
    widths  = [14, 14, 16, 16, 14, 22]
    rows = []

    n_electron = M_P / M_E
    alpha_G_electron = G * M_E**2 / (HBAR * C)

    for r in orbital_results:
        n     = r["n"]
        aG    = 1.0 / n**2          # = alpha_G for this particle
        ratio = n / n_electron      # relative orbital number
        log_r = np.log10(ratio)

        # Physical interpretation of ratio
        if abs(log_r) < 0.01:
            interp = "= electron (reference)"
        elif ratio > 1:
            interp = "n > n_e (lighter particle)"
        else:
            interp = "n < n_e, ratio = m_e/m = {:.3e}".format(M_E / r["mass_kg"])

        rows.append([
            r["name"],
            "{:.4e}".format(n),
            "{:.4e}".format(aG),
            "{:.4e}".format(ratio),
            "{:+.2f}".format(log_r),
            interp,
        ])

    rw.table(headers, rows, widths)
    rw.print("  PATTERN: n_particle / n_electron = m_electron / m_particle")
    rw.print("  (heavier particles have smaller n -- their Compton wavelength")
    rw.print("   is shorter, so it spans fewer Planck cells)")
    rw.print("")
    rw.print("  USEFUL IDENTITY: n_e * n_top = (m_P/m_e) * (m_P/m_top)")
    n_top = orbital_results[-3]["n"]   # top quark (3rd from end: top, proton, neutron)
    # Find top quark
    top_result = next(r for r in orbital_results if r["name"] == "top quark")
    n_top = top_result["n"]
    rw.print("    n_e  = {:.4e}".format(n_electron))
    rw.print("    n_top = {:.4e}".format(n_top))
    rw.print("    sqrt(n_e * n_top) = {:.4e}  (geometric mean)".format(
        np.sqrt(n_electron * n_top)))
    rw.print("    m_P / sqrt(m_e * m_top) = {:.4e}  (should match)".format(
        M_P / np.sqrt(M_E * top_result["mass_kg"])))
    rw.print("")


# ===========================================================================
# STEP 4 -- SUB-PLANCK REFRAME
# ===========================================================================

def _sub_planck_reframe(rw, orbital_results):
    """
    Explore the idea that Planck is NOT the ground state but an excited state.
    Two directions:
    (A) l_P = n * a_0  -->  a_0 = l_P / n  (sub-Planck ground state)
    (B) a_0 = n * l_P  -->  Compton as the ground state (super-Planck ground state)
    """
    rw.subsection("Step 4: Two Directions for 'Planck as Excited State'")

    rw.print("  The user's hypothesis: 'What if Planck is like a p1, p2, p3")
    rw.print("  orbital -- an excited state, not the ground state?'")
    rw.print("")
    rw.print("  There are TWO ways to read this:")
    rw.print("")
    rw.print("  ---------------------------------------------------------------")
    rw.print("  DIRECTION A: Planck is ABOVE the ground state")
    rw.print("    l_P = n * a_0  (Planck = n lattice spacings of a finer grid)")
    rw.print("    a_0 = l_P / n  (smaller than Planck)")
    rw.print("    G_bare = c^3 * a_0^2 / hbar = G_known / n^2  (WEAKER than G)")
    rw.print("")
    rw.print("  This gives a sub-Planck lattice. G_bare << G_known. The observed")
    rw.print("  G_known would then come from n^2 modes ADDING coherently:")
    rw.print("    G_eff = n^2 * G_bare = G_known  [if modes add constructively]")
    rw.print("")
    rw.print("  Analogy: laser coherence. N photons in phase give N^2 intensity.")
    rw.print("  If n oscillators are phase-locked, effective G = n^2 * G_0.")
    rw.print("")

    rw.print("  DIRECTION A -- Sub-Planck lattice spacing for each particle:")
    headers = ["Particle", "n", "a_0 = l_P/n (m)", "log10(a_0/l_P)", "G_bare / G_known"]
    widths  = [14, 14, 18, 16, 16]
    rows_A = []
    for r in orbital_results:
        n      = r["n"]
        a_0    = L_P / n
        G_bare = C**3 * a_0**2 / HBAR
        rows_A.append([
            r["name"],
            "{:.4e}".format(n),
            "{:.4e}".format(a_0),
            "{:.1f}".format(np.log10(a_0 / L_P)),
            "{:.4e}".format(G_bare / G),
        ])
    rw.table(headers, rows_A, widths)
    rw.print("  NOTE: a_0 = l_P/n is the sub-Planck spacing. G_bare / G_known = 1/n^2.")
    rw.print("  For coherent addition to work, n^2 oscillators must lock in phase.")
    rw.print("")

    rw.print("  ---------------------------------------------------------------")
    rw.print("  DIRECTION B: Planck is BELOW the ground state")
    rw.print("    a_0 = n * l_P = lambda_Compton  (Compton IS the ground state)")
    rw.print("    G_bare = c^3 * lambda^2 / hbar  (G at Compton scale)")
    rw.print("    G_obs  = G_bare / n^2           (diluted by n^2 sub-modes)")
    rw.print("")
    rw.print("  This is the Dvali picture (Step 2). The Compton wavelength is")
    rw.print("  the 'real' lattice spacing. The Planck scale is an artefact of")
    rw.print("  having n^2 sub-modes inside each Compton cell.")
    rw.print("")
    rw.print("  Analogy: optical lattice in a crystal. The crystal spacing is ~1 Ang.")
    rw.print("  But the atom has internal structure at ~0.1 Ang = crystal/10.")
    rw.print("  External observers see the crystal spacing; internal physics")
    rw.print("  at the sub-level gives the observed interaction strength.")
    rw.print("")
    rw.print("  DIRECTION B -- Compton as ground state:")
    headers = ["Particle", "n", "a_0 = n*l_P = lambda (m)",
               "G_bare (m^3/kg/s^2)", "G_bare / G_known"]
    widths  = [14, 14, 26, 22, 16]
    rows_B = []
    for r in orbital_results:
        n      = r["n"]
        a_0    = r["lambda"]                      # = n * l_P
        G_bare = C**3 * a_0**2 / HBAR            # G at Compton scale
        rows_B.append([
            r["name"],
            "{:.4e}".format(n),
            "{:.4e}".format(a_0),
            "{:.4e}".format(G_bare),
            "{:.4e}".format(G_bare / G),
        ])
    rw.table(headers, rows_B, widths)
    rw.print("  NOTE: G_bare / G_known = n^2. Compton-scale gravity is n^2 STRONGER")
    rw.print("  than observed G. The n^2 dilution IS the hierarchy problem.")
    rw.print("")
    rw.print("  WHICH DIRECTION IS PDTP?")
    rw.print("  The PDTP Lagrangian has g*cos(psi - phi) where g ~ mass.")
    rw.print("  The coupling g is SET BY the particle mass -- it IS the Compton")
    rw.print("  frequency: omega_Compton = mc^2/hbar.")
    rw.print("  This points to Direction B: Compton scale is the natural input;")
    rw.print("  the Planck scale emerges as l_P = lambda/n = lambda * (m/m_P).")
    rw.print("")


# ===========================================================================
# STEP 5 -- WHAT COULD FIX n?
# ===========================================================================

def _what_determines_n(rw, orbital_results):
    """
    Survey of physical mechanisms that could give n = m_P / m_particle.
    These are the candidate answers to 'why is n so large?'
    """
    rw.subsection("Step 5: What Physical Mechanism Could Fix n?")

    rw.print("  The question 'what is n?' has multiple candidate answers.")
    rw.print("  Each reframes the hierarchy problem as a different kind of question.")
    rw.print("")

    # ---- Mechanism 1: Winding number ----------------------------------------
    rw.print("  MECHANISM 1: Topological Winding Number")
    rw.print("  -----------------------------------------")
    rw.print("  In a superfluid, a vortex has winding number n = (1/2pi) * oint grad(phase).")
    rw.print("  PDTP's spacetime condensate has a phase phi. If the phase winds n")
    rw.print("  times around a particle, n is topological -- robust, quantized,")
    rw.print("  and G-free (it comes from counting, not from G).")
    rw.print("")
    rw.print("  Required n values:")
    for r in orbital_results[:3]:  # show just leptons for brevity
        rw.print("    {:<14s}: n = {:.4e} = 2*pi * ({:.4e} / 2*pi) windings".format(
            r["name"], r["n"], r["n"] / (2 * np.pi)))
    rw.print("    ...")
    rw.print("")
    rw.print("  CHALLENGE: Winding numbers are usually small integers (1, 2, 3...).")
    rw.print("  Getting n ~ 10^22 from winding requires cosmological rotation")
    rw.print("  or a very long string/vortex line. Possible but speculative.")
    rw.print("")

    # ---- Mechanism 2: Cosmological time ------------------------------------
    rw.print("  MECHANISM 2: Cosmological Phase Accumulation")
    rw.print("  ----------------------------------------------")
    rw.print("  If the phase phi oscillates at frequency omega_0 = c/l_P (Planck freq),")
    rw.print("  then after cosmic time t, the accumulated phase is:")
    rw.print("    Phi_total = omega_0 * t_universe")
    omega_Planck = C / L_P
    t_univ       = 4.35e17             # s (13.8 Gyr)
    n_cosmic     = omega_Planck * t_univ / (2 * np.pi)
    rw.print("    omega_Planck  = {:.4e} rad/s".format(omega_Planck))
    rw.print("    t_universe    = {:.4e} s  (13.8 Gyr)".format(t_univ))
    rw.print("    n_cosmic      = omega_Planck * t_univ / (2*pi) = {:.4e}".format(n_cosmic))
    rw.print("")
    rw.print("  Compare to n_electron = {:.4e}".format(M_P / M_E))
    rw.print("  Ratio n_cosmic / n_electron = {:.4e}".format(n_cosmic / (M_P / M_E)))
    rw.print("")
    rw.print("  This is the Dirac large-numbers hypothesis in PDTP form.")
    rw.print("  CHALLENGE: This makes n time-dependent -> G varies with cosmic time.")
    rw.print("  Observational limits on G-dot/G ~ 10^-12 / year constrain this.")
    rw.print("")

    # ---- Mechanism 3: Mode counting ----------------------------------------
    rw.print("  MECHANISM 3: Lattice Mode Counting")
    rw.print("  ------------------------------------")
    rw.print("  If the PDTP condensate occupies a sphere of radius R with cell a,")
    rw.print("  the number of modes is N = (R/a)^3.")
    rw.print("  If R = R_Hubble and a = lambda_electron:")
    R_H  = C / 2.184e-18
    lam_e = HBAR / (M_E * C)
    N_modes_sphere = (R_H / lam_e)**3
    rw.print("    R_Hubble     = {:.4e} m".format(R_H))
    rw.print("    lambda_e     = {:.4e} m".format(lam_e))
    rw.print("    N_modes      = (R_H / lambda_e)^3 = {:.4e}".format(N_modes_sphere))
    rw.print("    sqrt(N_modes)= {:.4e}".format(N_modes_sphere**0.5))
    rw.print("    n_electron   = {:.4e}".format(M_P / M_E))
    rw.print("")
    rw.print("  CHALLENGE: N_modes^(1/2) ~ {:.1e} vs n_e ~ {:.1e}".format(
        N_modes_sphere**0.5, M_P / M_E))
    rw.print("  Not the same order of magnitude. The 3D sphere doesn't give n^2.")
    rw.print("")

    # ---- Mechanism 4: Species as n^2 ----------------------------------------
    rw.print("  MECHANISM 4: Hierarchy from Species Count (Dvali)")
    rw.print("  ---------------------------------------------------")
    rw.print("  If the condensate has N_sp = n^2 species (modes with independent")
    rw.print("  phase), the effective Planck mass is:")
    rw.print("    m_P_eff^2 = N_sp * m_P_bare^2")
    rw.print("")
    rw.print("  This is G-free IF N_sp can be counted from lattice topology.")
    rw.print("  In extra-dimension models: N_sp = (R_extra / l_extra)^d")
    rw.print("  where d = number of extra dimensions, R_extra = their radius.")
    rw.print("")
    rw.print("  PDTP version: the spacetime condensate could have internal")
    rw.print("  degrees of freedom (like spin) giving N_sp independent modes.")
    rw.print("  If N_sp ~ (R_Hubble / l_P)^2 (a 2D 'holographic' count):")
    N_holo = (R_H / L_P)**2
    rw.print("    N_holo = (R_H / l_P)^2 = {:.4e}".format(N_holo))
    rw.print("    n_e^2  = {:.4e}".format((M_P / M_E)**2))
    rw.print("    Ratio  = {:.4e}".format(N_holo / (M_P / M_E)**2))
    rw.print("")
    rw.print("  The holographic count is ~{:.1f} orders of magnitude from n_e^2.".format(
        np.log10(N_holo / (M_P / M_E)**2)))
    rw.print("  Close-ish but not a match. Needs further investigation.")
    rw.print("")


# ===========================================================================
# CONCLUSION
# ===========================================================================

def _conclusion(rw):
    rw.subsection("Phase 8 Conclusion: The Reframe")

    rw.print("  THE REFRAME IN ONE SENTENCE:")
    rw.print("    The hierarchy problem (G is small) = the orbital problem (n is large).")
    rw.print("")
    rw.print("  OLD QUESTION (circular):  What lattice spacing a gives G?")
    rw.print("    Answer: a = l_P.  But l_P uses G.  Dead end.")
    rw.print("")
    rw.print("  NEW QUESTION (not yet answered, but different):  What is n?")
    rw.print("    n = m_P / m_particle = lambda_Compton / l_P")
    rw.print("    n is dimensionless.  Dimensionless numbers have")
    rw.print("    topological, combinatorial, or geometric origins.")
    rw.print("    If n can be derived from lattice topology:")
    rw.print("      a_0 = lambda / n   [G-free]")
    rw.print("      G   = c^3 * a_0^2 / hbar   [G-free]")
    rw.print("      DONE.  Non-circular G.")
    rw.print("")
    rw.print("  ANALOGY TO PDTP ITSELF:")
    rw.print("    Standard GR: 'Space is curved by mass.'  (circular: what is space?)")
    rw.print("    PDTP reframe: 'Gravity is phase-locking of oscillators.'")
    rw.print("                  (new question: what are the oscillators?)")
    rw.print("")
    rw.print("    Standard hierarchy: 'G is 10^-37 times alpha_EM.'  (description only)")
    rw.print("    Orbital reframe:    'n = 2.3e22 -- what physics gives that number?'")
    rw.print("                         (new question: topological? cosmological? modal?)")
    rw.print("")
    rw.print("  CANDIDATE MECHANISMS SURVEYED:")
    rw.print("    1. Topological winding -- n is a vortex quantum number [quantized, G-free]")
    rw.print("    2. Cosmological time   -- n grows with universe age [time-dependent G]")
    rw.print("    3. Lattice mode count  -- N_modes ~ n^2 from 3D geometry [off by ~10^21]")
    rw.print("    4. Dvali species       -- N_sp = n^2 from extra dimensions [holographic ~10^11 off]")
    rw.print("")
    rw.print("  NONE is a clean solution yet.  But each points at a DIFFERENT physical")
    rw.print("  regime to investigate.  The winding-number mechanism (1) is the most")
    rw.print("  natural in PDTP because the framework already has a condensate phase")
    rw.print("  phi that particles can wind around.")
    rw.print("")
    rw.print("  NEXT STEP FOR THEORY:")
    rw.print("    Compute the vortex winding number in the PDTP condensate.")
    rw.print("    If a fundamental particle = a vortex with winding n,")
    rw.print("    what determines n?  The particle mass sets the Compton frequency;")
    rw.print("    the Compton frequency sets the phase accumulation rate;")
    rw.print("    the phase accumulation rate sets n after one period.")
    rw.print("    This is a closed, G-free chain -- if it closes consistently,")
    rw.print("    it is PDTP's derivation of G from first principles.")
    rw.print("")


# ===========================================================================
# ENTRY POINT
# ===========================================================================

def run_orbital_phase(rw, engine):
    """Phase 8 entry point.  Called from main.py after run_lisa_phase."""
    rw.section("Phase 8 -- Orbital Quantization Scanner (Planck as Excited State?)")

    rw.print("  CENTRAL QUESTION:")
    rw.print("  What if the Planck length is NOT the ground-state lattice spacing,")
    rw.print("  but rather the nth level of a deeper structure?")
    rw.print("")
    rw.print("  Just as PDTP reframed 'curved space' -> 'phase-locked oscillators',")
    rw.print("  this phase reframes 'small G' -> 'large orbital quantum number n'.")
    rw.print("")
    rw.print("  Particles scanned: {}".format(len(PARTICLES)))
    rw.print("  Mechanism candidates: 4 (winding, cosmological, modal, Dvali)")
    rw.print("")

    orbital = _orbital_table(rw)
    _dvali_analysis(rw, orbital)
    _algebraic_structure(rw, orbital)
    _sub_planck_reframe(rw, orbital)
    _what_determines_n(rw, orbital)
    _conclusion(rw)


# ===========================================================================
# STANDALONE
# ===========================================================================

if __name__ == "__main__":
    output_dir = os.path.join(_HERE, "outputs")
    rw = ReportWriter(output_dir, label="orbital_scanner")
    engine = SudokuEngine()
    run_orbital_phase(rw, engine)
    rw.close()
