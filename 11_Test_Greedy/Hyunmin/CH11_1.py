import sys

n = sys.stdin.readline().rstrip()
arr = list(map(int, sys.stdin.readline().rstrip().split()))

totalCnt = subCnt = 0
for i in range(len(arr)):  # range 실행순서
    subCnt += 1
    scary = arr[i]  # 공포도
    if subCnt == scary:
        totalCnt += 1
        subCnt = 0

print(totalCnt)

