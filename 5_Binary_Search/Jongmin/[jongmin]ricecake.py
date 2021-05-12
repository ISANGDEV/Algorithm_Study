N,M=map(int,input().split())
rk=list(map(int,input().split()))
left=0
right=max(rk)
while(left<=right):
    mid=(left+right)//2
    summ=0
    for r in rk:
        if(r>mid):
            summ+=(r-mid)
    if(summ==M):
        print(mid)
        break
    elif(summ<M):
        right=mid-1
    else:
        left=mid+1
