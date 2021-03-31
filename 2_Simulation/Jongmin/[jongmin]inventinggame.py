N,M=map(int,input().split())
A,B,d=map(int,input().split())
gamemap=[]
visited=[[False]*M for i in range(N)]
visited[A][B]=True
for i in range(N):
    gamemap.append(list(map(int,input().split())))
result=1
directions=[0,3,2,1]
godir=[[-1,0],[0,-1],[1,0],[0,1]]
def nextdirection(nowdir):
    pos=directions.index(nowdir)
    pos=(pos+1)%len(directions)
    return directions[pos]
while(True):
    savedD=d
    st=True
    for i in range(len(directions)):
        d=nextdirection(d)
        movey,movex=godir[d]
        nexty=A+movey
        nextx=B+movex
        if(visited[nexty][nextx]==False and gamemap[nexty][nextx]==0):
            A=nexty
            B=nextx
            visited[A][B]=True
            result+=1
            st=False
    if(st):
        nexty=A-godir[d][0]
        nextx=B-godir[d][1]
        if (visited[nexty][nextx] == False and gamemap[nexty][nextx] == 0):
            A = nexty
            B = nextx
            visited[A][B] = True
            result+=1
        else:
            break
print(result)