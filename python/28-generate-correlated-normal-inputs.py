# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2027)

rho = .7
assert -1 <= rho <= 1, "Correlation must lie between -1 and 1"
z = rng.normal(size=(20000, 2))
a = z[:, 0]
b = rho*a + np.sqrt(1-rho*rho)*z[:, 1]
paired = np.column_stack([a, b])  # Put the two inputs into columns.
cost_a = 100 + 10*paired[:, 0]
cost_b = 80 + 8*paired[:, 1]
print("Sample standardised covariance:")
print(np.cov(paired, rowvar=False).round(3))
print("Correlation:", round(np.corrcoef(cost_a, cost_b)[0, 1], 3))
print("Total-cost SD:", round((cost_a+cost_b).std(ddof=1), 3))
