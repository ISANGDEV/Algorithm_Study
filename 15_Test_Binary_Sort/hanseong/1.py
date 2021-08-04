from bisect import bisect_left


n,x=map(int,input().split())
nums=list(map(int,input().split()))

ix=bisect_left(nums,x)
count=-1

for i in range(ix,len(nums)):
    count+=1   
    if(nums[i]!=x):
        break
print(count)
