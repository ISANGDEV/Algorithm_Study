import heapq 
N, M = list(map(int, input().split()))
INF = int(1e9)
# 인접리스트로 시도  
graph = [[] for _ in range(N+1)] 
result = [] 
def dijkstra(start, start_value): 
    q = []
    heapq.heappush(q, (start, start_value))
    distance = [INF] * (N + 1)
    
    distance[start] = start_value  
    while q: 
        now, now_value = heapq.heappop(q)
        for values in graph[now]:  # now(1) 에서 갈 수 있는 것들 다 
            next, next_value = values[0], values[1]
            if distance[next] > distance[now] + next_value: 
                heapq.heappush(q, (next, next_value))
                distance[next] = distance[now] + next_value 
    for i in range(N+1):
        if distance[i] == INF: 
            distance[i] = -1 
    max_value = max(distance)
    for i in range(N+1): 
        if max_value == distance[i]: 
            result.append((i, distance[i]))

            
for _ in range(M): 
    a, b = list(map(int, input().split())) 
    graph[a].append((b, 1))
    graph[b].append((a, 1))

dijkstra(1, 0)  # in = starting point out = toHideIdx, value, 같은 거리인 값은 나중에 찾는다. 
result.sort(key=lambda x: x[0])
print(result[0][0], result[0][1], len(result))
