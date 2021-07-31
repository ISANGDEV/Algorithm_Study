N, x = map(int, input().split())
numbers = list(map(int, input().split()))
left = 0
right = N - 1
leftidx = N - 1
rightidx = 0
status = False
while (left <= right):
    mid = (left + right) // 2
    target = numbers[mid]
    if (target == x):
        status = True
        leftidx = min(leftidx, mid)
        right = mid -1
    elif (target < x):
        left = mid + 1
    else:
        right = mid - 1
left = leftidx
right = N - 1
while (left <= right):
    mid = (left + right) // 2
    target = numbers[mid]
    if (target == x):
        status = True
        rightidx = max(rightidx, mid)
        left = mid + 1
    elif (target < x):
        left = mid + 1
    else:
        right = mid - 1
if(status):
    print(rightidx - leftidx + 1)
else:
    print(-1)