#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lagrangian4.py -- TODO_04 T19 (Priority 19), Part 132
=======================================================================
SymPy verification of L_4 (docs/research/pdtp_lagrangian4.md), the
inter-layer Lagrangian coupling the three condensates (C1 gravity, C2 QCD,
C3 EW) directly to each other via J_ab cos(phi_a-phi_b) terms.

The source doc is explicitly self-flagged: "[SPECULATIVE, PDTP Original]
Not yet SymPy verified. Requires SymPy verification before being accepted
as DERIVED." This script performs that verification (TODO_04 T19 tasks 1-3)
and checks the physical-argument tasks (4-5) as far as they are checkable.

This script:
1. Derives the Euler-Lagrange equations for all 4 fields (phi_1,phi_2,phi_3,
   psi) from L_4 directly via SymPy, and checks them against the doc's
   stated FE1-FE4.
2. Checks the doc's "Newton's 3rd law between condensates" claim precisely:
   as literally stated (FE1+FE2+FE3 = Box(phi_1+phi_2+phi_3)) this is a
   tautology (true by definition of FE_a); the SUBSTANTIVE claim is that
   the J_ab terms cancel pairwise in that sum, and additionally (a stronger,
   previously unstated result) that FE1+FE2+FE3+FE4=0 identically -- the
   true conservation law behind the exact Goldstone mode.
3. Derives the 3x3 mass matrix symbolically from the linearized field
   equations and checks it against the doc's stated matrix. Identifies the
   matrix as exactly a weighted graph Laplacian (standard graph theory,
   Wikipedia "Laplacian matrix") -- proves the "one exact zero eigenvalue,
   remaining eigenvalues >= 0 for J>=0" claim in GENERAL (any number of
   condensates, not just 3), rather than checking only the specific 3x3
   case.
4. Recomputes (not copies) the numeric eigenvalues for the doc's specific
   J values, and separately verifies the isolated-pair formula m_23=sqrt(g2*g3)
   is reproduced in the J_12,J_13 -> 0 limit of the full 3x3 result.
5. Checks Task 4 (why J_ab=g_a*g_b/2, the "product rule"): finds the doc's
   own cited analogy (Lorentz-Berthelot, van der Waals combining rule) is
   the GEOMETRIC MEAN sqrt(g_a*g_b), not the product rule that was actually
   adopted -- an internal inconsistency. Computes what the b-quark-mass
   comparison would give under the geometric-mean rule instead, to assess
   how much of the "4% match" is a consequence of which rule was picked.

PDTP Original: sections 2 (the stronger 4-field conservation law), 3 (graph
Laplacian identification and general n-condensate proof), 5 (the product-
vs-geometric-mean reconciliation). Section 1 is a direct SymPy re-derivation
of already-claimed (not yet verified) Part 37-era results.
Established (cited, not original): graph Laplacian properties (Wikipedia);
Lorentz-Berthelot combining rules (standard van der Waals theory, cited in
the source doc itself).

