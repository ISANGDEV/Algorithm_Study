import sys

n = int(sys.stdin.readline())
number = list(map(int,sys.stdin.readline().split()))
op = list(map(int,sys.stdin.readline().split()))
max_r = -1e9
min_r = 1e9
# 1 : + , 2 : - , 3 : *, 4: /

def dfs(count,plus,minus,multiply,divide,result):
    global max_r
    global min_r
    if count == n:
        max_r = max(result, max_r)
        min_r = min(result,min_r)
        return
    else:
        if plus:
            dfs(count+1,plus-1,minus,multiply,divide,result+number[count])
        if minus:
            dfs(count+1,plus,minus-1,multiply,divide,result-number[count])
        if multiply:
            dfs(count+1,plus,minus,multiply-1,divide,result*number[count])
        if divide:
            dfs(count+1,plus,minus,multiply,divide-1,int(result/number[count]))

dfs(1,op[0],op[1],op[2],op[3],number[0])

print(max_r)
print(min_r)