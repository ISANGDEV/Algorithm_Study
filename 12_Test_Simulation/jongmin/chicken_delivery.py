from itertools import combinations
def distance(p1,p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
def minDistance(chickenhouses, home):
    result=distance(chickenhouses[0],home)
    for i in range(1,len(chickenhouses)):
        result=min(result,distance(chickenhouses[i],home))
    return result

N,M=map(int,input().split())
cities=[]
chickenhouse=[]
house=[]
for i in range(N):
    cities.append(list(map(int,input().split())))
    for j in range(N):
        if cities[i][j]==2:
            chickenhouse.append([i,j])
        elif cities[i][j]==1:
            house.append([i,j])
minChickenidx=-1
minChickenValue=10**6
chickenCombs=list(combinations(chickenhouse,M))
for ch in chickenCombs:
    ch=list(ch)
    tempResult=0
    for h in house:
        tempResult += minDistance(ch, h)
    minChickenValue=min(minChickenValue,tempResult)
print(minChickenValue)

