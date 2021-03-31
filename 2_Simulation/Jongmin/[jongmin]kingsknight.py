position=input()
alphamap='abcdefgh'
N=8
directions=[[2,1],[2,-1],[-2,1],[2,-1],[1,2],[-1,2],[1,-2],[-1,-2]]
answer=0
for direction in directions:
    xmove,ymove=direction
    nextx=alphamap.index(position[0])+xmove
    nexty=int(position[1])-1+ymove
    if(0<=nextx<N and 0<=nexty<N):
        answer+=1
print(answer)