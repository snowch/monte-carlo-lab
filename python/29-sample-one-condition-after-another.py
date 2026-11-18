# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2028)

rain_probability = .3
rainy = rng.random(30000) < rain_probability
attendance_probability = np.where(rainy, .5, .8)
attendance = rng.binomial(100, attendance_probability)
exact_mean = 100*(.3*.5 + .7*.8)
print("Simulated / exact mean attendance:", round(attendance.mean(), 3), exact_mean)
print("Mean on rainy / dry days:", round(attendance[rainy].mean(), 2), round(attendance[~rainy].mean(), 2))
print("Overall attendance SD:", round(attendance.std(ddof=1), 3))
print("P(attendance > 80):", round((attendance > 80).mean(), 4))
