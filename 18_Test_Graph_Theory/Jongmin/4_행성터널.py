N=int(input())
def cost(A,B):
    return min(abs(A[0]-B[0]),abs(A[1]-B[1]),abs(A[2]-B[2]))
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
points=[]
for i in range(N):
    x,y,z=map(int,input().split())
    points.append([x,y,z])
edges =[]
for p in range(1,len(points)):
    for j in range(p):
        edges.append([p,j,cost(points[p],points[j])])
edges.sort(key=lambda x:x[2])
parents = [i for i in range(N)]
result=0
for e in edges:
    x,y,c=e
    if(find(parents,x)!=find(parents,y)):
        union(parents,x,y)
        result+=c
print(result)
