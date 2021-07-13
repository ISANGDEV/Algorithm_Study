import sys

n = sys.stdin.readline().rstrip()

stack = []
sum = 0

for i in n:
    if i.isdigit() == 1:
        sum += int(i)
    else:
        stack.append(i)
stack.sort()

result = ""

for i in stack:
    result+= i

result += str(sum)

print(result)