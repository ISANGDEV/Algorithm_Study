N,T=map(int, input().split())
dp=[[0]*(T+1) for i in range(N+1)]
kt=[]
st=[]
for i in range(N):
    K,S=map(int, input().split())
    kt.append(K)
    st.append(S)
for i in range(N+1):
    for w in range(T+1):
        if(i==0 or w==0):
            dp[i][w]=0
        elif kt[i-1]<=w:
            dp[i][w]=max(st[i-1]+dp[i-1][w-kt[i-1]],dp[i-1][w])
        else:
            dp[i][w]=dp[i-1][w]
print(dp[N][T])