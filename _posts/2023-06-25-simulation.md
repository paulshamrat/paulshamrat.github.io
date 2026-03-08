---
layout: post
title:  "Simulation in python"
image: assets/images/wsl2.png
---
This post demonstrates a simplified molecular dynamics (MD) simulation implemented in Python. We'll explore the core components required to simulate particle motion under the influence of physical forces.

## Simulation Components

### 1. Constants
The simulation is governed by a few key physical parameters:
- **Mass:** The mass of the particles in the system.
- **dt:** The time step size, which determines the resolution of the simulation.
- **Steps:** The total number of iterations to perform.

### 2. Initial State
The positions and velocities of the particles are represented using NumPy arrays:
- **Positions:** An array representing the starting coordinates of each particle.
- **Velocities:** An array representing the initial speed and direction of the particles.

### 3. Force Calculation
The `calculate_forces` function determines the interactions between particles. In this simplified model, we use a basic placeholder, but in a real simulation, this would involve potentials like the Lennard-Jones or harmonic oscillators.

## The Simulation Loop
The core loop follows the Velocity Verlet integration steps:
1. **Calculate Forces** based on current positions.
2. **Update Positions and Velocities** using the equations of motion.
3. **Log Data** for later analysis.

---

### Python Implementation

```python
import numpy as np

# Simulation Constants
mass = 1.0
dt = 0.001
steps = 1000

# Initial State: Two particles in 3D space
positions = np.array([[0.0, 0.0, 0.0],
                      [1.0, 0.0, 0.0]])
velocities = np.array([[0.0, 0.0, 0.0],
                       [0.0, 1.0, 0.0]])

def calculate_forces(pos):
    """Placeholder for force calculation logic."""
    forces = np.zeros_like(pos)
    # Example: Simple attraction towards the origin
    forces = -0.5 * pos 
    return forces

# Simulation Loop
print("Starting Simulation...")
for step in range(steps):
    # Determine current forces
    forces = calculate_forces(positions)
    
    # Update state using Euler-Cromer integration
    velocities += (forces / mass) * dt
    positions += velocities * dt
    
    # Optional: Log output periodically
    if (step + 1) % 100 == 0:
        print(f"Step {step+1}: Particle 1 Position -> {positions[0]}")

print("Simulation Complete.")
```

---

### Conclusion
This code serves as a foundational demonstration of MD principles. For realistic biological simulations involving thousands of atoms, specialized high-performance software like **GROMACS**, **NAMD**, or **LAMMPS** is recommended.

