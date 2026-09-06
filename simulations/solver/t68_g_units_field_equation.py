"""
T68 (g-units audit), Part 33/94/95/128 pass -- independent SymPy dimensional
check of the field equation box(phi) = g*sin(psi-phi).

Checks, independently, what [g] the field equation requires in full SI
dimensional analysis (kg, m, s as base dimensions), WITHOUT assuming Part
128's own shortcut ("c already folds space into time"). Compares against
Part 94's g = omega_gap = m_cond*c^2/hbar.

Output DATA only -- interpretation lives in docs/research/g_units_audit_scoping.md.
"""

import sympy as sp


def dalembertian_dimension_check():
    """Derive [box(phi)] from the standard relativistic wave operator,
    box = (1/c^2) d^2/dt^2 - Laplacian, with x in meters and t in seconds,
    for a DIMENSIONLESS field phi. Does NOT assume the two terms already
    match -- verifies it."""
    c, t, x = sp.symbols('c t x', positive=True)
    phi = sp.Function('phi')(t, x)

    # symbolic dimension bookkeeping via unit placeholders (mass=1 dummy,
    # since phi is dimensionless -- only length/time dimensions matter here)
    L, T = sp.symbols('L T', positive=True)  # stand-ins for [length], [time]

    # d^2 phi/dt^2 : phi dimensionless, t has dim T -> result has dim T^-2
    d2phi_dt2_dim = T**-2
    # (1/c^2): c has dim L/T -> c^2 has dim L^2/T^2 -> 1/c^2 has dim T^2/L^2
    inv_c2_dim = T**2 / L**2
    term1_dim = sp.simplify(inv_c2_dim * d2phi_dt2_dim)  # should be 1/L^2

    # Laplacian d^2 phi/dx^2 : phi dimensionless, x has dim L -> dim L^-2
    term2_dim = L**-2

    match = sp.simplify(term1_dim - term2_dim) == 0
    return {
        'term1_dim_time_part_times_invc2': term1_dim,
        'term2_dim_spatial_laplacian': term2_dim,
        'terms_match': match,
        'box_phi_dimension': term1_dim,  # = 1/L^2 if match
    }


def g_dimension_from_field_equation(box_phi_dim):
    """[g] = [box(phi)] / [sin(...)] = [box(phi)] since sin is dimensionless."""
    return box_phi_dim  # sin(psi-phi) is dimensionless


def omega_gap_dimension():
    """[omega_gap] = [m_cond * c^2 / hbar], independently, SI."""
    M, L, T = sp.symbols('M L T', positive=True)  # mass, length, time
    m_cond_dim = M
    c2_dim = (L / T) ** 2
    hbar_dim = M * L**2 / T  # J*s = kg*m^2/s
    omega_gap_dim = sp.simplify(m_cond_dim * c2_dim / hbar_dim)
    return omega_gap_dim  # expect 1/T


def compare_conventions():
    L, T = sp.symbols('L T', positive=True)
    box_result = dalembertian_dimension_check()
    g_field_eq_dim = g_dimension_from_field_equation(box_result['box_phi_dimension'])
    omega_gap_dim = omega_gap_dimension()

    # Express omega_gap^2 in the same L,T symbols for comparison
    omega_gap_sq_dim = sp.simplify(omega_gap_dim ** 2)  # expect 1/T^2

    # Candidate reconciliation: omega_gap^2 / c^2 (c^2 has dim L^2/T^2)
    c2_dim = (L / T) ** 2
    reconciled_dim = sp.simplify(omega_gap_sq_dim / c2_dim)

    return {
        'box_phi_dim': box_result['box_phi_dimension'],       # 1/L^2 (SI-correct)
        'terms_of_box_match': box_result['terms_match'],
        'g_required_by_field_eq': g_field_eq_dim,              # 1/L^2
        'omega_gap_dim': omega_gap_dim,                        # 1/T  (Part 94)
        'omega_gap_squared_dim': omega_gap_sq_dim,             # 1/T^2 (Part 128's claimed fix)
        'omega_gap_squared_over_c2_dim': reconciled_dim,       # 1/L^2 (proposed reconciliation)
        'part128_claim_matches_field_eq': sp.simplify(
            omega_gap_sq_dim - g_field_eq_dim) == 0,           # False if dims differ (1/T^2 vs 1/L^2)
        'reconciled_matches_field_eq': sp.simplify(
            reconciled_dim - g_field_eq_dim) == 0,             # True: 1/L^2 == 1/L^2
    }


if __name__ == "__main__":
    r = compare_conventions()
    print("=" * 74)
    print("T68 g-units check: box(phi) = g*sin(psi-phi), full SI dimensional analysis")
    print("=" * 74)
    print()
    print("Both terms of box(phi) match dimensionally:", r['terms_of_box_match'])
    print("[box(phi)] required by field equation      :", r['box_phi_dim'], "(length^-2)")
    print("[g] required by field equation              :", r['g_required_by_field_eq'])
    print()
    print("[omega_gap] (Part 94, m_cond*c^2/hbar)      :", r['omega_gap_dim'], "(time^-1)")
    print("[omega_gap^2] (Part 128's claimed fix)      :", r['omega_gap_squared_dim'], "(time^-2)")
    print("[omega_gap^2 / c^2] (reconciliation attempt):", r['omega_gap_squared_over_c2_dim'])
    print()
    print("Does Part 128's omega_gap^2 match the field-eq requirement (1/L^2)? ->",
          r['part128_claim_matches_field_eq'])
    print("Does omega_gap^2/c^2 match the field-eq requirement (1/L^2)?        ->",
          r['reconciled_matches_field_eq'])
