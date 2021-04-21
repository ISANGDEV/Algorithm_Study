from collections import deque
import sys


def bfs(n,m):
    global geo
    dxdy = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
    que = deque()
    que.append((n,m))
    geo[n][m] = 0
    while que:
        x, y = que.popleft()
        for i, j in dxdy:
            dx = x + i
            dy = y + j
            if dx >=0 and dx < h and dy >= 0 and dy < w:
                if geo[dx][dy] == 1:
                    geo[dx][dy] = 0
                    que.append((dx,dy))



while True:
    geo = []
    count = 0
    w,h = map(int,sys.stdin.readline().split())

    if w == 0 and h == 0 :
        break
    for i in range(h):
        geo.append(list(map(int,sys.stdin.readline().split())))

    for i in range(h):
        for j in range(w):
            if geo[i][j] == 1:
                count += 1
                bfs(i,j)



    print(count)
