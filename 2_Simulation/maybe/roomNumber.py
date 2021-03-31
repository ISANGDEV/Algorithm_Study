from math import ceil


def min_sets(num):
    count = {}
    for i in range(10):
        count[i] = num.count(str(i))
    a = ceil((count[6] + count[9]) / 2)
    del count[6]
    del count[9]
    return max(list(count.values()) + [a])


room_num = input('')
print(min_sets(room_num))
