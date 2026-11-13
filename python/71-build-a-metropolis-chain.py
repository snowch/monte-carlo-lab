# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2070)
import matplotlib.pyplot as plt

def log_target(p):
    return 19*np.log(p)+13*np.log1p(-p) if 0<p<1 else -np.inf
chain = np.empty(12000)
x, accepted = .2, 0
for i in range(len(chain)):
    proposal = x+rng.normal(0,.12)
    if np.log(rng.random()) < min(0,log_target(proposal)-log_target(x)):
        x = proposal
        accepted += 1
    chain[i] = x
kept = chain[2000:]
print("Acceptance fraction:", round(accepted/len(chain),3))
print("Kept chain mean:", round(kept.mean(),4), "exact:", 20/34)
print("Repeated-state fraction:", round(np.mean(np.diff(kept)==0),3))
plt.plot(chain[:500],linewidth=1,color="#315bf6")
plt.xlabel("Iteration, including warm-up")
plt.ylabel("Parameter p")
