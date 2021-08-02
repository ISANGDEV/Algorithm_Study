N = int(input())
nums = list(map(int, input().split()))
left = 0
right = N - 1
status=False
while (left <= right):
    mid = (left + right) // 2
    if(mid==nums[mid]):
        status=True
        print(mid)
        break
    elif(mid<nums[mid]):
        right=mid-1
    else:
        left=mid+1
if(not status):
    print(-1)