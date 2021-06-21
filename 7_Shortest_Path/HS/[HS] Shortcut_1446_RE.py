import sys
n,d = map(int,sys.stdin.readline().split())
# n은 지름길 수 d는 목적지 까지의 거리
line = []

for i in range(n):
    temp = list(map(int,sys.stdin.readline().split()))
    if temp[1] - temp[0] <= temp[2]:
        continue
    if temp[1] > d:
        continue
    line.append(temp)

distance = [i for i in range(d+1)]


for i in range(d+1):
    if i != 0 :
        distance[i] = min(distance[i],distance[i-1] + 1)

    for a,b,c in line:
        if a == i and distance[i] + c < distance[b]:
            distance[a] = distance[i] + c


print(distance[d])



