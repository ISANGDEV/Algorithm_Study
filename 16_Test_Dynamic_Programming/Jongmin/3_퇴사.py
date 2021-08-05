N=int(input())
counsels=[]
for i in range(N):
    counsels.append(list(map(int,input().split())))
dp=[0]*(N+1)
for i in range(N+1):
    for j in range(i):
        time, point=counsels[j]
        if(i-time>=j):
            dp[i]=max(dp[i],dp[j]+point)
print(max(dp))
#dp[i]는 i전까지 최대값. 이렇게 해놓으면 dp[i]에다가 point[i]더하면 선택가능한 선에서 i를 선택했을때 최댓값구할 수 있음