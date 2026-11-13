# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2043)

n = 20000
u, v = rng.random((2, n))
paired_difference = u**3 - u**2
unpaired_difference = v**3 - u**2
print("Exact difference:", -1/12)
for name, difference in [("paired", paired_difference), ("separate", unpaired_difference)]:
    print(name, "estimate:", round(difference.mean(), 5),
          "estimated MCSE:", round(difference.std(ddof=1)/np.sqrt(n), 6))
