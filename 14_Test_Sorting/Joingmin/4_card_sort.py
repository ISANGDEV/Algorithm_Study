import heapq
N=int(input())
cards=[]
for i in range(N):
    heapq.heappush(cards,int(input()))
result=0
while len(cards)>1:
    a=heapq.heappop(cards)
    b=heapq.heappop(cards)
    heapq.heappush(cards,a+b)
    result+=(a+b)
print(result)