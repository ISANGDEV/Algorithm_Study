"""그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000),
탐색을 시작할 정점의 번호 V가 주어진다.
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다.
입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다.
V부터 방문된 점을 순서대로 출력하면 된다."""

from collections import deque

n,m,v = map(int,input("정점, 간선, 탐색 시작 번호").split())
info = []
graph = [[] for i in range(n+1)] # 정점 개수 만큼 입력 받을 준비
visited_DFS = [False] * (n+1)
visited_BFS = [False] * (n+1)

for i in range(m):
    info.append(list(map(int,input("간선이 연결하는 번호").split())))

for i,j in info:
    graph[i].append(j)
    graph[j].append(i)

for i in range(n+1):
    graph[i].sort() # 정점이 작은 것부터 방문하기 위해서 정렬

def dfs(graph,v):
    global visited_DFS
    visited_DFS[v] = True
    print(v)

    for i in graph[v]:
        if visited_DFS[i] != True:
            dfs(graph,i)

    return

def bfs(graph,v):
    global visited_BFS
    queue = deque()
    queue.append(v)
    visited_BFS[v] = True
    print(v)
    while queue:
        num = queue.popleft()
        for i in graph[num]:
            if visited_BFS[i] != True:
                queue.append(i)
                visited_BFS[i] = True
                print(i)

    return

print("dfs")
dfs(graph,v)

print("bfs")
bfs(graph,v)
