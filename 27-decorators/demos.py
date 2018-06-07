"""
1. Sharing code between functions
2. Generic Decorators
3. Parameterized Decorators
"""

def matrix_do(size, f):
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            print(f(i, j), end='')
        print('')

def matrix_sum(size):
    matrix_do(size, lambda i, j: f'{i + j:5}')

def matrix_mul(size):
    matrix_do(size, lambda i, j: f'{i * j:5}')

matrix_sum(10)
print('--')
matrix_mul(10)
