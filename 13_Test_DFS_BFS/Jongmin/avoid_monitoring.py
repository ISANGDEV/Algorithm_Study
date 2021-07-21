N=int(input())
board=[]
teachers=[]
for i in range(N):
    aisle=list(input().split())
    board.append(aisle)
    for j in range(N):
        if(board[i][j]=='T'):
            teachers.append([i,j])

result=False
endState=False
def isAvoidable(arr):
    L=len(arr)
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    for t in teachers:
        x,y=t
        for i in range(len(dx)):
            idx=0
            while(0<=x+dx[i]*idx<L and 0<=y+dy[i]*idx<L):
                if(arr[x+dx[i]*idx][y+dy[i]*idx]=='O'):
                    break
                elif(arr[x+dx[i]*idx][y+dy[i]*idx]=='S'):
                    return False
                idx+=1
    return True



def sol(arr,cnt,start):
    global endState
    global result
    if(endState==True):
        return
    if(cnt==3):
        if(isAvoidable(arr)):
            result=True
            endState=True
            return
    else:
        for i in range(start,N*N):
            ypos = i // N
            xpos = i % N
            if(board[ypos][xpos]=='X'):
                board[ypos][xpos]='O'
                sol(arr,cnt+1,start+1)
                board[ypos][xpos]='X'
sol(board,0,0)
if(result):
    print('YES')
else:
    print('NO')