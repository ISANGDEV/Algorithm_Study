import sys

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])

    return parent[x]

def union_parent(parent,a,b):
    a_p = find_parent(parent,a)
    b_p = find_parent(parent,b)
    if a < b :
        parent[b_p] = a_p
    else:
        parent[a_p] = b_p

n,m = map(int,sys.stdin.readline().split())
# n 집의수 / m 도로 수
road = []
parent = [0] * (n)
temp = 0
result = 0
for i in range(n):
    parent[i] = i

for i in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    road.append([c,a,b])

road.sort() # 최대로 절약해야하니까 정렬 하고

for cost,a,b in road:
    temp += cost # 전체 간선 비용
    if find_parent(parent,a) != find_parent(parent,b): # 사이클이 없으면
        # 합쳐서
        union_parent(parent,a,b)
        result += cost
        # 필요한 것.

print(temp - result)

# 전체 - 필요한것 = 불필요한 것
# 일부 가로등을 비 활성화하여 절약할 수 있는 최대 금액 출력