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
        easy = e
        eamid = em
        mid = m
        midhi = mh
        high = h
        middle = (left + right) // 2
        easy -= middle
        mid -= middle
        high -= middle

        if easy < 0 :
            eamid = eamid + easy
            easy = 0
        if high < 0 :
            midhi = midhi + high
            high = 0

        if mid < 0 :
            for i in range(abs(mid)):
                if eamid > midhi:
                    eamid -= 1
                    mid += 1
                elif midhi > eamid:
                    midhi -= 1
                    mid += 1
                else:
                    eamid -= 1
                    mid += 1


        if min(eamid,midhi) < 0:
            right = middle - 1

        elif min(eamid,midhi) >= 0:
            left = middle + 1


    return right

e, em, m, mh, h = map(int,sys.stdin.readline().split())

left = 0
right = (e + em + m + mh + h) // 3


print(binary(left,right,e,em,m,mh,h))
