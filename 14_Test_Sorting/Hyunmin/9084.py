T = int(input())
for _ in range(T):
    N = int(input())
    COINS = list(map(int, input().split()))
    M = int(input())
    coin_count = [0] * (M + 1)
    coin_count[0] = 1
    for coin in COINS:
        for i in range(1, M + 1):
            if i - coin >= 0:
                coin_count[i] += coin_count[i - coin]
    print(coin_count[M])

