from collections import deque


numberOfTests = input()
testCases = []

for i in range(len(numberOfTests)):
    factors = list(map(int, input().split()))
    farm = [[0]*factors[0] for _ in range(factors[1])]
    for j in range(factors[2]):
        coordinates = list(map(int, input().split()))
        farm[coordinates[1]][coordinates[0]] = 1
    testCases.append(farm)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
result = 0

for i in range(len(testCases)):
    xlen = len(testCases[i][0])
    ylen = len(testCases[i])
    for j in range(ylen):
        for k in range(xlen):
            if testCases[i][j][k] == 1:
                result += 1
                q = deque()
                q.append((j, k))
                while q:
                    y, x = q.popleft()
                    testCases[i][y][x] = 0
                    for l in range(len(dx)):
                        xpos = x + dx[l]
                        ypos = y + dy[l]
                        if 0 <= xpos < xlen and 0 <= ypos < ylen and testCases[i][ypos][xpos]==1:
                            q.append((ypos, xpos))

print(result)





