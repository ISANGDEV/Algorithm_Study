import sys

def search(number):
    global dic

    if number in dic:
        return dic[number]
    elif number == 1 or number == 2:
        return 1
    else:
        dic[number] = search(number-1) + search(number-2)
        return dic[number]

# 1 1     / 1
# 2 10 / 1
# 3 101, 100 / 2
# 4 1010, 1000, 1001 / 3
# 5 10100, 10000,10001, 10010, 10101 / 5
# 6 101000, 100000,100010,100100,101010, 101001,100001,100101 / 8


n = int(sys.stdin.readline())

dic = {}

print(search(n))