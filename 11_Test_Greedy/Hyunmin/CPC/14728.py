# 배점 높은 순으로 정렬
import sys

n, t = map(int, sys.stdin.readline().rstrip().split())
# k = [0]*n
# s = [0]*n
arr = []
for i in range(n):
    k, s = map(int, sys.stdin.readline().rstrip().split())
    arr.append((k, s))

    # k[i], s[i] = map(int, sys.stdin.readline().rstrip().split())
arr.sort(reverse=True, key=lambda x: x[1])

total = 0
for i in range(n):
    if t - arr[i][0] >= 0:
        total += arr[i][1]
        t -= arr[i][0]
    # else:
    #     break

print(total)





