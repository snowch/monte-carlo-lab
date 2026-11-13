# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2011)

log_mean, log_sd = np.log(10), .7
value = rng.lognormal(log_mean, log_sd, 30000)
print("Sample median:", round(np.median(value), 3))
print("Model median:", round(np.exp(log_mean), 3))
print("Sample mean:", round(value.mean(), 3))
print("Model mean:", round(np.exp(log_mean + log_sd**2/2), 3))
print("Minimum sampled value:", round(value.min(), 4))
