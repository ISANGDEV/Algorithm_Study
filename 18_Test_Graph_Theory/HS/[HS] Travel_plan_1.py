import sys

# n은 전체, m은 여행 계획에 있는 도시 수
infi = int(1e9)
n,m = map(int,sys.stdin.readline().split())
geo = [[infi for i in range(n+1)] for j in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            geo[i][j] = 0

for i in range(n): # i 가 갈 수 있는 여행지. 즉 i는 출발지
    temp_0 = list(map(int,sys.stdin.readline().split()))
    temp_1 = []
    for j in range(n): # j는 i가 갈 수 있는 여행지. 즉 목표
        if temp_0[j] == 1:
            temp_1.append(j+1)

    for k in temp_1: # 길 쌍방임.
        geo[i][k] = 1
        geo[k][i] = 1

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            geo[j][k] = min(geo[j][k],geo[j][i]+geo[i][k])

goal = list(map(int,sys.stdin.readline().split()))
goal.insert(0,goal[0])

check = 1
for i in range(1,len(goal)):
    if geo[goal[i-1]][goal[i]] != infi:
        continue
    else:
        check = 0
        break

if check == 1:
    print("YES")

elif check == 0:
    print("NO")