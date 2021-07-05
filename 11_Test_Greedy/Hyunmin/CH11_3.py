import sys
s = sys.stdin.readline().rstrip()

if s.count('1') < s.count('0'):
    # 1보다 0이 크므로 1을 뒤집어야 한다.
    # -> 연속되어있는 1이 몇 개인지 세야 함
    # 쭉 탐색 ?
    count = 0
    tf = False
    for i in s:
        if i == '1':
            tf = True
        else:
            if tf:
                count += 1
                tf = False
    if tf:  # 00011 마지막 경우
        count += 1
    print(count)

else:
    count = 0
    tf = False
    for i in s:
        if i == '0':
            tf = True
        else:
            if tf:
                count += 1
                tf = False
    if tf:  # 11100 마지막 경우
        count += 1
    print(count)


