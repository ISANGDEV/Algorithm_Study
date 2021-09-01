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

n = int(input())

parent = [0] * n
edges = []
xList = []
yList = []
zList = []

for i in range(n):
    x, y, z = map(int, input().split())
    xList.append((x, i))
    yList.append((y, i))
    zList.append((z, i))
    parent[i] = i

xList.sort()
yList.sort()
zList.sort()

for i in range(1, n):
    edges.append((xList[i][0] - xList[i-1][0], xList[i-1][1], xList[i][1]))
    edges.append((yList[i][0] - yList[i-1][0], yList[i-1][1], yList[i][1]))
    edges.append((zList[i][0] - zList[i-1][0], zList[i-1][1], zList[i][1]))

result = 0
edges.sort()
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        
print(result)