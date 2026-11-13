# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2002)

attendance = rng.binomial(60, 0.65, size=5000)
ticket_price, fixed_cost = 25, 900
profit = ticket_price * attendance - fixed_cost
print("Estimated mean profit (£):", round(profit.mean(), 2))
print("Estimated P(loss):", round((profit < 0).mean(), 4))
print("Profit percentiles 10/50/90 (£):", np.quantile(profit, [.1, .5, .9]))
