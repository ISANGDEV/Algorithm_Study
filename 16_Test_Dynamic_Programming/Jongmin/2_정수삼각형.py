n = int(input())
triangle = []
dx = [0, -1]
dy = [-1, -1]
for i in range(n):
    row = list(map(int, input().split()))
    triangle.append(row)
dp = [[0] * n for i in range(n)]
dp[0][0] = triangle[0][0]
for i in range(1, n):
    for j in range(i + 1):
        for k in range(len(dx)):
            nexty = i + dy[k]
            nextx = j + dx[k]
            dp[i][j] = max(triangle[i][j] + dp[nexty][nextx], dp[i][j])
print(max(dp[-1]))
