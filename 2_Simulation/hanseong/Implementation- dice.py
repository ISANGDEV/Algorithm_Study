n, m, y, x, k=map(int, input().split())
total=[]
dice=[0] *6
for i in range(n):
    total.append(list(map(int,input().split())))

steps=map(int, input().split())

for i in steps:
    if(i==1 and x<m):
        x+=1
        dice[0],dice[1],dice[2],dice[3]=dice[2],dice[3],dice[1],dice[0]
    elif(i==2 and x>0):
        x-=1
        dice[0],dice[1],dice[2],dice[3]=dice[3],dice[2],dice[0],dice[1]
    elif(i==3 and y>0):
        y-=1
        dice[0],dice[1],dice[4],dice[5]=dice[5],dice[4],dice[0],dice[1]
    elif(i==4 and y<n):
        y+=1
        dice[0],dice[1],dice[4],dice[5]=dice[4],dice[5],dice[1],dice[0]
        
    if(total[y][x]==0):
        print(dice[0])
        total[y][x]=dice[1]
    else:
        print(dice[0])
        dice[1]=total[y][x]
        
        
