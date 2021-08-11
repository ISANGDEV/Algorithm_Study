# LIS  
N = int(input())
INPUT = list(map(int, input().split()))
# 오름차순?으로 바꿈 
INPUT.reverse()

dp = [1]*(N)
# 4 2 5 8 4 11 15 
for i in range(N): 
    for j in range(i):          
        if INPUT[j] < INPUT[i]: 
            dp[i] = max(dp[i], dp[j] + 1)
print(N - max(dp))  # 마지막에 있는 숫자가 최대가 아님 



