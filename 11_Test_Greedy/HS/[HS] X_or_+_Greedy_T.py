import sys

s = str(sys.stdin.readline())
temp = 0
s.strip()


for i in s:
    if i == '0' or i == '1' or temp <= 1:
        temp += int(i)
    else:
        temp *= int(i)
print(temp)
