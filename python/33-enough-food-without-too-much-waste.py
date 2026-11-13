# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2032)
import pandas as pd

attendance = rng.binomial(150, .72, 20000)
rows = []
for meals in [100, 110, 120]:
    shortage = np.maximum(attendance-meals, 0)
    waste = np.maximum(meals-attendance, 0)
    loss = 12*shortage + 3*waste
    rows.append({"meals":meals, "P_shortage":(shortage > 0).mean(), "expected_loss":loss.mean()})
print(pd.DataFrame(rows).to_string(index=False, float_format=lambda x:f"{x:.3f}"))
