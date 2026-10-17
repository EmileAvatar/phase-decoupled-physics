#!/usr/bin/env python3
"""
t83e_z3_target.py -- T83 sub-task 83e: SU(3) Z_3 target-space audit
====================================================================
Filed and worked by CLAUDE OPUS 5.5 (2026-10-17). Part 158.

GOAL:
    Part 37 claims the SU(3) Lagrangian supports topologically stable Z_3
    ("1/3-winding") vortices with energy E_Z3/E_U1 = 1/9 per vortex, and that
    three of them have "total winding 1 (integer, stable)". Test:
      (a) whether the coupling Re Tr(Psi^dag U) is invariant under the
          center shift U -> w U (needed for the target SU(3)/Z_3),
      (b) which modified couplings ARE center-invariant (alternatives B, C),
          and whether they keep the U(1) limit cos(psi - phi),
      (c) the minimal-energy generator X with exp(2 pi i X) = w * 1 inside
          SU(3), and the energy ratio it gives,
      (d) whether Part 37's path exp(i theta/3) * 1 lies in SU(3),
      (e) Z_3 fusion of three unit charges,
      (f) the U(3) minimal vortex (alternative D),
      (g) the Y-junction force balance (topology-independent).

EQUATIONS USED:
    Eq 1: L_3 = K Tr[(d U^dag)(d U)] + sum_i K_i Tr[(d Psi_i^dag)(d Psi_i)]
               + sum_i (g_i/3) Re Tr(Psi_i^dag U)        (Part 37) [ASSUMED]
    Eq 2: center of SU(3): Z_3 = {w^k * 1}, w = exp(2 pi i/3)
          https://en.wikipedia.org/wiki/Special_unitary_group [ASSUMED]
    Eq 3: pi_1(SU(3)) = 0 (simply connected); pi_1(PSU(3)) = pi_1(SU(3)/Z_3) = Z_3
          https://en.wikipedia.org/wiki/Projective_unitary_group [ASSUMED, cited]
    Eq 4: pi_1(U(n)) = Z, isomorphism induced by det
          https://en.wikipedia.org/wiki/Unitary_group [ASSUMED, cited]
    Eq 5: for U = exp(i theta X), theta = azimuth, the kinetic term gives
          E/L = 2 pi K Tr(X^2) ln(R/xi)   (generalises 2 pi K n^2 ln(R/xi),
          Kosterlitz & Thouless 1973, used by Part 37 Step 6) [DERIVED below]
    Eq 6: Balachandran, Digal & Matsuura (2006), Phys. Rev. D 73, 074009,
          arXiv:hep-ph/0509276 -- U(3)-type semi-superfluid strings [cited]

ASSUMPTIONS:
    [A1] Vortex energies compared at the logarithmic (far-field) level only;
         core energies are model-dependent and not compared.
    [A2] The "U(1) vortex" reference of Part 37 Step 6 (E = 2 pi K * 1^2 ln)
         is read as the scalar winding exp(i theta) * 1_3, i.e. Tr(X^2) = 3,
         which reproduces Part 37's own 1/9 when its path is inserted.
         The 1x1 normalisation (Tr = 1) is reported alongside.
    [A3] pi_1 values are cited mathematics, not computed here.

SIGN CONVENTIONS:
    +cos coupling (stable locking, CLAUDE.md); Tr(T^a T^b) = delta^ab / 2.

OUTPUT (data only): invariance residuals, minimal generator and Tr(X^2),
    energy ratios, determinant of the Part 37 path, Z_3 fusion class,
    U(3) generator, Sudoku scorecard.
"""

import itertools
import os
import sys

import numpy as np
import sympy as sp
from scipy.linalg import expm

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from print_utils import ReportWriter  # noqa: E402

W = sp.exp(2 * sp.pi * sp.I / 3)                  # center element w
x, y = sp.symbols('x y', real=True)               # Tr(Psi^dag U) = x + i y
th, a, b = sp.symbols('theta a b', real=True)     # azimuth; U(1) phases


# =====================================================================
# DERIVATIONS (symbolic, exact)
# =====================================================================

