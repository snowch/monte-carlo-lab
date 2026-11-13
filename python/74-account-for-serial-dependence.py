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
spectrum = np.fft.rfft(centred,n=2*n)
acov = np.fft.irfft(spectrum*np.conj(spectrum))[:n]/n
acf = acov/acov[0]
tau = -1.
for lag in range(0,n-1,2):
    pair = acf[lag]+acf[lag+1]
    if pair <= 0: break
    tau += 2*pair
tau = max(tau,1.)
ess = n/tau
print("Draws:",n,"estimated mean ESS:",round(ess,1))
print("iid SE:",round(x.std(ddof=1)/np.sqrt(n),5))
print("Dependence-adjusted mean SE:",round(x.std(ddof=1)/np.sqrt(ess),5))
print("Theoretical long-run ESS approximation:",round(n*(1-rho)/(1+rho),1))
