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
def solution(n, costs):
    answer = 0
    parents=[i for i in range(n)]
    costs.sort(key=lambda x:x[2])
    for item in costs:
        a,b,cost=item
        if(find(parents,a)!=find(parents,b)):
            answer+=cost
            union(parents,a,b)
    return answer
print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))