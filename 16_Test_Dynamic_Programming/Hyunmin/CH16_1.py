dx = [-1, 0, 1]
T = int(input())
for _ in range(T): 
    N, M = map(int, input().split())
    golds = list(map(int, input().split()))

    idx = 0 
    golds_map = []
    dp_map = [[-1]*M for _ in range(N)]
    for i in range(N): 
        golds_map.append(golds[idx:idx + M])
        idx += M
        dp_map[i][0] = golds_map[i][0]

    for i in range(1, M): 
        for j in range(N): 
            # 현재 값 = 현재 값(golds_map) + max (상중하)
            # 상중하 검사 
            max_value = -1 
            for x in dx: 
                prev_x = x + j 
                prev_y = i - 1 
                if prev_x >= 0 and prev_x < N and prev_y >= 0: 
                    max_value = max(max_value, dp_map[prev_x][prev_y])                    
            dp_map[j][i] = golds_map[j][i] + max_value 

    result = 0 
    for i in range(N):
        result = max(result, dp_map[i][M-1])
    print(result)
    




#bfs
#import sys 
#from collections import deque 
#T = int(input())
#N, M = map(int, input().split())
#golds = deque(map(int, sys.stdin.readline().split()))
#golds_map = [[] for _ in range(N)]
#dp_map = [[-1]*M for _ in range(N)]
#
#def bfs(input_x, input_y):
#    q = deque()
#    q.append((input_x, input_y))
#    dp_map[input_x][input_y] = golds_map[input_x][input_y]
#    # 오른쪽 상, 오른쪽, 오른쪽 하 
#    dx = [-1, 0, 1]
#    # dy = [1, 1, 1]
#    while q: 
#        cur_x, cur_y = q.popleft() 
#        # 상 중 하
#        for x in dx: 
#            next_x = cur_x + x 
#            next_y = cur_y + 1
#            if next_x >= 0 and next_x + x < N and next_y < M: 
#                # 현 값 + 다음 값이 원래 있던 dp_map값 보다 크다면 삽입 
#                if dp_map[next_x][next_y] < dp_map[cur_x][cur_y] + golds_map[next_x][next_y]: 
#                    dp_map[next_x][next_y] = dp_map[cur_x][cur_y] + golds_map[next_x][next_y] 
#                    q.append((next_x, next_y))
#    
#
#
#
## 한 줄 입력을 2차원 배열로 변환 
#for i in range(N): 
#    for _ in range(M): 
#      golds_map[i].append(golds.popleft())
#
#for i in range(N): 
#    # 재귀 함수 필요 
#    bfs(i, 0)

#result = 0 
#for i in range(N):
#    result = max(result, dp_map[i][M-1])
