import sys

N = int(sys.stdin.readline())
grade = []
for i in range(N):
    x,y = sys.stdin.readline().split()
    grade.append([x,int(y)])

grade.sort(key = lambda x:x[1])

for x,y in grade:
    print(x)

