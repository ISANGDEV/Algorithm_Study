"""동빈이는 N * M 크기의 직사각형 미로에 갇혀 있다. 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다.
 동빈이의 위치는 (1, 1)이고 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있다.
  이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다.
   미로는 반드시 탈출할 수 있는 형태로 제시된다. 이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오.
   칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.


입력

첫째 줄에 두 정수 N, M(4<=N, M <= 200)이 주어집니다.
다음 N개의 줄에는 각각 M개의 정수(0 혹은 1)로 미로의 정보가 주어진다.
각각의 수들은 공백 없이 붙어서 입력으로 제시된다.
또한 시작 칸과 마지막 칸은 항상 1이다. """

# dfs는 순열이랑 조합같은 문제에 활용 할 수 있음

# bfs를 이용한 최단 거리 확인은 Tree 구조의 "레벨"값을 이용한 풀이임.
#같은 레벨의 노드라면 어떤 노드에서 출발 하더라도 각각의 노드에 도착하는 최단 거리는 동일 함.
from collections import deque

n,m = map(int,input("세로 가로 입력").split())
count = 1
dx = [1,-1,0,0]
dy = [0,0,1,-1]
geo = []
for i in range(n):
    geo.append(list(map(int,input("미로의 정보 입력"))))

def bfs(x,y):
    col = x - 1
    row = y - 1
    queue = deque()
    queue.append((col,row))
    # deque()(col,row)) 로 하니까 error.
    while queue:
        pos_x,pos_y = queue.popleft()

        for i in range(4):
            next_col = pos_x + dx[i]
            next_row = pos_y + dy[i]

            if next_col < 0 or next_col >= n or next_row < 0 or next_row >= m : # 범위 확인
                continue

            if geo[next_col][next_row] == 0 : # 벽이라면 못 감
                continue

            if geo[next_col][next_row] == 1 : # 방문하지 않은 곳이라면
                geo[next_col][next_row] = geo[pos_x][pos_y] + 1 # 이전의 이동거리 (레벨) + 1
                queue.append((next_col,next_row)) # 이동한 후에는 덱에 넣어주기


    return geo[n-1][m-1] # 최종 목적지의 값을 리턴하면 -> 함수에 들어간 지점부터 이 도착지까지의 거리가 나온다. (48행)

result = bfs(1,1)

print(result)
