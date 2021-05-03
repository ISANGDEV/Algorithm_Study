N=int(input())
cards=list(map(int,input().split()))
cards.sort()
def binarysearch(x,l,left,right):
    if(left>right):
        return False
    mid=(left+right)//2
    if(l[mid]==x):
        return True
    elif(l[mid]<x):
        return binarysearch(x,l,mid+1,right)
    else:
        return binarysearch(x,l,left,mid-1)
M=int(input())
tests=list(map(lambda x: '1' if binarysearch(int(x),cards,0,len(cards)-1) else '0',input().split()))
print(' '.join(tests))
