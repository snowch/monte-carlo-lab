# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2014)

n = 2000
values = rng.exponential(scale=5, size=n)
mcse = values.std(ddof=1) / np.sqrt(n)
batches = rng.exponential(scale=5, size=(300, n)).mean(axis=1)
print("Estimated mean wait (minutes):", round(values.mean(), 4))
print("Estimated MCSE (minutes):", round(mcse, 4))
print("Model SE (minutes):", round(5/np.sqrt(n), 4))
print("SD of independent batch means:", round(batches.std(ddof=1), 4))
