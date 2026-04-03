# Emergent Speed of Light c — A7 FCC (Part 95)

**Status:** PARTIAL — c structurally derived; numerical value free (same as A1)
**Script:** `simulations/solver/emergent_c.py` (Phase 64)
**Scorecard:** 12/12 PASS

---

## Problem Statement

In PDTP, c appears in every equation but is never derived. Part 34 showed that
c_s = c exactly for the spacetime condensate. Is this a coincidence, or is c itself
the phonon speed of the condensate — i.e., emergent rather than postulated?

---

## Plain English Summary

Think of the spacetime condensate as a crystal. The speed of sound in a crystal is a
**material property** — it depends on how stiff the springs between atoms are and how
heavy the atoms are. It is not a fundamental law; it is what comes out when you build
the crystal.

In PDTP, the "speed of sound" of the spacetime crystal is `c`. Photons are the sound
waves (massless phonons). Electrons and protons are whirlpools (vortices) — they have
a rest energy, so they can never reach c.

The number c = 3×10^8 m/s is not God-given — it is what you get when you plug in
the condensate's stiffness (g) and lattice spacing (l_P). But those in turn depend
on m_cond, which is still free (A1). So c is structurally derived, numerically still free.

**The user's insight:** yes, you can replace c everywhere with `sqrt(g_GP * n / m_cond)`.
In flat vacuum this just gives c back. Near matter (where n varies), it gives
`c_local != c` — that is genuinely new physics. Variable c = variable condensate density.

---

## Result 1: c = c_s(C1 condensate) [DERIVED, Part 34]

**Starting equation [Part 34, Eq 4b]:**
```
(95.0)  c_s = sqrt(g_GP * n / m_cond)
```

Where (from Eqs 4a, 4d):
```
g_GP   = hbar^3 / (m_cond^2 * c)          [Eq 4a]
n      = (m_cond * c / hbar)^3             [Eq 4d]
```

**Derivation (substitute and simplify):**
```
(95.1)  c_s^2 = g_GP * n / m_cond
             = [hbar^3 / (m_cond^2 * c)] * [(m_cond * c / hbar)^3] / m_cond
             = hbar^3 * m_cond^3 * c^3 / (m_cond^2 * c * hbar^3 * m_cond)
             = c^2                                                    [EXACT]
```

Result: c_s = c for **any** m_cond. This is structural — not specific to m_P.

Numerical verification: ratio c_s/c = 1.00000000000000 (machine precision, 14 decimal places).
Checked for m_cond = m_P and m_cond = m_electron: both give c_s/c = 1 exactly.

**Physical interpretation:** c is not a postulate in PDTP. It is the sound speed of the
spacetime condensate, fully determined by three condensate parameters. We just happen
to call it c because that is how we measure it in experiments.

---

## Result 2: c = omega_0 × l_0 — Condensate Lattice Identity [DERIVED]

In the condensate lattice:
```
(95.2)  omega_0 = g = m_cond * c^2 / hbar   [Planck angular frequency, Eq 4e]
(95.3)  l_0     = l_P = c / g               [Planck length = lattice spacing, Eq 2b]
(95.4)  c = omega_0 * l_0 = g * (c/g) = c   [EXACT, tautological in isolation]
```

**Physical meaning:** The speed c is the product of the condensate's natural frequency
(how fast each "lattice site" oscillates) and the lattice spacing (how far apart they are).
This is exactly how sound speed works in a crystal: c_sound = freq × spacing.

**Is this circular?** In isolation: yes. The parameters g and l_P themselves contain c.
But the identity shows WHERE c comes from structurally — it is set by the product of
two condensate properties, not postulated independently.

In a variable-c scenario (Result 5 below), if omega_0 and l_0 change locally,
c_local = omega_0_local × l_0_local gives a non-trivial prediction.

---

## Result 3: Photon = Massless Phonon; Matter = Massive Vortex [PDTP Original]

**Phonon (= photon in PDTP):**

Acoustic phonon dispersion in a condensate at long wavelength:
```
(95.5)  omega = c_s * k = c * k    [LINEAR dispersion, massless]
```
Group velocity:
```
(95.6)  v_g = d(omega)/dk = c      [EXACTLY c, for all k]
```

