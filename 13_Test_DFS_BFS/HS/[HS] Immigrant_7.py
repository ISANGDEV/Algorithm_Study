import sys
from collections import deque

def bfs(x,y,day,geo_1,geo_2,n):
    global visit
    
    save_pos = []
    visit_temp = [[0 for i in range(n)] for j in range(n)]
    if day % 2 == 0:
        que = deque()
        count = 1
        que.append([x,y])
        temp = geo_1[x][y]
        visit[x][y] = 1
        visit_temp[x][y] = 1

        while que:

            a,b = que.popleft()
            for i,j in vec:
                new_x = a + i
                new_y = b + j
                if 0<= new_x < n and 0 <= new_y < n :
                    if l<= abs(geo_1[a][b] - geo_1[new_x][new_y]) <=r and visit_temp[new_x][new_y] == 0:
                        que.append([new_x,new_y])
                        count += 1
                        temp += geo_1[new_x][new_y]
                        visit[new_x][new_y] = 1
                        visit_temp[new_x][new_y] = 1
        if count == 1:
            return count


        for i in range(n):
            for j in range(n):
                if visit_temp[i][j] == 1:
                    geo_2[i][j] = temp // count

        return count

    elif day % 2 == 1:
        que = deque()
        count = 1
        que.append([x,y])
        temp = geo_2[x][y]
        visit[x][y] = 1
        visit_temp[x][y] = 1

        while que:
            a,b = que.popleft()
            for i,j in vec:
                new_x = a + i
                new_y = b + j
                if 0<= new_x < n and 0 <= new_y < n :
                    if (l <= abs(geo_2[a][b] - geo_2[new_x][new_y]) <= r) and (visit_temp[new_x][new_y] == 0):
                        que.append([new_x,new_y])
                        count += 1
                        temp += geo_2[new_x][new_y]
                        visit[new_x][new_y] = 1
                        visit_temp[new_x][new_y] = 1
        if count == 1:
            return count
        
        for i in range(n):
            for j in range(n):
                if visit_temp[i][j] == 1:
                    geo_1[i][j] = temp // count

        return count


n,l,r = map(int, sys.stdin.readline().split())
vec = [[-1,0],[1,0],[0,1],[0,-1]]
geo_1 = []
geo_2 = []
day = 0

for i in range(n):
   geo_1.append(list(map(int,sys.stdin.readline().split())))

while 1:
    visit = [[0 for i in range(n)] for j in range(n)]
    temp = 0

    if day % 2 == 0:
        geo_2 = [item[:] for item in geo_1]

        for i in range(n):
            for j in range(n):
                if visit[i][j] == 1:
                    temp += 1
                else:
                    temp += bfs(i, j, day, geo_1,geo_2,n)

    elif day % 2 == 1:
        geo_1 = [item[:] for item in geo_2]
        for i in range(n):
            for j in range(n):
                if visit[i][j] == 1:
                    temp += 1
                else:
                    temp += bfs(i, j, day, geo_1,geo_2,n)
    if temp == n*n:
        break
    elif temp != n*n:
        day += 1

print(day)
