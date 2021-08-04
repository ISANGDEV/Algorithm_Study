N,M,H=map(int,input().split())
blocks=[[] for i in range(N+1)]
for i in range(N):
    blocks[i+1]=list(map(int,input().split()))
dp=[[0]*(N+1) for _ in range(H+1)]
for j in range(N+1):
    dp[0][j]=1
for i in range(1,H+1):
    for j in range(1,N+1):
        for block in blocks[j]:
            if(i-block>=0):
                dp[i][j]+=dp[i-block][j-1]
        dp[i][j]+=dp[i][j-1]
print(dp[-1][-1]%10007)