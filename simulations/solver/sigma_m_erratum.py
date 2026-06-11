#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sigma_m_erratum.py -- Phase 86: Part 89 Eq 89.17 Erratum (Part 118)
===================================================================
Part 89 Eq 89.17 states the DM self-interaction cross-section as

    sigma/m_DM ~ G/c^4 ~ 8.3e-43 m^2/kg = 8.3e-39 cm^2/g     ... (89.17)

Part 116 flagged three problems (Open Question O3):
  (1) DIMENSIONS: [G/c^4] = s^2 kg^-1 m^-1, NOT m^2/kg -- the formula
      as written is dimensionally inconsistent;
  (2) NUMBER: G/c^4 evaluates to 8.26e-45 (SI), not 8.3e-43 -- factor 100;
  (3) UNITS: 1 m^2/kg = 10 cm^2/g, so "8.3e-43 m^2/kg = 8.3e-39 cm^2/g"
      is internally inconsistent by a factor 1000.

This phase derives the CORRECT gravitational self-interaction
cross-section and verifies every claim by computation:

  S1: Dimensional audit of G/c^4 and of the corrected formula [SymPy units]
  S2: Corrected formula -- gravitational (Rutherford-type) scattering:
        b_90 = 2 G m / v^2   [90-degree deflection impact parameter]
        sigma ~ pi b_90^2  ->  sigma/m = 4 pi G^2 m / v^4
      (geometric strong-deflection estimate; Coulomb-analog log factors
      omitted -- order of magnitude)
  S3: Numbers for the Part 116 Planck vortex (m = m_P, v = 220 km/s)
      and margin vs the Bullet Cluster bound
  S4: Sudoku consistency check

Sources:
  Rutherford scattering / gravitational analog: b_90 = 2Gm/v^2 follows
      from the hyperbolic-orbit deflection theta = 2 arctan(GM/(b v^2));
      standard result, e.g. Binney & Tremaine, "Galactic Dynamics" (2008),
      S3.1 (two-body relaxation impact parameter).
  Clowe et al. (2006), ApJ 648 L109 -- Bullet Cluster sigma/m < 1 cm^2/g.

Research doc: erratum notes in condensate_layer_optics.md (Part 89),
  dark_matter_energy.md, dm_winding_selection.md (Part 116).
Output log: simulations/solver/outputs/sigma_m_erratum_<ts>.txt

