
"""행복 왕국의 왕실 정원은 체스판과 같은 8 X 8 좌표 평면이다. 왕실 정원의 특정한 한 칸에 나이트가 서 있다.
나이트는 매우 충성스러운 신하로서 매일 무술을 연마한다.

나이트는 말을 타고 있기 때문에 이동을 할 때에는 L자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없다.
 나이트는 특정한 위치에서 다음과 같은 2가지 경우로 이동할 수 있다.

수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
이처럼 8 X 8 좌표 평면상에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하시오.
이때 왕실의 정원에서 행 위치를 표현할 때는 1부터 8로 표현하며, 열 위치를 표현할 때는 a부터 h로 표현한다."""

# 2칸 위로 가기 / 아래로 가기 /
# 1칸 왼쪽으로 가기 / 오른쪽으로 가기
# y +2, y-2 / x-1 x + 1 4가지

#  2칸 왼쪽으로 가기 / 오른쪽으로 가기
# 1칸 위로 가기 / 아래로 가기
# x + 2, x-2 / y +1 , y-1  4가지
column = [1,2,3,4,5,6,7,8]
row = ['A','B','C','D','E','F','G','H']
for i in range(8):
    row[i] = ord(row[i])

count = 0

dxy = [[-2,1],[-2,-1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2]]

position = input("A8 처럼 좌표 입력하기")
pos_column = int(position[1])
pos_row = ord(position[0])

#pos_column,pos_row = map(int,input("행, 열 좌표 입력하기").split())
pos_now = [[pos_row,pos_column] for j in range(8)]

#pos_possible = [[0 for k in range(8)] for l in range(8)]


for i in range(8):
    pos_now[i][0] = pos_now[i][0] + dxy[i][0]
    pos_now[i][1] = pos_now[i][1] + dxy[i][1]
    if (pos_now[i][0] in row)and (pos_now[i][1] in column):
        count += 1

print(count)
