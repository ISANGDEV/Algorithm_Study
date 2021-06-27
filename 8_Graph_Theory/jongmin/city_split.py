N,M=map(int, input().split())
edges=[]
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


for i in range(M):
    homeOne, homeTwo, cost=map(int, input().split())
    edges.append([cost,homeOne,homeTwo])
edges.sort(key=lambda x:x[0])
maxCost=-1
result=0
for i in edges:
    cost, homeOne, homeTwo=i
    if(find(parents,homeOne)!=find(parents,homeTwo)):
        union(parents,homeOne,homeTwo)
        maxCost = max(cost, maxCost)
        result+=cost
print(result-maxCost)