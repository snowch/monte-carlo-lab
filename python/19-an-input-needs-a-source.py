# Copyright © 2026 Christopher Snow
# Invented input register. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2018)
import pandas as pd

inputs = pd.DataFrame([
    {"name":"arrivals", "value":48, "unit":"per day", "source":"assumption"},
    {"name":"open_hours", "value":8, "unit":"hours/day", "source":"scenario"},
    {"name":"service_mean", "value":7, "unit":"minutes", "source":"invented pilot estimate"}])
print(inputs.to_string(index=False))
arrivals_per_hour = inputs.value.iloc[0] / inputs.value.iloc[1]
print("Converted assumed arrival rate per hour:", arrivals_per_hour)
