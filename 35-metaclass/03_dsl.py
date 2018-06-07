import fileinput
from collections import defaultdict

class Registry(type):
    registers = defaultdict(int)
    handlers = {}

    def __init__(cls, name, parents, props):
        super().__init__(name, parents, props)
        if hasattr(cls, '__cmd__'):
            Registry.handlers[cls.__cmd__] = cls

    @classmethod
    def create(cls, name):
        return Registry.handlers[name](Registry.registers)

class Handler(metaclass=Registry):
    def __init__(self, registers):
        self.registers = registers

class AddHandler(Handler):
    __cmd__ = 'add'
    def run(self, reg, val):
        self.registers[reg] += int(val)

class SubstractHandler(Handler):
    __cmd__ = 'sub'
    def run(self, reg, val):
        self.registers[reg] -= int(val)

class PrintHandler(Handler):
    __cmd__ = 'print'
    def run(self, reg):
        print(self.registers[reg])

for line in fileinput.input('calc.txt'):
    cmd, *args = line.strip().split()
    handler = Registry.create(cmd)
    handler.run(*args)
