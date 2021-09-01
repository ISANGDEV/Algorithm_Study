import sys
N = int(input())
arr = list(map(int, sys.stdin.readline().split())) 
dp = [[0]*(5001) for _ in range(5001)]

def solution(start, end):
    if start >= end:
        return 0 
    if dp[start][end] != 0: 
        return dp[start][end]

    # print("S, E = ", start, end)
    if arr[start] == arr[end]: 
        dp[start][end] = solution(start+1, end-1)
    else:
        dp[start][end] = min(solution(start+1, end), solution(start, end-1)) + 1
    return dp[start][end]

print(solution(0, N-1))
# 처음에 end 뒤에 arr[start] 값을 추가하는 방법만 있다고 생각함. 
# while start<=end: 
#    if arr[start] != arr[end]: 
        # arr.insert(end+1, arr[start])
        # end -= 1 
#        cnt += 1 
#        start += 1 
#        continue

#    end -= 1 
#    start += 1 
# print(cnt)
