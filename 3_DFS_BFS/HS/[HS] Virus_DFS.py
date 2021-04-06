"""어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때,
 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다.
둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다.
 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다. """

n = int(input("컴퓨터의 수"))
m = int(input("연결된 쌍의 수"))
graph = [[]] # 인덱싱 편하기 하기 위해서 쓸모 없는 공간 만들기
info = []
count = 0
visited = [False] *( n + 1 )
for i in range(n):
    graph.append([]) # 간선 그래프 생성 위해서 일단 각 노드 별로 영역 만들어 주기

for i in range(m):
    info.append(list(map(int,input("번호 쌍 입력").split())))

for i,j in info:
    graph[i].append(j)
    graph[j].append(i)

def dfs(graph,num):
    global visited

    visited[num] = True

    for i in graph[num]:
        if visited[i] != True:
            dfs(graph,i)
    return

dfs(graph,1)

for i in visited:
    if i == True:
        count += 1

print(count-1) # 1번 컴퓨터는 제외 해야 함.