ALL returned values are COMPUTED (RECHECK rule) -- no hardcoded results.
"""

import os
import sys

import numpy as np
import sympy as sp
from sympy.physics import units as u
from sympy.physics.units import meter, kilogram, second
from sympy.physics.units.systems.si import SI

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from sudoku_engine import HBAR, C, G, M_P
from print_utils import ReportWriter

V_HALO = 220e3                  # m/s
BULLET_BOUND_M2KG = 1.0e-4      # m^2/kg  (= 1 cm^2/g)
PART89_QUOTED_M2KG = 8.3e-43    # value printed in Eq 89.17
PART89_QUOTED_CM2G = 8.3e-39    # cm^2/g value printed in Eq 89.17


def dims_of(expr):
    """Return the SI dimensional expression of a sympy units expression."""
    return SI.get_dimension_system().get_dimensional_dependencies(
        u.Quantity._collect_factor_and_dimension(expr)[1]
        if hasattr(u.Quantity, '_collect_factor_and_dimension')
        else expr)


def step1_dimensional_audit(rw):
    """SymPy units: dimensions of G/c^4 vs sigma/m = m^2/kg."""
    rw.subsection("S1: Dimensional audit [SymPy units]")

    Gq = u.gravitational_constant
    cq = u.speed_of_light
    mq = u.kilogram

    target = meter**2 / kilogram

    expr_89 = Gq / cq**4
    expr_new = Gq**2 * mq / (meter / second)**4

    f89, d89 = SI._collect_factor_and_dimension(expr_89)
    ftg, dtg = SI._collect_factor_and_dimension(target)
    fnw, dnw = SI._collect_factor_and_dimension(expr_new)

    same_89 = (SI.get_dimension_system().equivalent_dims(d89, dtg))
    same_new = (SI.get_dimension_system().equivalent_dims(dnw, dtg))

    rw.print("  dim(G/c^4)          = " + str(d89))
    rw.print("  dim(sigma/m target) = " + str(dtg))
    rw.print("  G/c^4 has sigma/m dimensions: " + str(bool(same_89)))
    rw.print("  dim(G^2 m / v^4)    = " + str(dnw))
    rw.print("  G^2 m/v^4 has sigma/m dimensions: " + str(bool(same_new)))
    rw.print("")
    rw.print("  -> Eq 89.17 'sigma/m ~ G/c^4' is dimensionally INCONSISTENT;")
    rw.print("     the corrected combination is sigma/m ~ G^2 m / v^4.")

    return {'dim_89_ok': bool(same_89), 'dim_new_ok': bool(same_new)}


def step2_corrected_formula(rw):
    """
    Gravitational two-body scattering: 90-degree deflection impact
    parameter b_90 = 2 G m / v^2 (Binney & Tremaine S3.1; reduced-mass
    factors absorbed into the order-of-magnitude estimate).
    Geometric cross-section sigma = pi b_90^2:

        sigma / m = 4 pi G^2 m / v^4        [PDTP erratum of Eq 89.17]
    """
    rw.subsection("S2: Corrected formula (derived symbolically)")

    Gs, ms, vs = sp.symbols('G m v', positive=True)
    b90 = 2 * Gs * ms / vs**2
    sigma = sp.pi * b90**2
    sigma_over_m = sp.simplify(sigma / ms)
    expected = 4 * sp.pi * Gs**2 * ms / vs**4
    residual = sp.simplify(sigma_over_m - expected)

    rw.print("  b_90        = 2 G m / v^2")
    rw.print("  sigma       = pi b_90^2 = " + str(sp.simplify(sigma)))
    rw.print("  sigma/m     = " + str(sigma_over_m))
    rw.print("  SymPy residual vs 4 pi G^2 m / v^4 = " + str(residual))

    return {'sigma_over_m_expr': sigma_over_m, 'residual_zero': residual == 0}


def step3_numbers(rw, s2):
    """Numerical values for the Part 116 Planck vortex."""
    rw.subsection("S3: Numbers (m_DM = m_P, v = 220 km/s)")

    Gs, ms, vs = sp.symbols('G m v', positive=True)
    f = sp.lambdify((Gs, ms, vs), s2['sigma_over_m_expr'], 'numpy')
    som_new = float(f(G, M_P, V_HALO))             # m^2/kg
    som_g_c4 = G / C**4                            # what 89.17 evaluates to
    margin_new = np.log10(BULLET_BOUND_M2KG / som_new)

    ratio_quoted_vs_gc4 = PART89_QUOTED_M2KG / som_g_c4
    unit_factor = PART89_QUOTED_CM2G / (PART89_QUOTED_M2KG * 10.0)

    rw.key_value("G/c^4 (numeric)", "{:.3e} (s^2 kg^-1 m^-1, NOT m^2/kg)".format(som_g_c4))
    rw.key_value("Part 89 quoted value", "{:.1e} 'm^2/kg'".format(PART89_QUOTED_M2KG))
    rw.key_value("quoted / G_c4 numeric", "{:.0f}  (factor-100 discrepancy)".format(ratio_quoted_vs_gc4))
    rw.key_value("quoted cm^2/g vs correct conversion x10",
                 "{:.0f}x  (internal unit inconsistency)".format(unit_factor))
    rw.print("")
    rw.key_value("CORRECTED sigma/m = 4 pi G^2 m_P/v^4",
                 "{:.3e} m^2/kg = {:.3e} cm^2/g".format(som_new, som_new * 10))
    rw.key_value("Bullet bound", "{:.1e} m^2/kg".format(BULLET_BOUND_M2KG))
    rw.key_value("margin", "{:.1f} orders of magnitude".format(margin_new))
    rw.print("")
    rw.print("  Conclusion of Parts 89/116 UNCHANGED (still dozens of orders")
    rw.print("  below the bound) -- but formula and numbers now correct.")
    rw.print("  Note sigma/m ~ m_DM: the n=1 Planck vortex is the LARGEST of")
    rw.print("  the spectrum; all n >= 1 are even safer.")

    return {'som_new': som_new, 'som_g_c4': som_g_c4,
            'margin_new': margin_new,
            'ratio_quoted_vs_gc4': ratio_quoted_vs_gc4,
            'unit_factor': unit_factor}


def sudoku_check(rw, s1, s2, s3):
    """Reads computed values from the step dicts (RECHECK trace path)."""
    rw.section("S4: Sudoku consistency check")

    tests = []

    def add(name, value, condition, note):
        tests.append((name, value, "PASS" if condition else "FAIL", note))

    add("T1 dim(G/c^4) != m^2/kg",
        "inconsistent" if not s1['dim_89_ok'] else "consistent",
        not s1['dim_89_ok'], "Eq 89.17 dimensional error confirmed")

    add("T2 dim(G^2 m/v^4) == m^2/kg",
        "consistent" if s1['dim_new_ok'] else "inconsistent",
        s1['dim_new_ok'], "corrected formula dimensionally OK")

    add("T3 sigma/m = 4 pi G^2 m/v^4 (SymPy residual 0)",
        "resid=0" if s2['residual_zero'] else "resid!=0",
        s2['residual_zero'], "derivation exact")

    add("T4 factor-100 numeric discrepancy in 89.17",
        "{:.0f}".format(s3['ratio_quoted_vs_gc4']),
        80 < s3['ratio_quoted_vs_gc4'] < 120,
        "quoted 8.3e-43 vs computed 8.3e-45")

    add("T5 factor-1000 internal unit error in 89.17",
        "{:.0f}".format(s3['unit_factor']),
        800 < s3['unit_factor'] < 1200,
        "cm^2/g value vs x10 conversion")

    add("T6 corrected value below Bullet bound",
        "{:.1e} m^2/kg".format(s3['som_new']),
        s3['som_new'] < BULLET_BOUND_M2KG,
        "margin {:.1f} orders".format(s3['margin_new']))

    add("T7 conclusion direction unchanged",
        "margin {:.0f} > 38 orders".format(s3['margin_new']),
        s3['margin_new'] > 38,
        "Parts 89/116 verdicts survive the correction")

    rows = [[t[0], t[1], t[2]] for t in tests]
    rw.table(["test", "computed value", "verdict"], rows)
    n_pass = sum(1 for t in tests if t[2] == "PASS")
    rw.print("")
    rw.print("  Score: {}/{} PASS".format(n_pass, len(tests)))
    return {'n_pass': n_pass, 'n_total': len(tests)}


def main():
    rw = ReportWriter(os.path.join(_HERE, "outputs"), label="sigma_m_erratum")
    rw.section("Phase 86 (Part 118): Part 89 Eq 89.17 erratum")
    rw.print("Correct the DM self-interaction cross-section formula.")

    s1 = step1_dimensional_audit(rw)
    s2 = step2_corrected_formula(rw)
    s3 = step3_numbers(rw, s2)
    s4 = sudoku_check(rw, s1, s2, s3)

    rw.section("Verdict (Part 118)")
    rw.print("  Eq 89.17 REPLACED:")
    rw.print("    OLD: sigma/m ~ G/c^4 ~ 8.3e-43 m^2/kg   [dimensionally wrong,")
    rw.print("         factor-100 numeric error, factor-1000 unit error]")
    rw.print("    NEW: sigma/m = 4 pi G^2 m_DM / v^4")
    rw.print("         = {:.2e} m^2/kg at m_DM = m_P, v = 220 km/s".format(
        s3['som_new']))
    rw.print("  Bullet margin: {:.1f} orders (was ~39-40). Verdicts of".format(
        s3['margin_new']))
    rw.print("  Parts 89 and 116 unchanged. Part 116 O3: RESOLVED.")
    rw.print("  Sudoku: {}/{} PASS".format(s4['n_pass'], s4['n_total']))
    rw.close()


if __name__ == "__main__":
    main()
