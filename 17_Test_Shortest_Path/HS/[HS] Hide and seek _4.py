import sys
import heapq
inf = int(1e9)
# 노드개수 간선 개수

n,m = map(int, sys.stdin.readline().split())
start = 1

geo = [[] for i in range(n+1)] # 비용 정보 기록 테이블
distance = [inf] * (n+1)

distance[1] = 0 # 시작점은 거리 0

for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    geo[a].append([b,1])
    geo[b].append([a,1])
    # 쌍방으로 갈 수 있음. 길 여부 갱신

def dijkstra(start): # 힙으로 다 익스트라 알고리즘 구현
    q = []
    heapq.heappush(q,[0,start])
    while q:
        cost,now = heapq.heappop(q)
        if distance[now] < cost : # 지금 방문한 노드의 비용이 거리테이블에 기록된 것보다 크면 저장할 필요 없으니까 continue
            continue
        #기록할 가치가 있다면,
        for i in geo[now]: #지금 방문한 노드와 연결된 노드들을 봤을 때
            temp = cost + 1 # 비용 (1) 이니까 원래 기록된 비용 + 1 하고
            if temp < distance[i[0]]: # 이 비용이 갱신 될 수 있으면 (지금 가는 길이 더 비용이 적으면)
                distance[i[0]] = temp # 거리 테이블을 작은 값으로 바꿔주고
                heapq.heappush(q,[temp,i[0]]) # 그 경로로 지나간다

dijkstra(start)

node_max = 0
cost_max = 0
result = []


for i in range(1,n+1):
    if cost_max < distance[i]:
        node_max = i
        cost_max = distance[i]
        result = [node_max]
    elif cost_max == distance[i]:
        result.append(i)

# 가장 최단 거리가 먼 노드 번호 / 그 노드까지의 거리 / 그런 노드가 몇개가 있는지지
print(node_max,cost_max,len(result))
