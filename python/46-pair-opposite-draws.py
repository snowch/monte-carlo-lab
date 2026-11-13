# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2045)

pairs, repetitions = 100, 300
u = rng.random((repetitions, pairs))
antithetic = ((np.exp(u) + np.exp(1-u))/2).mean(axis=1)
ordinary = np.exp(rng.random((repetitions, 2*pairs))).mean(axis=1)
print("Exact expectation of exp(U):", round(np.e-1, 6))
print("Ordinary SD across estimates:", round(ordinary.std(ddof=1), 6))
print("Antithetic SD across estimates:", round(antithetic.std(ddof=1), 6))
print("Equal function evaluations:", 2*pairs)
