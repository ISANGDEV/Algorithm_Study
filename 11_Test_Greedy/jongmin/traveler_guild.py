from collections import deque
N=map(int, input())
traveler=list(map(int, input().split()))
traveler.sort()
tq=deque(traveler)
result=0
status=True
while tq:
    traveler1=tq.popleft()
    if(len(tq)<traveler1):
        break
    for i in range(traveler1-1):
        if(len(tq)==0):
            status=False
            break
        tq.popleft()
    if(status):
        result+=1
print(result)