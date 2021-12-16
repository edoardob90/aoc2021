import fileinput

depths = [int(line.strip()) for line in fileinput.input()]

def moving_map(func, data, size=1):
    """Applies `func` over a window of size `size` in the specified `data`"""
    assert size > 0 and size < len(data), "Invalid window size"
    M = len(data) - size - 1
    new_data = [data[i:i - M] for i in range(M)] + [data[M:]]
    return list(map(func, new_data))

subtract = lambda x: x[-1] - x[0]

# Part 1
print("Part 1")
print(len(list(filter(lambda x: x > 0, moving_map(subtract, depths, 1)))))

# Part 2
print("Part 2")
three_sized_window = moving_map(subtract, moving_map(sum, depths, size=2), 1)
print(len(list(filter(lambda x: x > 0, three_sized_window))))
