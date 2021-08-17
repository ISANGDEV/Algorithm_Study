import sys
import heapq
vec =[[-1,0],[0,-1],[1,0],[0,1]]
inf = int(1e9)
t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    geo = []
    for i in range(n):
        temp = list(map(int,sys.stdin.readline().split()))
        geo.append(temp)
    # 2차원 배열 입력 받기
    # 0,0 -> -1,-1 특정점에서 특정점으로 이동하는거니까 다익스트라 알고리즘 사용

    distance = [[inf] * n for i in range(n)] # 거리 모두 무제한으로 설정 / 노드가 일반 배열이 아니라 2차원이니까 거리테이블도 2차원.
    distance[0][0] = geo[0][0] # 시작점은 거리 0 인줄 알았는데 해답 풀이 보니까 그 시작하는 지점 비용도 포함해야함. 그니까 첫점 일치 시켜주고
    x,y = 0,0
    q = [[geo[x][y],x,y]] # 비용이랑, 위치 xy값 담아주고

    while q : # heap으로 다익스트라 쓰면
        cost,x,y = heapq.heappop(q)
        if distance[x][y] < cost: #
            continue
        for a,b in vec:
            nx = x + a
            ny = y + b
            if 0 <= nx < n and 0<= ny < n :
                temp = cost + geo[nx][ny]
                if temp < distance[nx][ny]:
                    distance[nx][ny] = temp
                    heapq.heappush(q,[temp,nx,ny])

print(distance[-1][-1])