**Vortex (= massive matter in PDTP, Part 33):**

A vortex has rest energy E_0 = m_cond * c^2, giving relativistic dispersion:
```
(95.7)  omega^2 = (m_cond * c^2 / hbar)^2 + c^2 * k^2
(95.8)  v_g     = c^2 * k / omega < c    [ALWAYS less than c]
```

**Numerical check (group velocities at k = 1/l_P):**
```
v_phonon / c = 1.000000   (exactly c, all k)
v_vortex / c = 0.707107   (= c/sqrt(2) at k = omega_rest/c = 1/l_P)
```

**Why this matters:** The speed difference between photons and matter is not postulated.
It follows directly from topology:
- Phonons = massless waves: no rest energy, must travel at c_s
- Vortices = topological defects: have rest energy m_cond * c^2, so v < c

This is a topological origin for the massless/massive distinction — entirely within PDTP.

---

## Result 4: Bessel Renormalization — c_eff = c × sqrt(J_0(phi_0)) [PDTP Original]

**Physical setup:** If the spacetime condensate has a background oscillation:
```
phi(t) = phi_0 * cos(omega_0 * t)
```
The coupling in the Lagrangian is renormalized by the Kapitza-Dirac / Floquet mechanism:
```
(95.9)  g_eff = g * J_0(phi_0)
```
where J_0 is the zeroth Bessel function of the first kind.

**Source:** Kapitza-Dirac effect (Kapitza & Dirac 1933); Floquet theory (Shirley 1965).
J_0 series: J_0(x) = sum_{m=0}^{inf} (-1)^m (x/2)^{2m} / (m!)^2    [DLMF 10.2.2]

Since c_s^2 is proportional to g_GP which is proportional to g:
```
(95.10) c_eff = c * sqrt(J_0(phi_0))    [PDTP Original]
```

**Numerical table:**
```
phi_0    J_0(phi_0)    c_eff/c
0.000    1.000000      1.000000    (normal vacuum)
0.500    0.938470      0.968747
1.000    0.765198      0.874756
1.500    0.511828      0.715421
2.000    0.223891      0.473171
2.4048   0.000000      0.000000    ("light stop")
2.600   -0.096805      0.000000    (condensate unstable)
```

**"Light stop" condition [PDTP Original, SPECULATIVE]:**
```
(95.11) J_0(phi_0) = 0  =>  phi_0 = 2.4048  =>  c_eff = 0
```
If the condensate amplitude reaches phi_0 = 2.4048 radians, the effective sound speed
vanishes: photons cannot propagate. This is the spacetime analog of Lene Hau stopping
light completely in a lab BEC.

**What sets phi_0?** Unknown — this is the same free parameter problem as A1. In
the ground-state vacuum, phi_0 = 0. A non-zero phi_0 means an excited condensate.
Near a source of strong gravitational waves or near a singularity, phi_0 might grow.

**Note:** J_0(phi_0) < 0 for phi_0 > 2.4048 is physically forbidden: c_eff^2 < 0
means imaginary sound speed, i.e., the condensate becomes unstable. The first Bessel
zero is the maximum phi_0 for a stable condensate.

---

## Result 5: Variable c from Condensate Density [PDTP Original]

If the condensate density varies locally from its vacuum value n_0 = (m_P c/hbar)^3:
```
(95.12) c_local = c * sqrt(n_local / n_0)    [PDTP Original]
```

**Derivation:** From c_s = sqrt(g_GP * n / m_cond) and c = sqrt(g_GP * n_0 / m_cond):
```
c_local / c = sqrt(n_local / n_0)
```

**Table:**
```
n_local / n_0    c_local / c
1.0              1.000000    (normal vacuum)
0.25             0.500000    (half c)
0.01             0.100000    (10% c)
1e-6             0.001000    (0.1% c)
1e-10            1e-5        (near condensate collapse)
```

**Physical interpretation:** Wherever the condensate is less dense than its vacuum value,
light travels slower. Near a black hole singularity (if the condensate is depleted),
c_local could be much less than c_vacuum. In the early universe (if n was different),
c was different — this is the PDTP version of VSL (Variable Speed of Light) theories.

