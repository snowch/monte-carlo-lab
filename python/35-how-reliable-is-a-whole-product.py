# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2034)

reliability = np.array([.98, .96, .99])
working = rng.random((50000, 3)) < reliability
series = working.all(axis=1)
parallel = working.any(axis=1)
print("Series simulated / exact:", round(series.mean(), 5), round(np.prod(reliability), 5))
print("Parallel simulated / exact:", round(parallel.mean(), 5), round(1-np.prod(1-reliability), 5))
print("Simulated trials:", len(working))
