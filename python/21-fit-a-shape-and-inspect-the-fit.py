# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2020)

from scipy import stats
observed = np.array([1.2, 1.6, 1.9, 2.0, 2.4, 2.9, 3.1, 4.0, 5.3, 7.2])
shape, loc, scale = stats.lognorm.fit(observed, floc=0)
probabilities = np.array([.1, .5, .9])
print("Empirical quantiles:", np.quantile(observed, probabilities).round(3))
print("Fitted quantiles:", stats.lognorm.ppf(probabilities, shape, loc=loc, scale=scale).round(3))
print("Fitted shape, loc, scale:", round(shape, 4), loc, round(scale, 4))
