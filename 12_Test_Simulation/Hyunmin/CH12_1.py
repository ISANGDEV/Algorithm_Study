import sys
str_data = sys.stdin.readline().rstrip()
end = len(str_data)
half = end//2
first = 0
for i in range(0, half):
    first += int(str_data[i])
sec = 0
for i in range(half, end):
    sec += int(str_data[i])

if first == sec:
    print("LUCKY")
else:
    print("READY")

# 답안 변수 하나만 사용.
# summary = input()
# for i in range(end//2):
#     summary += int(input(i))
# for i in range(end//2):
#     summary -= int(input(i))
#     if summary == 0:

