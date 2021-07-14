def solution(n, build_frame):
    # frame = [x, y, a, b] x = 가로 , y 세로, a = 0기1보, b = 0삭1설
    result_frame = []
    for frame in build_frame:
        x, y, a, b = frame
        print(frame)
        # 설치
        if b == 1:
            result_frame.append([x, y, a])
            if not ok(result_frame):
                result_frame.remove([x, y, a])
                print("not build")
        # 삭제
        elif b == 0:
            result_frame.remove([x, y, a])
            if not ok(result_frame):
                # 어차피 xxx in result_frame 으로 검사하여 insert로 특정 위치에 넣을 필요 없다.
                result_frame.append([x, y, a])

        print(result_frame)
        print()

    result_frame.sort(key=lambda xx: (xx[0], xx[1], xx[2]))
    return result_frame


def ok(result_frame):
    for frame in result_frame:
        x, y, a = frame
        # 기둥이
        if a == 0:
            # 바닥의 위에 있거나
            if y == 0:
                continue
            # 기둥의 위에 있거나
            elif [x, y - 1, 0] in result_frame:
                continue
            # 보의 위에 있거나
            elif [x, y, 1] in result_frame or [x - 1, y, 1] in result_frame:
                continue
            # 다른 케이스 => False
            else:
                return False
        # 보가
        elif a == 1:
            # 왼끝 오끝 밑에 기둥이 있거나
            if [x + 1, y - 1, 0] in result_frame or [x, y - 1, 0] in result_frame:
                continue
            # 양쪽 끝이 다른 보와 동시 연결되어 있거나
            elif [x-1, y, 1] in result_frame and [x+1, y, 1] in result_frame:
                continue
            else:
                return False
    return True

# def check2():
#     result = True
#     for frame in result_frame:
#         # 기둥일때
#         if frame[2] == 0:
#             # 바닥 위에 있어야함
#             if frame[1] == 0:
#                 continue
#                 # result = True
#             # 기둥 아래 기둥 있어야 함
#             elif [frame[0], frame[1] - 1, 0] in result_frame:
#                 continue
#                 # result = True
#             # 기둥 아래 보 있어야 함
#             elif [frame[0] - 1, frame[1], 1] in result_frame:
#                 continue
#                 # result = True
#             else:
#                 result = False
#             if not result:
#                 return result
#         # 보일때
#         else:
#             # 보의 왼쪽 아래가 기둥.
#             if [frame[0] + 1, frame[1] - 1, 0] in result_frame:
#                 continue
#                 # result = True
#             elif [frame[0], frame[1] - 1, 0] in result_frame:
#                 continue
#                 # result = True
#             # 보의 오른쪽 아래가 기둥
#             elif [frame[0] + 1, frame[1], 0] in result_frame:
#                 continue
#                 # result = True
#             # 보의 오른쪽 왼쪽이 보
#             elif [frame[0] - 1, frame[1], 1] in result_frame and [frame[0] + 1, frame[1], 1] in result_frame:
#                 continue
#                 # result = True
#             else:
#                 result = False
#             if not result:
#                 return result
#
#     return result

ans = solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])
# ans = solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
#                    [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]])
print(ans)

