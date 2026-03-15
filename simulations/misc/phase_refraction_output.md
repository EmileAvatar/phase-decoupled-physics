================================================================================
PHASE REFRACTION ANALYSIS: GRAVITY AND ATOMIC BINDING
================================================================================

================================================================================
1. REFERENCE VALUES
================================================================================

  Bohr radius:           a_0 = 5.291772e-11 m
  Hartree energy:     E_Hart = 27.211386 eV
  Ionization energy:   E_ion = 13.605693 eV
  Rydberg energy:      R_inf = 13.605693 eV
  Fine structure:    alpha_EM = 7.297353e-03
  Compton wavelength: lam_C  = 3.861593e-13 m
  Classical e radius:   r_e  = 2.817940e-15 m

  Gravitational coupling at a_0:
    g_grav(e-p) = G*m_e*m_p/a_0 = 1.9217e-57 J = 1.1994e-38 eV
    g_EM / g_grav = 2.2687e+39
    This is the hierarchy problem: EM is ~10^39 times stronger than gravity

================================================================================
2. THE TWO-COUPLING PROBLEM
================================================================================

  PDTP has ONE coupling per matter field: g_i cos(psi_i - phi)
  For gravity:  g_grav ~ G*m^2/r ~ 10^-40 eV (at atomic scale)
  For EM:       g_EM   ~ e^2/(4*pi*eps_0*r) ~ 27 eV (at Bohr radius)

  These CANNOT be the same coupling constant.
  The refraction picture works for BOTH, but at vastly different strengths.

  Gravitational coupling: alpha_G = G*m_e*m_p/(hbar*c) = 3.2166e-42
  EM coupling:            alpha_EM = 7.297353e-03
  Hierarchy ratio:    alpha_EM/alpha_G = 2.2687e+39

  Gravity is the SAME mechanism (phase refraction) but ~10^36 times weaker.
  This is equivalent to saying: gravity has an enormously weaker refractive index.

================================================================================
3. CALCULATION 1: PDTP WAVE EQUATION -> SCHRODINGER
================================================================================

  PDTP field equation for matter wave:
    Box(psi) = -g sin(psi - phi)

  Step 1: Weak-field linearization (small phase mismatch)
    sin(psi - phi) ~ psi - phi  for |psi - phi| << 1
    Box(psi) ~ -g(psi - phi)

  Step 2: Identify background phase field as potential
    phi(r) = V(r)/(hbar*omega)  where V(r) is the potential energy
    For Coulomb: V(r) = -e^2/(4*pi*eps_0*r)

  Step 3: Non-relativistic limit (standard KG -> Schrodinger)
    Source: Klein-Gordon equation, Wikipedia
    https://en.wikipedia.org/wiki/Klein%E2%80%93Gordon_equation

    Write psi(x,t) = Psi(x,t) * exp(-i*m*c^2*t/hbar)
    where Psi is slowly varying (|Psi_tt| << m*c^2*|Psi_t|/hbar)

    The Box(psi) = (1/c^2)*d^2(psi)/dt^2 - nabla^2(psi) becomes:
    -(m^2*c^2/hbar^2)*Psi - 2i*(m/hbar)*dPsi/dt - nabla^2(Psi)
      = -g*(psi - phi)/hbar^2

    Keeping only first-order time derivatives:
    i*hbar * dPsi/dt = -(hbar^2/2m)*nabla^2(Psi) + V(r)*Psi

    [YES] This IS the Schrodinger equation.

  RESULT: The PDTP wave equation reduces to the Schrodinger equation
  in the non-relativistic, weak-field limit. This is a COMPATIBILITY
  check, not a derivation -- the Coulomb potential V(r) is input, not derived.

  Hydrogen energy levels from Schrodinger equation:
  Source: https://en.wikipedia.org/wiki/Hydrogen_atom

     n      E_n (eV)  E_n = -13.6/n^2 (eV)    Match?
  ----      --------  --------------------    ------
     1      -13.6057              -13.6000       YES
     2       -3.4014               -3.4000       YES
     3       -1.5117               -1.5111       YES
     4       -0.8504               -0.8500       YES
     5       -0.5442               -0.5440       YES
     6       -0.3779               -0.3778       YES
     7       -0.2777               -0.2776       YES

