L1=input()
L2=input()
dp=[[0]*(len(L2)+1) for i in range(len(L1)+1)]
result=0
for i in range(len(L1)):
    for j in range(len(L2)):
        if(L1[i]==L2[j]):
            dp[i+1][j+1]=dp[i][j]+1
        else:
            dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
print(dp[len(L1)][len(L2)])