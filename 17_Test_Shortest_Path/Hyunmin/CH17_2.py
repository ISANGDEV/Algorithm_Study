N, M = list(map(int, input().split())) 
INF = int(1e9)
graph = [[INF]*(N+1) for _ in range(N+1)]

for _ in range(M): 
    a, b = list(map(int, input().split()))
    graph[a][b] = 1 

for i in range(N+1): 
    graph[i][i] = 0 

for k in range(N+1):
    for a in range(N+1): 
        for b in range(N+1): 
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0 
for i in range(1, N+1): 
    count = 0 
    for j in range(1, N+1):
        # 숫자의 가로줄 세로줄 중 각각 INF가 아닌 값의 개수가 학생에게 들어온 개수, 학생으로부터 나간 개수 이다.
        if graph[i][j]!=INF or graph[j][i]!=INF: 
            count += graph[j][i]
    if count == N: 
        result += 1
print("result= ", result)


