# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2039)

trials, days, lead = 2000, 30, 2
stock = np.full(trials, 20)
pipeline = np.zeros((trials, lead), dtype=int)
lost = np.zeros(trials, dtype=int)
for day in range(days):
    stock += pipeline[:, 0]
    pipeline[:, :-1] = pipeline[:, 1:]
    pipeline[:, -1] = 0
    demand = rng.poisson(5, trials)
    served = np.minimum(stock, demand)
    lost += demand-served
    stock -= served
    order = stock + pipeline.sum(axis=1) < 15
    pipeline[order, -1] += 20
print("Mean lost sales over 30 days:", round(lost.mean(), 3))
print("P(any lost sale):", round((lost > 0).mean(), 4))
print("Mean final stock:", round(stock.mean(), 3))
