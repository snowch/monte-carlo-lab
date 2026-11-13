# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2066)

from scipy import stats
from scipy.special import logsumexp
for shift in [0, 2, 4]:
    x = rng.normal(shift, 1, 20000)
    log_weight = stats.norm.logpdf(x)-stats.norm.logpdf(x, loc=shift)
    weights = np.exp(log_weight-logsumexp(log_weight))
    ess = 1/np.sum(weights**2)
    estimate = np.sum(weights*x)
    print("proposal shift:", shift, "weight ESS:", round(ess, 2),
          "largest normalised weight:", round(weights.max(), 4), "weighted target mean:", round(estimate, 4))
print("Known target mean:", 0)
