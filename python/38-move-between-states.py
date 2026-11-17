# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2037)

transition = np.array([[.75, .20, .05], [.25, .50, .25], [.15, .35, .50]])
assert np.allclose(transition.sum(axis=1), 1)
initial_state = 0  # 0 = clear, 1 = cloudy, 2 = wet
states = np.full(10000, initial_state, dtype=int)
print("Initial state:", initial_state)
print("Proportions in order: clear, cloudy, wet")
for step in range(1, 21):
    cumulative = np.cumsum(transition[states], axis=1)
    states = (rng.random((len(states), 1)) > cumulative).sum(axis=1)
    if step in (1, 5, 20):
        proportions = np.bincount(states, minlength=3) / len(states)
        print(f"Step {step}:", proportions)
print("Row sums:", transition.sum(axis=1))
