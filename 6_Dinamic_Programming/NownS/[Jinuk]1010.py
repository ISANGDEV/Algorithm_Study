T = int(input())

dp = [[0 for _ in range(30)] for _ in range(30)]


def comb(n, r, li):
    if li[n][r] == 0:
        if n == 0 or r == 0:
            return 1
        elif n < r:
            return 0
        elif n == r:
            return 1
        li[n][r] = comb(n-1, r-1, li) + comb(n-1, r, li)
    return li[n][r]


for _ in range(T):
    N, M = map(int, input().split())
    print(comb(M, N, dp))