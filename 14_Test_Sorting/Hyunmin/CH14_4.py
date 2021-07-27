import heapq

N = int(input())
cards = []
for _ in range(N):
    cards.append(int(input()))

if N == 1:  # ex) N==1 cards = [1]일때 비교 횟수는 0임.
    print(0)
elif N == 2:
    print(cards[0] + cards[1])
else:
    result = 0
    heapq.heapify(cards)
    for _ in range(N - 1):  # 연산 횟수는 총 N-1
        a, b = heapq.heappop(cards), heapq.heappop(cards)
        tot = a + b
        result += tot
        heapq.heappush(cards, tot)
    print(result)

