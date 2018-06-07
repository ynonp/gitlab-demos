class ReadOnlyField:
    def __get__(self, obj, klass):
        return self.value

    def __set__(self, obj, val):
        if hasattr(self, 'value'):
            raise AttributeError(f"Can't modify a readonly field")
        self.value = val

class Person:
    name = ReadOnlyField()

    def __init__(self, name):
        self.name = name

p = Person('ynon')
print(p.name)

p.name = 'demo'