
# pdtp_emulator.py
# ---------------------------------------------
# PDTP Emulator (Conceptual / Educational)
# No real physics claims. Control-system sandbox.
# ---------------------------------------------

import numpy as np
import time

# ==============================
# Configuration
# ==============================
DT = 0.02
GRID_SIZE = (60, 60, 60)

PHASE_DAMPING = 0.05
NOISE_LEVEL = 0.002

KAPPA_MIN = 0.0
KAPPA_MAX = 1.0
MAX_GRADIENT = 3.0

# ==============================
# Utility Functions
# ==============================
def clamp(value, vmin, vmax):
    return max(vmin, min(value, vmax))

def magnitude(v):
    return np.linalg.norm(v)

def normalize(v):
    n = magnitude(v)
    return v / n if n > 0 else v

def smooth(current, target, rate=0.05):
    return current + (target - current) * rate

def clamp_vector(v, max_mag):
    mag = magnitude(v)
    if mag > max_mag:
        return normalize(v) * max_mag
    return v

# ==============================
# Phase Field
# ==============================
class PhaseField:
    def __init__(self, size):
        self.size = size
        self.phi = np.zeros(size)
        self._init_gravity_slope()

    def _init_gravity_slope(self):
        for z in range(self.size[2]):
            self.phi[:, :, z] -= z * 0.02

    def sample(self, pos):
        x, y, z = map(int, pos)
        return self.phi[x, y, z]

    def gradient(self, pos):
        x, y, z = map(int, pos)
        gx = self.phi[min(x+1,59), y, z] - self.phi[max(x-1,0), y, z]
        gy = self.phi[x, min(y+1,59), z] - self.phi[x, max(y-1,0), z]
        gz = self.phi[x, y, min(z+1,59)] - self.phi[x, y, max(z-1,0)]
        return clamp_vector(np.array([gx, gy, gz]), MAX_GRADIENT)

    def add_noise(self):
        self.phi += np.random.normal(0, NOISE_LEVEL, self.size)

# ==============================
# Craft
# ==============================
class Craft:
    def __init__(self, position):
        self.position = np.array(position, dtype=float)
        self.velocity = np.zeros(3)
        self.phi_internal = 0.0
        self.kappa = 1.0

    def update_phase_lock(self, external_phi):
        error = self.phi_internal - external_phi
        self.phi_internal -= error * PHASE_DAMPING

    def apply_motion(self, gradient, dt):
        accel = self.kappa * gradient
        self.velocity += accel * dt
        self.position += self.velocity * dt
        self.position = np.clip(self.position, 1, 58)

# ==============================
# Controller
# ==============================
class PDTPController:
    def __init__(self):
        self.mode = "HOVER"
        self.target_direction = np.array([1.0, 0.0, 0.0])

    def update(self, craft, field):
        local_phi = field.sample(craft.position)
        gradient = field.gradient(craft.position)

        craft.update_phase_lock(local_phi)
        self._update_mode(craft)
        self._adjust_coupling(craft)
        gradient = self._shape_gradient(gradient)

        return gradient

    def _update_mode(self, craft):
        speed = magnitude(craft.velocity)
        self.mode = "HOVER" if speed < 0.2 else "TRANSLATE"

    def _adjust_coupling(self, craft):
        if self.mode == "HOVER":
            craft.kappa = smooth(craft.kappa, 0.25)
        else:
            craft.kappa = smooth(craft.kappa, 0.45)

        craft.kappa = clamp(craft.kappa, KAPPA_MIN, KAPPA_MAX)

    def _shape_gradient(self, gradient):
        if self.mode == "TRANSLATE":
            gradient += normalize(self.target_direction) * 0.5
        return clamp_vector(gradient, MAX_GRADIENT)

# ==============================
# Main Simulation
# ==============================
def main():
    field = PhaseField(GRID_SIZE)
    craft = Craft(position=(30, 30, 50))
    controller = PDTPController()

    print("Starting PDTP Emulator (CTRL+C to stop)")
    print("Mode | Position | Velocity | Kappa")

    try:
        while True:
            field.add_noise()
            grad = controller.update(craft, field)
            craft.apply_motion(grad, DT)

            print(f"{controller.mode:9} | "
                  f"{craft.position.round(2)} | "
                  f"{craft.velocity.round(2)} | "
                  f"{craft.kappa:.2f}")

            time.sleep(DT)

    except KeyboardInterrupt:
        print("\nSimulation stopped.")

if __name__ == "__main__":
    main()
