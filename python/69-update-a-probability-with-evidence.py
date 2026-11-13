# Copyright © 2026 Christopher Snow
# Exact calculation with invented observations. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2068)

from scipy import stats
a, b = 2, 2
successes, trials = 18, 30
post_a, post_b = a+successes, b+trials-successes
print("INVENTED observations:", successes, "successes from", trials)
print("Prior mean:", a/(a+b))
print("Posterior shapes:", post_a, post_b)
print("Posterior mean:", post_a/(post_a+post_b))
print("Central 95% posterior interval for p:", stats.beta.ppf([.025,.975],post_a,post_b).round(4))
