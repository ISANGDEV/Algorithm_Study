import sys
from collections import deque

def make_wall():
    # 선생 좌표는 고정
    # 학생을 만나면 1 반환, 못 만나면 0 반환
    for a,b in wall:
        for c,d in wall:
            for e,f in wall:

                if (geo[a][b] == "X" and geo[c][d] == "X" and geo[e][f] == "X") and not ((a == c and b == d) or (c == e and d == f) or (a == e and b == f)):
                    geo[a][b] = "O"
                    geo[c][d] = "O"
                    geo[e][f] = "O"
                    answer = 0

                    for i, j in teacher:
                        answer += bfs(i,j,geo)

                    if answer == 0: #학생 못 만났음.
                        return 0

                    geo[a][b] = "X"
                    geo[c][d] = "X"
                    geo[e][f] = "X"

    return 1 # 감시하는 걸 막지 못했음

def bfs(new_x,new_y,geo_temp): # 여기에 teacher 좌표 집어 넣으면 됨.
    # geo_temp = make_wall(geo) # 벽 세우기 이렇게 하면 벽 한번만 세우고 끝나니까 이렇게 하면 안되고
    vec = [[-1, 0], [1, 0], [0, 1], [0, -1]]


    for i, j in vec:
        temp_x = new_x
        temp_y = new_y

        while True:
            temp_x += i
            temp_y += j
            if temp_x < 0 or temp_x >= n or temp_y < 0 or temp_y >= n or geo_temp[temp_x][temp_y] == "O": # 벽이 있거나, 범위를 벗어났으면 더 이상 진행을 못하니 종료
                break
            elif 0 <= temp_x < n and 0 <= temp_y < n :
                if geo_temp[temp_x][temp_y] == "X": # 빈 공간일 때는 진행 가능하니 계속 진행
                    continue
                elif geo_temp[temp_x][temp_y] == "S": # 학생을 만났을 때 1 값 반환
                    return 1

    return 0


n = int(sys.stdin.readline())
geo = []

teacher = []
result = int(1e9)

for i in range(n):
    geo.append(list(map(str, sys.stdin.readline().split())))


wall = []

for i in range(n):
    for j in range(n):
        wall.append([i,j])

for i,j in wall:
    if geo[i][j] == "T":
        teacher.append([i,j])

result = min(result,make_wall())


if result > 0:
    print("NO")
elif result == 0:
    print("YES")