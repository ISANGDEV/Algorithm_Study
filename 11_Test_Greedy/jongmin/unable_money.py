##이해안감 -> result이전까지 다 만들 수 있으니까 그다음에 나오는 돈 단위가 result보다 같거나 작으면됨
N=int(input())
money=list(map(int, input().split()))
money.sort()
result=1
for m in money:
    if(result<m):
        break
    result+=m
print(result)
