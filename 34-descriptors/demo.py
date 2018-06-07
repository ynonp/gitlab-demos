"""
1. Hello Descriptors - structure and simple demo
2. APIField descriptor
3. ReadOnlyField descriptor
"""

class HelloDescriptor:
    def __init__(self):
        pass

    def __get__(self, obj, type=None):
        return "Hello World!"

    # def __set__(self, obj, value):
    #     pass
    #
    # def __delete__(self, obj):
    #     pass

class Person:
    name = HelloDescriptor()

p = Person()
print(p.name)

