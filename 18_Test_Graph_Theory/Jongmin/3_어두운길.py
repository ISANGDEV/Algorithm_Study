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

N,M=map(int, input().split())
edges = []
total =0
for i in range(M):
    X,Y,Z=map(int,input().split())
    edges.append([X,Y,Z])
    total+=Z
edges.sort(key=lambda x:x[2])
parents = [i for i in range(N)]

mini=0
for edge in edges:
    x,y,cost = edge
    if(find(parents,x)!=find(parents,y)):
        union(parents,x,y)
        mini+=cost
print(total-mini)



