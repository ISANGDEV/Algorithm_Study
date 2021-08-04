T=int(input())
for _ in range(T):
    n,m=map(int,input().split())
    dp=[[0]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        dp[i][1]=i
    for j in range(2,m+1):
        for i in range(2, n + 1):
            dp[j][i]+=dp[j//2][i-1]
            dp[j][i]+=dp[j-1][i]
    print(dp[m][n])
