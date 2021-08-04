n=int(input())
arr=list(map(int,input().split()))

result=[]
def binary(arr, result, start, end):
    mid=(end+start)//2
    if(start>end or arr[mid] > mid):
        return result
    elif(arr[mid]==mid):
        result.append(mid)
        binary(arr, result, start, mid-1)
    elif(arr[mid]<mid):
        binary(arr, result, mid+1, end)
    print(arr, result, mid)
binary(arr, result, 0, n-1)

print(result)
