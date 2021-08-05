T = int(input())
dx = [-1, -1, -1]
dy = [-1, 0, 1]
for _ in range(T):
    n, m = map(int, input().split())
    golds = [[0] * m for i in range(n)]
    goldinput = list(map(int, input().split()))
    for i in range(n * m):
        golds[i // m][i % m] = goldinput[i]
    dp = [[0] * m for i in range(n)]
    for i in range(n):
        dp[i][0] = golds[i][0]
    for i in range(1, m):  # 가로
        for j in range(n):  # 세로
            for k in range(len(dx)):
                nexty = j + dy[k]
                nextx = i + dx[k]
                if (0 <= nexty < n and 0 <= nextx < m):
                    dp[j][i] = max(dp[j][i], dp[nexty][nextx] + golds[j][i])
    result=-1
    for i in range(n):
        result=max(result,dp[i][m-1])
    print(result)