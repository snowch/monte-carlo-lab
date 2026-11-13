# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2007)

n, p = 30, .95
passed = rng.binomial(n, p, 20000)
print("Observed range:", passed.min(), passed.max())
print("Sample / model means:", round(passed.mean(), 3), n*p)
print("Sample / model variances:", round(passed.var(ddof=1), 3), n*p*(1-p))
print("Estimated P(all pass):", round((passed == n).mean(), 4))
