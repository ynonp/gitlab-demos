"""
1. Normal dictionary based objects
2. compact objects
"""

class Point:
    __slots__ = ['x', 'y']

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
p.z = 10

print(p.z)











