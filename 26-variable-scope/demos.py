"""
1. Local (function) variables
2. Global (file) variables
3. non-local variables
4. Scope quiz
"""

x = 10
arr = [10, 20, 30, 40]

def foo():
    x = 20
    def bar():
        nonlocal x
        print(x)
        x += 1
    bar()

foo()
print(x)