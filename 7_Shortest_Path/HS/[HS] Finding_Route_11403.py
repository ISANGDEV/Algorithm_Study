import sys

infi = 9999

n = int(sys.stdin.readline())

geo = []

for i in range(n):
    geo.append(list(map(int,sys.stdin.readline().split())))

for i in range(n):
    for j in range(n):
        if geo[i][j] == 0:
            geo[i][j] = infi

for k in range(n):
    for a in range(n):
        for b in range(n):
            geo[a][b] = min(geo[a][b], geo[a][k] + geo[k][b])

result = []
for i in range(n):
    temp = []
    for j in range(n):
        if geo[i][j] == infi:
            temp.append(0)
        else:
            temp.append(1)
    result.append(temp)


for i in range(n):
    print(result[i])
