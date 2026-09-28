#!/usr/bin/env python3
"""
t83d_geff.py -- T83 sub-task 83d: is G_eff = 2 G_bare physical?
================================================================
Filed and worked by CLAUDE OPUS 5.5 (2026-09-28). Part 156.

GOAL:
    Part 62 states G_eff = 2 G_bare (two-phase vacuum phi_- = pi/2 vs the
    single-phase theory at the same g), and CLAUDE.md links it to the
    Newton's-3rd-law factor psi_tt = -2 phi_+tt. Test, at equal g:
      (a) source -> field: static field per unit phase offset,
      (b) field -> test: force amplitude on a matter phase,
      (c) their product (what "G" measures),
      (d) an unrelated observable (relative-mode frequency),
      (e) whether the Newton factor survives a change of field basis,
      (f) the phi_- dependence of G_eff (Part 62 wrote g_eff = 2g sin phi_-).

EQUATIONS USED:
    Eq 1: L_1 = 1/2(d phi)^2 + 1/2(d psi)^2 + g cos(psi - phi)   (CLAUDE.md) [ASSUMED]
    Eq 2: L_2 = 1/2[(d psi)^2 + (d phi_b)^2 + (d phi_s)^2]
               + g cos(psi - phi_b) - g cos(psi - phi_s)          (Part 61) [ASSUMED]
    Eq 3: field eq. with inertia/stiffness I: I(q_tt - nabla^2 q) = F_q,
          F_q = dL_int/dq; static nabla^2 q = -F_q/I  (Goldstein Sec 13.3)
    Eq 4: Newtonian interaction energy of a source and a test body through a
          field with stiffness K and couplings a_s, a_t scales as a_s a_t / K
          (Green's function of K nabla^2), e.g. Coulomb/Newton by analogy:
          https://en.wikipedia.org/wiki/Poisson%27s_equation

ASSUMPTIONS:
    [A1] Two-phase vacuum phi_- = pi/2 held fixed (Part 119); Theta' =
         psi - phi_+ - pi/2 plays the role of the single-phase gap Delta.
    [A2] Linear response (sin x ~ x) for the mode frequency.
    [A3] A held phase offset is assumed to exist (Part 153 / 83i: the
         Lagrangian alone does not supply it); results compare strengths
         GIVEN an offset.

OUTPUT (data only): ratios two-phase / single-phase, basis-dependence of the
    Newton factor, G_eff(phi_-) profile, Sudoku scorecard.
"""

import os
import sys
import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from print_utils import ReportWriter  # noqa: E402

g = sp.Symbol('g', positive=True)
psi, phi, pb, ps = sp.symbols('psi phi phi_b phi_s', real=True)
pp, pm, S, d = sp.symbols('phi_p phi_m Sigma Delta', real=True)


# =====================================================================
# DERIVATIONS
# =====================================================================

def derive_amplitude():
    """Two-phase coupling in mode variables and its amplitude at phi_- = pi/2."""
    L2 = g * sp.cos(psi - (pp + pm)) - g * sp.cos(psi - (pp - pm))
    at_vac = sp.simplify(sp.expand_trig(L2.subs(pm, sp.pi / 2)))
    target = 2 * g * sp.cos(psi - pp - sp.pi / 2)
    resid = sp.simplify(sp.expand_trig(at_vac - target))
    amp = sp.simplify(sp.expand_trig(L2)).subs(psi, pp + sp.pi / 2)
    return {'L_vac': at_vac, 'identity_residual': resid,
            'amplitude_general': sp.simplify(amp)}


