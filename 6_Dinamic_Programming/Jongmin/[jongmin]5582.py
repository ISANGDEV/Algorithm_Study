s1=input()
s2=input()
l1=len(s1)
l2=len(s2)

dp=[[0]*(l1+1) for i in range(l2+1)]
answer=0
for j in range(1,l1+1):
    for i in range(1,l2+1):
        if(s1[j-1]==s2[i-1]):
            temp=dp[i-1][j-1]+1
            dp[i][j]=temp
            answer=max(answer,temp)
print(answer)