import heapq
def solution(food_times, k):
    if(sum(food_times)<=k):
        return -1
    heap=[]
    L=len(food_times)
    for f in range(L):
        heapq.heappush(heap,(food_times[f],f+1))
    minusval=0
    sumval=0
    while sumval+((heap[0][0]-minusval)*L)<=k:
        val,idx=heapq.heappop(heap)
        sumval+=(val-minusval)*L
        L-=1
        minusval=val
    heap.sort(key=lambda x:x[1])
    return heap[(k-sumval)%len(heap)][1]

print(solution([3, 1, 2],5))
print(solution([1, 1, 1,1,1,1],5))
print(solution([1, 1, 1,1,1],5))
print(solution([4,2,3,6,7,1,5,8],16))
print(solution([4,2,3,6,7,1,5,8],27))


# 0~1초 동안에 1번 음식을 섭취한다. 남은 시간은 [2,1,2] 이다.
# 1~2초 동안 2번 음식을 섭취한다. 남은 시간은 [2,0,2] 이다.
# 2~3초 동안 3번 음식을 섭취한다. 남은 시간은 [2,0,1] 이다.
# 3~4초 동안 1번 음식을 섭취한다. 남은 시간은 [1,0,1] 이다.
# 4~5초 동안 (2번 음식은 다 먹었으므로) 3번 음식을 섭취한다. 남은 시간은 [1,0,0] 이다.
# 5초에서 네트워크 장애가 발생했다. 1번 음식을 섭취해야 할 때 중단되었으므로, 장애 복구 후에 1번 음식부터 다시 먹기 시작하면 된다.

# import heapq
# def solution(food_times, k):
#     if(sum(food_times)<=k):
#         return -1
#     heap=[]
#     L=len(food_times)
#     for f in range(L):
#         heapq.heappush(heap,(food_times[f],f+1))
#     minusval=0
#     for f in range(L):
#         val,idx=heapq.heappop(heap)
#         if(k<(val-minusval)*L):
#             heapq.heappush(heap,(val,idx))
#             break
#         k-=(val-minusval)*L
#         L-=1
#         minusval=val
#     heap.sort(key=lambda x:x[1])
#     return heap[k][1]