def derive_newton_factor(basis):
    """psi_tt = -k * X_tt for X the gravity-mode variable of the basis.
    'plus': X = phi_+ = (phi_b + phi_s)/2 (inertia 2)
    'sum' : X = Sigma = phi_b + phi_s     (inertia 1/2)
    Joint shift psi, phi_b, phi_s -> +a moves X by w_X (1 for phi_+, 2 for
    Sigma), so Noether gives F_psi + w_X F_X = 0 and k = I_X / w_X
    (RECHECK fix: first version used w_X = 1 in both bases)."""
    pt, mt, St = sp.symbols('p_t m_t S_t', real=True)
    if basis == 'plus':
        T = sp.Rational(1, 2) * ((pt + mt)**2 + (pt - mt)**2)
        I_X = 2 * sp.expand(T).coeff(pt, 2)
        L_int = g * sp.cos(psi - (pp + pm)) - g * sp.cos(psi - (pp - pm))
        F_X = sp.diff(L_int, pp)
        w_X = 1
    else:
        T = sp.Rational(1, 2) * ((St / 2 + mt)**2 + (St / 2 - mt)**2)
        I_X = 2 * sp.expand(T).coeff(St, 2)
        L_int = g * sp.cos(psi - (S / 2 + pm)) - g * sp.cos(psi - (S / 2 - pm))
        F_X = sp.diff(L_int, S)
        w_X = 2
    F_psi = sp.diff(L_int, psi)
    balance = sp.simplify(F_psi + w_X * F_X)         # Noether: 0
    psi_tt, X_tt = F_psi / 1, F_X / I_X
    k = sp.simplify(-psi_tt / X_tt)
    return {'I_X': I_X, 'w_X': w_X, 'balance': balance, 'k': k}


def derive_response():
    """(a) source->field and (b) field->test coefficients, linearised.
    Single phase: nabla^2 phi = -F_phi/1, F_phi = g sin(Delta), F_psi = -g sin(Delta).
    Two phase (phi_- = pi/2): nabla^2 phi_+ = -F_+/2, psi = phi_+ + pi/2 + Delta."""
    L1 = g * sp.cos(psi - phi)
    F1_field = sp.diff(L1, phi).subs(psi, phi + d)
    F1_test = sp.diff(L1, psi).subs(psi, phi + d)
    src1 = sp.series(-F1_field / 1, d, 0, 2).removeO()       # nabla^2 phi
    tst1 = sp.series(F1_test, d, 0, 2).removeO()
    L2 = (g * sp.cos(psi - (pp + pm)) - g * sp.cos(psi - (pp - pm))).subs(pm, sp.pi / 2)
    sub = {psi: pp + sp.pi / 2 + d}
    F2_field = sp.diff(L2, pp).subs(sub)
    F2_test = sp.diff(L2, psi).subs(sub)
    src2 = sp.series(sp.simplify(-F2_field / 2), d, 0, 2).removeO()
    tst2 = sp.series(sp.simplify(F2_test), d, 0, 2).removeO()
    return {'src1': sp.expand(src1), 'tst1': sp.expand(tst1),
            'src2': sp.expand(src2), 'tst2': sp.expand(tst2)}


def derive_mode_frequency():
    """(d) relative-mode omega^2 at the lock: single phase Delta_tt =
    -(1/I_psi + 1/I_phi) g Delta; two phase with inertias (1, 2) and
    amplitude 2g."""
    w1 = g * (sp.Rational(1, 1) + sp.Rational(1, 1))
    w2 = 2 * g * (sp.Rational(1, 1) + sp.Rational(1, 2))
    return {'w2_single': w1, 'w2_two': w2}


def derive_geff_profile():
    """(f) coupling amplitude a(phi_-) = 2 g sin(phi_-); phi_+ stiffness 2.
    G ~ a_s a_t / K (Eq 4) -> G_eff/G_single(g) = (2 g sin)^2 / 2 / g^2."""
    x = sp.Symbol('x', real=True)
    a = 2 * g * sp.sin(x)
    ratio = sp.simplify(a**2 / 2 / g**2)
    return {'ratio_expr': ratio, 'at_pi2': ratio.subs(x, sp.pi / 2),
            'at_pi4': ratio.subs(x, sp.pi / 4),
            'part62_linear_at_pi4': sp.simplify((a / g).subs(x, sp.pi / 4))}


# =====================================================================
# SUDOKU
# =====================================================================

