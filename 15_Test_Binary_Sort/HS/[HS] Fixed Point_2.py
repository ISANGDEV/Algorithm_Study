import sys


def binary(arry, st,ed):

    while st <= ed:
        mid = (st + ed)// 2

        if arry[mid] > mid:
            ed = mid - 1
        elif arry[mid] < mid:
            st = mid + 1
        elif arry[mid] == mid:
            return mid

    return -1

n = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))
result = binary(arr,0,n-1)

if result == -1 :
    print(-1)

else:
    print(result)
