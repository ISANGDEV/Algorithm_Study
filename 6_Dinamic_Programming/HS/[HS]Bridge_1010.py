import sys

def fac(number):
    global memory

    if number in memory:
        return memory[number]
    elif number <= 1:
        return 1
    else:
        memory[number] = number * fac(number -1)
        return memory[number]

def bridge(m,n):
    result = fac(m) / (fac(n) * fac(m-n))
    return result

result = []
t = int(sys.stdin.readline())

memory = {}
# mCn = m! / (n! * (m-n)!)
for i in range(t):
    n, m = map(int,sys.stdin.readline().split())
    print(int(bridge(m,n)))

