import sys

"""n,m = map(int,sys.stdin.readline().split())

length = list(map(int,sys.stdin.readline.split()))

result = 0
"""
def binary_searching(length,m):
    low = 0
    high = max(length)

    while low <= high:
        sum = 0
        criteria = (low + high) // 2
        for i in length:
            if i > criteria:
                sum += i - criteria

        if sum < m: # 절단기 높이를 낮춰야 함.
            high = criteria - 1
        else: # 절단기 높이를 높여도 됨.
            result = criteria
            low = criteria + 1

    print(result)

binary_searching([19,15,10,17],6)
