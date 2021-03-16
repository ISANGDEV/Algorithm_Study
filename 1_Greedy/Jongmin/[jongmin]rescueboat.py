def solution(people, limit):
    people.sort(reverse=True)
    visited=[0 for i in range(len(people))]
    answer=greedy(people,visited,limit)
    return answer
def greedy(people, visited, limit):
    answer=0
    for i in range(len(people)):
        if(0 not in visited):
            return answer
        if(visited[i]==0 and people[i]<=limit):
            visited[i]=1
            for j in range(len(people)-1,i,-1):
                if (visited[j] == 0 and people[j] <= limit-people[i]):
                    visited[j] = 1
                    break
            answer+=1
    return answer
print(solution([70, 50, 80, 50],100))
print(solution([70, 80, 50],100))
print(solution([10,20,30,40,50,60,70,80,90], 100))
print(solution([20, 50, 50, 80], 100))
print(solution([40, 40, 40],100))
