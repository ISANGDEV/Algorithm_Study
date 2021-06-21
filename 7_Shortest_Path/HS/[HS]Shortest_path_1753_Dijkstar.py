import heapq
import sys

inf = int(1e9)

v,e = map(int,sys.stdin.readline().split())
start_num = int(sys.stdin.readline())

table = [[] for i in range(v+1)]
distance = [inf] * (v+1)

for i in range(e):
    a,b,c = map(int,sys.stdin.readline().split())
    table[a].append((b,c))


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

for i in range(1,v+1):
    if distance[i] == inf:
        print("INF")
    else:
        print(distance[i])



