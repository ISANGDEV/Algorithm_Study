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

g = int(input())
p = int(input())

parent = [0] * (g+1)
for i in range(g+1):
    parent[i] = i

k = []
for _ in range(p):
    k.append(int(input()))

result = 0
for i in k:
    r = find_parent(parent, i)
    if r != 0:
        result += 1
        union_parent(parent, r, r-1)
    else:
        break

print(result)