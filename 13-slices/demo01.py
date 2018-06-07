import numpy as np

# Indexes and Slices
# 1. Access
# 2. Scikit-Image - slices

print("new version")

############
game = np.array([
    ['x', 'o', ' '],
    ['x', 'x', 'o'],
    ['o', ' ', 'x'],
])

print(np.all(game[(0, 1, 2), (0, 1, 2)] == ['x', 'x', 'x']))
