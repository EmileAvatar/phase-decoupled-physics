================================================================================
PART 32: KOIDE-LATTICE ANALYSIS
Bottom-up derivation: particle masses -> lattice parameters -> G
================================================================================

================================================================================
1. KOIDE FORMULA VERIFICATION
================================================================================

  Source: Y. Koide, Lett. Nuovo Cimento 34, 201 (1982)
  Source: PDG 2024, https://pdg.lbl.gov/

  Charged leptons (e, mu, tau):
    m_e   = 0.51099895 MeV
    m_mu  = 105.6583755 MeV
    m_tau = 1776.86 MeV
    Q     = 0.66666051
    2/3   = 0.66666667
    |Q - 2/3| = 6.16e-06  (< 10^-5: YES)

  Quark triplets:
  Source: W. Rodejohann & H. Zhang, arXiv:1101.5525 (2011)
  Source: A. Rivero, arXiv:1111.7232 (2011)

  Triplet                                   Q         |Q-2/3|     delta 
  ----------------------------------------------------------------------
  u, c, t (up-type generational)             0.84894  1.8227e-01  1.7589
  d, s, b (down-type generational)           0.73122  6.4552e-02  1.5451
  c, b, t (heavy quarks)                     0.66937  2.7020e-03  1.4199
  -s, c, b (Rivero signed)                   0.67504  8.3768e-03  0.8665

================================================================================
2. BRANNEN PARAMETERIZATION OF LEPTON MASSES
================================================================================

  Source: C.A. Brannen, 'The Lepton Masses' (2006)
  Source: docs/research/koide_derivation.md

  Ansatz: sqrt(m_i) = mu * (1 + delta * cos(theta_0 + 2*pi*i/3))
  Koide condition: delta = sqrt(2)  (Q = 2/3 iff delta = sqrt(2))

  Fitted parameters:
    mu     = 17.715562 MeV^(1/2)
    theta_0 = 0.222230 rad = 12.7328 deg
    theta_0 ~ 2/9 = 0.222222 rad? diff = 7.41e-06
    delta   = 1.414201  (sqrt(2) = 1.414214)

  The Koide base mass scale:
    M_0 = mu^2 = 313.8411 MeV
    M_0 = 5.5947e-28 kg
    M_0/m_e  = 614.1718  (about 614 electron masses)
    M_0/m_mu = 2.9703  (close to: 620.3048 = 3*m_mu/m_e ratio hint)
    Note: M_0 ~ m_proton/3 ~ constituent quark mass
    m_p/3 = 312.7573 MeV (proton mass / 3)

  Fit verification:
  Note: Brannen assigns i=0 to heaviest (tau), i=1 to electron, i=2 to muon.
  Lepton      i     sqrt(m) meas.  sqrt(m) pred.  Residual      Rel err 
  --------------------------------------------------------------------
  electron       1      0.714842      0.714685      0.000157    0.0220%
  muon           2     10.279026     10.278957      0.000069    0.0007%
  tau            0     42.152817     42.153043     -0.000226    0.0005%

================================================================================
3. MASS AND LENGTH SCALES DERIVABLE FROM PARTICLE PHYSICS ALONE
================================================================================

  The Koide formula gives RATIOS only -- not the absolute scale.
  The scale mu (= M_0^{1/2}) is set by whichever mass we measure.

  Candidate mass scales (all derived from particle masses, no G):

  Scale                                     Mass (MeV)    Mass (kg)       Length hbar/(mc) [m]
  -------------------------------------------------------------------------------------
  m_e (electron)                                  0.5110      9.1094e-31      3.8616e-13
  m_mu (muon)                                   105.6584      1.8835e-28      1.8676e-15
  m_tau (tau)                                  1776.8600      3.1675e-27      1.1105e-16
  M_0 = mu^2 (Koide base)                       313.8411      5.5947e-28      6.2875e-16
  M_geom = (m_e*m_mu*m_tau)^{1/3}                45.7782      8.1607e-29      4.3105e-15
  M_hop = M_0/2 (hopping term)                  156.9206      2.7974e-28      1.2575e-15
  m_p (proton)                                  938.2720      1.6726e-27      2.1031e-16

================================================================================
4. SYSTEMATIC MAXWELL-TERM SEARCH
   Testing candidates for the lattice spacing 'a'
   G_pred = c^3 * a^2 / hbar   (PDTP formula with K = hbar/(4*pi*c))
