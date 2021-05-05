n, m = map(int, input().split())
numbers = []
sub = 9999999999
for _ in range(n):
    numbers.append(int(input()))
numbers.sort()

le = 0
r = 0

for i in range(n):
    while True:
        ogsub = sub
        if i+r >= n and i-le < 0:
            break
        if i + r < n:
            tmpsub1 = numbers[i + r] - numbers[i]
            if m <= tmpsub1 < sub:
                sub = tmpsub1
            elif tmpsub1 >= sub:
                r = r - 1
                break
            r += 1
        if i - le >= 0:
            tmpsub2 = numbers[i] - numbers[i - le]
            if m <= tmpsub2 < sub:
                sub = tmpsub2
            elif tmpsub2 >= sub:
                le = le - 1
                break
            le += 1
        if ogsub != sub:
            break

print(sub)