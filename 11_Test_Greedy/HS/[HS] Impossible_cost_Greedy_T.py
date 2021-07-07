import sys
n = int(sys.stdin.readline())
cost = list(map(int,sys.stdin.readline().split()))
cost.sort()

target = 1
for i in cost:
    if target < i:
        break
    target += i
print(target)
