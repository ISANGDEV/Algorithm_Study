from collections import deque

n = int(input())
visit = [False] * (n+1)
link = [[] for _ in range(n+1)]

st, en = map(int, input().split())

for _ in range(int(input())):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)

queue = deque()


def bfs(graph, start, end, visited):
    count = 0
    queue.append((start, count))
    visited[start] = True
    while queue:
        k, count = queue.popleft()
        if k == end:
            return count
        count += 1
        for i in graph[k]:
            if not visited[i]:
                queue.append((i, count))
                visited[i] = True
    return -1


print(bfs(link, st, en, visit))