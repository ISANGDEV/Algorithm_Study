numOfGuitar = int(input())
sNums = []
sNums_sum = {}

for i in range(numOfGuitar):
    serialNum = input()
    sNums.append(serialNum)
    total = 0
    for j in serialNum:
        if j.isdigit():
            total += int(j)
    sNums_sum[serialNum] = total

sNums = sorted(sNums, key=lambda x: sNums_sum[x])
for i in set(sNums_sum.values()):
    keys = list(filter(lambda x: sNums_sum[x] == i, sNums_sum))
    if len(keys) > 1:
        idx = []
        for j in keys:
            idx.append(sNums.index(j))
        tmp = sNums[min(idx):max(idx)+1]
        tmp.sort()
        sNums[min(idx):max(idx) + 1] = tmp

sNums = sorted(sNums, key=lambda x: len(x))

print(sNums)