================================================================================
4. CALCULATION 2: CRITICAL ANGLE AND IONIZATION
================================================================================

  PDTP coupling energy: V(theta) = -g_EM * cos(theta)  where theta = psi - phi

  Ground state: theta = 0 (phase-locked)
    V(0) = -g_EM = -27.2 eV

  Total decoupling: theta = 90 deg
    V(pi/2) = 0
    DeltaV = g_EM = 27.2 eV (full Coulomb energy)

  BUT: ionization energy is only 13.6 eV = g_EM/2
  Source: Virial theorem for 1/r potentials
  https://en.wikipedia.org/wiki/Virial_theorem
  For Coulomb: 2<KE> = -<V>, so E_total = <V>/2 = -g_EM/2

  Phase angle at ionization (where E_total = 0):

  For shell n: E_n = -g_EM/(2*n^2)
  Energy needed to ionize from shell n: DeltaE_n = g_EM/(2*n^2)
  Phase angle: cos(theta_n) = 1 - DeltaE_n/g_EM = 1 - 1/(2*n^2)

     n    E_n (eV)   DE_ion (eV)     cos(th)    th (deg)                  Interpretation
  ----    --------   -----------      ------     -------                  --------------
     1    -13.6057       13.6057    0.500000       60.00  Ground state -> 60 deg, NOT 90
     2     -3.4014        3.4014    0.875000       28.96                   Excited state
     3     -1.5117        1.5117    0.944444       19.19                   Excited state
     4     -0.8504        0.8504    0.968750       14.36      High-n -> approaches 0 deg
     5     -0.5442        0.5442    0.980000       11.48      High-n -> approaches 0 deg
     6     -0.3779        0.3779    0.986111        9.56      High-n -> approaches 0 deg
     7     -0.2777        0.2777    0.989796        8.19      High-n -> approaches 0 deg

  KEY FINDING: Ionization from the ground state requires rotating the
  phase angle to 60 deg, NOT 90 deg.

  The 90 deg point corresponds to TOTAL Coulomb stripping (27.2 eV),
  not ionization. Ionization happens when the kinetic energy equals
  the remaining potential energy (virial theorem), which is at 60 deg.

  Physical meaning of different angles:
    theta =   0 deg:  Perfect phase lock -- fully bound (ground state, cos = 1)
    theta =  60 deg:  Ionization threshold -- just barely unbound (cos = 0.5)
    theta =  90 deg:  Total decoupling -- no EM interaction at all (cos = 0)
    theta = 180 deg:  Anti-phase -- maximum repulsion (cos = -1, antiparticle)

  SNELL'S LAW MAPPING:
  Source: https://en.wikipedia.org/wiki/Snell%27s_law

  In optics: n_1 sin(theta_1) = n_2 sin(theta_2)
  Critical angle: sin(theta_c) = n_2/n_1

  In PDTP phase coupling: alpha = cos(psi - phi)
  The coupling projects the matter phase onto the field phase.

  Connection to Snell's law:
  The effective refractive index near a proton is:
    n_grav(a_0) = 1/sqrt(1 - 2*Phi/c^2) = 1.000000000000000
    Delta_n = n - 1 = 0.0000e+00 (gravitational -- negligible)

    n_EM_eff(a_0) = 1 + E_Coulomb/(m_e*c^2) = 1.0000532514
    Delta_n_EM = 5.3251e-05 (electromagnetic -- much larger than gravitational)
    (Gravitational Delta_n too small for float64; using weak-field approx)
    Delta_n_grav ~ GM/(r*c^2) = 2.3473e-44
    Ratio Delta_n_EM/Delta_n_grav ~ 2.2687e+39

