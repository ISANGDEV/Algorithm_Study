import sys
n,k = map(int,sys.stdin.readline().split())

a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))



a.sort()
b.sort()
b.reverse()

temp = 0

while temp < k :
    for i,j in zip(a,b):
        if i < j :
            a.remove(i)
            a.append(j)
            b.remove(j)

            temp += 1
            break

print(sum(a))