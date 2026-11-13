# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2057)

parent = np.random.SeedSequence(2026)
children = parent.spawn(4)
streams = [np.random.default_rng(child) for child in children]
first_draws = [stream.integers(0, 1000000, 4).tolist() for stream in streams]
replay_children = np.random.SeedSequence(2026).spawn(4)
replay = [np.random.default_rng(child).integers(0, 1000000, 4).tolist() for child in replay_children]
assert first_draws == replay
print("Child-stream first draws:", first_draws)
print("Replay identical:", first_draws == replay)
print("Spawn keys:", [child.spawn_key for child in children])
