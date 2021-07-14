
from itertools import combinations
n,m=map(int,input().split())
graph=[]
home=[]
chicken=[]

for i in range(n):
    graph.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if(graph[i][j]==2):
            chicken.append([i,j])
        elif(graph[i][j]==1):
            home.append([i,j])
last=20000
for c in combinations(chicken, m):
    answer=0
    for h in home:
        result=20000
        for i in c:
             temp=abs(h[0]-i[0])+abs(h[1]-i[1])
             if(temp<result):
                result=temp
        answer+=result
    if(answer<last):
        last=answer
            
print(last)
