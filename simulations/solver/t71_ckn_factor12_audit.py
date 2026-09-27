"""
T71 (TODO_04.md), Part 152 -- Audit the CKN "factor 12" formula
discrepancy (Part 54).

Two citations of the CKN (Cohen-Kaplan-Nelson) bound appeared to disagree:

  cosmological_constant_fcc.md (Part 54 prose): rho_CKN ~ hbar*c/L_eff^4
                                                 = hbar*c/(l_P^2*L_H^2)
  equation_reference.md / the actual code:      rho_CKN = c^2/(G*L_H^2)

This script traces the discrepancy to its source, rather than assuming
either side is simply wrong.

Four things are established here, all computed (not asserted):

1. [VERIFIED] The two formulas are NOT literally the same quantity: a
   proper sympy.physics.units dimensional check shows hbar*c/(l_P^2*L_H^2)
   has units of ENERGY density (J/m^3), while c^2/(G*L_H^2) has units of
   MASS density (kg/m^3) -- they differ by exactly a factor of c^2, the
   standard energy-density-to-mass-density conversion (rho_mass =
   rho_energy/c^2), not a random inconsistency.

2. [VERIFIED, algebraic] Substituting the standard identity l_P^2 =
   hbar*G/c^3 into the energy-density form hbar*c/(l_P^2*L_H^2) gives
   EXACTLY c^4/(G*L_H^2) -- and dividing this by c^2 (the energy-to-mass
   conversion) gives EXACTLY c^2/(G*L_H^2), matching the code's mass-
   density form with zero residual. The two formulas are consistent,
   related by a well-defined physical conversion the Part 54 prose never
   states explicitly -- that omission, not a numerical error, is the bug.

3. [VERIFIED] The code's own internal identity (used in
   cosmo_constant.py's comment, never independently checked before this
   audit) rho_Planck*(l_P/L_H)^2 = c^2/(G*L_H^2) is confirmed exactly
   (residual 0) -- the actual computed number 7.1e-26 kg/m^3 used
   throughout the project is a self-consistent mass density, not the
   product of the units bug.

4. [RECOMPUTED, PRECISE] rho_CKN, rho_Lambda_obs, and their ratio are
   recomputed here directly from the same constants already used
   elsewhere in the project (sudoku_engine.py), to confirm (not just
   re-cite) whether "factor 12" survives at full precision.

Output DATA only -- interpretation lives in
docs/research/ckn_factor12_audit.md.
"""

import sympy as sp
import sympy.physics.units as u
from sympy.physics.units.systems import SI
import math
import sys
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from sudoku_engine import HBAR, C, G, L_P, H_0


# ---------------------------------------------------------------------
# 1. Dimensional check: energy density vs mass density
# ---------------------------------------------------------------------

def verify_dimensional_mismatch():
    """Use sympy.physics.units to independently confirm the two cited
    formulas have DIFFERENT physical dimensions (energy density vs mass
    density), differing by exactly a factor of c^2. Comparison done via
    get_dimensional_dependencies() (base mass/length/time powers), the
    robust way to compare two dimensional expressions that may be
    written in different (but equivalent) derived-unit forms."""
    from sympy.physics.units.dimensions import Dimension

    energy_density_form = (u.hbar * u.speed_of_light) / (u.meter**2 * u.meter**2)
    mass_density_form = (u.speed_of_light**2) / (u.gravitational_constant * u.meter**2)

    ds = SI.get_dimension_system()
    dep1 = ds.get_dimensional_dependencies(Dimension(SI.get_dimensional_expr(energy_density_form)))
    dep2 = ds.get_dimensional_dependencies(Dimension(SI.get_dimensional_expr(mass_density_form)))

    ref_energy_density = ds.get_dimensional_dependencies(
        Dimension(SI.get_dimensional_expr(u.joule / u.meter**3)))
    ref_mass_density = ds.get_dimensional_dependencies(
        Dimension(SI.get_dimensional_expr(u.kilogram / u.meter**3)))

    # Normalize dict keys (Dimension(length) vs Dimension(length, L) print
    # differently but represent the same base dimension) by comparing on
    # dimension NAME strings rather than the Dimension objects themselves.
    def norm(d):
        return {str(k.name): v for k, v in d.items()}

    formula1_is_energy_density = norm(dep1) == norm(ref_energy_density)
    formula2_is_mass_density = norm(dep2) == norm(ref_mass_density)

    # Ratio of the two dimensions, expressed as base powers: dep1 - dep2
    # should equal the dimensional dependencies of c^2 (velocity^2).
    all_keys = set(norm(dep1)) | set(norm(dep2))
    ratio_dep = {k: norm(dep1).get(k, 0) - norm(dep2).get(k, 0) for k in all_keys}
    ratio_dep = {k: v for k, v in ratio_dep.items() if v != 0}

    c_squared_dep = norm(ds.get_dimensional_dependencies(
        Dimension(SI.get_dimensional_expr(u.speed_of_light**2))))

    ratio_is_c_squared = ratio_dep == c_squared_dep

    return {
        'dim_of_hbar_c_over_L4': norm(dep1),
        'dim_of_c2_over_GL2': norm(dep2),
        'formula1_is_energy_density': formula1_is_energy_density,
        'formula2_is_mass_density': formula2_is_mass_density,
        'ratio_of_the_two_dimensions': ratio_dep,
        'ratio_equals_c_squared_dimension': ratio_is_c_squared,
    }


