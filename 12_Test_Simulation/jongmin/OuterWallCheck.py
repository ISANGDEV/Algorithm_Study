from itertools import permutations
def solution(n, weak, dist):
    answer = 0
    weak_new=[i+n for i in weak]
    weak_new=weak+weak_new
    dist.sort(reverse=True)
    students=permutations(dist)
    for sets in students:
        studentidx=0
        cnt=1

        coverlen=sets[studentidx]
        weakIdx=0



    return answer

print(solution(12,[1, 5, 6, 10],[1, 2, 3, 4]))
print(solution(12,[1, 3, 4, 9, 10],[3, 5, 7]))