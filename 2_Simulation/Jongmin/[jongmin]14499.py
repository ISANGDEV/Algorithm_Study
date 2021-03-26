N,M,y,x,K=map(int,input().split())
maps=[]
dice=[0]*7
for i in range(N):
    maps.append(list(map(int,input().split())))
commands=list(map(int,input().split()))
for command in commands:
    if(command==1):
        newx=x+1
        newy=y
    elif(command==2):
        newx=x-1
        newy=y
    elif(command==3):
        newx=x
        newy=y-1
    else:
        newx=x
        newy=y+1
    if(0<=newx<M and 0<=newy<N):
        if (command == 1):
            dice[1],dice[4],dice[3],dice[6]=dice[4],dice[6],dice[1],dice[3]
        elif (command == 2):
            dice[1], dice[4], dice[3],dice[6] = dice[3], dice[1], dice[6],dice[4]
        elif (command == 3):
            dice[1],dice[2],dice[5],dice[6]=dice[2],dice[6],dice[1],dice[5]
        else:
            dice[1],dice[2],dice[5],dice[6]=dice[5],dice[1],dice[6],dice[2]
        x=newx
        y=newy
        if(maps[y][x]==0):
            maps[y][x]=dice[6]
        else:
            dice[6]=maps[y][x]
            maps[y][x]=0
        print(dice[1])