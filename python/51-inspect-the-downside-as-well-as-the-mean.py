# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2050)

loss = rng.lognormal(3, 1, 30000)
p95 = np.quantile(loss, .95)
tail = loss[loss >= p95]
print("Mean loss:", round(loss.mean(), 3))
print("P95 loss:", round(p95, 3))
print("Empirical mean at/above P95:", round(tail.mean(), 3))
print("Tail observations:", len(tail), "of", len(loss))
print("Largest observed loss:", round(loss.max(), 3))
