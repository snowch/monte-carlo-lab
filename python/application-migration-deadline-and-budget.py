# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2001)

worlds = 10000
complexity = rng.lognormal(-.5*.2**2,.2,size=worlds)
a = rng.triangular(8,12,24,size=worlds)*complexity
b = rng.triangular(6,10,20,size=worlds)*complexity
validation = rng.triangular(3,5,10,size=worlds)*complexity
for label, factor, fixed in [("Standard",1.,15000),("Extra staff",.8,30000),("Smaller first release",.7,25000)]:
    days = factor*np.maximum(a,b)+validation
    cost = fixed+1800*days
    deadline_ok, budget_ok = days<=25, cost<=70000
    assert np.all(days>=validation)
    print(label,"P(deadline):",round(deadline_ok.mean(),3),
          "P(budget):",round(budget_ok.mean(),3),"P(both):",round((deadline_ok&budget_ok).mean(),3),
          "Duration P90 (days):",round(np.quantile(days,.9),2))
