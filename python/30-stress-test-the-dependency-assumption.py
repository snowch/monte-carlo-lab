# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2029)
import pandas as pd

rows = []
z = rng.normal(size=(30000, 2))
for rho in [-.5, 0, .5, .9]:
    factor = np.linalg.cholesky([[1, rho], [rho, 1]])
    paired = z @ factor.T
    total = 180 + 10*paired[:, 0] + 10*paired[:, 1]
    rows.append({"rho_scenario":rho, "mean_total":total.mean(), "P_above_205":(total > 205).mean()})
print(pd.DataFrame(rows).to_string(index=False, float_format=lambda x:f"{x:.4f}"))
