n = int(input())
arr = []
for _ in range(n):
    arr.append((input()))

arr.sort()

for i in range(7):
    print(arr[i])

