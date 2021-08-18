import sys


n,m = map(int,sys.stdin.readline().split())

wrong = sys.stdin.readline()
right = sys.stdin.readline()

# 편집거리랑 비슷한데 i -> ijl 매칭 가능. v -> vw
# 역은 안됨. w -> v로는 인식 안함

# 편집거리 ?

distance = [[0 for i in range(len(wrong)+1)] for j in range(len(right)+1)]


for i in range(1,len(wrong)+1):
    distance[0][i] = i

for j in range(1,len(right)+1):
    distance[j][0] = j

for i in range(1, len(wrong)+1):
    for j in range(1, len(right)+1):
        if wrong[i-1] == right[j-1]: # 똑같으면 기록하고 넘어가면 되고
            distance[j][i] = distance[j-1][i-1]

        elif wrong[i-1] != right[j-1]: # 다른데, i v 인 경우에는 맞는 걸로 처리하면면
            if wrong[i-1] == 'i' and (right[j-1] == 'j' or right[j-1] == 'l'):
                distance[j][i] = distance[j-1][i-1]
            elif wrong[i-1] == 'v' and right[j-1] == 'w':
                distance[j][i] = distance[j - 1][i - 1]
            else:
                distance[j][i] = 1+ min(distance[j-1][i-1],distance[j-1][i],distance[j][i-1])

print(distance[-1][-1])