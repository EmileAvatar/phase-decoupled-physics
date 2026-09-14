"""
T77 (TODO_04.md), Part 145 -- Timeflow Gravity (Trofimov 2026, Class.
Quantum Grav. 43 135020) structural comparison vs PDTP.

Before building any comparison narrative on top of Timeflow Gravity's
(TFG's) own claims, this script independently re-derives TFG's own key
algebraic steps -- exactly the discipline CLAUDE.md demands of any
external claim used as a load-bearing comparison point, extended here
to a real peer-reviewed paper rather than an AI review.

Verified here (all TFG's own equations, cited by number from the paper):
1. Eq 86 -> 87: the speed-of-light factor cancels from the equilibrium
   function mu(a, a0, theta).
2. Eq 87 -> 88: the coherent limit (cos(theta) -> 1) reduces mu exactly
   to Milgrom's simple MOND interpolating function a/(a+a0).
3. Eq 89 -> 90: the deep-MOND limit (a << a0) gives the standard MOND
   scaling relation a = sqrt(gN * a0).
4. Eq 99: the topological partition f_order = 1/pi (trivial arithmetic,
   flagged separately in the write-up as a MODELING CHOICE -- diameter
   vs circumference -- not a theorem, regardless of the arithmetic
   being correct).
5. Eq 133 -> 137 -> 138: the dark-energy equation-of-state derivation,
   from the continuity equation through to the numeric w(1) ~= -0.84
   figure compared against DESI's w0 = -0.838 +- 0.055.

Output DATA only -- interpretation and the PDTP comparison live in
docs/research/timeflow_gravity_comparison.md.
"""

import sympy as sp

# ---------------------------------------------------------------------
# 1-2. MOND-limit reduction (Eq 86 -> 87 -> 88)
# ---------------------------------------------------------------------

def verify_mond_reduction():
    a, a0, c, theta = sp.symbols('a a0 c theta', positive=True)

    # Eq 86, as written in the paper
    mu_86 = ((a/c)**2 + (a/c)*(a0/c)*sp.cos(theta)) / \
            ((a/c)**2 + (a0/c)**2 + 2*(a/c)*(a0/c)*sp.cos(theta))

    # Eq 87, claimed c-independent form
    mu_87 = (a**2 + a*a0*sp.cos(theta)) / (a**2 + a0**2 + 2*a*a0*sp.cos(theta))

    residual_86_87 = sp.simplify(mu_86 - mu_87)

    # Eq 88: coherent limit cos(theta) -> 1
    mu_88_from_87 = sp.simplify(mu_87.subs(theta, 0))
    mu_88_claimed = a / (a + a0)
    residual_87_88 = sp.simplify(mu_88_from_87 - mu_88_claimed)

    return {
        'residual_86_to_87': residual_86_87,
        'c_cancels_exactly': residual_86_87 == 0,
        'mu_88_computed': mu_88_from_87,
        'residual_87_to_88': residual_87_88,
        'coherent_limit_is_milgrom_form': residual_87_88 == 0,
    }


# ---------------------------------------------------------------------
# 3. Deep-MOND limit (Eq 89 -> 90)
# ---------------------------------------------------------------------

def verify_deep_mond_limit():
    a, a0, gN = sp.symbols('a a0 gN', positive=True)

    mu_87_cos1 = a / (a + a0)  # Eq 88, exact coherent-limit form

    # Eq 89: leading behavior as a -> 0 (a << a0), i.e. series in a
    mu_89_series = sp.series(mu_87_cos1, a, 0, 2).removeO()
    mu_89_claimed = a / a0
    residual_89 = sp.simplify(mu_89_series - mu_89_claimed)

    # Eq 90: gN = a*mu (deep limit) => gN = a^2/a0 => a = sqrt(gN*a0)
    gN_expr = a * mu_89_claimed  # gN = a * (a/a0)
    a_solved = sp.solve(sp.Eq(gN, gN_expr), a)
    a_solved_positive = [s for s in a_solved if s.is_positive or True]
    a_expected = sp.sqrt(gN * a0)
    residual_90 = sp.simplify(sp.sqrt(gN * a0) - sp.sqrt(gN_expr.subs(a, sp.sqrt(gN*a0))**0 * gN*a0))

    # Direct check: does a = sqrt(gN*a0) satisfy gN = a^2/a0 identically?
    check_90 = sp.simplify((sp.sqrt(gN*a0))**2 / a0 - gN)

    return {
        'mu_89_series': mu_89_series,
        'residual_89_vs_claimed': residual_89,
        'deep_limit_matches': residual_89 == 0,
        'a_solutions_from_gN_eq': a_solved,
        'a_expected_sqrt_gN_a0': a_expected,
        'check_90_residual': check_90,
        'deep_mond_scaling_confirmed': check_90 == 0,
    }


# ---------------------------------------------------------------------
# 4. Topological partition (Eq 99) -- arithmetic check only
# ---------------------------------------------------------------------

