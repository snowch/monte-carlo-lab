# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2067)

from scipy import stats
from scipy.special import logsumexp, gamma
x = rng.normal(size=20000)
log_weight = -x**4/4 - stats.norm.logpdf(x)
weights = np.exp(log_weight-logsumexp(log_weight))
estimate = np.sum(weights*x*x)
exact = 2*gamma(.75)/gamma(.25)
print("Self-normalised E[X²] estimate:", round(estimate, 6))
print("Analytical target E[X²]:", round(exact, 6))
print("Weighted symmetry check E[X]:", round(np.sum(weights*x), 5))
print("Weight ESS diagnostic:", round(1/np.sum(weights*weights), 2))
