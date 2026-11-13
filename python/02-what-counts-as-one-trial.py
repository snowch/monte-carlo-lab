# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2001)

guest_attends = rng.random((6, 8)) < 0.6
counts = guest_attends.sum(axis=1)
print("Rows=events, columns=guests:")
print(guest_attends.astype(int))
print("Attendance per event:", counts)
print("Fraction of events above 5 guests:", (counts > 5).mean())
print("Guest attendance fraction:", guest_attends.mean())
