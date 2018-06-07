"""
1. The problem with lists
2. Hello Generators
3. Generator Iteration
4. itertools: islice, takewhile
5. Generator Comprehension
"""


def fib(n):
    result = [1, 1]
    for i in range(n - 2):
        result.append(result[-1] + result[-2])

    return result


# prints: [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
print(fib(10))
