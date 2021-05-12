N=int(input())
components=list(map(int,input().split()))
components.sort()
M=int(input())
finds=map(int,input().split())
def binarysearch(target, arr):
    left=0
    right=len(arr)-1
    while(left<=right):
        mid=(left+right)//2
        if(arr[mid]==target):
            return 'yes'
        elif(arr[mid]<target):
            left=mid+1
        else:
            right=mid-1
    return 'no'
for f in finds:
    print(binarysearch(f,components))