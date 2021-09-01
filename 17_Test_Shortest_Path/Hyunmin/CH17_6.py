import sys 
n, m = list(map(int, input().split()))
dp = [[0]*(m+1) for _ in range(n+1)]
result = sys.stdin.readline() 
answer = sys.stdin.readline()

for j in range(n+1): 
    dp[j][0] = j 
for i in range(m+1): 
    dp[0][i] = i

# 추가는 왼쪽, 삭제는 위쪽, 교체는 왼쪽위 대각선인데, i -> jl v-> w는 글자 비교할때 같은 것으로 간주 
for i in range(1, n+1): 
    for j in range(1, m+1):
        # 같을 때, 왼쪽위 대각선 
        if result[i-1] == answer[j-1]: 
            dp[i][j] = dp[i-1][j-1]
        # 비교를 효율적으로 해야함 
        elif result[i-1] == "i" or answer[j-1] == "v":
            if result[i-1] == "i" and (answer[j-1] == "j" or answer[j-1] == "l" or answer[j-1] == "l"): 
                # 같은 것으로 간주 
                dp[i][j] = dp[i-1][j-1]
            elif result[i-1] == "v" and answer[j-1] == "w": 
                # 같은 것으로 간주 
                dp[i][j] = dp[i-1][j-1]
        else: 
             
            dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
                


print(dp[n-1][m-1])
