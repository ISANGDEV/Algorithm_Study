import sys
vec = [[-1,-1],[0,-1],[1,-1]]

# 첫번째 열의 아무 곳,  (0,1) (1,-1) (1,1)

t = int(sys.stdin.readline())

for i in range(t):
    n,m = map(int,sys.stdin.readline().split()) # n 세로 m 가로
    geo = [[0] * m for j in range(n)]
    temp = list(map(int,sys.stdin.readline().split()))
    for i in range(n*m):
        geo[ i //m][i%m] = temp[i]

    dp = [[0]*m for i in range(n)]

    for i in range(n):
        dp[i][0] = geo[i][0]

    for i in range(1,m): # 가로
        for j in range(n): # 세로
            for y,x in vec:
                ny = y + j
                nx = x + i
                if 0<= nx < m and 0 <= ny < n :
                    dp[j][i] = max(dp[j][i], dp[ny][nx] + geo[j][i])
    result = -1
    for i in range(n):
        result = max(result, dp[i][m - 1])
    print(result)

"""
    result = []

    for i in range(n):
        result.append(dp[i][m-1])

    print(max(result))

"""

