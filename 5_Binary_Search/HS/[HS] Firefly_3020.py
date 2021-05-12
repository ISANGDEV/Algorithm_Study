import sys
def binary(obstacle,target):
    left = 0
    right = len(obstacle) - 1
    while left <= right:
        middle = (left + right) // 2
        if obstacle[middle] > target:
            right = middle - 1
        elif obstacle[middle] < target:
            left = middle + 1

    return len(obstacle) - right - 1

    # 123 456
    # len : 6 / middle = 2 2.5

n,h = map(int,sys.stdin.readline().split())

obstacle_top = []
obstacle_bottom = []

for i in range(n):
    if i % 2 == 0 :
        obstacle_bottom.append(int(sys.stdin.readline()))
    else:
        obstacle_top.append(int(sys.stdin.readline()))

obstacle_top.sort()
obstacle_bottom.sort()
# x + y = k를 최소로
# x :

answer = n
count = 0
for i in range(0,h):
    low = binary(obstacle_bottom, i + 0.5)
    high = binary(obstacle_top, h - i - 0.5)

    if answer > low + high:
        answer = low + high
        count = 1
    elif answer < low + high:
        continue
    elif answer == low + high:
        count += 1


print(answer,count)

