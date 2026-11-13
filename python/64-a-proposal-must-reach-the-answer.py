# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2063)

restricted = rng.uniform(0, .5, 30000)
wrong = .5 * restricted**2
component = rng.random(30000) < .8
x = np.where(component, rng.uniform(0, .5, len(component)), rng.random(len(component)))
mixture_density = .2 + 1.6*(x <= .5)
correct = x*x/mixture_density
print("Restricted weighted estimate:", round(wrong.mean(), 5))
print("Full-support mixture estimate:", round(correct.mean(), 5))
print("Exact full target:", 1/3)
print("Mixture sample fraction above .5:", round((x > .5).mean(), 4))
