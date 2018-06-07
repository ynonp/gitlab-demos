import time
from threading import Thread

class Task(Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        x = 10
        time.sleep(2)
        print(x)

t = Task()
t.start()

p = Task()
p.start()

#p.join()
#t.join()
print("--- the end")
