"""
Python Lambda Expressions
1. Defining lambdas
2. Calling lambdas
3. Lambda use cases
"""

f = lambda x: x * 2
print(f(4))

# g = lambda a: a[0] = 10
# arr = [1, 2,3]
# g(arr)


print(list(filter(lambda x: x > 10, range(20))))

# [lambda x: 10, lambda x: 20]