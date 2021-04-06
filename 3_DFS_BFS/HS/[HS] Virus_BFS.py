"""어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때,
 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다.
둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다.
 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다. """

from collections import deque

n = int(input("컴퓨터 개수"))
m = int(input("연결 쌍 개수"))
graph = [[] for i in range(n+1)] # []는 인덱싱 편하게 하기 위해서, + 빈공간을 연결 쌍의 개수만큼 생성
visited = [False] * (n + 1) # +1도 마찬가지로 인덱싱 편하기 하기 위해서.
info = []
for i in range(m):
    info.append(list(map(int,input("연결 번호 정보 입력").split())))

for i,j in info:
    graph[i].append(j)
    graph[j].append(i) # 그래프 정보를 조작할 수 있도록 , 익숙한 형태로 만들어 줬음


def bfs(graph): # 어차피 1번이랑 연결된 것만 찾으면 되니까, 숫자를 입력 받지 않아도 된다. + DFS는 재귀함수라서, 숫자 입력받아야함.
    global visited
    queue = deque()
    queue.append(1)

    visited[1] = True

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if visited[i] != True:
                queue.append(i)
                visited[i] = True

    return

count = 0

bfs(graph)
for i in visited:
    if i == True:
        count += 1

print(count-1) # 1 제외
