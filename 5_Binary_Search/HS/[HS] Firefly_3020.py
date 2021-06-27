import sys
def binary(obstacle,target):
    left = 0
    right = len(obstacle) - 1
    while left <= right:
        middle = (left + right) // 2
        if obstacle[middle] > target: # 장애물이 부딪히는가
            right = middle - 1
        elif obstacle[middle] < target: # 확인하고
            left = middle + 1

    return len(obstacle) - right - 1 # 부딪히는 장애물 다음부터는 다 부딪히니까
# 전체 갯수에서 - 부딪힌 장애물 index 빼주고, 0에서 index가 시작하니까 1 더 빼주고
# ㅁㅁㅁright "부딪힌 장애물" leftㅁㅁㅁㅁㅁ -> -right -1 하던, -left 하던 둘다 ㅇㅋ
# 이진탐색하고 index 결과 이해하기
    # 123 456
    # len : 6 / middle = 2 2.5

n,h = map(int,sys.stdin.readline().split())

obstacle_top = []
obstacle_bottom = []

for i in range(n):
    if i % 2 == 0 :
        obstacle_bottom.append(int(sys.stdin.readline()))
    else:
        obstacle_top.append(int(sys.stdin.readline())) # 맨처음에 h - 입력 받은 수로 했다가, 틀린거 깨달았음
        # 어차피 밑에서 입력 해줄 때 h - i 로 해줄꺼라서 그냥 "높이 값" 자체를 넣어야함

obstacle_top.sort()
obstacle_bottom.sort()
# x + y = k를 최소로
# x :

answer = n
count = 0
for i in range(0,h):
    low = binary(obstacle_bottom, i + 0.5)
    high = binary(obstacle_top, h - i - 0.5) # 중간을 지니가니까 +- 0.5 해주고
    # 높이 별로 최솟값 확인
    # N개의 높이에서 N개의 장애물 일일히 확인하기 -> 정렬된 배열을 이진탐색으로 찾아서 이거에 부딪히는 장애물 찾기(log N) 맞나? 어쨋든 많이 줄여서
    # N^2을 피했음
    if answer > low + high:
        answer = low + high
        count = 1
    elif answer < low + high:
        continue
    elif answer == low + high:
        count += 1


print(answer,count)

