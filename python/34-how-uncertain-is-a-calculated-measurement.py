# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2033)

width = rng.normal(10, .1, 30000)
height = rng.normal(5, .2, 30000)
area = width * height
print("Mean area (cm²):", round(area.mean(), 4))
print("Propagated area percentiles 2.5/50/97.5 (cm²):", np.quantile(area, [.025, .5, .975]).round(3))
print("Fraction in specification [48, 52] cm²:", round(((area >= 48) & (area <= 52)).mean(), 4))
