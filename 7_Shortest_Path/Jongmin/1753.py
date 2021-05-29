import sys
from heapq import heappush,heappop
INF=int(1e9)
V,E=map(int, input().split())
K=int(input())
graph=[[] for i in range(V+1)]
for i in range(E):
    u,v,w=map(int, sys.stdin.readline().split())
    graph[u].append([w,v])
distance = [INF] * (V + 1)
heap=[]
def dijkstra(start):
    distance[start]=0
    heappush(heap,[0,start])
    while heap:
        c,p=heappop(heap)
        for point in graph[p]:
            cc,pp=point
            cost=cc+c
            if cost<distance[pp]:
                distance[pp]=cost
                heappush(heap,[cost, pp])
dijkstra(K)
for i in range(1,V+1):
    if distance[i]==INF:
        print("INF")
    else:
        print(distance[i])
