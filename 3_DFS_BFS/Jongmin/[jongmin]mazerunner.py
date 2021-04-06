N,M=map(int,input().split())
graph=[]
for i in range(N):
    graph.append(list(map(int,list(input()))))
q=[[0,0,1]]
answer=0
dx=[0,0,-1,1]
dy=[-1,1,0,0]
while q:
    y,x,depth=q.pop(0)
    if(y==N-1 and x==M-1):
        print(depth)
        break
    graph[y][x]=0
    for k in range(len(dx)):
        ypos = y + dy[k]
        xpos = x + dx[k]
        if (0 <= ypos < N and 0 <= xpos < M and graph[ypos][xpos] == 1):
            q.append([ypos, xpos,depth+1])