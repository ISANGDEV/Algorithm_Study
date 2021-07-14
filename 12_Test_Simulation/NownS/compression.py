def solution(s):
    answer = 0
    min = len(s)
    for i in range(1, len(s) // 2 + 1):
        s_length = 0
        idx = 0
        before = ""
        zip_count = 0
        while True:
            if s[idx:idx+i] != before:
                before = s[idx:idx+i]
                if len(before) != i:
                    s_length += len(before)
                    break
                s_length += i
                zip_count = 1
            else:
                if zip_count == 1 or zip_count == 9 or zip_count == 99 or zip_count == 999:
                    s_length += 1
                zip_count += 1
            idx += i
            if idx == len(s):
                break
        if s_length < min:
            min = s_length
    answer = min
    return answer