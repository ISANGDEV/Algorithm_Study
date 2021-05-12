n,m= map(int, input().split())

lesson=list(map(int,input().split()))


def search(std):
    sum=0
    result=0
    
    for i in range(n):
        if(sum+lesson[i]<=std):
            sum+=lesson[i]
        else:
            result+=1
            sum=lesson[i]
    result+=1
    return result


start, end = max(lesson), sum(lesson)

temp=0

while start<=end:
    mid = (start + end) // 2    
    temp=search(mid)

    
    if(temp>m):
       start = mid + 1
       
    elif(temp<=m):
        end = mid - 1

print(start)
    
