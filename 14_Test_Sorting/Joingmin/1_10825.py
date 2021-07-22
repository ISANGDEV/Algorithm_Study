N=int(input())
result=[]
for _ in range(N):
    name,k,y,s=input().split()
    result.append([name,int(k),int(y),int(s)])
result=sorted(result,key=lambda x:(-x[1],x[2],-x[3],x[0]))
for r in result:
    print(r[0])