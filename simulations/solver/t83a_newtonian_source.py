#!/usr/bin/env python3
"""
t83a_newtonian_source.py -- T83 sub-task 83a: what sources the 1/r field?
==========================================================================
Filed and worked by CLAUDE OPUS 5.5 (2026-09-28). Part 153.

GOAL:
    Audit the Newtonian limit of the U(1) and two-phase PDTP Lagrangians.
    (a) Check the Part 63 S4 step "nabla^2 Phi proportional to Phi -> 1/r".
    (b) Identify the massless mode (Noether current of the joint phase
        shift) and compute the exterior monopole coefficient C of a static,
        spherically symmetric matter ball in two models:
          Model E ("extended"): psi defined everywhere, coupling g only
                                inside the ball, psi - phi -> Delta_inf at
                                infinity.
          Model K ("confined"): psi exists only inside the ball, no psi
                                flux through its surface (Neumann).
    (c) Check whether the two-phase vacuum sources any static field.

EQUATIONS USED:
    Eq 1: L = 1/2 (d phi)^2 + 1/2 (d psi)^2 + g(x) cos(psi - phi)
          Source: PDTP U(1) Lagrangian (CLAUDE.md) [ASSUMED]
    Eq 2: L_2 = 1/2[(d psi)^2 + (d phi_b)^2 + (d phi_s)^2]
                + g cos(psi - phi_b) - g cos(psi - phi_s)
          Source: PDTP two-phase Lagrangian, Part 61 [ASSUMED]
    Eq 3: Static E-L equation for a field q with unit kinetic term:
          -nabla^2 q = dL_int/dq   (from q_tt - nabla^2 q = dL_int/dq)
          Source: Euler-Lagrange field equation, Goldstein Sec 13.3
    Eq 4: Radial Laplacian: nabla^2 f(r) = (1/r^2) d/dr (r^2 df/dr)
          Source: https://en.wikipedia.org/wiki/Laplace_operator
    Eq 5: Noether's theorem: continuous symmetry -> conserved current
          Source: https://en.wikipedia.org/wiki/Noether%27s_theorem
    Eq 6: Newtonian exterior potential Phi = -GM/r, M = (4/3) pi R^3 rho
          Source: https://en.wikipedia.org/wiki/Poisson%27s_equation

ASSUMPTIONS:
    [A1] Static, spherically symmetric configuration (standard setup for the
         Newtonian limit; same as mathematical_formalization.md Sec 7.1).
    [A2] Coupling localised to the matter ball: g(x) = g for r < R, 0 outside
         (same as Sec 7.2: "outside the mass ... no matter sources").
    [A3] Linearisation sin(Delta) ~ Delta for the analytic cases; the
         nonlinear case is solved numerically (compute_nonlinear_extended).
    [A4] Natural units in the static equations (c = 1); g then has units of
         1/length^2 and k_Delta = sqrt(2 g) is a wavenumber.

SIGN CONVENTIONS:
    Metric (+,-,-,-); L = T - V; coupling +cos (stable at psi = phi);
    E-L: d_mu(dL/d(d_mu q)) - dL/dq = 0.

OUTPUT (data only):
    - Noether residuals, Laplacian ratios, monopole coefficients C(R),
      scaling ratios C(2R)/C(R), nonlinear/linear ratio, two-phase vacuum
      gradient and Hessian eigenvalues, Sudoku scorecard.
"""

import os
import sys
import numpy as np
import sympy as sp
from scipy.integrate import solve_bvp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from print_utils import ReportWriter  # noqa: E402

# Shared symbols
r, R, g, k = sp.symbols('r R g k', positive=True)
psi, phi, phi_b, phi_s = sp.symbols('psi phi phi_b phi_s', real=True)
D_inf, A, C = sp.symbols('Delta_inf A C', real=True)


def radial_laplacian(f):
    """Eq 4: (1/r^2) d/dr (r^2 df/dr)."""
    return sp.simplify(sp.diff(r**2 * sp.diff(f, r), r) / r**2)


# =====================================================================
# DERIVATIONS (symbolic only; return SymPy objects / dicts)
# =====================================================================

def derive_noether_u1():
    """Joint shift psi -> psi + a, phi -> phi + a.
    Step 1: L_int = g cos(psi - phi)                       [Eq 1]
    Step 2: dL_int/dpsi + dL_int/dphi                       [chain rule]
            = -g sin(psi-phi) + g sin(psi-phi) = 0          [DERIVED]
    => current J_mu = d_mu phi + d_mu psi is conserved (Eq 5)."""
    L_int = g * sp.cos(psi - phi)
    residual = sp.simplify(sp.diff(L_int, psi) + sp.diff(L_int, phi))
    return {'L_int': L_int, 'residual': residual}


