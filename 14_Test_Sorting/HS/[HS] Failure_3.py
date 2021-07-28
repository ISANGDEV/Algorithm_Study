def solution(N, stages):
    dic = {}
    num = len(stages)  # 분모
    for i in range(1, N + 1):
        if num != 0:
            count = stages.count(i)  # 해당 stage 실패인원 (분자)
            dic[i] = count / num  # 해당 stage 실패율
            num -= count  # 높은 스테이지 올라갈 때, 해당 스테이지보다 밑의 인원들은 제외 해야 함
        else:
            dic[i] = 0

    return sorted(dic, key=lambda x: dic[x], reverse=True)