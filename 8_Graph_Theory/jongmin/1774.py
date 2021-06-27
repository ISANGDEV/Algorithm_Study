N,M=map(int, input().split())
edges=[]
points=[[-1,-1]]
parents=[i for i in range(N+1)]

def find(parent, x):
    if parent[x] != x:
        return find(parent, parent[x])
    return x


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def distance(p1,p2):
    x1=p1[0]
    y1=p1[1]
    x2=p2[0]
    y2=p2[1]
    return pow(pow(x1-x2,2)+pow(y1-y2,2),0.5)


for i in range(N):
    X,Y=map(int, input().split())
    points.append([X,Y])
for i in range(M):
    pointOne, pointTwo=map(int, input().split())
    if (find(parents, pointOne) != find(parents, pointTwo)):
        union(parents, pointOne, pointTwo)
for i in range(1,N+1):
    for j in range(1,N+1):
        if(i!=j):
            cost=distance(points[i],points[j])
            edges.append([cost,i,j])
edges.sort(key=lambda x:x[0])
result=0.0
for i in edges:
    cost, pointOne, pointTwo=i
    if(find(parents,pointOne)!=find(parents,pointTwo)):
        union(parents,pointOne,pointTwo)
        result+=cost
print(format(result,".2f"))