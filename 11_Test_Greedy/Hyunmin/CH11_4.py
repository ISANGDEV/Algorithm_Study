import sys

n = int(input())
s = list(map(int, sys.stdin.readline().rstrip().split()))
s.sort()

idx = 0
total = 0
i = 0
# for 문에서 i-- 하고 continue 하는것을 파이썬에서 어떻게 해야하나
while i < len(s):
    idx += 1
    if idx > total:
        if s[i] <= idx <= s[i] + total:
            pass
        else:
            break
        total += s[i]
        i += 1
    else:
        continue

print(idx)
# for i in s:
#     idx += 1  # 찾는 값이자, 1부터 idx 까지의 값을 만들 수 있다는 것을 의미한다.
#     if idx > total:
#         # if idx가 가능한지 먼저 check. 불가능시 break.
#         if i <= idx <= i + total:
#             pass
#         else:
#             break
#         total += i
#     else:
#         continue
# print(idx)

