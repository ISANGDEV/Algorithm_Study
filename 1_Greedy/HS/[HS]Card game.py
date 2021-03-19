"""숫자 카드 게임은 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임이다.
단, 게임의 룰을 지키며 카드를 뽑아야 하고 룰은 다음과 같다.
숫자가 쓰인 카드들이 N X M 형태로 놓여 있다. 이 때 N은 행의 개수를 의미하며, M은 열의 개수를 의미한다.
먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
그다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
따라서 처음에 카드를 골라낼 행을 선택할 때,
이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여
최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.
카드들이 N X M 형태로 놓여 있을 때, 게임의 룰에 맞게 카드를 뽑는 프로그램을 만드시오.

입력 조건	 - 첫째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의 개수 M이 공백을 기준으로 하여 각각 자연수로 주어진다. (1 ≤ N, M ≤ 100)
 - 둘째 줄에 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1 이상 10,000 이하의 자연수이다.
출력 조건	 첫째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력한다. """

# 각 행의 숫자들 중에서, 가장 작은 수를 골라내어서 리스트에 담고 정렬해서 가장 큰 수가 무엇인지 고르면 해결. N,M이 행렬이라고 했으니 2차 배열 사용하기

minnum = [] # 최종적으로 가장 높은 숫자 고르기 위한 배열

print("행과 열을 공백을 기준으로 입력하세요")
n, m = map(int,input("행과 열이 될 숫자 2개를 입력").split())
card = [0 for i in range(n)]

print("각 카드에 적힐 숫자를 입력하세요")
for i in range(n): # n -1 ?? -> 필요 없음
    #num = list(map(int,input("숫자 입력").split())) 처음에 이렇게 하고, card 배열에 집어 넣으려고 했는데, 굳이 그럴필요가?? 바로 card에 넣으면 되지
    card[i]=list(map(int, input().split())) # 1차원 배열 선언하고, 원소에 배열 집어 넣어도 2차원 배열 완성.
    #card[i] = num // c에서는 이거 된 거같은데 파이썬은 안되네 ?

for i in range(n):
    card[i].sort() # card에 있는 각 행의 숫자들을 정렬 하고
    minnum.append(card[i][0]) # 그 정렬된 숫자들 중에서 가장 작은 값 추가하가
    #minnum[i] = card[i][0] 이거 왜 안댐? 찾아봐야겠따
minnum.sort() # 그거 정렬하고 가장 큰거
print(minnum[n-1]) # 출력
