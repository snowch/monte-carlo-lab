# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2052)

demand = rng.poisson(25, 40000)
choices = np.array([15, 20, 25, 30, 35, 40])
loss = 10*np.maximum(demand[:, None]-choices, 0) + 2*np.maximum(choices-demand[:, None], 0)
best_fixed = loss.mean(axis=0).min()
perfect_information = loss.min(axis=1).mean()
evpi = best_fixed-perfect_information
regret = loss-loss.min(axis=1, keepdims=True)
print("Best fixed expected loss:", round(best_fixed, 4))
print("Perfect-information expected loss:", round(perfect_information, 4))
print("EVPI upper bound before information cost:", round(evpi, 4))
print("Expected regret by stock choice:", regret.mean(axis=0).round(3))
assert evpi >= -1e-10
