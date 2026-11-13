# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2053)

latent = rng.normal(size=30000)
signal = latent + rng.normal(0, 1, len(latent))
demand = np.maximum(0, np.rint(25+5*latent+rng.normal(0, 3, len(latent)))).astype(int)
fixed_stock = np.full(len(demand), 30)
adaptive_stock = np.where(signal > .5, 36, 27)
for name, stock in [("fixed", fixed_stock), ("signal policy", adaptive_stock)]:
    loss = 10*np.maximum(demand-stock, 0)+2*np.maximum(stock-demand, 0)
    print(name, "expected loss:", round(loss.mean(), 3), "P(shortage):", round((demand > stock).mean(), 4))
print("Signal / demand correlation:", round(np.corrcoef(signal, demand)[0, 1], 3))
