# Copyright © 2026 Christopher Snow
# Constructed log-weight example. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2064)

from scipy.special import logsumexp
log_weights = np.array([-1001.0, -1000.0, -999.0])
direct = np.exp(log_weights)
weights = np.exp(log_weights-logsumexp(log_weights))
shifted = np.exp((log_weights+5000)-logsumexp(log_weights+5000))
assert np.allclose(weights, shifted)
print("Direct exponential sum:", direct.sum())
print("Stable normalised weights:", weights.round(6))
print("Weight sum:", round(weights.sum(), 12))
print("Weighted average of [1,2,3]:", round(np.dot(weights, [1,2,3]), 6))
