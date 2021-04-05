"""N * M 크기의 얼음틀이 있다. 구멍이 뚫려있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
  이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오.
2. 입력
첫 번째 줄에 얼음 틀의 새로 길이 N과 가로 길이 M이 주어진다.( 1<=N, M <= 1000)
두 번째 줄부터 N+1번째 줄까지 얼음 틀의 형태가 주어진다.
이때 구멍이 뚫여있는 부분은 0, 그렇지 않은 부분은 1이다."""

n, m = map(int, input("세로 가로 입력").split())
geo = []
for i in range(n):
    geo.append(list(map(int,input("맵 정보 입력"))))

# x y 세로 가로
def dfs(geo,x,y):
    global n
    global m

    if x < 0 or x >= n or y < 0 or y >= m :
        return;
    if geo[x][y] == (1 or 2) :
        return;

    if geo[x][y] == 0 :
        geo[x][y] = 2
        dfs(geo,x-1,y)
        dfs(geo,x+1,y)
        dfs(geo,x,y-1)
        dfs(geo,x,y+1)
        return 1
    return 0

result = 0

for i in range(n):
    for j in range(m):
        if dfs(geo,i,j) == 1 :
            result = result + 1

print(result)
