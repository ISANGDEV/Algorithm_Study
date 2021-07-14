from collections import deque

n = int(input())
k = int(input())
dummy_map = [[0] * n for _ in range(n)]
dummy_map[0][0] = 2
for _ in range(k):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    dummy_map[a][b] = 1
l = int(input())
direction_change = []
for _ in range(l):
    a, b = input().split()
    direction_change.append((int(a), b))
direction = 0
dx_dy = [(0, 1), (-1, 0), (0, -1), (1, 0)]
q = deque()
now = (0,0)
q.appendleft(now)
time = 0
l_idx = 0
while True:
    time += 1

    x, y = now[0] + dx_dy[direction][0], now[1] + dx_dy[direction][1]
    now = (x, y)
    q.appendleft(now)
    if x >= n or x < 0 or y >= n or y < 0:
        break
    if dummy_map[x][y] == 2:
        break
    if dummy_map[x][y] == 0:
        a, b = q.pop()
        dummy_map[a][b] = 0
    dummy_map[x][y] = 2

    if len(direction_change) > l_idx and time == direction_change[l_idx][0]:
        if direction_change[l_idx][1] == "L":
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4
        l_idx += 1

print(time)