# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2048)
import pandas as pd

demand = rng.poisson(25, 20000)
rows = []
for stock in [20, 25, 30, 35]:
    shortage = np.maximum(demand-stock, 0)
    leftover = np.maximum(stock-demand, 0)
    loss = 10*shortage + 2*leftover
    rows.append({"stock":stock, "expected_loss":loss.mean(), "P_shortage":(shortage > 0).mean()})
print(pd.DataFrame(rows).to_string(index=False, float_format=lambda x:f"{x:.3f}"))
