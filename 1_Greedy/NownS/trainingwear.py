def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    lost_reserve_set = set(lost + reserve)
    lost_new = list(lost_reserve_set - set(reserve))
    reserve_new = list(lost_reserve_set - set(lost))
    for i in reserve_new:
        j = 0
        while j < len(lost_new):
            if i-1 == lost_new[j] or i+1 == lost_new[j]:
                lost_new.pop(j)
                break
            j = j+1
    answer = n - len(lost_new)
    return answer
solution(5, [2, 4], [1, 3, 5])
solution(5, [2, 4], [3])
solution(3, [3], [1])
