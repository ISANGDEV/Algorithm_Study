import sys



# 사람 3명
#  a는 b보다 낮고 b는 c보다 작다. -> 3명

# 사람 4명
# a는 b보다 높고 a는 c보다 높다. a는 d보다 높다. a는 1등인걸 알고 있음.
# 근데 나머지는 등수 알지 못함. a > bcd

# 한 노드에서 나머지 노드로 모두 갈 수 있으면 등수 알 수 있음.
# 당 양방향이어야함. a -> b, a -> c, a -> d 높은쪽에서 낮은 쪽.


n, m = map(int,sys.stdin.readline().split())

inf = int(1e9)
result = 0
geo = [[inf] * (n+1) for i in range(n+1)]
# 플로이드 와샬 알고리즘. 전체 무한으로 선언  / 1부터 인덱싱하기 위해서 n+1.

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j :
            geo[i][j] = 0
            # 자기 자신까지 거리는 0임.

for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    geo[b][a] = 1
# a,b 는 a < b 라는 의미임
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            geo[j][k] = min(geo[j][k], geo[j][i] + geo[i][k])

for i in range(1,n+1):
    count = 0
    for j in range(1,n+1):
        if (geo[i][j] != inf and geo[i][j] != 0) or geo[j][i] != 0 and geo[j][i] != inf:
            count += 1

    if count == n - 1:
        result += 1

print(result)
