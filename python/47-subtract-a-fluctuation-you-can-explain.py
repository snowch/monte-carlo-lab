# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2046)

pilot = rng.random(2000)
beta = np.cov(np.exp(pilot), pilot, ddof=1)[0, 1] / pilot.var(ddof=1)
u = rng.random(20000)
plain = np.exp(u)
controlled = plain - beta*(u-.5)
print("Pilot coefficient:", round(beta, 4))
for name, values in [("plain", plain), ("controlled", controlled)]:
    print(name, "mean:", round(values.mean(), 6), "MCSE:", round(values.std(ddof=1)/np.sqrt(len(values)), 6))
print("Exact target:", round(np.e-1, 6))
