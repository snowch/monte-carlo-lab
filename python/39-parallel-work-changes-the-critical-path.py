# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2038)

a = rng.triangular(2, 4, 8, 20000)
b = rng.triangular(3, 6, 11, 20000)
review = rng.triangular(1, 2, 5, 20000)
serial = a + b + review
parallel = np.maximum(a, b) + review
assert np.all(parallel <= serial)
print("Serial / parallel median (days):", round(np.median(serial), 3), round(np.median(parallel), 3))
print("Parallel P(finish <= 12 days):", round((parallel <= 12).mean(), 4))
print("Fraction where B is the longer preparation:", round((b > a).mean(), 4))
