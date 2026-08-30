#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
t66_rotation_field_tetrad.py -- TODO_04 T66 (Step 1 of the approved plan)
=======================================================================
Gate check for T66: does promoting PDTP's scalar phase field phi(x) to a
local rotation field R(x) in SO(2) -- as literally proposed in the source
note (R(theta) = [[cos, -sin],[sin, cos]], a single angle theta(x)) --
add any new structure to the framework?

Established math used (cited, not re-derived): SO(2) is a 1-dimensional
Lie group (dim SO(n) = n(n-1)/2, the antisymmetric-generator count).
Source: Wikipedia, "Orthogonal group" / "Rotation group SO(3)", and any
standard Lie-group text (e.g. Hall, "Lie Groups, Lie Algebras, and
Representations", 2015).

PDTP Original: the APPLICATION of this fact to T66's specific question --
does R(theta(x)) with theta(x)=phi(x) (the note's literal construction)
carry more information than phi(x) alone? -- and the consequence chain
for Key Questions 1-4 that follows from the answer.

Output: DATA only. Interpretation in docs/research/rotation_field_gate_check.md.
"""

import sympy as sp


def verify_so2_is_u1_representation():
    """Verify R(theta) is a faithful 1-parameter representation of U(1):
    R(a)*R(b) = R(a+b) [group homomorphism], R(theta)^T*R(theta)=I
    [orthogonal], det(R(theta))=1 [special], eigenvalues = exp(+-i*theta)
    [matches the standard SO(2)-U(1) isomorphism]. All checked as exact
    SymPy identities (residual = 0), not numerically."""
    a, b, theta = sp.symbols('a b theta', real=True)

    def R(t):
        return sp.Matrix([[sp.cos(t), -sp.sin(t)], [sp.sin(t), sp.cos(t)]])

    homomorphism_residual = sp.simplify(R(a) * R(b) - R(a + b))
    orthogonality_residual = sp.simplify(R(theta).T * R(theta) - sp.eye(2))
    det_val = sp.simplify(R(theta).det())
    trace_val = sp.simplify(R(theta).trace())

    # Vieta's formulas: a matrix's eigenvalues are the roots of
    # lambda^2 - trace*lambda + det = 0. Separately, Euler's formula gives
    # exp(i*theta) + exp(-i*theta) = 2*cos(theta) and exp(i*theta)*exp(-i*theta)
    # = 1 EXACTLY. trace(R)=2*cos(theta) and det(R)=1 (both just verified
    # above) therefore uniquely force R(theta)'s eigenvalues to be
    # {exp(i*theta), exp(-i*theta)} -- this is a complete proof via Vieta's
    # formulas, without needing SymPy to symbolically collapse a sqrt-vs-exp
    # expression (which it does not do automatically).
    eigenvals_match = (trace_val == 2 * sp.cos(theta)) and (det_val == 1)

    return {
        'homomorphism_residual': homomorphism_residual,
        'homomorphism_holds': homomorphism_residual == sp.zeros(2, 2),
        'orthogonality_residual': orthogonality_residual,
        'orthogonality_holds': orthogonality_residual == sp.zeros(2, 2),
        'det': det_val,
        'det_is_one': det_val == 1,
        'trace': trace_val,
        'eigenvalues_match_exp_i_theta': eigenvals_match,
    }


def derive_so_n_dimension(n):
    """Derive dim(SO(n)) FROM the antisymmetry constraint on the Lie
    algebra so(n) = {A : A^T = -A}, by literally constructing the most
    general n x n antisymmetric matrix and counting its free parameters --
    not just quoting the n(n-1)/2 formula."""
    entries = {}
    A = sp.zeros(n, n)
    free_syms = []
    for i in range(n):
        for j in range(i + 1, n):
            s = sp.Symbol(f'a_{i}{j}')
            free_syms.append(s)
            A[i, j] = s
            A[j, i] = -s
    antisymmetry_residual = sp.simplify(A.T + A)
    return {
        'n': n,
        'generator_matrix': A,
        'num_free_parameters': len(free_syms),
        'formula_n(n-1)/2': n * (n - 1) // 2,
        'matches_formula': len(free_syms) == n * (n - 1) // 2,
        'antisymmetry_holds': antisymmetry_residual == sp.zeros(n, n),
    }


def verify_r_theta_is_lossless_relabeling():
    """The note's literal construction sets theta(x) = phi(x) -- i.e. R(x)
    is built FROM the existing scalar field, not from new independent data.
    Verify the round-trip phi -> R(phi) -> angle(R) recovers phi exactly
    via atan2 inversion, proving zero information is gained or lost.
    SymPy's symbolic simplify does not auto-collapse atan2(sin(phi),cos(phi))
    to phi (a genuine branch-cut subtlety, not a bug) -- so this is checked
    numerically over a fine sweep of phi covering a full period, which is
    the mathematically appropriate way to verify an identity that holds
    piecewise/by branch rather than as a single global symbolic simplification."""
    import math
    phi = sp.symbols('phi', real=True)
    R_phi = sp.Matrix([[sp.cos(phi), -sp.sin(phi)], [sp.sin(phi), sp.cos(phi)]])
    recovered_phi_expr = sp.atan2(R_phi[1, 0], R_phi[0, 0])

    n_samples = 200
    max_abs_error = 0.0
    for i in range(n_samples):
        phi_val = -math.pi + 2 * math.pi * i / n_samples  # sweep (-pi, pi], the atan2 principal range
        recovered = math.atan2(math.sin(phi_val), math.cos(phi_val))
        max_abs_error = max(max_abs_error, abs(recovered - phi_val))

    return {
        'R_phi': R_phi,
        'recovered_phi_expr': recovered_phi_expr,
        'n_samples_checked': n_samples,
        'max_abs_error_over_sweep': max_abs_error,
        'roundtrip_exact': max_abs_error < 1e-10,
    }


def verify_lagrangian_unchanged_under_relabeling():
    """Substitute phi(x) -> angle(R(x)) [= phi(x) exactly, per the previous
    check] into the PDTP coupling term g*cos(psi-phi) and confirm the
    expression is literally unchanged -- so every downstream single-phase
    result (Newtonian limit, GR recovery Part 98/101, PPN Part 112) that
    was already derived from g*cos(psi-phi) carries over with ZERO new
    derivation required, because the substitution is the identity map."""
    psi, phi, g = sp.symbols('psi phi g', real=True)
    L_original = g * sp.cos(psi - phi)

    R_phi = sp.Matrix([[sp.cos(phi), -sp.sin(phi)], [sp.sin(phi), sp.cos(phi)]])
    angle_from_R = sp.atan2(R_phi[1, 0], R_phi[0, 0])
    L_via_R = g * sp.cos(psi - angle_from_R)

    residual = sp.simplify(L_original - L_via_R)
    return {
        'L_original': L_original,
        'L_via_R': L_via_R,
        'residual': residual,
        'lagrangian_identical': residual == 0,
    }


def compare_dof_counts():
    """RECHECK-style comparison table: how many independent scalar degrees
    of freedom does each candidate structure actually carry per lattice
    site? Computed from derive_so_n_dimension(), not hardcoded."""
    u1_scalar_dof = 1  # phi(x), established, Part 1
    so2_result = derive_so_n_dimension(2)
    so2_literal_dof = so2_result['num_free_parameters']  # the note's literal proposal
    so3_result = derive_so_n_dimension(3)
    so3_hypothetical_dof = so3_result['num_free_parameters']  # NOT proposed by the note; for context only
    su3_part84_dof = 8  # Part 37/75/84, established in the project

    return {
        'u1_scalar_phi': u1_scalar_dof,
        'so2_literal_note_proposal': so2_literal_dof,
        'so2_equals_u1': so2_literal_dof == u1_scalar_dof,
        'so3_hypothetical_independent_field': so3_hypothetical_dof,
        'su3_part84_emergent_metric': su3_part84_dof,
        'so2_below_su3_by': su3_part84_dof - so2_literal_dof,
        'so3_hypothetical_below_su3_by': su3_part84_dof - so3_hypothetical_dof,
    }


def main():
    print("=" * 78)
    print("T66 Step 1: Rotation-Field Gate Check -- Is R(x) New Structure?")
    print("=" * 78)

    r1 = verify_so2_is_u1_representation()
    print("\n[1] SO(2) is a faithful representation of U(1):")
    print(f"    Homomorphism R(a)R(b)=R(a+b): residual={r1['homomorphism_residual'].tolist()}, "
          f"holds={r1['homomorphism_holds']}")
    print(f"    Orthogonality R^T R = I: holds={r1['orthogonality_holds']}")
    print(f"    det(R(theta)) = {r1['det']} (special): {r1['det_is_one']}")
    print(f"    trace(R(theta)) = {r1['trace']}; by Vieta's formulas this forces "
          f"eigenvalues = exp(+-i*theta): {r1['eigenvalues_match_exp_i_theta']}")

    print("\n[2] Lie algebra dimension count (derived from antisymmetry, not quoted):")
    for n in (2, 3):
        r2 = derive_so_n_dimension(n)
        print(f"    dim(so({n})) = {r2['num_free_parameters']} free params "
              f"(formula n(n-1)/2 = {r2['formula_n(n-1)/2']}); match={r2['matches_formula']}; "
              f"antisymmetry holds={r2['antisymmetry_holds']}")

    r3 = verify_r_theta_is_lossless_relabeling()
    print(f"\n[3] Round-trip phi -> R(phi) -> angle(R), {r3['n_samples_checked']} samples over (-pi,pi]:")
    print(f"    max |recovered - original| = {r3['max_abs_error_over_sweep']:.2e}, "
          f"exact={r3['roundtrip_exact']}")

    r4 = verify_lagrangian_unchanged_under_relabeling()
    print(f"\n[4] Lagrangian g*cos(psi-phi) under phi->angle(R(phi)) substitution:")
    print(f"    residual = {r4['residual']}, identical = {r4['lagrangian_identical']}")

    r5 = compare_dof_counts()
    print(f"\n[5] DOF comparison table:")
    print(f"    U(1) scalar phi(x)                    : {r5['u1_scalar_phi']} DOF")
    print(f"    SO(2) R(x), literal note proposal      : {r5['so2_literal_note_proposal']} DOF "
          f"(equals U(1): {r5['so2_equals_u1']})")
    print(f"    SO(3) independent field (hypothetical, NOT proposed by the note): {r5['so3_hypothetical_independent_field']} DOF")
    print(f"    SU(3) Part 84 emergent metric (established): {r5['su3_part84_emergent_metric']} DOF")
    print(f"    SO(2) literal proposal falls short of Part 84 by: {r5['so2_below_su3_by']} DOF")
    print(f"    SO(3) hypothetical falls short of Part 84 by: {r5['so3_hypothetical_below_su3_by']} DOF")

    all_pass = (r1['homomorphism_holds'] and r1['orthogonality_holds'] and r1['det_is_one']
                and r1['eigenvalues_match_exp_i_theta'] and r3['roundtrip_exact']
                and r4['lagrangian_identical'] and r5['so2_equals_u1'])
    print(f"\nAll checks consistent with the gate-check conclusion: {all_pass}")


if __name__ == '__main__':
    main()
