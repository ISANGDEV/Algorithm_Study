N=int(input())
leftCard=list(map(int,input().split()))
rightCard=list(map(int,input().split()))
dp=[[0]*(N+1) for i in range(N+1)]
for i in range(N-1,-1,-1):
    for j in range(N-1,-1,-1): #차례로가면 모든 상황을 고려하기 어려움, 최종 결과부터 거꾸로 가기
        if(rightCard[j]<leftCard[i]):
            dp[i][j]=max(dp[i][j+1]+rightCard[j],dp[i+1][j],dp[i+1][j+1]) #오른쪽카드를 버리고 점수를 얻었을 때, 왼쪽카드 버렸을 때, 둘다 버렸을 때 중 가장 큰 점수
        else:
            dp[i][j]=max(dp[i+1][j],dp[i+1][j+1]) #왼쪽카드 버렸을 때, 둘다 버렸을 때 중 가장 큰 점수
print(dp[0][0])