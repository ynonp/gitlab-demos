import checkIsraelID

def fib(n):
    x, y = 1, 1
    for i in range(n):
        x, y = y, x + y
        print(x)

print(checkIsraelID.checkID('123456789'))

# fib(10)