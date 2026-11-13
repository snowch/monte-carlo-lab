# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2075)

from scipy import stats
a, b, future_n, draws = 20, 14, 20, 20000
p = rng.beta(a,b,size=draws)
predictive = rng.binomial(future_n,p)
plugin = rng.binomial(future_n,a/(a+b),size=draws)
print("Full predictive mean / variance:", round(predictive.mean(),3),round(predictive.var(ddof=1),3))
print("Exact beta-binomial mean / variance:", stats.betabinom.stats(future_n,a,b,moments="mv"))
print("Plug-in mean / variance:",round(plugin.mean(),3),round(plugin.var(ddof=1),3))
print("Full predictive count quantiles:",np.quantile(predictive,[.05,.5,.95]))
print("Posterior p quantiles:",np.quantile(p,[.05,.5,.95]).round(3))
