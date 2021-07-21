import sys
from collections import deque
def bfs(a,visit,geo,number,level):
    que = deque()
    que.append([a,number])
    visit[a] = True
    while que:
        x,y = que.popleft()
        level[x] = y
        for i in geo[x]:
            if visit[i] != True:
                que.append([i,y+1])
                visit[i] = True

n,m,k,x = map(int,sys.stdin.readline().split())
geo = [[] for i in range(n+1)]
visit = [False] * (n+1)
level = [0] * (n+1)

for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    geo[a].append(b)

bfs(x,visit,geo,0,level)
result = []

for i in range(len(level)):
    if level[i] == k:
        result.append(i)

if len(result) == 0:
    print(-1)

else:
    for i in result:
        print(i)