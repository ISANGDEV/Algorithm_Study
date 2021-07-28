n = int(input())
homes = list(map(int, input().split()))

homes.sort()
answer = homes[len(homes) // 2 - 1]

print(answer)