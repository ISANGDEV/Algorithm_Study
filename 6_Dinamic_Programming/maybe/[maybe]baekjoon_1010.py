import operator as op
from functools import reduce


def combination(n, r):
    u = reduce(op.mul, range(n, n-r, -1), 1)
    d = reduce(op.mul, range(r, 0, -1), 1)
    return u // d


t = int(input())
result = []
for i in range(t):
    n, m = map(int, input().split())
    result.append(combination(m, n))

for i in range(len(result)):
    print(result[i])


'''
def bridge(west, east):
    if west == east:
        return 1
    if west == 1:
        return east
    total = 0
    for j in range(west - 1, east):
        total += bridge(west - 1, j)
    return total


t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    print(bridge(n, m))
'''
