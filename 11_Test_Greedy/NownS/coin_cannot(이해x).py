n = int(input())
coin = list(map(int,input().split()))

coin.sort(reverse=True)

value = 1
for i in coin:
    if value < i:
        break
    value += i

print(value)

#?? 이해가 잘 안감(책 답안 확인했는데, 이해가 안가요...)