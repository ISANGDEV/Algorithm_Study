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
    
