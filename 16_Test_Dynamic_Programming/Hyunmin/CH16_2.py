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


