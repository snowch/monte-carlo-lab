# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2021)

low, mode, high = 2, 4, 12
duration = rng.triangular(low, mode, high, 20000)
print("Sample mean (days):", round(duration.mean(), 3))
print("Model mean (days):", (low+mode+high)/3)
print("Median and P90 (days):", np.quantile(duration, [.5, .9]).round(3))
print("Any draw above hard upper bound:", bool((duration > high).any()))
