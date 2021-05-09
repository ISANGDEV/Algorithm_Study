N,M=map(int,input().split())
lessons=list(map(int,input().split()))
left=max(lessons)
right=sum(lessons)
answer=right
while(left<=right):
    mid=(left+right)//2
    cnt=0
    temp=0
    for i in range(len(lessons)):
        temp+=lessons[i]
        if(temp>mid):
            cnt+=1
            temp=lessons[i]
    cnt+=1
    if(cnt>M):
        left=mid+1
    else:
        answer=min(answer,mid)
        right=mid-1
print(answer)

