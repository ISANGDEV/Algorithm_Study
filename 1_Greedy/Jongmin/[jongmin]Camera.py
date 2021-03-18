def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1],reverse=False)
    i=0
    while(i<len(routes)):
        start,end=routes[i]
        while(i+1<len(routes) and end>=routes[i+1][0]):
            i+=1
        i+=1
        answer+=1
    return answer

print(solution([[-20,10], [-14,-5], [-18,-13], [-5,-3]])) #2
print(solution([[0,2],[2,3],[3,4],[4,6]] ))
print(solution([ [0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15] ]))