#!/usr/bin/env python3
"""
t83c_biharmonic.py -- T83 sub-task 83c: re-derive the two-phase biharmonic
===========================================================================
Filed and worked by CLAUDE OPUS 5.5 (2026-09-28). Part 155.

GOAL:
    Re-derive Part 61's static "biharmonic gravity" equation
        nabla^4 Phi + 4 g^2 Phi = source      (as stated in Part 61)
    from the two-phase Lagrangian with (i) the correct inertias (1 for psi,
    2 for phi_+ and phi_-), (ii) the correct static sign, and (iii) exact
    operator elimination. Test every combination of the old conventions to
    locate where the "+4g^2" came from. Then check the Green's function
    claims (Part 61 "Poisson at short range"; Part 86 "1/r at r << 1/sqrt(g)").

EQUATIONS USED:
    Eq 1: L = 1/2 psi_t^2 + phi_+t^2 + phi_-t^2 (minus gradients)
              + 2 g sin(psi - phi_+) sin(phi_-)
          Source: Part 61 two-phase Lagrangian in mode variables [ASSUMED];
          kinetic diagonalisation verified in Part 154 (S4).
    Eq 2: Field equation for q with inertia I: I (q_tt - nabla^2 q) = F_q,
          F_q = dL_int/dq. Static: nabla^2 q = -F_q / I.
          Source: Euler-Lagrange field equation, Goldstein Sec 13.3
    Eq 3: Radial Laplacian (1/r^2) d/dr (r^2 d/dr).
          Source: https://en.wikipedia.org/wiki/Laplace_operator
    Eq 4: 3D Fourier inverse of a radial kernel:
          G(r) = 1/(2 pi^2 r) * Integral_0^inf k sin(k r) G~(k) dk
          Source: https://en.wikipedia.org/wiki/Fourier_transform

ASSUMPTIONS:
    [A1] Static, linearised about Theta = psi - phi_+ = 0, phi_- = 0
         (the point used by Part 61).
    [A2] Operator elimination treats D = nabla^2 as a commuting symbol
         (constant coefficients -- valid for uniform g).
    [A3] "Fixed-psi" model: psi is an external, prescribed source (Part 61's
         own treatment). "Dynamical-psi" model: psi obeys its own equation.
    [A4] g is the bare coupling, units 1/length^2 (term_glossary Sec 4),
         g_bare = omega_gap^2/c^2 = 1/a_0^2.

SIGN CONVENTIONS:
    L = T - V; F_q = dL_int/dq; static nabla^2 q = -F_q/I; G solves
    (nabla^4 - kappa^4) G = delta.

OUTPUT (data only):
    Operator polynomials for each convention, static eigenvalues of D,
    Green's function checks, scale ratios, Sudoku scorecard.
"""

import os
import sys
import numpy as np
import sympy as sp
from scipy.integrate import quad

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from print_utils import ReportWriter  # noqa: E402

g = sp.Symbol('g', positive=True)
D = sp.Symbol('D')                 # stands for nabla^2 (A2)
psi, pp, pm = sp.symbols('psi phi_p phi_m', real=True)
r, kap = sp.symbols('r kappa', positive=True)


def linear_forces():
    """Linearised F = dL_int/dq at Theta = 0, phi_- = 0 (Eq 1)."""
    L_int = 2 * g * sp.sin(psi - pp) * sp.sin(pm)
    th = sp.Symbol('Theta')
    out = {}
    for name, q in (('psi', psi), ('p', pp), ('m', pm)):
        F = sp.diff(L_int, q).subs(psi, th + pp)
        F = sp.series(sp.series(F, th, 0, 2).removeO(), pm, 0, 2).removeO()
        out[name] = sp.expand(F.subs(th, psi - pp))
    return out


def radial_laplacian(f):
    return sp.simplify(sp.diff(r**2 * sp.diff(f, r), r) / r**2)


# =====================================================================
# DERIVATIONS
# =====================================================================

def derive_fixed_psi(inertia, static_sign):
    """Fixed-psi model. Static relations D q = static_sign * F_q / I_q for
    q = phi_+, phi_- (correct: static_sign = -1). Eliminate phi_- exactly
    and return P(D) with P(D) phi_+ = Q psi, normalised so P = D^2 + c0."""
    F = linear_forces()
    eqs = [sp.Eq(D * pp, static_sign * F['p'] / inertia[1]),
           sp.Eq(D * pm, static_sign * F['m'] / inertia[2])]
    sol = sp.solve(eqs, [pp, pm], dict=True)[0]
    ratio = sp.together(sol[pp] / psi)          # = Q / P(D)
    num, den = sp.fraction(ratio)
    lead = sp.Poly(den, D).LC()
    P = sp.expand(den / lead)
    Q = sp.expand(num / lead)
    return {'P': P, 'Q': Q, 'c0': P.subs(D, 0)}


