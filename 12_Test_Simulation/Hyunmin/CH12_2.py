s = input()
list = []
num = 0
for i in range(len(s)):
    if s[i].isdigit():
        num += int(s[i])
    else:
        list.append(s[i])
list.sort()
for i in list:
    print(i, end="")
if num != 0:
    print(num)
# list를 문자열로 변환
# print(''.join(list))
# chr -> 아스키 코드 숫자를 문자로
# ord -> 문자를 아스키코드 숫자로
# isdigit
# isalpha


# K1KA5CB7



