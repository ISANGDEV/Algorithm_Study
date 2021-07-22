T=int(input())
for _ in range(T):
    N=int(input())
    coins=list(map(int,input().split()))
    K=int(input())
    dp=[0]*(K+1)
    dp[0]=1
    for c in coins:
        for i in range(1,K+1):
            if(i-c>=0):
                dp[i]+=dp[i-c]
    print(dp[K])