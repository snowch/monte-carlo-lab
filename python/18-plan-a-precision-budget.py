# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2017)

from scipy import stats
z = stats.norm.ppf(.975)
for half_width in [.05, .02, .01]:
    n = int(np.ceil(z*z*.25/(half_width*half_width)))
    print("Target approximate half-width:", half_width, "planned trials:", n)
pilot_sd, mean_half_width = 12, .5
n_mean = int(np.ceil((z*pilot_sd/mean_half_width)**2))
print("Mean-estimation count from assumed SD:", n_mean)
