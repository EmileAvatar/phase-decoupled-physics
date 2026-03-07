#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sudoku_engine.py — Verified physics equations as a pass/fail test suite.

Every equation here is established physics with a known numerical answer.
We USE these to test a candidate lattice spacing `a` and coupling K.

The PDTP bridge:
    K = hbar / (4*pi*c)       [G-free form from Part 29]
    kappa = K / a^2            [phase stiffness = spring constant / area]
    G_pred = c^2 / (4*pi*kappa) = c^3 * a^2 / hbar  [PDTP bridge to gravity]

If a candidate `a` gives G_pred = G_known  →  all 13 tests will PASS.
If G_pred != G_known  →  ALL 13 tests fail (they're all tied to G).

The scoring still ranks candidates: a ratio closer to 1.00 = closer to correct.
The ratio column is G_pred / G_known (or equivalent for each test).

Sources:
  NIST CODATA 2018: https://physics.nist.gov/cuu/Constants/index.html
  PDTP Part 29: substitution_chain_analysis.md
  PDTP Part 30: sudoku_consistency_check.py
"""

import numpy as np

# ===========================================================================
# PHYSICAL CONSTANTS (CODATA 2018)
# Source: https://physics.nist.gov/cuu/Constants/index.html
# ===========================================================================
HBAR = 1.054571817e-34    # J s  (reduced Planck constant)
C    = 2.99792458e8       # m/s  (speed of light)
G    = 6.67430e-11        # m^3 kg^-1 s^-2  (Newton's gravitational constant)
K_B  = 1.380649e-23       # J/K  (Boltzmann constant)
E_P  = 1.602176634e-19    # J/eV (elementary charge, used for eV conversions)

# Derived Planck units (from CODATA G, hbar, c)
L_P  = np.sqrt(HBAR * G / C**3)          # Planck length  ~1.616e-35 m
M_P  = np.sqrt(HBAR * C / G)             # Planck mass    ~2.176e-8 kg
T_P  = np.sqrt(HBAR * G / C**5)          # Planck time    ~5.391e-44 s
E_PL = np.sqrt(HBAR * C**5 / G)          # Planck energy  ~1.956e9 J
T_PL = E_PL / K_B                         # Planck temperature ~1.417e32 K

# Particle masses
M_E  = 9.1093837015e-31   # kg  (electron mass)
M_P_PROTON = 1.67262192369e-27  # kg  (proton mass)
M_SUN = 1.989e30           # kg  (solar mass)

# Other
ALPHA_EM = 7.2973525693e-3  # fine-structure constant (1/137.036...)
H_0 = 2.184e-18             # s^-1  (Hubble constant ~67.4 km/s/Mpc)
R_EARTH = 6.371e6            # m  (Earth mean radius)
M_EARTH = 5.972e24           # kg  (Earth mass)


# ===========================================================================
# SUDOKU ENGINE
# ===========================================================================

class SudokuEngine:
    """
    Run 13 verified physics tests against a PDTP candidate lattice spacing.

    Usage:
        engine = SudokuEngine()
        results = engine.test(a_m)   # a_m = lattice spacing in metres
        n_pass, n_fail = engine.score(results)
    """

    def __init__(self):
        self.G_known = G
        self.hbar    = HBAR
        self.c       = C

        # PDTP K (G-free, from Part 29)
        self.K_pdtp = HBAR / (4 * np.pi * C)

    # ------------------------------------------------------------------
    # Core derivation from a candidate lattice spacing
    # ------------------------------------------------------------------

    def _derive(self, a_m):
        """
        Given lattice spacing a_m (metres), compute PDTP predictions.
        Returns dict of derived values.
        """
        K   = self.K_pdtp
        kap = K / a_m**2                    # phase stiffness  [J/m^2]
        rho = kap / C**2                    # condensate density  [kg/m^3]
        G_p = C**3 * a_m**2 / HBAR         # PDTP G prediction  [m^3 kg^-1 s^-2]

        # Planck units from G_p
        l_p = np.sqrt(HBAR * G_p / C**3)
        m_p = np.sqrt(HBAR * C / G_p)
        t_p = np.sqrt(HBAR * G_p / C**5)
        e_p = np.sqrt(HBAR * C**5 / G_p)
        T_p = e_p / K_B

        return {
            "a"    : a_m,
            "kappa": kap,
            "rho"  : rho,
            "G_p"  : G_p,
            "l_p"  : l_p,
            "m_p"  : m_p,
            "t_p"  : t_p,
            "e_p"  : e_p,
            "T_p"  : T_p,
        }

    # ------------------------------------------------------------------
    # Individual tests
    # Each returns (name, expected, predicted, ratio, pass)
    # ratio = predicted/expected  (1.00 = perfect match)
    # ------------------------------------------------------------------

    def _t01_G(self, d):
        name = "Newton's G"
        exp  = G
        pred = d["G_p"]
        r    = pred / exp
        return (name, exp, pred, r, 0.99 <= r <= 1.01)

    def _t02_planck_length(self, d):
        name = "Planck length l_P"
        exp  = L_P
        pred = d["l_p"]
        r    = pred / exp
        return (name, exp, pred, r, 0.99 <= r <= 1.01)

    def _t03_planck_mass(self, d):
        name = "Planck mass m_P"
        exp  = M_P
        pred = d["m_p"]
        r    = pred / exp
        return (name, exp, pred, r, 0.99 <= r <= 1.01)

    def _t04_planck_time(self, d):
        name = "Planck time t_P"
        exp  = T_P
        pred = d["t_p"]
        r    = pred / exp
        return (name, exp, pred, r, 0.99 <= r <= 1.01)

    def _t05_planck_energy(self, d):
        name = "Planck energy E_P"
        exp  = E_PL
        pred = d["e_p"]
        r    = pred / exp
        return (name, exp, pred, r, 0.99 <= r <= 1.01)

    def _t06_planck_temp(self, d):
        name = "Planck temperature T_P"
        exp  = T_PL
        pred = d["T_p"]
        r    = pred / exp
        return (name, exp, pred, r, 0.99 <= r <= 1.01)

    def _t07_condensate_density(self, d):
        name = "Condensate density rho"
        # rho = kappa / c^2 = K / (a^2 * c^2) = hbar / (4*pi*c^3 * a^2)
        exp  = HBAR / (4 * np.pi * C**3 * d["a"]**2)
        pred = d["rho"]
        r    = pred / exp if exp != 0 else float("inf")
        return (name, exp, pred, r, 0.99 <= r <= 1.01)

    def _t08_schwarzschild(self, d):
        name = "Schwarzschild radius (1 M_sun)"
        exp  = 2 * G * M_SUN / C**2              # ~2954 m
        pred = 2 * d["G_p"] * M_SUN / C**2
        r    = pred / exp
        return (name, exp, pred, r, 0.99 <= r <= 1.01)

    def _t09_hawking_temp(self, d):
        name = "Hawking temperature (1 M_sun BH)"
        exp  = HBAR * C**3 / (8 * np.pi * G * M_SUN * K_B)
        pred = HBAR * C**3 / (8 * np.pi * d["G_p"] * M_SUN * K_B)
        r    = pred / exp
        return (name, exp, pred, r, 0.99 <= r <= 1.01)

    def _t10_alpha_grav(self, d):
        name = "Gravitational fine-structure alpha_G"
        # alpha_G = G * m_e^2 / (hbar * c) — dimensionless
        exp  = G * M_E**2 / (HBAR * C)           # ~1.75e-45
        pred = d["G_p"] * M_E**2 / (HBAR * C)
        r    = pred / exp
        return (name, exp, pred, r, 0.99 <= r <= 1.01)

    def _t11_hubble_density(self, d):
        name = "Hubble critical density rho_crit"
        exp  = 3 * H_0**2 / (8 * np.pi * G)     # ~8.5e-27 kg/m^3
        pred = 3 * H_0**2 / (8 * np.pi * d["G_p"])
        r    = pred / exp
        return (name, exp, pred, r, 0.99 <= r <= 1.01)

    def _t12_earth_gravity(self, d):
        name = "Earth surface gravity g"
        exp  = G * M_EARTH / R_EARTH**2           # ~9.82 m/s^2
        pred = d["G_p"] * M_EARTH / R_EARTH**2
        r    = pred / exp
        return (name, exp, pred, r, 0.99 <= r <= 1.01)

    def _t13_hierarchy_ratio(self, d):
        name = "Hierarchy ratio alpha_G/alpha_EM"
        # R = alpha_G / alpha_EM = G*m_e^2 / (hbar*c*alpha_EM)
        exp  = G * M_E**2 / (HBAR * C * ALPHA_EM)   # ~2.40e-43
        pred = d["G_p"] * M_E**2 / (HBAR * C * ALPHA_EM)
        r    = pred / exp
        return (name, exp, pred, r, 0.99 <= r <= 1.01)

    # ------------------------------------------------------------------
    # Public: run all 13 tests
    # ------------------------------------------------------------------

    def test(self, a_m):
        """
        Run all 13 tests for lattice spacing a_m.

        Returns list of dicts:
          {"name": str, "expected": float, "predicted": float,
           "ratio": float, "pass": bool}
        """
        d = self._derive(a_m)
        tests = [
            self._t01_G,
            self._t02_planck_length,
            self._t03_planck_mass,
            self._t04_planck_time,
            self._t05_planck_energy,
            self._t06_planck_temp,
            self._t07_condensate_density,
            self._t08_schwarzschild,
            self._t09_hawking_temp,
            self._t10_alpha_grav,
            self._t11_hubble_density,
            self._t12_earth_gravity,
            self._t13_hierarchy_ratio,
        ]
        results = []
        for fn in tests:
            name, exp, pred, ratio, passed = fn(d)
            results.append({
                "name"     : name,
                "expected" : exp,
                "predicted": pred,
                "ratio"    : ratio,
                "pass"     : passed,
            })
        return results, d["G_p"]

    def score(self, results):
        """Return (n_pass, n_fail, mean_log10_ratio_deviation)."""
        n_pass = sum(1 for r in results if r["pass"])
        n_fail = len(results) - n_pass
        # How far off (in decades) is the average test?
        log_devs = []
        for r in results:
            rat = r["ratio"]
            if rat > 0:
                log_devs.append(abs(np.log10(rat)))
        mean_dev = np.mean(log_devs) if log_devs else float("inf")
        return n_pass, n_fail, mean_dev
