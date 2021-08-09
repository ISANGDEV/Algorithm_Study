N = int(input())
arr = []
dp = [] 
for i in range(N): 
    arr.append(list(map(int, input().split())))
    dp.append([-1] * (i + 1)) 
result = dp[0][0] = arr[0][0]
for i in range(N-1): 
    for j in range(i+1):
        # 대각선 dp 값 = 현 dp 값 + 다음 arr 값  
        # left down 
        if dp[i+1][j] < arr[i+1][j] + dp[i][j]: 
            dp[i+1][j] = arr[i+1][j] + dp[i][j] 
        # right down 
        if dp[i+1][j+1] < arr[i+1][j+1] + dp[i][j]: 
            dp[i+1][j+1] = arr[i+1][j] + dp[i][j]

print(max(dp[N-1]))

