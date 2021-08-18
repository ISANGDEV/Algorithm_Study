n, m = map(int, input().split())

INF = int(10e9)

graph = [[INF for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for i in range(1, n+1):
    graph[i][i] = 0

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0

for i in range(1, n+1):
    could = True
    for j in range(1, n+1):
        if graph[i][j] == INF and graph[j][i] == INF:
            could = False
            break
    if could:
        result += 1

print(result)