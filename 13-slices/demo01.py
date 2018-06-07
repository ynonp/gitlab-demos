import numpy as np

# Indexes and Slices
# 1. Access
# 2. Scikit-Image - slices

arr = np.arange(1, 100).reshape(33, 3)
print(arr)

print(arr[2,2])

###################
print(arr[2])
print(arr[:, 1])

print(arr[0:2,0:2])

#############
print('-----')
print(arr[(0, 2), (0, 1)])
print(arr.shape)



############
game = np.array([
    ['x', 'o', ' '],
    ['x', 'x', 'o'],
    ['o', ' ', 'x'],
])

print(np.all(game[(0, 1, 2), (0, 1, 2)] == ['x', 'x', 'x']))
