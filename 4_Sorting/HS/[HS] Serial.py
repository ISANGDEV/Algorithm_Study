import sys

guitar = []


n = int(sys.stdin.readline())

for i in range(n):
    temp = 0
    serial = sys.stdin.readline()
    for j in serial:
        if j.isdigit():
            temp+= int(j)
    guitar.append([serial.rstrip(),temp])

guitar.sort(key = lambda x:(len(x[0]),x[1],x[0]))
# 숫자 아스키 코드가 Alphabet보다 작으니까 이게 되는데, 만약 숫자가 사전 순으로 알파벳 보다 크다고 하면 ??

for i,j in guitar:
    print(i)
