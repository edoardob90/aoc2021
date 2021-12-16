import fileinput

depths = [int(line.strip()) for line in fileinput.input()]

increased = 0
for i, j in zip(depths[:-1], depths[1:]):
    if j - i > 0:
        increased += 1

print(f"Depth increased {increased} times")

