# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2008)

rate_per_hour, hours = 4, .5
expected_count = rate_per_hour * hours
counts = rng.poisson(expected_count, 20000)
print("Model expected count:", expected_count)
print("Sample mean / variance:", round(counts.mean(), 3), round(counts.var(ddof=1), 3))
print("Estimated P(no arrivals):", round((counts == 0).mean(), 4))
print("Exact model P(no arrivals):", round(np.exp(-expected_count), 4))
