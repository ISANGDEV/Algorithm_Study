def card_game(table, n):
    ans = 0
    for i in range(n):
        m = min(table[i])
        if ans < m:
            ans = m
    return ans


shape = list(map(int, input('').split(' ')))
num_table = []

for _ in range(shape[0]):
    num_table.append(list(map(int, input('').split(' '))))

print(card_game(num_table, shape[0]))
