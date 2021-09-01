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

parent = [0 for _ in range(n)]

for i in range(n):
    parent[i] = i

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            union_parent(parent, i, j)

cities = list(set(map(int, input().split())))
root = find_parent(parent, cities[0])
can = True
for city in cities:
    if root != find_parent(parent, city):
        can = False
        break
if can:
    print("YES")
else:
    print("NO")