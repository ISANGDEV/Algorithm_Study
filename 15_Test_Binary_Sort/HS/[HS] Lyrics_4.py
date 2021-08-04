def solution(words, queries):
    answer = []
    for i in queries:
        count = 0
        for j in words:
            temp = ""
            if len(i) != len(j):  # 길이가 다르면 패스
                continue
            else:
                for check_0, check_1 in zip(i, j):  # 길이가 같음.
                    if check_0 == check_1:
                        temp += check_0
                    else:
                        if check_0 == '?':
                            temp += check_1
            if temp == j:
                count += 1

        answer.append(count)
    return answer