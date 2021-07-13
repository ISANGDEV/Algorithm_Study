import sys

n = (sys.stdin.readline())
n = n.rstrip()

length = len(n)
temp_l = 0
temp_r = 0

for i in range(length//2):
    temp_l += int(n[i])

for j in range((length//2),length,1):
    temp_r += int(n[j])


if temp_l == temp_r:
    print("LUCKY")
else:
    print("READY")

