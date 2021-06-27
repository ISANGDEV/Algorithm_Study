n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
stack = []
num = -1

def dfs(graph, start, visited):
    stack.append(start)
    visited[start] = True
    global num
    num += 1
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, 1, visited)
print(num)