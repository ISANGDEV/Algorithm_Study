import sys
gears=[[] for _ in range(6)]
gearrightpos=[3]*6
for i in range(4):
    gears[i+1]=list(map(int,[0]+list(input())+[0]))
gears[0]=[0]*10
gears[5]=[0]*10
K=int(input())
def move(n,dir):
    if(dir==1):
        if (gearrightpos[n] == 1):
            gearrightpos[n] = 8
        else:
            gearrightpos[n] -= 1
    else:
        if (gearrightpos[n] == 8):
            gearrightpos[n] = 1
        else:
            gearrightpos[n] += 1
for i in range(K):
    num,direction=map(int, sys.stdin.readline().split())
    rightdirection=direction
    leftdirection=direction
    rotates = [[num,direction]]
    for j in range(num,5):
        right = gearrightpos[j + 1] - 4 if gearrightpos[j + 1] > 4 else gearrightpos[j + 1] + 4
        if(gears[j+1][right]!=gears[j][gearrightpos[j]]):
            rotates.append([j+1,-rightdirection])
            rightdirection=-rightdirection
        else:
            break
    for j in range(num,0,-1):
        left = gearrightpos[j] - 4 if gearrightpos[j] > 4 else gearrightpos[j] + 4
        if (gears[j][left] != gears[j-1][gearrightpos[j-1]]):
            rotates.append([j-1,-leftdirection])
            leftdirection=-leftdirection
        else:
            break
    for rotate in rotates:
        n,d=rotate
        move(n,d)
result=0
for i in range(4):
    twelve=gearrightpos[i+1]-2 if gearrightpos[i+1] >2 else 8+gearrightpos[i+1]-2
    if(gears[i+1][twelve]==1):
        result+=(2**i)
print(result)
