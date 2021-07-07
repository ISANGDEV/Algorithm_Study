import sys

n = int(sys.stdin.readline())

data = []
count = 0
result = 0
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))

data.sort()

for i in data:
    count += 1 # 그룹에 포함 된 사람 수
    if count >= i:
        result += 1 # 그룹 수
        count = 0 # 그룹 생성 되면 사람 0

print(result)