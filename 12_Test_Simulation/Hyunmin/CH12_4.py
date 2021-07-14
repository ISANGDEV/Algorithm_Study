def solution(key, lock):
    main_map = Map(key, lock)

    # 총 4번 회전시켜 모두 확인
    for turned in range(4):
        for i in range(main_map.lock_size * 3):
            for j in range(main_map.lock_size * 3):
                main_map.paint(i, j)
                if main_map.check():  # check 한 후 2로 바뀐 것(자물쇠가 0->1로 변한 것은 2로 표시)은 다음번 계산을 위해 다시 0으로 변환
                    return True
                main_map.erase(i, j)
                # paint -> check -> erase
        main_map.turn()  # 시계 방향 90도 회전
    return False

class Map:
    # 해당 lock ( M * M ) 에서 (M*3 * M*3) 만큼 만들어 놓고 key 이동시키기 and 돌리기하며 find 하는 방식 ?
    # -> 비효율적. 가능할지 모르겠다. -> 확인 해 보니, 파이썬에서 초당 2000만에서 1억 번의 연산이 가능하여 위 방식 가능할듯.
    def __init__(self, key, lock):
        self.key_size = len(key)
        self.lock_size = len(lock)
        self.key = key
        self.lock = [[0] * (self.lock_size * 3) for _ in range(self.lock_size * 3)]
        for i in range(self.lock_size, self.lock_size * 2):
            for j in range(self.lock_size, self.lock_size * 2):
                self.lock[i][j] = lock[i - self.lock_size][j - self.lock_size]

    #  열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됩니다 ! ! ! -> 문제를 자세히 읽자
    def paint(self, i, j):
        for x in range(i, i + self.key_size):
            for y in range(j, j + self.key_size):
                if y >= self.lock_size * 3 or x >= self.lock_size * 3:
                    continue
                if self.key[x-i][y-j] > 0:
                    if self.lock[x][y] == 1:
                        return # 돌기가 겹치면 안된다.
                    if self.lock[x][y] == 1:
                        self.lock[x][y] = 3
                    if self.lock[x][y] == 0:
                        self.lock[x][y] = 2

    def erase(self, i, j):
        for x in range(i, i + self.key_size):
            for y in range(j, j + self.key_size):
                if y >= self.lock_size * 3 or x >= self.lock_size * 3:
                    continue
                if self.key[x-i][y-j] > 0:
                    if self.lock[x][y] == 1:
                        return # 돌기가 겹치면 안된다.
                    if self.lock[x][y] == 3:
                        self.lock[x][y] = 1
                    if self.lock[x][y] == 2:
                        self.lock[x][y] = 0

    def check(self):
        for i in range(self.lock_size, self.lock_size * 2):
            for j in range(self.lock_size, self.lock_size * 2):
                if self.lock[i][j] < 1:
                    return False
        return True

    # def print(self):
    #     for i in range(self.lock_size * 3):
    #         for j in range(self.lock_size * 3):
    #             print(self.lock[i][j], end=" ")
    #         print()

    def turn(self):
        # 시계 방향 90도로 key 회전
        new_arr = [[0] * self.key_size for _ in range(self.key_size)]  # [[0, 0, 0], [1, 0, 0], [0, 1, 1]] 의 형태
        for i in range(self.key_size):
            for j in range(self.key_size):
                new_arr[j][((self.key_size - 1) - i)] = self.key[i][j]
        self.key = new_arr
# print(solution([[0, 0, 0], [1, 0, 0]
