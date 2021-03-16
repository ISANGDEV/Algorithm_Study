def solution(people, limit):
    answer=0
    people.sort(reverse=True)
    i=0
    while(i<len(people)):
        if(people[i]<=limit):
            value=people[i]
            del people[i]
            i-=1
            t=solution(people,limit-value)
            answer+=1
        i+=1
    return answer

print(solution([70, 50, 80, 50],100))
print(solution([70, 80, 50],100))
print(solution([10,20,30,40,50,60,70,80,90], 100))