# ---------------------------------------------------------------------
# 2. Algebraic reconciliation: l_P^2 = hbar*G/c^3 substitution
# ---------------------------------------------------------------------

def verify_algebraic_reconciliation():
    """Substitute l_P^2 = hbar*G/c^3 into the energy-density form and
    confirm it reduces to c^4/(G*L_H^2); confirm dividing that by c^2
    (energy -> mass density) gives EXACTLY c^2/(G*L_H^2), matching the
    code's own formula with zero residual."""
    hbar, c, G_sym, L_H = sp.symbols('hbar c G L_H', positive=True)
    lP2 = hbar * G_sym / c**3   # standard identity, l_P^2

    energy_density_form = hbar * c / (lP2 * L_H**2)
    energy_density_reduced = sp.simplify(energy_density_form)

    expected_c4_form = c**4 / (G_sym * L_H**2)
    residual_vs_c4_form = sp.simplify(energy_density_reduced - expected_c4_form)

    mass_density_from_conversion = sp.simplify(energy_density_reduced / c**2)
    code_mass_density_form = c**2 / (G_sym * L_H**2)
    residual_vs_code_form = sp.simplify(mass_density_from_conversion - code_mass_density_form)

    return {
        'energy_density_form_reduced': energy_density_reduced,
        'expected_c4_form': expected_c4_form,
        'residual_vs_c4_form': residual_vs_c4_form,
        'reduces_to_c4_form_exactly': residual_vs_c4_form == 0,
        'mass_density_after_dividing_by_c2': mass_density_from_conversion,
        'code_mass_density_form': code_mass_density_form,
        'residual_vs_code_form': residual_vs_code_form,
        'energy_to_mass_conversion_reconciles_exactly': residual_vs_code_form == 0,
    }


# ---------------------------------------------------------------------
# 3. Code's own internal identity: rho_Planck*(l_P/L_H)^2 = c^2/(G*L_H^2)
# ---------------------------------------------------------------------

def verify_code_internal_identity():
    """cosmo_constant.py's own comment asserts
    rho_Planck*(l_P/L_H)^2 = c^2/(G*L_H^2) with rho_Planck = c^5/(hbar*G^2)
    and l_P^2 = hbar*G/c^3. Never independently checked before -- do so
    here."""
    hbar, c, G_sym, L_H = sp.symbols('hbar c G L_H', positive=True)
    rho_planck = c**5 / (hbar * G_sym**2)
    lP2 = hbar * G_sym / c**3

    lhs = sp.simplify(rho_planck * (lP2 / L_H**2))
    rhs = c**2 / (G_sym * L_H**2)
    residual = sp.simplify(lhs - rhs)

    return {
        'lhs_rho_planck_times_ratio_squared': lhs,
        'rhs_code_formula': rhs,
        'residual': residual,
        'code_internal_identity_confirmed': residual == 0,
    }


# ---------------------------------------------------------------------
# 4. Precise numerical recomputation of rho_CKN, rho_Lambda, and the ratio
# ---------------------------------------------------------------------

