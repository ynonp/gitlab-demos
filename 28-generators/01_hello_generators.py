# Generator Function
def fib():
    x, y = 1, 1
    while True:
        yield x
        x, y = y, x + y

for index, val in enumerate(fib()):
    if val > 200:
        break
    if index >= 10:
        break
    print(val)
