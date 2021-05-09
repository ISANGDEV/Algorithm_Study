import sys

def binary(number):
    global cmpnt
    left = 0
    right = len(cmpnt) - 1
    while left <= right:
        pivot = (left + right) // 2
        if number > cmpnt[pivot]:
            left = pivot + 1
        elif number < cmpnt[pivot]:
            right = pivot - 1
        elif number == cmpnt[pivot]:
            return 'yes'

    return 'no'
"""
n = int(sys.stdin.readline())
cmpnt = list(map(int,sys.stdin.readline().split()))

m = int(sys.stdin.readline())
paper = list(map(int,sys.stdin.readline().split()))
"""

cmpnt = [8,3,7,9,2]
paper = [5,7,9]
result = []

cmpnt.sort()
for i in paper:
    result.append(binary(i))

print(' '.join(result))
