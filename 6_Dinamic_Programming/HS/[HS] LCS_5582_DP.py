import sys

"""
s1 = str(sys.stdin.readline())
s2 = str(sys.stdin.readline())

s1.rstrip('\n')
s2.rstrip('\n')
"""
s1 = 'UPWJCIRUCAXIIRGL'
s2 = 'SBQNYBSBZDFNEV'
dp = [[0 for i in range(len(s1)+1)] for j in range(len(s2)+1)]
result = 0
for i in range(1,len(s2)+1):
    for j in range(1,len(s1)+1):
        if s2[i-1] == s1[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            result = max(result,dp[i][j])

print(result)
