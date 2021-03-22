N,M=map(int,input().split())
result=0
for i in range(N):
    result=max(result,min(list(map(int,input().split()))))
print(result)