def derive_dynamic_psi():
    """Dynamical-psi model, correct conventions: D x = A x for
    x = (psi, phi_+, phi_-). Eigenvalues of A are the allowed values of
    nabla^2; D^2 = kappa^4 gives the biharmonic coefficient."""
    F = linear_forces()
    inert = {'psi': 1, 'p': 2, 'm': 2}
    x = (psi, pp, pm)
    A = sp.Matrix([[sp.diff(-F[n] / inert[n], v) for v in x]
                   for n in ('psi', 'p', 'm')])
    return {'A': A, 'eigs': A.eigenvals()}


def derive_green_function():
    """G = (cos(kappa r) - exp(-kappa r)) / (8 pi kappa^2 r).
    Check (nabla^4 - kappa^4) G = 0 for r > 0, small-r series, and that
    nabla^2 G ~ -1/(4 pi r) near 0 (so nabla^4 G = delta)."""
    G = (sp.cos(kap * r) - sp.exp(-kap * r)) / (8 * sp.pi * kap**2 * r)
    lapG = radial_laplacian(G)
    resid = sp.simplify(radial_laplacian(lapG) - kap**4 * G)
    ser = sp.series(G, r, 0, 3).removeO()
    inv_r_coeff = sp.simplify(ser.coeff(r, -1))
    lap_lead = sp.simplify(sp.limit(lapG * r, r, 0))
    return {'G': G, 'residual': resid, 'series': sp.expand(ser),
            'inv_r_coeff': inv_r_coeff, 'r_lapG_at_0': lap_lead}


# =====================================================================
# COMPUTATION
# =====================================================================

def compute_old_green_at_origin(a4=1.0):
    """Part 61/86 operator nabla^4 + a4 (a4 = 4g^2 > 0): Eq 4 at r -> 0
    gives G(0) = 1/(2 pi^2) Integral k^2/(k^4 + a4) dk. Finite => no 1/r
    divergence at short range (contradicts Part 86's 'source/(8 pi r)')."""
    val, err = quad(lambda k: k**2 / (k**4 + a4), 0, np.inf)
    G0 = val / (2 * np.pi**2)
    # compare with the analytic value 1/(4 sqrt(2) pi a4^(1/4))
    G0_exact = 1.0 / (4 * np.sqrt(2) * np.pi * a4**0.25)
    return {'G0': G0, 'G0_exact': G0_exact, 'quad_err': err}


def compute_new_green_numeric(kappa=1.0, r_vals=(0.5, 2.0, 7.0)):
    """Principal-value route: G = G_osc - G_yuk with
    G_osc = cos(kr)/(8 pi k^2 r) etc.; cross-check the closed form against
    the decomposition 1/(k^4 - kappa^4) = [1/(k^2-kappa^2) - 1/(k^2+kappa^2)]
    /(2 kappa^2) using the known transforms (Wikipedia: Yukawa potential;
    Helmholtz Green's function)."""
    out = []
    for rv in r_vals:
        closed = (np.cos(kappa * rv) - np.exp(-kappa * rv)) / (8 * np.pi * kappa**2 * rv)
        decomp = (np.cos(kappa * rv) / (4 * np.pi * rv)
                  - np.exp(-kappa * rv) / (4 * np.pi * rv)) / (2 * kappa**2)
        out.append((rv, closed, decomp))
    return out


# =====================================================================
# SUDOKU
# =====================================================================

