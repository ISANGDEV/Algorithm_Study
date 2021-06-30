import sys
input = sys.stdin.readline

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

n, m = map(int, input().split())

parent = [0 for _ in range(n+1)]
for i in range(n+1):
    parent[i] = i

vertexs = []

for _ in range(m):
    a, b, c = map(int, input().split())
    vertexs.append((c, (a,b)))
vertexs.sort()

result = 0
last = 0
for vertex in vertexs:
    distance, edge = vertex
    if find_parent(parent, edge[0]) != find_parent(parent, edge[1]):
        union_parent(parent, edge[0], edge[1])
        result += distance
        last = distance
result -= last
print(result)