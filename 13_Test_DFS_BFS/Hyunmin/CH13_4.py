def solution(p):
    if p == "" or is_right(p):
        return "" if p == "" else p

    u, v = "", ""
    op = p[0]
    min_op = 1
    max_idx = 0
    for i in range(1, len(p)):
        if op == p[i]:
            min_op += 1
        else:
            min_op -= 1

        if min_op == 0:
            max_idx = i
            break
    u = p[0:max_idx + 1]
    v = p[max_idx + 1:]
    if is_right(u):
        u += solution(v)
        # do 1.단계부터
    else:
        # do 4.단계부터
        u = not_right(u, v)
    return u

def not_right(u, v):
    result = "("
    result += solution(v)
    result += ")"
    before = u[1:len(u) - 1]
    after = ""
    for i in range(len(before)):
        if before[i] == "(":
            after += ")"
        elif before[i] == ")":
            after += "("
    u = result + after
    return u


def is_right(w):
    stack = []
    for i in range(len(w)):
        if w[i] == "(":
            stack.append("(")
            pass
        else:
            if stack and stack[len(stack) - 1] == "(":
                stack.pop()
    if stack:
        return False
    return True


def is_balanced(w):
    total = 0
    for i in range(len(w)):
        if w[i] == "(":
            total += 1
        else:
            total -= 1

    if total:
        return False
    return True


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))

