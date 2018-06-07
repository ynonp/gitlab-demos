import math
from multiprocessing import Process, Lock, Value, Pool

def is_prime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

pool = Pool()
data = range(2, 1_000_000)

results = pool.map(is_prime, data)
print(sum([1 for n in results if n is True]))