def derive_center_action():
    """Action of U -> w U on candidate couplings, with t = Tr(Psi^dag U).
    Linearity of the trace: Tr(Psi^dag (w U)) = w t."""
    t = x + sp.I * y
    re_shift = sp.simplify(sp.re(sp.expand(W * t)) - sp.re(t))
    # joint shift (U, Psi) -> (w U, w Psi): Tr((w Psi)^dag w U) = conj(w) w t
    joint = sp.simplify(sp.conjugate(W) * W * t - t)
    # adjoint form |t|^2 under U -> w U
    adj = sp.simplify(sp.expand(sp.Abs(W * t)**2 - sp.Abs(t)**2))
    return {'re_shift_residual': re_shift, 'joint_residual': joint,
            'adjoint_residual': adj}


def derive_u1_limits():
    """N = 1: U = exp(i b), Psi = exp(i a). Fundamental vs adjoint coupling."""
    t1 = sp.exp(-sp.I * a) * sp.exp(sp.I * b)
    fund = sp.simplify(sp.re(sp.expand_complex(t1)) - sp.cos(a - b))
    adj_value = sp.simplify(sp.Abs(t1)**2 - 1)    # adjoint of U(1): |t|^2 - 1
    adj_vs_cos = sp.simplify(adj_value - sp.cos(a - b))
    return {'fund_residual': fund, 'adjoint_value': adj_value,
            'adjoint_minus_cos': adj_vs_cos}


def derive_minimal_generator(charge=1, kmax=3):
    """Traceless diagonal X with exp(2 pi i X) = w^charge * 1 has eigenvalues
    q_j in charge/3 + Z, sum q_j = 0. Minimise Tr(X^2) over |k| <= kmax."""
    base = sp.Rational(charge, 3)
    best = None
    for ks in itertools.product(range(-kmax, kmax + 1), repeat=3):
        q = [base + k for k in ks]
        if sum(q) != 0:
            continue
        tr2 = sum(qi**2 for qi in q)
        if best is None or tr2 < best[0]:
            best = (tr2, tuple(sorted(q)))
    q = best[1]
    X = sp.diag(*q)
    expQ = sp.diag(*[sp.exp(2 * sp.pi * sp.I * qi) for qi in q])
    resid = sp.simplify(expQ - (W**charge) * sp.eye(3))
    return {'X_eigs': q, 'TrX2': best[0], 'exp_residual': resid,
            'traceless': sum(q)}


def derive_part37_path():
    """Part 37 Step 6 uses winding n = 1/3 of a single phase, i.e. the path
    U(theta) = exp(i theta/3) * 1_3. SU(3) requires det U = 1."""
    U = sp.exp(sp.I * th / 3) * sp.eye(3)
    det = sp.simplify(U.det())
    end = sp.simplify(U.subs(th, 2 * sp.pi))
    trq2 = 3 * sp.Rational(1, 3)**2                # X = (1/3) * 1_3
    return {'det': det, 'det_at_pi': sp.simplify(det.subs(th, sp.pi)),
            'endpoint_is_w': sp.simplify(end - W * sp.eye(3)) == sp.zeros(3),
            'TrX2': trq2}


def derive_fusion():
    """Z_3 charges add mod 3; as matrices, (w * 1)^3 = 1."""
    m = sp.simplify((W * sp.eye(3))**3 - sp.eye(3))
    return {'class_of_three': (1 + 1 + 1) % 3,
            'matrix_residual': m}


def derive_option_c_locking(X_eigs):
    """Option C: U = Psi = exp(i theta X) (joint winding). Then Psi^dag U = 1,
    so the coupling Re Tr(Psi^dag U)/3 stays at its locked maximum 1."""
    U = sp.diag(*[sp.exp(sp.I * th * q) for q in X_eigs])
    Psi = U
    coupling = sp.simplify(sp.re(sp.expand_complex((Psi.H * U).trace())) / 3)
    return {'coupling_along_path': coupling}


def derive_option_b_vacua():
    """Option B: coupling |Tr(W_rel)|^2 with W_rel = Psi^dag U. Its value at
    the three center elements w^k * 1 (k = 0, 1, 2) vs. its upper bound 9."""
    vals = [sp.simplify(sp.Abs((W**k * sp.eye(3)).trace())**2) for k in range(3)]
    return {'values_at_center': vals, 'bound': 9}


