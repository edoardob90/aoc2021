import fileinput

depths = [int(line.strip()) for line in fileinput.input()]

def moving_map(func, data, size):
    """Applies `func` over a window of size `size` in the specified `data`"""
    new_data = [data[i:i-size] for i in range(size)] + [data[size:]]
    assert len(new_data) == size+1
    return list(map(func, zip(*new_data)))

def subtract(data):
    assert len(data) == 2
    return data[-1] - data[0]

# Part 1
print("Part 1")
print(len(list(filter(lambda x: x > 0, moving_map(subtract, depths, 1)))))

# Part 2
print("Part 2")
three_sized_window = moving_map(subtract, moving_map(sum, depths, size=2), 1)
print(len(list(filter(lambda x: x > 0, three_sized_window))))
