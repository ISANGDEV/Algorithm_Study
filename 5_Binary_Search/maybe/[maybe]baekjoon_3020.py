n, h = map(int, input().split())

UpObstacle = []
DownObstacle = []
for _ in range(n//2):
    UpObstacle.append(int(input()))
    DownObstacle.append(int(input()))

s = 0
e = h

while s < e:
    m = (s + e) // 2
    