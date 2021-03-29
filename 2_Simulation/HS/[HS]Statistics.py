import math

count = int(input("개수 입력하기"))
number = []
dict = {}
sum = 0
# 산술평균
# 중앙값
# 최빈 값
# 범위


for i in range(count):
    number.append(int(input("숫자 입력하기")))

number.sort()

for i in number:
    sum = sum + i

average = sum / count

middle = number[math.floor(len(number)/2)]

for i in range(count):
    dict[number[i]] = number.count(number[i])
most = list(dict.items())
most.sort(key = lambda x:x[1])

most_count = max([most[i][1] for i in range(len(most))])
most_list = []

if len(most) == 1 :
    most_result = most[0][0]

else :
    for i in range(len(most)):
        if most[i][1] == most_count:
            most_list.append(most[i][0])

    most_list.sort()

    if len(most_list) == 1:
        most_result = most_list[0]
    else :
        most_result = most_list[1]





"""for i in range(len(most)-1):
    cmp = most[i][1]
    temp = most[i+1][1]
    if cmp < temp :
        most_result = most[i][0]
        break

    elif cmp == temp :
        continue"""


range = number[-1] - number[0]


print(average, middle, most_result,range, sep = '\n')
