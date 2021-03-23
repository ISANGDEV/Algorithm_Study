n=int(input())

lost=list(map(int,input().split()))

reserve=list(map(int,input().split()))
count=0

total=[1]*5

for i in range(len(lost)):
    lost[i]-=1
for i in range(len(reserve)):
    reserve[i]-=1

for i in lost:
    total[i]-=1

for i in reserve:
    total[i]+=1

for i in range(n):
    if(total[i]==0):
        if(i-1>=0 and total[i-1]==2):
            total[i-1]=1
            total[i]=1
        elif(i+1<n and total[i+1]==2):
            total[i+1]=1
            total[i]=1

for i in range(n):
    if(total[i]>=1):
        count+=1

print(count)
