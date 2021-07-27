import sys
n = int(input())
data = []
for _ in range(n):
    name, kor, eng, mat = sys.stdin.readline().split()
    data.append([name, int(kor), int(eng), int(mat)])

data.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for name in data:
    print(name[0])





