#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_generator.py — Generates candidate lattice spacings to test against G.

Three modes:
  1. Named candidates  — from Parts 29-32 (re-run fresh for consistency check)
  2. Power-law sweep   — a = l_P * (m_e/m_P)^p1 * (m_p/m_P)^p2 * alpha^p3
  3. Mass-combo sweep  — geometric/harmonic/RMS means of all particle-mass pairs/triplets

Each candidate is a dict:
  {
    "name" : str,        (human-readable label)
    "a"    : float,      (lattice spacing in metres)
    "mode" : str,        ("named" | "power_law" | "mass_combo")
    "meta" : dict,       (extra info for printing, e.g. power exponents)
  }
"""

import numpy as np
from itertools import combinations

# ===========================================================================
# CONSTANTS (must match sudoku_engine.py)
# ===========================================================================
HBAR = 1.054571817e-34
C    = 2.99792458e8
G    = 6.67430e-11
E_P  = 1.602176634e-19   # J/eV

L_P  = np.sqrt(HBAR * G / C**3)
M_P  = np.sqrt(HBAR * C / G)

# Particle masses in kg (PDG 2024)
MeV  = 1e6 * E_P / C**2       # MeV/c^2 → kg

MASSES = {
    # Leptons
    "electron": 0.511    * MeV,
    "muon"    : 105.658  * MeV,
    "tau"     : 1776.86  * MeV,
    # Quarks (current, not constituent)
    "up"      : 2.16     * MeV,
    "down"    : 4.70     * MeV,
    "strange" : 93.5     * MeV,
    "charm"   : 1270.0   * MeV,
    "bottom"  : 4180.0   * MeV,
    "top"     : 172570.0 * MeV,
    # Baryons
    "proton"  : 938.272  * MeV,
    "neutron" : 939.565  * MeV,
}

# Koide base mass M0 = mu^2 where mu = mean(sqrt(m_i)) for leptons
_sqrt_lep = [np.sqrt(MASSES[p] * C**2 / E_P / 1e6)   # MeV^(1/2)
             for p in ["electron", "muon", "tau"]]
MU_KOIDE  = np.mean(_sqrt_lep)                         # MeV^(1/2)
M0_KOIDE  = MU_KOIDE**2 * MeV                          # kg

# Breathing mode estimate (geometric mean of hbar*c and Planck energy, Part 30)
E_GAP_GeV  = 69.4                                      # GeV (geometric mean model)
M_BREATH   = E_GAP_GeV * 1e3 * MeV                    # kg

ALPHA_EM   = 7.2973525693e-3                           # fine-structure constant


def _compton(mass_kg):
    """Reduced Compton wavelength: hbar / (m c)"""
    return HBAR / (mass_kg * C)


# ===========================================================================
# MODE 1: NAMED CANDIDATES
# ===========================================================================

def named_candidates():
    """
    Re-run the candidates from Parts 29-32 plus a few new ones.
    Returns list of candidate dicts.
    """
    cands = []

    def add(name, a, **meta):
        cands.append({"name": name, "a": a, "mode": "named", "meta": meta})

    # --- Controls (circular — use G) ---
    add("Planck length [CIRCULAR]",       L_P)
    add("Compton lambda_C(Planck mass) [CIRCULAR]", _compton(M_P))

    # --- Lepton-scale candidates ---
    add("lambda_C(electron)",             _compton(MASSES["electron"]))
    add("lambda_C(muon)",                 _compton(MASSES["muon"]))
    add("lambda_C(tau)",                  _compton(MASSES["tau"]))
    add("classical electron radius r_e",  ALPHA_EM * _compton(MASSES["electron"]))

    # --- Quark-scale candidates ---
    add("lambda_C(up quark)",             _compton(MASSES["up"]))
    add("lambda_C(down quark)",           _compton(MASSES["down"]))
    add("lambda_C(strange)",              _compton(MASSES["strange"]))
    add("lambda_C(charm)",                _compton(MASSES["charm"]))
    add("lambda_C(bottom)",               _compton(MASSES["bottom"]))
    add("lambda_C(top)",                  _compton(MASSES["top"]))

    # --- Baryon-scale candidates ---
    add("lambda_C(proton)",               _compton(MASSES["proton"]))
    add("lambda_C(neutron)",              _compton(MASSES["neutron"]))

    # --- Koide-derived candidates (Part 32) ---
    add("lambda_C(Koide M0 = 313.84 MeV)", _compton(M0_KOIDE))
    add("alpha * lambda_C(Koide M0)",       ALPHA_EM * _compton(M0_KOIDE))

    M_HOP = np.sqrt(0.5) * M0_KOIDE
    add("lambda_C(Koide hopping M_hop)",  _compton(M_HOP))

    M_GEOM = np.sqrt(MASSES["electron"] * MASSES["muon"])
    add("lambda_C(geom mean e*mu)",       _compton(M_GEOM))

    # --- Breathing mode estimate (Part 30) ---
    add("lambda_C(breathing gap 69.4 GeV)", _compton(M_BREATH))

    # --- NEW: geometric means with Planck scale ---
    add("sqrt(lambda_C(e) * l_P)  [NEW]",
        np.sqrt(_compton(MASSES["electron"]) * L_P))
    add("sqrt(lambda_C(proton) * l_P)  [NEW]",
        np.sqrt(_compton(MASSES["proton"]) * L_P))
    add("sqrt(lambda_C(M0) * l_P)  [NEW]",
        np.sqrt(_compton(M0_KOIDE) * L_P))

    # --- NEW: alpha-scaled Planck combinations ---
    add("l_P / alpha_EM  [NEW]",           L_P / ALPHA_EM)
    add("l_P * alpha_EM  [NEW]",           L_P * ALPHA_EM)
    add("l_P / sqrt(alpha_EM)  [NEW]",     L_P / np.sqrt(ALPHA_EM))
    add("l_P * sqrt(alpha_EM)  [NEW]",     L_P * np.sqrt(ALPHA_EM))

    # --- NEW: hierarchy motivated ---
    #   If G_pred/G_known = (m_P/m_e)^2, then correct a = l_P * (m_e/m_P) = lambda_C(e)/sqrt(4*pi)
    #   But we already test lambda_C(e). This tests the exact correction:
    hierarchy_factor = np.sqrt(MASSES["electron"] / M_P)
    add("l_P * sqrt(m_e/m_P)  [hierarchy fix]",
        L_P * hierarchy_factor)

    return cands


# ===========================================================================
# MODE 2: POWER-LAW SWEEP
# a = l_P * (m_e/m_P)^p1 * (m_p/m_P)^p2 * alpha_EM^p3
# ===========================================================================

def power_law_candidates(step=0.5, p_range=(-2, 2)):
    """
    Systematic sweep: a = l_P * (m_e/m_P)^p1 * (m_p/m_P)^p2 * alpha_EM^p3

    With step=0.5, p_range=(-2,2): 9^3 = 729 combinations.
    With step=0.25: 17^3 = 4913 combinations (slower but finer).
    """
    cands = []
    lo, hi = p_range
    powers = np.arange(lo, hi + step * 0.1, step)

    r_e_mp   = MASSES["electron"] / M_P
    r_p_mp   = MASSES["proton"]   / M_P

    for p1 in powers:
        for p2 in powers:
            for p3 in powers:
                a = L_P * (r_e_mp**p1) * (r_p_mp**p2) * (ALPHA_EM**p3)
                if a > 0 and np.isfinite(a):
                    name = "l_P*(m_e/m_P)^{:.2f}*(m_p/m_P)^{:.2f}*alpha^{:.2f}".format(
                        p1, p2, p3)
                    cands.append({
                        "name": name,
                        "a"   : a,
                        "mode": "power_law",
                        "meta": {"p1": p1, "p2": p2, "p3": p3},
                    })
    return cands


# ===========================================================================
# MODE 3: MASS-COMBINATION SWEEP
# Compton wavelengths of all pairs and triplets (geometric/harmonic/RMS means)
# ===========================================================================

def mass_combo_candidates():
    """
    Test lambda_C of geometric, harmonic, and RMS means for:
      - all pairs of particle masses
      - all triplets of particle masses
    Also includes: lambda_C of each particle scaled by alpha_EM and 1/alpha_EM.
    """
    cands = []
    names  = list(MASSES.keys())
    masses = [MASSES[n] for n in names]

    def add(label, mass_kg):
        if mass_kg > 0 and np.isfinite(mass_kg):
            a = _compton(mass_kg)
            cands.append({"name": label, "a": a, "mode": "mass_combo", "meta": {}})

    # Alpha-scaled single particles
    for n, m in zip(names, masses):
        add("alpha*lambda_C({})".format(n),       m / ALPHA_EM)   # heavier → shorter
        add("lambda_C({})/alpha".format(n),        m * ALPHA_EM)   # lighter → longer

    # All pairs
    for (n1, m1), (n2, m2) in combinations(zip(names, masses), 2):
        geom = np.sqrt(m1 * m2)
        harm = 2 * m1 * m2 / (m1 + m2)
        rms  = np.sqrt((m1**2 + m2**2) / 2)
        add("lambda_C(geom({},{}))".format(n1, n2), geom)
        add("lambda_C(harm({},{}))".format(n1, n2), harm)
        add("lambda_C(rms({},{}))".format(n1, n2),  rms)

    # All triplets (just geometric mean to keep size manageable)
    for (n1, m1), (n2, m2), (n3, m3) in combinations(zip(names, masses), 3):
        geom = (m1 * m2 * m3) ** (1.0/3.0)
        add("lambda_C(geom3({},{},{}))".format(n1, n2, n3), geom)

    return cands


# ===========================================================================
# ANALYTICAL: Find the exact power law that gives G_known
# ===========================================================================

def analytical_power_law():
    """
    Find the exact (p1, p2, p3) such that
      G_pred = c^3 * a^2 / hbar = G_known
    where a = l_P * (m_e/m_P)^p1 * (m_p/m_P)^p2 * alpha_EM^p3.

    Since G_pred = G_known requires a = l_P exactly (because l_P = sqrt(hbar*G/c^3)),
    the required correction factor is 1.  We need:
      (m_e/m_P)^p1 * (m_p/m_P)^p2 * alpha_EM^p3 = 1

    Taking log10:
      p1 * log10(m_e/m_P) + p2 * log10(m_p/m_P) + p3 * log10(alpha_EM) = 0

    This is one equation in 3 unknowns — infinitely many solutions.
    We report the family of solutions and the simplest ones.
    """
    L_e  = np.log10(MASSES["electron"] / M_P)   # ~ -22.2
    L_p  = np.log10(MASSES["proton"]   / M_P)   # ~ -19.1
    L_a  = np.log10(ALPHA_EM)                    # ~ -2.137

    # With p3=0: p1*L_e + p2*L_p = 0  →  p1/p2 = -L_p/L_e
    # Simplest: p1=1, p2 = -L_p/L_e
    p2_for_p1_1 = -L_p / L_e       # ~ 0.859
    # Simplest integer: p1=19, p2=22 (approximately)
    ratio = -L_p / L_e             # L_p/L_e ratio

    return {
        "L_e"          : L_e,
        "L_p"          : L_p,
        "L_alpha"      : L_a,
        "equation"     : "p1 * {:.4f} + p2 * {:.4f} + p3 * {:.4f} = 0".format(L_e, L_p, L_a),
        "p3_0_solution": "p1=1, p2={:.4f} (or p1={:.0f}, p2={:.0f} integers)".format(
            p2_for_p1_1, round(1/p2_for_p1_1 * 10), 10),
        "ratio_Lp_Le"  : ratio,
        "note"         : ("The condition forces a = l_P, which uses G. "
                          "There is no non-circular solution in this family."),
    }
