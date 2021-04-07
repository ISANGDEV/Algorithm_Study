from collections import deque
import copy


def dfs(maze, c, r, count):
    if 0 <= c < M and 0 <= r < N:
        if c == M-1 and r == N-1:
            count_list.append(count)
        if maze[c][r] == 1:
            maze[c][r] = 0
            dfs(maze, c + 1, r, count + 1)
            dfs(maze, c, r + 1, count + 1)
            dfs(maze, c - 1, r, count + 1)
            dfs(maze, c, r - 1, count + 1)
        else:
            return
    else:
        return


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if matrix_2[nx][ny] == 0:
                continue
            if matrix_2[nx][ny] == 1:
                matrix_2[nx][ny] = matrix_2[x][y] + 1
                queue.append((nx, ny))
    return matrix_2[M-1][N-1]


# 데이터 처리
M, N = map(int, input('').split())
matrix = []
for i in range(M):
    matrix.append(list(map(int, input(''))))

# dfs 실행
matrix_1 = copy.deepcopy(matrix)
count_list = []
dfs(matrix_1, 0, 0, 1)
print(min(count_list))

# bfs 실행
matrix_2 = copy.deepcopy(matrix)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
print(bfs(0, 0))
