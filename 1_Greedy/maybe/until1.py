def until1(n, k):
    cnt = 0
    while n > 1:
        if n % k == 0:
            n /= k
        else:
            n -= 1
        cnt += 1
    return cnt


factors = list(map(int, input('').split(' ')))
print(until1(factors[0], factors[1]))

