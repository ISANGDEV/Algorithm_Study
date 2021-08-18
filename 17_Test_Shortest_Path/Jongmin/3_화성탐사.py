from heapq import heappush,heappop
dx=[-1,1,0,0]
dy=[0,0,1,-1]
INF=int(1e9)
heap=[]
T=int(input())
for _ in range(T):
    N = int(input())
    graph = []
    distance =[[INF]*N for i in range(N)]
    for i in range(N):
        graph.append(list(map(int, input().split())))
    heappush(heap, [graph[0][0],0,0])
    while heap:
        c,y,x=heappop(heap)
        for i in range(len(dx)):
            nexty=y+dy[i]
            nextx=x+dx[i]
            if(0<=nexty<N and 0<=nextx<N):
                cost= c+graph[nexty][nextx]
                if(distance[nexty][nextx]>cost):
                    distance[nexty][nextx]=min(distance[nexty][nextx],cost)
                    heappush(heap,[cost, nexty,nextx])
    print(distance[-1][-1])