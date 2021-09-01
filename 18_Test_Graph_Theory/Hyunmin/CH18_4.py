N = int(input())

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

# x, y, z 의 cost를 좌표 당 각각 더하는 것과 x,y,z 행성의 모든 경우의 수를 구하나 같다 
x, y, z = [], [], [] 
for i in range(1, N + 1):
    a, b, c = list(map(int, input().split()))
    # i는 각 좌표의 몇번째에서 몇번째로 갔는지 표시하기 위해 필요 
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))

x.sort()
y.sort()
z.sort() 

for i in range(0, N-1):  # i + 1 사용하므로 N 전까지 
    edges.append((abs(x[i+1][0] - x[i][0]), x[i+1][1], x[i][1]))  # x cost, 출발 a, 도착 b 
    edges.append((abs(y[i+1][0] - y[i][0]), y[i+1][1], y[i][1]))  # y cost, 출발 a, 도착 b 
    edges.append((abs(z[i+1][0] - z[i][0]), z[i+1][1], z[i][1]))  # z cost, 출발 a, 도착 b 
edges.sort()


result = 0
for edge in edges:
    cost, a, b = edge 

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost 
print(result)


 
