# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2051)
import pandas as pd

rows = []
choices = np.array([20, 25, 30, 35, 40])
for mean_demand in [18, 22, 26, 30, 34]:
    demand = rng.poisson(mean_demand, 20000)
    losses = 10*np.maximum(demand[:, None]-choices, 0) + 2*np.maximum(choices-demand[:, None], 0)
    average = losses.mean(axis=0)
    rows.append({"assumed_mean":mean_demand, "preferred_stock":choices[np.argmin(average)], "expected_loss":average.min()})
print(pd.DataFrame(rows).to_string(index=False, float_format=lambda x:f"{x:.3f}"))
