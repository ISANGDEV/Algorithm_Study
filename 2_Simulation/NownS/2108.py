import sys

n = int(input())

nums = []
numdict = {}
for i in range(n):
    nums.append(int(sys.stdin.readline()))
    try:
        numdict[nums[i]] += 1
    except KeyError:
        numdict[nums[i]] = 1

print(int(round(sum(nums) / len(nums), 0)))

nums.sort()
print(nums[len(nums)//2])

items = list(numdict.items())
max_val = numdict[max(items, key=lambda x:x[1])[0]]
modes = []
for i in numdict.keys():
    if numdict[i] == max_val:
        modes.append(i)
modes.sort()
print(modes[0] if len(modes) == 1 else modes[1])


print(nums[-1] - nums[0])