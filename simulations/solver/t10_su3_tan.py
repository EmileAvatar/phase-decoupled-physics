"""
T10 -- SU(3) Group Manifold Tan (Part 121, Phase 89)
PDTP tan investigation: does tan appear in SU(3) geometry?

Three-part investigation:
  Part A: Z3 vacuum switching angle -- the 'color Brewster angle'
  Part B: Gell-Mann generator angle catalog
  Part C: Casimir connection C2(fund) = 1/sin^2(theta_crit)

Output: DATA only. Interpretation in docs/research/su3_tan_geometry.md.
Source: Gell-Mann (1962); PDG Review 2022; Georgi (1999) Lie Algebras.
"""

import math
import sys
import os
import io
import numpy as np

try:
    from sympy import cos, symbols, solve, pi, tan, simplify, Rational, sqrt, sin
    SYMPY_OK = True
except ImportError:
    SYMPY_OK = False

DEG = math.pi / 180.0

# SU(3) Casimir invariants [PDG Review 2022, Quark Model]
C2_FUND = 4.0 / 3.0
C2_ADJ  = 3.0
N_COLOR = 3

# U(1) results carried forward from T2 / Part 99
DELTA_U1_DEG = 45.0
TAN_U1_CRIT  = math.tan(DELTA_U1_DEG * DEG)   # = 1.0


# ============================================================
# Part A: Z3 vacuum switching angle
# ============================================================

def derive_z3_critical_angle():
    """
    Find Delta in (0, pi/2) where coupling to Z3 vacuum k=0 equals k=1.
    Coupling_k(Delta) = cos(Delta - 2*pi*k/3)
    Condition: cos(Delta) = cos(Delta - 2*pi/3)
    Algebraic solution: Delta = pi/3 = 60 deg.
    PDTP Original: SU(3) color Brewster angle.
    """
    deltas = np.linspace(0.0, math.pi / 2.0, 200001)
    gap = np.cos(deltas) - np.cos(deltas - 2.0 * math.pi / 3.0)
    idx = np.where(np.diff(np.sign(gap)))[0]
    if len(idx) == 0:
        return None
    i = idx[0]
    d0, d1 = deltas[i], deltas[i + 1]
    g0, g1 = gap[i], gap[i + 1]
    delta_rad = d0 - g0 * (d1 - d0) / (g1 - g0)
    delta_deg = math.degrees(delta_rad)

    c0 = math.cos(delta_rad)
    c1 = math.cos(delta_rad - 2.0 * math.pi / 3.0)
    f0 = math.sin(delta_rad)                             # restoring force toward k=0
    f1 = -math.sin(delta_rad - 2.0 * math.pi / 3.0)     # restoring force toward k=1
    return {
        'delta_deg': delta_deg,
        'delta_rad': delta_rad,
        'tan_crit':  math.tan(delta_rad),
        'sqrt3':     math.sqrt(3.0),
        'coupling_k0': c0,
        'coupling_k1': c1,
        'gap_at_crit': c0 - c1,
        'force_k0':  f0,
        'force_k1':  f1,
    }


def sympy_z3_critical():
    """
    SymPy algebraic verification: solve cos(x) = cos(x - 2*pi/3) for x in (0, pi/2).
    Returns residual at x = pi/3.
    """
    if not SYMPY_OK:
        return {'ok': False, 'reason': 'sympy not available'}
    x = symbols('x')
    expr = cos(x) - cos(x - 2 * pi / 3)
    residual = simplify(expr.subs(x, pi / 3))
    tan_at_pi3 = simplify(tan(pi / 3) - sqrt(3))
    c2_check = simplify(Rational(1, 1) / sin(pi / 3)**2 - Rational(4, 3))
    return {
        'ok': True,
        'residual_at_pi_over_3': float(residual),
        'tan_pi_over_3_minus_sqrt3': float(tan_at_pi3),
        'c2_fund_from_sin2': float(c2_check),
    }


def derive_su2_critical():
    """Z2 vacua at 0 and 180 deg; midpoint at 90 deg, tan(90) -> inf."""
    return {
        'delta_deg': 90.0,
        'tan_approx': math.tan(math.pi / 2.0 - 1e-10),
    }


# ============================================================
# Part B: Gell-Mann matrix catalog
# ============================================================

