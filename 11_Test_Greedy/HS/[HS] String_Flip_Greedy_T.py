import sys

s = sys.stdin.readline()

result_zero = 0
result_one = 0


if s[0] == '1':
    result_zero +=1
else:
    result_one += 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '1':
            result_zero += 1
        else:
            result_one += 1

print(min(result_zero,result_one))