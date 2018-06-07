"""
1. Python uses Reference count
2. __del__ is called when an object is deleted
3. circular reference, weakref / explicit close method
"""

import gc

def two():
    return [1, 2]

print(len(gc.get_objects()))
two()
print(len(gc.get_objects()))