================================================================================
5. CALCULATION 3: ANGULAR MOMENTUM AS REFRACTION ANGLE
================================================================================

  In optics: a wave hitting a spherical cavity at angle theta has
  angular momentum L = n*k*r*sin(theta), where k = 2*pi/lambda.
  Source: https://en.wikipedia.org/wiki/Whispering-gallery_wave

  In QM: orbital angular momentum L = sqrt(l*(l+1)) * hbar
  The centrifugal barrier is V_cf = l*(l+1)*hbar^2/(2*m*r^2)
  Source: https://en.wikipedia.org/wiki/Hydrogen_atom#Mathematical_summary

  Refraction angle interpretation:
    l = 0:   radial wave (head-on incidence, theta_inc = 0 deg)
    l = n-1: tangential wave (grazing incidence, theta_inc -> 90 deg)

  For each (n, l), the 'incidence angle' at the classical turning point:
    sin(theta_inc) = L/(p * r_tp)  where p = hbar*k is the radial momentum

     n     l    L/hbar   r_max/a_0   th_inc(deg)             Type
  ----  ----    ------    --------   -----------             ----
     1     0     0.000         1.0           0.0       s (radial)

     2     0     0.000         4.0           0.0       s (radial)
     2     1     1.414         4.0          45.0     p (dumbbell)

     3     0     0.000         9.0           0.0       s (radial)
     3     1     1.414         9.0          28.1     p (dumbbell)
     3     2     2.449         9.0          54.7       d (clover)

     4     0     0.000        16.0           0.0       s (radial)
     4     1     1.414        16.0          20.7     p (dumbbell)
     4     2     2.449        16.0          37.8       d (clover)
     4     3     3.464        16.0          60.0      f (complex)

     5     0     0.000        25.0           0.0       s (radial)
     5     1     1.414        25.0          16.4     p (dumbbell)
     5     2     2.449        25.0          29.3       d (clover)
     5     3     3.464        25.0          43.9      f (complex)
     5     4     4.472        25.0          63.4              l=4

  RESULT: The semiclassical incidence angle sin(theta) = sqrt(l*(l+1))/n
  correctly gives:
    l = 0:   theta = 0 deg (radial, head-on)
    l = n-1: theta -> 90 deg for large n (tangential, grazing)

  This is the SAME as the whispering gallery mode classification
  in wave optics. The centrifugal barrier is the angular-momentum-
  dependent refraction angle.

  CAUTION: This mapping is QUALITATIVE. The quantitative match
  requires showing that the centrifugal barrier formula emerges
  from the PDTP refraction geometry, which is not yet proven.

================================================================================
6. SUDOKU CONSISTENCY CHECK: g_EM = E_Hartree = 27.2 eV
================================================================================

  New value introduced: g_EM = e^2/(4*pi*eps_0*a_0) = 27.2 eV
  This is the Hartree energy -- established physics, not a new claim.
  The NEW claim is: g_EM plays the role of the PDTP coupling constant
  for the EM sector, analogous to g_grav for gravity.

  H ground state E_1 = -g_EM/2
    predicted = -2.179872e-18,  known = -2.179906e-18
    ratio = 0.999985  [MATCH]

  Bohr radius from g_EM
    predicted = 5.291772e-11,  known = 5.291772e-11
    ratio = 1.000000  [MATCH]

  alpha_EM = g_EM * a_0/(hbar*c)
    predicted = 7.297353e-03,  known = 7.297353e-03
    ratio = 1.000000  [MATCH]

  Rydberg = m_e c^2 alpha^2/2
    predicted = 2.179872e-18,  known = 2.179872e-18
    ratio = 1.000000  [MATCH]

  a_0/lambda_C = 1/alpha_EM
    predicted = 1.370360e+02,  known = 1.370360e+02
    ratio = 1.000000  [MATCH]

  a_0/r_e = 1/alpha^2
    predicted = 1.877887e+04,  known = 1.877887e+04
    ratio = 1.000000  [MATCH]

  g_EM = m_e c^2 alpha^2
    predicted = 4.359745e-18,  known = 4.359745e-18
    ratio = 1.000000  [MATCH]

  alpha_EM/alpha_G = g_EM/g_grav
    predicted = 2.268661e+39,  known = 2.268661e+39
    ratio = 1.000000  [MATCH]

  Ionization angle = 60 deg
    predicted = 6.000000e+01,  known = 6.000000e+01
    ratio = 1.000000  [MATCH]

  Lyman-alpha = 3*g_EM/8
    predicted = 1.634904e-18,  known = 1.634220e-18
    ratio = 1.000419  [MATCH]

  H-alpha = 5*g_EM/72
    predicted = 3.027601e-19,  known = 3.028114e-19
    ratio = 0.999830  [MATCH]

  -----------------------------------------------
  SUDOKU SCORECARD: 11 matches, 0 contradictions out of 11 tests
  -----------------------------------------------

  ALL PASS -- g_EM = 27.2 eV is internally consistent.
  NOTE: This is expected -- the Hartree energy is established physics.
  The consistency confirms the MAPPING (g_EM = Hartree energy in PDTP)
  is at least algebraically valid.

