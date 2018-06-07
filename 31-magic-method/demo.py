"""
1. What are magic methods (python calls our methods)
2. Demos: str, ne, eq, hash
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point [{self.x}, {self.y}]'

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return NotImplemented

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(self.x) & hash(self.y)

p = Point(10, 20)
q = Point(10, 20)
print(p == q)
