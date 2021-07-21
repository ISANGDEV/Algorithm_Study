import sys
import copy
sys.setrecursionlimit(100000)

n,m = map(int,sys.stdin.readline().split())

graph = [list(map(int,sys.stdin.readline().split())) for i in range(n)]
graph_copy = copy.deepcopy(graph)

vec = [[-1,0],[1,0],[0,1],[0,-1]]
terr = 0

def dfs(x,y,wall):
    wall[x][y] = 2
    for i,j in vec:
        nx,ny = x + i, y + j
        if 0 <= nx < n and 0 <= ny < m:
            if wall[nx][ny] == 0:
                dfs(nx,ny,wall)

def make_wall(st,count):
    global terr

    if count == 3:
        wall = copy.deepcopy(graph_copy)
        for i in range(n):
            for j in range(m):
                if wall[i][j] == 2:
                    dfs(i,j,wall)
        safe_count = sum(i.count(0) for i in wall)
        terr = max(terr,safe_count)
        return
    else:
        for i in range(st,n*m):
            r = i // m
            c = i % m
            if graph_copy[r][c] == 0:
                graph_copy[r][c] = 1
                wall(i,count+1)
                graph_copy[r][c] = 0
wall(0,0)
print(safe_region)