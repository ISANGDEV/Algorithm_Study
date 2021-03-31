import sys

N, M, x, y, K = map(int, sys.stdin.readline().split())

my_map = []
for i in range(N):
    tmp = map(int, sys.stdin.readline().split())
    tmp = list(tmp)
    my_map.append(tmp)

command = list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))

dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)
dice = [0 for i in range(7)]

idx_x = x
idx_y = y
dice_index = 0

for i in command:
    idx_x += dx[i]
    idx_y += dy[i]
    if idx_x == -1 or  idx_y == -1 or  idx_x == len(my_map) or idx_y == len(my_map[0]):
        idx_x -= dx[i]
        idx_y -= dy[i]
        continue

# ???? 여기 알고리즘을 어떻게 해야할지 모르겠다, 아얘 잘못한건가

    if my_map[idx_x][idx_y] == 0:
        my_map[idx_x][idx_y] = dice[dice_index]
    else:
        dice[dice_index] = my_map[idx_x][idx_y]
        my_map[idx_x][idx_y] = 0

    print(dice[5 - dice_index])
