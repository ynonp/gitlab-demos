import math
from multiprocessing import Process, Lock, Value

def is_prime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def find_primes(start, offset, end, lock, counter):
    for i in range(start, end, offset):
        if is_prime(i):
            with lock:
                counter.value += 1

counter = Value('i', 0)
lock = Lock()
# workers = [Process(target=find_primes, args=(2, 1, 1_000_000, lock, counter))]

workers = [
Process(target=find_primes, args=(2, 4, 1_000_000, lock, counter)),
Process(target=find_primes, args=(3, 4, 1_000_000, lock, counter)),
Process(target=find_primes, args=(5, 4, 1_000_000, lock, counter)),
        ]

[w.start() for w in workers]
[w.join() for w in workers]
print(counter.value)
