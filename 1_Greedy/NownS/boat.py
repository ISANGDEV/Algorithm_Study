def solution(people, limit):
    people.sort()
    rightidx = len(people)
    for i in range(len(people)):
        if people[i] + people[i+1] > limit:
            break
        while True:
            rightidx -= 1
            if people[i] + people[rightidx] <= limit:
                people.pop(rightidx)
                break
    answer = len(people)
    return answer

solution([70, 50, 80, 50], 100)
solution([70, 80, 50], 100)
