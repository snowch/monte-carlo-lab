# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2035)

a, b = 0, 2
x = rng.uniform(a, b, 20000)
f = x*x
estimate = (b-a)*f.mean()
mcse = (b-a)*f.std(ddof=1)/np.sqrt(len(f))
exact = (b**3-a**3)/3
print("Integral estimate:", round(estimate, 5))
print("Estimated MCSE:", round(mcse, 5))
print("Exact integral:", round(exact, 5))
print("Unscaled average:", round(f.mean(), 5))
