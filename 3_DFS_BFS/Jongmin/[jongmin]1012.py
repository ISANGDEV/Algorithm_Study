T=int(input())
dx=[-1,1,0,0]
dy=[0,0,-1,1]
result=[]
visited=[]
graph=[]
def dfs(x,y):
    for l in range(len(dx)):
        posx=x+dx[l]
        posy=y+dy[l]
        if (0 <= posx < M and 0 <= posy < N and visited[posy][posx] == 0 and graph[posy][posx] == 1):
            visited[posy][posx] = 1
            dfs(posx, posy)

for i in range(T):
    M, N, K = map(int, input().split(" "))
    graph = [[0 for k in range(M)] for l in range(N)]
    visited = [[0 for k in range(M)] for l in range(N)]
    for j in range(K):
        x, y = map(int, input().split(" "))
        graph[y][x] = 1
    count = 0
    for j in range(N):
        for k in range(M):
            if (graph[j][k] == 1 and visited[j][k] == 0):
                visited[j][k]=1
                dfs(k,j)
                count += 1
    result.append(count)
for i in result:
    print(i)



