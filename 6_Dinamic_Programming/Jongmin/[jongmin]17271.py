N,M=map(int,input().split())
DIV=1000000007
dp=[1]*(N+1)
if(N>=M):
    dp[M]=2 #M전까지는 전부다 AAA밖에안됨, M일때는 AAAAAA혹은 B 이렇게 두가지 가능
    for i in range(M+1,N+1): #M이후로는 dp 적용
        dp[i]=(dp[i-1]+dp[i-M]) #i-1 경우에 맨 뒤에 A만 붙이는 경우 + i-M 경우에 맨 뒤에 B만 붙이는 경우
    print(dp[N]%DIV)
else:
    print(1)