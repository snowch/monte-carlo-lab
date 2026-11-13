# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2065)

from scipy import stats
n, threshold, shift = 30000, 5, 5
naive = rng.normal(size=n) > threshold
x = rng.normal(shift, 1, n)
log_weight = -shift*x + shift*shift/2
contribution = (x > threshold)*np.exp(log_weight)
print("Naive target hits:", int(naive.sum()), "of", n)
print("Proposal hit fraction:", round((x > threshold).mean(), 4))
print("Importance estimate:", format(contribution.mean(), '.7g'))
print("Estimated MCSE:", format(contribution.std(ddof=1)/np.sqrt(n), '.7g'))
print("Exact target tail:", format(stats.norm.sf(threshold), '.7g'))
