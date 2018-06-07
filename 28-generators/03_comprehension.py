import itertools as it

def fib():
    x, y = 1, 1
    while True:
        yield x
        x, y = y, x + y

sqr_fib = (x * x for x in fib())

for val in it.islice(sqr_fib, 10):
    print(val)