def compute_precise_ratio():
    """Recompute rho_CKN and rho_Lambda_obs directly from the SAME
    constants already used elsewhere in this project (sudoku_engine.py),
    to confirm whether 'factor 12' survives at full precision -- not
    re-cited from the earlier script's own printed value."""
    L_H = C / H_0                                    # m
    RHO_CKN = C**2 / (G * L_H**2)                     # kg/m^3, mass density

    RHO_CRIT = 3.0 * H_0**2 / (8.0 * math.pi * G)     # kg/m^3
    OMEGA_LAMBDA = 0.6847                             # Planck 2018
    RHO_LAMBDA_OBS = OMEGA_LAMBDA * RHO_CRIT           # kg/m^3

    ratio = RHO_CKN / RHO_LAMBDA_OBS

    # Cross-check via the rho_Planck*(l_P/L_H)^2 route (should match
    # RHO_CKN exactly, per Step 3's confirmed identity)
    RHO_PLANCK = C**5 / (HBAR * G**2)
    RHO_CKN_VIA_PLANCK_ROUTE = RHO_PLANCK * (L_P / L_H)**2
    cross_check_residual = abs(RHO_CKN - RHO_CKN_VIA_PLANCK_ROUTE) / RHO_CKN

    # What the ENERGY-density form would give if used directly WITHOUT
    # the c^2 conversion (the literal misreading Part 54's prose invites)
    L_EFF = math.sqrt(L_P * L_H)
    RHO_CKN_ENERGY_DENSITY_MISREAD = HBAR * C / L_EFF**4   # J/m^3, wrong units
    # if mistakenly compared directly to a mass density:
    misread_ratio_vs_rho_lambda = RHO_CKN_ENERGY_DENSITY_MISREAD / RHO_LAMBDA_OBS

    return {
        'L_H_m': L_H,
        'RHO_CKN_kg_m3': RHO_CKN,
        'RHO_LAMBDA_OBS_kg_m3': RHO_LAMBDA_OBS,
        'ratio_ckn_over_lambda': ratio,
        'RHO_CKN_via_planck_route': RHO_CKN_VIA_PLANCK_ROUTE,
        'cross_check_relative_residual': cross_check_residual,
        'cross_check_passes': cross_check_residual < 1e-12,
        'RHO_CKN_energy_density_if_misread_J_m3': RHO_CKN_ENERGY_DENSITY_MISREAD,
        'misread_ratio_if_c2_conversion_skipped': misread_ratio_vs_rho_lambda,
        'misread_ratio_is_c2_times_correct_ratio': abs(
            misread_ratio_vs_rho_lambda / ratio - C**2) / C**2 < 1e-9,
    }


# ---------------------------------------------------------------------
# Sudoku consistency check -- 10 tests
# ---------------------------------------------------------------------

def run_sudoku_checks(s1, s2, s3, s4):
    checks = []

    def add(label, computed, expected_desc, passed):
        checks.append({'label': label, 'computed': computed,
                        'expected': expected_desc,
                        'pass': (None if passed is None else bool(passed))})

    add('S1: hbar*c/(l_P^2*L_H^2) has dimensions of ENERGY density',
        s1['dim_of_hbar_c_over_L4'], 'energy/length^3',
        s1['formula1_is_energy_density'])
    add('S2: c^2/(G*L_H^2) has dimensions of MASS density',
        s1['dim_of_c2_over_GL2'], 'mass/length^3',
        s1['formula2_is_mass_density'])
    add('S3: the two formulas differ by exactly a factor of c^2 dimensionally',
        s1['ratio_of_the_two_dimensions'], 'c^2',
        s1['ratio_equals_c_squared_dimension'])
    add('S4: energy-density form reduces exactly to c^4/(G*L_H^2) under l_P^2=hbar*G/c^3',
        s2['residual_vs_c4_form'], '0 (exact)',
        s2['reduces_to_c4_form_exactly'])
    add('S5: dividing by c^2 (energy->mass) reconciles EXACTLY with the code formula',
        s2['residual_vs_code_form'], '0 (exact)',
        s2['energy_to_mass_conversion_reconciles_exactly'])
    add("S6: code's own internal identity rho_Planck*(l_P/L_H)^2=c^2/(G*L_H^2) confirmed",
        s3['residual'], '0 (exact)', s3['code_internal_identity_confirmed'])
    add('S7: two independent routes to RHO_CKN (direct vs via rho_Planck) agree to <1e-12',
        s4['cross_check_relative_residual'], '< 1e-12',
        s4['cross_check_passes'])
    add('S8: recomputed rho_CKN matches the previously-cited 7.1e-26 kg/m^3 to 2 sig figs',
        s4['RHO_CKN_kg_m3'], '~7.1e-26',
        abs(s4['RHO_CKN_kg_m3'] - 7.1e-26) / 7.1e-26 < 0.02)
    add('S9: ratio rho_CKN/rho_Lambda is within the previously-cited "~12" ballpark',
        s4['ratio_ckn_over_lambda'], '~12',
        11.0 < s4['ratio_ckn_over_lambda'] < 13.0)
    add('S10: the literal-misread (energy density, no c^2 conversion) ratio is '
        'exactly c^2 times too large -- confirms this IS the source of the '
        'apparent discrepancy, not a separate error',
        s4['misread_ratio_if_c2_conversion_skipped'],
        'c^2 * correct_ratio',
        s4['misread_ratio_is_c2_times_correct_ratio'])

    n_pass = sum(1 for c in checks if c['pass'] is True)
    n_fail = sum(1 for c in checks if c['pass'] is False)
    n_na = sum(1 for c in checks if c['pass'] is None)
    return checks, n_pass, n_fail, n_na


