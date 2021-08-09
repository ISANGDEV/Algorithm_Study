N = int(input())
arr = []
for i in range(N): 
    arr.append(list(map(int, input().split())))

dp = [0]*(N+1) 
# 뒤에서부터 생각 
# dp[i] (현재까지의 값 중 최고 총합) = {dp[i+1] (이전까지 값의 총합)} vs {현재 값[1] + dp[i + [0]](현재 값으로부터 t만큼 지났을때 그 "t까지 값의 총합")} 
for i in reversed(range(N)):
    if i + arr[i][0] < N+1: 
        # dp[x] 는 dp[x]부터 끝(dp[N-1])까지 다 더한 값. 
        dp[i] = max(dp[i+1], dp[arr[i][0]+i] + arr[i][1])
    # dp 범위를 초과할 때 현 arr[i][0]이 1이라면 다음 것(dp[i+arr[i][0]])을 검사하는데 0이면 안된다. 
    # 다음 다음 dp 부터 값이 들어 있을 수 있기 때문에 범위 초과의 경우 total 값을 넣어준다
    else:
        dp[i] = dp[i+1]

print(dp[0])




# 아래는 dp가 아니다. 
# N = int(input())
# arr = [] 
# for i in range(N): 
#     a, b = map(int, input().split())
#     # N을 초과하는 경우는 추가하지 X 
#     #if i + a <= N: 
#     arr.append([a, b])
# 
# dp = [] 
# # 3  5  1  1  2     4  2 
# # 10 20 10 20 15    40 200 
# result = 0 
# for i in range(N-1):
#     if arr[i][0] + i > N: 
#         continue
# 
#     # 겹친다면 
#     # 0, 3, 총 (1~6 (because arr[1][0] == 5))까지의 합  vs  1, 5 (총 20) 
#     if arr[i][0] > 1:
#         idx = arr[i][0] + i 
#         sec_max = arr[i+1][0] + i + 1 
#         a_result = arr[i][1]
#         # 포함여부 확인
#         print("vals,", idx, sec_max, a_result)
#         while idx + arr[idx][0] <= sec_max:
#             print("idx ", idx, arr[idx][0], arr[idx][1])
#             a_result += arr[idx][1]
#             idx += arr[idx][0]
#         print(a_result)
#         if a_result > b_result: 
#             pass 
# 
#     # 안겹치면? 그냥 더하기  
#     else: 
#         pass 
# 
# 
# if arr[N-1][0] == 1:
#     result += arr[N-1][0]


    

