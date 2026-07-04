#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
t47_mcond_scanner.py -- Phase 88: m_cond Consequence Scanner (Part 120)
=======================================================================
T47: Scan m_cond from ~1 eV/c^2 to m_P c^2 ~ 1.22e28 eV/c^2 and
tabulate all cascade consequences.  One free parameter -- one table row.

PURPOSE: LOOKUP TABLE, not a finder.
  Part 115 no-go theorem proves m_cond cannot be selected by any internal
  PDTP principle (scale-invariance argument, algebraically proven).
  A future measurement of omega_gap or rho_cond selects one row and
  rules out all others.

CASCADE FORMULAS (all DERIVED in Parts 33/34 -- no new results here):
  G       = hbar*c / m_cond^2              [Part 33]
  omega   = m_cond*c^2 / hbar              [Part 33]
  a_0     = hbar / (m_cond*c)              [Part 33]
  n_e     = m_cond / m_e                   [Part 33]
  m_DM    = m_cond   (n=1 vortex)          [Part 116]
  rho     = m_cond^4*c^3 / hbar^3          [Parts 21/34]
  xi      = a_0 / sqrt(2)                  [Part 34]
  g_GP    = hbar^3 / (m_cond^2*c)          [Part 34, PDTP Original]
  L_bih   = a_0 / 2  (biharmonic scale)    [Part 61]
  kappa_GL = sqrt(2)  (Type II -- CHECK)   [Part 36/37]

SUDOKU at m_cond = m_P (12 tests, all PASS expected):
  T1 G_pred / G_known = 1.000
  T2 omega_gap / omega_P = 1.000
  T3 a_0 / l_P = 1.000
  T4 rho_cond / rho_P = 1.000
  T5 xi*sqrt(2) / l_P = 1.000
  T6 g_GP*n_0 / (m_P*c^2) = 1.000  (chemical potential check)
  T7 c_s / c = 1.000                (Part 34 key result)
  T8 m_DM / m_P = 1.000
  T9 n_e / (m_P/m_e) = 1.000
  T10 r_S(m_P) / (2*a_0) = 1.000   (Dvali-Gomez alpha_gr=1, Part 115)
  T11 kappa_GL / sqrt(2) = 1.000
  T12 alpha_G(pred) / alpha_G(known) = 1.000

