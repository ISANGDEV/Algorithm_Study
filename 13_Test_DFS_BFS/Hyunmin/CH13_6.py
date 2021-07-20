import itertools
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

X = 0
T = 1
S = 2
O = 3

n = int(input())
pos = []

map_arr = [[0] * n for _ in range(n)]
tea_list = []
stu_list = []
base_visited = [[False] * n for _ in range(n)]
visited = []

for i in range(n):
    d = input().split()
    for j in range(len(d)):
        if d[j] == "X":
            map_arr[i][j] = 0
        elif d[j] == "T":
            map_arr[i][j] = 1
            base_visited[i][j] = True
            tea_list.append((i, j))
        else:
            map_arr[i][j] = 2
            stu_list.append((i, j))
        pos.append((i, j))

# 3개 장애물 설치 모든 경우의 수, 6*6중에서 3개 36c3, X 중복
result = list(itertools.combinations(pos, 3))
ok = False
for wall_1, wall_2, wall_3 in result:
    if map_arr[wall_1[0]][wall_1[1]] != X or map_arr[wall_2[0]][wall_2[1]] != X or map_arr[wall_3[0]][wall_3[1]] != X:
        continue

    del_data = []
    del_data.append((wall_1[0], wall_1[1], map_arr[wall_1[0]][wall_1[1]]))
    del_data.append((wall_2[0], wall_2[1], map_arr[wall_2[0]][wall_2[1]]))
    del_data.append((wall_3[0], wall_3[1], map_arr[wall_3[0]][wall_3[1]]))

    # 벽 세우기
    map_arr[wall_1[0]][wall_1[1]] = O
    map_arr[wall_2[0]][wall_2[1]] = O
    map_arr[wall_3[0]][wall_3[1]] = O

    check = True
    for tea_pos in tea_list:
        for i in range(4):
            next_x = tea_pos[0] + dx[i]
            next_y = tea_pos[1] + dy[i]
            while next_x < n and next_y < n and next_x >= 0 and next_y >= 0:
                if map_arr[next_x][next_y] == S:
                    check = False
                    break
                if map_arr[next_x][next_y] == O:
                    break
                next_x = next_x + dx[i]
                next_y = next_y + dy[i]
    # 한 번도 T가 S를 잡지 않았다면, 즉 학생 모두 생존
    if check:
        ok = True
        break

    # 벽 복구
    length = len(del_data)
    for _ in range(length):
        xx, yy, zz = del_data.pop()
        map_arr[xx][yy] = zz

if ok:
    print("YES")
else:
    print("NO")

