import math
from threading import Thread, Lock

def is_prime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

class Counter:
    def __init__(self):
        self.value = 0
        self.lock = Lock()

    def inc(self):
        with self.lock:
            self.value += 1

class PrimesDetector(Thread):
    def __init__(self, start, offset, end, counter):
        super().__init__()
        self._start = start
        self._offset = offset
        self._end = end
        self._counter = counter

    def run(self):
        for i in range(self._start, self._end, self._offset):
            if is_prime(i):
                self._counter.inc()

counter = Counter()
# workers = [PrimesDetector(2, 1, 1_000_000, counter)]

workers = [
PrimesDetector(2, 4, 1_000_000, counter),
PrimesDetector(3, 4, 1_000_000, counter),
PrimesDetector(4, 4, 1_000_000, counter),
PrimesDetector(5, 4, 1_000_000, counter),
        ]

[w.start() for w in workers]
[w.join() for w in workers]
print(counter.value)
