# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2015)

from scipy import stats
waits = rng.exponential(5, size=10000)
mean = waits.mean()
mcse = waits.std(ddof=1)/np.sqrt(len(waits))
margin = stats.norm.ppf(.975) * mcse
print("Mean wait estimate (minutes):", round(mean, 4))
print("Approximate 95% MC interval:", np.array([mean-margin, mean+margin]).round(4))
print("Known model expectation:", 5)
print("Outcome percentiles 2.5/97.5:", np.quantile(waits, [.025, .975]).round(3))
