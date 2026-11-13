# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2072)

rho = .85
scale = np.sqrt(1-rho*rho)
x, y = 0., 0.
chain = np.empty((16000,2))
for i in range(len(chain)):
    x = rng.normal(rho*y,scale)
    y = rng.normal(rho*x,scale)
    chain[i] = x,y
kept = chain[2000:]
print("Kept means; target [0,0]:", kept.mean(axis=0).round(3))
print("Kept covariance; target diagonal 1 and off-diagonal rho:")
print(np.cov(kept.T).round(3))
print("Lag-1 correlation of X:", round(np.corrcoef(kept[:-1,0],kept[1:,0])[0,1],3))
