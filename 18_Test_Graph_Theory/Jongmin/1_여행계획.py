N, M = map(int, input().split())

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

graph = []
parent = [i for i in range(N)]
for i in range(N):
    inArr = list(map(int, input().split(' ')))
    for j in range(N):
        if(inArr[j]==1):
            union(parent, i, j)
travel = list(map(int,input().split(' ')))
result = find(parent,travel[0]-1)
status=True
for t in travel:
    if(find(parent,t-1)!=result):
        status=False
        break
print(status)
