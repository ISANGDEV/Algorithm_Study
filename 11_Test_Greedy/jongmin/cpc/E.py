N=int(input())
result=0
for i in range(N):
    C,K=map(int, input().split())
    result+=C*K
print(result)