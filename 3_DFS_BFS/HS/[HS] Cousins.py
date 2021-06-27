from collections import deque

def bfs(relation,q,w,visited):
    que = deque()
    count = 0
    que.append((q,count)) # 2개 추가 할 때 괄호..
    visited[q] = 1
    while que:
        x,y = que.popleft()
        for i in relation[x]:
            if visited[i] != 1 :
                if i == w :
                    return y+1
                que.append((i,y+1))
                visited[i] = 1

    return -1

relation = {}
n = int(input("전체 사람 수"))
p,q = map(int,input("계산 대상 번호").split())
m = int(input("관계 개수"))
visited = [0] * (n+1)
for i in range(m):
    a, b = map(int,input("관계 정보 입력").split())
    if a in relation.keys():
        relation[a].add(b)
    else:
        relation[a] = set([b])

    if b in relation.keys():
        relation[b].add(a)

    else:
        relation[b] = set([a])

answer = bfs(relation,p, q, visited)

print(answer)
