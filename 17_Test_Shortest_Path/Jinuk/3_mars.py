import heapq

t = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

INF = int(10e10)

answer = []

for _ in range(t):
    n = int(input())
    distance = [[INF for _ in range(n)] for _ in range(n)]
    mars_map = []
    for _ in range(n):
        mars_map.append(list(map(int, input().split())))
    
    q = [(mars_map[0][0], 0, 0)]
    distance[0][0] = mars_map[0][0]

    while q:
        d, x, y = heapq.heappop(q)
        if distance[x][y] < d:
            continue

        for i in range(4):
            nextx, nexty = x + dx[i], y + dy[i]
            if nextx < 0 or nextx > n-1 or nexty < 0 or nexty > n-1:
                continue
            cost = d + mars_map[nextx][nexty]
            if cost < distance[nextx][nexty]:
                distance[nextx][nexty] = cost
                heapq.heapqpush(q, (cost, nextx, nexty))

    answer.append(distance[n-1][n-1])

for i in range(t):
    print(answer[i])
    
