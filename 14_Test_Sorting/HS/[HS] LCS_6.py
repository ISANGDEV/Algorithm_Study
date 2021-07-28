import sys

len1 =' ' + sys.stdin.readline().rstrip()
len2 =' ' + sys.stdin.readline().rstrip()


check = [[0 for i in range(len(len2))] for j in range(len(len1))]

result = -1
for i in range(1,len(len1)):
    for j in range(1,len(len2)):
        if len1[i] == len2[j] :
            check[i][j] = check[i-1][j-1] + 1
        else:
            check[i][j] = max(check[i-1][j], check[i][j-1])

print(check[-1][-1])
