# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2036)
import matplotlib.pyplot as plt

steps = rng.choice([-1, 1], size=(3000, 100))
paths = np.cumsum(steps, axis=1)
final_above = paths[:, -1] >= 10
ever_above = (paths >= 10).any(axis=1)
print("P(final >= 10):", round(final_above.mean(), 4))
print("P(ever >= 10):", round(ever_above.mean(), 4))
plt.plot(paths[:12].T, alpha=.6)
plt.xlabel("Step"); plt.ylabel("Position"); plt.tight_layout()
