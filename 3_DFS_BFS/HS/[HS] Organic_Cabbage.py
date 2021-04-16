
temp = 0
result = []
pos = [[1,0],[-1,0],[0,1],[0,-1]]
t = int(input("테스트 케이스 개수"))

def dfs(geo,x,y):
    #global geo ,그러게 왜 전역변수를 안써도 가능한거
    global m
    global n

    if x < 0 or x >= n or y < 0 or y >= m: # 범위가 벗어났다면
        return 0 # 종료


    if geo[x][y] == 1 : # 양배추가 심어진 곳이라면
        geo[x][y] = 2 # 방문으로 바꾸고
        for i,j in pos:
            dfs(geo,x+i,y+j)

        return 1 # 처음 방문한 곳이라고 알려준다.

    else: #  땅이라면 (0이라면)
        return 0


for i in range(t):
    m,n,k = map(int,input("가로길이, 세로길이, 배추 존재 개수").split())
    cabbage = []
    temp = 0
    geo = [[0 for i in range(m)] for j in range(n)]

    for i in range(k):
        cabbage.append(list(map(int,input("배추의 위치 입력").split())))

    for i,j in cabbage:
        geo[j][i] = 1

    for i in range(m):
        for j in range(n):
            if dfs(geo,j,i) == 1: #전역변수를 안 쓰네 ??
                temp += 1

    result.append(temp)


print(result)