def derive_noether_two_phase():
    """Joint shift of (psi, phi_b, phi_s); also the phi_- direction
    (phi_b -> phi_b + a, phi_s -> phi_s - a), which should NOT be a symmetry."""
    L_int = g * sp.cos(psi - phi_b) - g * sp.cos(psi - phi_s)
    joint = sp.simplify(sp.diff(L_int, psi) + sp.diff(L_int, phi_b)
                        + sp.diff(L_int, phi_s))
    minus_dir = sp.simplify(sp.diff(L_int, phi_b) - sp.diff(L_int, phi_s))
    return {'L_int': L_int, 'joint_residual': joint,
            'minus_direction': minus_dir}


def derive_static_linear_modes():
    """Static, linearised U(1) equations (Eq 3), Delta = psi - phi:
    Step 1: -nabla^2 phi = dL/dphi = g sin(Delta)  ~  g*Delta
    Step 2: -nabla^2 psi = dL/dpsi = -g sin(Delta) ~ -g*Delta
    Step 3: nabla^2 Delta = nabla^2 psi - nabla^2 phi = 2 g Delta
    Step 4: nabla^2 (phi + psi) = 0
    Coefficients are extracted from SymPy derivatives, not typed in."""
    d = sp.Symbol('Delta', real=True)
    L_int = g * sp.cos(psi - phi)
    lap_phi = -sp.diff(L_int, phi).subs(psi, phi + d)
    lap_psi = -sp.diff(L_int, psi).subs(psi, phi + d)
    lap_phi_lin = sp.series(lap_phi, d, 0, 2).removeO()
    lap_psi_lin = sp.series(lap_psi, d, 0, 2).removeO()
    lap_Delta = sp.simplify(lap_psi_lin - lap_phi_lin)
    lap_S = sp.simplify(lap_psi_lin + lap_phi_lin)
    k2 = sp.simplify(lap_Delta / d)
    return {'lap_Delta': lap_Delta, 'lap_S': lap_S, 'k_Delta_sq': k2}


def derive_laplacian_checks():
    """Eq 4 applied to candidate exterior profiles; ratio = lap(f)/f."""
    m = sp.Symbol('m', positive=True)
    out = {}
    out['inv_r'] = radial_laplacian(1 / r)
    out['yukawa_ratio'] = sp.simplify(
        radial_laplacian(sp.exp(-m * r) / r) / (sp.exp(-m * r) / r))
    out['oscill_ratio'] = sp.simplify(
        radial_laplacian(sp.cos(m * r) / r) / (sp.cos(m * r) / r))
    out['lap_r'] = radial_laplacian(r)
    out['lap_lap_r'] = radial_laplacian(out['lap_r'])
    out['m'] = m
    return out


def derive_extended_case():
    """Model E. Inside (r<R): nabla^2 Delta = k^2 Delta, regular solution
    Delta_in = A sinh(k r)/r. Outside (g = 0): nabla^2 Delta = 0,
    Delta_out = Delta_inf - C/r. Match value and slope at r = R."""
    D_in = A * sp.sinh(k * r) / r
    D_out = D_inf - C / r
    eqs = [sp.Eq(D_in.subs(r, R), D_out.subs(r, R)),
           sp.Eq(sp.diff(D_in, r).subs(r, R), sp.diff(D_out, r).subs(r, R))]
    sol = sp.solve(eqs, [A, C], dict=True)[0]
    C_expr = sp.simplify(sol[C])
    weak = sp.simplify(sp.series(C_expr, k, 0, 4).removeO())
    strong = sp.limit(C_expr / R, k, sp.oo)
    return {'A': sp.simplify(sol[A]), 'C': C_expr,
            'C_weak': weak, 'C_over_R_strong': strong,
            'C_at_zero_offset': sp.simplify(C_expr.subs(D_inf, 0))}


def derive_confined_case():
    """Model K. Inside: S = phi + psi harmonic and regular -> S = s0 (const);
    Delta = A sinh(k r)/r. psi = (S + Delta)/2, phi = (S - Delta)/2.
    Neumann (no psi flux out of the ball): psi'(R) = 0 -> solve for A.
    Exterior phi = phi_inf - C/r, slope continuity: C = R^2 phi'_in(R)."""
    s0 = sp.Symbol('s0', real=True)
    D_in = A * sp.sinh(k * r) / r
    psi_in = (s0 + D_in) / 2
    phi_in = (s0 - D_in) / 2
    flux_sum = sp.simplify(sp.diff(phi_in, r) + sp.diff(psi_in, r))
    A_sol = sp.solve(sp.Eq(sp.diff(psi_in, r).subs(r, R), 0), A)
    A_val = A_sol[0] if A_sol else None
    C_expr = sp.simplify((R**2 * sp.diff(phi_in, r)).subs(r, R).subs(A, A_val))
    return {'flux_sum': flux_sum, 'A_solution': A_val, 'C': C_expr}


