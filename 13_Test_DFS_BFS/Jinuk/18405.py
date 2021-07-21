from collections import deque

n, k = map(int, input().split())

virus_map = []
for _ in range(n):
    virus_map.append(list(map(int, input().split())))

s, x, y = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

start = []

for i in range(n):
    for j in range(n):
        if virus_map[i][j] != 0:
            start.append((virus_map[i][j], (i, j), 0))
q = deque(sorted(start))

while q:
    virus, x_y, time = q.popleft()
    if time == s:
        break
    for k in range(4):
        next_x = x_y[0] + dx[k]
        next_y = x_y[1] + dy[k]

        if 0 <= next_x < n and 0 <= next_y < n and virus_map[next_x][next_y] == 0:
            virus_map[next_x][next_y] = virus
            q.append((virus, (next_x, next_y), time + 1))

print(virus_map[x-1][y-1])