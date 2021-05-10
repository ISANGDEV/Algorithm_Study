#답 봄 다시풀기
N,H=map(int,input().split())
uobs=[]
dobs=[]
for i in range(N):
    if(i%2==0):
        dobs.append(int(input()))
    else:
        uobs.append(int(input()))
dobs.sort()
uobs.sort()
result=[N+1,0]
def biselect(arr,h):
    l=0
    r=len(arr)-1
    while(l<=r):
        mid=(l+r)//2
        if(arr[mid]>=h):
            r=mid-1
        else:
            l=mid+1
    return l
for i in range(1,H+1):
    tempcnt=0
    tempcnt+=(len(uobs)-biselect(uobs,H-i+1))
    tempcnt+=(len(dobs)-biselect(dobs,i))
    if(result[0]>tempcnt):
        result=[tempcnt,1]
    elif(result[0]==tempcnt):
        result[1]+=1
print(result[0],result[1])