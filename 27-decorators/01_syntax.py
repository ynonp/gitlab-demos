"""
Decorator Syntax
"""

def do_in_matrix(f):
    def wrapper(size):
        for i in range(1, size + 1):
            for j in range(1, size + 1):
                print(f(i, j), end='')
            print('')
    return wrapper

@do_in_matrix
def matrix_sum(i, j):
    return f'{i + j:5}'

@do_in_matrix
def matrix_mul(i, j):
    return f'{i*j:5}'

matrix_sum(10)
print('--')
matrix_mul(10)
