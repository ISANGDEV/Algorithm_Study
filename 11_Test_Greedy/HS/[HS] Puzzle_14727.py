import sys

n = int(sys.stdin.readline()) # 직사각형 개수
# 너비는 1로 고정
h = []
for i in range(n):
    h.append(int(sys.stdin.readline())) # 직사각형 높이

h.sort()