def derive_u3_vortex():
    """Option D: U(3) target. Minimal loop U = diag(exp(i theta), 1, 1):
    det winds once (generator of pi_1(U(3)) = Z); Tr(X^2) = 1 vs scalar 3."""
    X = sp.diag(1, 0, 0)
    U = sp.diag(sp.exp(sp.I * th), 1, 1)
    det = sp.simplify(U.det())
    winding = sp.simplify(sp.integrate(sp.diff(sp.log(det), th) / sp.I, (th, 0, 2 * sp.pi))
                          / (2 * sp.pi))
    return {'TrX2': (X * X).trace(), 'det': det, 'det_winding': winding,
            'ratio_to_scalar': sp.Rational((X * X).trace(), 3)}


def derive_kinetic_density():
    """Eq 5: for U = exp(i theta(phi_az) X), Tr[(dU^dag)(dU)] = Tr(X^2) (d theta)^2.
    Checked for a diagonal X with symbolic eigenvalues."""
    q1, q2, q3 = sp.symbols('q1 q2 q3', real=True)
    U = sp.diag(*[sp.exp(sp.I * th * q) for q in (q1, q2, q3)])
    dU = U.diff(th)
    dens = sp.simplify((dU.H * dU).trace())
    return {'density': dens, 'residual': sp.simplify(dens - (q1**2 + q2**2 + q3**2))}


def derive_y_junction():
    """Three unit vectors at 120 deg sum to zero (force balance, Part 37 S8)."""
    vecs = [sp.Matrix([sp.cos(2 * sp.pi * k / 3), sp.sin(2 * sp.pi * k / 3)])
            for k in range(3)]
    s = sp.simplify(vecs[0] + vecs[1] + vecs[2])
    return {'sum': s}


# =====================================================================
# COMPUTATION
# =====================================================================

def compute_energy_ratios(gen, old):
    """Log-level energy ratios from Eq 5: E/L proportional to Tr(X^2)."""
    ref_scalar = 3                                  # exp(i theta) * 1_3  [A2]
    ref_1x1 = 1                                     # U(1) 1x1 normalisation
    return {
        'E_Z3_over_scalar': sp.Rational(gen['TrX2']) / ref_scalar,
        'E_Z3_over_1x1': sp.Rational(gen['TrX2']) / ref_1x1,
        'three_Z3_over_scalar': 3 * sp.Rational(gen['TrX2']) / ref_scalar,
        'part37_ratio_reproduced': sp.Rational(old['TrX2']) / ref_scalar,
    }


# =====================================================================
# VERIFICATION (independent, numerical)
# =====================================================================

def _rand_su3(rng):
    A = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    H = (A + A.conj().T) / 2
    H -= np.trace(H) / 3 * np.eye(3)
    return expm(1j * H)


def verify_center_numeric(n=200, seed=158):
    """Random SU(3) pairs: max change of Re Tr, |Tr|^2, joint Tr under shifts."""
    rng = np.random.default_rng(seed)
    w = np.exp(2j * np.pi / 3)
    d_re, d_adj, d_joint, det_err = 0.0, 0.0, 0.0, 0.0
    for _ in range(n):
        U, P = _rand_su3(rng), _rand_su3(rng)
        t = np.trace(P.conj().T @ U)
        t_w = np.trace(P.conj().T @ (w * U))
        t_j = np.trace((w * P).conj().T @ (w * U))
        d_re = max(d_re, abs(t_w.real - t.real))
        d_adj = max(d_adj, abs(abs(t_w)**2 - abs(t)**2))
        d_joint = max(d_joint, abs(t_j - t))
        det_err = max(det_err, abs(np.linalg.det(U) - 1))
    return {'max_dRe': d_re, 'max_dAdj': d_adj, 'max_dJoint': d_joint,
            'max_det_err': det_err}


