# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2024)

u, v = rng.random((2, 30000))
independent_total = (20 + 20*u) + (20 + 20*v)
shared_total = (20 + 20*u) + (20 + 20*u)
for name, total in [("independent", independent_total), ("shared", shared_total)]:
    print(name, "mean:", round(total.mean(), 3), "P(total > 70):", round((total > 70).mean(), 4))
