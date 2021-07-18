import itertools
from collections import deque

n, m = map(int, input().rstrip().split())
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# BFS 함수 정의
def bfs(visited, start_x, start_y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([(start_x, start_y)])
    # 현재 노드를 방문 처리
    visited[start_x][start_y] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        # 상 하 좌 우 확인 후 추가
        for i in range(4):
            # 범위 오류
            next_x, next_y = v[0] + dx[i], v[1] + dy[i]
            if next_x >= n or next_x < 0 or next_y >= m or next_y < 0:
                continue
            # 벽에 막힘
            # print(visited[next_x][next_y])
            if visited[next_x][next_y]:
                continue
            else:
                queue.append((next_x, next_y))
                visited[next_x][next_y] = True


map_arr = [0] * n
for i in range(n):
    map_arr[i] = list(map(int, input().rstrip().split()))

pos = []
for i in range(n):
    for j in range(m):
        pos.append((i, j))
wall_cases = list(itertools.combinations(pos, 3))

big = 0
for x, y, z in wall_cases:

    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if map_arr[i][j] == 1:
                visited[i][j] = True
            # 코드 수정
            if map_arr[i][j] == 2:
                visited[i][j] = True

    if visited[x[0]][x[1]] or visited[y[0]][y[1]] or visited[z[0]][z[1]]:
        continue

    visited[x[0]][x[1]] = True
    visited[y[0]][y[1]] = True
    visited[z[0]][z[1]] = True

    for i in range(n):
        for j in range(m):
            if map_arr[i][j] == 2:
                bfs(visited, i, j)

    # 0 count
    count = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                count += 1

    big = max(big, count)
    # remove wall
print(big)

