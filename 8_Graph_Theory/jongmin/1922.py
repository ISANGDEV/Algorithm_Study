N=int(input())
M=int(input())
edges=[]
parents=[i for i in range(N+1)]

def find(parent, x):
    if parent[x] != x:
        return find(parent, parent[x])
    return x


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(M):
    computerOne, computerTwo, cost=map(int, input().split())
    edges.append([cost, computerOne,computerTwo])
edges.sort(key=lambda x:x[0])

result=0
for e in edges:
    cost, computerOne,computerTwo=e
    if(find(parents,computerOne)!=find(parents,computerTwo)):
        union(parents,computerOne,computerTwo)
        result+=cost
print(result)
