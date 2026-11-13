# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2027)

correlation = np.array([[1.0, .7], [.7, 1.0]])
factor = np.linalg.cholesky(correlation)
z = rng.normal(size=(20000, 2))
paired = z @ factor.T
cost_a = 100 + 10*paired[:, 0]
cost_b = 80 + 8*paired[:, 1]
print("Sample standardised covariance:")
print(np.cov(paired, rowvar=False).round(3))
print("Correlation:", round(np.corrcoef(cost_a, cost_b)[0, 1], 3))
print("Total-cost SD:", round((cost_a+cost_b).std(ddof=1), 3))
