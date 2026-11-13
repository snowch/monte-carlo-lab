# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2044)

n, repetitions = 100, 300
ordinary = np.mean(rng.random((repetitions, n))**2, axis=1)
stratified_u = (np.arange(n)[None, :] + rng.random((repetitions, n))) / n
stratified = np.mean(stratified_u**2, axis=1)
print("Exact expectation:", 1/3)
print("SD across ordinary estimates:", round(ordinary.std(ddof=1), 6))
print("SD across stratified estimates:", round(stratified.std(ddof=1), 6))
print("Evaluations per estimate:", n)
