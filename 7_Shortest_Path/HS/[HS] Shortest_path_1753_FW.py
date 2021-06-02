#메모리 초과, 다익스트라로 해야할 듯
import sys
inf = int(1e9)
v,e = map(int,sys.stdin.readline().split())

start_num = int(sys.stdin.readline())
line = []
table = [[inf] * (v+1) for i in range(v+1)]
for i in range(e):
    temp = list(map(int,sys.stdin.readline().split()))
    line.append(temp)
# 자기 자신까지 거리는 0
for a in range(1,v+1):
    for b in range(1,v+1):
        if a == b:
            table[a][b] = 0
# 지름길 있으면 입력해줌
# #서로 다른 두 정점 사이에 여러개 간선 있다고 했으니까 그 중 최소
for a,b,c in line:
    table[a][b] = min(table[a][b],c)

for k in range(1,v+1):
    for a in range(1,v+1):
        for b in range(1,v+1):
            table[a][b] = min(table[a][b],table[a][k] + table[k][b])
result = []
for i in range(1,v+1):
    if table[start_num][i] == inf:
        result.append("INF")
        continue
    if start_num == i :
        result.append(0)
        continue
    result.append(table[start_num][i])

for i in result:
    print(i)
