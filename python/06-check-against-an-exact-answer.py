# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2005)

from scipy import stats
invited, probability, seats = 150, 0.72, 110
attendance = rng.binomial(invited, probability, size=20000)
estimate = (attendance > seats).mean()
exact = stats.binom.sf(seats, invited, probability)
print("Simulated overflow probability:", round(estimate, 5))
print("Exact model probability:", round(exact, 5))
print("Difference:", round(estimate - exact, 5))
