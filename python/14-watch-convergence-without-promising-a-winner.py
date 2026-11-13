# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2013)
import matplotlib.pyplot as plt

u = rng.random(20000)
running = np.cumsum(u**2) / np.arange(1, len(u)+1)
for n in [100, 400, 1600, 6400]:
    batches = rng.random((200, n))**2
    rmse = np.sqrt(np.mean((batches.mean(axis=1)-1/3)**2))
    print("n:", n, "RMSE across batches:", round(rmse, 5))
plt.plot(np.arange(1, len(u)+1), running, color="#315bf6")
plt.axhline(1/3, color="#a45c37", linestyle="--", label="Exact expectation")
plt.xscale("log"); plt.xlabel("Independent draws"); plt.ylabel("Running estimate of E[U²]")
plt.legend(); plt.tight_layout()
