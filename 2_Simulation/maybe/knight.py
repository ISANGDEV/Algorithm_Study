a = list(input(''))
x = ord(a[0]) - ord('a')
y = int(a[1]) - 1

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

cnt = 0
for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or ny < 0 or nx > 7 or nx > 7:
        continue
    cnt += 1

print(cnt)
