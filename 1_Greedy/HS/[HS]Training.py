def solution(n, lost, reserve):
    std_lost = set(lost) - set(reserve) # 옷이 없는 놈
    std_reserve = set(reserve) - set(lost) # 옷 남는 놈
    # 2개 줬다가 1개 훔쳐질 수도 있는데, 이러면 남는 것도 아니고 없는 것도 아님. 그래서 차집합 써야 함

    for i in std_reserve : # 남는 놈들만 줄 수 있으니까, 반복 조건으로
        x = i - 1 # 남는놈 보다 작은
        y = i + 1 # 남는놈 보다 큰
        if x in std_lost: # 작은놈이 없다면,
            std_lost.remove(x) # 옷을 준다
        elif y in std_lost: # 작은놈은 있고 큰놈이 없다면
            std_lost.remove(y) # 큰놈 준다

# 남는 놈들이 다 주고 나면
# 전체 - 없는놈 = 수업 가능한 사람

    answer = n - len(std_lost)

    return answer