def derive_two_phase_vacuum():
    """Two-phase coupling in (psi, phi_+, phi_-):
    L_int = 2 g sin(psi - phi_+) sin(phi_-)   (product identity, Part 61;
    cos(A)-cos(B) = -2 sin((A+B)/2) sin((A-B)/2), A&S 4.3.37).
    V = -L_int. Claimed vacuum: psi - phi_+ = pi/2, phi_- = pi/2 (Part 119).
    Return gradient of V there and Hessian eigenvalues in (Theta, phi_-),
    Theta = psi - phi_+."""
    th, pm = sp.symbols('Theta phi_m', real=True)
    V = -2 * g * sp.sin(th) * sp.sin(pm)
    # identity check against the original variables (independent)
    pp = sp.Symbol('phi_p', real=True)
    L_orig = (g * sp.cos(psi - (pp + pm)) - g * sp.cos(psi - (pp - pm)))
    identity_res = sp.simplify(sp.expand_trig(
        L_orig - 2 * g * sp.sin(psi - pp) * sp.sin(pm)))
    pt = {th: sp.pi / 2, pm: sp.pi / 2}
    grad = [sp.simplify(sp.diff(V, v).subs(pt)) for v in (th, pm)]
    H = sp.Matrix([[sp.diff(V, a, b).subs(pt) for b in (th, pm)]
                   for a in (th, pm)])
    return {'identity_residual': identity_res, 'grad': grad,
            'hessian_eigs': list(H.eigenvals().keys())}


def derive_two_phase_dynamics():
    """Kinetic terms 1/2(psi_t^2 + phi_b_t^2 + phi_s_t^2) become
    1/2 psi_t^2 + phi_+t^2 + phi_-t^2 (inertia 1, 2, 2).
    Newton 3rd law: psi_tt + 2 phi_+tt = F_psi + F_+ (Noether) -> 0.
    Linearise at Theta = 0, phi_- = 0 (the point used by Part 61) for the
    Jeans matrix acting on (Theta, phi_-)."""
    th, pm, pp = sp.symbols('Theta phi_m phi_p', real=True)
    L_int = 2 * g * sp.sin(psi - pp) * sp.sin(pm)
    F_psi = sp.diff(L_int, psi)
    F_p = sp.diff(L_int, pp)
    F_m = sp.diff(L_int, pm)
    a_psi, a_p, a_m = F_psi / 1, F_p / 2, F_m / 2       # inertias 1, 2, 2
    newton3 = sp.simplify(a_psi + 2 * a_p)
    sub = {psi: th + pp}
    a_th = sp.expand((a_psi - a_p).subs(sub))
    a_m2 = sp.expand(a_m.subs(sub))
    lin = lambda e: sp.expand(sp.series(sp.series(e, th, 0, 2).removeO(),
                                        pm, 0, 2).removeO())
    a_th_l, a_m_l = lin(a_th), lin(a_m2)
    M = sp.Matrix([[a_th_l.coeff(th), a_th_l.coeff(pm)],
                   [a_m_l.coeff(th), a_m_l.coeff(pm)]])
    return {'newton3_residual': newton3, 'M': M,
            'eigs': list(M.eigenvals().keys())}


# =====================================================================
# VERIFICATION (independent of the derive_* route)
# =====================================================================

def verify_extended_solution(ext):
    """Substitute the derived A, C back into the interior ODE and both
    matching conditions; all residuals must vanish."""
    D_in = ext['A'] * sp.sinh(k * r) / r
    D_out = D_inf - ext['C'] / r
    ode_res = sp.simplify(radial_laplacian(D_in) - k**2 * D_in)
    val_res = sp.simplify((D_in - D_out).subs(r, R))
    slope_res = sp.simplify(sp.diff(D_in - D_out, r).subs(r, R))
    return {'ode': ode_res, 'value': val_res, 'slope': slope_res,
            'ok': all(x == 0 for x in (ode_res, val_res, slope_res))}


# =====================================================================
# COMPUTATION (numerical)
# =====================================================================

