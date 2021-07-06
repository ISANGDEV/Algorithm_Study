import sys
#
n, m = sys.stdin.readline().rstrip().split()
data = list(map(int, sys.stdin.readline().rstrip().split()))

cnt = 0
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if data[i] == data[j]:
            continue
        cnt += 1

print(cnt)

