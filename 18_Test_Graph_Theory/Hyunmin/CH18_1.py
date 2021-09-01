def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)] 
path = list(map(int, input().split()))
parent = [0] * (N+1)

for i in range(1, N + 1):
    parent[i] = i

for i in range(N):
    for j in range(N): 
        if arr[i][j]: 
            union_parent(parent, i + 1, j + 1)

tf = 'YES' 
for i in range(0, M):
    if find_parent(parent, path[i]) != find_parent(parent, path[i+1]): 
        tf = 'NO'
        break 
print(tf)





