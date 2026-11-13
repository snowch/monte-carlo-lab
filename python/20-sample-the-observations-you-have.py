# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2019)

observed = np.array([42, 55, 61, 47, 83, 59, 66, 52, 74, 58])
simulated = rng.choice(observed, size=10000, replace=True)
print("Observed and resampled means:", observed.mean(), round(simulated.mean(), 3))
print("Observed range:", observed.min(), observed.max())
print("Resampled range:", simulated.min(), simulated.max())
print("P(demand > 80) under this empirical model:", round((simulated > 80).mean(), 4))
