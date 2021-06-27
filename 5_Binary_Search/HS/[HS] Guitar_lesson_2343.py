import sys

def binary(left,right,m):
    global length


    while left <= right:
        temp = 0 # 블루레이에 들어간 강의들의 길이 합
        sum_blueray = 0  # 블루레이 개수
        middle = (left + right) // 2
        for i in length:
            if temp + i <= middle: # 더 넣을수 있으면
                temp += i # 더 넣고
            else:
                temp = i # 못 넣는다면
                sum_blueray += 1 # 새 블루레이에 강의 담기

        if temp > 0: # 강의가 들어있는 블루레이가 있다면 // 더 넣을 수 있는 공간이 있지만 강의가 없어서 넣지못한
            sum_blueray += 1 # 이것도 블루레이 개수 + 1

        if sum_blueray > m : # 블루레이 갯수가 너무 많다면
            left = middle + 1 # 블루레이 크기를 키우고
        elif sum_blueray <= m: # 갯수가 너무 적으면
            right = middle - 1 # 

    return left

n,m = map(int,sys.stdin.readline().split())

length = list(map(int,sys.stdin.readline().split()))

left = max(length) # 블루레이 개수가 강의의 수와 동일할 때 최대가 됨. 이 때 블루레이 크기는 최소가 됨.
right = sum(length) # 블루레이 개수가 1개일 때, 크기는 최대가 됨
print(binary(left,right,m))
