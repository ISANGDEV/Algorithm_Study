import sys

dp = [0] * (n+1)
a = 2
b = 3
c = 5

a_i,b_i,c_i = 0,0,0

dp[0] = 1

for i in range(1,n):
    dp[i] = min(a,b,c)
    if dp[i] == a:
        a_i += 1
        a = dp[a_i] * 2
    if dp[i] == b:
        b_i += 1
        b = dp[b_i] * 3
    if dp[i] == c:
        c_i  +=1
        c =dp[c_i] * 5

print(ugly[-1])
