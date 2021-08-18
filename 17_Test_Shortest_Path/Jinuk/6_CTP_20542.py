n, m = map(int, input().split())

str1 = input()
str2 = input()

dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][0] = i
for i in range(1, m+1):
    dp[0][i] = i

for i in range(1, n+1):
    for j in range(1, m+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1]
        elif str1[i-1] == 'v' and str2[j-1] == 'w':
            dp[i][j] = dp[i-1][j-1]
        elif str1[i-1] == 'i' and (str2[j-1] == 'j' or str2[j-1] == 'l'):
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j]) + 1

print(dp[n][m])

