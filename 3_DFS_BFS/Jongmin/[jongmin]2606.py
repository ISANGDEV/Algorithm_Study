N=int(input())
M=int(input())
graph=[[0 for i in range(N+1)] for j in range(N+1)]
for i in range(M):
    row, col=map(int, input().split(" "))
    graph[row][col]=1
    graph[col][row]=1
visited=[0 for i in range(N+1)]
def dfs(n):
    for i in range(1,N+1):
        if(visited[i]==0 and graph[n][i]==1):
            visited[i]=1
            dfs(i)
dfs(1)
print(visited.count(1)-1)