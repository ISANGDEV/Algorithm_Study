DELETE=0
INSTALL=1
KIDUNG=0
BO=1
def isValid(kidungs,bos):
    status=True
    for k in kidungs:
        x,y=k
        if (y == 0 or [x, y - 1] in kidungs or [x - 1, y] in bos or [x,y] in bos):
            pass
        else:
            status=False
            return status
    for b in bos:
        x,y=b
        if([x,y-1] in kidungs or [x+1,y-1] in kidungs):
            pass
        elif([x-1,y] in bos and [x+1,y] in bos):
            pass
        else:
            status=False
            return status
    return status
def solution(n, build_frame):
    result=[]
    kidungs=[]
    bos=[]
    for _ in build_frame:
        x,y,a,b=_
        if(a==KIDUNG):
            if(b==INSTALL):
                if(isValid(kidungs+[[x,y]],bos)):
                    result.append([x,y,a])
                    kidungs.append([x,y])
            elif(b==DELETE):
                result.remove([x,y,a])
                kidungs.remove([x,y])
                if(not isValid(kidungs,bos)):
                    result.append([x,y,a])
                    kidungs.append([x,y])
        else:
            if (b == INSTALL):
                if (isValid(kidungs, bos + [[x, y]])):
                    result.append([x, y, a])
                    bos.append([x, y])
            elif (b == DELETE):
                result.remove([x, y, a])
                bos.remove([x, y])
                if (not isValid(kidungs, bos)):
                    result.append([x, y, a])
                    bos.append([x, y])
    result.sort(key=lambda x: x[0]*10001+x[1]*101+x[2])
    return result

print(solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))