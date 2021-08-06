N=int(input())
forces=list(map(int,input().split()))
dp=[1]*(N+1)
for i in range(1, N):
    for j in range(i):
        if(forces[i]<forces[j]):
            dp[i]=max(dp[i],dp[j]+1)
print(N-max(dp))