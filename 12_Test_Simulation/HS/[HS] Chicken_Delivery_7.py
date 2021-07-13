import sys
from itertools import combinations #이거 안 쓰고는 방법이 없나??
n, m = map(int,sys.stdin.readline().split())
# 지도 크기는 n*n

geo = []
chick_dis = 0

house = []
chicken = []

for i in range(n):
    geo.append(list(map(int,sys.stdin.readline().split())))
for i in range(n):
    for j in range(n):
        if geo[i][j] == 1:
            house.append([i+1,j+1])
        elif geo[i][j] == 2 :
            chicken.append([i+1,j+1])


members = combinations(chicken,m)
combi_sum = []

for i in members:
    combi_chicken = list(i)
    diff_list = []

    for a,b in house:
        diff = int(1e9)
        for c,d in combi_chicken:
            diff = min(diff,abs(c-a) + abs(d-b))

        diff_list.append(diff)

    combi_sum.append(sum(diff_list))
print(min(combi_sum))





"""
result = [int(1e9) for i in range(len(house))]
check = 0

for a,b in house:
    for c,d in chicken:
        result[check] = min(result[check], (abs(c-a) + abs(d-b)))
    check += 1
result.sort()
answer = 0
for i in range(m):
    answer += result[i]
print(answer)"""