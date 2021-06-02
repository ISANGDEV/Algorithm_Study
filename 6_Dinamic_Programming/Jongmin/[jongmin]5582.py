s1=input()
s2=input()
l1=len(s1)
l2=len(s2)

dp=[[0]*(l1+1) for i in range(l2+1)]
answer=0
for j in range(1,l1+1):
    for i in range(1,l2+1):
        if(s1[j-1]==s2[i-1]): #같다면
            temp=dp[i-1][j-1]+1 #이전꺼까지의 연속된 길이+1 만약에 중간에 끊겼다면 0부터 다시 시작
            dp[i][j]=temp
            answer=max(answer,temp) #지속적으로 최대값 업데이트
print(answer)