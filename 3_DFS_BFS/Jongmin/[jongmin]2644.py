from collections import deque
n=int(input())
a,b=map(int,input().split())
m=int(input())
graph=[[] for i in range(n+1)]
for i in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
q=deque()
q.append([a,0])
cnt=0
visited=[False for i in range(n+1)]
visited[a]=True
result=True
while q:
    x,cnt=q.popleft()
    if(x==b):
        print(cnt)
        result=False
        break
    for j in graph[x]:
        if(visited[j]==False):
            q.append([j,cnt+1])
            visited[j]=True
if(result):
    print(-1)
