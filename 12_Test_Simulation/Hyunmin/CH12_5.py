d = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # 튜플사용, 우회전 시 = 남 -> 서 -> 북 -> 동


def turn(c, idx):
    if c == "D":
        idx += 1
    else:
        idx -= 1
    if idx > 3:
        idx = 0
    if idx < 0:
        idx = 3
    return idx


n = int(input())  # 보드의 크기
k = int(input())  # 사과

map_arr = [[0] * (n + 1) for _ in range(n + 1)]  # 1,1이 시작점이 되어야해서 더미 추가

for _ in range(k):
    i, j = map(int, input().rstrip().split())
    map_arr[i][j] = 2  # 2는 사과

line = int(input())
lines = []
for _ in range(line):
    x, c = input().rstrip().split()
    x = int(x)
    lines.append((x, c))  # x 오름차순 저장

idx = 3  # d[] 의 idx 처음에 동쪽이니까 3으로 설정
i = 1
j = 1
sec = 0
tail = []

while True:

    tail.append((i, j))  # 제거할 때 사용하기 위해 tail 에 추가
    map_arr[i][j] = 1  # 꼬리 방문

    i = i + d[idx][0]
    j = j + d[idx][1]

    if i < 1 or i >= n + 1 or j < 1 or j >= n + 1:
        break
    if map_arr[i][j] == 1:
        break

    if map_arr[i][j] == 2:  # is apple
        map_arr[i][j] = 1
    else:
        prev = tail.pop(0)
        map_arr[prev[0]][prev[1]] = 0
        map_arr[i][j] = 1
        # 꼬리 삭제
    sec += 1  # 1초 완료 했다.
    for x in lines:
        if x[0] == sec:  # 방향 전환
            idx = turn(x[1], idx)
            break
        if sec < x[0]:
            break

print(sec+1)

