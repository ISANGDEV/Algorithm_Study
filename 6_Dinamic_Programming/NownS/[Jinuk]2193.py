N = int(input())

dp = [1, 1] + [0 for _ in range(N-2)]


def pinary(n, li):
    if dp[n] == 0:
        dp[n] = pinary(n-1, li) + pinary(n-2, li)
    return dp[n]


print(pinary(N-1, dp))