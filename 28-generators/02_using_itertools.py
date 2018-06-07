import itertools as it
def fib():
    x, y = 1, 1
    while True:
        yield x
        x, y = y, x + y

for val in it.islice(fib(), 10):
    print(val)

for val in it.takewhile(lambda x: x < 200, fib()):
    print(val)
    