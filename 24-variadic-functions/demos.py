"""
1. Positional Arguments
2. Keyword Arguments
3. Reading parameters to array
4. Reading parameters to dictionary
5. Passing array as arguments
6. Passing dictionary as arguments
"""

def twice(x, y, z):
    return (x + y + z) * 2

def two_x_plus_y(x, y):
    return 2 * x + y

def longer_than(minlen, *words):
    return [w for w in words if len(w) > minlen]

def sum_weights(sentence, **weights):
    return sum([weights.get(w, 0) for w in sentence.split()])



print(two_x_plus_y(x=2, y=3))
print(longer_than(4, 'hello world', 'a', 'b', 'test'))

print(sum_weights('I can can can see a tree', I=20, can=30))

words = ['hello world', 'a', 'b', 'test']
print(longer_than(4, *words))

data = { 'd': 10, 'c': 20 }
print("I have {d} dollars and {c} cents".format(**data))