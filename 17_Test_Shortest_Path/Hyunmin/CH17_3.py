import heapq
INF = int(1e9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra(graph, n):
    visited = [[False] * n for _ in range(n)]
    distance = [[INF] * n for _ in range(n)]
    distance[0][0] = graph[0][0] #  
    q = []
    heapq.heappush(q, (0, 0)) # x, y 

    while q: 
        x, y = heapq.heappop(q)
        
        for i in range(4): 
            nx, ny = x + dx[i], y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if distance[nx][ny] > distance[x][y] + graph[nx][ny]: 
                    heapq.heappush(q, (nx, ny))
                    distance[nx][ny] = distance[x][y] + graph[nx][ny] 
    return distance[n-1][n-1]

T = int(input())
result = []
for _ in range(T):
    N = int(input().rstrip())
    graph = [list(map(int, input().split())) for _ in range(N)]
    # 0 -> N-1, N-1 
    # 다익스트라 사용 
    result.append(dijkstra(graph, N))
print("results = ", result)

