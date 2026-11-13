# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2004)

first = np.random.default_rng(17)
replay = np.random.default_rng(17)
other = np.random.default_rng(18)
a = first.integers(0, 100, 8)
b = replay.integers(0, 100, 8)
c = other.integers(0, 100, 8)
print("Original:", a)
print("Replay:", b)
print("Different seed:", c)
print("Replay identical:", np.array_equal(a, b))
