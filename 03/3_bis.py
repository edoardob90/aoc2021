import fileinput
from functools import partial

### Part 1

def transpose(_list):
    return [list(i) for i in zip(*_list)]

# a partial function to sort a list of lists by the last element
sort = partial(sorted, key=lambda x: x[-1])

# tally the 0 and 1 in a list representing the digits of a binary number
def count_zero_one(num):
    return [[i, num.count(i)] for i in (0,1)]

# convert from binary to decimal a list of digits
def bin_to_dec(digits):
    return sum([i * 2**(len(digits) - 1 - j) for j, i in enumerate(digits)])

### Part 2

# a function to select 5-bit numbers that have a given bit value in the same bit
def select_number(number, bit_pos, bit_value, max_bits=5):
    assert isinstance(number, list), "Number must be a list"
    assert bit_pos < max_bits, f"Bit position cannot be > {max_bits}"
    return True if number[bit_pos] == bit_value else False

if __name__ == "__main__":
    # read the input
    numbers = []
    for line in fileinput.input():
        numbers.append([int(x) for x in line.strip()])

    # solve Part 1
    def solve_p1():

        numbers_T = transpose(numbers) # transpose the list

        counts = list(map(count_zero_one, numbers_T)) # tally the numbers of 1 and 0 in each "column"

        # sort each element of the list by it's last number
        sorted_counts = list(map(sort, counts))

        # every element of `sorted_counts` is a list of lists of lists. We only need to consider the third level of `sorted_counts`. Example:
        # [ <--- 1st level
        #   [ <--- 2nd level
        #     [0, 5], [1, 7] <--- 3rd level
        #   ],
        #   [[0, 7], [1, 5]],
        #   [[0, 4], [1, 8]],
        #   [[0, 5], [1, 7]],
        #   [[0, 7], [1, 5]]
        # ]
        # for each element at the third level we need to take only the first element o
        epsilon_and_gamma = list(map(bin_to_dec, [list(i) for i in zip(*[(x[0][0], x[1][0]) for x in sorted_counts])]))

        print("[epsilon, gamma] = ", epsilon_and_gamma)
        print(f'gamma * epsilon = {(lambda x, y: x*y)(*epsilon_and_gamma)}')

    # Solve part 2
    def solve_p2():
        # size of our numbers
        num_bits = len(numbers[0])

        most_common = lambda num: 1 if num.count(1) >= num.count(0) else 0 # oxygen rating
        least_common = lambda num: 0 if num.count(1) >= num.count(0) else 1 # co2 rating
        
        def calc_rating_number(numbers, filter_func, debug=False):
            bit_counter = 0
            while len(numbers) > 1:
                numbers_T = transpose(numbers)
                selector = partial(select_number,
                            bit_pos=bit_counter,
                            bit_value=filter_func(numbers_T[bit_counter]),
                            max_bits=num_bits)
                numbers = list(filter(selector, numbers))
                if debug:
                    print(f"counter {bit_counter}: {numbers}")
                bit_counter += 1
            
            return bin_to_dec(numbers[0])

        o_rating = calc_rating_number(numbers, most_common)
        c_rating = calc_rating_number(numbers, least_common)

        print(f"life support rating = {o_rating * c_rating}")
    
    solve_p1()
    solve_p2()