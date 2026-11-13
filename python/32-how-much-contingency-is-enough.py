# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2031)

hours = rng.triangular(30, 40, 65, 20000)
materials = rng.lognormal(np.log(700), .2, 20000)
total_cost = 40*hours + materials
baseline = 2500
p90 = np.quantile(total_cost, .9)
print("Mean / P90 cost (£):", round(total_cost.mean(), 2), round(p90, 2))
print("Baseline budget (£):", baseline)
print("Additional reserve to model P90 (£):", round(max(0, p90-baseline), 2))
print("Estimated P(over baseline):", round((total_cost > baseline).mean(), 4))
