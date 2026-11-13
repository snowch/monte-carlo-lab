# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2071)

from scipy import stats
def log_target(p):
    return stats.beta.logpdf(p,20,14)
def log_q(p):
    return stats.beta.logpdf(p,3,3)
x, accepted = .5, 0
chain = np.empty(12000)
for i in range(len(chain)):
    proposal = rng.beta(3,3)
    log_ratio = log_target(proposal)-log_target(x)+log_q(x)-log_q(proposal)
    if np.log(rng.random()) < min(0,log_ratio):
        x = proposal
        accepted += 1
    chain[i] = x
print("Acceptance fraction:", round(accepted/len(chain),3))
print("Kept mean:", round(chain[2000:].mean(),4), "exact:", 20/34)
