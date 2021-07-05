##이해안감
N=int(input())
money=list(map(int, input().split()))
money.sort()
result=1
for m in money:
    if(result<m):
        break
    result+=m
print(result)