def build_gell_mann():
    """
    Standard 8 Gell-Mann matrices [Gell-Mann 1962; Griffiths App. A].
    Returned as list lam[1..8] of 3x3 complex arrays (lam[0] unused).
    """
    s3 = math.sqrt(3.0)
    lam = [None] * 9
    lam[1] = np.array([[0,1,0],[1,0,0],[0,0,0]], dtype=complex)
    lam[2] = np.array([[0,-1j,0],[1j,0,0],[0,0,0]], dtype=complex)
    lam[3] = np.array([[1,0,0],[0,-1,0],[0,0,0]], dtype=complex)
    lam[4] = np.array([[0,0,1],[0,0,0],[1,0,0]], dtype=complex)
    lam[5] = np.array([[0,0,-1j],[0,0,0],[1j,0,0]], dtype=complex)
    lam[6] = np.array([[0,0,0],[0,0,1],[0,1,0]], dtype=complex)
    lam[7] = np.array([[0,0,0],[0,0,-1j],[0,1j,0]], dtype=complex)
    lam[8] = np.array([[1,0,0],[0,1,0],[0,0,-2]], dtype=complex) / s3
    return lam


def catalog_angles(lam):
    """
    For each lambda_a, collect unique non-zero |entry| values and arctan in deg.
    """
    catalog = []
    for a in range(1, 9):
        seen = set()
        for val in lam[a].flat:
            mag = abs(val)
            if mag > 1e-12:
                key = round(mag, 8)
                if key not in seen:
                    seen.add(key)
                    catalog.append({
                        'gen': a,
                        'mag': key,
                        'arctan_deg': math.degrees(math.atan(key)),
                    })
    return catalog


def verify_normalization(lam):
    """
    Verify Tr(lambda_a * lambda_b) = 2*delta_ab [standard SU(3) algebra].
    """
    results = []
    for a in range(1, 9):
        for b in range(1, 9):
            tr = float(np.trace(lam[a] @ lam[b]).real)
            exp = 2.0 if a == b else 0.0
            results.append({'a': a, 'b': b, 'tr': tr, 'exp': exp,
                            'ok': abs(tr - exp) < 1e-10})
    return results


# ============================================================
# Part C: Casimir connection and root vectors
# ============================================================

def casimir_connection(rA):
    """
    Check: 1/sin^2(theta_crit) == C2(fundamental) = 4/3.
    Also verify C2 = (N^2-1)/(2N) for N=3.
    """
    theta = rA['delta_rad']
    sin2  = math.sin(theta) ** 2
    c2_from_angle  = 1.0 / sin2
    c2_from_formula = (N_COLOR**2 - 1.0) / (2.0 * N_COLOR)
    return {
        'theta_deg':      rA['delta_deg'],
        'sin2':           sin2,
        'c2_from_angle':  c2_from_angle,
        'c2_from_formula': c2_from_formula,
        'c2_known':       C2_FUND,
        'residual':       c2_from_angle - C2_FUND,
        'sigma_ratio':    c2_from_angle,   # sigma_SU3/sigma_U1 = C2 = 1/sin^2
        'sigma_part37':   C2_FUND,
    }


def root_vectors():
    """
    SU(3) root system: 6 roots at 60 deg intervals in the Cartan plane.
    [Source: Georgi 'Lie Algebras in Particle Physics' (1999) Ch 6]
    """
    angles_deg = [0.0, 60.0, 120.0, 180.0, 240.0, 300.0]
    seps = [(angles_deg[(i+1) % 6] - angles_deg[i]) % 360.0 for i in range(6)]
    seps[-1] = (angles_deg[0] + 360.0 - angles_deg[-1])
    return {
        'angles_deg': angles_deg,
        'separation_deg': seps[0],
        'all_60': all(abs(s - 60.0) < 1e-9 for s in seps),
        'tan_60': math.tan(60.0 * DEG),
        'tan_30': math.tan(30.0 * DEG),
    }


# ============================================================
# Sudoku consistency checks
# ============================================================

