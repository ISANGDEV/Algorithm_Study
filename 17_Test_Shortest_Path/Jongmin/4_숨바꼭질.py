from heapq import heappush,heappop
heap=[]
N,M=map(int,input().split())
INF=10**6
distances = [INF]*N
graph = [[] for _ in range(N)]
for _ in range(M):
    A,B=map(int,input().split())
    graph[A-1].append(B-1)
    graph[B-1].append(A-1)
heappush(heap, [0,0])
while heap:
    cost, p = heappop(heap)
    for pp in graph[p]:
        if(distances[pp]>cost+1):
            distances[pp]=cost+1
            heappush(heap, [cost+1, pp])
maxval=-1
maxidx=-1
for i in range(1,len(distances)):
    if(distances[i]>maxval):
        maxval=distances[i]
        maxidx=i
print(maxidx+1, maxval, distances[1:].count(maxval))