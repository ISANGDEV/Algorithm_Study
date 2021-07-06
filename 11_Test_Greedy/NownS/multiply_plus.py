s = input()

val = 0

for str in s:
    val1 = val * int(str)
    val2 = val + int(str)
    if val1 > val2:
        val = val1
    else:
        val = val2

print(val)