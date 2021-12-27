"""AoC 7, 2021: 07"""

# Standard library imports
import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [int(x) for x in puzzle_input.split(',')]


def part1(data):
    """Solve part 1"""
    _max = max(data)
    fuel = []
    for x in range(1, _max+1):
        fuel.append(sum([abs(y-x) for y in data]))
    return min(fuel)


def part2(data):
    """Solve part 2"""
    def sum_fuel(x):
        return x * (x+1) // 2
    _max = max(data)
    fuel = []
    for x in range(1, _max+1):
        fuel.append(sum([sum_fuel(abs(y-x)) for y in data]))
    return min(fuel)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
