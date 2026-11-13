# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2000)

worlds, years = 10000, 5
initial = rng.lognormal(np.log(800),.15,size=worlds)
growth = rng.triangular(.02,.12,.3,size=worlds)
electricity = rng.triangular(.12,.20,.35,size=worlds)  # £ per kWh
demand = initial[:,None]*(1+growth[:,None])**np.arange(years)
budget = 110000
# Label, installed units, sustainable work/day/unit, capex/unit, kW/unit.
options = [("Small fleet",8,220,5000,.25),("Larger fleet",12,220,5000,.25),("Dense fleet",7,360,9000,.4)]
for name, units, capacity, capital, kw in options:
    useful_capacity = units*capacity*.8  # explicit reserve factor
    cost = units*capital+units*kw*24*365*years*electricity
    failure = np.any(demand>useful_capacity,axis=1)
    required = np.ceil(demand.max(axis=1)/(capacity*.8))
    print(name,"P(any capacity shortfall):",round(failure.mean(),3),
          "TCO P90 (£):",round(np.quantile(cost,.9)),"P(over budget):",round((cost>budget).mean(),3),
          "P90 required units:",np.quantile(required,.9))
