v, e = map(int, input().split())
k = int(input())

INF = int(10e9)

graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)
visited = [False] * (v+1)

for i in range(e):
    u, l, w = map(int, input().split())
    graph[u].append((l, w))


def get_smallest_node():
    min_val = INF
    idx = 0
    for i in range(1, v+1):
        if not visited[i] and distance[i] < min_val:
            min_val = distance[i]
            idx = i
    return idx


def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for i in graph[start]:
        distance[i[0]] = i[1]
    for _ in range(v-1):
        now = get_smallest_node()
        visited[now] = True
        for i in graph[now]:
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost


dijkstra(k)
for i in range(1, v+1):
    if i == k:
        print("0")
    elif distance[i] == INF:
        print("INF")
    else:
        print(distance[i])