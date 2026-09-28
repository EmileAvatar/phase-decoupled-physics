#!/usr/bin/env python3
"""
t83b_jeans_correction.py -- T83 sub-task 83b: two-phase Jeans eigenvalue
=========================================================================
Filed and worked by CLAUDE OPUS 5.5 (2026-09-28). Part 154.

GOAL:
    Re-derive the linearised two-phase dynamics independently of any
    change of variables, and locate the source of the Part 61 value
    lambda = +/- 2*sqrt(2)*g.
      Route 1: original fields (psi, phi_b, phi_s), all unit inertia, so
               x_tt = -Hess(V) x with no bookkeeping.
      Route 2: (Theta = psi - phi_+, phi_-) with the inertias that follow
               from the kinetic term (1 for psi, 2 for phi_+ and phi_-).
      Route 3: same as Route 2 but with every inertia set to 1 (the
               assumption implicit in two_phase_lagrangian.py L445-464).
    Also evaluate the linear dynamics at the Part 119 true vacuum.

EQUATIONS USED:
    Eq 1: L = 1/2(psi_t^2 + phi_b_t^2 + phi_s_t^2)
              + g cos(psi - phi_b) - g cos(psi - phi_s)
          Source: PDTP two-phase Lagrangian, Part 61 [ASSUMED]
    Eq 2: phi_+ = (phi_b + phi_s)/2, phi_- = (phi_b - phi_s)/2  (Part 61)
    Eq 3: Lagrange equations for q_i with L = 1/2 q^T K q_t - V(q):
          K q_tt = -grad V  ->  linearised q_tt = -K^-1 Hess(V) q
          Source: Goldstein, Classical Mechanics, Sec 6.2 (small oscillations)
    Eq 4: Wave form: each field obeys (d_t^2 - c^2 nabla^2) q = (force)/K,
          so a plane wave e^{i(kx - wt)} gives w^2 = c^2 k^2 - lambda,
          lambda an eigenvalue of -K^-1 Hess(V).

ASSUMPTIONS:
    [A1] Spatially uniform (k = 0) for the eigenvalues; Eq 4 restores k.
    [A2] Linearisation about the equilibrium used by Part 61
         (psi = phi_b = phi_s, i.e. Theta = 0, phi_- = 0) and about the
         Part 119 vacuum (Theta = pi/2, phi_- = pi/2).

SIGN CONVENTIONS:
    L = T - V, V = -L_int; x_tt = M x, eigenvalue lambda > 0 -> growth
    (sigma = sqrt(lambda)), lambda < 0 -> oscillation (omega = sqrt(-lambda)).

OUTPUT (data only):
    Matrices and eigenvalues from Routes 1-3, vacuum eigenvalues,
    dispersion branches, numerical cross-check, Sudoku scorecard.
"""

import os
import sys
import numpy as np
import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from print_utils import ReportWriter  # noqa: E402

g = sp.Symbol('g', positive=True)
psi, pb, ps = sp.symbols('psi phi_b phi_s', real=True)
th, pp, pm = sp.symbols('Theta phi_p phi_m', real=True)


def V_original():
    """V = -L_int in the original fields (Eq 1)."""
    return -(g * sp.cos(psi - pb) - g * sp.cos(psi - ps))


# =====================================================================
# DERIVATIONS
# =====================================================================

def derive_route1_original():
    """Unit inertias: M = -Hess(V) at psi = phi_b = phi_s = 0."""
    V = V_original()
    q = (psi, pb, ps)
    H = sp.hessian(V, q).subs({psi: 0, pb: 0, ps: 0})
    M = -H
    return {'M': M, 'eigs': M.eigenvals()}


def derive_mode_basis(inertia):
    """Routes 2/3. Fields (psi, phi_p, phi_m) with given inertias.
    L_int = g cos(psi - phi_p - phi_m) - g cos(psi - phi_p + phi_m)
    (Eq 2 substituted into Eq 1, no trig identity used)."""
    L_int = g * sp.cos(psi - pp - pm) - g * sp.cos(psi - pp + pm)
    a_psi = sp.diff(L_int, psi) / inertia[0]
    a_p = sp.diff(L_int, pp) / inertia[1]
    a_m = sp.diff(L_int, pm) / inertia[2]
    sub = {psi: th + pp}
    a_th = (a_psi - a_p).subs(sub)
    a_mm = a_m.subs(sub)
    return {'a_th': a_th, 'a_m': a_mm}


