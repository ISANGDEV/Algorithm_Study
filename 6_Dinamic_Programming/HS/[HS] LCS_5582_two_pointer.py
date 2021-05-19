import sys

def lcs(s1,s2):
    # s1 < s2
    global result
    left = 0
    right = 0


    while left <= len(s1)-1 and right <= len(s1)-1:
        if s1[left:right] in s2:
            if right - left > max(result):
                result = []
                result.append(right-left)
            right += 1
        elif left == right:
            right += 1
        elif s1[left:right] not in s2:
            left += 1

    return

s1 = (sys.stdin.readline())
s2 = (sys.stdin.readline())
result = [0]
if len(s1) < len(s2):
    lcs(s1,s2)
else:
    lcs(s2,s1)

print(max(result))
