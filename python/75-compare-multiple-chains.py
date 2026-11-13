# Copyright © 2026 Christopher Snow
# Constructed diagnostic draws. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2074)

from scipy import stats
def basic_rhat(z):
    m, n = z.shape
    within = np.var(z,axis=1,ddof=1).mean()
    between = n*np.var(z.mean(axis=1),ddof=1)
    return np.sqrt(((n-1)/n*within+between/n)/within)
def rank_normalise(z):
    ranks = stats.rankdata(z.ravel()).reshape(z.shape)
    return stats.norm.ppf((ranks-.375)/(z.size+.25))
def diagnostics(chains):
    half = chains.shape[1]//2
    z = np.concatenate([chains[:,:half],chains[:,-half:]],axis=0)
    rank_rhat = basic_rhat(rank_normalise(z))
    folded = np.abs(z-np.median(z))
    folded_rhat = basic_rhat(rank_normalise(folded))
    return basic_rhat(z), max(rank_rhat,folded_rhat)
good = rng.normal(size=(4,4000))
scale_mismatch = good*np.array([1,1,1,2])[:,None]
for label, chains in [("Agreement",good),("Scale disagreement",scale_mismatch)]:
    raw, modern = diagnostics(chains)
    print(label,"raw split R-hat:",round(raw,4),"rank/folded maximum:",round(modern,4))
