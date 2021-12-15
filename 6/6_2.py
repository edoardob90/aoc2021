import sys
from collections import defaultdict

input_ = [int(x) for x in sys.stdin.readline().strip().split(',')]

init = defaultdict(int)
for x in input_:
    if x not in init:
        init[x] = 0
    init[x] += 1

try:
    days = int(sys.argv[1])
except IndexError:
    days = 80

# outfile = open('evolution_fast.txt', 'w')

for day in range(days):
    # using a defaultdict so that we have a int(0) value for non-existent keys
    fishes = defaultdict(int)
    for k, count in init.items():
        if k == 0:
            fishes[6] += count
            fishes[8] += count
        else:
            fishes[k-1] += count
    init = fishes
    # outfile.write(f"{day} {sum(Y.values())}\n")

print(sum(fishes.values()))
