# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2006)

labels = np.array(["standard", "vegetarian", "premium"])
probabilities = np.array([.5, .3, .2])
chosen = rng.choice(labels, size=10000, p=probabilities)
print({label: round((chosen == label).mean(), 4) for label in labels})
costs = {"standard": 7, "vegetarian": 6, "premium": 11}
print("Estimated mean ingredient cost (£):", round(np.mean([costs[x] for x in chosen]), 3))
