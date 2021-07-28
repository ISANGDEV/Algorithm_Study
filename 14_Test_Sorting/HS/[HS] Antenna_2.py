import sys

n = int(sys.stdin.readline())

geo = list(map(int, sys.stdin.readline().split()))

geo.sort()

idx = len(geo) // 2

print(geo[idx])