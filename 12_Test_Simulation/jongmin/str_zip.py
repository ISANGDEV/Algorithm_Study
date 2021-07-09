def zipstr(s,l):
    newstr=""
    token=s[:l]
    cnt = 1
    for i in range(l,len(s),l):
        compToken=s[i:i+l]
        if(token==compToken):
            cnt+=1
        else:
            if(cnt!=1):
                newstr+=str(cnt)+token
            else:
                newstr+=token
            cnt = 1
            token=compToken
    if (cnt != 1):
        newstr += str(cnt) + token
    else:
        newstr += token
    return len(newstr)

def solution(s):
    L=len(s)//2
    result=len(s)
    for i in range(1,L+1):
        result=min(result,zipstr(s,i))
    return result

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))