**SM compatibility note:** Standard QED assumes c is universal. If c_local varies, then
all c-dependent quantities (fine structure constant alpha = e^2/(4pi*epsilon_0*hbar*c),
Compton wavelengths, etc.) would also vary locally. This is a **testable prediction**
in principle — look for variations of alpha near dense astrophysical objects.

---

## Result 6: Hau Slow-Light Analogy [ANALOGY]

Lene Hau (1999) slowed light to 17 m/s in a sodium BEC. The mechanism was
Electromagnetically Induced Transparency (EIT), creating a dark-state polariton
whose group velocity depends on the BEC parameters.

The BEC phonon speed formula:
```
(95.13) c_s(lab) = sqrt(g_GP_atom * n_atom / m_atom)
                 = sqrt(4*pi*hbar^2*a_s*n / m^2)
```
is the **identical formula** as PDTP's c = c_s(C1):
```
(95.14) c_s(C1)  = sqrt(g_GP * n / m_cond)
```

**Numerical comparison:**
```
PDTP C1 vacuum: c_s = 2.998e8 m/s     (= c, by construction)
Hau Na BEC:     c_s = 0.46 mm/s       (BEC phonon speed; Hau's 17 m/s was EIT group velocity)
n_Planck / n_Hau = 2.96e86            (spacetime condensate 10^86 times denser)
```

**Clarification:** Hau's reported 17 m/s was the group velocity of a dark-state polariton
(light-matter quasiparticle) via the EIT mechanism, which depends on laser coupling strengths
and is NOT simply c_s(BEC). The BEC phonon speed (formula 95.13) gives ~0.5 mm/s for Hau's
parameters. The PDTP analogy is at the level of the formula: both obey c_s = sqrt(g_GP * n / m),
just with different condensates and parameters.

**PDTP insight from the Hau experiment:** Hau's experiment proves that the speed at which
light propagates through a medium is a material property of that medium. In PDTP, spacetime
IS the medium. Normal vacuum has maximum condensate density n = n_Planck, giving c_s = c.
Depleting n locally (the PDTP analog of cooling to BEC) would reduce c_local. The Hau
experiment is a proof of concept for this mechanism, just in a non-relativistic atomic BEC.

---

## Result 7: Two-Phase Group Velocities [DERIVED, Part 61]

From the two-phase dispersion relation (Eq 6b):
```
Branch A (phi_+, gravity): omega_A^2 = c^2*k^2 + 2*sqrt(2)*g   [gapped, breathing mode]
Branch B (phi_-, surface): omega_B^2 = c^2*k^2 - 2*sqrt(2)*g   [Jeans unstable for k < k_J]
```

Group velocities:
```
(95.15) v_g = c^2 * k / omega
```

**At high k (k >> k_J):** Both branches approach v_g = c (relativistic limit).
**At low k (k ~ k_J):** Branch A slows down; Branch B enters Jeans instability.

**Jeans wavenumber:**
```
(95.16) k_J = sqrt(2*sqrt(2)*g) / c ~ 2.4e13 /m
k_J / k_Planck = 3.9e-22  <<  1
```

The Jeans instability scale (lambda_J ~ 0.26 pm) is much larger than the Planck length
(l_P ~ 1.6e-35 m) but still sub-nuclear. This means the gravitational condensate's own
Jeans instability operates at nuclear scales, not cosmological ones.

**Note on units:** The dispersion formula uses g in the natural-unit sense (units [mass]^2).
The Eq 4e value g = 1.86e43 rad/s (SI) gives a k_J that is an order-of-magnitude estimate.
The exact value requires resolving the SI vs natural-unit normalization of g (see Part 94 note).

---

## Free Parameter Status of c

```
Chain 1:  m_cond (free) -> g = m_cond*c^2/hbar -> G = c^5/(hbar*g^2)
Chain 2:  m_cond (free) -> g_GP, n -> c_s = c  [structural identity]
Chain 3:  c = omega_0 * l_0 = g * l_P          [lattice identity]
```

In ALL chains: c appears as an input AND an output. The c's cancel algebraically
(as shown in Result 1, Step 95.1). This means:
- c is **structurally derived** (follows from condensate parameters)
- c is **numerically free** (the number 3×10^8 m/s requires knowing m_cond)

