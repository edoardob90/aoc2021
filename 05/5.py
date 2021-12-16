import fileinput
import sys

def solve(p2=False):
    
    grid = [[0 for _ in range(1000)] for _ in range(1000)]

    for line in fileinput.input():
        (x_0, y_0), (x_1, y_1) = [[int(y) for y in x.split(',')]
                                for x in line.strip().split(' -> ')]

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
            if p2:
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

    unroll = []
    for r in grid:
        unroll.extend(r)

    print("Number of points to avoid: {:d}".format(len(list(filter(lambda x: x >= 2, [_ for _ in unroll])))))

    sys.stdin.seek(0) # rewind the file descriptor

if __name__ == "__main__":
    print("Part 1")
    solve()
    print("Part 2")
    solve(p2=True)