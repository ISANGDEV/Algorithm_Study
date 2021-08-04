import sys

def binary_first(arry,target,st,ed):

    while st <= ed:
        mid = (st + ed) // 2
        if arry[mid] == target:
            if mid == 0 or arry[mid-1] != target:
                return mid
            else:
                ed = mid - 1
        elif arry[mid] >= target:
            ed = mid - 1
        else:
            st = mid + 1
    return -1

def binary_last(arry,target,st,ed):

    while st <= ed:
        mid = (st + ed) // 2
        if arry[mid] == target:
            if mid == len(arry)-1 or arry[mid+1] != target:
                return mid
            else:
                st = mid + 1
        elif arry[mid] >= target:
            ed = mid - 1
        else:
            st = mid + 1

    return -1

n,x = map(int,sys.stdin.readline().split())
info = list(map(int,sys.stdin.readline().split()))

fst = binary_first(info,x,0,n-1)

last = binary_last(info,x,0,n-1)

if fst + last == -2:
    print(-1)

else:
    print(last-fst+1)











