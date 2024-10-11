import math
test_data = [1, 3, 3, 5, 6, 6, 6, 1, 2, 3, 4, 5, 3, 20, 30, 64, 6, 7, 8, 9]
def get_mean(data: list):
    total = sum(data)
    mean = total / len(data)
    print("Total:", total, "Length:", len(data))
    return mean
get_mean(test_data)
def get_median(data: list):
    #bubble-sort
    final_index = len(data)-1
    for x in range(final_index, 0, -1):
        for y in range(x):
            if data[y] > data[y+1]:
                data[y], data[y+1] = data[y+1], data[y]
    median = 0
    if len(data) % 2 == 0:
        n1 = int(final_index / 2)
        n2 = int(n1 + 1)
        median = (data[n1] + data[n2]) / 2
    else:
        n1 = int(final_index / 2)
        median = data[n1]
    return median

def get_mode(data: list):
    map = {}
    for i in data:
        if f"{i}" not in map:
            map.update({f"{i}": 1})
        else:
            val = map.get(f"{i}")
            val += 1
            map.update({f"{i}": val})
    mode = max(map, key=map.get)
    return mode

def get_standard_deviation(data: list):
    mean = get_mean(data)
    print(mean)
    n_data = data
    total = 0
    for i in range(len(n_data) - 1):
        n_data[i] = n_data[i] - mean
        n_data[i] = n_data[i] * n_data[i]
        total += n_data[i]
    variance = total / len(n_data)
    print(variance)
    sd = math.sqrt(variance)
    return sd
print(test_data)
print(get_standard_deviation(test_data))