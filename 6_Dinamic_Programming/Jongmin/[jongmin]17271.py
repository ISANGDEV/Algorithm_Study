N,M=map(int,input().split())
DIV=1000000007
dp=[1]*(N+1)
if(N>=M):
    dp[M]=2
    for i in range(M+1,N+1):
        dp[i]=(dp[i-1]+dp[i-M])
    print(dp[N]%DIV)
else:
    print(1)