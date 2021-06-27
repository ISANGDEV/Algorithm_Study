import sys

def binary(left,right,c):
    global house
    while left <= right:
        middle = (left + right) // 2
        temp = 1 #  공유기 개수 1개인 이유는 시작점에서는 설치하고 가니까 + 최소 갯수가 2개임. 만약 집이 2개라면 temp + 1 되서 2 되고 마무리
        cur_router = house[0] # 시작점. house[-1]에서 시작해서, for문 역순으로 해도 됨
        for i in range(1,len(house),0): # 첫번째 집은 했으니까 2번째 집부터. (cur_router)
            if house[i] - cur_router >= middle: # 마지막으로 공유기가 설치된 집에서, 다음 공유기 설치 가능 집 거리 비교
                temp += 1 # 설치가능하면 공유기 개수 +1
                cur_router = house[i] # 마지막으로 공유기 설치한 위치 갱신

        # 기준거리 정해서 설치 다 했으면 공유기 갯수로 비교. 
        if temp >= c : # 공유기가 너무 많다면 // 공유기 최대거리니까 = 이 여기에 들어감 ............
            left = middle + 1 # 거리 늘리고
        elif temp < c : # 공유기가 너무 적다면
            right = middle - 1 # 거리를 줄이고
            
    return right # 결과 반환 // 최댓값이니까 범위의 오른쪽 반환. left면 오답

n,c = map(int,sys.stdin.readline().split())
house = []


for i in range(n):
    house.append(int(sys.stdin.readline()))

house.sort()

left = 0 # 가능한 범위 최소 
right = house[-1] - house[0] #범위 최대

print(binary(left,right,c))
