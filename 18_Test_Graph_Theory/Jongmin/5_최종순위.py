#틀림
from collections import deque
T=int(input())

for t in range(T):
    n=int(input())
    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n + 1)
    ranks=list(map(int,input().split()))
    for r in range(len(ranks)-1):
        graph[ranks[r]].append(ranks[r+1])
        indegree[ranks[r+1]]+=1
    m=int(input())
    for j in range(m):
        a,b=map(int,input().split())
        graph[a],graph[b]=graph[b],graph[a]
        indegree[a],indegree[b]=indegree[b],indegree[a]
    q=deque()
    for i in range(1,len(indegree)):
        if(indegree[i]==0):
            q.append(i)
    result = []
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    for i in result:
        print(i, end=' ')
    print()