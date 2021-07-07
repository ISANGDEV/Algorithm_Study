n=int(input())

total=[[ 0 for _ in range(501)] for _ in range(501)]

for _ in range(n):
    x1,y1,x2,y2=map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            total[i][j]=1
result=0
for i in total:
    result+=sum(i)
print(result)

    
