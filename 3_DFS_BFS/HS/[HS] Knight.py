import sys
from collections import deque

def knight(x_n,y_n):
    to_go = [[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1],[-1,2]]
    que = deque()
    que.append([x_n,y_n])
    while que:
        pos = que.popleft()
        if [pos[0],pos[1]] == [x_t,y_t]:
            return geo[x_t][y_t]
        for i,j in to_go:
            if pos[0] + i >= 0  and pos[0] + i < length and pos[1] + j >= 0 and pos[1] + j < length:
                if geo[pos[0] + i][pos[1] + j] == 0:
                    geo[pos[0] + i][pos[1] + j] = geo[pos[0]][pos[1]] + 1
                    que.append([pos[0]+i,pos[1]+j])




m = int(sys.stdin.readline())

for i in range(m):
    length = int(sys.stdin.readline())
    x_n, y_n = map(int,sys.stdin.readline().split())
    x_t, y_t = map(int,sys.stdin.readline().split())
    if x_n == x_t and y_n == y_t:
        print(0)
        continue
    geo = [[0 for i in range(length)] for j in range(length)]
    print(knight(x_n,y_n))

