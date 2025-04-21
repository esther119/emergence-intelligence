# Simulation: Temporal Dispersion of First Inter-Arrival Time

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skewnorm
import sys
import os

# Add star_formation directory to path to import the module
sys.path.append("star_formation")
from star_formation import star_formation_rate

# Simulation parameters
n_stars = 1000  # number of stars per simulation
n_simulations = 1000  # number of universe simulations
mean_life_delay = 1000  # mean life emergence delay (Myr)
sigma_life_delay = 0.7  # spread of life emergence delay

# Store first inter-arrival times
first_arrival_times = []

for _ in range(n_simulations):
    # Sample star formation times using the distribution from star_formation.py
    # Convert from Gyr to Myr for consistency with the rest of the simulation
    time_samples = np.linspace(0, 14, n_stars)  # 0 to 14 Gyr as in star_formation.py
    probabilities = star_formation_rate(time_samples)
    # Normalize probabilities to use as weights
    probabilities = probabilities / np.sum(probabilities)
    # Sample star formation times according to the star formation rate
    star_times = np.random.choice(time_samples * 1000, size=n_stars, p=probabilities)

    # Sample life emergence delays
    delay_times = np.random.lognormal(
        mean=np.log(mean_life_delay), sigma=sigma_life_delay, size=n_stars
    )

    # Calculate civilization emergence times
    civilization_times = star_times + delay_times

    # Record the earliest civilization time
    first_arrival_times.append(np.min(civilization_times))

# Plot the histogram of first arrival times
plt.figure(figsize=(10, 6))
plt.hist(first_arrival_times, bins=50, edgecolor="black")
plt.xlabel("First Inter-Arrival Time (Myr)")
plt.ylabel("Frequency")
plt.title("Temporal Dispersion of First Inter-Arrival Time")
plt.grid(True)
plt.savefig("inter_arrival_times.png", dpi=300, bbox_inches="tight")
plt.close()


# Optional: print basic stats
print(f"Mean: {np.mean(first_arrival_times):.2f} Myr")
print(f"Std Dev: {np.std(first_arrival_times):.2f} Myr")
print(f"Min: {np.min(first_arrival_times):.2f} Myr")
print(f"Max: {np.max(first_arrival_times):.2f} Myr")