================================================================================
7. THE HIERARCHY AS REFRACTIVE INDEX RATIO
================================================================================

  If both gravity and EM are phase refraction at different strengths:

    Gravitational 'refractive index' change at a_0:
      Delta_n_grav = G*M/(r*c^2) = 2.3473e-44

    EM 'refractive index' change at a_0:
      Delta_n_EM = E_Coulomb/(m_e*c^2) = 5.3251e-05

    Ratio: Delta_n_EM / Delta_n_grav = 2.2687e+39

  The EM 'medium' bends electron waves ~10^36 times more than the
  gravitational 'medium'. This is WHY atoms exist but gravitational
  'atoms' (gravitational bound states of electrons) do not -- the
  gravitational refraction is too weak to trap anything at atomic scales.

  'Gravitational Bohr radius': a_G = hbar^2/(G*m_e^2*m_p) = 1.2005e+29 m
  = 2.2687e+39 * a_0
  = 1.2005e+20 * 10^9 m  (bigger than Jupiter's orbit!)

  This shows: gravity CAN form 'atoms' in principle, but they would
  be ~10^29 times larger than hydrogen -- confirming the refraction
  picture: weaker medium -> wider bend radius -> enormous 'orbitals'.

================================================================================
8. SUMMARY OF FINDINGS
================================================================================

  CALCULATION 1 (KG -> Schrodinger):
    [YES] PDTP wave equation reduces to Schrodinger in non-relativistic limit
    [YES] This is a standard result (KG -> Schrodinger), confirms COMPATIBILITY
    [NO]  Does NOT prove refraction IS the mechanism (Coulomb potential is input)

  CALCULATION 2 (Critical angle and ionization):
    [YES] g_EM = 27.2 eV (Hartree energy) is the correct EM coupling constant
    [NO]  Ionization angle is 60 deg, NOT 90 deg (virial theorem)
    -> 90 deg = total EM decoupling (full Coulomb stripping)
    -> 60 deg = ionization (kinetic energy = potential energy)
    -> The simple 'critical angle = 90 deg' picture FAILS for ionization
    -> BUT: 60 deg has a clear physical meaning (virial equipartition)

  CALCULATION 3 (Angular momentum -> refraction angle):
    [YES] sin(theta) = sqrt(l*(l+1))/n correctly classifies orbital geometry
    [YES] l = 0 -> head-on (s-orbital), l = n-1 -> grazing (whispering gallery)
    [NO]  Quantitative derivation from PDTP refraction geometry not yet done
    -> This is QUALITATIVE, not a derivation

  SUDOKU CONSISTENCY CHECK:
    11/11 tests pass -- g_EM = Hartree energy is fully consistent

  OVERALL ASSESSMENT:
    The refraction interpretation provides a UNIFIED PHYSICAL PICTURE:
    gravity and atomic binding are both wave refraction, differing only
    in coupling strength (alpha_G vs alpha_EM, ratio ~10^36).

    However, this is INTERPRETIVE, not PREDICTIVE at this stage.
    No new predictions beyond standard QM are generated.
    The hierarchy problem (WHY alpha_EM/alpha_G ~ 10^36) is restated,
    not solved -- it becomes: WHY is the EM refractive index 10^36
    times larger than the gravitational one?

    The 60 deg vs 90 deg finding is an INFORMATIVE FAILURE:
    it reveals that ionization is NOT simple critical-angle escape,
    but rather a virial equipartition threshold. The 90 deg point
    (total phase decoupling) corresponds to a HIGHER energy state
    -- complete removal of all Coulomb interaction.

