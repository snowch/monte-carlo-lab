# Copyright © 2026 Christopher Snow
# Seeded teaching simulation. No real-world outcomes were measured.
import numpy as np
rng = np.random.default_rng(2042)

inputs = rng.normal(10, 2, size=(2000, 3))
loop_result = np.array([row[0] + max(row[1], row[2]) for row in inputs])
array_result = inputs[:, 0] + np.maximum(inputs[:, 1], inputs[:, 2])
assert np.array_equal(loop_result, array_result)
chunked = np.concatenate([chunk[:, 0]+np.maximum(chunk[:, 1], chunk[:, 2]) for chunk in np.array_split(inputs, 7)])
assert np.array_equal(chunked, array_result)
print("Loop/vector/chunk answers identical:", True)
print("Input array bytes:", inputs.nbytes)
print("Mean outcome:", round(array_result.mean(), 4))
