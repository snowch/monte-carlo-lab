# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2022)

observed = np.array([42, 55, 61, 47, 83, 59, 66, 52, 74, 58])
samples = rng.choice(observed, size=(5000, len(observed)), replace=True)
bootstrap_means = samples.mean(axis=1)
print("Daily-demand SD:", round(observed.std(ddof=1), 3))
print("Bootstrap SD of estimated mean:", round(bootstrap_means.std(ddof=1), 3))
print("Percentile bootstrap interval for mean:", np.quantile(bootstrap_means, [.025, .975]).round(3))
