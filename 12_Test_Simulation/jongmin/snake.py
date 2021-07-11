N=int(input())
K=int(input())
board=[[0 for i in range(N+1)] for j in range(N+1)]
apples=[]
turns=[]
def turn(op, vecx, vecy):
    if(op=='L'):
        dx=vecy
        dy=-vecx
    else:
        dx=-vecy
        dy=vecx
    return (dx,dy)
for i in range(K):
    row,col=map(int, input().split())
    board[row][col]=1
L=int(input())
for i in range(L):
    X,C=input().split()
    turns.append([int(X),C])
head=[1,1] #row,col
snake=[[head[0],head[1]]]
board[head[0]][head[1]]=2
sec=0
dx=1
dy=0
while True:
    head[0]=head[0]+dy
    head[1]=head[1]+dx
    xpos=head[1]
    ypos=head[0]
    if(ypos<1 or xpos<1 or ypos>N or xpos>N or board[ypos][xpos]==2):
        sec+=1
        break
    if(board[head[0]][head[1]]==1):
        pass
    else:
        tail=snake.pop(0)
        board[tail[0]][tail[1]]=0
    board[head[0]][head[1]] = 2
    snake.append([ypos,xpos])
    sec+=1
    if(len(turns)>0 and turns[0][0]==sec):
        dx,dy=turn(turns[0][1],dx,dy)
        turns.pop(0)
print(sec)