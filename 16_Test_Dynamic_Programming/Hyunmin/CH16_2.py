N = int(input())
dp = [] 
for _ in range(N): 
    dp.append(list(map(int, input().split())))

for i in range(1, N): 
    for j in range(i+1): 
        left_up = right_up = -1 
        # left up 
        if j == 0: 
            # dont have right up 
            pass 
        else: 
            left_up = dp[i][j] + dp[i-1][j-1] 
        # right up 
        if j == i: 
            # dont have right up 
            pass 
        else: 
            right_up = dp[i][j] + dp[i-1][j]
        dp[i][j] = max(left_up, right_up)

print(max(dp[N-1]))




# dp[i][j] 일때 dp[i][j]의 대각선 아래와 대각선 오른쪽을 체워 넣는 방식 -> 틀렸습니다.
#N = int(input())
#arr = []
#dp = [] 
#for i in range(N): 
#    arr.append(list(map(int, input().split())))
#    dp.append([-1] * (i + 1)) 
#result = dp[0][0] = arr[0][0]
#for i in range(N-1): 
#    for j in range(i+1):
#        # 대각선 dp 값 = 현 dp 값 + 다음 arr 값  
#        # left down 
#        if dp[i+1][j] < arr[i+1][j] + dp[i][j]: 
#            dp[i+1][j] = arr[i+1][j] + dp[i][j] 
#        # right down 
#        if dp[i+1][j+1] < arr[i+1][j+1] + dp[i][j]: 
#            dp[i+1][j+1] = arr[i+1][j] + dp[i][j]
#
#print(max(dp[N-1]))

