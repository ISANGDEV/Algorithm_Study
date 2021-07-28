import sys
import heapq



n = int(sys.stdin.readline())
info = []
result = 0
for i in range(n):
    temp =int(sys.stdin.readline())
    heapq.heappush(info,temp)


while len(info) >= 2:
    temp_1 = heapq.heappop(info)
    temp_2 = heapq.heappop(info)
    temp_sum = temp_1 + temp_2
    result += temp_sum
    heapq.heappush(info,temp_sum)


print(result)