def main():
    print("=" * 78)
    print("T71 / Part 152 -- CKN 'factor 12' formula discrepancy audit")
    print("=" * 78)

    print("\n--- Step 1: dimensional check (sympy.physics.units) ---")
    s1 = verify_dimensional_mismatch()
    print(f"  dim[hbar*c/(l_P^2*L_H^2)] = {s1['dim_of_hbar_c_over_L4']} "
          f"(energy density: {s1['formula1_is_energy_density']})")
    print(f"  dim[c^2/(G*L_H^2)] = {s1['dim_of_c2_over_GL2']} "
          f"(mass density: {s1['formula2_is_mass_density']})")
    print(f"  ratio of dimensions = {s1['ratio_of_the_two_dimensions']} "
          f"(= c^2: {s1['ratio_equals_c_squared_dimension']})")

    print("\n--- Step 2: algebraic reconciliation ---")
    s2 = verify_algebraic_reconciliation()
    print(f"  hbar*c/(l_P^2*L_H^2) reduces to: {s2['energy_density_form_reduced']}")
    print(f"  residual vs c^4/(G*L_H^2): {s2['residual_vs_c4_form']} "
          f"(exact match: {s2['reduces_to_c4_form_exactly']})")
    print(f"  divided by c^2: {s2['mass_density_after_dividing_by_c2']}")
    print(f"  residual vs code's c^2/(G*L_H^2): {s2['residual_vs_code_form']} "
          f"(reconciles: {s2['energy_to_mass_conversion_reconciles_exactly']})")

    print("\n--- Step 3: code's own internal identity check ---")
    s3 = verify_code_internal_identity()
    print(f"  rho_Planck*(l_P/L_H)^2 = {s3['lhs_rho_planck_times_ratio_squared']}")
    print(f"  residual vs c^2/(G*L_H^2): {s3['residual']} "
          f"(confirmed: {s3['code_internal_identity_confirmed']})")

    print("\n--- Step 4: precise numerical recomputation ---")
    s4 = compute_precise_ratio()
    print(f"  L_H = {s4['L_H_m']:.6e} m")
    print(f"  rho_CKN = {s4['RHO_CKN_kg_m3']:.6e} kg/m^3")
    print(f"  rho_Lambda_obs = {s4['RHO_LAMBDA_OBS_kg_m3']:.6e} kg/m^3")
    print(f"  ratio = {s4['ratio_ckn_over_lambda']:.4f}")
    print(f"  cross-check (via rho_Planck route): {s4['RHO_CKN_via_planck_route']:.6e} kg/m^3 "
          f"(relative residual: {s4['cross_check_relative_residual']:.3e})")
    print(f"  literal energy-density misread: {s4['RHO_CKN_energy_density_if_misread_J_m3']:.6e} J/m^3")
    print(f"  misread ratio (if c^2 conversion skipped): {s4['misread_ratio_if_c2_conversion_skipped']:.6e}")
    print(f"  misread ratio == c^2 * correct ratio: {s4['misread_ratio_is_c2_times_correct_ratio']}")

    print("\n--- Sudoku Consistency Check ---")
    checks, n_pass, n_fail, n_na = run_sudoku_checks(s1, s2, s3, s4)
    for c in checks:
        status = 'PASS' if c['pass'] is True else ('FAIL' if c['pass'] is False else 'N/A')
        print(f"[{status}] {c['label']}")
        print(f"       computed: {c['computed']}")
        print(f"       expected: {c['expected']}")

    print(f"\nScorecard: {n_pass} PASS, {n_fail} FAIL, {n_na} N/A "
          f"out of {len(checks)} checks")


if __name__ == '__main__':
    main()
