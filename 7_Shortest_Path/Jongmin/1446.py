N,D=map(int,input().split())
dp=[i for i in range(10001)]
road=[[] for i in range(10001)]
for i in range(N):
    s,d,c=map(int,input().split())
    road[s].append([d,c])

for i in range(D+1):
    if(i!=0):
        dp[i]=min(dp[i],dp[i-1]+1)
    for d,c in road[i]:
        if(d<=D and dp[d]>dp[i]+c):
            dp[d]=dp[i]+c
print(dp[D])