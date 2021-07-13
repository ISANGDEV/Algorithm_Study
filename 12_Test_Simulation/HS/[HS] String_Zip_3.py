def zip(string, number):
    temp = ""
    split = [string[i:i + number] for i in range(0, len(string), number)]
    count = 1
    for i in range(1, len(split)):
        pre, cur = split[i - 1], split[i]
        if pre == cur:
            count += 1
        else:
            if count > 1:
                temp += (str(count) + pre)
                count = 1`
            else:
                temp += pre
                count = 1

    if count > 1:
        temp += (str(count) + split[-1])
    else:
        temp += split[-1]

    return len(temp)


def solution(s):
    answer = 1000

    for i in range(1, len(s) + 1):
        answer = min(answer, zip(s, i))

    return answer