def compute_scaling(ext, k_val=1.0, D_val=1.0):
    """Ratio C(2R)/C(R) at fixed k (fixed density) in weak (kR<<1) and
    strong (kR>>1) regimes. Newton (Eq 6): C ~ M ~ R^3 -> ratio 8."""
    Cf = sp.lambdify((R, k, D_inf), ext['C'], 'numpy')
    rows = []
    for R0 in (0.01, 100.0):
        c1, c2 = float(Cf(R0, k_val, D_val)), float(Cf(2 * R0, k_val, D_val))
        rows.append({'R': R0, 'kR': k_val * R0, 'C_R': c1, 'C_2R': c2,
                     'ratio': c2 / c1})
    return rows


def compute_nonlinear_extended(g_val=0.5, R_val=2.0, D_val=1e-3,
                               r0=1e-4, r_max=200.0, width=0.01):
    """Solve the full nonlinear static equation for Model E:
        Delta'' + (2/r) Delta' = 2 g(r) sin(Delta)
    g(r) = g * (1 - tanh((r-R)/w))/2 (smoothed step, [A2]).
    BCs: Delta'(r0) = 0; exterior form Delta_inf - C/r at r_max gives the
    Robin condition Delta + r Delta' = Delta_inf. Then C = r_max^2 Delta'."""
    def gfun(x):
        return g_val * 0.5 * (1.0 - np.tanh((x - R_val) / width))

    def rhs(x, y):
        return np.vstack([y[1], -2.0 * y[1] / x + 2.0 * gfun(x) * np.sin(y[0])])

    def bc(ya, yb):
        return np.array([ya[1], yb[0] + r_max * yb[1] - D_val])

    mesh = np.unique(np.concatenate([np.linspace(r0, R_val + 1, 4000),
                                     np.geomspace(R_val + 1, r_max, 2000)]))
    y0 = np.vstack([np.full_like(mesh, D_val), np.zeros_like(mesh)])
    sol = solve_bvp(rhs, bc, mesh, y0, tol=1e-8, max_nodes=200000)
    C_num = r_max**2 * sol.sol(r_max)[1]
    return {'success': bool(sol.success), 'C_num': float(C_num),
            'k': float(np.sqrt(2 * g_val)), 'R': R_val, 'D_inf': D_val}


# =====================================================================
# SUDOKU SCORECARD (reads computed values from the step dicts)
# =====================================================================

def run_sudoku_checks(n1, n2, modes, lap, ext, ver, scal, nl, conf, vac, dyn):
    """Each row: (id, test, computed, expected, MATCH/CONTRADICTION)."""
    rows = []

    def add(tid, name, computed, expected, ok):
        rows.append((tid, name, str(computed), str(expected),
                     'MATCH' if ok else 'CONTRADICTION'))

    add('S1', 'U(1) joint-shift Noether residual', n1['residual'], 0,
        n1['residual'] == 0)
    add('S2', 'Two-phase joint-shift Noether residual',
        n2['joint_residual'], 0, n2['joint_residual'] == 0)
    add('S3', 'phi_- direction is NOT a symmetry (nonzero)',
        n2['minus_direction'], '!= 0', n2['minus_direction'] != 0)
    add('S4', 'Laplace: nabla^2(1/r) (Newton exterior)', lap['inv_r'], 0,
        lap['inv_r'] == 0)
    add('S5', 'Part 63 S4: nabla^2 Phi ~ Phi gives 1/r? lap/f for e^-mr/r',
        lap['yukawa_ratio'], 0, lap['yukawa_ratio'] == 0)
    add('S6', 'Model E solution satisfies ODE + matching', ver['ok'], True,
        ver['ok'])
    w, s = scal[0], scal[1]
    add('S7', 'Weak coupling C(2R)/C(R) vs Newton 8 (kR={:.2g})'.format(w['kR']),
        '{:.4f}'.format(w['ratio']), 8, abs(w['ratio'] / 8 - 1) < 0.01)
    add('S8', 'Strong coupling C(2R)/C(R) vs Newton 8 (kR={:.2g})'.format(s['kR']),
        '{:.4f}'.format(s['ratio']), 8, abs(s['ratio'] / 8 - 1) < 0.01)
    add('S9', 'Model E, zero offset: C (Newton: nonzero for M>0)',
        ext['C_at_zero_offset'], '!= 0', ext['C_at_zero_offset'] != 0)
    add('S10', 'Model K (confined psi): C (Newton: nonzero for M>0)',
        conf['C'], '!= 0', conf['C'] != 0)
    C_lin = float(ext['C'].subs({R: nl['R'], k: nl['k'], D_inf: nl['D_inf']}))
    ratio_nl = nl['C_num'] / C_lin
    add('S11', 'Nonlinear BVP C / linear C (small offset)',
        '{:.5f}'.format(ratio_nl), 1, nl['success'] and abs(ratio_nl - 1) < 0.01)
    grad_zero = all(x == 0 for x in vac['grad'])
    hess_pos = all(sp.simplify(e).is_positive for e in vac['hessian_eigs'])
    add('S12', 'Two-phase vacuum: grad V=0 & Hessian>0 -> zero-source '
        'static solution (Newton: field)', 'grad={}, eig={}'.format(
            vac['grad'], vac['hessian_eigs']), 'source != 0',
        not (grad_zero and hess_pos))
    add('S13', 'Newton 3rd law psi_tt + 2 phi_+tt (inertias 1,2,2)',
        dyn['newton3_residual'], 0, dyn['newton3_residual'] == 0)
    pos = [e for e in dyn['eigs'] if sp.simplify(e).is_positive]
    add('S14', 'Jeans: a positive growth eigenvalue exists', dyn['eigs'],
        '> 0 exists', len(pos) > 0)
    return rows


