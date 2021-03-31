import copy
N,M=map(int,input().split())
office=[]
cameras=[]
for i in range(N):
    office.append(list(map(int,input().split())))
    for j in range(M):
        if(office[i][j]!=0 and office[i][j]!=6):
            cameras.append([i,j,office[i][j]])
def up(x,y,officemap):
    for j in range(y,-1,-1):
        if (officemap[j][x] == 0):
            officemap[j][x]='#'
        if(officemap[j][x]==6):
            break
def down(x,y,officemap):
    for j in range(y + 1, N):
        if (officemap[j][x] == 0):
            officemap[j][x]='#'
        if(officemap[j][x]==6):
            break
def right(x,y,officemap):
    for j in range(x + 1, M):
        if (officemap[y][j] == 0):
            officemap[y][j]='#'
        if(officemap[y][j]==6):
            break
def left(x,y,officemap):
    for j in range(x,-1,-1):
        if (officemap[y][j] == 0):
            officemap[y][j]='#'
        if(officemap[y][j]==6):
            break
result=99999999999
direc=[[],[[0],[1],[2],[3]],[[0,2],[1,3]],[[0,1],[1,2],[2,3],[3,0]],[[1,2,3],[0,2,3],[0,1,3],[0,1,2]],[[0,1,2,3]]]
def sol(officearr,cnt):
    global result
    if(cnt==len(cameras)):
        cnt=0
        for line in officearr:
            cnt+=line.count(0)
        result=min(result,cnt)
        return
    y,x,cnum=cameras[cnt]
    for dirlist in direc[cnum]:
        temparr = copy.deepcopy(officearr)
        for dirs in dirlist:
            if(dirs==0):
                up(x,y,temparr)
            elif(dirs==1):
                right(x,y,temparr)
            elif(dirs==2):
                down(x,y,temparr)
            else:
                left(x,y,temparr)
        sol(temparr,cnt+1)
sol(office,0)
print(result)