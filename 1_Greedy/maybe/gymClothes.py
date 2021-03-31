# 빌려주는 사람 입장에서 보면 되는걸 빌리는 입장에서 봐서 우선순위 정하고 혼자 쌩쇼함
# 코드 구상 시간을 조금 더 잡고, 찬찬히 생각해볼 것

def process(lost, reserve):
    answer = 0
    for i in lost:
        if i+1 in reserve:
            reserve.remove(i+1)
            answer += 1
        elif i-1 in reserve:
            reserve.remove(i-1)
            answer += 1
    return answer, reserve


def solution(n, lost, reserve):
    reserve_temp = reserve[:]
    for i in reserve_temp:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)
    secondary = [x for x in lost if x+1 in reserve and x-1 in reserve]
    priority = [x for x in lost if x not in secondary]
    a1, reserve = process(priority, reserve)
    a2, reserve = process(secondary, reserve)
    answer = n - len(lost) + a1 + a2
    return answer