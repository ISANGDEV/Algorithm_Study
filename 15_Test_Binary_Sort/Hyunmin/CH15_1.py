import sys
import bisect
N, X = map(int, input().split())
nums = list(map(int, sys.stdin.readline().split()))
answer = bisect.bisect_right(nums, X) - bisect.bisect_left(nums, X)
print(answer if answer > 0 else -1)