def run_sudoku_checks(res, dyn, gf, old0, num):
    rows = []

    def add(tid, name, comp, exp, ok):
        rows.append((tid, name, str(comp), str(exp), 'MATCH' if ok else 'CONTRADICTION'))

    c_ok = res[(1, 2, 2, -1)]['c0']
    add('S1', 'Fixed psi, correct conventions: P(D) constant term', c_ok,
        'Part 61: +4g^2', sp.simplify(c_ok - 4 * g**2) == 0)
    signs = {k: v['c0'] for k, v in res.items()}
    any_plus = any(sp.simplify(v).subs(g, 1) > 0 for v in signs.values())
    add('S2', 'Any convention combo reproduces +4g^2?', signs, '+4g^2 somewhere',
        any_plus)
    c_old = res[(1, 1, 1, +1)]['c0']
    add('S3', 'Old conventions (inertia 1, D q = +F) give', c_old, -4 * g**2,
        sp.simplify(c_old + 4 * g**2) == 0)
    Q_ok = res[(1, 2, 2, -1)]['Q']
    add('S4', 'Fixed psi source term Q', Q_ok, -g**2, sp.simplify(Q_ok + g**2) == 0)
    ev = sorted(dyn['eigs'].keys(), key=lambda e: float(e.subs(g, 1)))
    add('S5', 'Dynamical psi: static eigenvalues of nabla^2', ev,
        '{0, +/-sqrt(3) g}', set(sp.simplify(e) for e in ev)
        == {0, sp.sqrt(3) * g, -sp.sqrt(3) * g})
    add('S6', 'Green fn (nabla^4 - kappa^4) residual, r > 0', gf['residual'], 0,
        gf['residual'] == 0)
    add('S7', 'r * nabla^2 G at r -> 0 (delta normalisation)', gf['r_lapG_at_0'],
        -1 / (4 * sp.pi), sp.simplify(gf['r_lapG_at_0'] + 1 / (4 * sp.pi)) == 0)
    add('S8', 'Coefficient of 1/r in G at small r (Part 86: 1/(8 pi))',
        gf['inv_r_coeff'], '1/(8*pi)', gf['inv_r_coeff'] == 1 / (8 * sp.pi))
    add('S9', 'Old operator G(0) finite (numeric vs analytic)',
        '{:.6f}'.format(old0['G0']), '{:.6f}'.format(old0['G0_exact']),
        abs(old0['G0'] / old0['G0_exact'] - 1) < 1e-6)
    ok_num = all(abs(c - d) < 1e-14 for _, c, d in num)
    add('S10', 'Closed-form G = decomposition (3 radii)', ok_num, True, ok_num)
    kap_new = sp.sqrt(-c_ok) ** sp.Rational(1, 2)
    kap_old_dim = (4 * g**2) ** sp.Rational(1, 4)
    ratio = sp.simplify(kap_old_dim / kap_new)
    add('S11', 'Length scale ratio L_new/L_old (old = (4g^2)^(-1/4))', ratio,
        'sqrt(2)', sp.simplify(ratio - sp.sqrt(2)) == 0)
    L_new = sp.simplify(1 / kap_new.subs(g, 1 / sp.Symbol('a_0', positive=True)**2))
    add('S12', 'L_bih = 1/kappa with g = 1/a_0^2', L_new, 'a_0',
        L_new == sp.Symbol('a_0', positive=True))
    return rows


def main():
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'outputs')
    rw = ReportWriter(out_dir, label='t83c_biharmonic')
    rw.section('T83c -- Two-phase biharmonic re-derivation (CLAUDE OPUS 5.5, Part 155)')

    res = {}
    for inertia in ((1, 2, 2), (1, 1, 1)):
        for sgn in (-1, +1):
            res[inertia + (sgn,)] = derive_fixed_psi(inertia, sgn)
    dyn = derive_dynamic_psi()
    gf = derive_green_function()
    old0 = compute_old_green_at_origin()
    num = compute_new_green_numeric()

    rw.subsection('Linearised forces F = dL_int/dq')
    for kname, v in linear_forces().items():
        rw.key_value('F_' + kname, v)
    rw.subsection('Fixed-psi model: P(D) phi_+ = Q psi, D = nabla^2')
    rw.table(['inertia', 'static sign', 'P(D)', 'Q'],
             [[str(k[:3]), str(k[3]), str(v['P']), str(v['Q'])] for k, v in res.items()],
             [12, 12, 22, 12])
    rw.subsection('Dynamical-psi model')
    rw.key_value('A (D x = A x)', dyn['A'])
    rw.key_value('eigenvalues of nabla^2', dyn['eigs'])
    rw.subsection('Green function of nabla^4 - kappa^4')
    rw.key_value('G', gf['G'])
    rw.key_value('(nabla^4 - kappa^4) G, r > 0', gf['residual'])
    rw.key_value('small-r series', gf['series'])
    rw.key_value('coeff of 1/r', gf['inv_r_coeff'])
    rw.key_value('lim r * nabla^2 G', gf['r_lapG_at_0'])
    rw.table(['r', 'closed form', 'decomposition'],
             [['{:.2f}'.format(a), '{:.10e}'.format(b), '{:.10e}'.format(c)]
              for a, b, c in num])
    rw.subsection('Old operator nabla^4 + a4 (a4 = 1)')
    rw.key_value('G(0) numeric', '{:.8f}'.format(old0['G0']))
    rw.key_value('G(0) analytic', '{:.8f}'.format(old0['G0_exact']))

    rw.section('Sudoku scorecard')
    rows = run_sudoku_checks(res, dyn, gf, old0, num)
    rw.table(['ID', 'Test', 'Computed', 'Expected', 'Result'], rows, [4, 52, 44, 18, 13])
    n = sum(1 for x in rows if x[4] == 'MATCH')
    rw.key_value('Score', '{} matches, {} contradictions out of {} tests'.format(
        n, len(rows) - n, len(rows)))
    rw.close()


if __name__ == '__main__':
    main()
