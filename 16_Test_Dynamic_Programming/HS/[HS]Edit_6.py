import sys

str_a = sys.stdin.readline()
str_b = sys.stdin.readline()


a_len = len(str_a)
b_len = len(str_b)


matrix = [[0 for i in range(a_len+1)] for j in range(b_len+1)]
#  a a a a
# b
# b
# b

for i in range(1,a_len+1):
    matrix[0][i] = i

for j in range(1,b_len+1):
    matrix[j][0] = j


for i in range(1, a_len + 1):
    for j in range(1, b_len + 1):
        if str_a[i-1] == str_b[j-1]:
            matrix[j][i] = matrix[j-1][i-1]

        elif str_a[i-1] != str_b[j-1]:
            matrix[j][i] = 1+ min(matrix[j-1][i-1],matrix[j-1][i],matrix[j][i-1])


print (matrix[-1][-1])

