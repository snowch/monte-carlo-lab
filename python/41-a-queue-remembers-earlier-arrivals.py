# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2040)

trials, customers = 1000, 100
arrival_rate, service_mean = .8, 1.0
arrivals = rng.exponential(1/arrival_rate, (trials, customers)).cumsum(axis=1)
services = rng.exponential(service_mean, (trials, customers))
finished = np.zeros(trials)
waits = np.zeros((trials, customers))
for i in range(customers):
    starts = np.maximum(arrivals[:, i], finished)
    waits[:, i] = starts-arrivals[:, i]
    finished = starts+services[:, i]
print("Mean customer wait (minutes):", round(waits.mean(), 3))
print("P(customer wait > 5 minutes):", round((waits > 5).mean(), 4))
print("Mean of final customer's wait:", round(waits[:, -1].mean(), 3))
