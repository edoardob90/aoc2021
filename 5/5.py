import fileinput

points = []
grid = [[0 for _ in range(1000)] for _ in range(1000)]

for line in fileinput.input():
    (x_0, y_0), (x_1, y_1) = [[int(y) for y in x.split(',')]
                              for x in line.strip().split(' -> ')]
    #print(x_0, y_0, x_1, y_1)
    if x_0 == x_1:  # vertical line
        if y_1 < y_0:
            y_0, y_1 = y_1, y_0
        for y in range(y_0, y_1 + 1):
            grid[x_0][y] += 1
    elif y_0 == y_1:  # horizontal line
        if x_1 < x_0:
            x_0, x_1 = x_1, x_0
        for x in range(x_0, x_1 + 1):
            grid[x][y_0] += 1
    else:  # diagonal line
        # Part 2
        if x_1 < x_0:
            x_0, x_1 = x_1, x_0
            y_0, y_1 = y_1, y_0
        if y_1 < y_0:
          for idx in range(x_1 - x_0 + 1):
            grid[x_0 + idx][y_0 - idx] += 1
        else:
          for idx in range(x_1 - x_0 + 1):
              grid[x_0 + idx][y_0 + idx] += 1

#print(*list(zip(*grid)), sep="\n", end="\n")

unroll = []
for r in grid:
    unroll.extend(r)

print(len(list(filter(lambda x: x >= 2, [_ for _ in unroll]))))