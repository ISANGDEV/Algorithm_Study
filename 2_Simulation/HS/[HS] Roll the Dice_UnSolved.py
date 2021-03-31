n,m,x,y,k = map(int, input("세로, 가로, 좌표x, 좌표y, 명령 개수").split())

dice = [0,0,0,0,0,0]
pos_now =[x,y]
#dice = [맨위 ,북,동, 서, 남, 맨 아래]
#dice = [1,2,3,4,5,6]

# 동쪽은 1 서쪽은 2 북쪽이 3 남쪽이 4
def turn_1(): # 동
    global pos_now
    global dice
    pos_now[1] = pos_now[1] + 1
    dice_old = dice
    dice[0] = dice_old[3]
    dice[2] = dice_old[0]
    dice[5] = dice_old[2]
    dice[3] = dice_old[5]
    print(dice)
def turn_2(): # 서
    global pos_now
    global dice
    pos_now[1] = pos_now[1] - 1
    dice_old = dice
    dice[3] = dice_old[0]
    dice[0] = dice_old[2]
    dice[5] = dice_old[3]
    dice[2] = dice_old[5]
    print(dice)
def turn_3(): # 북
    global pos_now
    global dice
    pos_now[0] = pos_now[0] - 1
    dice_old = dice
    dice[0] = dice_old[4]
    dice[1] = dice_old[0]
    dice[5] = dice_old[1]
    dice[4] = dice_old[5]
    print(dice)
def turn_4(): # 남
    global pos_now
    global dice
    pos_now[0] = pos_now[0] + 1
    dice_old = dice
    dice[0] = dice_old[1]
    dice[4] = dice_old[0]
    dice[1] = dice_old[5]
    dice[5] = dice_old[4]
    print(dice)


#index

# 남쪽 1 -> 0 이 되고, 0 -> 4가 되고, 4가 5가 되고, 5 -> 1가 됨. 2과 3는 그대로
# 동쪽 0 -> 2이 되고, 2 -> 5, 5 -> 3, 3 -> 0 1이랑 4는 그대로
# 북쪽 4 ->0 , 0-> 1 , 1-> 5 , 5-> 4, 2과 3는 그대로
# 서쪽 0 -> 3, 2-> 0, 5-> 2, 3-> 5 1이랑 4는 그대로


# 주사위 값 변경 실제 위치
# 남쪽 2 -> 1 이 되고, 1 -> 5가 되고, 5가 6이 되고, 6 -> 2가 됨. 3과 4는 그대로
# 동쪽 1 -> 3이 되고, 3 -> 6, 6 -> 4, 4 -> 1, 2랑 5는 그대로
# 북쪽 5 ->1 , 1-> 2 , 2-> 6 , 6-> 5, 3과 4는 그대로
# 서쪽 1 -> 4, 3-> 1, 6-> 3, 4-> 6 2랑 5는 그대로





# 동쪽은 1 서쪽은 2 북쪽이 3 남쪽이 4
info = []

for j in range(n):
    info.append(list(map(int, input("맵 정보 입력").split())))


print(info)
# map으로 만든건 인덱싱이 안댐
command = map(int,input("명령 입력").split())
command = list(command)

info[pos_now[0]][pos_now[1]] = 0

for i in range(k):
    if command[i] == 1 and (pos_now[1] <= len(info[0]) - 2) :
        turn_1()
        #print(dice[0], '\n')
        if info[pos_now[0]][pos_now[1]] == 0 :
            info[pos_now[0]][pos_now[1]] = dice[5]
        elif info[pos_now[0]][pos_now[1]] != 0 :
            dice[5] = info[pos_now[0]][pos_now[1]]
            #print(dice[5])
            info[pos_now[0]][pos_now[1]] = 0
        #print(dice[0], '\n') # 이러니까 안나오지 맵이랑 돌리고 나서 하는게 맞다고 생각해서 밑에다가 넣었는데 상관이 없네
    elif command[i] == 2 and (pos_now[1] >= 1) :
        turn_2()
        #print(dice[0], '\n')
        if info[pos_now[0]][pos_now[1]] == 0 :
            info[pos_now[0]][pos_now[1]] = dice[5]
        elif info[pos_now[0]][pos_now[1]] != 0:
            dice[5] = info[pos_now[0]][pos_now[1]]
            #print(dice[5])
            info[pos_now[0]][pos_now[1]] = 0

    elif command[i] == 3 and (pos_now[0] >= 1) :
        turn_3()
        #print(dice[0], '\n')
        if info[pos_now[0]][pos_now[1]] == 0 :
            info[pos_now[0]][pos_now[1]] = dice[5]
        elif info[pos_now[0]][pos_now[1]] != 0:
            dice[5] = info[pos_now[0]][pos_now[1]]
            #print(dice[5])
            info[pos_now[0]][pos_now[1]] = 0

    elif command[i] == 4 and (pos_now[0] <= len(info) - 2) :
        turn_4()
        #print(dice[0], '\n')
        if info[pos_now[0]][pos_now[1]] == 0 :
            info[pos_now[0]][pos_now[1]] = dice[5]
        elif info[pos_now[0]][pos_now[1]] != 0 :
            dice[5] = info[pos_now[0]][pos_now[1]]
            #print(dice[5])
            info[pos_now[0]][pos_now[1]] = 0

    print(dice[0], '\n')
