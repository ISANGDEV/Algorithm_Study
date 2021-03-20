# 그리디 알고리즘이 뭐냐 . 지금 많이 먹을 수 있으면 먹는게 베스트임.
# 그러면 이 문제 적용하면 많이 태울 수 있으면 태우는게 베스트
# 두명을 어떻게 태울 수 있나 -> 가벼운 + 가벼운 / 가 + 무 / 무 + 무 로 조합을 했을 때 무무 는 불가능, 무무가 불가능하니까 가가도 불가능. 따라서 가 + 무가 best
def solution(people, limit):
    people.sort() # 사람 몸무게 대로 정렬하고
    index_ed = len(people) - 1
    index_st = 0
    cnt = 0  # 보트 개수

    while index_ed >= index_st : # index가 가운데에 왔다 -> 그 index에 해당하는 사람 1명만 보트 못 타고 남아있다.
        if people[index_ed] + people[index_st] > limit: # 만약 2명이 못탄다
            cnt += 1 # 보트 + 1
            index_ed -= 1 # 한명만 태워 보낸다
        else : # 두명 탈 수 있다.
            if len(people) > 1: # 사람이 두명 이상 남아 있다.
                index_ed -= 1 # 가장 무거운 사람 이랑
                index_st += 1 # 가장 가벼운 사람 태우면 됨
                cnt += 1 # 보트 + 1
            else :# 사람이 한명만 있다
                index_ed -= 1  # 걔 태워서 보낸다
                cnt += 1 # 보트  +1
    answer = cnt
    return answer