def verify_topological_partition():
    A0 = sp.symbols('A0', positive=True)
    C_total = 2 * sp.pi * A0   # Eq 97
    C_order = 2 * A0           # Eq 98
    f_order = sp.simplify(C_order / C_total)
    f_order_claimed = 1 / sp.pi
    residual = sp.simplify(f_order - f_order_claimed)

    return {
        'f_order_computed': f_order,
        'residual_vs_1_over_pi': residual,
        'arithmetic_correct': residual == 0,
        'numeric_value': float(f_order_claimed.evalf()),
        'note': 'Arithmetic is trivially correct given C_order=2*A0 and '
                'C_total=2*pi*A0 -- but WHY the coherent sector is measured '
                'by the diameter (2*A0) and the total by the circumference '
                '(2*pi*A0) is a MODELING CHOICE (Section 8, "the rank-one '
                'form is invariant under u->-u, so this axis is a diameter"), '
                'not a theorem forced by the field equations alone. Flagged, '
                'not re-derived, in the comparison doc.',
    }


# ---------------------------------------------------------------------
# 5. Dark energy equation of state (Eq 133 -> 137 -> 138)
# ---------------------------------------------------------------------

def verify_w_of_a():
    a, H, rho_c0 = sp.symbols('a H rho_c0', positive=True)
    pi = sp.pi

    # Eq 121: rho_vac(a)/rho_c0 = 1 - a/pi
    rho_vac_over_rho_c0 = 1 - a/pi
    rho_vac = rho_c0 * rho_vac_over_rho_c0

    # Eq 134: rho_dot_vac = d(rho_vac)/da * a_dot, with a_dot = a*H
    drho_da = sp.diff(rho_vac, a)
    rho_dot = sp.simplify(drho_da * a * H)
    rho_dot_claimed = -rho_c0/pi * a * H
    residual_134 = sp.simplify(rho_dot - rho_dot_claimed)

    # Eq 133 continuity: rho_dot + 3H(rho_vac + P_vac) = 0
    # => rho_vac + P_vac = -rho_dot / (3H)
    rho_plus_P = sp.simplify(-rho_dot / (3*H))
    rho_plus_P_claimed = rho_c0/(3*pi) * a
    residual_136 = sp.simplify(rho_plus_P - rho_plus_P_claimed)

    # Eq 137: w(a) = P_vac/rho_vac = (rho_vac+P_vac)/rho_vac - 1
    w_a = sp.simplify(rho_plus_P / rho_vac - 1)
    w_a_claimed = a / (3*(pi - a)) - 1
    residual_137 = sp.simplify(w_a - w_a_claimed)

    # Eq 138: numeric value at a=1
    w_1 = float(w_a_claimed.subs(a, 1).evalf())

    return {
        'rho_dot': rho_dot,
        'residual_134': residual_134,
        'rho_plus_P': sp.simplify(rho_plus_P),
        'residual_136': residual_136,
        'w_a_computed': sp.simplify(w_a),
        'w_a_claimed': w_a_claimed,
        'residual_137': residual_137,
        'w_of_a_derivation_confirmed': residual_137 == 0,
        'w_1_computed': w_1,
        'w_1_paper_claim': -0.84,
        'desi_w0_measured': -0.838,
        'desi_w0_uncertainty': 0.055,
        'w_1_within_desi_1sigma': abs(w_1 - (-0.838)) < 0.055,
    }


def main():
    print("=" * 78)
    print("T77 / Part 145 -- Timeflow Gravity: independent verification of "
          "the paper's own key equations")
    print("=" * 78)

    print("\n--- MOND-limit reduction (Eq 86 -> 87 -> 88) ---")
    r1 = verify_mond_reduction()
    for k, v in r1.items():
        print(f"  {k}: {v}")

    print("\n--- Deep-MOND limit (Eq 89 -> 90) ---")
    r2 = verify_deep_mond_limit()
    for k, v in r2.items():
        print(f"  {k}: {v}")

    print("\n--- Topological partition (Eq 99) ---")
    r3 = verify_topological_partition()
    for k, v in r3.items():
        print(f"  {k}: {v}")

    print("\n--- Dark energy w(a) derivation (Eq 133 -> 137 -> 138) ---")
    r4 = verify_w_of_a()
    for k, v in r4.items():
        print(f"  {k}: {v}")

    print("\n--- Summary ---")
    all_confirmed = (r1['c_cancels_exactly'] and r1['coherent_limit_is_milgrom_form']
                      and r2['deep_limit_matches'] and r2['deep_mond_scaling_confirmed']
                      and r3['arithmetic_correct'] and r4['w_of_a_derivation_confirmed'])
    print(f"All checked TFG derivation steps confirmed: {all_confirmed}")
    print(f"w(1) computed = {r4['w_1_computed']:.4f}, within DESI 1-sigma: "
          f"{r4['w_1_within_desi_1sigma']}")


if __name__ == '__main__':
    main()