def main():
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'outputs')
    rw = ReportWriter(out_dir, label='t83a_newtonian_source')
    rw.section('T83a -- Newtonian source audit (CLAUDE OPUS 5.5, Part 153)')

    n1, n2 = derive_noether_u1(), derive_noether_two_phase()
    modes = derive_static_linear_modes()
    lap = derive_laplacian_checks()
    ext = derive_extended_case()
    ver = verify_extended_solution(ext)
    scal = compute_scaling(ext)
    nl = compute_nonlinear_extended()
    conf = derive_confined_case()
    vac = derive_two_phase_vacuum()
    dyn = derive_two_phase_dynamics()

    rw.subsection('Noether (joint phase shift)')
    rw.key_value('U(1) residual dL/dpsi + dL/dphi', n1['residual'])
    rw.key_value('Two-phase joint residual', n2['joint_residual'])
    rw.key_value('Two-phase phi_- direction derivative', n2['minus_direction'])
    rw.subsection('Static linear modes (U(1))')
    for key in ('lap_Delta', 'lap_S', 'k_Delta_sq'):
        rw.key_value(key, modes[key])
    rw.subsection('Radial Laplacian checks')
    for key in ('inv_r', 'yukawa_ratio', 'oscill_ratio', 'lap_r', 'lap_lap_r'):
        rw.key_value(key, lap[key])
    rw.subsection('Model E (psi extended, g localised)')
    for key in ('A', 'C', 'C_weak', 'C_over_R_strong', 'C_at_zero_offset'):
        rw.key_value(key, ext[key])
    rw.key_value('verify residuals (ode, value, slope)',
                 (ver['ode'], ver['value'], ver['slope']))
    rw.table(['R', 'kR', 'C(R)', 'C(2R)', 'C(2R)/C(R)'],
             [['{:.3g}'.format(x['R']), '{:.3g}'.format(x['kR']),
               '{:.6g}'.format(x['C_R']), '{:.6g}'.format(x['C_2R']),
               '{:.5f}'.format(x['ratio'])] for x in scal])
    rw.key_value('Nonlinear BVP success', nl['success'])
    rw.key_value('Nonlinear C (k={:.3g}, R={}, D_inf={})'.format(
        nl['k'], nl['R'], nl['D_inf']), '{:.8e}'.format(nl['C_num']))
    rw.subsection('Model K (psi confined, Neumann)')
    for key in ('flux_sum', 'A_solution', 'C'):
        rw.key_value(key, conf[key])
    rw.subsection('Two-phase vacuum and dynamics')
    rw.key_value('product identity residual', vac['identity_residual'])
    rw.key_value('grad V at (pi/2, pi/2)', vac['grad'])
    rw.key_value('Hessian eigenvalues', vac['hessian_eigs'])
    rw.key_value('Newton 3rd residual', dyn['newton3_residual'])
    rw.key_value('Jeans matrix M (Theta, phi_-)', dyn['M'])
    rw.key_value('Jeans eigenvalues', dyn['eigs'])

    rw.section('Sudoku scorecard')
    rows = run_sudoku_checks(n1, n2, modes, lap, ext, ver, scal, nl, conf,
                             vac, dyn)
    rw.table(['ID', 'Test', 'Computed', 'Expected', 'Result'], rows,
             [4, 62, 34, 12, 13])
    n_match = sum(1 for x in rows if x[4] == 'MATCH')
    rw.key_value('Score', '{} matches, {} contradictions out of {} tests'.format(
        n_match, len(rows) - n_match, len(rows)))
    rw.close()


if __name__ == '__main__':
    main()
