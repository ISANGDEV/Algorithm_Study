N,M,V=map(int, input().split(' '))
graph=[[0 for i in range(N+1)] for j in range(N+1)]
visited=[0 for i in range(N+1)]
for i in range(M):
    a,b=map(int, input().split(' '))
    graph[a][b]=1
    graph[b][a]=1
def dfs(v):
    for i in range(1, N + 1):
        if (graph[v][i] == 1 and visited[i] == 0):
            print(i, end=" ")
            visited[i] = 1
            dfs(i)
def bfs(v):
    queue=list()
    queue.append(v)
    while queue:
        node=queue.pop(0)
        for i in range(1,N+1):
            if(graph[node][i]==1 and visited[i]==0):
                print(i,end=" ")
                queue.append(i)
                visited[i]=1
print(V,end=" ")
visited[V]=1
dfs(V)
print('')
visited=[0 for i in range(N+1)]
print(V, end=" ")
visited[V] = 1
bfs(V)