================================================================================

  PDTP G formula source: simulations/substitution_chains.py, Part 29
  K = hbar/(4*pi*c) = 2.7993e-44 kg*m  (G-free, uses only hbar and c)

    #  Candidate                                           a (m)           G_pred          Score   
  ----------------------------------------------------------------------------------------------------
    0  Candidate 0 (Control): a = l_Planck                     1.6163e-35      6.6743e-11  PASS    
    1  Candidate 1: a = lambda_C(electron)                     3.8616e-13      3.8099e+34  FAIL    
    2  Candidate 2: a = r_e (classical electron radius)        2.8179e-15      2.0288e+30  FAIL    
    3  Candidate 3: a = lambda_C(M_0)  -- Koide base mass      6.2875e-16      1.0100e+29  FAIL    
    4  Candidate 4: a = lambda_C(M_geom)  -- geometric mean of leptons      4.3105e-15      4.7472e+30  FAIL    
    5  Candidate 5: a = lambda_C(M_hop)  -- circulant hopping term      1.2575e-15      4.0402e+29  FAIL    
    6  Candidate 6: a = lambda_C(proton)                       2.1031e-16      1.1301e+28  FAIL    
    7  Candidate 7: a = alpha * lambda_C(M_0)  -- EM-scaled Koide      4.5882e-18      5.3786e+24  FAIL    
    8  Candidate 8: a = lambda_C(m_e/theta_0^2)  -- phase-angle scale      1.9071e-14      9.2924e+31  FAIL    
    9  Candidate 9: a = lambda_C(m_*) where G_pred = G_known      1.6163e-35      6.6743e-11  PASS    

  SUDOKU SCORECARD: 2 PASS, 8 FAIL (out of 10)

================================================================================
5. HIERARCHY WALL ANALYSIS
   Express each G_pred/G_known as (m_Pl/m_particle)^N
================================================================================

  Reference hierarchy ratios:
    m_Pl/m_e   = 2.3892e+22  (Planck/electron)
    m_Pl/m_mu  = 1.1555e+20  (Planck/muon)
    m_Pl/M_0   = 3.8902e+19  (Planck/Koide base)
    m_Pl/m_p   = 1.3012e+19  (Planck/proton)

    #  Candidate                                      G_pred/G_knwn  N (m_Pl/m_e)^N  Interpretation
  -----------------------------------------------------------------------------------------------
    0  Candidate 0 (Control): a = l_Planck              1.0000e+00  N=0.00          (m_Pl/m_e)^0.00
    1  Candidate 1: a = lambda_C(electron)              5.7084e+44  N=2.00          (m_Pl/m_e)^2.00
    2  Candidate 2: a = r_e (classical electron radi    3.0398e+40  N=1.81          (m_Pl/m_e)^1.81
    3  Candidate 3: a = lambda_C(M_0)  -- Koide base    1.5133e+39  N=1.75          (m_Pl/m_e)^1.75
    4  Candidate 4: a = lambda_C(M_geom)  -- geometr    7.1127e+40  N=1.83          (m_Pl/m_e)^1.83
    5  Candidate 5: a = lambda_C(M_hop)  -- circulan    6.0533e+39  N=1.78          (m_Pl/m_e)^1.78
    6  Candidate 6: a = lambda_C(proton)                1.6932e+38  N=1.71          (m_Pl/m_e)^1.71
    7  Candidate 7: a = alpha * lambda_C(M_0)  -- EM    8.0587e+34  N=1.56          (m_Pl/m_e)^1.56
    8  Candidate 8: a = lambda_C(m_e/theta_0^2)  --     1.3923e+42  N=1.88          (m_Pl/m_e)^1.88
    9  Candidate 9: a = lambda_C(m_*) where G_pred =    1.0000e+00  N=-0.00         (m_Pl/m_e)^-0.00

  Key finding:
    ALL candidates give ratio = (m_Pl/m_particle)^N for some N.
    This is the hierarchy problem: the lattice spacing that would give G
    must be the PLANCK LENGTH, not any particle physics scale.
    No combination of lepton masses and dimensionless numbers (alpha, 2/9, ...)
    bridges the 22-order-of-magnitude gap between particle physics and gravity.

================================================================================
6. THE 3x3 CIRCULANT MASS MATRIX
   Brannen parameterization as tight-binding eigenvalue problem
================================================================================

  Source: docs/research/koide_derivation.md Section 3

  The Brannen ansatz sqrt(m_i) = mu*(1 + sqrt(2)*cos(theta_0 + 2pi*i/3))
  is the eigenspectrum of a 3x3 Hermitian circulant matrix M_circ:

  For theta_0 = 0 (real symmetric case):
    M_circ = mu * I + (mu/sqrt(2)) * C
  where C is the adjacency matrix of a 3-site ring:
    C = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]

  Eigenvalues of C: {2, -1, -1}
  Eigenvalues of M_circ (theta_0=0): mu*(1+sqrt(2)), mu*(1-sqrt(2)/2), mu*(1-sqrt(2)/2)

  With mu = 17.715562 MeV^(1/2):
    Eigenvalues of M_circ (theta_0=0): 42.7691, 5.1888, 5.1888 MeV^(1/2)
    Squared (= predicted masses for theta_0=0):
      m_1 = 1829.2001 MeV  (cf. tau = 1776.86 MeV)
      m_2 = 26.9233 MeV  (degenerate)
      m_3 = 26.9233 MeV  (degenerate)

  With theta_0 = 2/9 (actual Brannen phase, breaking degeneracy):
  The matrix becomes Hermitian (complex off-diagonals) and the eigenvalues
  reproduce the three lepton masses:
    sqrt(m_i) eigenvalues: 42.1530, 10.2790, 0.7147 MeV^(1/2)
    Squared masses: 1776.8790, 105.6570, 0.510775 MeV
    Actual masses:  1776.8600, 105.6584, 0.510999 MeV

  Matrix elements and PDTP interpretation:
    Diagonal mu = 17.7156 MeV^(1/2)
    Off-diagonal t = mu/sqrt(2) = 12.5268 MeV^(1/2)

  In mass units (squaring):
    M_0     = mu^2   = 313.8411 MeV  (Koide base mass, shared mode)
    t^2     = mu^2/2 = 156.9206 MeV  (inter-generation hopping energy)

  In PDTP, the 'hopping energy' t^2 * c^2 corresponds to the inter-oscillator
  coupling g. With a = hbar/(t*c) (where t = mu/sqrt(2) treated as mass):
    t^2 = 156.9206 MeV, a_hop = lambda_C(t^2) = 1.2575e-15 m
    G_pred(a_hop) = 4.0402e+29 m^3/(kg s^2)
    G_pred/G_known = 6.0533e+39
    This is same as Candidate 5 (M_hop) -- FAIL

