T = int(input())

answers = []

for _ in range(T):
    n, m = map(int, input().split())

    gold_origin = list(map(int, input().split()))
    gold = [[0 for _ in range(m)] for _ in range(n)]
    k = 0
    for i in range(n):
        for j in range(m):
            gold[i][j] = gold_origin[k]
            k += 1
    
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        dp[i][0] = gold[i][0]
    for i in range(1, m):
        for j in range(n):
            if j == 0:
                dp[j][i] = max(gold[j][i] + dp[j][i-1], gold[j][i] + dp[j+1][i-1])
            elif j == n-1:
                dp[j][i] = max(gold[j][i] + dp[j][i-1], gold[j][i] + dp[j-1][i-1])
            else:
                dp[j][i] = max(gold[j][i] + dp[j][i-1], gold[j][i] + dp[j-1][i-1], gold[j][i] + dp[j+1][i-1])

    max = 0
    for i in range(n):
        if dp[i][m-1] > max:
            max = dp[i][m-1]
    answers.append(max)


for answer in answers:
    print(answer)