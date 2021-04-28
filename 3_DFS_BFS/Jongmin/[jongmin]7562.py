from _collections import deque
T=int(input())
dx=[2,1,-1,-2,-2,-1,1,2]
dy=[-1,-2,-2,-1,1,2,2,1]
for t in range(T):
    l=int(input())
    visited=[[False for a in range(l)] for b in range(l)]
    nowx,nowy=map(int,input().split())
    tox,toy=map(int,input().split())
    q=deque()
    q.append([nowx,nowy,0])
    visited[nowy][nowx]=True
    while q:
        x,y,cnt=q.popleft()
        if(x==tox and y==toy):
            print(cnt)
            break
        for i in range(len(dx)):
            newx=x+dx[i]
            newy=y+dy[i]
            if(0<=newx<l and 0<=newy<l and visited[newy][newx]==False):
                q.append([newx,newy,cnt+1])
                visited[newy][newx]=True
