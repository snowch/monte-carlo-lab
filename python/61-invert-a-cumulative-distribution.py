# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2060)

from scipy import stats
u = rng.random(20000)
scale = 2
transformed = -scale*np.log1p(-u)
reference = stats.expon.ppf(u, scale=scale)
assert np.allclose(transformed, reference)
print("Maximum inverse-CDF difference:", round(np.max(np.abs(transformed-reference)), 12))
print("Sample / model means:", round(transformed.mean(), 4), scale)
print("Sample median / model median:", round(np.median(transformed), 4), round(scale*np.log(2), 4))
