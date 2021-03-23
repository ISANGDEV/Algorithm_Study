def solution(number, k):
    answer = ''
    startidx = 0
    endidx = 0
    choose = len(number) - k
    while True:
        idx = -1
        endidx = len(number)-1 - (choose-1)
        if endidx < startidx or choose == 0:
            break
        elif startidx == endidx:
            answer += number[startidx:]
            break
        maxval = -1
        for i in number[startidx:endidx+1]:
            if maxval < int(i):
                maxval = int(i)
            if maxval == 9:
                break
        idx = number[startidx:endidx+1].find(str(maxval))
        answer += str(maxval)
        startidx += idx+1
        choose -= 1
    return answer

solution("1924", 2)
solution("1231234", 3)
solution("4177252841", 4)
