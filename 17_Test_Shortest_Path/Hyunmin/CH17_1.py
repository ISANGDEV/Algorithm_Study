N = int(input())
M = int(input())
INF = int(1e9)
dp = [[INF]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    # dp[a][b] = min(dp[a][b], c) 매번 삽입까지 하게돼서 시간초과 발생 
    if c < dp[a][b]: 
        dp[a][b] = c 

for i in range(N+1):
    dp[i][i] = 0

for mid in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            dp[a][b] = min(dp[a][b], dp[a][mid] + dp[mid][b])

for i in range(1, N+1):
    for j in range(1, N+1):
        print(dp[i][j], end=" ") if dp[i][j] != INF else print(0, end=" ")
    print()

