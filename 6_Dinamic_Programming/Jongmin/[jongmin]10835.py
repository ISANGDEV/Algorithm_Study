N=int(input())
leftCard=list(map(int,input().split()))
rightCard=list(map(int,input().split()))
dp=[[0]*(N+1) for i in range(N+1)]
for i in range(N-1,-1,-1):
    for j in range(N-1,-1,-1):
        if(rightCard[j]<leftCard[i]):
            dp[i][j]=max(dp[i][j+1]+rightCard[j],dp[i+1][j],dp[i+1][j+1])
        else:
            dp[i][j]=max(dp[i+1][j],dp[i+1][j+1])
print(dp[0][0])