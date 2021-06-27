import math

number = input("방 번호 입력")

count = {"0" : 0, "1" : 0, "2" : 0, "3" : 0,"4" : 0,"5" : 0,"7" : 0,"8" : 0,"A" : 0}
check = 0
result = []
for i in range(len(number)):
    if number[i] == "0" :
        count["0"] += 1
    elif number[i] == "1" :
        count["1"] += 1
    elif number[i] == "2" :
        count["2"] += 1
    elif number[i] == "3" :
        count["3"] += 1
    elif number[i] == "4" :
        count["4"] += 1
    elif number[i] == "5" :
        count["5"] += 1
    elif number[i] == "6" :
        count["A"] += 1
    elif number[i] == "7" :
        count["7"] += 1
    elif number[i] == "8" :
        count["8"] += 1
    elif number[i] == "9" :
        count["A"] += 1
key = math.ceil(count["A"]/2)

if key > count['0'] and key > count['1'] and key > count['2'] and key > count['3'] and key > count['4'] and key > count['5'] and key > count['7'] and key > count['8']:
    print(key)
else :
    result.append(count['0'])
    result.append(count['1'])
    result.append(count['2'])
    result.append(count['3'])
    result.append(count['4'])
    result.append(count['5'])
    result.append(count['7'])
    result.append(count['8'])
    result.sort()
    print(result[-1])

# 숫자 개수 중 가장 높은 수 만큼 숫자 세트 필요함
# 9999 -> 9가 4개 , 4세트 필요. but 6이랑 대체 가능. 따라서 2 세트
# 9996 -> 9가 3개, 6이 1개. 그러면 2세트 필요. -> 99 66은 9996으로 변환 가능하니까.
# 99996 -> 9가 4개 6이 1개. 3세트 필요. 999666 -> 999966으로 변환 가능. 5개 /2
# 9999996 -> 9가 6개 6이 1개. 4세트 -> 69/ 69/ 69/ 69 -> A가 8개 있으니, A가 7개 필요하다 7 /2 3.5 니까, 4개
# 15783 -> 모든 숫자가 1개씩 : 1세트면 됨.
# 115783 : 1이 2개 필요함. 2세트 필요함

#33333396 : 3이 6개 , A가 2개. 이러면 6세트가 필요 함.
#33339999 : 3이 4개 A가 4개. 이러면 4세트
#3399996 : 3이 2개, A가 5개 . 이러면 3세트 -> ceil(A/2)가 다른 숫자의 최대치 보다 크면 ceil (A/2)가 정답. 아니라면 다른 숫자 최대치가 정답.
