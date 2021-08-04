n,c = map(int, input().split())
houses = []
for _ in range(n):
    houses.append(int(input()))
houses.sort()

left = 1
right = houses[-1] - houses[0]
result = 0

while(left <= right):
    mid = (right + left) // 2
    val = houses[0]
    cnt = 1
    for i in range(1, n):
        if houses[i] - val >= mid:
            val = houses[i] 
            cnt += 1
    if cnt < c:
        right = mid - 1
    else:
        left = mid + 1
        result = mid

print(result)