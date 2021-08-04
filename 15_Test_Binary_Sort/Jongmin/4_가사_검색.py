##해설좀 보고함
from bisect import bisect_left, bisect_right
def solution(words, queries):
    answer = []
    wordlist = {}
    reversedWordList = {}
    for word in words:
        L=len(word)
        if L in wordlist:
            wordlist[L].append(word)
        else:
            wordlist[L]=[word]
        if L in reversedWordList:
            reversedWordList[L].append(word[::-1])
        else:
            reversedWordList[L]=[word[::-1]]
    for w in wordlist:
        wordlist[w].sort()
    for w in reversedWordList:
        reversedWordList[w].sort()
    for q in queries:
        N = len(q)
        if(N not in wordlist):
            answer.append(0)
        elif(q[0]=='?'):
            q=q[::-1]
            left = bisect_left(reversedWordList[N],q.replace('?','a'))
            right=bisect_right(reversedWordList[N],q.replace('?','z'))
            answer.append(right-left)
        else:
            left = bisect_left(wordlist[N],q.replace('?','a'))
            right=bisect_right(wordlist[N],q.replace('?','z'))
            answer.append(right-left)
    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
