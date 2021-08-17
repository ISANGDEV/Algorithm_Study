import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

inf = int(1e9)

cost = [[inf] * (n) for i in range(n)]
#s = [[inf] * n for i in range(n)]

for i in range(n): # 자기 자신으로 가는 비용은 0
    for j in range(n):
        if i == j:
            cost[i][j] = 0

# a b c : a에서 b로 가는데 c만큼 비용이 듭니다.
for i in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    cost[a-1][b-1] = min(c, cost[a-1][b-1])
    # 최종 비용 = 최소(버스가 다니는 길, 기존 비용 테이블에 기록된 비용)

for i in range(n):
    for j in range(n):
        for k in range(n):
            cost[j][k] = min(cost[j][k], cost[j][i] + cost[i][k])

for i in range(n):
    temp = []
    for j in range(n):
        if cost[i][j] == inf:
            print(0,end = " ")
        else:
            print(cost[i][j], end = " ")

    print()



