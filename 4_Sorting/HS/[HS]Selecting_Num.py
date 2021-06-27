import sys
n, m = map(int,sys.stdin.readline().split())


index_s = 0
index_e = 0

number = []

for i in range(n):
    number.append(int(sys.stdin.readline()))

number.sort()

result = number[-1] - number[0]

while index_s < n and index_e < n :
    if number[index_e] - number[index_s] < m:
        index_e += 1
    else:
        result = min(result,number[index_e]-number[index_s])
        index_s +=1

print(result)