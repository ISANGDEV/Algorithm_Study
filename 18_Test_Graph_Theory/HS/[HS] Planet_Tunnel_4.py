import sys

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])

    return parent[x]

def union_find(parent,a,b):
    a_p = find_parent(parent,a)
    b_p = find_parent(parent,b)

    if a_p < b_p:
        parent[b_p] = a_p
    else:
        parent[a_p] = b_p

n = int(sys.stdin.readline())

parent = [0] * (n+1)
result = 0

for i in range(1,n+1):
    parent[i] = i
planet_x = []
planet_y = []
planet_z = []

for i in range(n):
    a,b,c = map(int,sys.stdin.readline().split())
    planet_x.append([a,i])
    planet_y.append([b,i])
    planet_z.append([c,i])

planet_x.sort()
planet_y.sort()
planet_z.sort()

edges = []
for i in range(n-1):
    edges.append([planet_x[i + 1][0] - planet_x[i][0], planet_x[i][1], planet_x[i + 1][1]])
    edges.append([planet_y[i + 1][0] - planet_y[i][0], planet_y[i][1], planet_y[i + 1][1]])
    edges.append([planet_z[i + 1][0] - planet_z[i][0], planet_z[i][1], planet_z[i + 1][1]])

edges.sort()

for cost,a,b in edges:

    if find_parent(parent,a) != find_parent(parent,b):
        union_find(parent,a,b)
        result += cost

print(result)
