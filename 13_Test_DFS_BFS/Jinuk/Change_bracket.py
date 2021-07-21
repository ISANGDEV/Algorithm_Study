def partition(p):
    stack_count = 0
    idx = 0
    for char in p:
        if char == "(":
            stack_count += 1
        elif char == ")":
            stack_count -= 1
        idx += 1
        if stack_count == 0:
            break
    return p[:idx], p[idx:]

def isgood(p):
    stack_count = 0
    for char in p:
        if char == "(":
            stack_count += 1
        elif char == ")":
            stack_count -= 1
        if stack_count < 0:
            return False
    return True

def change(p):
    if p == "":
        return ""
    
    u, v = partition(p)
    if isgood(u):
        return u + change(v)
    else:
        answer = "("
        answer += change(v)
        answer += ")"
        u = u[1:-1]
        for char in u:
            if char == "(":
                answer += ")"
            else:
                answer += "("
        return answer

def solution(p):
    answer = ''
    answer = change(p)
    return answer