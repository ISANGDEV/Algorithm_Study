from collections import deque
N,L,R=map(int, input().split())
countires=[[] for i in range(N)]
for i in range(N):
    countires[i]=list(map(int, input().split()))
cnt=0
dx=[0,0,-1,1]
dy=[1,-1,0,0]
def bfs(x,y):
    result=[]
    result.append([x,y])
    q=deque()
    q.append([x,y])
    while q:
        item=q.popleft()
        value=countires[item[1]][item[0]]
        for i in range(len(dx)):
            xpos=item[0]+dx[i]
            ypos=item[1]+dy[i]
            if(0<=xpos<N and 0<=ypos<N and visits[ypos][xpos]==0 and L<=abs(value-countires[ypos][xpos])<=R):
                q.append([xpos,ypos])
                result.append([xpos,ypos])
                visits[ypos][xpos]=1
    return result
cnt=0
while True:
    st=False
    visits=[[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            if(visits[i][j]==0):
                visits[i][j]=1
                result=bfs(j,i)
                if(len(result)>1):
                    st=True
                    total=0
                    for r in result:
                        xpos=r[0]
                        ypos=r[1]
                        total+=countires[ypos][xpos]
                    value=total//len(result)
                    for r in result:
                        xpos = r[0]
                        ypos = r[1]
                        countires[ypos][xpos]=value
    if(st==False):
        break
    cnt+=1
print(cnt)