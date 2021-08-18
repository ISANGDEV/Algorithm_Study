n, m = map(int, input().split())
INF = int(10e10)
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
visited = [False] * (n+1)

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

def get_smallest_node():
    min_val = INF
    idx = 0
    for i in range(1, n+1):
        if not visited[i] and distance[i] < min_val:
            min_val = distance[i]
            idx=i
    return idx

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for i in graph[start]:
        distance[i] = 1
    for _ in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for i in graph[now]:
            cost = distance[now] + 1
            if cost < distance[i]:
                distance[i] = cost

dijkstra(1)

max = -1
count = 1
for i in range(1, n+1):
    if max < distance[i] and distance[i] != INF:
        max = distance[i]
        idx = i
        count = 1
    elif max == distance[i]:
        count += 1

print(idx, max, count)
