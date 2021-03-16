#투포인터 알고리즘으로 해결
def solution(people, limit):
    people.sort(reverse=True)
    answer=0
    i = 0
    j = len(people) - 1
    while (i <= j):
        if (people[j] <= limit - people[i]):
            j-=1
        i+=1
        answer += 1
    return answer
print(solution([70, 50, 80, 50],100))
print(solution([70, 80, 50],100))
print(solution([10,20,30,40,50,60,70,80,90], 100))
print(solution([20, 50, 50, 80], 100))
print(solution([40, 40, 40],100))
