class NoDucks(type):
    def __init__(cls, name, parents, props):
        super().__init__(name, parents, props)
        if 'quack' in props:
            raise Exception("No Ducks Allowed")

class MyBase(metaclass=NoDucks):
    pass

class A(MyBase):
    def run(self):
        pass


class B(MyBase):
    def quack(self):
        pass


