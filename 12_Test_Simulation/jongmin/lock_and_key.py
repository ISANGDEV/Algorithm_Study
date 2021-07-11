def turnRight(arr):
    L=len(arr)
    ret = [[0]*L for _ in range(L)]
    for r in range(L):
        for c in range(L):
            ret[c][L-1-r] = arr[r][c]
    return ret

def solution(key, lock):
    M=len(key)
    N=len(lock)
    for _ in range(4):
        board = [[0] * (M*2+N) for _ in range(M*2+N)]
        for i in range(N):
            for j in range(N):
                board[M+i][M+j] = lock[i][j]
        for x in range(M+N):
            for y in range(M+N):
                status = True
                board = [[0] * (M * 2 + N) for _ in range(M * 2 + N)]
                for i in range(N):
                    for j in range(N):
                        board[M + i][M + j] = lock[i][j]
                for i in range(M):
                    for j in range(M):
                        board[x+i][y+j]+=key[i][j]
                for i in range(N):
                    for j in range(N):
                        if(board[M+i][M+j]==0 or board[M+i][M+j]==2):
                            status=False
                            break
                    if(status==False):
                        break
                if(status==True):
                    return True
        key=turnRight(key)
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))