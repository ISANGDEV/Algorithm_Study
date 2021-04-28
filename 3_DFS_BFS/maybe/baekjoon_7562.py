from collections import deque


numberOfCases = int(input())

for i in range(numberOfCases):
    boardSize = int(input())
    start = list(map(int, input().split()))
    destination = list(map(int, input().split()))
    graph = [[-1] * boardSize for _ in range(boardSize)]
    distance = 0

    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [-1, 1, -2, 2, -2, 2, -1, 1]

    graph[start[1]][start[0]] = 0
    q = deque()
    q.append([start[1], start[0]])
    while q:
        y, x = q.popleft()
        if x == destination[0] and y == destination[1]:
            print(graph[y][x])
            break
        for j in range(len(dx)):
            xpos = x + dx[j]
            ypos = y + dy[j]
            if 0 <= xpos < boardSize and 0 <= ypos < boardSize and graph[ypos][xpos] < 0:
                q.append([ypos, xpos])
                graph[ypos][xpos] = graph[y][x] + 1
