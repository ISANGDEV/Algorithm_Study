numA = int(input())
a = list(map(int, input().split()))
numB = int(input())
b = list(map(int, input().split()))

a = sorted(a)

for i in b:
    first = 0
    last = numA - 1

    while first <= last:
        mid = (first + last) // 2
        if a[mid] == i:
            print(1, end=' ')
            break
        elif a[mid] > i:
            last = mid - 1
        else:
            first = mid + 1
    else:
        print(0, end=' ')




