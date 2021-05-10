import sys

def binary(left,right,m):
    global length


    while left <= right:
        temp = 0
        sum_blueray = 0
        middle = (left + right) // 2
        for i in length:
            if temp + i <= middle:
                temp += i
            else:
                temp = i
                sum_blueray += 1

        if temp > 0:
            sum_blueray += 1

        if sum_blueray > m :
            left = middle + 1
        elif sum_blueray <= m:
            right = middle - 1

    return left

n,m = map(int,sys.stdin.readline().split())

length = list(map(int,sys.stdin.readline().split()))

left = max(length)
right = sum(length)
print(binary(left,right,m))
