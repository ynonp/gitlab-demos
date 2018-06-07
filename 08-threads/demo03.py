import time
from threading import Thread, Lock

class Counter:
    def __init__(self, total):
        self.count = total
        self.lock = Lock()

    def take(self):
        with self.lock:
            x = self.count
            time.sleep(0)
            self.count = x - 1
        print(f"Remaining: {self.count}")

class Consumer(Thread):
    def __init__(self, count, counter):
        super().__init__()
        self.count = count
        self.counter = counter

    def run(self):
        for i in range(self.count):
            self.counter.take()
            self.count -= 1

c = Counter(100)
consumers = []
for i in range(10):
    consumers.append(Consumer(10, c))
    consumers[-1].start()

[t.join() for t in consumers]
print(c.count)