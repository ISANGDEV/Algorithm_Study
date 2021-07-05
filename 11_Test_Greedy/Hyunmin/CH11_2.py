# import sys
# input = sys.stdin.readline().rstrip()
# operation = True  # True = * False = +
# arr = []
# for s in input:
#     if int(s) != 0:
#         arr.append(int(s))
# if len(arr) == 0:
#     print(0)
# else:
#     total = arr[0]
#     for i in range(1, len(arr)):
#         if arr[i] == 1:
#             total += arr[i]
#         else:
#             total *= arr[i]
#     print(total)


# 개선된 코드
s = input()
total = int(s[0])   # 처음에 0이 들어오면 0을 곱하면 이상해진다
for i in range(1, len(s)):
    if int(s[i]) <= 1 or total <= 1:
        total += int(s[i])
    else:
        total *= int(s[i])

print(total)


