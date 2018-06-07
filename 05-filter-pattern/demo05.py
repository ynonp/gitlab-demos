import fileinput
from collections import defaultdict

def key(word):
    return tuple(sorted(word))

res = defaultdict(list)

for word in fileinput.input('words'):
    sortedword = key(word.strip())
    res[sortedword].append(word)

print(res)



