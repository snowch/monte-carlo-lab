# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2012)

for n in [25, 400, 6400]:
    batches = rng.normal(100, 20, size=(100, n))
    print("Draws per batch:", n,
          "average outcome SD:", round(batches.std(axis=1, ddof=1).mean(), 2),
          "SD of batch means:", round(batches.mean(axis=1).std(ddof=1), 3))
