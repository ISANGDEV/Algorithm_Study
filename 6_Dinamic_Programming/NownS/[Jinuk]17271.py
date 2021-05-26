N, M = map(int, input().split())

dp = [[0 for _ in range(100001)] for _ in range(101)]


def skill(n, m, table):
    if n < m:
        return 1
    if table[m][n] == 0:
        table[m][n] = skill(n-m, m, table) + skill(n-1, m, table)
    return table[m][n]


print(skill(N, M, dp) % 1000000007)