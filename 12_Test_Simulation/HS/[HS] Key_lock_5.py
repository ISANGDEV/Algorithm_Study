def rotation(key):
    l = len(key) - 1
    temp = [[0] * len(key) for i in range(len(key))]
    for i in range(len(key)):
        for j in range(len(key)):
            temp[j][l] = key[i][j]  # j랑 i 돌려서

        l -= 1  # l은 하나씩 줄면서 반복
    return temp


def insert(key, lock, start_i, start_j, end):
    length = (2 * len(key)) + len(lock) - 2
    background = [[0 for i in range(length)] for j in range(length)]  # 0으로 다 채운 배경 생성

    # 배경에 key + lock 으로 겹침
    for i in range(len(key)):
        for j in range(len(key)):
            background[start_i + i][start_j + j] = key[i][j]

    for i in range(len(key) - 1, end):
        for j in range(len(key) - 1, end):
            background[i][j] += lock[i - len(key) + 1][j - len(key) + 1]
            if background[i][j] != 1:
                return False

    return True


def solution(key, lock):
    end = len(key) + len(lock) - 1
    for k in range(4):
        for i in range(end):
            for j in range(end):
                start_i = i
                start_j = j
                if insert(key, lock, start_i, start_j, end) == True:
                    return True
        # key 4번(360도) 돌려가면서 한번 씩 삽입
        key = rotation(key)

    return False