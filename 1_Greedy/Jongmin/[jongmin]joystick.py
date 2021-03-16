def solution(name):
    N=len(name)
    pos=0
    initString=['A' for i in range(N)]
    initString[0]=name[0]
    answer=min(ord(name[0])-ord('A'),ord('Z')-ord(name[0])+1)
    while(''.join(initString)!=name):
        left=pos
        right=pos
        while(True):
            left-=1
            right+=1
            if (list(name)[right] != 'A' and initString[right] == 'A'):
                answer += right - pos
                pos = right
                break
            elif(list(name)[left]!='A' and initString[left]=='A'):
                answer+=pos-left
                pos=left
                break
        answer += min(ord(name[pos]) - ord('A'), ord('Z') - ord(name[pos])+1)
        initString[pos]=name[pos]
    return answer

print(solution("BBBAAAB"))#9
print(solution("ABABAAAAABA")) #11