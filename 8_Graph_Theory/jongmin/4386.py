n=int(input())
stars=[[0.0,0.0]]
edges=[]
parents=[i for i in range(n+1)]

def distance(p1,p2):
    x1=p1[0]
    y1=p1[1]
    x2=p2[0]
    y2=p2[1]
    return pow(pow(x1-x2,2)+pow(y1-y2,2),0.5)

def find(parent, a):
    if a!=parent[a]:
        return find(parent,parent[a])
    else:
        return a

def union(parent, a,b):
    a=find(parent,a)
    b=find(parent,b)
    if(a<b):
        parent[a]=b
    else:
        parent[b]=a

for i in range(n):
    x,y=map(float,input().split())
    stars.append([x,y])
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i!=j):
            cost=distance(stars[i],stars[j])
            edges.append([cost,i,j])
edges.sort(key=lambda x:x[0])
result=0.0
for e in edges:
    cost, a,b=e
    if(find(parents,a)!=find(parents,b)):
        result+=cost
        union(parents,a,b)
print(format(result, ".2f"))