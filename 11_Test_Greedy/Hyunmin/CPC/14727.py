n = int(input())
arr = [0]*n
for i in range(n):
    arr[i] = int(input())

print(min(arr)*n)