def solution(s):
    min_total = 1001
    for t in range(len(s)):
        min_temp = 0
        jump = t+1
        i = 0
        while i < len(s):
            temp = 1
            if s[i:i+jump] == s[i+jump:i+jump+jump]:
                while s[i:i+jump] == s[i+jump:i+jump+jump]:# 다음 거 , 다음거, 다음거
                    temp += 1
                    i += jump
                i += jump # 한번 검사 헀으니 + 1 까지 검사한것이고 i 도 jump 만큼
                min_temp += len(str(temp))+jump
            else:
                i += jump
                if i < len(s):
                    min_temp += jump
                else:
                    for _ in range(i-jump, len(s)):
                        min_temp += 1
                    break
        if min_temp < min_total:
            min_total = min_temp
    return min_total








print(solution("abcabcdede"))
