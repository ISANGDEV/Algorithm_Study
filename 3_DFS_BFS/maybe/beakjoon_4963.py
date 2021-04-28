w, h = map(int, input().split())

graph = []

for i in range(h):
    landscape = list(map(int, input().split()))
    graph.append(landscape)

dx = [-1, -1, -1, 1, 1, 1, 0, 0]
dy = [-1, 0, 1, -1, 0, 1, -1, 1]
result = 0

for i in range(h):
    for j in range(w):
        stack = [[i, j]]
        if graph[i][j] == 1:
            result += 1
            while stack:
                y, x = stack.pop()
                graph[y][x] = 0
                for k in range(len(dx)):
                    xpos = x + dx[k]
                    ypos = y + dy[k]
                    if 0 <= xpos < w and 0 <= ypos < h and graph[ypos][xpos] == 1:
                        stack.append([ypos, xpos])

print(result)
