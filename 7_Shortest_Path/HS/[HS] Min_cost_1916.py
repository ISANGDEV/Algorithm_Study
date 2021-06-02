import heapq
import sys

inf = int(1e9)
n = int(sys.stdin.readline()) #도시 개수
m = int(sys.stdin.readline()) # 버스(간선) 개수
table = [[] for i in range(n+1)]
distance = [inf] * (n+1)

distance[0] = 0

for i in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    table[a].append((b,c))
start_num, end_num = map(int,sys.stdin.readline().split())

def dijkstra(start_num):
    heap = []
    heapq.heappush(heap,(0,start_num))
    distance[start_num] = 0
    while heap:
        dist,now = heapq.heappop(heap)
        if distance[now] < dist:
            continue
        for i in table[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap,(cost,i[0]))

dijkstra(start_num)

print(distance[end_num])
