N=int(input())
graph=[[0]*501 for i in range(501)]
for i in range(N):
    x1,y1,x2,y2=map(int,input().split())
    for y in range(y1,y2):
        for x in range(x1,x2):
            graph[x][y]=1
result=0
for i in range(501):
    for j in range(501):
        result+=graph[i][j]
print(result)
