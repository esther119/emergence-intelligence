# Simulation: Temporal Dispersion of First Inter-Arrival Time

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skewnorm

# Parameters
n_stars = 1000  # number of stars per simulation
n_simulations = 1000  # number of universe simulations
mean_star_time = 5000  # mean star formation time (Myr)
sigma_star_time = 1000  # standard deviation for star formation time
skewness = 5  # positive skew factor for star formation

mean_life_delay = 1000  # mean life emergence delay (Myr)
sigma_life_delay = 0.7  # spread of life emergence delay

# Store first inter-arrival times
first_arrival_times = []

for _ in range(n_simulations):
    # Sample star formation times
    star_times = skewnorm.rvs(
        a=skewness, loc=mean_star_time, scale=sigma_star_time, size=n_stars
    )

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

# Plot the historical star formation rate (simulated)
# Create a time axis
time_axis = np.linspace(0, 10000, 1000)
# Simulated star formation rate: a skewed normal pdf
sfr_pdf = skewnorm.pdf(time_axis, a=skewness, loc=mean_star_time, scale=sigma_star_time)

plt.figure(figsize=(10, 6))
plt.plot(time_axis, sfr_pdf, label="Simulated Star Formation Rate", color="blue")
plt.xlabel("Time (Myr)")
plt.ylabel("Relative Star Formation Rate")
plt.title("Historical Star Formation Rate (Simulated)")
plt.grid(True)
plt.legend()
plt.savefig("star_formation_rate.png", dpi=300, bbox_inches="tight")
plt.close()

# Optional: print basic stats
print(f"Mean: {np.mean(first_arrival_times):.2f} Myr")
print(f"Std Dev: {np.std(first_arrival_times):.2f} Myr")
print(f"Min: {np.min(first_arrival_times):.2f} Myr")
print(f"Max: {np.max(first_arrival_times):.2f} Myr")
