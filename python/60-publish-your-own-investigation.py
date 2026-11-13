# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2059)
import pandas as pd

import os
case = "inventory"  # inventory, project, or measurement
assert case in {"inventory", "project", "measurement"}, "Choose a documented case"
defaults = {
    "inventory": [42, 55, 61, 47, 83, 59, 66, 52, 74, 58],
    "project": [2, 3, 4, 5, 7, 3, 6, 4, 8, 5],
    "measurement": [9.8, 10.1, 10.0, 9.9, 10.2, 10.1, 9.95, 10.05]}
if os.path.exists("data.csv"):
    data = pd.read_csv("data.csv")
    assert "value" in data.columns, "CSV needs a value column"
    values = data.value.to_numpy(dtype=float)
    print("INPUT: uploaded CSV; justify its provenance and sampling assumptions.")
else:
    values = np.asarray(defaults[case], dtype=float)
    print("INPUT: INVENTED starter values, not measured evidence.")
assert len(values) >= 8, "Use at least eight input observations for this exercise"
assert np.isfinite(values).all() and (values > 0).all(), "Values must be positive and finite"
assert np.ptp(values) > 0, "Constant inputs need a different uncertainty argument"
n = 10000
print("CASE:", case, "TRIALS:", n, "INPUT OBSERVATIONS:", len(values))
if case == "inventory":
    demand = rng.choice(values, n, replace=True)
    rows = []
    for stock in [50, 65, 80]:
        loss = 12*np.maximum(demand-stock, 0)+2*np.maximum(stock-demand, 0)
        rows.append({"stock":stock, "P_shortage":(demand > stock).mean(),
            "expected_loss":loss.mean(), "MCSE_expected_loss":loss.std(ddof=1)/np.sqrt(n)})
    print(pd.DataFrame(rows).to_string(index=False, float_format=lambda x:f"{x:.4f}"))
elif case == "project":
    baseline = rng.choice(values, (n, 5), replace=True).sum(axis=1)
    for multiplier in [1.0, .85, .7]:
        finish = baseline*multiplier
        print("Duration multiplier:", multiplier, "P(finish <= 20 days):", round((finish <= 20).mean(), 4),
              "P90 days:", round(np.quantile(finish, .9), 3))
else:
    radius = rng.choice(values, n, replace=True)
    area = np.pi*radius**2
    print("Mean area (cm²):", round(area.mean(), 4))
    print("Propagated area percentiles 2.5/50/97.5:", np.quantile(area, [.025, .5, .975]).round(4))
    print("MCSE of mean area:", round(area.std(ddof=1)/np.sqrt(n), 5))
print("LIMIT: empirical independent resampling is an assumption; model uncertainty remains.")
