def partition(list, start, end):
    pivot = list[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and list[left] <= pivot:
            left += 1
        while left <= right and list[right] > pivot:
            right -= 1
        if right < left:
            done = True
        else:
            list[left], list[right] = list[right], list[left]
    list[start], list[right] = list[right], list[start]
    return right
def kth(a, k):
    stack=[[0,len(a)-1]]
    l=a
    while stack:
        left,right=stack.pop()
        pivot = partition(l,left,right)
        if(pivot+1==k):
            return a[pivot]
        elif(pivot+1<k):
            stack.append([pivot+1,right])
        else:
            stack.append([left,pivot-1])

import random
sample=[3,5,4,2,3,7,2,8]
print(kth(sample,6))
print(sorted(sample))
for j in range(500):
    sample = []
    for i in range(50000):
        sample.append(random.randint(0,300000))
    print(kth(sample,48000))
    sample.sort()
    print(sample[48000-1])