def linear_matrix(acc, point):
    """Jacobian of (Theta_tt, phi_m_tt) w.r.t. (Theta, phi_m) at point."""
    J = sp.Matrix([[sp.diff(acc['a_th'], v) for v in (th, pm)],
                   [sp.diff(acc['a_m'], v) for v in (th, pm)]])
    J = sp.simplify(J.subs(point))
    return {'M': J, 'eigs': J.eigenvals()}


def derive_kinetic_inertias():
    """Kinetic term 1/2(phi_b_t^2 + phi_s_t^2) with phi_b = p + m,
    phi_s = p - m: coefficients of p_t^2 and m_t^2 (should be 1 each,
    i.e. inertia 2 in the 1/2*I*q_t^2 convention)."""
    pt, mt = sp.symbols('p_t m_t', real=True)
    T = sp.Rational(1, 2) * ((pt + mt)**2 + (pt - mt)**2)
    T = sp.expand(T)
    return {'T': T, 'I_p': 2 * T.coeff(pt, 2), 'I_m': 2 * T.coeff(mt, 2),
            'cross': T.coeff(pt, 1).coeff(mt, 1)}


def derive_dispersion(lam_list):
    """Eq 4: omega^2 = c^2 k^2 - lambda for each eigenvalue."""
    c, k = sp.symbols('c k', positive=True)
    return [sp.expand(c**2 * k**2 - lam) for lam in lam_list]


def derive_newton3(inertia):
    """psi_tt + 2*phi_p_tt for the given inertias (Part 61 claims 0)."""
    L_int = g * sp.cos(psi - pp - pm) - g * sp.cos(psi - pp + pm)
    val = sp.diff(L_int, psi) / inertia[0] + 2 * sp.diff(L_int, pp) / inertia[1]
    return sp.simplify(val)


def verify_product_identity():
    """cos(A)-cos(B) = -2 sin((A+B)/2) sin((A-B)/2) (A&S 4.3.37) applied."""
    lhs = g * sp.cos(psi - pp - pm) - g * sp.cos(psi - pp + pm)
    rhs = 2 * g * sp.sin(psi - pp) * sp.sin(pm)
    return sp.simplify(sp.expand_trig(lhs - rhs))


# =====================================================================
# COMPUTATION
# =====================================================================

def compute_numeric_eigs(M_sym, g_val=1.0):
    """numpy eigenvalues of the Route 1 matrix at g = g_val."""
    Mn = np.array(M_sym.subs(g, g_val).tolist(), dtype=float)
    return np.sort(np.linalg.eigvals(Mn).real)


# =====================================================================
# SUDOKU
# =====================================================================

def run_sudoku_checks(r1, r2, r3, vac, kin, n3_ok, n3_bad, num, ident, disp_ratio):
    rows = []

    def add(tid, name, comp, exp, ok):
        rows.append((tid, name, str(comp), str(exp), 'MATCH' if ok else 'CONTRADICTION'))

    nz1 = sorted([e for e in r1['eigs'] if e != 0], key=lambda e: float(e.subs(g, 1)))
    e2 = sorted(r2['eigs'].keys(), key=lambda e: float(e.subs(g, 1)))
    e3 = sorted(r3['eigs'].keys(), key=lambda e: float(e.subs(g, 1)))
    part61 = sp.Matrix([[0, 4 * g], [2 * g, 0]])
    add('S1', 'Route 1 (original fields) nonzero eigenvalues', nz1,
        'equal Route 2', all(sp.simplify(a - b) == 0 for a, b in zip(nz1, e2)))
    add('S2', 'Route 2 vs Part 61 value +/-2sqrt(2)g', e2,
        [-2 * sp.sqrt(2) * g, 2 * sp.sqrt(2) * g],
        all(sp.simplify(a - b) == 0 for a, b in
            zip(e2, [-2 * sp.sqrt(2) * g, 2 * sp.sqrt(2) * g])))
    add('S3', 'Route 3 (all inertia 1) reproduces Part 61 matrix', r3['M'],
        part61, sp.simplify(r3['M'] - part61) == sp.zeros(2, 2))
    add('S4', 'Kinetic inertias of phi_+, phi_- (cross term)',
        (kin['I_p'], kin['I_m'], kin['cross']), (2, 2, 0),
        (kin['I_p'], kin['I_m'], kin['cross']) == (2, 2, 0))
    add('S5', 'Newton 3rd psi_tt+2phi_+tt, inertias (1,2,2)', n3_ok, 0, n3_ok == 0)
    add('S6', 'Newton 3rd psi_tt+2phi_+tt, inertias (1,1,1)', n3_bad, 0, n3_bad == 0)
    add('S7', 'Route 1 has one zero mode (joint shift)',
        r1['eigs'].get(0, 0), 1, r1['eigs'].get(0, 0) == 1)
    add('S8', 'numpy eigenvalues at g=1 vs sqrt(3)',
        np.round(num, 6).tolist(), round(float(np.sqrt(3)), 6),
        abs(max(num) / np.sqrt(3) - 1) < 1e-9)
    pos = [e for e in e2 if e.subs(g, 1) > 0]
    add('S9', 'Jeans: positive growth eigenvalue exists', pos, '> 0', len(pos) > 0)
    ev = list(vac['eigs'].keys())
    add('S10', 'Part 119 vacuum: all eigenvalues < 0 (stable)', ev, '< 0',
        all(e.subs(g, 1) < 0 for e in ev))
    add('S11', 'Product identity residual', ident, 0, ident == 0)
    add('S12', 'k_J(new)/k_J(old) = (sqrt3/(2sqrt2))^(1/2)',
        '{:.6f}'.format(disp_ratio),
        '{:.6f}'.format(float(sp.sqrt(sp.sqrt(3) / (2 * sp.sqrt(2))))),
        abs(disp_ratio - float(sp.sqrt(sp.sqrt(3) / (2 * sp.sqrt(2))))) < 1e-12)
    return rows


