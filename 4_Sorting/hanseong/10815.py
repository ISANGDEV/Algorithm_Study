def binary(arr, target, start, end):
    if(start> end):
        result.append('0')
        return 
    mid=(end+start)//2

    if(arr[mid]==target):
        result.append('1')
        return 
    elif(arr[mid]>target):
        binary(arr, target, start, mid-1)

    else:
        binary(arr, target, mid+1, end)



n=int(input())



card=(list(map(int,input().split())))

card.sort()

m=int(input())



find=list(map(int,input().split()))


result=[]

for i in find:
    binary(card,i,0,n-1)

print(' '.join(result))
    
