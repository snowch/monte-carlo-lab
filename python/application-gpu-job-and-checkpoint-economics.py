# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2002)

worlds, useful_hours, mean_uptime = 1000, 20., 8.
max_attempts = 500
uniforms = rng.random((worlds,max_attempts))
interruptions = -mean_uptime*np.log1p(-uniforms)
for chunk in [.5,2.,5.]:
    chunks = int(useful_hours/chunk)
    checkpoint_hours, rate = .05, 3.0
    elapsed, failures = np.zeros(worlds), np.zeros(worlds,dtype=int)
    for world in range(worlds):
        completed, attempt = 0, 0
        while completed < chunks:
            if attempt >= max_attempts:
                raise RuntimeError("Attempt cap reached; inspect the model")
            lifetime = interruptions[world,attempt]
            attempt += 1
            elapsed[world] += min(lifetime,chunk)
            if lifetime >= chunk:
                completed += 1
                elapsed[world] += checkpoint_hours
            else:
                failures[world] += 1
    assert np.all(elapsed>=useful_hours+chunks*checkpoint_hours-1e-9)
    print("Chunk (h):",chunk,"mean billed £:",round((rate*elapsed).mean(),2),
          "P90 completion (h):",round(np.quantile(elapsed,.9),2),"mean interruptions:",round(failures.mean(),2))
