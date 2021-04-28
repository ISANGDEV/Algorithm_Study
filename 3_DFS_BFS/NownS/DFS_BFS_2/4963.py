from collections import deque

queue = deque()
dx = [1,-1,0,0,1,1,-1,-1]
dy = [0,0,1,-1,1,-1,1,-1]
count_case = []

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    case_map = []
    
    for _ in range(h):
        case_map.append(list(map(int, input().split())))
    
    count = 0

    for i in range(h):
        for j in range(w):
            if case_map[i][j] == 0:
                pass
            else:
                count += 1
                queue.append((i, j))
                case_map[i][j] = 0
                while queue:
                    sampley, samplex = queue.popleft()
                    for a in range(8):
                        try:
                            aroundy = sampley+dy[a]
                            aroundx = samplex+dx[a]
                            if aroundx < 0 or aroundy < 0:
                                raise IndexError
                            if case_map[aroundy][aroundx] == 1:
                                queue.append((aroundy, aroundx))
                                case_map[aroundy][aroundx] = 0
                        except IndexError:
                            pass
    count_case.append(count)

for count in count_case:
    print(count)