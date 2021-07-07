n = int(input())

total = 0
for _ in range(n):
    c, k = map(int, input().split())

    if k > 0 and c > 0:
        temp = 0
        c = (c * k)
        k -= 1
        if k == 0:
            temp = c
        else:
            temp = (c * (2 ** k))
        total += temp
print(total % 10e9 + 7)
