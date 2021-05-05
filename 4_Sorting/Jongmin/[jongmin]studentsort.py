N=int(input())
result=[]
for i in range(N):
    name,score=input().split()
    result.append([int(score),name])
result.sort(key=lambda x:x[0])
for r in result:
    print(r[1],end=' ')