================================================================================
7. THE MISSING 'MAXWELL TERM'
   What would it need to be to give G_known?
================================================================================

  Maxwell's insight: add partial_E/partial_t to Ampere's law
  -> consistency gives c = 1/sqrt(epsilon_0 * mu_0) for free.
  Here: what single equation, when added to the Koide framework,
  yields G without using G as input?

  Required: a = l_Planck = 1.6163e-35 m  (from G = c^3 a^2 / hbar)
  The required a IS the Planck length -- using G circularly.

  What mass M* gives lambda_C(M*) = l_Planck?
    M* = hbar / (l_Planck * c) = m_Planck = 1.2209e+22 MeV
    Ratio M*/M_0 = 3.8902e+19
    Ratio M*/m_e = 2.3892e+22

  The Maxwell term would need to INTRODUCE the Planck scale.
  This cannot come from the Koide/Brannen structure alone.

  OPTIONS for a Maxwell-like term:
  1. Postulate K directly (K = hbar/(4*pi*c)) -- this IS G-free
     but still requires 'a' from outside the Koide framework.
  2. Measure the breathing mode frequency omega_gap directly:
     omega_gap -> a = pi*c/omega_gap -> G = c^3 a^2/hbar (Strategy A, Part 29)
  3. Introduce N_eff (Sakharov): G = a^2/(N_eff*pi*hbar*c)
     If BOTH a AND N_eff come from lattice structure, G follows.
  4. Dvali species count: if the lattice has N ~ 10^38 modes/Planck vol,
     gravity is weak BECAUSE spacetime has many degrees of freedom.

  The Koide formula is a constraint on RATIOS, not absolute scales.
  It cannot provide the Maxwell term by itself.

================================================================================
8. QUARK TRIPLET ANALYSIS
   Do quark triplets imply a different or consistent M_0?
================================================================================

  Source: docs/research/koide_derivation.md Section 7

  Triplet                         Q         delta     M_0 (MeV)       M_0/M_0_lep     a = l_C(M_0)
  ------------------------------------------------------------------------------------------
  (u, c, t) up-type                0.84894    1.7589        22752.93         72.4982      8.6726e-18
  (d, s, b) down-type              0.73122    1.5451          650.09          2.0714      3.0354e-16
  (c, b, t) heavy                  0.66937    1.4199        29550.23         94.1567      6.6777e-18

  Key: Each triplet gives a DIFFERENT M_0 value.
  The three Koide base masses are NOT consistent with each other.
  This means there is no single lattice spacing that works for all triplets.
  Either:
    a) Quarks and leptons live in different phase sectors (different a)
    b) The quark triplets are not true Koide triplets (Q != 2/3)
    c) QCD corrections shift the quark masses from their 'bare' Koide values

