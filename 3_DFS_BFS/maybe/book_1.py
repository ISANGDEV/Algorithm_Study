def dfs(matrix, c, r):
    if 0 <= c < M and 0 <= r < N:
        if matrix[c][r] == 0:
            matrix[c][r] = 1
            dfs(matrix, c + 1, r)
            dfs(matrix, c - 1, r)
            dfs(matrix, c, r + 1)
            dfs(matrix, c, r - 1)
        else:
            return
    else:
        return


M, N = map(int, input('').split())
matrix = []
for i in range(M):
    matrix.append(list(map(int, input(''))))

count = 0
for i in range(M):
    for j in range(N):
        if matrix[i][j] == 0:
            dfs(matrix, i, j)
            count += 1

print(count)




