N,M=map(int, input().split())
graph=[]
for i in range(N):
    graph.append(list(map(int,list(input()))))
answer=0
dx=[0,0,-1,1]
dy=[-1,1,0,0]
for i in range(N):
    for j in range(M):
        if(graph[i][j]==0):
            q=[[i,j]]
            answer+=1
            while q:
                y,x=q.pop(0)
                graph[y][x]=1
                for k in range(len(dx)):
                    ypos=y+dy[k]
                    xpos=x+dx[k]
                    if(0<=ypos<N and 0<=xpos<M and graph[ypos][xpos]==0):
                        q.append([ypos,xpos])
print(answer)

'''
test case
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
'''