from collections import deque
import sys

input = sys.stdin.readline

n, m, k, x = map(int, input().rstrip().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

q = deque()

def bfs(graph, start, max):
    ret = []
    q.append((start, 0))
    visited[start] = True
    while q:
        now, depth = q.popleft()
        for i in graph[now]:
            if visited[i]:
                continue
            else:
                if depth == max-1:
                    ret.append(i)
                    visited[i] = True
                    continue
                q.append((i, depth+1))
                visited[i] = True
    if ret:
        return sorted(ret)
    else:
        return [-1]


for answer in bfs(graph, x, k):
    print(answer)