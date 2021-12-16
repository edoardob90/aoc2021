import fileinput

h_pos = 0
depth = 0
aim = 0

for i, line in enumerate(fileinput.input()):
    x = int(line.split()[-1])
    if line.startswith('forward'):
        h_pos += x
        depth += aim * x
    elif line.startswith('down'):
        aim += x
    elif line.startswith('up'):
        aim -= x
    print(f'{line.strip()}: pos= {h_pos}, aim= {aim}, depth= {depth}')

print(f'Final horizontal position: {h_pos}\nFinal depth: {depth}\nResult: {h_pos*depth}')
