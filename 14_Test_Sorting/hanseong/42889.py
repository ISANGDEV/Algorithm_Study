def solution(N, stages):
    total=[[0]*4 for _ in range(N+2)]
    answer = [] 
    for stage in stages:
        total[stage][1]+=1
        for i in range(1,stage+1):
            total[i][0]+=1
    for i,item in enumerate(total):
        if(i)==0:
            continue
        if(item[0]==0):
            item[2]=0
        else:
            item[2]=item[1]/item[0]
        item[3]=i
    total=total[1:-1]
    total=sorted(total,key=lambda x: x[2], reverse=True)
    print(total)
    for i in range(0,len(total)):
        answer.append(total[i][3])
    return answer
