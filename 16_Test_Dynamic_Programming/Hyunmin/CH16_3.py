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




    

