import fileinput

for line in fileinput.input('shells', inplace=True):
    if line.startswith('#'): continue
    if len(line) == 1: continue
    print(line)