import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    num = int(input())
    heapq.heappush(heap, num)

answer = 0

while len(heap) != 1:
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    answer += first + second
    heapq.heappush(heap, first+second)

print(answer)