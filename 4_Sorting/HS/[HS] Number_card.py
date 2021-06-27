import sys
sys.setrecursionlimit(10000)

def search(card,number,left,right):
    criteria = (left + right) // 2
    if criteria < 0 or criteria >= len(card) or left > right:
        return

    middle = card[criteria]

    if number == middle:
        return 1
    elif middle > number:
        right = criteria - 1
    elif middle < number:
        left = criteria + 1

    return search(card,number,left,right)

n = int(sys.stdin.readline())
card = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
check = list(map(int,sys.stdin.readline().split()))


answer = ''
card.sort()

for i in check:
    if search(card,i,0,len(card)-1) == 1:
        answer += '1 '
    else:
        answer += '0 '

print(answer.rstrip())


"""for i in check:
    temp = 0
    for j in card:
        if i == j:
            temp = 1
        elif i < j:
            break



    if temp == 1 :
        answer += '1 '
    else:
        answer += '0 '

answer.rstrip()

print(answer)"""