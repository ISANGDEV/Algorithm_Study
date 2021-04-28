import sys
from collections import deque
def bfs(dictionary, q, w):
    que = deque()
    count = 0
    que.append([q,count])
    visited = [0] * (n+1)
    visited[q] = 1
    while que:
        a,b = que.popleft()
        
        if a == w:
            return b
        for i in dictionary[a]:
            if visited[i] != 1:
                que.append([i,b+1])
                visited[i] = 1
    return -1

n = int(sys.stdin.readline()) # 전체 사람
q, w = map(int,sys.stdin.readline().split()) # 관계 대상
m = int(sys.stdin.readline()) # 관계 개수
dictionary = {}

for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    if x in dictionary.keys():
        dictionary[x].append(y)
    elif x not in dictionary.keys():
        dictionary[x] = [y]

    if y in dictionary.keys():
        dictionary[y].append(x)
    elif y not in dictionary.keys():
        dictionary[y] = [x]

print(bfs(dictionary,q,w))
