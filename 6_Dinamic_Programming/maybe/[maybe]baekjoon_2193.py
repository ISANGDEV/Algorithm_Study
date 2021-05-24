n = int(input())

d0 = [0] * 91
d1 = [0] * 91

d0[1], d1[1] = 0, 1
d0[2], d1[2] = 1, 0

for i in range(3, n + 1):
    d0[i] = d0[i-1] + d1[i-1]
    d1[i] = d0[i-1]

print(d0[n] + d1[n])
