import sys

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])

    return parent[x]

def union_parent(parent,a,b):
    a_p = find_parent(parent,a)
    b_p = find_parent(parent,b)

    if a_p < b_p :
        parent[b_p] = a_p
    else:
        parent[a_p] = b_p


g = int(sys.stdin.readline()) # 탑승구 숫자
p = int(sys.stdin.readline()) # 비행기 숫자
parent = [0] * (g+1)
result = 0
for i in range(1,g+1): # 자기는 자신의 부모.
    parent[i] = i

for i in range(p):
    temp = find_parent(parent,int(sys.stdin.readline()))
    if temp == 0 :
        break
    else:
        union_parent(parent,temp,temp-1)
        result += 1

print(result) # 도킹할 수 있는 최대 비행기 개수. + 순서대로 도킹해야함.