The variable-c prediction (Result 5) is genuinely new: c_local = c * sqrt(n_local/n_0)
gives c as a dynamical field, not a constant. This breaks the circularity locally.

**Summary of A-series status:**

| Parameter | Status | Note |
|---|---|---|
| A1: m_cond | FREE | All paths exhausted |
| A2: alpha_EM | FREE | 5 paths negative |
| A3: Lambda | FREE | CKN consistent, not derived |
| A4: theta_0 | FREE | No SU(3) origin |
| A5: sin^2(theta_W) | PARTIAL | SU(5) fixes at GUT scale |
| A6: g | PARTIAL | G*g^2 = c^5/hbar; reduces to A1 |
| **A7: c** | **PARTIAL** | **c = c_s(C1); numerical value reduces to A1** |

---

## Sudoku Scorecard — 12/12 PASS

| Test | Result | Value | Tag |
|---|---|---|---|
| S1: c_s = c for m_cond = m_P | PASS | 1.000000 | [DERIVED, Part 34] |
| S2: c_s = c for m_cond = m_electron | PASS | 1.000000 | [STRUCTURAL] |
| S3: c = omega_0 * l_0 | PASS | 1.000000 | [DERIVED] |
| S4: photon (phonon) v_g = c | PASS | 1.000000 | [DERIVED] |
| S5: vortex (matter) v_g < c at k=1/l_P | PASS | 0.707107 | [DERIVED] |
| S6: J_0(0)=1 -> c_eff=c in vacuum | PASS | 1.000000 | [PDTP Original] |
| S7: J_0(2.405)~0 -> light stop | PASS | ~0 | [PDTP Original, SPECULATIVE] |
| S8: c_s(C1) = c via Hau formula | PASS | 1.000000 | [DERIVED] |
| S9: n_Planck >> n_Hau (spacetime denser) | PASS | 2.96e86 | [ANALOGY] |
| S10: v_g(phi_+) -> c at high k | PASS | 1.000000 | [DERIVED, Eq 6b] |
| S11: k_J << k_Planck (Jeans cosmological) | PASS | 3.9e-22 | [DERIVED, Eq 6b] |
| S12: c_local = c/2 when n = n_0/4 | PASS | 0.500000 | [PDTP Original] |

---

## Conclusion

**c is emergent in PDTP — structurally derived, not postulated.**

c is the phonon speed of the C1 spacetime condensate:
```
c = c_s = sqrt(g_GP * n / m_cond)    [DERIVED, any m_cond]
```

Photons travel at c because they ARE massless phonons of the condensate.
Matter travels at v < c because vortices (particles) have rest energy m_cond*c^2.

**New results [PDTP Original]:**
1. c_eff = c * sqrt(J_0(phi_0)) — Bessel renormalization under condensate oscillation
2. "Light stop": phi_0 = 2.4048 -> c_eff = 0 (spacetime analog of Hau experiment)
3. c_local = c * sqrt(n_local/n_0) — variable c from condensate density variation
4. k_J << k_Planck — Jeans instability scale is nuclear, not Planck

**Negative:** The numerical value of c is not independently determined. It reduces to A1
(m_cond free). Until m_cond = m_P is derived, c = c_s remains a structural identity
with a free numerical parameter.

**Observational path:** Look for alpha variation (alpha = e^2/(4pi*hbar*c)) near dense
astrophysical objects where n_local may differ from n_0. Any detection of variable c or
variable alpha would be direct evidence for the condensate density mechanism.

**Status change:** A7 OPEN (HIGH) -> PARTIAL + FREE — CLOSED

---

**Sources:**
- Part 34, `condensate_selfconsist.py` — c_s = c exactly (Eq 4b)
- Part 33, `vortex_winding.py` — vortex rest energy; photon vs matter
- Part 61, `two_phase_lagrangian.py` — two-phase dispersion (Eq 6b)
- Hau et al. (1999), Nature 397, 594 — slow light in BEC
- Kapitza & Dirac (1933), Proc.Camb.Phil.Soc. 29, 297 — Kapitza-Dirac effect
- DLMF 10.2.2 — Bessel function J_0 series definition

**Changelog:** 2026-04-04 — Part 95 created (A7 FCC)
