# 다시 풀기
import sys
n,d = map(int,sys.stdin.readline().split())
geo = []

for i in range(n):
    a,b,c = map(int,sys.stdin.readline().split())
    if b - a <= c:
        continue
    if b > d :
        continue
    geo.append([a,b,c])

distance = [i for i in range(d+1)]

for i in range(len(distance)):
    if i > 0:
        distance[i] = min(distance[i], distance[i-1]+1)
    for a,b,c in geo:
        if i == a and distance[i] + c < distance[b]:
            #갈 수 있는 지름길이 있고,
            distance[b] = distance[i] + c

print(distance[d])
