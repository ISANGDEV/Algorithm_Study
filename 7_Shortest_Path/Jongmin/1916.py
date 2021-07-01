import sys
from heapq import heappush,heappop
INF=int(1e9)
heap=[]
N=int(input())
M=int(input())
graph=[[] for i in range(N+1)]
distance=[INF]*(N+1)
for i in range(M):
    s,e,c=map(int,sys.stdin.readline().split())
    graph[s].append([c,e])
start,end=map(int,input().split())
distance[start]=0
heappush(heap,[0,start])
while heap:
    c,p=heappop(heap)
    for cc,pp in graph[p]:
        cost=c+cc
        if(distance[pp]>cost):
            distance[pp]=cost
            heappush(heap,[cost,pp])
print(distance[end])
