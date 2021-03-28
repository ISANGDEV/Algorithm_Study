def big_num(lst, m, k):
    total, cnt = 0, 0
    lst = sorted(lst)
    for i in range(m):
        if cnt < k:
            total += lst[-1]
            cnt += 1
        else:
            total += lst[-2]
            cnt = 0
    return total


factors = list(map(int, input('').split(' ')))
num_list = list(map(int, input('').split(' ')))

print(big_num(num_list, factors[1], factors[2]))
