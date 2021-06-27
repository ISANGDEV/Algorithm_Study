import sys

# e : a
# em : ab
# m : b
# mh : bc
# h : c
# 문제 개최시 : a or ab + ab or b or bc + bc or c
# 재사용 불가능

def binary(left,right,e,em,m,mh,h):
    while left <= right:
        easy = e # 변수 옮겨 담고
        eamid = em
        mid = m
        midhi = mh
        high = h
        middle = (left + right) // 2 # 문제 대회 설정
        easy -= middle
        mid -= middle
        high -= middle # 일단 다 빼고

        if easy < 0 : # 모자란건 각각 대체 가능한 문제들로 채운다
            eamid = eamid + easy
            easy = 0
        if high < 0 :
            midhi = midhi + high
            high = 0

        if mid < 0 :
            for i in range(abs(mid)): # mid가 모자란만큼 대체가능한 문제들로 메꿔줌.
                if eamid > midhi:
                    eamid -= 1
                    mid += 1
                elif midhi > eamid:
                    midhi -= 1
                    mid += 1
                else:  # 여기서 중요한건 예전에 앞에서 풀었던 Greedy 체육복처럼 숫자가 같을 때 "왼쪽에서 오른쪽 방향"으로 부족한걸 채워주는것. 쉬움 -> 어려움 -> mid 채우기
                    #  반대로 어려움 -> 쉬움 -> mid를 midhi, eamid 순으로 채워도 됨. 방향만 일치시켜주면 ok
                    eamid -= 1
                    mid += 1

        # 다 매꾸고 나서 보니 대체 가능한 문제의 갯수가 모자라다면, 대회 횟수 줄여야 함
        if min(eamid,midhi) < 0:
            right = middle - 1
        # 대체 가능 문제가 남는다면, 대회 횟수 늘려도 ok
        elif min(eamid,midhi) >= 0:
            left = middle + 1


    return right

e, em, m, mh, h = map(int,sys.stdin.readline().split())

left = 0
right = (e + em + m + mh + h) // 3


print(binary(left,right,e,em,m,mh,h))
