w=-1
h=-1
result=[]
dx=[0,0,-1,1,-1,-1,1,1]
dy=[-1,1,0,0,1,-1,-1,1]
while True:
    w,h=map(int, input().split())
    if(w==0 and h==0):
        break
    board=[[] for j in range(h)]
    for i in range(h):
        board[i]=list(map(int, input().split()))
    cnt=0
    for i in range(h):
        for j in range(w):
            if(board[i][j]==1):
                cnt+=1
                stack = []
                stack.append([i,j])
                while stack:
                    savedypos,savedxpos=stack.pop()
                    board[savedypos][savedxpos]=0
                    for k in range(len(dy)):
                        ypos=savedypos+dy[k]
                        xpos=savedxpos+dx[k]
                        if(0<=ypos<h and 0<=xpos<w and board[ypos][xpos]==1):
                            stack.append([ypos,xpos])
    result.append(cnt)
for r in result:
    print(r)