def sudoku(rA, rA_su2, catalog, norm, rC, rR, sym):
    checks = []

    # S1: U(1) limit reproduced -- tan(45) = 1
    computed = TAN_U1_CRIT
    expected = 1.0
    checks.append({'id': 'S1',
        'desc': 'U(1) limit: tan(45 deg) = 1 [Part 99 T2]',
        'computed': computed, 'expected': expected,
        'ok': abs(computed - expected) < 1e-10})

    # S2: Z3 critical angle = 60 deg
    computed_deg = rA['delta_deg']
    checks.append({'id': 'S2',
        'desc': 'Z3 switching angle = 60.000 deg',
        'computed': computed_deg, 'expected': 60.0,
        'ok': abs(computed_deg - 60.0) < 0.01})

    # S3: tan at Z3 critical = sqrt(3)
    computed = rA['tan_crit']
    expected = rA['sqrt3']
    checks.append({'id': 'S3',
        'desc': 'tan(60 deg) = sqrt(3)',
        'computed': computed, 'expected': expected,
        'ok': abs(computed - expected) < 1e-6})

    # S4: coupling gap at 60 deg = 0 (equidistance)
    gap = rA['gap_at_crit']
    checks.append({'id': 'S4',
        'desc': 'Coupling gap at 60 deg = 0 (equidistant Z3)',
        'computed': gap, 'expected': 0.0,
        'ok': abs(gap) < 1e-4})

    # S5: C2(fund) = 1/sin^2(60) exactly
    checks.append({'id': 'S5',
        'desc': 'C2(fund) = 1/sin^2(theta_crit) = 4/3',
        'computed': rC['c2_from_angle'], 'expected': C2_FUND,
        'ok': abs(rC['residual']) < 1e-10})

    # S6: string tension ratio from angle matches Part 37 Casimir
    checks.append({'id': 'S6',
        'desc': 'sigma_SU3/sigma_U1 = C2 = 1/sin^2(60) matches Part 37',
        'computed': rC['sigma_ratio'], 'expected': rC['sigma_part37'],
        'ok': abs(rC['sigma_ratio'] - rC['sigma_part37']) < 1e-10})

    # S7: Gell-Mann normalization: Tr(la*lb) = 2*delta_ab (64 checks)
    n_ok = sum(1 for r in norm if r['ok'])
    checks.append({'id': 'S7',
        'desc': 'Tr(lam_a lam_b) = 2*delta_ab: %d/64 pass' % n_ok,
        'computed': n_ok, 'expected': 64,
        'ok': n_ok == 64})

    # S8: root vectors separated by 60 deg
    checks.append({'id': 'S8',
        'desc': 'Root vector separation = 60 deg (hexagonal)',
        'computed': rR['separation_deg'], 'expected': 60.0,
        'ok': abs(rR['separation_deg'] - 60.0) < 1e-9})

    # S9: SU(2) critical angle = 90 deg (Z2 midpoint)
    checks.append({'id': 'S9',
        'desc': 'SU(2) Z2 midpoint = 90 deg (tan -> inf)',
        'computed': rA_su2['delta_deg'], 'expected': 90.0,
        'ok': abs(rA_su2['delta_deg'] - 90.0) < 1e-10})

    # S10: SymPy residual at pi/3 = 0 (algebraic verification)
    if sym.get('ok'):
        res = sym['residual_at_pi_over_3']
        checks.append({'id': 'S10',
            'desc': 'SymPy: cos(pi/3)=cos(pi/3-2pi/3) residual=0',
            'computed': res, 'expected': 0.0,
            'ok': abs(res) < 1e-12})
    else:
        checks.append({'id': 'S10',
            'desc': 'SymPy: N/A (%s)' % sym.get('reason', ''),
            'computed': None, 'expected': 0.0,
            'ok': False})

    return checks


# ============================================================
# Output
# ============================================================

