n = int(input())
numbers = list(map(int, input().split()))

left, right = 0, len(numbers) - 1

mid = (left + right) // 2

while(numbers[mid] != mid):
    if right > left:
        mid = -1
        break
    if numbers[mid] < mid:
        left = mid + 1
    elif numbers[mid] > mid:
        right = mid - 1
    else:
        break
    mid = (left + right) // 2

print(mid)