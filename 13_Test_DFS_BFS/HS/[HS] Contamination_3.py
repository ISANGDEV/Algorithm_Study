import sys
from collections import deque
def bfs(s,x,y):
    q = deque(virus)
    time = 0

    while q :
        if time == s:
            break
        for i in range(len(q)): # 이것도 중요한 점 for 문 써서 같은 시간대 바이러스만 증식
            temp,a,b = q.popleft()
            for c,d in vec:
                nx = a + c
                ny = b + d
                if 0 <= nx < n and 0 <= ny < n :
                    if geo[nx][ny] == 0:
                        geo[nx][ny] = temp # 이전 값으로 감염
                        q.append((geo[nx][ny],nx,ny))
        time+=1
    return geo[x-1][y-1] # 첫번쨰점이 1,1

n,k = map(int,sys.stdin.readline().split())
geo = []
virus = []
vec = [[-1,0],[1,0],[0,1],[0,-1]]

for i in range(n):
    geo.append(list(map(int,sys.stdin.readline().split())))
    for j in range(n):
        if geo[i][j] != 0 :
            virus.append((geo[i][j],i,j))

s,x,y = map(int,sys.stdin.readline().split())

virus.sort() # 첫번째만 정렬을 해주면 그 이후는 자연스럽게 신경 쓸 필요가 없지
print(bfs(s,x,y))

















"""
def bfs(x,y,time,geo):
    vector = [[-1,0],[1,0],[0,1],[0,-1]]
    if geo[x][y][0] == 0 :
        return
    if x
    que = deque()
    que.append([x,y])
    while que:
        a,b = que.popleft()

        for c,d in vector:
            if geo[a+c][b+d][0] == 0:
                geo[a+c][b+d][0] = geo[a][b][0]
                geo[a+c][b+d][1] = time + 1




n, k = map(int,sys.stdin.readline().split())
geo = []
for i in range(n):
    temp = list(map(list,sys.stdin.readline().split()))
    geo.append(temp)
s,x,y = map(int,sys.stdin.readline().split())


# 순서대로??,, 일단 전체 맵에다가 차원 하나 추가 시켜서 횟수를 넣는게  생각이 남
근데 200*200*10000하면 너무 커져서 이거 안될듯





if geo[x][y] == 0 :
    print(0)
else:
    print(geo[x][y])

"""