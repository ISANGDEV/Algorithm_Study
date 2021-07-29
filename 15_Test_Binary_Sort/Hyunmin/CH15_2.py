import sys
#  loop 
def bst(target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if mid == nums[mid]:
            return mid
        elif mid > nums[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1

N = int(input())
nums = list(map(int, sys.stdin.readline().split()))
fixed_point = bst(N//2, 0, N)
print(fixed_point) if fixed_point else print(-1)



