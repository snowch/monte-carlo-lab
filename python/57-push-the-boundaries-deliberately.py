# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2056)

demand = np.array([0, 1, 10, 1000])
for stock in [0, 5, 100]:
    served = np.minimum(demand, stock)
    unmet = demand-served
    remaining = stock-served
    assert np.all((served >= 0) & (served <= demand))
    assert np.all(served+unmet == demand)
    assert np.all(remaining >= 0)
    print("stock:", stock, "served:", served, "unmet:", unmet)
print("Ledger invariants passed for extreme cases.")
