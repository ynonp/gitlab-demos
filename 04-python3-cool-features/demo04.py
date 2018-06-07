from pathlib import Path
from collections import defaultdict

dirs = defaultdict(int)

for fname in Path('.').glob('**/*.pl'):
    directory = fname.resolve().parents[0]
    dirs[str(directory)] += 1

print(dirs)
