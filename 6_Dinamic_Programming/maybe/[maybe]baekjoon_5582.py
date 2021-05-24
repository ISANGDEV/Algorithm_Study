a = input()
b = input()

ans = 0

for i in range(len(a)):
    for j in range(i + ans + 1, len(a) + 1):
        tmp = str(a[i:j])
        if tmp in b:
            ans = j - i
        else:
            break

print(ans)