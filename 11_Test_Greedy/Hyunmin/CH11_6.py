def solution(food_times, k):
    temp = 0
    _max = len(food_times)
    while True:
        for i in range(_max):
            if food_times[i]:   # 존재 한다면
                if temp > 0:
                    temp = 0
                if k < 1: #    네트워크 고치고 먹을 음식
                    return i+1
                food_times[i] -= 1
                k -= 1
            else:
                if temp >= _max:
                    return -1
                else:
                    temp += 1
                    continue

