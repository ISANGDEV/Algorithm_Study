from collections import deque


def dfs(graph, visited, v):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, visited, i)


def dfs_non_recursive(graph, s):
    visited = [False] * len(graph)
    stack = [s]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            print(v, end=' ')
            stack += reversed(graph[v])


def bfs(graph, s):
    visited = [False] * len(graph)
    queue = deque([s])
    visited[s] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


factors = list(map(int, input('').split(' ')))
graph = [[] for i in range(factors[0]+1)]
for i in range(factors[1]):
    lines = list(map(int, input('').split(' ')))
    graph[lines[0]].append(lines[1])
    graph[lines[1]].append(lines[0])
for i in range(len(graph)):
    graph[i].sort()
start = factors[2]

visited = [False] * len(graph)
dfs(graph, visited, start)
print()
dfs_non_recursive(graph, start)
print()
bfs(graph, start)




