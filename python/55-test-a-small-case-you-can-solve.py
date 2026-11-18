# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2054)

def loss(demand, stock):
    return 10*np.maximum(demand-stock, 0)+2*np.maximum(stock-demand, 0)
cases = [(0, 5, 10), (5, 5, 0), (8, 5, 30)]
for demand, stock, expected in cases:
    actual = float(loss(demand, stock))
    print("demand, stock, actual, expected:", demand, stock, actual, expected)
    assert actual == expected
print("All exact boundary cases passed.")
