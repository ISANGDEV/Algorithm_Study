T=int(input())
N=30
M=30
dp=[[0]*(31) for i in range(31)] #한번에 30개 미리 다 만들어놓기. 매번만들 필요 x
for i in range(1,M+1):
    dp[1][i]=i #서쪽에 다리 한개, 동쪽에 i개면 i개만큼 가능
for i in range(2,N+1):
    for j in range(1,M+1):
        for k in range(i-1,j):
            dp[i][j]+=dp[i-1][k] #서쪽에 다리 i개, 동쪽에 다리 j개면 i번째-i번째 이었을때 경우, i번째-i+1 이었을때 ,,, i번째-j번째 이었을때 경우까지 다 더함
for _ in range(T):
    N,M=map(int,input().split())
    print(dp[N][M])


