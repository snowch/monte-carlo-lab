# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2023)
import pandas as pd

scenarios = {"ordinary": 40, "busy": 70, "disrupted": 100}
rows = []
for name, mean_demand in scenarios.items():
    demand = rng.poisson(mean_demand, 10000)
    rows.append({"scenario":name, "assumed_mean":mean_demand,
                 "P_above_80":float((demand > 80).mean())})
print(pd.DataFrame(rows).to_string(index=False, float_format=lambda x:f"{x:.4f}"))
