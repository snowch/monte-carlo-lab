# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2000)

invited, probability, seats = 150, 0.72, 110
attendance = rng.binomial(invited, probability, size=10000)
overflow = attendance > seats
print("Simulated events:", len(attendance))
print("Estimated P(attendance > seats):", round(overflow.mean(), 4))
print("Mean attendance:", round(attendance.mean(), 2))

# Inspect the actual simulated distribution, not only its mean.
import matplotlib.pyplot as plt
bins = np.arange(attendance.min() - .5, attendance.max() + 1.5)
plt.hist(attendance, bins=bins, color="#6750ad")
plt.axvline(seats + .5, color="#197568", linestyle="--",
            label=f"Overflow: above {seats}")
plt.xlabel("Attendees per event"); plt.ylabel("Simulated events")
plt.legend(); plt.tight_layout()
