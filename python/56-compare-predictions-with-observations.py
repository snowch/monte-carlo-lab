# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2055)

from scipy import stats
observed_holdout = np.array([18, 22, 25, 20, 31, 28, 23, 27, 35, 24, 29, 26])
assumed_mean = 20
upper = stats.poisson.ppf(.9, assumed_mean)
simulated = rng.poisson(assumed_mean, 30000)
print("Model nominal P90 count:", upper)
print("Model fraction <= threshold:", round((simulated <= upper).mean(), 4))
print("Held-out observed fraction <= threshold:", round((observed_holdout <= upper).mean(), 4))
print("Holdout observations:", len(observed_holdout))
