N,C=map(int,input().split())
houses=[]
for i in range(N):
    houses.append(int(input()))
houses.sort()
start=1
end=houses[-1]-houses[0]
result=0
while(start<=end):
    mid=(start+end)//2
    prev=houses[0]
    cnt=1
    for i in range(1,N):
        if houses[i]>=prev+mid:
            cnt+=1
            prev=houses[i]
    if(cnt>=C):
        start=mid+1
        result=mid
    else:
        end=mid-1
print(result)
