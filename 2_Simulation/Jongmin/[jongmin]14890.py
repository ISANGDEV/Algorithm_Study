N,L=map(int,input().split())
maparr=[]
for i in range(N):
    maparr.append(list(map(int,input().split())))
result=0
def isPossible(line,N):
    isPossesed=[False]*N
    cur = line[0]
    status = True
    for j in range(N):
        if (line[j] != cur):
            if (line[j] == cur + 1):
                cnt = 0
                for k in range(j - 1, -1, -1):
                    if (line[k] != cur or isPossesed[k]):
                        break
                    cnt += 1
                if (cnt < L):
                    status = False
                    break
                else:
                    for k in range(j - L, j):
                        isPossesed[k] = True
            elif (line[j] == cur - 1):
                cnt = 0
                for k in range(j, N):
                    if (line[k] != line[j] or isPossesed[k]):
                        break
                    cnt += 1
                if (cnt < L):
                    status = False
                    break
                else:
                    for k in range(j, j + L):
                        isPossesed[k] = True
            else:
                status = False
                break
        cur = line[j]
    return status
for i in range(N):
    #세로
    linearr=[]
    for j in range(N):
        linearr.append(maparr[j][i])
    if(isPossible(linearr,N)):
        result+=1
    #가로
    linearr=[]
    for j in range(N):
        linearr.append(maparr[i][j])
    if(isPossible(linearr,N)):
        result+=1
print(result)