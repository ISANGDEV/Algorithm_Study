from collections import deque
import sys

n, m, k, x = map(int, sys.stdin.readline().rstrip().split())
city_map = [[] for _ in range(n + 1)]  # 0은 더미
visited = [False] * (n + 1)

def bfs():
    result = []
    visited[x] = True  # 출발지점 -> x
    # q = deque([(x, level)])  # 출발 x요소와 깊이 level 넣으면서 큐 만듬 -> 시간 초과
    # -> level 리스트 생성
    level = [0] * (n + 1)
    q = deque([x])  # 출발 x요소 넣으면서 큐 만듬
    while q:
        t = q.popleft()
        for i in city_map[t]:
            if not visited[i]:
                level[i] = level[t] + 1
                visited[i] = True
                q.append(i)
                if level[i] == k:
                    result.append(i)
    if result:
        result.sort()
        for i in result:
            print(i)
    else:
        print(-1)


for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    city_map[a].append(b)

bfs()

# bfs
# [a, b, level] 최단거리 만났을 때 result 에 append.

