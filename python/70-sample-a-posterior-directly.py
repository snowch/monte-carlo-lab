# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2069)

from scipy import stats
a, b, n = 20, 14, 20000
p = rng.beta(a,b,size=n)
event = p > .6
estimate = event.mean()
mcse = event.std(ddof=1)/np.sqrt(n)
print("Posterior P(p > .6), Monte Carlo:", round(estimate,5))
print("Independent-draw MCSE:", round(mcse,5))
print("Exact posterior probability:", round(stats.beta.sf(.6,a,b),5))
print("Posterior outcome SD of p:", round(p.std(ddof=1),5))
