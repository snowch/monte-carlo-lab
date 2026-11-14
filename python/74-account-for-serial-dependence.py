# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2073)

rho, n = .9, 16000
x = np.empty(n)
x[0] = rng.normal()
for i in range(1,n):
    x[i] = rho*x[i-1]+np.sqrt(1-rho*rho)*rng.normal()
centred = x-x.mean()
# Inspectable lag correlations; no Fourier-transform machinery is needed.
max_lag = 200  # A teaching cutoff; very long dependence needs a longer analysis.
denominator = np.sum(centred**2)
acf = np.ones(max_lag+1)
for lag in range(1, max_lag+1):
    acf[lag] = np.sum(centred[:-lag]*centred[lag:])/denominator
tau = -1.
for lag in range(0,max_lag,2):
    pair = acf[lag]+acf[lag+1]
    if pair <= 0: break
    tau += 2*pair
tau = max(tau,1.)
ess = n/tau
print("Draws:",n,"estimated mean ESS:",round(ess,1))
print("iid SE:",round(x.std(ddof=1)/np.sqrt(n),5))
print("Dependence-adjusted mean SE:",round(x.std(ddof=1)/np.sqrt(ess),5))
print("Theoretical long-run ESS approximation:",round(n*(1-rho)/(1+rho),1))
