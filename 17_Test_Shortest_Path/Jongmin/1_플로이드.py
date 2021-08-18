n = int(input())
m = int(input())
INF = 10 ** 10
adj = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    adj[i][i] = 0
for i in range(m):
    a, b, c = map(int, input().split())
    adj[a][b] = min(adj[a][b], c)
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(0 if adj[i][j]==INF else adj[i][j], end=' ')
    print()