def main():
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'outputs')
    rw = ReportWriter(out_dir, label='t83b_jeans_correction')
    rw.section('T83b -- Two-phase Jeans eigenvalue (CLAUDE OPUS 5.5, Part 154)')

    r1 = derive_route1_original()
    acc2 = derive_mode_basis((1, 2, 2))
    acc3 = derive_mode_basis((1, 1, 1))
    origin = {th: 0, pm: 0, pp: 0}
    r2 = linear_matrix(acc2, origin)
    r3 = linear_matrix(acc3, origin)
    vac = linear_matrix(acc2, {th: sp.pi / 2, pm: sp.pi / 2, pp: 0})
    kin = derive_kinetic_inertias()
    n3_ok, n3_bad = derive_newton3((1, 2, 2)), derive_newton3((1, 1, 1))
    num = compute_numeric_eigs(r1['M'])
    ident = verify_product_identity()
    lam_new = max(r2['eigs'].keys(), key=lambda e: float(e.subs(g, 1)))
    lam_old = max(r3['eigs'].keys(), key=lambda e: float(e.subs(g, 1)))
    disp_new = derive_dispersion(list(r2['eigs'].keys()))
    disp_ratio = float(sp.sqrt(lam_new / lam_old))

    rw.subsection('Route 1: original fields (psi, phi_b, phi_s), unit inertia')
    rw.key_value('M = -Hess V', r1['M'])
    rw.key_value('eigenvalues {value: multiplicity}', r1['eigs'])
    rw.key_value('numpy eigenvalues (g=1)', num.tolist())
    rw.subsection('Route 2: (Theta, phi_-), inertias (1,2,2)')
    rw.key_value('kinetic T', kin['T'])
    rw.key_value('M', r2['M'])
    rw.key_value('eigenvalues', r2['eigs'])
    rw.key_value('Newton 3rd residual', n3_ok)
    rw.subsection('Route 3: all inertias 1 (Part 61 implicit)')
    rw.key_value('M', r3['M'])
    rw.key_value('eigenvalues', r3['eigs'])
    rw.key_value('Newton 3rd residual psi_tt+2phi_+tt', n3_bad)
    rw.subsection('Part 119 vacuum (Theta = phi_- = pi/2), inertias (1,2,2)')
    rw.key_value('M', vac['M'])
    rw.key_value('eigenvalues', vac['eigs'])
    rw.subsection('Dispersion (Eq 4)')
    for d in disp_new:
        rw.key_value('omega^2', d)
    rw.key_value('lambda_new / lambda_old', sp.nsimplify(lam_new / lam_old))
    rw.key_value('k_J new / k_J old', '{:.6f}'.format(disp_ratio))

    rw.section('Sudoku scorecard')
    rows = run_sudoku_checks(r1, r2, r3, vac, kin, n3_ok, n3_bad, num, ident, disp_ratio)
    rw.table(['ID', 'Test', 'Computed', 'Expected', 'Result'], rows,
             [4, 50, 40, 26, 13])
    n = sum(1 for x in rows if x[4] == 'MATCH')
    rw.key_value('Score', '{} matches, {} contradictions out of {} tests'.format(
        n, len(rows) - n, len(rows)))
    rw.close()


if __name__ == '__main__':
    main()
