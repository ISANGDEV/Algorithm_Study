from collections import deque
N,K=map(int,input().split())
dx=[1,-1,0,0]
dy=[0,0,-1,1]
board=[]
templist=[]
for i in range(N):
    board.append(list(map(int,input().split())))
    for j in range(N):
        if(board[i][j]!=0):
            templist.append([board[i][j],i,j,0])
S,X,Y=map(int,input().split())
templist.sort(key=lambda x:x[0])
q=deque(templist)
while q:
    value,y,x,timeCnt=q.popleft()
    if(timeCnt==S):
        break
    for i in range(len(dx)):
        nexty=y+dy[i]
        nextx=x+dx[i]
        if(0<=nextx<N and 0<=nexty<N and board[nexty][nextx]==0):
            q.append([value,nexty,nextx,timeCnt+1])
            board[nexty][nextx]=value
print(board[X-1][Y-1])
