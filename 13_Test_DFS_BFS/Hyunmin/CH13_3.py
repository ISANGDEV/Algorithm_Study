from collections import deque
import heapq

n, k = map(int, input().rstrip().split())

arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
s, x, y = map(int, input().rstrip().split())

q = []
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    q_length = len(q)
    for _ in range(q_length):
        vi, i, j = q.popleft()
        for l in range(4):
            ni = i + dx[l]
            nj = j + dy[l]

            if ni < 0 or nj < 0 or ni >= n or nj >= n:
                continue
            if arr[ni][nj] > 0:
                continue

            arr[ni][nj] = vi
            q.append([vi, ni, nj])


# 바이러스 번호가 중복 가능이라고 가정
k_list = []
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            k_list.append([arr[i][j], i, j])  # k, x, y


# heapq.heapify(k_list)
k_list.sort(key=lambda l: l[0])  # default 가 [0]일수도
q = deque(k_list)  # 글로벌 큐

done = False
if s == 0:
    print(arr[x - 1][y - 1])
    done = True
else:
    for sec in range(1, s + 1):
        bfs()
        if arr[x - 1][y - 1]:
            done = True
            print(arr[x - 1][y - 1])
            break
if not done:
    print(0)


