# Demonstration of Algorithmic Strength Reduction
# Replacing a computationally expensive operation with a faster approximation

import math
import time
import numpy as np

# Create large dataset
data = np.random.rand(10_000_000)

# Slow version with high precision
start = time.time()
result_slow = np.exp(data)
end = time.time()
print("High precision time:", end - start)

# Fast version using approximation
# Using a simple approximation
# exp(x) ≈ 1 + x + x^2/2
start = time.time()
result_fast = 1 + data + (data**2) / 2
end = time.time()
print("Approximation time:", end - start)

# Compare difference
error = np.mean(np.abs(result_slow - result_fast))
print("Average error:", error)