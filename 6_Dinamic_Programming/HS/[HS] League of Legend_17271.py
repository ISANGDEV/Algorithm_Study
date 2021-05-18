# 실패
# 메모리에서 걸린건가
# (n- x*m+x) C x
# (n- x*m+x)! / x! * (n-x*m)!
# 1이 n개 //nCn m 이 0 개
# 1이 n-m 개 : (n-m)C1 // m이 1개
# 1이 n - 2m 개 ( n- 2m)C2 // m이 2개
# 1이 n - 3m 개 (n-3m) C 3
# .... n//m = x 일때 m이 x개, 1은 n- x*m 개
# mCn = m! / (n!) (m-n)!

import sys
sys.setrecursionlimit(100000)

def fac(number):
    global dic

    if number in dic:
        return dic[number]
    elif number == 1 or number == 0:
        return 1
    else:
        dic[number] = number * fac(number-1)
        return dic[number]

dic = {}

n, m = map(int,sys.stdin.readline().split())

result = []

if n < m:
    print(0)
    sys.exit()

for i in range((n//m) + 1):
    temp = fac(n-i*m+i) / (fac(i) * fac(n -i*m))
    result.append(int(temp))

print(sum(result) % (1000000007))
