import sys

n, m = map(int, sys.stdin.readline().split())

temp_w = list(map(int,sys.stdin.readline().split()))

dic = {}
for i in temp_w:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

result = dic.values()
num = 0
for i in result:
    temp = 0
    w_sum = sum(result) - i
    temp = i * w_sum
    num += temp


print(num/2)

