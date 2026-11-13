# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2037)

transition = np.array([[.75, .20, .05], [.25, .50, .25], [.15, .35, .50]])
assert np.allclose(transition.sum(axis=1), 1)
states = np.zeros(10000, dtype=int)
for day in range(20):
    cumulative = np.cumsum(transition[states], axis=1)
    states = (rng.random((len(states), 1)) > cumulative).sum(axis=1)
print("Final proportions for clear/cloudy/wet:", np.bincount(states, minlength=3)/len(states))
print("Row sums:", transition.sum(axis=1))
