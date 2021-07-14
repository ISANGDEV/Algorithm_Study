n = input()

cnt = 0
right_start = len(n) // 2
left = 0
right = 0

for i in n:
    if cnt >= right_start:
        right += int(i)
    else:
        left += int(i)
    cnt += 1

if right == left:
    print("LUCKY")
else:
    print("READY")
