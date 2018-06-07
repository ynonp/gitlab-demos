class ByeBye:
    def __del__(self):
        print('bye bye')

def two():
    b = ByeBye()

two()
print('--- The end')