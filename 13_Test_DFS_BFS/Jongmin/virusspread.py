import copy
temp=input().split(' ')
N=int(temp[0])
M=int(temp[1])
A = [list(map(int, input().split())) for _ in range(N)]
viruslist=[]
sumlist=[]


def virusspread(arr):
    for i in range(N):
        for j in range(M):
            if A[i][j] == 2:
                viruslist.append([i, j])
    while True:
        if len(viruslist) == 0:
            break
        vir_pos=viruslist.pop()
        for pos in [[-1,0],[1,0],[0,1],[0,-1]]:
            x=pos[0]
            y=pos[1]
            nx=vir_pos[1]+x
            ny=vir_pos[0]+y
            if M>nx>=0 and N>ny>=0:
                if arr[ny][nx]==0:
                    arr[ny][nx]=2
                    viruslist.append([ny,nx])
    sum=0
    for i in range(N):
        for j in range(M):
            if arr[i][j]==0:
                sum+=1
    return sum


def wall(start,cnt):
    if cnt==3:
        arr_temp=copy.deepcopy(A)
        sumlist.append(virusspread(arr_temp))
    else:
        for i in range(start,M*N):
            ypos=i//M
            xpos=i%M
            if A[ypos][xpos]==0:
                A[ypos][xpos]=1
                wall(i+1,cnt+1)
                A[ypos][xpos]=0
wall(0,0)
print(max(sumlist))