================================================================================
9. COMPLETE NUMERICAL SUMMARY
================================================================================

  Constants (non-gravitational):
    hbar = 1.054572e-34 J*s
    c    = 2.997925e+08 m/s
    G_known = 6.674300e-11 m^3/(kg*s^2)  [for comparison only]

  Koide/Brannen parameters (leptons):
    mu      = 17.715562 MeV^(1/2)
    M_0     = 313.841127 MeV
    theta_0 = 0.222230 rad = 2/9 + 7.41e-06
    delta   = 1.414201  (sqrt(2) = 1.414214)

  Planck units (computed from G_known -- NOT used in G_pred calculations):
    m_Pl  = 2.1764e-08 kg  = 1.2209e+22 MeV
    l_Pl  = 1.6163e-35 m
    E_Pl  = 1.9561e+09 J   = 1.2209e+19 GeV

  All G predictions:

    #  Candidate                                           a (m)           G_pred        G_pred/G_kn   Score 
  ---------------------------------------------------------------------------------------------------------
    0  Candidate 0 (Control): a = l_Planck                     1.6163e-35    6.6743e-11    1.0000e+00  PASS    N=0.00
    1  Candidate 1: a = lambda_C(electron)                     3.8616e-13    3.8099e+34    5.7084e+44  FAIL    N=2.00
    2  Candidate 2: a = r_e (classical electron radius)        2.8179e-15    2.0288e+30    3.0398e+40  FAIL    N=1.81
    3  Candidate 3: a = lambda_C(M_0)  -- Koide base mass      6.2875e-16    1.0100e+29    1.5133e+39  FAIL    N=1.75
    4  Candidate 4: a = lambda_C(M_geom)  -- geometric me      4.3105e-15    4.7472e+30    7.1127e+40  FAIL    N=1.83
    5  Candidate 5: a = lambda_C(M_hop)  -- circulant hop      1.2575e-15    4.0402e+29    6.0533e+39  FAIL    N=1.78
    6  Candidate 6: a = lambda_C(proton)                       2.1031e-16    1.1301e+28    1.6932e+38  FAIL    N=1.71
    7  Candidate 7: a = alpha * lambda_C(M_0)  -- EM-scal      4.5882e-18    5.3786e+24    8.0587e+34  FAIL    N=1.56
    8  Candidate 8: a = lambda_C(m_e/theta_0^2)  -- phase      1.9071e-14    9.2924e+31    1.3923e+42  FAIL    N=1.88
    9  Candidate 9: a = lambda_C(m_*) where G_pred = G_kn      1.6163e-35    6.6743e-11    1.0000e+00  PASS    N=-0.00

  FINAL SCORECARD: 2 PASS, 8 FAIL out of 10 candidates

================================================================================
10. CONCLUSIONS
================================================================================

  1. KOIDE FORMULA VERIFIED
     Q = 0.66666051 for (e, mu, tau) -- agrees with 2/3 to 1 part in 10^5.
     Brannen parameterization: mu = 17.7156 MeV^(1/2), M_0 = 313.84 MeV

  2. KOIDE GIVES RATIOS, NOT ABSOLUTE SCALE
     The formula Q = 2/3 is dimensionless and scale-invariant.
     It fixes mu only AFTER one mass is measured.
     No candidate 'a' derived from mu alone reproduces G.

  3. HIERARCHY WALL CONFIRMED
     Every candidate gives G_pred/G_known = (m_Pl/m_x)^N.
     This is the hierarchy problem: m_Pl is 22 orders of magnitude
     above particle physics scales. The Koide formula cannot bridge this gap.

  4. THE 'MAXWELL TERM' CANNOT COME FROM KOIDE ALONE
     Maxwell's displacement current was an INDEPENDENT measurement
     (capacitor charging rate) that gave c = 1/sqrt(eps0*mu0) for free.
     The PDTP equivalent would be:
       - A direct measurement of omega_gap (breathing mode frequency)
       - This gives: a = pi*c/omega_gap  ->  G = c^3 a^2 / hbar
       - This IS a Maxwell-like term: independent input, G as output.

  5. QUARK TRIPLETS
     No single M_0 is consistent across lepton and quark triplets.
     The Koide structure appears to be a feature of the LEPTON sector;
     quarks require different (or running) parameters.

  6. BEST REMAINING PATH (unchanged from Part 29):
     Strategy A: breathing mode detection -> omega_gap -> a -> G
     Strategy B: hierarchy ratio R = alpha_G/alpha_EM from lattice topology
     Both require physics INPUT beyond the mass spectrum alone.

  PDTP Original: The systematic Koide-lattice analysis confirms the
  circularity from a new direction. The Koide formula is a STRUCTURE
  theorem (mass ratios), not a SCALE theorem (absolute masses).
  Breaking the circularity requires a non-gravitational measurement
  that accesses the Planck scale directly.

  All results saved to: simulations/koide_lattice_output.md

