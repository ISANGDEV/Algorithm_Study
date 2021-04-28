from collections import deque

ddx = [1,-1,0,0]
ddy = [0,0,1,-1]

t = int(input())

count = [0 for i in range(t)]

for i in range(t):
    m, n, k = map(int, input().split())
    farm = [[0]*n for j in range(m)]
    queue = deque()
    for _ in range(k):
        x, y = map(int, input().split())
        farm[x][y] = 1
    for dx in range(m):
        for dy in range(n):
            if farm[dx][dy] == 0:
                pass
            else:
                count[i] += 1
                queue.append((dx, dy))
                farm[dx][dy] = 0
                while queue:
                    samplex, sampley = queue.popleft()
                    for a in range(4):
                        try:
                            aroundx = samplex+ddx[a]
                            aroundy = sampley+ddy[a]
                            if aroundx < 0 or aroundy < 0:
                                raise IndexError
                            if farm[aroundx][aroundy] == 1:
                                queue.append((aroundx, aroundy))
                                farm[aroundx][aroundy] = 0
                        except IndexError:
                            continue

for i in count:
    print(i)