test_case = int(input().rstrip())
arr = [0] * test_case  # char
result = []  # int
for i in range(test_case):
    arr[i] = input()
# 문자열로 입력받은 상태
for idx in range(test_case):
    total = 0
    for i in range(16):
        if (16-i-1) % 2 == 1:
            temp = int(arr[idx][(16-i-1)]) * 2
            if temp >= 10:
                # print(int(arr[idx][(16-i-1)]))
                total += int((int(str(temp)[0])) + (int(str(temp)[1])))
            else:
                total += temp
        else:
            total += int(arr[idx][(16-i-1)])

    # print(total)
    result.append(total)

for answer in result:
    # print(answer==73)
    # print(answer % 10)
    if answer % 10 == 0:
        print("T")
    else:
        print("F")

print(2+5+2+9+9+2+5+1+2+8+4+8+5+6+5)