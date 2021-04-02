from collections import deque

#입력받기 
n, m, v=map(int, input().split())
graph=[[] for _ in range(n+1)]
visit=[False]*(n+1)

for i in range(m):
    a, b= map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


for i in range(n):
    graph[i].sort()

#dfs 
dfs_list=[]
def dfs(graph, v, visit):
    visit[v]=True
    dfs_list.append(v)

    for i in graph[v]:
        if not visit[i]:
            dfs(graph, i, visit)

dfs(graph,v,visit)
print(dfs_list)


#bfs
visit=[False]*(n+1)
bfs_list=[]
def bfs(graph, v, visit):
    queue=deque([v])

    visit[v]=True

    while queue:
        v=queue.popleft()
        bfs_list.append(v)

        for i in graph[v]:
            if not visit[i]:
                queue.append(i)
                visit[i]=True
bfs(graph, v, visit)
print(bfs_list)
    
    
