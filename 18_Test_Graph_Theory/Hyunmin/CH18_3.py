N, M = list(map(int, input().split()))

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

parent = [0] * (N + 1)  

edges = []
result = 0

for i in range(1, N + 1):
    parent[i] = i

for _ in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
    else: 
        result += cost  # 사이클일 발생할 경우 == 절약할수 있는 금액, 비활성화한 가로등의 cost를 result에 추가 
print(result)