def verify_minimal_generator_numeric(kmax=4):
    """Independent brute force (floats, wider range, matrix exponential)."""
    w = np.exp(2j * np.pi / 3)
    best = None
    rng = range(-kmax, kmax + 1)
    for k1, k2 in itertools.product(rng, rng):
        q = np.array([1 / 3 + k1, 1 / 3 + k2, -(2 / 3 + k1 + k2)])
        # third eigenvalue fixed by tracelessness; check it is in 1/3 + Z
        if not np.isclose((q[2] - 1 / 3) % 1, 0) and not np.isclose((q[2] - 1 / 3) % 1, 1):
            continue
        if not np.allclose(expm(2j * np.pi * np.diag(q)), w * np.eye(3)):
            continue
        tr2 = float(np.sum(q**2))
        if best is None or tr2 < best:
            best = tr2
    return {'min_TrX2': best}


# =====================================================================
# SUDOKU
# =====================================================================

def run_sudoku_checks(ca, u1, gen, gen2, old, fus, oc, ob, u3, kin, yj, er,
                      vnum, vgen):
    rows = []

    def add(tid, name, comp, exp, ok):
        rows.append((tid, name, str(comp), str(exp),
                     'MATCH' if ok else 'CONTRADICTION'))

    z3 = sp.zeros(3)
    add('S1', 'Part 37 needs Re Tr(Psi^dag U) Z3-invariant (residual)',
        ca['re_shift_residual'], 0, ca['re_shift_residual'] == 0)
    add('S2', 'Joint (wU, wPsi) shift invariant (option C)',
        ca['joint_residual'], 0, ca['joint_residual'] == 0)
    add('S3', 'Adjoint |Tr|^2 invariant under U->wU (option B)',
        ca['adjoint_residual'], 0, ca['adjoint_residual'] == 0)
    add('S4', 'U(1) limit Re Tr -> cos(psi-phi) (Part 37 S3)',
        u1['fund_residual'], 0, u1['fund_residual'] == 0)
    add('S5', 'U(1) limit of adjoint coupling = cos(psi-phi)? (option B)',
        u1['adjoint_minus_cos'], 0, u1['adjoint_minus_cos'] == 0)
    add('S6', 'Kinetic density = Tr(X^2)(d theta)^2 (Eq 5 residual)',
        kin['residual'], 0, kin['residual'] == 0)
    add('S7', 'exp(2 pi i X_min) = w*1 (residual matrix zero)',
        gen['exp_residual'] == z3, True, gen['exp_residual'] == z3)
    add('S8', 'min Tr(X^2): exact enumeration = independent float search',
        gen['TrX2'], vgen['min_TrX2'],
        abs(float(gen['TrX2']) - vgen['min_TrX2']) < 1e-12)
    add('S9', 'Antivortex (w^2) min Tr(X^2) equals vortex value',
        gen2['TrX2'], gen['TrX2'], gen2['TrX2'] == gen['TrX2'])
    add('S10', 'Part 37 path exp(i th/3)*1 in SU(3)? det at th=pi',
        old['det_at_pi'], 1, sp.simplify(old['det_at_pi'] - 1) == 0)
    add('S11', 'E_Z3/E_U1 per vortex = 1/9 (Part 37 S7)',
        er['E_Z3_over_scalar'], sp.Rational(1, 9),
        er['E_Z3_over_scalar'] == sp.Rational(1, 9))
    add('S12', 'Part 37 1/9 reproduced by its own (invalid) path, ref [A2]',
        er['part37_ratio_reproduced'], sp.Rational(1, 9),
        er['part37_ratio_reproduced'] == sp.Rational(1, 9))
    add('S13', 'Three Z3 units nontrivial ("total winding 1", Part 37)',
        fus['class_of_three'], 1, fus['class_of_three'] == 1)
    add('S14', '(w*1)^3 = 1 (Z3 fusion to identity; junction allowed)',
        fus['matrix_residual'] == z3, True, fus['matrix_residual'] == z3)
    add('S15', 'Option C joint vortex keeps locking: Re Tr/3 = 1',
        oc['coupling_along_path'], 1, oc['coupling_along_path'] == 1)
    add('S16', 'Option B: three degenerate maxima |Tr|^2 = 9 at w^k*1',
        ob['values_at_center'], ob['bound'],
        all(v == ob['bound'] for v in ob['values_at_center']))
    add('S17', 'Option D: U(3) minimal loop det winding = 1',
        u3['det_winding'], 1, u3['det_winding'] == 1)
    add('S18', 'Y-junction: 3 unit vectors at 120 deg sum to 0 (Part 37 S8)',
        list(yj['sum']), [0, 0], yj['sum'] == sp.zeros(2, 1))
    add('S19', 'Numeric: max |dRe Tr| under U->wU over 200 SU(3) pairs > 0',
        '{:.3f}'.format(vnum['max_dRe']), '> 0', vnum['max_dRe'] > 1e-6)
    add('S20', 'Numeric: adjoint and joint changes < 1e-10',
        '{:.1e}, {:.1e}'.format(vnum['max_dAdj'], vnum['max_dJoint']), '< 1e-10',
        vnum['max_dAdj'] < 1e-10 and vnum['max_dJoint'] < 1e-10)
    return rows


