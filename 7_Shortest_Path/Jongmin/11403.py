N=int(input())
INF=int(1e9)
graph=[]
for _ in range(N):
    graph.append(list(map(lambda x: INF if int(x)==0 else int(x),input().split())))
for k in range(N):
    for i in range(N):
        for j in range(N):
            if(graph[i][j]>graph[i][k]+graph[k][j]):
                graph[i][j]=graph[i][k]+graph[k][j]
for i in range(N):
    for j in range(N):
        if(graph[i][j]==INF):
            print("0",end=' ')
        else:
            print("1",end=' ')
    print()