n = int(input())

# arr = []
arr = [[0]*10 for i in range(10)]

# arr = [[0 for _ in range(501)] for _ in range(501)]
# for i in range(501):
#     arr[i] = [0]*501

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    # y층 만큼
    y_temp = y1 + 1
    for _ in range(y2-(y1+1)):
        x_temp = x1
        for _ in range((x2-x1) + 1):
            arr[x_temp][y_temp] = 1
            x_temp += 1
        y_temp += 1

total = 0
print(arr)
for i in range(10):
    total += sum(arr[i])

print(total)
