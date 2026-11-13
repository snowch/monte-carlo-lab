# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2061)

proposal = rng.random(30000)
accept = rng.random(len(proposal)) < proposal
accepted = proposal[accept]
print("Proposals / accepted:", len(proposal), len(accepted))
print("Acceptance fraction / target:", round(accept.mean(), 4), .5)
print("Accepted sample mean / target:", round(accepted.mean(), 4), 2/3)
print("All accepted values in support:", bool(((accepted >= 0) & (accepted <= 1)).all()))
