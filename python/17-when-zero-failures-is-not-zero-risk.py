# Copyright © 2026 Christopher Snow
# Constructed simulation record. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2016)

from scipy import stats
n, failures = 1000, 0
interval = stats.binomtest(failures, n).proportion_ci(.95, method="exact")
one_sided_upper = 1 - .05**(1/n)
print("Observed failure fraction:", failures/n)
print("Two-sided 95% exact interval:", round(interval.low, 6), round(interval.high, 6))
print("One-sided 95% upper bound:", round(one_sided_upper, 6))
print("Naive plug-in SE:", np.sqrt((failures/n)*(1-failures/n)/n))
