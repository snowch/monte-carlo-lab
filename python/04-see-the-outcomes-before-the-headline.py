# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2003)
import matplotlib.pyplot as plt

delay = rng.lognormal(mean=1.2, sigma=0.6, size=5000)
print("Mean delay (days):", round(delay.mean(), 3))
print("Median and P90 (days):", np.quantile(delay, [.5, .9]).round(3))
plt.hist(delay, bins=35, color="#315bf6", alpha=.85)
plt.xlabel("Delay (days)")
plt.ylabel("Simulated draws")
plt.tight_layout()
