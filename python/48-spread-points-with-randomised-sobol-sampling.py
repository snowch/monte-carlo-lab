# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2047)

from scipy.stats import qmc
estimates, ordinary = [], []
for seed in range(20):
    points = qmc.Sobol(d=2, scramble=True, seed=seed).random_base2(m=10)
    estimates.append(np.exp(points.sum(axis=1)).mean())
    ordinary.append(np.exp(rng.random((1024, 2)).sum(axis=1)).mean())
print("Exact integral:", round((np.e-1)**2, 6))
print("Scrambled Sobol mean / replicate SD:", round(np.mean(estimates), 6), round(np.std(estimates, ddof=1), 6))
print("Ordinary mean / replicate SD:", round(np.mean(ordinary), 6), round(np.std(ordinary, ddof=1), 6))
print("Points per estimate:", 1024)
