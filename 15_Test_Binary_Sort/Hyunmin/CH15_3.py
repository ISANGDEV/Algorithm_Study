n, c = list(map(int, input().split(' ')))

arr = []
for _ in range(n): 
    arr.append(int(input()))
arr.sort()
# 1 2 4 8 9 

start = 1  # 가장 작은 차이부터 -> 1
end = arr[-1] - arr[0]   # 가장 큰 차이까지 -> 8 숫자를 탐색할 거임. 
# 찾는 숫자 중에서 가장 큰 값이 최대 거리 
largest = 0 
while start <= end: 
    mid = (start + end) // 2 
    count = 1
    prev_idx = 0 
    for i in range(1, n): 
        if arr[i] >= arr[prev_idx] + mid:  # 
            count += 1
            prev_idx = i 
    
    if count >= c: 
        largest = max(largest, mid)
        start = mid + 1
    else: 
        end = mid - 1
print(largest)
        
