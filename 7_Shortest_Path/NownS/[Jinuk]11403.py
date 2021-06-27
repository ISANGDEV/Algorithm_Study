INF = int(10e9)

n = int(input())

graph = [[INF for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j, k in zip(range(1, n+1), map(int, input().split())):
        if k == 0:
            graph[i][j] = INF
        else:
            graph[i][j] = k

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print("0", end=" ")
        else:
            print("1", end=" ")
    print()