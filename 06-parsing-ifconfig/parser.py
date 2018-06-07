import fileinput
import re

fields = {
    'block_name': re.compile(r'^(?P<block_name>[a-z0-9]+):'),
    'inet': re.compile(r'inet (?P<inet>\d+\.\d+\.\d+\.\d+)'),
    'status': re.compile(r'status: (?P<status>\w+)'),

}
# 
current_block = None
blocks = []

for line in fileinput.input('ifconfig.txt'):

    m = fields['block_name'].search(line)
    if m is not None:
        if current_block is not None:
            blocks.append(current_block)
        current_block = {}

    for name, pat in fields.items():
        m = pat.search(line)
        if m is not None:
            current_block[name] = m.group(name)


print(blocks)