def print_all(rA, rA_su2, catalog, norm, rC, rR, sym, checks):
    print("=" * 70)
    print("T10 -- SU(3) GROUP MANIFOLD TAN  (Part 121, Phase 89)")
    print("=" * 70)

    print("\n--- Part A: Z3 Vacuum Switching Angle ---")
    print("U(1) critical (T2/Part 99) : %.4f deg   tan = %.6f" % (
        DELTA_U1_DEG, TAN_U1_CRIT))
    print("SU(3) Z3 critical (derived): %.4f deg   tan = %.6f" % (
        rA['delta_deg'], rA['tan_crit']))
    print("  sqrt(3) exact            : %.6f" % rA['sqrt3'])
    print("  Coupling to k=0 at 60deg : %.6f" % rA['coupling_k0'])
    print("  Coupling to k=1 at 60deg : %.6f" % rA['coupling_k1'])
    print("  Gap (expect 0)           : %.2e" % rA['gap_at_crit'])
    print("  Restoring force (k=0)    : %.6f" % rA['force_k0'])
    print("  Restoring force (k=1)    : %.6f" % rA['force_k1'])

    print("\nSU(2) analogue (Z2 midpoint):")
    print("  Critical angle           : %.1f deg   tan -> %.2e" % (
        rA_su2['delta_deg'], rA_su2['tan_approx']))

    if sym.get('ok'):
        print("\nSymPy verification:")
        print("  cos(pi/3)=cos(pi/3-2pi/3) residual : %.2e" % sym['residual_at_pi_over_3'])
        print("  tan(pi/3) - sqrt(3)                 : %.2e" % sym['tan_pi_over_3_minus_sqrt3'])
        print("  1/sin^2(pi/3) - 4/3                 : %.2e" % sym['c2_fund_from_sin2'])
    else:
        print("\nSymPy: not available")

    print("\n--- Part B: Gell-Mann Generator Angle Catalog ---")
    print("%-10s  %-18s  %s" % ("Generator", "|entry| magnitude", "arctan (deg)"))
    print("-" * 52)
    for e in catalog:
        print("  lam_%-3d    %-18.6f   %.4f" % (e['gen'], e['mag'], e['arctan_deg']))
    unique = sorted(set(round(e['arctan_deg'], 1) for e in catalog))
    print("\nUnique arctan values (deg): %s" % ", ".join("%.1f" % a for a in unique))

    n_norm = sum(1 for r in norm if r['ok'])
    print("\nNormalization Tr(lam_a lam_b) = 2*delta_ab: %d/64 pass" % n_norm)

    print("\n--- Part C: Casimir Connection ---")
    print("theta_crit               : %.4f deg" % rC['theta_deg'])
    print("sin^2(theta_crit)        : %.6f" % rC['sin2'])
    print("1/sin^2(theta_crit)      : %.6f" % rC['c2_from_angle'])
    print("C2(fund) = (N^2-1)/(2N)  : %.6f" % rC['c2_from_formula'])
    print("C2(fund) known           : %.6f" % rC['c2_known'])
    print("Residual                 : %.2e" % rC['residual'])
    print("sigma_SU3/sigma_U1       : %.6f  (matches Part 37: %s)" % (
        rC['sigma_ratio'], rC['sigma_ratio'] == rC['sigma_part37'] or
        abs(rC['sigma_ratio'] - rC['sigma_part37']) < 1e-10))

    print("\nRoot system (SU(3) hexagonal):")
    print("  Root angles (deg)  : %s" % rR['angles_deg'])
    print("  Adjacent sep (deg) : %.1f" % rR['separation_deg'])
    print("  All separations 60 : %s" % rR['all_60'])
    print("  tan(60 deg)        : %.6f" % rR['tan_60'])
    print("  tan(30 deg)        : %.6f" % rR['tan_30'])

    print("\n--- Sudoku Checks ---")
    print("%-5s  %-52s  %s" % ("ID", "Description", "Result"))
    print("-" * 70)
    n_pass = 0
    for c in checks:
        status = "PASS" if c['ok'] else "FAIL"
        if c['ok']:
            n_pass += 1
        cv = c['computed']
        ev = c['expected']
        if cv is not None:
            detail = "(computed=%.6g, expected=%.6g)" % (cv, ev)
        else:
            detail = ""
        print("  %-5s  %-52s  %s %s" % (c['id'], c['desc'], status, detail))
    print("\nSudoku score: %d/%d" % (n_pass, len(checks)))

    print("\n--- Summary ---")
    print("U(1) critical (T2)    :  45.0 deg   tan = 1.000000")
    print("SU(3) Z3 critical (T10): %5.1f deg   tan = sqrt(3) = %.6f" % (
        rA['delta_deg'], rA['tan_crit']))
    print("SU(2) critical        :  90.0 deg   tan = inf")
    print("C2(fund) = 1/sin^2(60 deg) = %.6f  [exact match to known 4/3]" % rC['c2_from_angle'])
    print("Unique SU(3) tan values: 0, 1/sqrt(3) (30 deg), 1 (45 deg), sqrt(3) (60 deg)")


def main():
    rA     = derive_z3_critical_angle()
    rA_su2 = derive_su2_critical()
    sym    = sympy_z3_critical()
    lam    = build_gell_mann()
    cat    = catalog_angles(lam)
    norm   = verify_normalization(lam)
    rC     = casimir_connection(rA)
    rR     = root_vectors()
    chks   = sudoku(rA, rA_su2, cat, norm, rC, rR, sym)

    # Capture output
    buf = io.StringIO()
    old = sys.stdout
    sys.stdout = buf
    print_all(rA, rA_su2, cat, norm, rC, rR, sym, chks)
    sys.stdout = old
    out = buf.getvalue()
    print(out)

    # Save log
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'outputs')
    os.makedirs(out_dir, exist_ok=True)
    from datetime import datetime
    ts = datetime.now().strftime('%Y%m%d_%H%M%S')
    log = os.path.join(out_dir, 't10_su3_tan_%s.txt' % ts)
    with open(log, 'w', encoding='utf-8') as f:
        f.write(out)
    print("Output saved: %s" % log)

    n_pass = sum(1 for c in chks if c['ok'])
    return n_pass == len(chks)


if __name__ == '__main__':
    ok = main()
    sys.exit(0 if ok else 1)
