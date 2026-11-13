# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2030)

tasks = np.column_stack([
    rng.triangular(2, 4, 8, 20000),
    rng.triangular(3, 5, 10, 20000),
    rng.triangular(1, 3, 7, 20000)])
finish = tasks.sum(axis=1)
deadline = 16
print("Median/P90 completion (days):", np.quantile(finish, [.5, .9]).round(3))
print("Estimated P(finish <= 16 days):", round((finish <= deadline).mean(), 4))
print("Mean task durations:", tasks.mean(axis=0).round(3))
