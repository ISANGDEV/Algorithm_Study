import sys

t = int(sys.stdin.readline())
test = []
for i in range(t):
    test.append(str(sys.stdin.readline()))

for number in test:
    odd = int(number[15])+ int(number[13]) + int(number[11]) + int(number[9]) + int(number[7]) + int(number[5]) + int(number[3]) + int(number[1])
    temp = 0
    for i in range(0,16,2):
        if int(number[i]) >= 5:
            temp += int(str(int(number[i]) * 2)[0]) + int(str(int(number[i]) * 2)[1])
        else:
            temp += int(number[i]) * 2
    if (odd + temp) % 10 == 0:
        print("T")
    else:
        print("F")