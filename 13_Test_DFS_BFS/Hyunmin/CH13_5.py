import itertools

def calculate(operation, last, now):
    if operation == 0:
        return last + now
    elif operation == 1:
        return last - now
    elif operation == 2:
        return last * now
    elif operation == 3:
        if (last > 0 and now > 0) or (last < 0 and now < 0):
            return last // now
        elif last < 0:
            return -((last * -1) // now)
        else:
            return -(last // (now * -1))


n = int(input())
data = list(map(int, input().rstrip().split()))
op = list(map(int, input().rstrip().split()))

table = []
for i in range(len(op)):
    if op[i] != 0:
        for j in range(op[i]):
            table.append(i)
# (3 2 1 0 0) (3 2 1 0 0) 같이 순서가 중복되면 안됨. 그냥 순열 구할 시 중복 여러개. -> set
result = list(set(itertools.permutations(table, n - 1)))

total_small = 1000000001
total_big = -1000000001
# count = 0
for operations in result:
    # count += 1
    # print(count)
    prev = data[0]
    for i in range(n - 1):  # 1 2 3 4 5 (6)
        # 연산자는 n-1개 i와 같음
        prev = calculate(operations[i], prev, data[i + 1])
    # prev == total 값임
    if prev < total_small:
        total_small = prev
    if prev > total_big:
        total_big = prev
print(total_big)
print(total_small)

