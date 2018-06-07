"""
1. Hello Metaclasses
2. Enforcing structure with metaclasses
3. Building dynamic registry with metaclasses
"""

class MyMeta(type):
    def __init__(cls, name, parents, props):
        super().__init__(name, parents, props)
        print(cls)
        print(name)
        print(parents)
        print(props)

class Demo(metaclass=MyMeta):
    foo = 10

class Foo(Demo):
    pass
