def separate(p):
    left=0
    right=0
    idx=0
    while not (left>0 and right>0 and left==right):
        if(p[idx]==")"):
            left+=1
        else:
            right+=1
        idx+=1
    return (p[:idx],p[idx:])

def reverseStr(p):
    answer=""
    for i in p:
        if(i=="("):
            answer+=")"
        else:
            answer+="("
    return answer

def isRight(p):
    stack=[]
    for i in p:
        if(i=="("):
            stack.append("(")
        else:
            if(len(stack)==0):
                return False
            else:
                stack.pop()
    if(len(stack)==0):
        return True
    return False

def transform(p):
    if (len(p) == 0):
        return p
    u = ""
    v = p
    u_temp, v_temp = separate(v)
    if (isRight(u_temp)):
        u += u_temp
        return u+transform(v_temp)
    else:
        answer="("
        answer+=transform(v_temp)
        answer+=")"
        return answer+reverseStr(u_temp[1:-1])


def solution(p):
    if(isRight(p)):
        return p
    return transform(p)

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))