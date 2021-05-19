T=int(input())
N=30
M=30
dp=[[0]*(31) for i in range(31)]
for i in range(1,M+1):
    dp[1][i]=i
for i in range(2,N+1):
    for j in range(1,M+1):
        for k in range(i-1,j):
            dp[i][j]+=dp[i-1][k]
for _ in range(T):
    N,M=map(int,input().split())
    print(dp[N][M])


