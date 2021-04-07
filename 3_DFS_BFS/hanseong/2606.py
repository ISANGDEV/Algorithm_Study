from collections import deque

#입력받기 
n=int(input())
m=int(input())
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

dfs(graph,1,visit)
print((len(dfs_list)-1))


    
    
