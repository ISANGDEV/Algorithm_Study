d=[[[-1,0],[-1,0]],[[1,0],[1,0]],[[0,-1],[0,-1]],[[0,1],[0,1]]]
result=10**6
def moves(p1, p2, board):
    L=len(board)
    ds=[-1,1]
    result = []
    if p1[0] == p2[0]:
        for d in ds:
            if 0<=p1[0] + d<L and 0<=p2[0] + d<L and board[p1[0] + d][p1[1]] == 0 and board[p2[0] + d][p2[1]] == 0:
                result.append((p1, [p1[0] + d, p1[1]]))
                result.append((p2, [p2[0] + d, p2[1]]))
    else:
        for d in ds:
            if 0<=p1[1] + d<L and 0<=p2[1] + d<L and board[p1[0]][p1[1] + d] == 0 and board[p2[0]][p2[1] + d] == 0:
                result.append(([p1[0], p1[1] + d], p1))
                result.append(([p2[0], p2[1] + d], p2))
    return result
def bfs(p1,p2,cnt,L,board,visited):
    global result
    if(cnt>result):
        return cnt
    if((p1[0]==L-1 and p1[1]==L-1)or(p2[0]==L-1 and p2[1]==L-1)):
        return cnt
    else:
        for dir in d:
            d1,d2=dir
            nextP1 = [p1[0] + d1[0], p1[1] + d1[1]]
            nextP2 = [p2[0] + d2[0], p2[1] + d2[1]]
            if((not [nextP1, nextP2] in visited) and
                    0<=nextP1[0]<L and 0<=nextP1[1]<L and 0<=nextP2[0]<L and 0<=nextP2[1]<L and
                    board[nextP1[0]][nextP1[1]]==0 and board[nextP2[0]][nextP2[1]]==0):
                visited.append([nextP1,nextP2])
                result=min(result, bfs(nextP1,nextP2,cnt+1,L,board,visited))
                visited.remove([nextP1,nextP2])
        turns=moves(p1,p2,board)
        for turn in turns:
            nextP1, nextP2 = turn
            if ((not [nextP1, nextP2] in visited) and
                    0 <= nextP1[0] < L and 0 <= nextP1[1] < L and 0 <= nextP2[0] < L and 0 <= nextP2[1] < L and
                    board[nextP1[0]][nextP1[1]] == 0 and board[nextP2[0]][nextP2[1]] == 0):
                visited.append([nextP1, nextP2])
                result = min(result, bfs(nextP1, nextP2, cnt + 1, L, board, visited))
                visited.remove([nextP1, nextP2])
        return result
def solution(board):
    N=len(board)
    visited=[]
    bfs([0,0],[0,1],0,N,board,visited)
    return result

print(solution(
    [[0, 0, 0, 1, 1],
     [0, 0, 0, 1, 0],
     [0, 1, 0, 1, 1],
     [1, 1, 0, 0, 1],
     [0, 0, 0, 0, 0]]))