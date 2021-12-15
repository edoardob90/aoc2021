import sys
from collections import defaultdict

input_ = [int(x) for x in sys.stdin.readline().strip().split(',')]

X = defaultdict(int)
print(X)
for x in input_:
    if x not in X:
        X[x] = 0
    X[x] += 1

print(X)

try:
    days = int(sys.argv[1])
except IndexError:
    days = 80

for _ in range(days):
    Y = defaultdict(int)
    for k, count in X.items():
        if k == 0:
            Y[6] += count
            Y[8] += count
        else:
            Y[k-1] += count
    X = Y

print(sum(Y.values()))
