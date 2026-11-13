# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2041)

horizon = 100
fractions = []
for trial in range(2000):
    t, up_time, down_time = 0.0, 0.0, 0.0
    while t < horizon:
        up = min(rng.exponential(10), horizon-t)
        up_time += up; t += up
        if t < horizon:
            down = min(rng.exponential(2), horizon-t)
            down_time += down; t += down
    assert abs(up_time+down_time-horizon) < 1e-8
    fractions.append(up_time/horizon)
print("Mean finite-window availability:", round(np.mean(fractions), 4))
print("Long-run reference for this model:", round(10/(10+2), 4))
