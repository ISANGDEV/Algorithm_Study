n = int(input())

arr = []
total = 0
for _ in range(n):
    c, k = map(int, input().split())
    if k > 0:
        total += (c*k)

print(total)

