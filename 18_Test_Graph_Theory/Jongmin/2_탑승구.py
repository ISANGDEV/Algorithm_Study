#답 봄
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
G=int(input())
P=int(input())
parents = [i for i in range(G+1)]
cnt=0
for i in range(P):
    a=int(input())
    f=find(parents,a)
    if(f==find(parents,0)):
        break
    else:
        union(parents,f,f-1)
        cnt+=1
print(cnt)