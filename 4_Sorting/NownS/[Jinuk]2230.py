n, m = map(int, input().split())


def solution(arr, m):
    arr.sort()
    min = 2000000000
    left = 0
    right = 0
    length = len(arr)
    while left <= right < length:
        diff = arr[right] - arr[left]
        if diff < m:
            right += 1
        elif diff > m:
            if diff < min:
                min = diff
            left += 1
        else:
            return diff
    return min



nums = []
for _ in range(n):
    a = int(input())
    nums.append(a)

print(solution(nums, m))
