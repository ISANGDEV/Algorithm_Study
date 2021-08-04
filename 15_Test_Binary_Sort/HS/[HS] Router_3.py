import sys

def binary(left,right,arry):
    while left <= right:


        mid = (left + right) // 2
        current = arry[0]
        count = 1
        for  i in range(1,len(arry)):
            if arry[i] >= current + mid :
                count += 1
                current = arry[i]

        if count >= c: # 공유기 개수가 너무 많으면
            left = mid + 1 # 간격 늘리고
            answer = mid
        elif count < c: # 공유기 개수가 너무 적으면
            right = mid - 1 # 간격 줄이고
        # 최소의 최대 거리를 찾아야되니까 count >= c:
    return answer

n,c = map(int,sys.stdin.readline().split())
geo = []
# 인접한 두 공유기 사이 최대 거리
for i in range(n):
    geo.append(int(sys.stdin.readline()))

geo.sort()



result = binary(1,geo[-1]-geo[0],geo)

print(result)