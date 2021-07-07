import sys
import heapq
n = int(sys.stdin.readline())

score = []

for i in range(n):
    heapq.heappush(score,float(sys.stdin.readline()))

result = []

for i in range(7):
    print('%0.3f' % heapq.heappop(score))

