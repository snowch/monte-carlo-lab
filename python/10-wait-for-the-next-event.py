# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2009)

rate_per_hour = 3
waits = rng.exponential(scale=1/rate_per_hour, size=30000)
already_waited = .5
remaining = waits[waits > already_waited] - already_waited
print("Mean wait (hours):", round(waits.mean(), 4))
print("Mean remaining wait after 0.5 hours:", round(remaining.mean(), 4))
print("Model mean wait:", 1/rate_per_hour)
