from collections import deque

n, m, v = map(int, input().split())

node = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

for i in range(n+1):
    node[i].sort()

stack = []
def dfs(graph, start, visited):
    stack.append(start)
    visited[start] = True
    print(start, end=" ")
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)



queue = deque()
def bfs(graph, start, visited):
    queue.append(start)
    visited[start] = True
    while queue:
        k = queue.popleft()
        print(k, end=" ")
        for i in graph[k]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True



visited = [False for i in range(n+1)]
dfs(node, v, visited)

print()

visited = [False for i in range(n+1)]
bfs(node, v, visited)
