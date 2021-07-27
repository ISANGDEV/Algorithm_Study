def solution(N, stages):
    answer = []
    count_sum = [0] * (N + 2)  # 계수 정렬에 쓰는 배열 (N = 500이하) 
    count_stages = 0  # stages 의 길이 
    for i in stages:
        count_sum[i] += 1
        count_stages += 1
    for i in range(1, N+1):
        first, sec = count_sum[i], count_stages - count_sum[i]  # 실패율 구하는 first / sec 
        if first <= 0 and sec > 0:
            answer.append((0, i))
        elif first > 0 and sec <= 0:
            answer.append((count_sum[i], i))
        else:
            answer.append((first / sec, i))  # float() 사용 안해도 같은 결과
            count_stages -= first
    answer.sort(key=lambda x: -x[0])  # 순서대로 append 되서 lambda x: (-x[0], x[1]) 와 같은 결과
    answer = [x[1] for x in answer]
    return answer
