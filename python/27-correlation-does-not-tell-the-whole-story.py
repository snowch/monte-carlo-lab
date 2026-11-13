# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2026)
import matplotlib.pyplot as plt

x = rng.uniform(-2, 2, 10000)
y = np.abs(x)
print("Pearson correlation:", round(np.corrcoef(x, y)[0, 1], 4))
print("Maximum mismatch with |X|:", np.max(np.abs(y-np.abs(x))))
plt.scatter(x[::20], y[::20], s=9, alpha=.5, color="#315bf6")
plt.xlabel("X"); plt.ylabel("Y = |X|"); plt.tight_layout()
