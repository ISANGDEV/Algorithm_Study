import sys
n = int(sys.stdin.readline())
express = []

for i in range(n):
    express.append(list(map(int,sys.stdin.readline().split())))

result = 0
for a,b in express:
    result += a*b

print(result)