def dfs_non_recursive(graph, s):
    visited = []
    stack = [s]
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            stack += reversed(graph[v])
    return len(visited) - 1


nodes = int(input(''))
lines = int(input(''))

graph = [[] for i in range(nodes+1)]
for i in range(lines):
    line = list(map(int, input('').split()))
    graph[line[0]].append(line[1])
    graph[line[1]].append(line[0])

print(dfs_non_recursive(graph, 1))

