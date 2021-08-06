A=input()
B=input()
LA=len(A)
LB=len(B)
dp=[[0]*(LB+1) for _ in range(LA+1)]
for i in range(LA+1):
    dp[i][0]=i
for j in range(LB+1):
    dp[0][j]=j
for i in range(LA):
    for j in range(LB):
        if(A[i]==B[j]):
            dp[i+1][j+1]=dp[i][j]
        else:
            dp[i+1][j+1]=min(dp[i][j+1], dp[i+1][j], dp[i][j])+1
print(dp[-1][-1])