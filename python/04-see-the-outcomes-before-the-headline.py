# Copyright © 2026 Christopher Snow
# Ten invented delays, not random draws. No real-world outcomes were measured.
import numpy as np
import matplotlib.pyplot as plt

delay = np.array([1, 1, 2, 2, 3, 3, 4, 4, 5, 15])
print("INVENTED delivery delays (days):", delay)
print("Mean delay (days):", round(delay.mean(), 3))
print("Median and P90 (days):", np.quantile(delay, [.5, .9]).round(3))
plt.hist(delay, bins=8, color="#315bf6", alpha=.85)
plt.xlabel("Delay (days)")
plt.ylabel("Invented observations")
plt.tight_layout()