def run_sudoku_checks(amp, nf_plus, nf_sum, resp, wf, prof):
    rows = []

    def add(tid, name, comp, exp, ok):
        rows.append((tid, name, str(comp), str(exp), 'MATCH' if ok else 'CONTRADICTION'))

    add('S1', 'phi_-=pi/2: L_int = 2g cos(psi - phi_+ - pi/2) (residual)',
        amp['identity_residual'], 0, amp['identity_residual'] == 0)
    add('S2', 'Noether balance F_psi + 1*F_X, basis phi_+', nf_plus['balance'], 0,
        nf_plus['balance'] == 0)
    add('S3', 'Noether balance F_psi + 2*F_X, basis Sigma', nf_sum['balance'], 0,
        nf_sum['balance'] == 0)
    add('S4', 'Newton factor k (basis phi_+) = 2 (Part 61)', nf_plus['k'], 2,
        nf_plus['k'] == 2)
    add('S5', 'Newton factor k basis-independent? (Sigma basis)', nf_sum['k'], 2,
        nf_sum['k'] == 2)
    c_src1 = resp['src1'].coeff(d)
    c_src2 = resp['src2'].coeff(d)
    c_tst1 = resp['tst1'].coeff(d)
    c_tst2 = resp['tst2'].coeff(d)
    r_src = sp.simplify(c_src2 / c_src1)
    r_tst = sp.simplify(c_tst2 / c_tst1)
    r_G = sp.simplify(r_src * r_tst)
    add('S6', 'source->field ratio (two/single)', r_src, 1, r_src == 1)
    add('S7', 'field->test ratio (two/single)', r_tst, 2, r_tst == 2)
    add('S8', 'G ratio = product (Part 62: 2)', r_G, 2, r_G == 2)
    r_w = sp.simplify(wf['w2_two'] / wf['w2_single'])
    add('S9', 'Relative-mode omega^2 ratio (uniform g->2g would give 2)', r_w, 2,
        r_w == 2)
    add('S10', 'G_eff/G(g) at phi_-=pi/2 from profile', prof['at_pi2'], 2,
        prof['at_pi2'] == 2)
    add('S11', 'G_eff/G(g) at phi_-=pi/4: sin^2 profile vs Part 62 linear',
        prof['at_pi4'], prof['part62_linear_at_pi4'],
        sp.simplify(prof['at_pi4'] - prof['part62_linear_at_pi4']) == 0)
    return rows, {'r_src': r_src, 'r_tst': r_tst, 'r_G': r_G, 'r_w': r_w}


def main():
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'outputs')
    rw = ReportWriter(out_dir, label='t83d_geff')
    rw.section('T83d -- G_eff = 2 G_bare audit (CLAUDE OPUS 5.5, Part 156)')
    amp = derive_amplitude()
    nf_plus, nf_sum = derive_newton_factor('plus'), derive_newton_factor('sum')
    resp = derive_response()
    wf = derive_mode_frequency()
    prof = derive_geff_profile()

    rw.subsection('Coupling amplitude')
    rw.key_value('L_int at phi_- = pi/2', amp['L_vac'])
    rw.key_value('identity residual', amp['identity_residual'])
    rw.key_value('L_int at psi = phi_+ + pi/2 (amplitude vs phi_-)', amp['amplitude_general'])
    rw.subsection('Newton factor psi_tt = -k X_tt by basis')
    for name, nf in (('phi_+ = (phi_b+phi_s)/2', nf_plus), ('Sigma = phi_b+phi_s', nf_sum)):
        rw.key_value(name + ': inertia I_X', nf['I_X'])
        rw.key_value(name + ': k', nf['k'])
    rw.subsection('Linear response (coefficient of Delta)')
    for key in ('src1', 'tst1', 'src2', 'tst2'):
        rw.key_value(key, resp[key])
    rw.subsection('Relative-mode frequency and G_eff profile')
    rw.key_value('omega^2 single / two', (wf['w2_single'], wf['w2_two']))
    rw.key_value('G_eff/G_single(g) vs phi_- (x)', prof['ratio_expr'])

    rw.section('Sudoku scorecard')
    rows, ratios = run_sudoku_checks(amp, nf_plus, nf_sum, resp, wf, prof)
    rw.table(['ID', 'Test', 'Computed', 'Expected', 'Result'], rows, [4, 58, 30, 18, 13])
    n = sum(1 for x in rows if x[4] == 'MATCH')
    rw.key_value('ratios', ratios)
    rw.key_value('Score', '{} matches, {} contradictions out of {} tests'.format(
        n, len(rows) - n, len(rows)))
    rw.close()


if __name__ == '__main__':
    main()
