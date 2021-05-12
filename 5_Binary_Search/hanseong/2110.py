n, c= map(int, input().split())

xi=[0] * n

for i in range(n):
    xi[i]=int(input())
    
xi.sort()

diff=[0] *(n-1)

for i in range(n-1):
    diff[i]=xi[i+1]-xi[i]

start=1
end=(xi[-1]-xi[0])+1

def search(std):
    sum=0
    result=0
    
    for i in range(len(diff)):
        if(sum+diff[i]>=std):
            sum=0
            result+=1
        else:
            sum+=diff[i]

    result+=1
    return result

answer=0
while start<=end:
    mid = (start + end) // 2    
    temp=search(mid)
    
    if(temp>=c):
        answer=mid
        start = mid + 1
       
    else:
        end = mid - 1


print(answer)

            



