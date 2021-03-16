def solution(n, lost, reserve):
    lost.sort()
    templost=[i for i in lost]
    for st in templost:
        if st in reserve:
            reserve.remove(st)
            lost.remove(st)
    result=n-len(lost)
    for st in lost:
        if(st-1 in reserve):
            reserve.remove(st-1)
            result+=1
        elif(st+1 in reserve):
            reserve.remove(st+1)
            result+=1
    return result

print(solution(5,[2, 4],[1, 3, 5])==5)
print(solution(5,[2, 4],[3])==4)
print(solution(3,[3],[1])==2)
print(solution(7,[1, 2, 3, 4, 5, 6, 7],[1, 2, 3]))
print(solution(5,[2, 3, 4],[1, 2, 3])==4)
