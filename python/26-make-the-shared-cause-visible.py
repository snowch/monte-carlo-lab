# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2025)

busy_factor = rng.lognormal(0, .25, 20000)
arrivals = rng.poisson(40 * busy_factor)
spend_per_customer = 12 * busy_factor + rng.normal(0, .5, len(busy_factor))
revenue = arrivals * spend_per_customer
print("Arrival/spending correlation:", round(np.corrcoef(arrivals, spend_per_customer)[0, 1], 3))
print("Mean and P90 revenue (£):", round(revenue.mean(), 2), round(np.quantile(revenue, .9), 2))
print("First three shared factors:", busy_factor[:3].round(3))
