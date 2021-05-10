import sys

def binary(left,right,c):
    global house
    while left <= right:
        middle = (left + right) // 2
        temp = 1 #  공유기 개수
        cur_router = house[0]
        for i in range(len(house)):
            if house[i] - cur_router >= middle:
                temp += 1
                cur_router = house[i]

        if temp >= c : # 공유기가 너무 많다면
            left = middle + 1 # 거리 늘리고
        elif temp < c : # 공유기가 너무 적다면
            right = middle - 1 # 거리를 줄이고



    return right



n,c = map(int,sys.stdin.readline().split())
house = []


for i in range(n):
    house.append(int(sys.stdin.readline()))

house.sort()

left = 0
right = house[-1] - house[0]

print(binary(left,right,c))