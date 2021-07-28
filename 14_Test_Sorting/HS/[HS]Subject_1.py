import sys

n = int(sys.stdin.readline())

info = []

for i in range(n):
    temp = list(map(str, sys.stdin.readline().split()))
    for i in range(1,4,1):
        temp[i] = int(temp[i])

    info.append(temp)



info.sort(key = lambda x: (-x[1], x[2], -x[3],x[0]))


for i in range(len(info)):
    print(info[i][0])
