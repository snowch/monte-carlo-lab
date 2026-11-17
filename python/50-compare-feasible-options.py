# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2049)
import pandas as pd

demand = rng.poisson(25, 30000)
max_shortage_probability = 0.10
rows = []
for stock in [25, 28, 32, 36]:
    loss = 10*np.maximum(demand-stock, 0) + 2*np.maximum(stock-demand, 0)
    risk = (demand > stock).mean()
    rows.append({"stock":stock, "expected_loss":loss.mean(), "shortage_probability":risk,
                 "meets_point_estimate_rule":risk <= max_shortage_probability})
result = pd.DataFrame(rows)
print(f"Shortage probability limit: {max_shortage_probability:g}")
print(result.to_string(index=False, float_format=lambda x:f"{x:.4f}"))
feasible = result[result.meets_point_estimate_rule]
if feasible.empty:
    print("No tested stock level meets the limit based on its estimated shortage probability.")
else:
    print("Best feasible point-estimate choice:", int(feasible.loc[feasible.expected_loss.idxmin(), "stock"]))
