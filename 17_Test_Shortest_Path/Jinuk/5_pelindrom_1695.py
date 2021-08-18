n = int(input())
numbers = list(map(int, input().split()))
reverse = list(reversed(numbers))

dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(n+1):
        if i==0 or j==0:
            dp[i][j] = 0
        elif numbers[i-1] == reverse[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(n-dp[n][n])