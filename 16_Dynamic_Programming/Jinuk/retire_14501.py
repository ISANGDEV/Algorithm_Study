n = int(input())
work = []
for _ in range(n):
    t, p = map(int, input().split())
    work.append((t, p))

dp = [0] * (n+1)
max_val = 0

for i in range(n-1, -1, -1):
    
    if i + work[i][0] <= n:
        dp[i] = max(work[i][1] + dp[i + work[i][0]], max_val)
        max_val = dp[i]
    
    else:
        dp[i] = max_val

print(max_val)

## 뭘까....
