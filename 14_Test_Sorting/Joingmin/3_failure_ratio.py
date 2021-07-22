def solution(N, stages):
    L=len(stages)
    ansDict={i+1:0 for i in range(N+1)}
    answer=[]
    for i in stages:
        ansDict[i]+=1
    for i in range(1,N+1):
        if(L==0):
            answer.append([0,i])
        else:
            answer.append([ansDict[i]/L,i])
            L-=ansDict[i]
    answer.sort(key=lambda x:(-x[0],x[1]))
    return list(map(lambda x:x[1],answer))

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))
print(solution(5, [2, 1, 2, 4, 2, 4, 3, 3]))