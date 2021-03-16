def solution(number, k):
    k=len(number)-k
    number+="0"
    answer = ''
    leftlimit=0
    for i in range(k):
        temp=number[leftlimit]
        idx=leftlimit
        end=len(number)-(k-i)
        for j in range(leftlimit,end):
            item=number[j]
            if(item=="9"):
                temp=item
                idx=j
                break
            elif(item>temp):
                temp=item
                idx=j
        answer+=temp
        leftlimit=idx+1
    return answer
print(solution("1924",2)=="94")
print(solution("1231234",3)=="3234")
print(solution("4177252841",4)=="775841")