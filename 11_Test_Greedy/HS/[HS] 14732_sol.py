import sys
n = int (sys.stdin.readline())
geo = []
max_x = 0
max_y = 0
min_x = 0
min_y = 0

for i in range(n):
    temp = list(map(int,sys.stdin.readline().split()))
    geo.append(temp)
    max_x = max(max_x,temp[2])
    max_y = max(max_y,temp[3])
    min_x = min(min_x,temp[0])
    min_y = min(min_y,temp[1])

h = max_y - min_y
l = max_x - min_x
square = [[0 for i in range(l)] for j in range(h)]
for a in range(h):
    for b in range(l):
        for q,w,e,r in geo: #q,w 왼쪽 아래 e,r 오른쪽 위
            if b >= q - min_x and b < e - min_x and a < h-w+min_y and a >= h-r+min_y:
                square[a][b] = 1
                break
result = 0
for a in range(h):
    for b in range(l):
        if square[a][b] == 1:
            result += 1
print(result)