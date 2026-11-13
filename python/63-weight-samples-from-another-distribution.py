# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2062)

from scipy import stats
proposal_mean = .5
x = rng.normal(proposal_mean, 1, 20000)
log_weight = stats.norm.logpdf(x)-stats.norm.logpdf(x, loc=proposal_mean)
contribution = np.exp(x + log_weight)
print("Weighted target expectation estimate:", round(contribution.mean(), 5))
print("Exact target E[exp(X)]:", round(np.exp(.5), 5))
print("Unweighted proposal average:", round(np.exp(x).mean(), 5))
print("Weighted estimated MCSE:", round(contribution.std(ddof=1)/np.sqrt(len(x)), 6))
