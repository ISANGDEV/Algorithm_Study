N,M=map(int, input().split())

OPERATION_MERGE_TEAM=0
OPERATION_CHECK_SAME_TEAM=1

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
    operation,teamOne, teamTwo=map(int, input().split())
    if(operation==OPERATION_MERGE_TEAM):
        union(parents, teamOne, teamTwo)
    elif(operation==OPERATION_CHECK_SAME_TEAM):
        if(find(parents,teamOne)!=find(parents,teamTwo)):
            print('NO')
        else:
            print('YES')
    else:
        raise Exception("Not Valid Operation: "+str(operation))