Prerequisites: Parts 33, 34, 36, 61, 115, 116
Output: simulations/solver/outputs/t47_mcond_scanner_<timestamp>.txt
ALL returned values COMPUTED from inputs -- no hardcoded physics results.
"""

import math
import os
import sys

import numpy as np

_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _DIR)
from print_utils import ReportWriter

# ------------------------------------------------------------------
# Physical constants (SI) -- all exact or CODATA 2018
# ------------------------------------------------------------------
HBAR    = 1.054571817e-34     # J s     reduced Planck constant (exact)
C       = 2.99792458e8        # m/s     speed of light (exact)
G_KNOWN = 6.67430e-11         # m^3 kg^-1 s^-2   Newton G (CODATA 2018)
M_E     = 9.1093837015e-31    # kg      electron mass
M_PROT  = 1.67262192369e-27   # kg      proton mass
EV_J    = 1.602176634e-19     # J/eV    exact SI definition

# Derived Planck units (computed, not hardcoded)
M_P     = math.sqrt(HBAR * C / G_KNOWN)        # kg   Planck mass
L_P     = math.sqrt(HBAR * G_KNOWN / C**3)     # m    Planck length
RHO_P   = M_P / L_P**3                         # kg/m^3  Planck density
OMEGA_P = M_P * C**2 / HBAR                    # rad/s   Planck frequency
ALPHA_G = G_KNOWN * M_E**2 / (HBAR * C)        # dimensionless grav coupling


def eV_to_kg(m_eV):
    """Convert eV/c^2 to kg."""
    return m_eV * EV_J / C**2


def kg_to_eV(m_kg):
    """Convert kg to eV/c^2."""
    return m_kg * C**2 / EV_J


# ------------------------------------------------------------------
# Individual calculator functions (matching user pseudocode structure)
# Each takes m_cond in kg and returns one computed quantity.
# ------------------------------------------------------------------

def Newtons(m_cond):
    """
    G = hbar*c / m_cond^2   [Part 33, DERIVED]
    Newton's G predicted from condensate grain mass.
    Returns G in m^3 kg^-1 s^-2.
    """
    return HBAR * C / m_cond**2


def BreathingMode(m_cond):
    """
    omega_gap = m_cond * c^2 / hbar   [Part 33, DERIVED]
    Breathing-mode gap frequency in rad/s.
    The 'gap' means no propagating mode exists below this frequency --
    it is the condensate's characteristic oscillation frequency.
    """
    return m_cond * C**2 / HBAR


def LatticeSpacing(m_cond):
    """
    a_0 = hbar / (m_cond * c)   [Part 33, DERIVED]
    Condensate lattice spacing = Compton wavelength of the grain.
    At m_cond = m_P this equals the Planck length exactly.
    Returns a_0 in metres.
    """
    return HBAR / (m_cond * C)


def WindingNumber(m_cond, m_particle):
    """
    n = m_cond / m_particle   [Part 33, DERIVED]
    Vortex winding number for a particle of mass m_particle.
    n < 1 means no stable vortex for that particle in this condensate.
    Called with m_particle = M_E to get the electron winding number.
    """
    return m_cond / m_particle


def DarkMatterMass(m_cond):
    """
    m_DM = m_cond   (n=1 vortex, Part 116 DERIVED)
    The lightest stable vortex has winding n=1.
    Its energy = m_cond * c^2.  Returns m_DM in kg.
    """
    return m_cond


def CondensateDensity(m_cond):
    """
    rho = m_cond / a_0^3 = m_cond^4 * c^3 / hbar^3   [Parts 21/34]
    Mass density of the condensate at the lattice scale.
    Returns rho in kg/m^3.
    """
    a_0 = LatticeSpacing(m_cond)
    return m_cond / a_0**3


def HealingLength(m_cond):
    """
    xi = a_0 / sqrt(2)   [Part 34, DERIVED]
    BEC healing length: the distance over which the condensate order
    parameter recovers from a point defect.  xi = a_0/sqrt(2) exactly.
    Returns xi in metres.
    """
    return LatticeSpacing(m_cond) / math.sqrt(2)


def GPInteractionConstant(m_cond):
    """
    g_GP = hbar^3 / (m_cond^2 * c)   [Part 34, PDTP Original]
    Gross-Pitaevskii interaction constant (units J m^3).
    Derived from the condition mu = g_GP * n_0 = m_cond * c^2
    (chemical potential = rest-mass energy of one grain).
    Returns g_GP in J m^3.
    """
    return HBAR**3 / (m_cond**2 * C)


def BiharmonicScreeningScale(m_cond):
    """
    L_bih = a_0 / 2 = hbar / (2 * m_cond * c)   [Part 61, approx]
    Screening scale from nabla^4 Phi + 4g^2 Phi = source.
    Crossover wavenumber k_screen satisfies k^4 = 4g^2 where
    g ~ omega_gap/c = m_cond*c/hbar, giving k_screen = 2*m_cond*c/hbar.
    Below L_bih: 4th-order biharmonic gravity.
    Above L_bih: standard Newtonian 1/r^2 gravity.
    Returns L_bih in metres.
    """
    return LatticeSpacing(m_cond) / 2.0


def GLParameter(m_cond):
    """
    kappa_GL = sqrt(2)   [Part 36/37 -- m_cond-INDEPENDENT]
    Ginzburg-Landau parameter for the PDTP condensate.
    kappa_GL > 1/sqrt(2) implies Type II condensate: Abrikosov flux
    tubes (vortices) form for any m_cond.
    This column is a SELF-CHECK: must equal sqrt(2) in every row.
    The m_cond argument is acknowledged but not used -- by design.
    """
    _ = m_cond   # not used: kappa_GL is m_cond-independent
    return math.sqrt(2)


# ------------------------------------------------------------------
# Row aggregator
# ------------------------------------------------------------------

def compute_row(m_cond_eV):
    """
    Compute all cascade consequences for m_cond (given in eV/c^2).
    Returns dict of all quantities in SI units, plus m_eV for labelling.
    All values are computed from m_cond -- no hardcoded physics.
    """
    m = eV_to_kg(m_cond_eV)
    return {
        'm_eV'    : m_cond_eV,
        'm_kg'    : m,
        'G_pred'  : Newtons(m),
        'omega_gap': BreathingMode(m),
        'a0'      : LatticeSpacing(m),
        'n_e'     : WindingNumber(m, M_E),
        'm_DM_eV' : kg_to_eV(DarkMatterMass(m)),
        'rho_cond': CondensateDensity(m),
        'xi'      : HealingLength(m),
        'g_GP'    : GPInteractionConstant(m),
        'L_bih'   : BiharmonicScreeningScale(m),
        'kappa_GL': GLParameter(m),
    }


# ------------------------------------------------------------------
# Table output (two sub-tables to stay under 120 chars wide)
# ------------------------------------------------------------------

def _sci(x):
    """Format a float as compact scientific notation (9 chars)."""
    if x == 0.0:
        return "0.000e+00"
    return "{:.3e}".format(x)


def print_tables(rows, rw):
    """
    Print two ASCII sub-tables.
    Table A: gravity-side quantities (G, omega_gap, a_0, xi, L_bih).
    Table B: condensate-side quantities (n_e, m_DM, rho, g_GP, kappa_GL).
    """
    # Table A
    rw.subsection("Table A -- Gravity cascade (G, omega_gap, a_0, xi, L_bih)")
    rw.print("  n_e < 1 flag: condensate lighter than electron (unphysical vortex).")
    rw.print("")
    hdr_a  = ["m_cond[eV]", "G[m3kgs2]", "omega[r/s]", "a0[m]", "xi[m]", "L_bih[m]"]
    wid_a  = [12, 12, 12, 12, 12, 12]
    data_a = [[_sci(r['m_eV']), _sci(r['G_pred']), _sci(r['omega_gap']),
               _sci(r['a0']), _sci(r['xi']), _sci(r['L_bih'])]
              for r in rows]
    rw.table(hdr_a, data_a, wid_a)

    # Table B
    rw.subsection("Table B -- Condensate cascade (n_e, m_DM, rho, g_GP, kappa_GL)")
    hdr_b  = ["m_cond[eV]", "n_e(elect)", "m_DM[eV]", "rho[kg/m3]", "g_GP[Jm3]", "kappa_GL"]
    wid_b  = [12, 12, 12, 12, 12, 10]
    data_b = [[_sci(r['m_eV']), _sci(r['n_e']), _sci(r['m_DM_eV']),
               _sci(r['rho_cond']), _sci(r['g_GP']), "{:.6f}".format(r['kappa_GL'])]
              for r in rows]
    rw.table(hdr_b, data_b, wid_b)


# ------------------------------------------------------------------
# Sudoku consistency checks at m_cond = m_P (12 tests)
# ------------------------------------------------------------------

def sudoku_checks(rw):
    """
    12 checks at m_cond = m_P against known Planck physics.
    Every ratio reads from compute_row() -- no hardcoded expected values.
    tol=0.01 (1%) unless noted.
    """
    rw.section("Sudoku Consistency Checks at m_cond = m_P")
    rw.print("  All ratios should be 1.000 within 1%.")
    rw.print("  m_P = {:.6e} kg = {:.4e} eV/c^2".format(M_P, kg_to_eV(M_P)))
    rw.print("")

    m_P_eV = kg_to_eV(M_P)
    row    = compute_row(m_P_eV)
    m      = row['m_kg']   # = M_P (computed, not assumed)

    passes = 0
    total  = 12

    def chk(label, ratio, tol=0.01):
        nonlocal passes
        ok  = abs(ratio - 1.0) < tol
        tag = "PASS" if ok else "FAIL"
        if ok:
            passes += 1
        rw.print("  {}: ratio={:.8f}  [{}]".format(label, ratio, tag))

    # T1: G_pred / G_known
    chk("T1  G_pred / G_known          ", row['G_pred'] / G_KNOWN)

    # T2: omega_gap / Planck frequency
    chk("T2  omega_gap / omega_P       ", row['omega_gap'] / OMEGA_P)

    # T3: a_0 / Planck length
    chk("T3  a_0 / l_P                 ", row['a0'] / L_P)

    # T4: rho_cond / Planck density
    chk("T4  rho_cond / rho_P          ", row['rho_cond'] / RHO_P)

    # T5: xi = l_P/sqrt(2) -> xi*sqrt(2)/l_P = 1
    chk("T5  xi*sqrt(2) / l_P          ", row['xi'] * math.sqrt(2) / L_P)

    # T6: g_GP * n_0 = m_P * c^2  (chemical potential = rest energy)
    # n_0 computed from rho_cond / m, both taken from row
    n_0      = row['rho_cond'] / m
    mu_pred  = row['g_GP'] * n_0
    mu_ref   = m * C**2
    chk("T6  g_GP*n_0 / (m_P*c^2)      ", mu_pred / mu_ref)

    # T7: c_s = c  (Part 34 key result: c_s = sqrt(g_GP*n_0/m_P) = c)
    c_s = math.sqrt(row['g_GP'] * n_0 / m)
    chk("T7  c_s / c                   ", c_s / C)

    # T8: m_DM = m_P  (trivially satisfied when m_cond = m_P)
    chk("T8  m_DM_eV / m_P_eV          ", row['m_DM_eV'] / m_P_eV)

    # T9: n_e = m_P / m_e
    n_e_ref = M_P / M_E
    chk("T9  n_e / (m_P/m_e)           ", row['n_e'] / n_e_ref)

    # T10: Schwarzschild r_S = 2*G*m_P/c^2
    # Dvali-Gomez (Part 115): r_S = 2*l_P = 2*a_0 at m_cond = m_P
    r_S = 2.0 * row['G_pred'] * m / C**2
    chk("T10 r_S / (2*a_0)             ", r_S / (2.0 * row['a0']))

    # T11: kappa_GL = sqrt(2)  (constant check -- not a prediction)
    chk("T11 kappa_GL / sqrt(2)        ", row['kappa_GL'] / math.sqrt(2))

    # T12: alpha_G = G*m_e^2/(hbar*c) matches known value
    alpha_G_pred = row['G_pred'] * M_E**2 / (HBAR * C)
    chk("T12 alpha_G(pred) / alpha_G   ", alpha_G_pred / ALPHA_G)

    rw.print("")
    rw.print("  SUDOKU SCORE: {}/{} PASS".format(passes, total))
    return passes, total


# ------------------------------------------------------------------
# Main
# ------------------------------------------------------------------

def main():
    out_dir = os.path.join(_DIR, "outputs")
    rw = ReportWriter(out_dir, label="t47_mcond_scanner")

    rw.section("T47: m_cond Consequence Scanner (Part 120, Phase 88)")
    rw.print("  Planck mass : m_P = {:.6e} kg = {:.4e} eV/c^2".format(M_P, kg_to_eV(M_P)))
    rw.print("  Planck len  : l_P = {:.6e} m".format(L_P))
    rw.print("  Planck dens : rho_P = {:.4e} kg/m^3".format(RHO_P))
    rw.print("  G (known)   : G   = {:.6e} m^3 kg^-1 s^-2".format(G_KNOWN))
    rw.print("  alpha_G     : {:.4e}  (gravitational fine-struct. const, electron)".format(ALPHA_G))
    rw.print("")
    rw.print("  LOOKUP TABLE: one row per m_cond decade, 29 rows total.")
    rw.print("  kappa_GL = sqrt(2) in every row is a CHECK, not a prediction.")
    rw.print("  n_e < 1 means m_cond < m_e (no stable electron vortex -- unphysical).")
    rw.print("")
    rw.print("  No-go theorem (Part 115): PDTP cannot select m_cond internally.")
    rw.print("  Measuring omega_gap picks a row; all others are ruled out.")

    # Build scan: 29 log-spaced decades 10^0 to 10^28 eV + exact m_P
    rw.section("Scan Results")
    m_eV_list = list(np.logspace(0, 28, 29))
    m_eV_list.append(kg_to_eV(M_P))   # ensure m_P is in the table
    m_eV_list = sorted(set(m_eV_list))
    rows = [compute_row(m_eV) for m_eV in m_eV_list]
    print_tables(rows, rw)

    # Reference rows for named particle / energy scales
    rw.subsection("Named Reference Rows")
    refs = [
        ("electron   m_e", M_E),
        ("proton     m_p", M_PROT),
        ("Lambda_QCD 200 MeV", eV_to_kg(200.0e6)),
        ("Higgs mass 125 GeV", eV_to_kg(125.1e9)),
        ("Planck     m_P", M_P),
    ]
    for label, m_ref_kg in refs:
        r = compute_row(kg_to_eV(m_ref_kg))
        rw.print("  [{}]".format(label))
        rw.print("    m_cond   = {:.4e} eV/c^2  ({:.4e} kg)".format(r['m_eV'], r['m_kg']))
        rw.print("    G_pred   = {:.4e} m^3/kg/s^2".format(r['G_pred']))
        rw.print("    omega    = {:.4e} rad/s".format(r['omega_gap']))
        rw.print("    a_0      = {:.4e} m".format(r['a0']))
        rw.print("    n_e      = {:.4e}  {}".format(
            r['n_e'], "(<1 unphysical)" if r['n_e'] < 1 else "(stable vortex)"))
        rw.print("    rho_cond = {:.4e} kg/m^3".format(r['rho_cond']))
        rw.print("    xi       = {:.4e} m".format(r['xi']))
        rw.print("    g_GP     = {:.4e} J m^3".format(r['g_GP']))
        rw.print("    kappa_GL = {:.6f}  [CHECK=sqrt(2)]".format(r['kappa_GL']))
        rw.print("")

    # Sudoku
    passes, total = sudoku_checks(rw)

    # Verdict
    rw.section("Verdict")
    rw.print("  Rows computed : {}".format(len(rows)))
    rw.print("  Sudoku        : {}/{} PASS at m_cond = m_P".format(passes, total))
    rw.print("")
    rw.print("  HOW TO USE:")
    rw.print("  1. Measure omega_gap (or rho_cond, or xi) experimentally.")
    rw.print("  2. Find the row with the matching value in Table A or B.")
    rw.print("  3. All other quantities in that row are then PREDICTED -- no free params.")
    rw.print("  4. Every row outside the measurement band is RULED OUT.")
    rw.print("")
    rw.print("  STRATEGIC NOTE:")
    rw.print("  m_cond = m_P (Planck mass) is the only row where G_pred = G_known.")
    rw.print("  That is WHY m_P is singled out -- not from theory, from measurement.")
    rw.print("  The Part 115 no-go theorem says this cannot change; only MEASURING")
    rw.print("  omega_gap can confirm it. That is Goal 1, Strategy A (Phase 7).")
    rw.print("")
    rw.print("  Output: {}".format(rw.path))
    rw.close()
    print("")
    print("Log saved to: {}".format(rw.path))


if __name__ == "__main__":
    main()


