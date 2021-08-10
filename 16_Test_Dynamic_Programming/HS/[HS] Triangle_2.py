def solution(triangle):
    for rows in range(1, len(triangle)):
        for index in range(rows + 1):
            if index == 0:
                triangle[rows][0] += triangle[rows - 1][0]
            elif index == rows:
                triangle[rows][index] += triangle[rows - 1][index - 1]
            # [2][2] [1][1]
            else:
                triangle[rows][index] += max(triangle[rows - 1][index - 1], triangle[rows - 1][index])

    return max(triangle[-1])