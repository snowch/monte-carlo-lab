# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2010)

error_sd = 2
error = rng.normal(loc=0, scale=error_sd, size=20000)
reading = 50 + error
print("Mean reading:", round(reading.mean(), 3))
print("Reading SD:", round(reading.std(ddof=1), 3))
print("Fraction within two error SDs:", round((np.abs(error) <= 2*error_sd).mean(), 4))
durations = rng.normal(1, 2, 20000)
print("Negative duration fraction in a questionable model:", round((durations < 0).mean(), 4))
