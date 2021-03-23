def solution(name):
    answer = 0
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in name:
        answer += min(alphabet.index(i), 26-alphabet.index(i))
    mov1 = len(name.rstrip("A")) - 1    # 앞으로만 가는경우
    mov2 = len(name.lstrip("A"))        # 뒤로만 가는경우
    idx = 0
    n = 1
    while True:
        tmp = name.find("A"*n)
        if tmp == -1:
            break
        idx = tmp
        n += 1                      # A가 가장 많은 곳 위치 찾기
    mov3 = 1000000000000
    if idx != 0 and idx != len(name.rstrip("A"))-1:
        # A가 가장 많은 곳이 맨앞 또는 맨 뒤쪽인 경우 배제
        mov3 = (idx-1)*2 + len(name) - (idx + n - 1)    
        # A가 가장 많은 곳을 기준으로 갔다가 돌아오는 경우
    answer += min(mov1, mov2, mov3)
    return answer

solution("JEROEN")
solution("JAN")
