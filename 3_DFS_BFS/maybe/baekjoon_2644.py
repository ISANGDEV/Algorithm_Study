from collections import deque


numberOfPeople = int(input())
p1, p2 = map(int, input().split())
relations = int(input())

graph = [[] for _ in range(numberOfPeople + 1)]
for _ in range(relations):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

distance = [-1] * (numberOfPeople + 1)
q = deque()
q.append(p1)
distance[p1] = 0

while q:
    v = q.popleft()
    if v == p2:
        print(distance[v])
        break
    for i in graph[v]:
        if distance[i] < 0:
            q.append(i)
            distance[i] = distance[v] + 1
else:
    print(-1)


