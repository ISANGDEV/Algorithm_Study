import sys

n, t = map(int,sys.stdin.readline().split())
score = [[0,0]]
knapsack = [[0 for i in range(t+1)] for j in range(n+1)]

for i in range(n):
    score.append(list(map(int,sys.stdin.readline().split())))


for i in range(1,n+1):
    for j in range(1,t+1):
        w = score[i][0]
        c = score[i][1]
        
        if j < w:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(c + knapsack[i-1][j-w], knapsack[i-1][j])

print(knapsack[n][t])
