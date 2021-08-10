import sys

n = int(sys.stdin.readline())

info = []

for i in range(n):
    temp = list(map(int,sys.stdin.readline().split()))

    info.append(temp)

dp = [0] * (n+1)



for i in range(n+1):
    for j in range(i):
        day,money = info[j]
        if i - day >= j:
            dp[i] = max(dp[i],dp[j] + money)

print(max(dp))