def main():
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'outputs')
    rw = ReportWriter(out_dir, label='t83e_z3_target')
    rw.section('T83e -- SU(3) Z3 target-space audit (CLAUDE OPUS 5.5, Part 158)')
    ca, u1 = derive_center_action(), derive_u1_limits()
    gen, gen2 = derive_minimal_generator(1), derive_minimal_generator(2)
    old, fus = derive_part37_path(), derive_fusion()
    oc, ob = derive_option_c_locking(gen['X_eigs']), derive_option_b_vacua()
    u3, kin, yj = derive_u3_vortex(), derive_kinetic_density(), derive_y_junction()
    er = compute_energy_ratios(gen, old)
    vnum, vgen = verify_center_numeric(), verify_minimal_generator_numeric()

    rw.subsection('Center action on couplings (t = Tr(Psi^dag U) = x + i y)')
    for k in ('re_shift_residual', 'joint_residual', 'adjoint_residual'):
        rw.key_value(k, ca[k])
    rw.subsection('U(1) limits (N = 1)')
    for k in ('fund_residual', 'adjoint_value', 'adjoint_minus_cos'):
        rw.key_value(k, u1[k])
    rw.subsection('Kinetic density for U = exp(i theta X)')
    rw.key_value('Tr[(dU^dag)(dU)] / (d theta)^2', kin['density'])
    rw.subsection('Minimal Z3 generator in SU(3)')
    rw.key_value('charge 1: X eigenvalues', gen['X_eigs'])
    rw.key_value('charge 1: Tr(X^2)', gen['TrX2'])
    rw.key_value('charge 2: X eigenvalues', gen2['X_eigs'])
    rw.key_value('charge 2: Tr(X^2)', gen2['TrX2'])
    rw.key_value('float search min Tr(X^2)', vgen['min_TrX2'])
    rw.subsection('Part 37 path exp(i theta/3) * 1_3')
    rw.key_value('det U(theta)', old['det'])
    rw.key_value('endpoint at theta=2 pi equals w*1', old['endpoint_is_w'])
    rw.key_value('Tr(X^2) of that path', old['TrX2'])
    rw.subsection('Energy ratios (log level, Eq 5)')
    for k, v in er.items():
        rw.key_value(k, v)
    rw.subsection('Alternatives')
    rw.key_value('B: |Tr|^2 at w^k*1 (k=0,1,2)', ob['values_at_center'])
    rw.key_value('C: Re Tr(Psi^dag U)/3 along joint vortex', oc['coupling_along_path'])
    rw.key_value('D: U(3) loop det', u3['det'])
    rw.key_value('D: det winding', u3['det_winding'])
    rw.key_value('D: Tr(X^2), ratio to scalar', (u3['TrX2'], u3['ratio_to_scalar']))
    rw.subsection('Numerical sampling (200 random SU(3) pairs, seed 158)')
    for k, v in vnum.items():
        rw.key_value(k, '{:.3e}'.format(v))

    rw.section('Sudoku scorecard')
    rows = run_sudoku_checks(ca, u1, gen, gen2, old, fus, oc, ob, u3, kin, yj,
                             er, vnum, vgen)
    rw.table(['ID', 'Test', 'Computed', 'Expected', 'Result'], rows,
             [4, 60, 26, 14, 13])
    n = sum(1 for r in rows if r[4] == 'MATCH')
    rw.key_value('Score', '{} matches, {} contradictions out of {} tests'.format(
        n, len(rows) - n, len(rows)))
    rw.close()


if __name__ == '__main__':
    main()
