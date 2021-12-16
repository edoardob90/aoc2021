import fileinput

h_pos = 0
depth = 0

for line in fileinput.input():
    x = int(line.split()[-1])
    if line.startswith('forward'):
        h_pos += x
    elif line.startswith('down'):
        depth += x
    elif line.startswith('up'):
        depth -= x

print(f'Final horizontal position: {h_pos}\nFinal depth: {depth}\nResult: {h_pos*depth}')
