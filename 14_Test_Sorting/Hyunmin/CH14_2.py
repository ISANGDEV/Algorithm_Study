import sys
n = int(input())
home = list(map(int, sys.stdin.readline().split()))
home.sort()
print(min(home[n//2], home[n//2-1]))



