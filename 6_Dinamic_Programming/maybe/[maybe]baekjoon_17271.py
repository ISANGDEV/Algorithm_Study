import operator as op
from functools import reduce


def combination_with_repetition(n, r):
    u = reduce(op.mul, range(n, n+r), 1)
    d = reduce(op.mul, range(1, r+1), 1)
    return u // d


n, m = map(int, input().split())
x = n // m
total = 0

for i in range(0, x + 1):
    if i * m == n:
        total += 1
        break
    total += combination_with_repetition(n - (i * m) + 1, i)

print(total % 1000000007)
