s = input()
start = s[0]
before = ""
cnt = 0

for str in s:
    if before == start and before != str:
        cnt += 1
    before = str

print(cnt)