import fileinput
import sys

def bin_to_dec(digits):
    assert isinstance(digits, list)
    return sum([i * 2**(len(digits) - 1 - j) for j, i in enumerate(digits)])

N = []
for line in fileinput.input():
    line = line.strip()
    N.append(list(line))

# Part 1
def most_common(num):
    return 1 if num.count('1') >= num.count('0') else 0
def least_common(num):
    return 0 if num.count('1') >= num.count('0') else 1

epsilon = []
gamma = []
for c in zip(*N):
    epsilon.append(most_common(c))
    gamma.append(least_common(c))

result = [bin_to_dec(x) for x in (epsilon, gamma)]
print(result[0]*result[1])

# Part 2
num_bits = len(N[0])
ratings = 1
for crit in most_common, least_common:
    numbers = N # shallow copy, as we'll filter out numbers iteratively
    for bit_idx in range(num_bits):
        col = list(zip(*numbers))[bit_idx]
        bit_crit = str(crit(col))
        numbers = list(filter(lambda x: x[bit_idx] == bit_crit, numbers))
        if len(numbers) == 1:
            last = [int(x) for x in numbers[0]]
            break
    ratings *= bin_to_dec(last)

print(ratings)