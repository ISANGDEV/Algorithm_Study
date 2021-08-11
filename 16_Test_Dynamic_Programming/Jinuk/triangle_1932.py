n = int(input())
mem = [[-1 for i in range(n)] for row in range(n)]
triangle = []
for i in range(n):
    triangle.append(tuple(map(int, input().split(" "))))
mem[0][0] = triangle[0][0] 

def tri(k):
    global mem, triangle
    n = k-1
    for i in range(k):
        if mem[n][i] >= 0:
            continue
        if i == 0:
            mem[n][i] = tri(k-1)[i] + triangle[n][i]
        elif i == n:
            mem[n][i] = tri(k-1)[i-1] + triangle[n][i]
        else:
            mem[n][i] = max(tri(k-1)[i-1] + triangle[n][i], tri(k-1)[i] + triangle[n][i])
    return mem[n]

print(max(tri(n)))