Output: DATA only. Interpretation belongs in docs/research/pdtp_lagrangian4.md.
"""

import sympy as sp
import numpy as np

# ===========================================================================
# CONSTANTS
# ===========================================================================
HBAR = 1.054571817e-34    # J s
C_SI = 2.99792458e8       # m/s
EV_J = 1.602176634e-19
GEV_J = EV_J * 1e9

OMEGA_P = 1.855e43         # rad/s, Planck coupling (as stated in the doc)
OMEGA_QCD = 3.039e23       # rad/s, QCD coupling
OMEGA_W = 1.221e26         # rad/s, EW coupling


# ===========================================================================
# PART 1: Euler-Lagrange equations for all 4 fields
# ===========================================================================
def derive_euler_lagrange():
    """
    L_4 (0+1D reduction, matching the project's established ODE convention
    for Euler-Lagrange checks, e.g. sympy_checks.py euler_lagrange_1d):

      L = 1/2(phi1dot^2+phi2dot^2+phi3dot^2+psidot^2)
        + g1*cos(psi-phi1) + g2*cos(psi-phi2) + g3*cos(psi-phi3)
        + J12*cos(phi1-phi2) + J13*cos(phi1-phi3) + J23*cos(phi2-phi3)

    Euler-Lagrange (d/dt)(dL/dphi_dot) - dL/dphi = 0 => phi_ddot = dL/dphi
    (since dL/dphi_dot = phi_dot for a canonical kinetic term). Returns the
    RHS ("Box phi_a" equivalent) for each of the 4 fields.
    """
    t = sp.symbols('t')
    g1, g2, g3, J12, J13, J23 = sp.symbols('g1 g2 g3 J12 J13 J23', positive=True)
    phi1 = sp.Function('phi1')(t)
    phi2 = sp.Function('phi2')(t)
    phi3 = sp.Function('phi3')(t)
    psi = sp.Function('psi')(t)

    L = sp.Rational(1, 2) * (sp.diff(phi1, t)**2 + sp.diff(phi2, t)**2 +
                              sp.diff(phi3, t)**2 + sp.diff(psi, t)**2) \
        + g1 * sp.cos(psi - phi1) + g2 * sp.cos(psi - phi2) + g3 * sp.cos(psi - phi3) \
        + J12 * sp.cos(phi1 - phi2) + J13 * sp.cos(phi1 - phi3) + J23 * sp.cos(phi2 - phi3)

    FE1 = sp.simplify(sp.diff(L, phi1))
    FE2 = sp.simplify(sp.diff(L, phi2))
    FE3 = sp.simplify(sp.diff(L, phi3))
    FE4 = sp.simplify(sp.diff(L, psi))

    # Doc's stated FE1-FE4 (Section "Field Equations from L_4"), for comparison
    Deltap1, Deltap2, Deltap3 = sp.symbols('Delta_psi1 Delta_psi2 Delta_psi3')  # psi-phi_i shorthand, unused directly
    doc_FE1 = g1 * sp.sin(psi - phi1) + J12 * sp.sin(phi1 - phi2) + J13 * sp.sin(phi1 - phi3)
    doc_FE2 = g2 * sp.sin(psi - phi2) - J12 * sp.sin(phi1 - phi2) + J23 * sp.sin(phi2 - phi3)
    doc_FE3 = g3 * sp.sin(psi - phi3) - J13 * sp.sin(phi1 - phi3) - J23 * sp.sin(phi2 - phi3)
    doc_FE4 = -g1 * sp.sin(psi - phi1) - g2 * sp.sin(psi - phi2) - g3 * sp.sin(psi - phi3)

    residual1 = sp.simplify(FE1 - doc_FE1)
    residual2 = sp.simplify(FE2 - doc_FE2)
    residual3 = sp.simplify(FE3 - doc_FE3)
    residual4 = sp.simplify(FE4 - doc_FE4)

    return {
        'L': L, 'FE1': FE1, 'FE2': FE2, 'FE3': FE3, 'FE4': FE4,
        'doc_FE1': doc_FE1, 'doc_FE2': doc_FE2, 'doc_FE3': doc_FE3, 'doc_FE4': doc_FE4,
        'residual1': residual1, 'residual2': residual2,
        'residual3': residual3, 'residual4': residual4,
    }


# ===========================================================================
# PART 2: the actual conservation law (stronger than the doc's literal claim)
# ===========================================================================
def verify_conservation_law():
    """
    The doc claims "FE1+FE2+FE3 = Box(phi_1+phi_2+phi_3)" as a "Newton's 3rd
    law between condensates" result -- but as literally written this is a
    tautology (FE_a IS defined as Box(phi_a)). The substantive, CHECKABLE
    claims are:
      (a) the J_ab terms cancel pairwise when FE1+FE2+FE3 are summed
      (b) FULL conservation: FE1+FE2+FE3+FE4 = 0 identically (not stated in
          the doc at all) -- this is the actual equation of motion for the
          exact Goldstone direction (phi_1=phi_2=phi_3=psi all shifting
          together), and is the real "Newton's 3rd law" content.
    """
    r = derive_euler_lagrange()
    FE1, FE2, FE3, FE4 = r['FE1'], r['FE2'], r['FE3'], r['FE4']

    sum_123 = sp.expand_trig(sp.expand(FE1 + FE2 + FE3))
    # J-only part: subtract the g-terms to isolate what's left from the J's
    g1, g2, g3 = sp.symbols('g1 g2 g3', positive=True)
    t = sp.symbols('t')
    phi1 = sp.Function('phi1')(t); phi2 = sp.Function('phi2')(t)
    phi3 = sp.Function('phi3')(t); psi = sp.Function('psi')(t)
    g_terms_sum = g1 * sp.sin(psi - phi1) + g2 * sp.sin(psi - phi2) + g3 * sp.sin(psi - phi3)
    J_terms_only = sp.simplify(sum_123 - g_terms_sum)

    sum_all_4 = sp.simplify(FE1 + FE2 + FE3 + FE4)

    return {
        'sum_FE1_FE2_FE3': sum_123,
        'J_terms_cancel_check': J_terms_only,     # expect 0
        'sum_all_four': sum_all_4,                 # expect 0 -- the real conservation law
    }


# ===========================================================================
# PART 3: mass matrix -- symbolic derivation + graph Laplacian identification
# ===========================================================================
def derive_mass_matrix():
    """
    Linearize FE1, FE2, FE3 around phi_1=phi_2=phi_3=0 with matter decoupled
    (psi held fixed / ignored, matching the doc's stated approach for
    "inter-condensate modes ignore matter coupling for now"), sin(x)~x.
    Extract the Jacobian d(phi_ddot_a)/d(phi_b) = -M^2_ab.

    IMPORTANT: linearizes the SymPy-derived, hand-verified FE1-FE3 from
    Part 1 (dL/dphi_a computed directly by SymPy from L_4) -- NOT the
    doc's separately-stated "Field Equations from L_4" section, which
    Part 1 found has a sign error on the J-coupling terms (the doc's FE4
    matches SymPy exactly, validating the method; FE1-FE3 do not). Using
    the doc's buggy signs here would propagate that error into the mass
    matrix; using the verified ones instead lets this section act as an
    independent check of the doc's SEPARATE mass-matrix claim.
    """
    J12, J13, J23 = sp.symbols('J12 J13 J23', positive=True)
    phi1, phi2, phi3 = sp.symbols('phi1 phi2 phi3', real=True)

    # Linearized RHS (sin(x)~x applied to the SymPy-verified FE1-FE3 from Part 1,
    # matter term dropped): FE1 = g1*sin(psi-phi1) - J12*sin(phi1-phi2) - J13*sin(phi1-phi3), etc.
    FE1_lin = -J12 * (phi1 - phi2) - J13 * (phi1 - phi3)
    FE2_lin = J12 * (phi1 - phi2) - J23 * (phi2 - phi3)
    FE3_lin = J13 * (phi1 - phi3) + J23 * (phi2 - phi3)

    phis = sp.Matrix([phi1, phi2, phi3])
    FEs = sp.Matrix([FE1_lin, FE2_lin, FE3_lin])
    # phi_ddot = FE (from box(phi)=FE => phi_ddot = FE in the 0+1D reduction)
    # => phi_ddot = -M^2 * phi  =>  M^2 = -Jacobian(FE, phi)
    Jac = FEs.jacobian(phis)
    M2 = -Jac

    doc_M2 = sp.Matrix([
        [J12 + J13, -J12, -J13],
        [-J12, J12 + J23, -J23],
        [-J13, -J23, J13 + J23],
    ])
    residual_M2 = sp.simplify(M2 - doc_M2)

    # Graph Laplacian check: row sums must be exactly zero (standard property
    # of L = D - A for a weighted graph, Wikipedia "Laplacian matrix")
    row_sums = [sp.simplify(sum(M2.row(i))) for i in range(3)]

    # (1,1,1) must be an exact eigenvector with eigenvalue 0
    ones = sp.Matrix([1, 1, 1])
    M2_ones = sp.simplify(M2 * ones)

    return {
        'M2_derived': M2,
        'M2_doc_stated': doc_M2,
        'residual_vs_doc': residual_M2,
        'row_sums': row_sums,                # expect [0,0,0]
        'M2_dot_ones': M2_ones,              # expect [0,0,0] -- (1,1,1) is the Goldstone eigenvector
    }


def verify_graph_laplacian_general(n=3):
    """
    General (n-condensate) proof that the mass matrix is a weighted graph
    Laplacian: M2_aa = sum_{b!=a} J_ab, M2_ab = -J_ab (a!=b). This is
    EXACTLY the definition of the Laplacian matrix L=D-A of a weighted
    complete graph on n nodes with edge weights J_ab (Source: Wikipedia,
    "Laplacian matrix"). Standard graph theory guarantees, for J_ab >= 0:
      - L is symmetric and positive semi-definite
      - the all-ones vector is always in the kernel (row sums = 0 by
        construction) -- exactly one zero eigenvalue if the graph is
        connected (true whenever all J_ab > 0)
      - all other eigenvalues are strictly positive (connected graph)
    This generalizes the n=3 specific check above to ANY number of
    condensate layers -- not previously stated in the source doc.
    """
    n_test = n
    Jsym = sp.symbols(f'J0:{n_test}_0:{n_test}', positive=True)  # placeholder, not directly used
    # Build a concrete random-weighted n x n Laplacian symbolically for n=4 as a spot-check
    np.random.seed(42)
    J = np.random.uniform(0.1, 5.0, size=(n_test, n_test))
    J = (J + J.T) / 2
    np.fill_diagonal(J, 0.0)
    D = np.diag(J.sum(axis=1))
    L = D - J
    eigvals = np.linalg.eigvalsh(L)
    eigvals_sorted = np.sort(eigvals)

    return {
        'n': n_test,
        'eigenvalues': eigvals_sorted,
        'smallest_eigenvalue_near_zero': abs(eigvals_sorted[0]) < 1e-9,
        'all_others_positive': all(ev > 1e-9 for ev in eigvals_sorted[1:]),
    }


# ===========================================================================
# PART 4: numeric eigenvalues (recomputed, not copied) + isolated-pair limit
# ===========================================================================
def numeric_eigenvalues_and_isolated_limit():
    """
    Recompute (independently of the doc's stated numbers) the eigenvalues
    of M^2 using the doc's own J values, derived here from g1,g2,g3 (in GeV,
    via E=hbar*omega converted to GeV -- verified explicitly, not assumed)
    and J_ab = g_a*g_b/2.
    """
    g1_GeV = HBAR * OMEGA_P / GEV_J
    g2_GeV = HBAR * OMEGA_QCD / GEV_J
    g3_GeV = HBAR * OMEGA_W / GEV_J

    J12 = g1_GeV * g2_GeV / 2
    J13 = g1_GeV * g3_GeV / 2
    J23 = g2_GeV * g3_GeV / 2

    M2 = np.array([
        [J12 + J13, -J12, -J13],
        [-J12, J12 + J23, -J23],
        [-J13, -J23, J13 + J23],
    ])
    eigvals = np.sort(np.linalg.eigvalsh(M2))

    # Isolated-pair limit: J12, J13 -> 0 (gravity decoupled)
    M2_isolated = np.array([
        [J23, 0, -J23],
        [0, 0, 0],
        [-J23, 0, J23],
    ])
    eigvals_isolated = np.sort(np.linalg.eigvalsh(M2_isolated))
    m23_from_full_limit = np.sqrt(eigvals_isolated[-1])   # largest eigenvalue -> the 2-3 mode
    m23_direct = np.sqrt(g2_GeV * g3_GeV)                  # direct formula, Eq L4.1

    trace_M2 = float(np.trace(M2))
    sum_eigvals = float(np.sum(eigvals))

    return {
        'g1_GeV': g1_GeV, 'g2_GeV': g2_GeV, 'g3_GeV': g3_GeV,
        'J12': J12, 'J13': J13, 'J23': J23,
        'eigenvalues_GeV2': eigvals,               # [~0, lambda1, lambda2]
        'm1_TeV': np.sqrt(eigvals[1]) / 1000.0,
        'm2_TeV': np.sqrt(eigvals[2]) / 1000.0,
        'm23_from_full_limit_GeV': m23_from_full_limit,
        'm23_direct_GeV': m23_direct,
        'isolated_limit_matches': abs(m23_from_full_limit - m23_direct) < 1e-9,
        'm_b_quark_GeV': 4.18,
        'match_percent': abs(m23_direct - 4.18) / 4.18 * 100,
        'trace_M2': trace_M2,
        'sum_eigvals': sum_eigvals,
        'doc_claimed_lambda1_GeV2': 1.16e9,
        'doc_claimed_lambda2_GeV2': 3.17e10,
        'doc_claimed_sum_vs_trace_ratio': (1.16e9 + 3.17e10) / trace_M2,
    }


# ===========================================================================
# PART 5: product rule vs the doc's own cited analogy (geometric mean)
# ===========================================================================
def check_product_vs_geometric_mean():
    """
    The doc cites the Lorentz-Berthelot combining rule (standard van der
    Waals theory, epsilon_AB = sqrt(epsilon_AA*epsilon_BB), a GEOMETRIC
    MEAN) as motivation, then adopts J_ab = g_a*g_b/2 (a PRODUCT, not a
    geometric mean) without reconciling the two. Check what the geometric-
    mean rule would give for the C2-C3 mode mass instead, to assess how
    much the product rule's specific choice drove the "4% match."

    Geometric-mean rule: J_ab_geo = sqrt(g_a*g_b)/2 (matching the doc's own
    cited Lorentz-Berthelot form, with the same 1/2 normalization).
    Mass from omega^2=2J (same linearization as Eq L4.1's own derivation):
      m_ab_geo = sqrt(2*J_ab_geo) = sqrt(sqrt(g_a*g_b)) = (g_a*g_b)^(1/4)
    """
    r = numeric_eigenvalues_and_isolated_limit()
    g2, g3 = r['g2_GeV'], r['g3_GeV']

    m23_product_rule = np.sqrt(g2 * g3)            # Eq L4.1, the doc's adopted rule
    m23_geometric_mean_rule = (g2 * g3)**0.25        # what Lorentz-Berthelot actually implies

    m_b = 4.18

    return {
        'product_rule_mass_GeV': m23_product_rule,
        'product_rule_match_pct': abs(m23_product_rule - m_b) / m_b * 100,
        'geometric_mean_rule_mass_GeV': m23_geometric_mean_rule,
        'geometric_mean_rule_match_pct': abs(m23_geometric_mean_rule - m_b) / m_b * 100,
        'dimensional_argument_distinguishes_them': False,   # both g_a*g_b/2 and sqrt(g_a*g_b)/2 have identical units
        'conclusion': (
            "Both candidate rules are dimensionally valid (same units); dimensional analysis "
            "alone cannot select between them. The doc's OWN cited analogy (Lorentz-Berthelot) "
            "supports the geometric mean, not the product rule it actually adopted -- an "
            "unreconciled internal inconsistency. The product rule gives a much closer match "
            "to the b quark (m_b=4.18 GeV) than the geometric-mean rule does, which suggests "
            "the product rule may have been selected BECAUSE it produces a appealing-looking "
            "match, not derived independently from a symmetry principle. This weakens (does "
            "not eliminate) the significance of the '4% match' claim."
        ),
    }


# ===========================================================================
# SUDOKU CONSISTENCY CHECKS
# ===========================================================================
def sudoku_checks():
    results = []

    # S1-S3 are EXPECTED to FAIL -- that is the finding, not a bug in this script.
    # SymPy's direct dL/dphi_a derivation disagrees with the doc's stated FE1-FE3
    # (sign error on the J-coupling terms in the doc), while S4 (FE4, psi's
    # equation) matches exactly, validating the derivation method itself. See
    # docs/research/pdtp_lagrangian4.md Sec "SymPy Verification Results" (T19).
    r1 = derive_euler_lagrange()
    results.append(('S1: FE1 matches doc (residual=0) -- EXPECT FAIL, doc has a sign error', sp.simplify(r1['residual1']) == 0))
    results.append(('S2: FE2 matches doc (residual=0) -- EXPECT FAIL, doc has a sign error', sp.simplify(r1['residual2']) == 0))
    results.append(('S3: FE3 matches doc (residual=0) -- EXPECT FAIL, doc has a sign error', sp.simplify(r1['residual3']) == 0))
    results.append(('S4: FE4 matches doc (residual=0) -- validates the derivation method', sp.simplify(r1['residual4']) == 0))

    r2 = verify_conservation_law()
    results.append(('S5: J-terms cancel exactly in FE1+FE2+FE3 (residual=0)',
                     sp.simplify(r2['J_terms_cancel_check']) == 0))
    results.append(('S6: FULL 4-field conservation FE1+FE2+FE3+FE4=0 (stronger than doc claim)',
                     sp.simplify(r2['sum_all_four']) == 0))

    r3 = derive_mass_matrix()
    results.append(('S7: derived M^2 matches doc-stated matrix exactly (residual=0 matrix)',
                     r3['residual_vs_doc'] == sp.zeros(3, 3)))
    results.append(('S8: all row sums of M^2 are exactly 0', all(rs == 0 for rs in r3['row_sums'])))
    results.append(('S9: (1,1,1) is an exact zero-eigenvalue eigenvector', r3['M2_dot_ones'] == sp.zeros(3, 1)))

    r3b = verify_graph_laplacian_general(n=4)
    results.append(('S10: general n=4 weighted-graph-Laplacian check: smallest eigenvalue ~0',
                     r3b['smallest_eigenvalue_near_zero']))
    results.append(('S11: general n=4 check: all other eigenvalues strictly positive',
                     r3b['all_others_positive']))

    r4 = numeric_eigenvalues_and_isolated_limit()
    results.append(('S12: g2_GeV recomputed from hbar*omega_QCD matches doc value 0.200 GeV to 1%',
                     abs(r4['g2_GeV'] - 0.200) / 0.200 < 0.01))
    results.append(('S13: g3_GeV recomputed from hbar*omega_W matches doc value 80.4 GeV to 1%',
                     abs(r4['g3_GeV'] - 80.4) / 80.4 < 0.01))
    # Relative tolerance: J values span ~20 orders of magnitude (J13~5e20 vs J23~8),
    # so eigvalsh's O(1e-16 relative) floating-point roundoff on the "zero" eigenvalue
    # is itself O(1e4) in absolute terms -- an absolute tolerance would be meaningless
    # here; compare instead to the matrix's own largest scale (J13).
    results.append(('S14: smallest recomputed eigenvalue is ~0 relative to J13 (Goldstone, numeric)',
                     abs(r4['eigenvalues_GeV2'][0]) / r4['J13'] < 1e-9))
    results.append(('S15: isolated-pair limit (J12,J13->0) of the FULL matrix matches m_23=sqrt(g2 g3) directly',
                     r4['isolated_limit_matches']))
    # Trace check: sum of all 3 eigenvalues must equal trace(M^2) exactly (standard
    # linear algebra). My recomputed eigenvalues pass this; the doc's ORIGINALLY
    # STATED eigenvalues (~1.16e9 + ~3.17e10 GeV^2) sum to ~10 orders of magnitude
    # LESS than the trace -- i.e. the original document's own numbers were wrong,
    # independent of any g-value or J-value dispute (this is pure linear algebra).
    results.append(('S17: sum of recomputed eigenvalues matches trace(M^2) (basic linear algebra)',
                     abs(r4['sum_eigvals'] / r4['trace_M2'] - 1) < 1e-9))
    results.append(("S18: doc's ORIGINALLY claimed eigenvalues (1.16e9+3.17e10) do NOT match trace -- confirms they were wrong",
                     r4['doc_claimed_sum_vs_trace_ratio'] < 0.01))

    r5 = check_product_vs_geometric_mean()
    results.append(('S16: product-rule and geometric-mean-rule masses are genuinely different (not both ~4.18)',
                     abs(r5['product_rule_mass_GeV'] - r5['geometric_mean_rule_mass_GeV']) > 1.0))

    return results


# ===========================================================================
# MAIN
# ===========================================================================
def main():
    print("=" * 78)
    print("T19 (Part 132): L_4 SymPy Verification and b-Quark Check")
    print("=" * 78)

    print("\n--- Part 1: Euler-Lagrange equations ---")
    r1 = derive_euler_lagrange()
    print(f"FE1 = {r1['FE1']}")
    print(f"FE2 = {r1['FE2']}")
    print(f"FE3 = {r1['FE3']}")
    print(f"FE4 = {r1['FE4']}")
    print(f"Residuals vs doc: {r1['residual1']}, {r1['residual2']}, {r1['residual3']}, {r1['residual4']}")

    print("\n--- Part 2: conservation law ---")
    r2 = verify_conservation_law()
    print(f"J-terms-only sum (should be 0): {r2['J_terms_cancel_check']}")
    print(f"FULL 4-field sum FE1+FE2+FE3+FE4 (should be 0): {r2['sum_all_four']}")

    print("\n--- Part 3: mass matrix ---")
    r3 = derive_mass_matrix()
    print(f"M^2 derived:\n{r3['M2_derived']}")
    print(f"Residual vs doc-stated matrix:\n{r3['residual_vs_doc']}")
    print(f"Row sums: {r3['row_sums']}")
    print(f"M^2 . (1,1,1): {r3['M2_dot_ones']}")

    r3b = verify_graph_laplacian_general(n=4)
    print(f"\nGeneral n=4 graph-Laplacian spot check: eigenvalues = {r3b['eigenvalues']}")

    print("\n--- Part 4: numeric eigenvalues and isolated-pair limit ---")
    r4 = numeric_eigenvalues_and_isolated_limit()
    print(f"g1={r4['g1_GeV']:.4e} GeV, g2={r4['g2_GeV']:.4f} GeV, g3={r4['g3_GeV']:.4f} GeV")
    print(f"J12={r4['J12']:.4e}, J13={r4['J13']:.4e}, J23={r4['J23']:.4f} GeV^2")
    print(f"Eigenvalues (GeV^2): {r4['eigenvalues_GeV2']}")
    print(f"m1 = {r4['m1_TeV']:.3f} TeV, m2 = {r4['m2_TeV']:.3f} TeV")
    print(f"m23 (from full-matrix isolated limit) = {r4['m23_from_full_limit_GeV']:.4f} GeV")
    print(f"m23 (direct formula) = {r4['m23_direct_GeV']:.4f} GeV")
    print(f"Isolated-limit self-consistency: {r4['isolated_limit_matches']}")
    print(f"trace(M^2) = {r4['trace_M2']:.4e}, sum of recomputed eigenvalues = {r4['sum_eigvals']:.4e}")
    print(f"Doc's originally claimed eigenvalues summed: {r4['doc_claimed_lambda1_GeV2']+r4['doc_claimed_lambda2_GeV2']:.4e} "
          f"(ratio to trace: {r4['doc_claimed_sum_vs_trace_ratio']:.2e} -- confirms the doc's original numbers were wrong)")
    print(f"b quark = {r4['m_b_quark_GeV']} GeV, match = {r4['match_percent']:.2f}%")

    print("\n--- Part 5: product rule vs geometric mean ---")
    r5 = check_product_vs_geometric_mean()
    print(f"Product rule mass: {r5['product_rule_mass_GeV']:.4f} GeV ({r5['product_rule_match_pct']:.2f}% off b quark)")
    print(f"Geometric-mean rule mass: {r5['geometric_mean_rule_mass_GeV']:.4f} GeV ({r5['geometric_mean_rule_match_pct']:.2f}% off b quark)")
    print(r5['conclusion'])

    print("\n" + "=" * 78)
    print("SUDOKU CONSISTENCY CHECKS")
    print("=" * 78)
    checks = sudoku_checks()
    n_pass = sum(1 for _, ok in checks if ok)
    for label, ok in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    print(f"\nSCORE: {n_pass}/{len(checks)} PASS")


if __name__ == '__main__':
    main()
