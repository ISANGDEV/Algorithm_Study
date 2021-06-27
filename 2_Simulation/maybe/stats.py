def average(num):
    return int(round(sum(num) / len(num), 0))


def median(num):
    return sorted(num)[len(num)//2]


def mode(num):
    cnt = {}
    for i in list(set(num)):
        cnt[i] = num.count(i)
    a = list(filter(lambda x: cnt[x] == max(cnt.values()), cnt.keys()))
    if len(a) > 1:
        return sorted(a)[1]
    else:
        return sorted(a)[0]


def _range(num):
    return max(num) - min(num)


num_list = []
n = int(input(''))
for _ in range(n):
    num_list.append(int(input('')))

print(average(num_list))
print(median(num_list))
print(mode(num_list))
print(_range(num_list))



