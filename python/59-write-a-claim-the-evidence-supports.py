# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2058)

from scipy import stats
mean_demand = 25
demand = rng.poisson(mean_demand, 30000)
stock = 32
count = int((demand > stock).sum())
estimate = count/len(demand)
interval = stats.binomtest(count, len(demand)).proportion_ci(.95, method="exact")
print(f"TARGET: P(demand > stock) under Poisson mean {mean_demand}; stock={stock}.")
print("TRIALS / SHORTAGES:", len(demand), count)
print("ESTIMATE:", round(estimate, 5))
print("95% conditional MC interval:", round(interval.low, 5), round(interval.high, 5))
print("LIMIT: input model and penalties have not been empirically validated.")
